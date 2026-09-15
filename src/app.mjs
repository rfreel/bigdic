import {parseDictionary,searchDictionary,compareSignatures,inspectPrompt,compileProject,emptyProject,validateProject,auditDictionary} from './core.mjs';
import {appendRecord,verifyJournal} from './journal.mjs';
const payload=JSON.parse(document.querySelector('#source-data').textContent);
const db=parseDictionary(payload.source),sha=payload.sha256,key='bigdic-workspace-v1:'+sha;
const $=s=>document.querySelector(s), esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const pretty=s=>s.replaceAll('_',' ').toLowerCase();
let current='dictionary',selected=db.byLexeme.get('LEX-verify')||db.lexemes[0],sense=db.bySignature.get('SIG-verify-P-external')||db.bySignature.get(selected.signatureIds[0]);
let pins=[],project=emptyProject(),events=[],storageRaw=null,busy=false,blocked=false,filterTimer;
let pendingSave=Promise.resolve();
function notify(s){$('#notice').textContent=s;}
function error(e){notify('Could not complete: '+e.message);}
function download(name,body,type='application/json'){const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([body],{type}));a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000);}
function pack(es=events){return {format:'bigdic-journal-v1',sourceHash:sha,head:es.at(-1)?.hash,events:es};}
function save(next,action){const task=pendingSave.then(()=>saveNow(next,action));pendingSave=task.catch(()=>{});return task;}
async function saveNow(next,action){
 if(blocked)throw new Error('Workspace history needs recovery. Export the raw backup first.');
 if(busy)throw new Error('A save is already in progress. Retry after it completes.');
 validateProject(db,next);busy=true;$('#save-status').textContent='Saving…';
 try{
  const write=async()=>{
   if(localStorage.getItem(key)!==storageRaw)throw new Error('Another tab changed this workspace. Reload to reconcile before editing.');
   const event=await appendRecord(events,next,action);const es=[...events,event];const raw=JSON.stringify(pack(es));
   localStorage.setItem(key,raw);storageRaw=raw;events=es;project=structuredClone(next);
  };
  if(navigator.locks)await navigator.locks.request('bigdic:'+sha,write);else await write();
  $('#save-status').textContent='Saved locally · '+events.length+' history events';renderStrip();renderHistory();
 }catch(e){$('#save-status').textContent='Not saved · '+e.message;throw e;}finally{busy=false;}
}
function showTab(tab){current=tab;for(const id of ['dictionary','compare','build','inspect'])$('#'+id).hidden=id!==tab;document.querySelectorAll('nav [data-tab]').forEach(b=>{b.classList.toggle('active',b.dataset.tab===tab);b.setAttribute('aria-current',b.dataset.tab===tab?'page':'false');});if(tab==='build')renderBuild();if(tab==='compare')renderCompare();}
function filters(){return {query:$('#search').value,contract:$('#contract').value,origin:$('#origin').value,role:$('#role').value,axis:$('#axis').value};}
function renderTerms(){
 const matches=searchDictionary(db,filters());$('#result-count').textContent=matches.length+' results';
 $('#term-list').innerHTML=matches.length?matches.map(({lex,senses})=>`<button class="term-row ${lex.id===selected?.id?'active':''}" data-lex="${esc(lex.id)}"><strong>${esc(lex.term)}</strong><span>${lex.signatureIds.length} ${lex.signatureIds.length===1?'sense':'senses'} · ${esc([...new Set(senses.map(s=>s.contractRef))].join(', '))}</span></button>`).join(''):'<div class="empty">No matching terms. Try a broader phrase or reset the filters.</div>';
 if(matches.length&&!matches.some(x=>x.lex.id===selected?.id)){selected=matches[0].lex;sense=matches[0].senses[0];renderTerms();renderDetail();}
 else if(matches.length){const row=matches.find(x=>x.lex.id===selected.id);if(!row.senses.some(s=>s.id===sense.id)){sense=row.senses[0];renderDetail();}}
 else $('#detail').innerHTML='<div class="empty">No term selected under these filters.</div>';
}
function fieldBlock(title,value){return value?`<div class="detail-section"><span class="field-label">${esc(title)}</span><p>${esc(value)}</p></div>`:'';}
function renderDetail(){
 if(!sense)return;if(!searchDictionary(db,filters()).length){$('#detail').innerHTML='<div class="empty">No term selected under these filters.</div>';return;}const s=sense,c=db.contracts[s.contractRef];
 const active=searchDictionary(db,filters()).find(x=>x.lex.id===selected.id)?.senses||selected.signatureIds.map(id=>db.bySignature.get(id));
 $('#detail').innerHTML=`<div class="detail-top"><div><h2>${esc(selected.term)}</h2><div class="small muted">${selected.signatureIds.length} senses · ${esc(selected.roles.join(', '))}</div></div><span class="badge">${s.origin==='AUTHORED_MIGRATION_PROPOSAL'?'Authored proposal':'Source-mapped'}</span></div><div class="sense-tabs" aria-label="Available senses">${active.map((x,i)=>`<button data-sense="${esc(x.id)}" class="${x.id===s.id?'active':''}" title="${esc(x.id)}">${esc(x.axis||x.id.split('-P-')[1]||x.source.split(' / ')[0]||'Sense '+(i+1))}</button>`).join('')}</div><div class="signature-id">${esc(s.id)}</div><p class="definition">${esc(s.definition)}</p><div class="role-flow"><div class="role-box"><small>Input</small>${esc(s.inputs.join(', '))}</div><span aria-hidden="true">→</span><div class="role-box"><small>Output</small>${esc(s.outputs.join(', '))}</div></div><div>${s.obligations.map(x=>`<span class="obligation">${esc(x)}</span>`).join('')}</div>${fieldBlock('Evidence required',s.evidence||c.fields['Evidence obligations'])}${fieldBlock('Status rule',s.statusRule||c.fields['Status rule'])}${fieldBlock('Modifier destination',s.destination)}${fieldBlock('Example',s.example)}<div class="button-row"><button data-add="${esc(s.id)}" class="primary">Add to sequence +</button><button data-pin="${esc(s.id)}" class="quiet">${pins.includes(s.id)?'Pinned':'Compare'}</button><button data-source="${esc(s.id)}" class="quiet">Source</button></div><p class="source-line">V2 lines ${s.start}–${s.end} · ${esc(s.source)}</p><details><summary>Inherited ${esc(s.contractRef)} contract</summary>${Object.entries(c.fields).map(([k,v])=>`<div class="contract-field"><strong>${esc(k)}</strong>${esc(v)}</div>`).join('')}</details>${s.closureRule?fieldBlock('Local closure refinement',s.closureRule):''}`;
}
function selectSense(id){sense=db.bySignature.get(id);if(!sense)return;selected=db.byLexeme.get(sense.lexemeId);$('#search').value='';for(const x of ['contract','origin','role','axis'])$('#'+x).value='';showTab('dictionary');renderTerms();renderDetail();}
function renderCompare(){
 if(pins.length<2){$('#comparison').innerHTML=`<div class="empty panel">${pins.length?'One sense pinned. Choose another from Dictionary.':'Pin two or more senses to compare their contracts.'}</div>`;return;}
 const rows=compareSignatures(db,pins);
 $('#comparison').innerHTML=`<div class="comparison-wrap"><table><thead><tr><th>Property</th>${pins.map(id=>`<th>${esc(db.bySignature.get(id).term)}<div class="signature-id">${esc(id)}</div><button data-unpin="${esc(id)}">Remove</button></th>`).join('')}</tr></thead><tbody>${rows.map(r=>`<tr class="${r.different?'different':''}"><td>${esc(r.key)}</td>${r.values.map(v=>`<td>${esc(Array.isArray(v)?v.join(', '):v||'Not locally specified')}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
}
function renderStrip(){
 $('#build-count').textContent=project.steps.length;$('#compare-count').textContent=pins.length;$('#strip-count').textContent=String(project.steps.length).padStart(2,'0');
 $('#strip-steps').innerHTML=project.steps.length?project.steps.map((s,i)=>`<button class="strip-step" data-tab="build">${String(i+1).padStart(2,'0')} &nbsp; ${esc(db.bySignature.get(s.signatureId).term)}<small>${esc(s.signatureId)}</small></button>`).join(''):'<span class="small muted">Choose a meaning above, then add it to your sequence.</span>';
}
function renderHistory(){
 $('#journal-status').textContent=events.length+' events';
 $('#history').innerHTML=events.slice(-12).reverse().map(e=>`<div class="history-row"><span class="muted">${String(e.seq).padStart(3,'0')}</span><span>${esc(e.action)} <button class="restore" data-restore="${e.seq}">Restore draft</button></span><time>${esc(new Date(e.at).toLocaleTimeString())}</time></div>`).join('');
}
function renderBuild(){
 $('#bindings').innerHTML=Object.entries(project.bindings).map(([k,v])=>`<label for="bind-${k}">${esc(k[0].toUpperCase()+k.slice(1))}</label><textarea id="bind-${k}" data-bind="${k}" rows="${k==='objective'||k==='scope'?2:1}" maxlength="4000" placeholder="${esc({objective:'What must the work achieve?',target:'Document, artifact, system, or proposition',scope:'What is included and excluded?',actor:'Who will perform the work?',revision:'Which version or time boundary?'}[k])}">${esc(v)}</textarea>`).join('');
 $('#step-count').textContent=project.steps.length+' steps';
 $('#steps').innerHTML=project.steps.length?project.steps.map((x,i)=>{const s=db.bySignature.get(x.signatureId);return `<article class="step"><div class="step-title"><strong><span class="muted">${String(i+1).padStart(2,'0')}</span> ${esc(s.term)}</strong><div class="step-tools"><button data-move="${i}" data-direction="-1" aria-label="Move step ${i+1} up" ${i===0?'disabled':''}>↑</button><button data-move="${i}" data-direction="1" aria-label="Move step ${i+1} down" ${i===project.steps.length-1?'disabled':''}>↓</button><button data-remove="${i}" aria-label="Remove step ${i+1}">Remove</button></div></div><div class="step-id">${esc(s.id)} · ${esc(s.origin)}</div><p class="small">${esc(s.definition)}</p><div class="step-fields"><div><label for="property-${i}">Required property / output</label><textarea id="property-${i}" data-step="${i}" data-field="property" rows="2" maxlength="4000">${esc(x.property)}</textarea></div><div><label for="evidence-${i}">Evidence plan</label><textarea id="evidence-${i}" data-step="${i}" data-field="evidence" rows="2" maxlength="4000">${esc(x.evidence)}</textarea></div></div></article>`;}).join(''):'<div class="empty">Your sequence is empty. Add an exact sense from the dictionary, or load the example.</div>';
 renderCompilation();renderHistory();
}
function renderCompilation(){const out=compileProject(db,project,sha);$('#draft-status').textContent=out.result.status.replaceAll('_',' ');$('#draft-status').className=out.result.status==='BOUND_DRAFT'?'bound':'muted';$('#lint').innerHTML=out.result.warnings.length?out.result.warnings.map(w=>`<div class="lint-item">${esc(w.code)} · ${esc(w.message)}</div>`).join(''):'<p class="bound">Required bindings supplied. Execution and semantic verification remain separate.</p>';$('#output').textContent=out.text;}
function sourceDialog(id){const s=db.bySignature.get(id);$('#source-title').textContent=`${s.id} · V2 lines ${s.start}–${s.end}`;$('#source-content').textContent=s.raw;$('#source-dialog').showModal();}
function inspect(){
 const text=$('#prompt').value;const result=inspectPrompt(db,text);let offset=0,html='';
 for(const m of result.occurrences){html+=esc(text.slice(offset,m.start))+'<mark>'+esc(text.slice(m.start,m.end))+'</mark>';offset=m.end;}html+=esc(text.slice(offset));
 $('#inspection').innerHTML=`<div class="highlight-prompt">${html||'Enter a prompt to inspect.'}</div><p class="small muted">${result.occurrences.length} expressions matched. All senses are retained; no interpretation is selected automatically.</p>`+result.occurrences.map(m=>`<article class="match"><div class="match-head"><div><h3>${esc(m.text)}</h3><span class="small muted">${m.signatureIds.length} candidate senses · characters ${m.start}–${m.end}</span></div><span class="badge">${m.signatureIds.length>1?'Ambiguous lexical match':'One indexed sense'}</span></div><div class="match-buttons">${m.lexemeIds.map(id=>`<button data-view="${esc(db.byLexeme.get(id).signatureIds[0])}">Explore ${esc(db.byLexeme.get(id).term)}</button>`).join('')}</div>${m.nested.length?`<details><summary>${m.nested.length} nested lexical matches retained</summary>${m.nested.map(n=>`<p>${esc(n.text)}: ${n.lexemeIds.map(esc).join(', ')}</p>`).join('')}</details>`:''}</article>`).join('');
}
async function loadExample(){const p=emptyProject();p.bindings={objective:'Check a document against its source without changing its meaning.',target:'A draft report and its cited source',scope:'Dates, amounts, obligations, and exceptions; no external publication',actor:'Reviewing assistant',revision:'Explicitly bind the supplied document revisions before execution'};const ids=['SIG-compile-SRC-0002','SIG-inspect-SRC-0055','SIG-verify-P-source'];
 // Resolve source senses by exact family only for this authored, labeled example.
 p.steps=['COMPILE','INSPECT','VERIFY'].map((term,i)=>{const lex=db.lexemes.find(l=>l.term===term);const s=i===2?db.bySignature.get('SIG-verify-P-source'):db.bySignature.get(lex.signatureIds.find(id=>db.bySignature.get(id).origin==='SOURCE_MAPPED_CANDIDATE')||lex.signatureIds[0]);return {signatureId:s.id,property:['Explicit scope and protected properties','Observed source values with locations','Correspondence between draft and source'][i],evidence:['Original request and document identifiers','Source quotations with line or page locations','Recorded comparisons for each required property'][i]};});await save(p,'Loaded example sequence');renderBuild();notify('Example loaded. Review and bind the actual document revisions before use.');}
async function handleClick(event){const b=event.target.closest('button');if(!b)return;
 try{
 await pendingSave;
 if(b.dataset.tab){showTab(b.dataset.tab);return;}
 if(b.dataset.close){$('#'+b.dataset.close).close();return;}
 if(b.dataset.lex){selected=db.byLexeme.get(b.dataset.lex);sense=searchDictionary(db,filters()).find(x=>x.lex.id===selected.id).senses[0];renderTerms();renderDetail();return;}
 if(b.dataset.sense){sense=db.bySignature.get(b.dataset.sense);renderDetail();return;}
 if(b.dataset.view){selectSense(b.dataset.view);return;}
 if(b.dataset.source){sourceDialog(b.dataset.source);return;}
 if(b.dataset.pin){if(!pins.includes(b.dataset.pin)){if(pins.length===4){notify('Four senses are already pinned. Remove one in Compare.');return;}pins.push(b.dataset.pin);}renderStrip();renderDetail();notify('Sense pinned. Open Compare to inspect the differences.');return;}
 if(b.dataset.unpin){pins=pins.filter(x=>x!==b.dataset.unpin);renderStrip();renderCompare();return;}
 if(b.dataset.add){const p=structuredClone(project);p.steps.push({signatureId:b.dataset.add,property:'',evidence:''});await save(p,'Added '+b.dataset.add);notify('Added '+db.bySignature.get(b.dataset.add).term+' to the sequence.');return;}
 if(b.dataset.remove!==undefined){const p=structuredClone(project);p.steps.splice(Number(b.dataset.remove),1);await save(p,'Removed step '+(Number(b.dataset.remove)+1));renderBuild();return;}
 if(b.dataset.move!==undefined){const p=structuredClone(project),i=Number(b.dataset.move),j=i+Number(b.dataset.direction);[p.steps[i],p.steps[j]]=[p.steps[j],p.steps[i]];await save(p,'Reordered step '+(i+1));renderBuild();return;}
 if(b.dataset.restore){const e=events.find(x=>x.seq===Number(b.dataset.restore));await save(e.project,'Restored draft from event '+e.seq);renderBuild();notify('Restored as a new event. Earlier history remains intact.');return;}
 switch(b.id){
 case 'help-button':$('#help-dialog').showModal();break;
 case 'reset':for(const id of ['search','contract','origin','role','axis'])$('#'+id).value='';renderTerms();renderDetail();break;
 case 'clear-compare':pins=[];renderStrip();renderCompare();break;
 case 'download-source':download('dictionary-v2.md',payload.source,'text/markdown');break;
 case 'example-sequence':await loadExample();break;
 case 'copy-instructions':{const text=compileProject(db,project,sha).text;try{await navigator.clipboard.writeText(text);notify('Instructions copied.');}catch{download('bigdic-instructions.md',text,'text/markdown');notify('Clipboard unavailable. Downloaded the instructions instead.');}break;}
 case 'export-markdown':download('bigdic-instructions.md',compileProject(db,project,sha).text,'text/markdown');break;
 case 'export-json':download('bigdic-contract.json',JSON.stringify(compileProject(db,project,sha).result,null,2));break;
 case 'export-project':download('bigdic-project.json',JSON.stringify({format:'bigdic-project-v1',sourceHash:sha,project},null,2));break;
 case 'backup-button':download('bigdic-history.json',blocked?(storageRaw||'null'):JSON.stringify(pack(),null,2));break;
 case 'import-button':$('#file-input').click();break;
 case 'inspect-button':inspect();break;
 case 'inspect-example':$('#prompt').value='Rigorously verify exactly two sources. Localize the failure, preserve scope, and do not claim independently verified.';inspect();break;
 }
 }catch(e){error(e);}
}
document.addEventListener('click',handleClick);
document.addEventListener('keydown',e=>{if(e.key==='/'&&!['INPUT','TEXTAREA','SELECT'].includes(document.activeElement.tagName)){e.preventDefault();showTab('dictionary');$('#search').focus();}});
$('#search').addEventListener('input',()=>{clearTimeout(filterTimer);filterTimer=setTimeout(()=>{renderTerms();renderDetail();},80);});
for(const id of ['contract','origin','role','axis'])$('#'+id).addEventListener('change',()=>{renderTerms();renderDetail();});
document.addEventListener('change',async e=>{const x=e.target;if(!x.dataset.bind&&x.dataset.step===undefined)return;await pendingSave;const p=structuredClone(project);if(x.dataset.bind)p.bindings[x.dataset.bind]=x.value;else p.steps[Number(x.dataset.step)][x.dataset.field]=x.value;try{await save(p,x.dataset.bind?'Bound '+x.dataset.bind:'Updated step '+(Number(x.dataset.step)+1)+' '+x.dataset.field);renderCompilation();}catch(err){error(err);renderBuild();}});
$('#file-input').addEventListener('change',async e=>{try{const file=e.target.files[0];if(!file)return;await pendingSave;if(file.size>10000000)throw new Error('Import limit is 10 MB.');const x=JSON.parse(await file.text());let p;if(x.format==='bigdic-journal-v1')p=await verifyJournal(db,x,sha);else if(x.format==='bigdic-project-v1'&&x.sourceHash===sha)p=validateProject(db,x.project);else throw new Error('Expected a BIGDIC project or history export from this dictionary revision.');await save(p,'Imported '+file.name);renderBuild();notify('Imported draft. Existing history is preserved; imported history was validated but is not merged.');}catch(err){error(err);}finally{e.target.value='';}});
window.addEventListener('storage',e=>{if(e.key===key&&e.newValue!==storageRaw){notify('Another tab updated the workspace. Reload before editing to preserve both histories.');}});
for(const [id,values] of [['contract',Object.keys(db.contracts)],['role',[...new Set(db.lexemes.flatMap(l=>l.roles))]],['axis',[...new Set(db.signatures.map(s=>s.axis).filter(Boolean))]]])for(const v of values.sort())$('#'+id).insertAdjacentHTML('beforeend',`<option value="${esc(v)}">${esc(id==='role'?pretty(v):v)}</option>`);
$('#inventory').textContent=`${db.lexemes.length} terms / ${db.signatures.length.toLocaleString()} senses`;
try{storageRaw=localStorage.getItem(key);if(storageRaw){const p=JSON.parse(storageRaw);project=await verifyJournal(db,p,sha);events=p.events;$('#save-status').textContent='Saved locally · '+events.length+' history events';}else await save(project,'Created workspace');}
catch(e){blocked=true;$('#fatal').hidden=false;$('#fatal').textContent='Workspace could not be loaded safely: '+e.message+'. Your stored data has not been overwritten. Dictionary, comparison, and inspection remain available. Use Build → Backup history to recover the raw record.';$('#save-status').textContent='History needs recovery';}
renderTerms();renderDetail();renderStrip();renderBuild();
