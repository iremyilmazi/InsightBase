"""Build live-data Windows deliveries; never copy a workbook."""
from pathlib import Path
import shutil,zipfile
root=Path(__file__).parent
for txt in [False,True]:
 out=root.parent/('InsightBase-Windows-Live-TXT' if txt else 'InsightBase-Windows-Live')
 out.mkdir(exist_ok=True)
 for name in ['InsightBase.html','InsightBase.css','InsightBase.js']:
  shutil.copy2(root.parent/'InsightBase-Windows'/name,out/(name+'.txt' if txt and name.endswith('.js') else name))
 shutil.copy2(root/'windows_start.cmd',out/('Baslat.cmd.txt' if txt else 'Baslat.cmd'))
 shutil.copy2(root/'WINDOWS_LIVE_README.md',out/'BASLANGIC.md')
 assert len(list(out.iterdir()))==5 and not any(p.suffix=='.xlsx' for p in out.iterdir())
 with zipfile.ZipFile(out.with_suffix('.zip'),'w',zipfile.ZIP_DEFLATED) as z:
  for p in sorted(out.iterdir()):z.write(p,p.name)
 print(out.with_suffix('.zip'))
