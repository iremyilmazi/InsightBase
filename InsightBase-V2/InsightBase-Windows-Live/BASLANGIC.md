# InsightBase — Windows / GitHub Raw ile güncelleme

Bu klasördeki beş dosya GitHub üzerinden alınır. Altıncı dosya olan **dataa.xlsx**, senin bilgisayarında kalır; GitHub'a yüklenmez.

## Güncellenecek dosyalar

- BASLANGIC.md
- Baslat.cmd
- InsightBase.css
- InsightBase.html
- InsightBase.js

GitHub klasörü: https://github.com/iremyilmazi/InsightBase/tree/main/InsightBase-V2/InsightBase-Windows-Live

## Raw ile kopyalama

1. InsightBase için açılan Edge penceresini kapat. Mevcut beş dosyanın yedeğini ayrı bir klasöre al.
2. GitHub klasöründe dosyayı aç, **Raw** düğmesine bas. GitHub'a giriş yapman gerekebilir.
3. Raw sayfasındaki dosya içeriğinin tamamını **Ctrl+A → Ctrl+C** ile kopyala.
4. Bilgisayarındaki aynı adlı dosyayı Not Defteri ile aç; içeriğin tamamını seçip yenisiyle değiştir. **UTF-8** olarak kaydet.
5. Bu işlemi beş dosya için tamamla. Aynı güncellemede tüm dosyaları aynı GitHub sürümünden al. Sabit sürüm için GitHub'da ilgili commit'i açıp o sürümün Raw dosyalarını kullanabilirsin.
6. Dosya adlarını değiştirme. Windows'ta **Dosya adı uzantıları** görünür olsun; dosyanın sonuna yanlışlıkla `.txt` eklenmesin. Farklı Kaydet kullanırsan dosya türü **Tüm dosyalar** olsun.
7. **dataa.xlsx dosyanı değiştirme veya silme.** Uygulama dosyalarıyla aynı klasörde kalmalı.
8. **Baslat.cmd** dosyasına çift tıkla. Eski görünüm kalırsa **Ctrl+F5** yap.

Dosya yerine GitHub giriş ekranını veya HTML arayüzünü kopyalamadığından emin ol. Raw erişimi kurum politikasıyla engelleniyorsa kurumunun onaylı aktarım yolunu kullan.

## Çalıştırma

Microsoft Edge gerekir. PowerShell, Python, Node.js ve yönetici yetkisi gerekmez. Baslat.cmd Edge'i ayrı `%TEMP%\InsightBase-Local` profili ve yerel dosya okuma izniyle açar. Bu pencereyi yalnızca InsightBase için kullan. Normal Edge profilin değiştirilmez. Kurumun tarayıcı ve çalıştırma kuralları geçerlidir.

GitHub'a yalnızca dosya güncellerken erişim gerekir. Uygulama çalışırken Excel'i yerelden okur; veriyi dışarı göndermez. Excel'i hesaplatıp kaydettikten sonra **Veriyi yenile** düğmesine bas.

## Excel yapısı

Sheet adları: BS_Sektör, BS_Ozel, BS_Kamu, P&L_Sektör, P&L_Ozel, P&L_Kamu. A sütunu kalem, B Format; veriler C'den başlar. BS tarihleri 1. satır, P&L tarihleri 2. satırdır. Kalem sırası güncel şablonla uyumlu olmalıdır.

TL: milyon TL. USD: milyon USD. %: oran. FX tutarlar TL'ye çevrilmez. Formatı boş toplam hacim satırları TL kabul edilir. Sayı görünümü **123,323.21** biçiminde, en fazla iki ondalık basamaktır.

## Sorun giderme

- Dosyaların tamamı ve dataa.xlsx aynı klasörde olmalı.
- Baslat.cmd bulunamıyorsa dosya adının Baslat.cmd.txt olmadığını kontrol et.
- Boş veya bozuk ekran görürsen Raw içeriğinin tamamını kopyaladığını ve UTF-8 kaydettiğini kontrol et.
- Excel uyarılarında sheet/başlık/Format bilgisini güncel şablonla karşılaştır.
- Fiziksel Windows testi yapılmadı; paket, hesaplamalar ve yerel tarayıcı akışı doğrulandı.
