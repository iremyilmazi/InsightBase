(function(root){
const DAY=86400000;
const iso=d=>new Date(d).toISOString().slice(0,10);
const shift=(date,days)=>iso(new Date(date+'T00:00:00Z').getTime()+days*DAY);
const yearAgo=date=>{const d=new Date(date+'T00:00:00Z'),m=d.getUTCMonth();d.setUTCFullYear(d.getUTCFullYear()-1);if(d.getUTCMonth()!==m)d.setUTCDate(0);return iso(d)};
const monthEnd=(year,month)=>iso(Date.UTC(year,month+1,0));
const monthAgo=date=>{const d=new Date(date+'T00:00:00Z'),day=d.getUTCDate();d.setUTCDate(1);d.setUTCMonth(d.getUTCMonth()-1);const last=new Date(Date.UTC(d.getUTCFullYear(),d.getUTCMonth()+1,0)).getUTCDate();d.setUTCDate(Math.min(day,last));return iso(d)};
const finite=x=>typeof x==='number'&&Number.isFinite(x);
const pct=(a,b)=>!finite(a)||!finite(b)||b<=0?null:(a/b-1)*100;
function at(series,date,tolerance=0){const s=series.filter(p=>p.date<=date&&finite(p.value)).at(-1);return s&&(new Date(date)-new Date(s.date))/DAY<=tolerance?s:null}
function compare(series,date,type,ratio=false,cumulative=false){
 const current=at(series,date,type==='BS'?7:32);if(!current)return {current:null,prior:null,yoy:null,ytd:null};
 const dt=new Date(current.date+'T00:00:00Z'),y=dt.getUTCFullYear(),m=dt.getUTCMonth();
 let prior=type==='BS'?at(series,monthAgo(current.date),7):at(series,monthEnd(y,m-1));
 if(cumulative&&prior&&prior.date.slice(0,4)!==current.date.slice(0,4))prior=null;
 const yoy=type==='BS'?at(series,yearAgo(current.date),7):at(series,monthEnd(y-1,m));
 const ytd=type==='BS'?at(series,`${y-1}-12-31`,7):null;
 const delta=b=>!b?null:ratio?current.value-b.value:pct(current.value,b.value);
 return {current,prior,yoy,ytd,change:delta(prior),yoyChange:delta(yoy),ytdChange:delta(ytd)};
}
// Shared monthly stock comparison; asOf determines whether the month has closed.
function monthlyCompare(source,date,type,ratio=false,cumulative=false,asOf=date){
 const m=compare(source,date,type,ratio,cumulative);if(type!=='BS'||!m.current)return m;
 const d=new Date(m.current.date+'T00:00:00Z'),end=monthEnd(d.getUTCFullYear(),d.getUTCMonth());
 m.provisional=asOf<end;
 if(!m.provisional){m.prior=at(source,monthEnd(d.getUTCFullYear(),d.getUTCMonth()-1),7);m.change=m.prior?(ratio?m.current.value-m.prior.value:pct(m.current.value,m.prior.value)):null;}
 return m;
}
function series(sheet,row){if(!sheet)return [];const r=sheet.rows.find(r=>r.row===row);if(!r)return [];
 return sheet.dates.map((date,i)=>({date,value:finite(r.values[i])?r.values[i]:null,source:r.label}));}
function metricSeries(sheet,row){
 let s=series(sheet,row);
 // Only stock LDR is derived; all flow and ratio definitions retain source rows.
 if(sheet?.type==='BS'&&row===57){const loans=series(sheet,3),dep=series(sheet,37);s=s.map((p,i)=>finite(p.value)?p:{...p,value:finite(loans[i]?.value)&&finite(dep[i]?.value)&&dep[i].value>0?loans[i].value/dep[i].value*100:null,source:'Hesaplanan: (Gross) Krediler / Mevduatlar'});}
 return s;
}
function cumulativeYoY(sheet,row,date,ratio=false){const s=series(sheet,row),c=at(s,date,32);if(!c)return {current:null,reference:null,change:null};const d=new Date(c.date+'T00:00:00Z');const reference=at(s,monthEnd(d.getUTCFullYear()-1,d.getUTCMonth()));return {current:c,reference,change:reference?ratio?c.value-reference.value:pct(c.value,reference.value):null};}
// Twelve calendar slots, one last available source observation per month.
function monthlyChanges(source,date,type,horizon='change',ratio=false,cumulative=false,ytdSource=source){
 const latest=at(source,date,type==='BS'?7:32),anchor=latest?.date||date,d=new Date(anchor+'T00:00:00Z');
 return Array.from({length:12},(_,i)=>{const end=monthEnd(d.getUTCFullYear(),d.getUTCMonth()-11+i),cut=end<date?end:date;
  const c=at(source,cut,type==='BS'?7:32);
  if(!c||c.date.slice(0,7)!==end.slice(0,7))return {date:end,value:null};
  const m=monthlyCompare(source,c.date,type,ratio,cumulative,cut);
  const ytd=type==='PL'?compare(ytdSource,c.date,type,ratio,true).yoyChange:m.ytdChange;
  return {date:end,sourceDate:c.date,priorDate:(horizon==='change'?m.prior:horizon==='yoyChange'?m.yoy:m.ytd)?.date,value:horizon==='ytdChange'?ytd:m[horizon]??null};
 });
}
root.FinoraEngine={DAY,iso,shift,monthEnd,monthAgo,finite,pct,at,compare,monthlyCompare,series,metricSeries,cumulativeYoY,monthlyChanges};
if(typeof module!=='undefined')module.exports=root.FinoraEngine;
})(typeof window==='undefined'?globalThis:window);
