"""The Windows deliverable contains exactly HTML, CSS, and JS."""
from pathlib import Path
import ast, json, zipfile

root=Path(__file__).parent
source=root/'dist'
out=root.parent/'InsightBase-Windows'
out.mkdir(exist_ok=True)

# Reuse the loopback server as a normal PowerShell command, not a fourth file.
tree=ast.parse((root/'package_local.py').read_text())
ps=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='ps' for t in n.targets) and isinstance(n.value,ast.Constant))
ps=ps.replace("'index.html','styles.css','app.js','structure.js','engine.js','xlsx.js','dataa.xlsx'", "'InsightBase.html','InsightBase.css','InsightBase.js','dataa.xlsx'")
ps=ps.replace("{'index.html'}", "{'InsightBase.html'}").replace('Sektovista','InsightBase')
ps=' '.join(line.strip() for line in ps.strip().splitlines())

html=(source/'index.html').read_text()
html=html.replace('Sektovista','InsightBase').replace('<span>sekto<span class="lens">vista</span></span>','<span>Insight<span class="lens">Base</span></span>').replace('brandmark">S','brandmark">I').replace('M24 8H8v8h16v8H8','M11 8h10M16 8v16M11 24h10')
html=html.replace('href="styles.css"','href="InsightBase.css"')
html=html.replace('<script src="structure.js"></script><script src="engine.js"></script><script src="xlsx.js"></script><script src="highlights.js"></script><script src="../vendor/pptxgen.bundle.js"></script><script>window.pptxgen=PptxGenJS;</script><script src="../vendor/jspdf.umd.min.js"></script><script src="presentation.js"></script><script src="app.js"></script>','<script src="InsightBase.js"></script>')
help_html='''<section id="windowsStart" class="panel windows-start" hidden>
<div class="panel-head"><h3>Windows’ta ilk açılış</h3><span class="pill">Üç dosya · Kurulum gerektirmez</span></div>
<p>HTML, CSS, JS ve kendi <strong>dataa.xlsx</strong> dosyan aynı klasörde olsun. Tarayıcı, çift tıklayarak açılan HTML’in yanındaki Excel’i otomatik okuyamaz.</p>
<ol><li>Dosya Gezgini adres çubuğuna <strong>cmd</strong> yazıp Enter’a bas.</li><li>Aşağıdaki komutu CMD’ye yapıştırıp Enter’a bas. Dashboard tarayıcıda otomatik açılır.</li></ol>
<button id="copyWindowsCommand" class="button primary">Başlatma komutunu kopyala</button>
<details><summary>Komutu göster</summary><textarea id="windowsCommand" readonly spellcheck="false" aria-label="Windows CMD başlatma komutu"></textarea></details>
<p id="commandFeedback" role="status"></p><p class="muted">Edge ayrı bir yerel profil ile açılır. CMD penceresini kapatabilirsin. Excel’i hesaplatıp kaydet, dashboard’u yenile. İnternet veya Python gerekmez. Bu profili yalnızca InsightBase için kullan. Kurumun tarayıcı politikaları geçerlidir.</p>
</section>'''
html=html.replace('<div class="notice" id="notice"',help_html+'<div class="notice" id="notice"')

app=(source/'app.js').read_text()
app=app.replace('Aynı klasördeki Excel’i otomatik okumak için Baslat.bat (Windows) veya Baslat.command (Mac) ile açın.', 'Windows başlatma komutunu bu klasördeki CMD’de çalıştırın. Açılan yerel dashboard, dataa.xlsx dosyasını otomatik okur.')
app=app.replace("['http:','https:']", "['http:','https:','file:']")
app=app.replace("loadState='ready';", "loadState='ready';document.querySelector('#windowsStart').hidden=true;")
app=app.replace('index.html','InsightBase.html').replace('Sektovista','InsightBase').replace('set_sektovista_view','set_insightbase_view')
setup='''
const commandBox=document.querySelector('#windowsCommand');
const windowsStart=document.querySelector('#windowsStart');
if(location.protocol==='file:'){
 windowsStart.hidden=false;
 // The command normally runs in the workbook folder. On Windows, bind it to this HTML's folder.
 const dir=decodeURIComponent(new URL('.',location.href).pathname);
 let windowsDir=/^\/[A-Za-z]:\//.test(dir)?dir.slice(1).replace(/\//g,'\\\\'):null;
 if(location.hostname)windowsDir='\\\\\\\\'+location.hostname+dir.replace(/\//g,'\\\\');
 commandBox.value='start "" msedge --allow-file-access-from-files --user-data-dir="%TEMP%/InsightBase-Local" "'+location.href+'"';
}
document.querySelector('#copyWindowsCommand').addEventListener('click',async()=>{
 try{
  if(navigator.clipboard?.writeText)await navigator.clipboard.writeText(commandBox.value);
  else{commandBox.closest('details').open=true;commandBox.select();if(!document.execCommand('copy'))throw Error('clipboard');}
  document.querySelector('#commandFeedback').textContent='Komut kopyalandı. Bu klasördeki CMD’ye yapıştırıp Enter’a bas.';
 }catch{
  commandBox.closest('details').open=true;commandBox.select();document.querySelector('#commandFeedback').textContent='Komutu seçtim; Ctrl+C ile kopyalayabilirsin.';
 }
});
'''
# Engine and XLSX reader are scoped IIFEs. Only one application entry point runs.
bundle='\n'.join((source/f).read_text() for f in ['structure.js','engine.js','xlsx.js','highlights.js'])
bundle+='\n'+(root/'vendor/pptxgen.bundle.js').read_text().split('//# sourceMappingURL=')[0]+'\nwindow.pptxgen=PptxGenJS;\n'+(root/'vendor/jspdf.umd.min.js').read_text().split('//# sourceMappingURL=')[0]+'\n'+(source/'presentation.js').read_text()
bundle+='\nconst WINDOWS_COMMAND='+json.dumps(ps)+';\n'+setup+'\n'+app
css=(source/'styles.css').read_text()+'''\n.windows-start{margin-bottom:22px}.windows-start[hidden]{display:none}.windows-start p,.windows-start li{font-size:14px;line-height:1.7}.windows-start li{margin-bottom:10px}.windows-start details{margin-top:14px}.windows-start summary{cursor:pointer;font-size:14px;color:var(--blue)}.windows-start textarea{width:100%;min-height:140px;margin-top:12px;font:12px/1.6 Consolas,monospace;border:1px solid var(--line);border-radius:6px;padding:12px;resize:vertical}\n'''
(out/'InsightBase.html').write_text(html)
(out/'InsightBase.css').write_text(css.replace('font-size:25px;font-weight:750','font-size:22px;font-weight:750'))
(out/'InsightBase.js').write_text(bundle)
assert sorted(p.name for p in out.iterdir())==['InsightBase.css','InsightBase.html','InsightBase.js']
with zipfile.ZipFile(root.parent/'InsightBase-Windows.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(out.iterdir()):z.write(p,arcname=p.name)
print('Exactly three files packaged.')
