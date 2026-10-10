from pathlib import Path
import shutil, zipfile
root = Path(__file__).parent
out = root.parent / 'Sektovista'
shutil.copy2(root / 'local_server.py', out / 'local_server.py')
# Invoke normal PowerShell commands directly: no policy overrides or install steps.
ps = r'''
$ErrorActionPreference='Stop';
$root=(Get-Location).Path;
$allowed=@('index.html','styles.css','app.js','structure.js','engine.js','xlsx.js','dataa.xlsx');
$types=@{'.html'='text/html; charset=utf-8';'.css'='text/css; charset=utf-8';'.js'='text/javascript; charset=utf-8';'.xlsx'='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'};
$listener=[Net.Sockets.TcpListener]::new([Net.IPAddress]::Loopback,8765);
try{$listener.Start()}catch{$listener=[Net.Sockets.TcpListener]::new([Net.IPAddress]::Loopback,0);$listener.Start()};
$port=$listener.LocalEndpoint.Port;
$url='http://127.0.0.1:'+ $port +'/';
Write-Host ('Sektovista: '+$url);Write-Host 'Keep this window open. Save dataa.xlsx and refresh the dashboard.';
Start-Process $url;
try{while($true){
$client=$listener.AcceptTcpClient();$client.ReceiveTimeout=10000;$client.SendTimeout=10000;
try{
$stream=$client.GetStream();$reader=[IO.StreamReader]::new($stream,[Text.Encoding]::ASCII,$false,1024,$true);
$request=$reader.ReadLine();if(!$request){continue};
$headers=0;while(($line=$reader.ReadLine()) -ne ''){if($null -eq $line){break};$headers++;if($headers -gt 100){throw 'Too many headers'}};
$parts=$request.Split(' ');$method=$parts[0];
$path=[Uri]::UnescapeDataString(($parts[1].Split('?')[0]));
$name=if($path -eq '/'){'index.html'}else{$path.Substring(1)};
$file=Join-Path $root $name;
$status='200 OK';$type='text/plain; charset=utf-8';$body=[byte[]]@();
if($method -ne 'GET' -and $method -ne 'HEAD'){$status='405 Method Not Allowed'}
elseif($allowed -notcontains $name -or $path -ne ('/'+$name) -and $path -ne '/'){$status='404 Not Found'}
elseif(!(Test-Path -LiteralPath $file -PathType Leaf)){$status='404 Not Found'}
else{$body=[IO.File]::ReadAllBytes($file);$type=$types[[IO.Path]::GetExtension($file)]};
$nl=[string][char]13+[char]10;
$header='HTTP/1.1 '+$status+$nl+'Content-Type: '+$type+$nl+'Content-Length: '+$body.Length+$nl+'Cache-Control: no-store'+$nl+'X-Content-Type-Options: nosniff'+$nl+'Cross-Origin-Resource-Policy: same-origin'+$nl+'Connection: close'+$nl+$nl;
$bytes=[Text.Encoding]::ASCII.GetBytes($header);$stream.Write($bytes,0,$bytes.Length);
if($method -ne 'HEAD' -and $body.Length -gt 0){$stream.Write($body,0,$body.Length)};
$stream.Flush();$reader.Dispose();
}catch{Write-Host ('Request could not be served: '+$_.Exception.Message)}finally{$client.Close()}
}}finally{$listener.Stop()}
'''
ps = ' '.join(line.strip() for line in ps.strip().splitlines())
# Escape double quotes for the cmd-to-PowerShell boundary.
ps = ps.replace('"', '\\"')
bat = '@echo off\r\ncd /d "%~dp0"\r\npowershell.exe -NoProfile -Command "' + ps + '"\r\nif errorlevel 1 pause\r\n'
(out / 'Baslat.bat').write_bytes(bat.encode('ascii'))
(out / 'Baslat.command').write_text('#!/bin/sh\ncd "$(dirname "$0")" || exit 1\nexec python3 local_server.py\n')
(out / 'Baslat.command').chmod(0o755)
(out / 'KULLANIM.txt').write_text('''SEKTOVISTA — AYNI KLASÖRDEN OTOMATİK EXCEL OKUMA

1. Bu klasörün tamamını iş bilgisayarına kopyala.
2. Veri Excel’ini dataa.xlsx adıyla index.html, styles.css ve JS dosyalarının yanına koy.
3. Windows: Baslat.bat dosyasına çift tıkla. Standart Windows PowerShell kullanılır; Python kurulumu gerekmez.
   Mac: Baslat.command dosyasını çalıştır. Python 3 gerekir.
   Alternatif: Bu klasörde python3 local_server.py çalıştır.
4. Tarayıcı otomatik açılır ve aynı klasördeki dataa.xlsx okunur. Başlatıcı penceresi açık kalmalı.
5. Excel’i güncelledikten sonra hesaplatıp kaydet; dashboard’u yenile.
6. BS kaynak birimini (bin/milyon/milyar TL) doğrula.

Paketteki dataa.xlsx, paylaşılan BOŞ ŞABLON kopyasıdır; gerçek veri içermez.
Ana dosyanı bu dosyanın yerine koy. Satır başlıkları ve konumlar şablonla aynı olmalıdır.
Excel’in kendi içinde dış veri bağlantıları varsa, bunları Excel’de güncelleyip kaydetmen gerekir.
Dashboard kaydedilmiş değerleri okur; Excel formüllerini veya dış bağlantılarını çalıştırmaz.

HTML’e doğrudan çift tıklamak yerine başlatıcıyı kullan. Tarayıcıların file:// güvenlik sınırı,
yanındaki Excel’in izinsiz okunmasını engeller. Başlatıcı yalnızca 127.0.0.1 adresinde çalışır;
internet bağlantısı ve harici sunucu gerekmez. Dosya seçme / yükleme ekranı bulunmaz.
Veri bulunamazsa veya boşsa demo üretilmez; açıklama ve “—” gösterilir.

Kurumun PowerShell veya yerel sunucu çalıştırmayı engelliyorsa kurum politikasına göre izin gerekir.
Windows başlatıcısı bu geliştirme ortamında çalıştırılamadı; Python yolu macOS’ta test edildi.
''', encoding='utf-8')
# Keep the old single-file delivery synchronized; direct file opening shows launcher guidance.
html=(out/'index.html').read_text()
html=html.replace('<link rel="stylesheet" href="styles.css">','<style>'+(out/'styles.css').read_text()+'</style>')
for f in ['structure.js','engine.js','xlsx.js','app.js']:
    html=html.replace('<script src="'+f+'"></script>','<script>'+(out/f).read_text()+'</script>')
(root.parent/'Sektovista.html').write_text(html)
with zipfile.ZipFile(root.parent/'Sektovista.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(out.iterdir()):
        if p.is_file():
            info=zipfile.ZipInfo.from_file(p,arcname='Sektovista/'+p.name)
            info.compress_type=zipfile.ZIP_DEFLATED
            z.writestr(info,p.read_bytes())
print('Local package: '+str(root.parent/'Sektovista.zip'))
