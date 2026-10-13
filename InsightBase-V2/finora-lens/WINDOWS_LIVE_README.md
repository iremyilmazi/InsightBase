# InsightBase — Windows canlı veri

Bu paket demo Excel içermez. Kendi güncel Excel’ini `dataa.xlsx` adıyla uygulama dosyalarıyla aynı klasöre koy.

## Hazırlık ve açılış

1. ZIP’i tamamen çıkar. TXT paketini kullanıyorsan Dosya Gezgini’nde Görünüm → Dosya adı uzantıları seçeneğini aç. `InsightBase.js.txt` adını `InsightBase.js`, `Baslat.cmd.txt` adını `Baslat.cmd` yap.
2. Kendi `dataa.xlsx` dosyanı aynı klasöre koy.
3. `Baslat.cmd` dosyasına çift tıkla. Microsoft Edge açılır. PowerShell ve kurulum gerekmez.
4. Excel’i güncellediğinde hesaplatıp kaydet; uygulamada Veriyi yenile’ye bas.

CMD dosyası Edge’i ayrı `%TEMP%\InsightBase-Local` profiliyle ve yerel dosya okuma izniyle açar. Bu profili yalnızca InsightBase için kullan. Kurumun tarayıcı/çalıştırma politikaları geçerlidir; engellenirse BT’nin onayladığı yöntem gerekir.

## Beklenen Excel

Sheet adları: BS_Sektör, BS_Ozel, BS_Kamu, P&L_Sektör, P&L_Ozel, P&L_Kamu. A sütunu kalem, B Format; veriler C’den başlar. BS tarihleri 1. satır, P&L tarihleri 2. satırdır. Yeni şablonun kalem sırası korunmalıdır. TL tutarlar milyon TL, USD tutarlar milyon USD, % kalemler orandır. FX değerleri TL’ye çevrilmez. Formatı boş toplam hacim satırları TL kabul edilir.

## Dosyalar

HTML, CSS, JS üç uygulama dosyasıdır. Baslat.cmd komut yazmadan açılış için, BASLANGIC.md kullanım rehberi için eklenmiştir. Pakette gerçek veya demo veri bulunmaz. Normal üç dosyalı ZIP de ayrıca mevcuttur. Sunum editörü düzenlenebilir PowerPoint ve PDF verir; dosya adları indirme tarih/saat/saniyesi içerir.

E-posta kabulü garanti değildir. Kurumun dosya taşıma ve çalıştırma kurallarına uygun kullan. Fiziksel Windows testi yapılmadı; Excel okuyucu ve tarayıcı demo akışı doğrulandı.
