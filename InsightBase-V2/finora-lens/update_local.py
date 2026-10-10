from pathlib import Path
import shutil, zipfile

root = Path(__file__).parent
dist = root / 'dist'
p = dist / 'index.html'
s = p.read_text()
s = s.replace('<span id="mode" class="badge">DEMO VERİ</span><button class="button primary" id="importTop">Excel aç</button>', '<span id="mode" class="badge">VERİ OKUNUYOR</span>')
s = s.replace('value="2026-09-25" max="2026-10-05"', 'value=""')
s = s.replace('Örnek senaryo · Tüm rakamlar sentetiktir. Gerçek sektör verisi veya yatırım yorumu değildir.', 'dataa.xlsx okunuyor…')
start = s.find('<dialog id="importDialog">')
if start >= 0:
    end = s.index('</dialog>', start) + len('</dialog>')
    s = s[:start] + s[end:]
p.write_text(s)

p = dist / 'app.js'
s = p.read_text()
s = s.replace(",pending=null;", ";")
start, end = s.index('function demo(){'), s.index('const sheet=')
s = s[:start] + "let dataset={sheets:[],warnings:[],demo:false},loadState='loading',loadError='',loadToken=0;\n" + s[end:]
s = s.replace('<button class="button primary" id="importData">Excel aç</button>', '<span class="pill">dataa.xlsx</span>')
s = s.replace('<button class="button" id="resetDemo">Demo veriye dön</button>', '')
s = s.replace('Dosya okuma tamamen yereldir; hiçbir veri isteği, sunucu kaydı veya tarayıcı depolaması yapılmaz.', 'Aynı klasördeki dataa.xlsx, yalnızca bilgisayarındaki yerel sunucudan okunur. Dış servise gönderilmez, sunucuda veya tarayıcı depolamasında kaydedilmez.')
s = s.replace('Excel’i hesaplayıp kaydederek yeniden açın.', 'Excel’i hesaplayıp kaydedin, ardından dashboard sayfasını yenileyin.')
s = s.replace('İçe aktarma kontrolü', 'Otomatik okuma kontrolü').replace('İçe aktarma uyarısı yok.', 'Dosya okuma uyarısı yok.')
old = " $('#mode').textContent=dataset.demo?'DEMO VERİ':'YEREL EXCEL';$('#bsUnitWrap').hidden=dataset.demo;$('#notice').textContent=dataset.demo?'Örnek senaryo · Tüm rakamlar sentetiktir. Gerçek sektör verisi veya yatırım yorumu değildir.':'Yerel Excel · Dosya bu sekmede işleniyor. Veriler sunucuya gönderilmez. Kaynak dönemlerini ve BS birimini kontrol edin.';"
new = " $('#mode').textContent=loadState==='loading'?'VERİ OKUNUYOR':loadState==='error'?'VERİ YOK':'YEREL EXCEL';$('#bsUnitWrap').hidden=false;$('#notice').classList.toggle('error',loadState==='error');$('#notice').textContent=loadState==='loading'?'dataa.xlsx okunuyor…':loadState==='error'?loadError:'dataa.xlsx · Aynı klasörden otomatik okundu. Excel’i kaydettikten sonra bu sayfayı yenileyin. BS kaynak birimini doğrulayın.';"
if old not in s:
    raise RuntimeError('Status replacement failed')
s = s.replace(old, new)
start = s.index("if(['importTop','importData']")
end = s.index('\n});', start)
s = s[:start] + "if(b.id==='closeDetail')$('#detail').close();" + s[end:]
start = s.index("$('#file').addEventListener")
end = s.index('\nif(document.modelContext', start)
s = s[:start] + '''
async function loadWorkbook(){
 const token=++loadToken;
 loadState='loading';loadError='';dataset={sheets:[],warnings:[],demo:false};render();
 try{
  if(!['http:','https:'].includes(location.protocol))throw Error('Aynı klasördeki Excel’i otomatik okumak için Baslat.bat (Windows) veya Baslat.command (Mac) ile açın.');
  const controller=new AbortController(),timer=setTimeout(()=>controller.abort(),20000);
  let response;
  try{response=await fetch('./dataa.xlsx',{cache:'no-store',signal:controller.signal});}finally{clearTimeout(timer);}
  if(!response.ok)throw Error(response.status===404?'dataa.xlsx bulunamadı. Veri Excel’ini index.html ile aynı klasöre dataa.xlsx adıyla koyup sayfayı yenileyin.':'dataa.xlsx okunamadı (HTTP '+response.status+').');
  const size=Number(response.headers.get('Content-Length'));
  if(size>20*1024*1024)throw Error('dataa.xlsx 20 MB sınırını aşıyor.');
  const file=await response.blob();
  const loaded=await LocalXLSX.read(file,T);
  if(token!==loadToken)return;
  dataset={...loaded,demo:false};loadState='ready';
  // Ignore empty future headers; start at the latest populated observation.
  const dates=loaded.sheets.flatMap(s=>s.dates.filter((d,i)=>s.rows.some(r=>E.finite(r.values[i]))));
  const latest=dates.sort().at(-1);
  if(latest){state.date=latest;$('#asof').value=latest;}
  render();
  const count=loaded.sheets.reduce((n,s)=>n+s.rows.reduce((n,r)=>n+r.values.filter(E.finite).length,0),0);
  if(!count)$('#notice').textContent='dataa.xlsx okundu; sayısal veri bulunmuyor. Boş hücreler “—” gösterilir.';
 }catch(error){
  if(token!==loadToken)return;
  loadState='error';loadError=error.name==='AbortError'?'dataa.xlsx okuma süresi doldu. Dosyayı kontrol edip sayfayı yenileyin.':error.message;render();
 }
}
const today=new Date();state.date=[today.getFullYear(),String(today.getMonth()+1).padStart(2,'0'),String(today.getDate()).padStart(2,'0')].join('-');$('#asof').value=state.date;
loadWorkbook();
''' + s[end:]
p.write_text(s)

out = root.parent / 'Sektovista'
out.mkdir(exist_ok=True)
for filename in ['index.html','styles.css','structure.js','engine.js','xlsx.js','app.js']:
    shutil.copy2(dist / filename, out / filename)
# Supplied workbook is an empty template. Never overwrite a user's data workbook.
if not (out / 'dataa.xlsx').exists():
    shutil.copy2('/Users/ozgur/Downloads/şablon.xlsx', out / 'dataa.xlsx')
