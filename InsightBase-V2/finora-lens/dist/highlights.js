/* Deterministic balance-sheet highlights. No AI, external data or stored state. */
(function(root){
const E=root.FinoraEngine,median=a=>{const s=[...a].sort((x,y)=>x-y),n=s.length;return n%2?s[(n-1)/2]:(s[n/2-1]+s[n/2])/2;};
function analyze(dataset,template,group,asOf=new Date().toISOString().slice(0,10)){
 const sh=dataset.sheets.find(s=>s.type==='BS'&&s.group===group);if(!sh)return {cards:[],candidates:[]};
 const date=sh.dates.filter((d,i)=>sh.rows.some(r=>E.finite(r.values[i]))).sort().at(-1);if(!date)return {cards:[],candidates:[]};
 const spec=id=>template.BS.rows.find(r=>r.row===id),series=(id,g=group)=>E.metricSeries(dataset.sheets.find(s=>s.type==='BS'&&s.group===g),id);
 const metric=(id,cut=date,g=group)=>{const m=E.monthlyCompare(series(id,g),cut,'BS',!!spec(id)?.ratio,false,asOf);return m.current?.date===cut?m:null;};
 const aligned=ms=>ms.every(m=>m?.current&&m.prior&&E.finite(m.change))&&ms.every(m=>m.current.date===ms[0].current.date&&m.prior.date===ms[0].prior.date);
 const growth=(id,cut)=>{const m=metric(id,cut);return aligned([m])?{value:m.change,metrics:[m],row:id,current:m.current.value,previous:m.prior.value,delta:m.current.value-m.prior.value,currency:spec(id)?.format}:null;};
 const gap=(a,b,cut,ga=group,gb=group)=>{const ms=[metric(a,cut,ga),metric(b,cut,gb)];return aligned(ms)?{value:ms[0].change-ms[1].change,metrics:ms,left:ms[0].change,right:ms[1].change}:null;};
 const share=(part,total,term,cut)=>{const ms=[metric(part,cut),metric(total,cut),metric(term,cut)];if(!aligned(ms))return null;for(const k of ['current','prior']){const [p,t,v]=ms.map(m=>m[k].value);if(t<=0||p<0||v<0||Math.abs(p+v-t)/t>.005)return null;}const current=ms[0].current.value/ms[1].current.value*100,previous=ms[0].prior.value/ms[1].prior.value*100;return {value:current-previous,metrics:ms,current,previous};};
 const definitions=[];
 const add=(id,theme,kind,rows,fn)=>definitions.push({id,theme,kind,rows,fn});
 for(const id of [3,12,21,31,28])add('growth'+id,'growth','growth',[id],cut=>growth(id,cut));
 for(const id of [12,21,31,28])add('product'+id,'growth','product',[id,3],cut=>gap(id,3,cut));
 add('creditFX','growth','currency',[4,6],cut=>gap(4,6,cut));
 for(const id of [37,38,39])add('deposit'+id,'funding','growth',[id],cut=>growth(id,cut));
 add('depositFX','funding','currency',[38,39],cut=>gap(38,39,cut));
 add('shareTL','funding','share',[50,38,42],cut=>share(50,38,42,cut));
 add('shareFX','funding','share',[51,39,43],cut=>share(51,39,43,cut));
 add('fundingGap','funding','fundingGap',[3,37],cut=>gap(3,37,cut));
 for(const id of [57,153,154])add('ldr'+id,'funding','ratio',[id],cut=>growth(id,cut));
 for(const id of [104,112,114,116,29,33,35,155,156])add('npl'+id,'risk','ratio',[id],cut=>growth(id,cut));
 // Acceleration only compares completed months with matching month-end bases.
 add('acceleration','growth','acceleration',[3],cut=>{const m=metric(3,cut);if(!aligned([m])||m.provisional)return null;const p=E.monthlyCompare(series(3),m.prior.date,'BS',false,false,asOf);return p.prior&&E.finite(p.change)?{value:m.change-p.change,metrics:[m],left:m.change,right:p.change}:null;});
 if(group==='Sektör')for(const id of [3,37,31])add('groups'+id,id===37?'funding':'growth','groups',[id],cut=>gap(id,id,cut,'Ozel','Kamu'));
 const anchor=new Date(date+'T00:00:00Z'),historyCuts=[];
 for(let i=1;i<=36;i++){const end=E.monthEnd(anchor.getUTCFullYear(),anchor.getUTCMonth()-i),p=E.at(series(3),end,7);if(p&&p.date.slice(0,7)===end.slice(0,7)&&end<asOf)historyCuts.push(p.date);}
 const candidates=definitions.flatMap(def=>{if(def.rows.some(id=>!spec(id)))return [];const v=def.fn(date);if(!v||!E.finite(v.value)||Math.abs(v.value)<1e-9)return [];
 const provisional=v.metrics.some(m=>m.provisional),history=historyCuts.map(c=>def.fn(c)?.value).filter(E.finite).slice(0,12);
 // Rank by empirical absolute deviation from each rule's own median; no invented financial threshold.
 let percentile=null,center=null,mad=null;if(!provisional&&history.length===12){center=median(history);const deviations=history.map(x=>Math.abs(x-center));mad=median(deviations);const distance=Math.abs(v.value-center);percentile=deviations.filter(x=>x<distance).length/12;}
 return [{...def,...v,provisional,date,baseDate:v.metrics[0].prior.date,historyCount:history.length,median:center,mad,percentile}];});
 const cards=[];
 for(const theme of ['growth','funding','risk']){const pool=candidates.filter(c=>c.theme===theme);pool.sort((a,b)=>{if(a.percentile!==null||b.percentile!==null)return (b.percentile??-1)-(a.percentile??-1)||a.id.localeCompare(b.id);const priority=['share','fundingGap','currency','product','ratio','growth','groups','acceleration'];return priority.indexOf(a.kind)-priority.indexOf(b.kind)||((a.kind===b.kind)?Math.abs(b.value)-Math.abs(a.value):0)||a.id.localeCompare(b.id);});if(pool.length)cards.push(pool[0]);}
 return {cards,candidates};
}
root.InsightHighlights={analyze};if(typeof module!=='undefined')module.exports=root.InsightHighlights;
})(typeof window==='undefined'?globalThis:window);
