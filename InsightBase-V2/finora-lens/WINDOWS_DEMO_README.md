# InsightBase — Windows / CMD başlangıç rehberi

Excel’deki tüm veriler sentetiktir. Gerçek banka/sektör verisi içermez.

## Paketin içeriği

- InsightBase.html: Uygulama.
- InsightBase.css: Tasarım.
- InsightBase.js: Excel okuyucu, hesaplamalar, grafikler ve dışa aktarma.
- dataa.xlsx: Sentetik demo veri; BS haftalık, P&L aylık; hacimler milyon TL.
- Baslat.cmd: CMD ile Edge’i uygun yerel dosya erişimi ayarlarıyla açar. PowerShell gerektirmez.
- BASLANGIC.md: Bu rehber.

Üç uygulama dosyası korunur. Excel demo verisini sağlar; CMD dosyası komut yazmadan çalıştırmayı kolaylaştırır; rehber kullanım adımlarını açıklar.

## Çalıştırma

1. ZIP’e sağ tıkla, **Tümünü ayıkla** seç. Altı dosya aynı klasörde kalsın.
2. **Baslat.cmd** dosyasına çift tıkla. Microsoft Edge açılır ve yanındaki dataa.xlsx otomatik okunur.
3. CMD penceresini kapatabilirsin. İnternet, PowerShell, Python, Node.js veya yönetici yetkisi gerekmez.

CMD çalıştırma dosyası kullanmak istemezsen InsightBase.html’i aç; sayfadaki başlatma komutunu kopyala. Klasörün adres çubuğuna **cmd** yazıp Enter’a bas; komutu yapıştırıp Enter’a bas.

Edge ayrı bir **InsightBase-Local** profiliyle açılır. `--allow-file-access-from-files` yalnızca bu profilin yerel HTML’den Excel okumasını sağlar; normal Edge profilini değiştirmez. Bu pencereyi yalnızca InsightBase için kullan. Kurum tarayıcı politikası bu ayarı engellerse kurum BT ekibinin onayladığı çalıştırma yöntemi gerekir.

## Kullanım

Kalem kartları detaylara açılır. Sunum oluştur alanında kalem, grafik, nominal/MoM/YoY/YTD ve tarih aralığı seçilebilir. PowerPoint çıktıları düzenlenebilir; PDF sabit görünümdür. İndirilen adlar tarih, saat ve saniye içerir. Demo veri kullanıldığında ekran ve sunumlar DEMO olarak işaretlenir.

## Gerçek veriye geçiş

Kendi şablonla uyumlu Excel’ini **dataa.xlsx** adıyla demo dosyasının yerine koy. Gerçek dosyada `INSIGHTBASE_DEMO` adlı sheet bulunmamalı. Excel’i hesaplatıp kaydet, uygulamada **Veriyi yenile** düğmesine bas. Veri yükleme ekranı yoktur.

## Sorun giderme

Dosyaları ZIP’in içinden çalıştırma. Microsoft Edge’in kurulu ve güncel olması gerekir. Eski sürüm görünüyorsa Ctrl+F5 yap. Excel bulunamazsa dosya adı ve klasörünü kontrol et. Kurum bir çalıştırma veya tarayıcı ayarını engelliyorsa güvenlik politikasını değiştirme; BT ekibinin onaylı yolunu kullan.

## Mail

InsightBase-Windows-Demo.zip dosyasını ek olarak gönder. Kurumsal mail sistemi JS/CMD içeren ZIP’i engellerse kurumun onaylı dosya paylaşım yolunu kullan.
