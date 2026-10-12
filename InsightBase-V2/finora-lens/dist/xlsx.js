/* Native, local XLSX reader. No remote dependencies or network calls. */
(function(root){
const decoder=new TextDecoder(),parse=s=>{const d=new DOMParser().parseFromString(s,'application/xml');if(d.querySelector('parsererror'))throw Error('Excel XML yapısı okunamadı.');return d;};
const nodes=(d,n)=>Array.from(d.getElementsByTagNameNS('*',n));
async function unzip(buffer){
 const a=new Uint8Array(buffer),v=new DataView(buffer);let e=-1;for(let i=a.length-22;i>=Math.max(0,a.length-65557);i--)if(v.getUint32(i,true)===0x06054b50){e=i;break}
 if(e<0)throw Error('Geçerli bir .xlsx dosyası değil.');let pos=v.getUint32(e+16,true),count=v.getUint16(e+10,true),total=0;const entries=new Map();
 if(count>10000||pos===0xffffffff)throw Error('Bu Excel arşiv biçimi desteklenmiyor.');
 for(let i=0;i<count;i++){
  if(v.getUint32(pos,true)!==0x02014b50)throw Error('Excel arşivi bozuk.');
  const flags=v.getUint16(pos+8,true),method=v.getUint16(pos+10,true),size=v.getUint32(pos+20,true),uncompressed=v.getUint32(pos+24,true),len=v.getUint16(pos+28,true),extra=v.getUint16(pos+30,true),comment=v.getUint16(pos+32,true),offset=v.getUint32(pos+42,true),name=decoder.decode(a.subarray(pos+46,pos+46+len));
  total+=uncompressed;if(total>120000000)throw Error('Açılmış Excel boyutu 120 MB sınırını aşıyor.');if(flags&1)throw Error('Şifreli Excel desteklenmiyor.');
  entries.set(name,{method,size,offset});pos+=46+len+extra+comment;
 }
 return async name=>{const x=entries.get(name);if(!x)return null;const off=x.offset;if(v.getUint32(off,true)!==0x04034b50)throw Error('Excel kaydı bozuk.');const start=off+30+v.getUint16(off+26,true)+v.getUint16(off+28,true),bytes=a.slice(start,start+x.size);
  if(x.method===0)return decoder.decode(bytes);if(x.method!==8)throw Error('Excel sıkıştırma yöntemi desteklenmiyor.');
  let stream;try{stream=new DecompressionStream('deflate-raw')}catch{throw Error('Bu tarayıcı yerel Excel okumayı desteklemiyor. Güncel Chrome veya Edge ile açın.');}
  return decoder.decode(await new Response(new Blob([bytes]).stream().pipeThrough(stream)).arrayBuffer());
 };
}
const normalize=s=>s.trim().toLocaleLowerCase('tr').replace(/\s+/g,' ');
async function read(file,template){
 if(file.size>20*1024*1024)throw Error('Dosya 20 MB sınırını aşıyor.');const get=await unzip(await file.arrayBuffer());
 const workbook=parse(await get('xl/workbook.xml')),rels=parse(await get('xl/_rels/workbook.xml.rels'));if(nodes(workbook,'workbookPr')[0]?.getAttribute('date1904')==='1')throw Error('1904 tarih sistemi desteklenmiyor. Excel’i 1900 tarih sistemiyle kaydedin.');
 const shared=await get('xl/sharedStrings.xml'),strings=shared?nodes(parse(shared),'si').map(si=>nodes(si,'t').map(t=>t.textContent).join('')):[];
 const styleText=await get('xl/styles.xml'),styles=styleText?parse(styleText):null,formats=new Map(styles?nodes(styles,'numFmt').map(n=>[Number(n.getAttribute('numFmtId')),n.getAttribute('formatCode')]):[]);
 const xfs=styles?nodes(styles,'cellXfs')[0]?.children:[];
 const output=[],warnings=[];
 for(const item of nodes(workbook,'sheet')){
  const name=item.getAttribute('name'),norm=normalize(name).replace(/ö/g,'o');
  const match=norm.match(/^(bs|p&l)_(sektor|ozel|kamu)$/);if(!match)continue;
  const type=match[1]==='bs'?'BS':'PL',group=({sektor:'Sektör',ozel:'Ozel',kamu:'Kamu'})[match[2]],id=item.getAttributeNS('http://schemas.openxmlformats.org/officeDocument/2006/relationships','id');
  const target=nodes(rels,'Relationship').find(r=>r.getAttribute('Id')===id)?.getAttribute('Target');if(!target)throw Error(name+' sheet bağlantısı eksik.');
  const path=target.startsWith('/')?target.slice(1):'xl/'+target.replace(/^\.\//,'');const raw=await get(path);if(!raw)throw Error(name+' okunamadı.');
  const xml=parse(raw),cells=new Map();
  for(const c of nodes(xml,'c')){
   const t=c.getAttribute('t'),raw=nodes(c,'v')[0]?.textContent;let value=null;
   if(t==='s')value=strings[Number(raw)];else if(t==='str')value=raw??null;else if(t==='inlineStr')value=nodes(c,'t').map(x=>x.textContent).join('');else if(t==='e'){warnings.push(name+'!'+c.getAttribute('r')+': Excel hata hücresi');}else if(raw!==undefined&&raw!==''&&t!=='str'&&t!=='b')value=Number(raw);
   const formatId=Number(xfs?.[Number(c.getAttribute('s')||0)]?.getAttribute('numFmtId')||0),percent=formatId===9||formatId===10||/%/.test(formats.get(formatId)||'');
   cells.set(c.getAttribute('r'),{value,percent});
  }
  const header=type==='BS'?1:2,dates=[],columns=[];
  for(const [ref,c]of cells){if(Number(ref.match(/\d+/)?.[0])===header&&!ref.startsWith('A'+header)&&typeof c.value==='number'&&c.value>=30000&&c.value<=80000){dates.push(new Date((c.value-25569)*86400000).toISOString().slice(0,10));columns.push(ref.replace(/\d+/g,''));}}
  if(!dates.length)throw Error(name+': beklenen tarih satırı bulunamadı.');if(new Set(dates).size!==dates.length)throw Error(name+': yinelenen tarihler var.');
  const order=dates.map((_,i)=>i).sort((a,b)=>dates[a].localeCompare(dates[b]));const rows=[];
  for(const spec of template[type].rows){
   const label=cells.get('A'+spec.row)?.value;if(typeof label!=='string'||normalize(label)!==normalize(spec.label)){warnings.push(name+'!A'+spec.row+': kalem başlığı şablonla eşleşmiyor; bu satır kullanılmadı.');continue;}
   const ratio=type==='BS'?spec.row===57:[29,30,31,32,45,67,68,69,70,83].includes(spec.row);
   rows.push({...spec,values:order.map(i=>{const c=cells.get(columns[i]+spec.row);return typeof c?.value==='number'&&Number.isFinite(c.value)?c.value*(ratio&&c.percent?100:1):null;})});
  }
  output.push({type,group,name,dates:order.map(i=>dates[i]),rows});
 }
 if(!output.length)throw Error('BS_Sektör / BS_Ozel / BS_Kamu veya P&L sheetleri bulunamadı.');return {sheets:output,warnings,demo:nodes(workbook,'sheet').some(s=>s.getAttribute('name')==='INSIGHTBASE_DEMO')};
}
root.LocalXLSX={read};
})(window);
