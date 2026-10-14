"""Synthetic finance demo for this computer's preview only. No real files changed."""
from pathlib import Path
from datetime import date, timedelta
import calendar, json, math, shutil, sys

root=Path(__file__).parent
template=json.loads((root/'dist/structure.json').read_text())
preview=Path('/private/tmp/insightbase-v2-preview')
preview.mkdir(exist_ok=True)
live_file=root.parent/'local-data/dataa.xlsx'
live=live_file.exists() and '--demo' not in sys.argv
if '--source' in sys.argv or live:
    source=root/'dist'
    html=(source/'index.html').read_text().replace('href="styles.css"','href="InsightBase.css"')
    start=html.index('<script src="structure.js">');html=html[:start]+'<script src="InsightBase.js"></script></body></html>'
    html=html.replace('Sektovista','InsightBase')
    bundle='\n'.join((source/f).read_text() for f in ['structure.js','engine.js','xlsx.js','highlights.js'])
    bundle+='\n'+(root/'vendor/pptxgen.bundle.js').read_text().split('//# sourceMappingURL=')[0]+'\nwindow.pptxgen=PptxGenJS;\n'+(root/'vendor/jspdf.umd.min.js').read_text().split('//# sourceMappingURL=')[0]+'\n'+(source/'presentation.js').read_text()+'\n'+(source/'app.js').read_text()
    (preview/'InsightBase.html').write_text(html)
    (preview/'InsightBase.css').write_text((source/'styles.css').read_text())
    (preview/'InsightBase.js').write_text(bundle)
else:
    for p in (root.parent/'InsightBase-Windows').iterdir():
        if p.is_file():shutil.copy2(p,preview/p.name)

if live:
    shutil.copy2(live_file,preview/'dataa.xlsx')
    (preview/'demo-data.json').unlink(missing_ok=True)
    print('Local preview ready: real adjacent workbook; no synthetic data.')
    sys.exit(0)

dates=[]
d=date(2024,12,27)
while d<=date(2026,10,2):
    dates.append(d.isoformat());d+=timedelta(days=7)
monthly=[date(y,m,calendar.monthrange(y,m)[1]).isoformat() for y in (2024,2025,2026) for m in range(1,13) if date(2024,12,1)<=date(y,m,1)<=date(2026,9,1)]

def balance(group,i):
    w=.58 if group=='Ozel' else .42
    g=.0053 if group=='Ozel' else .0046
    loans=15800000*w*(1+g)**i*(1+.003*math.sin(i*.48))
    deposits=19800000*w*(1+g+.0006)**i*(1+.006*math.sin(i*.36+(0 if group=='Ozel' else 1)))
    retail=loans*.21*(1+.02*math.sin(i*.17))
    cards=loans*.18*(1+.06*math.sin(i*.23))
    commercial=loans-retail-cards
    tl_share=.72+.015*math.sin(i*.1)
    npl=.023+.005*i/len(dates)+(.003 if group=='Kamu' else 0)
    tl_dep=.64+.025*math.sin(i*.12)
    term=.77-.025*math.sin(i*.08)
    td=deposits*term;dd=deposits-td
    c_tl=commercial*.69
    return {3:loans,4:loans*tl_share,5:loans*tl_share*npl,6:loans*(1-tl_share),7:loans*(1-tl_share)*npl,
      8:loans*.16,9:loans*.11,10:loans*.05,12:retail,13:retail,14:retail*npl,15:retail*.52,16:retail*.52*npl,
      17:retail*.29,18:retail*.05,19:retail*.14,21:commercial,22:commercial*npl,23:c_tl,24:c_tl*npl,
      25:commercial-c_tl,26:(commercial-c_tl)*npl,27:loans*.12,28:commercial*.47,29:commercial*.47*npl,
      31:cards,32:cards*.73,33:cards*.73*npl*1.3,34:cards*.27,35:cards*.27*npl,
      37:deposits,38:deposits*tl_dep,39:deposits*(1-tl_dep),41:td,42:td*tl_dep,43:td*(1-tl_dep),
      44:td*tl_dep*.53,45:td*tl_dep*.47,46:td*(1-tl_dep)*.58,47:td*(1-tl_dep)*.42,
      49:dd,50:dd*tl_dep,51:dd*(1-tl_dep),52:dd*tl_dep*.56,53:dd*tl_dep*.44,54:dd*(1-tl_dep)*.61,55:dd*(1-tl_dep)*.39,
      57:loans/deposits*100}

def flows(group,y,m):
    w=.58 if group=='Ozel' else .42
    factor=1+.27*(y-2025)
    phase=0 if group=='Ozel' else .8
    nii=122000*w*factor*(1+.018*(m-1))*(1+.08*math.sin(m*.58+phase))
    # A September scenario gives the dashboard different movements to investigate.
    if y==2026 and m==9:nii*=1.08 if group=='Ozel' else 1.04
    fee=54000*w*factor*(1+.022*(m-1))*(1+.045*math.cos(m*.67))
    trading=13000*w*factor*(1+.28*math.sin(m*.9+phase))
    other=20000*w*factor*(1+.012*(m-1))
    expense=76000*w*factor*(1+.013*(m-1))*(1+.035*math.sin(m*.7))
    ecl=23000*w*factor*(1+.015*(m-1))*(1+.2*math.sin(m*.5+phase))
    if y==2026 and m==9:ecl*=1.23 if group=='Kamu' else 1.12
    prov=7000*w*factor
    income=nii+fee+trading+other;pre=income-expense;pbt=pre-ecl-prov;tax=pbt*.25;profit=pbt-tax
    assets=26000000*w*factor*(1+.01*(m-1));equity=assets*.11
    return {49:nii,50:nii*3.35,51:nii*2.35,52:fee+trading+other,53:fee,54:trading,55:other,56:income,
      57:expense,58:expense*.57,59:expense*.43,60:pre,61:ecl,62:prov,63:pbt,64:tax,65:profit,
      67:profit*12/assets*100,68:profit*12/equity*100,69:expense/income*100,70:nii*12/assets*100,
      72:income,73:nii,74:fee,75:0,76:trading,77:other,78:ecl+prov,79:expense,80:tax,81:profit,83:fee/expense*100}

