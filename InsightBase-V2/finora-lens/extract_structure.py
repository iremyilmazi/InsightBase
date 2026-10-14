"""Extract labels, source positions, formats and date headers only; never values."""
import zipfile,xml.etree.ElementTree as ET,json,datetime,sys
from pathlib import Path
ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
root=Path(__file__).parent
BS={3:3,4:5,6:6,8:24,9:25,10:26,12:8,13:9,14:10,15:11,17:12,18:13,19:15,21:18,23:19,25:20,28:21,29:22,31:28,32:29,33:30,34:31,35:32,37:34,38:35,39:43,42:39,43:47,44:40,45:41,46:48,47:49,50:36,51:44,52:37,53:38,54:45,55:46,57:52,104:4,114:14,116:16,153:53,154:54,155:55,156:56}
# Current reference: şablon (2).xlsx; removed consumer-loan rows are not reused.
BS={ident:(src-1 if src>=10 else src) for ident,src in BS.items() if ident not in [13,14]}
BS[112]=9
with zipfile.ZipFile(sys.argv[1]) as z:
 strings=[''.join(t.itertext()) for t in ET.fromstring(z.read('xl/sharedStrings.xml'))] if 'xl/sharedStrings.xml' in z.namelist() else []
 rel={x.get('Id'):x.get('Target') for x in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
 styles=ET.fromstring(z.read('xl/styles.xml'));fonts=styles.find('m:fonts',ns);xfs=styles.find('m:cellXfs',ns)
 structure={}
 for sheet in ET.fromstring(z.read('xl/workbook.xml')).find('m:sheets',ns):
  name=sheet.get('name');kind='BS' if name=='BS_Sektör' else 'PL' if name=='P&L_Sektör' else None
  if not kind:continue
  target=rel[sheet.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')];path=target.lstrip('/') if target.startswith('/') else 'xl/'+target
  cells={};cell_styles={}
  for c in ET.fromstring(z.read(path)).findall('m:sheetData/m:row/m:c',ns):
   v=c.find('m:v',ns);value=v.text if v is not None else ''
   if c.get('t')=='s':value=strings[int(value)]
   elif c.get('t')=='inlineStr':value=''.join(c.find('m:is',ns).itertext())
   cells[c.get('r')]=(value,c.get('t'));cell_styles[c.get('r')]=int(c.get('s','0'))
  header=1 if kind=='BS' else 2;dates=[]
  for ref,(v,t) in cells.items():
   col=''.join(filter(str.isalpha,ref));row=int(''.join(filter(str.isdigit,ref)))
   if row==header and col not in ['A','B'] and t not in ['s','inlineStr','str'] and v:
    dates.append((datetime.datetime(1899,12,30)+datetime.timedelta(days=float(v))).strftime('%Y-%m-%d'))
  mapping=BS if kind=='BS' else {r+3:r for r in range(3,81) if cells.get('A'+str(r),('',None))[0].strip() not in ['', 'Cumulative','Monthly']}
  rows=[]
  for ident,src in mapping.items():
   label=cells['A'+str(src)][0].strip();fmt=cells.get('B'+str(src),('',None))[0].strip() or 'TL'
   xf=xfs[cell_styles.get('A'+str(src),0)];font=fonts[int(xf.get('fontId','0'))];alignment=xf.find('m:alignment',ns);color=font.find('m:color',ns)
   indent=int(float(alignment.get('indent','0'))) if alignment is not None else 0
   gray=color is not None and ((color.get('theme')=='0' and float(color.get('tint','0'))<0) or color.get('rgb','')[-6:].upper() in ['808080','7F7F7F','999999'])
   title_style={'indent':indent,'gray':gray,'bold':font.find('m:b',ns) is not None}
   rows.append({'titleStyle':title_style,'row':ident,'sourceRow':src,'label':label,'format':fmt,'ratio':fmt=='%'})
  rows.sort(key=lambda item:item['sourceRow'])
  structure[kind]={'dates':dates,'headerRow':header,'firstDateColumn':'C','rows':rows}
(root/'dist/structure.json').write_text(json.dumps(structure,ensure_ascii=False))
(root/'dist/structure.js').write_text('window.TEMPLATE = '+json.dumps(structure,ensure_ascii=False)+';\n')
print('Extracted schema only:',{k:len(v['rows']) for k,v in structure.items()})
