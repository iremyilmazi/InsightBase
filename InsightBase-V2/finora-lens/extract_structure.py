"""Extract only labels and date headers; never financial values."""
import zipfile, xml.etree.ElementTree as ET, json, datetime
from pathlib import Path
ns = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile('/Users/ozgur/Downloads/şablon.xlsx') as z:
    strings = [''.join(t.itertext()) for t in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si', ns)]
    structure = {}
    for name, filename, header in [('BS','sheet1.xml',1), ('PL','sheet2.xml',2)]:
        cells = ET.fromstring(z.read('xl/worksheets/'+filename)).findall('m:sheetData/m:row/m:c',ns)
        dates, rows = [], []
        for c in cells:
            ref = c.get('r'); v = c.find('m:v',ns)
            if v is None: continue
            col = ''.join(filter(str.isalpha,ref)); row = int(''.join(filter(str.isdigit,ref)))
            if row == header and col != 'A' and c.get('t') != 's':
                dates.append((datetime.datetime(1899,12,30)+datetime.timedelta(days=float(v.text))).strftime('%Y-%m-%d'))
            if col == 'A' and c.get('t') == 's' and row > header:
                label = strings[int(v.text)].strip()
                if label and label not in ['Cumulative','Monthly']: rows.append({'row':row,'label':label})
        structure[name] = {'dates':dates,'rows':rows}
    Path(__file__).with_name('dist').joinpath('structure.json').write_text(json.dumps(structure,ensure_ascii=False),encoding='utf8')