ratio_rows={29,30,31,32,45,67,68,69,70,83}
bs_values={g:[balance(g,i) for i in range(len(dates))] for g in ['Ozel','Kamu']}
bs_values['Sektör']=[{r:a[r]+b[r] for r in a if r!=57} for a,b in zip(bs_values['Ozel'],bs_values['Kamu'])]
for v in bs_values['Sektör']:v[57]=v[3]/v[37]*100

# Updated schema stores FX stocks in million USD and NPL rows as percentages.
for group,observations in bs_values.items():
    for v in observations:
        v.update({104:(v[5]+v[7])/v[3]*100,114:v[18]*.028/v[18]*100,116:2.7,153:v[4]/v[38]*100,154:v[6]/v[39]*100,155:2.6,156:2.9})
        for r,base in [(14,13),(29,28),(33,32),(35,34)]:v[r]=v[r]/v[base]*100
        v[112]=v[14]
        for r in [6,10,25,39,43,46,47,51,54,55]:v[r]/=40

def month_values(group,d):
    y,m=map(int,d[:7].split('-'))
    parts=[flows(g,y,m) for g in ['Ozel','Kamu']] if group=='Sektör' else [flows(group,y,m)]
    result={r:sum(p[r] for p in parts) for r in parts[0]}
    w=1 if group=='Sektör' else (.58 if group=='Ozel' else .42)
    assets=26000000*w*(1+.27*(y-2025))*(1+.01*(m-1));equity=assets*.11
    result.update({67:result[65]*12/assets*100,68:result[65]*12/equity*100,69:result[57]/result[56]*100,70:result[49]*12/assets*100,83:result[53]/result[57]*100})
    cumulative={}
    for k in range(1,m+1):
        fp=[flows(g,y,k) for g in ['Ozel','Kamu']] if group=='Sektör' else [flows(group,y,k)]
        for r in result:
            if r not in ratio_rows:cumulative[r-38]=cumulative.get(r-38,0)+sum(p[r] for p in fp)
    cumulative.update({29:cumulative[27]*12/m/assets*100,30:cumulative[27]*12/m/equity*100,
      31:cumulative[19]/cumulative[18]*100,32:cumulative[11]*12/m/assets*100,45:cumulative[15]/cumulative[19]*100})
    return {**result,**cumulative,4:round(11500*w),5:round(211000*w),6:6800000*w,7:710000*w}

sheets=[]
for g in ['Sektör','Ozel','Kamu']:
    for kind,periods,values in [('BS',dates,bs_values[g]),('PL',monthly,[month_values(g,d) for d in monthly])]:
        sheets.append({'type':kind,'group':g,'name':('BS' if kind=='BS' else 'P&L')+'_'+g,
          'dates':periods,'rows':[{**r,'values':[round(v[r['row']],3) for v in values]} for r in template[kind]['rows']]})

# Independent checks: totals and annual resets, including the highlighted September scenario.
for g in ['Sektör','Ozel','Kamu']:
    for v in bs_values[g]:
        assert abs(v[3]-v[4]-v[6]*40)<.01
        assert abs(v[37]-v[38]-v[39]*40)<.01
        assert abs(v[37]-v[41]-v[49])<.01
    for y in [2025,2026]:
        jan=month_values(g,f'{y}-01-31');assert abs(jan[27]-jan[65])<.01
    sep=month_values(g,'2026-09-30')
    assert abs(sep[65]-(sep[56]-sep[57]-sep[61]-sep[62]-sep[64]))<.01
    assert abs(sep[27]-sum(flows(g,2026,m)[65] for m in range(1,10)))<.01 if g!='Sektör' else True

data={'sheets':sheets,'warnings':[],'demo':True}
(preview/'demo-data.json').write_text(json.dumps(data,ensure_ascii=False))
js=(preview/'InsightBase.js').read_text()
js=js.replace("fetch('./dataa.xlsx'", "fetch('./demo-data.json'")
js=js.replace("const file=await response.blob();\n  const loaded=await LocalXLSX.read(file,T);", "const loaded=await response.json();")
js=js.replace('dataset={...loaded,demo:false,','dataset={...loaded,demo:true,')
js=js.replace("?'VERİ YOK':'YEREL EXCEL'", "?'VERİ YOK':'DEMO VERİ'")
js=js.replace('dataa.xlsx · Aynı klasörden otomatik okundu. Excel’i kaydettikten sonra bu sayfayı yenileyin. BS kaynak birimini doğrulayın.',
 'DEMO · Tüm rakamlar sentetiktir; gerçek sektör verisi değildir. BS: 2 Ekim 2026 · P&L: Eylül 2026 · Birim: milyon TL.')
js=js.replace('Şablon yapısı ile uyumlu · Veriler yalnızca bu sekmede','Sentetik örnek senaryo · Gerçek veri içermez')
(preview/'InsightBase.js').write_text(js)
print(f'Demo ready: {len(sheets)} sheets; {len(dates)} weekly and {len(monthly)} monthly periods.')
