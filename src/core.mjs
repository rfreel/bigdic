// Parsing is structural, not semantic inference. Every sense keeps its source span.
export const clean=x=>String(x??'').replaceAll('`','').trim();
export const normal=x=>String(x).normalize('NFKC').toLowerCase().trim().replace(/[\s_-]+/g,' ');
const codes=x=>[...String(x??'').matchAll(/`([^`]+)`/g)].map(x=>x[1]);
const field=(raw,label)=>raw.split('\n').find(l=>l.startsWith(label+': '))?.slice(label.length+2)||'';
const required=(value,label)=>{if(!value)throw new Error('Missing '+label);return value;};
export function parseDictionary(source){
 const lines=source.split('\n');const headings=[];
 lines.forEach((line,i)=>{const m=/^(#{2,4}) (.+)$/.exec(line);if(m)headings.push({level:m[1].length,title:m[2],line:i});});
 const span=h=>{const next=headings.find(x=>x.line>h.line&&x.level<=h.level);return {start:h.line+1,end:next?next.line:lines.length,raw:lines.slice(h.line,next?.line??lines.length).join('\n')};};
 const contracts={};
 for(const h of headings.filter(h=>h.level===3&&h.title.startsWith('Contract '))){const s=span(h);const name=h.title.slice(9);const fields={},prose=[];for(const l of s.raw.split('\n')){const m=/^([^:]+): (.*)$/.exec(l);if(m)fields[m[1]]=m[2];else if(l.trim()&&!l.startsWith('### Contract '))prose.push(l);}contracts[name]={name,...s,fields,prose:prose.join('\n')};}
 const lexStart=required(headings.find(h=>h.title==='Lexical dictionary'),'Lexical dictionary heading').line;
 const lexEnd=headings.find(h=>h.level===2&&h.line>lexStart)?.line??lines.length;
 const lexemes=[];const signatures=[];
 for(const h of headings.filter(h=>h.level===3&&h.line>lexStart&&h.line<lexEnd)){
  const s=span(h);const id=required(/ID: `(LEX-[^`]+)`/.exec(s.raw)?.[1],'lexeme ID at '+s.start);
  const roleLine=field(s.raw,'ID');const roles=(/Roles: ([^.]+)\./.exec(roleLine)?.[1]||'').split(',').map(x=>x.trim()).filter(Boolean);
  const lex={id,term:h.title,roles,forms:codes(field(s.raw,'Source forms')),start:s.start,end:s.end,signatureIds:[]};
  for(const sh of headings.filter(x=>x.level===4&&x.line>h.line&&x.line<s.end)){
   const ss=span(sh);const op=field(ss.raw,'Operator');const obligation=field(ss.raw,'Correctness obligations');const origin=field(ss.raw,'Origin');
   const sig={id:sh.title,lexemeId:id,term:h.title,...ss,
    origin:origin.split('. Source: ')[0],source:origin.split('. Source: ').slice(1).join('. Source: '),
    operator:required(/`([^`]+)`/.exec(op)?.[1],'operator'),
    inputs:codes(/Input roles: (.*?)\. Output roles:/.exec(op)?.[1]),outputs:codes(/Output roles: (.*)/.exec(op)?.[1]),
    obligations:codes(obligation.split('. Contract:')[0]),contractRef:required(/Contract: `([^`]+)`/.exec(obligation)?.[1],'contract'),
    definition:required(field(ss.raw,'Transition or retained definition'),'definition'),
    evidence:field(ss.raw,'Evidence required'),statusRule:field(ss.raw,'Status rule'),closureRule:field(ss.raw,'Closure rule'),
    example:field(ss.raw,'Concrete instance'),principle:field(ss.raw,'Abstract principle'),
    axis:codes(field(ss.raw,'Axis'))[0]||'',destination:field(ss.raw,'Axis').split('. Destination: ').slice(1).join('. Destination: '),
    assessment:field(ss.raw,'Assessment dimension'),macro:field(ss.raw,'Macro source expression')};
   if(!contracts[sig.contractRef])throw new Error('Unresolved contract '+sig.contractRef);
   signatures.push(sig);lex.signatureIds.push(sig.id);
  }
  if(!lex.signatureIds.length)throw new Error('Lexeme without signatures: '+id);
  lexemes.push(lex);
 }
 if(new Set(lexemes.map(l=>l.id)).size!==lexemes.length||new Set(signatures.map(s=>s.id)).size!==signatures.length)throw new Error('Duplicate record ID');
 return {title:lines[0].replace(/^# /,''),lexemes,signatures,contracts,source,lines,bySignature:new Map(signatures.map(s=>[s.id,s])),byLexeme:new Map(lexemes.map(l=>[l.id,l]))};
}
export function searchDictionary(db,{query='',contract='',origin='',role='',axis=''}={}){
 const q=normal(query);const words=q.split(/\s+/).filter(Boolean);
 return db.lexemes.map(lex=>{
  const senses=lex.signatureIds.map(id=>db.bySignature.get(id)).filter(s=>(!contract||s.contractRef===contract)&&(!origin||s.origin===origin)&&(!axis||s.axis===axis));
  if(!senses.length||(role&&!lex.roles.includes(role)))return null;
  const hay=normal([lex.term,...lex.forms,...lex.roles,...senses.map(s=>[s.id,s.definition,s.operator,s.contractRef,s.axis,s.obligations.join(' '),s.inputs.join(' '),s.outputs.join(' ')].join(' '))].join(' '));
  if(!words.every(w=>hay.includes(w)))return null;
  const exact=[lex.term,...lex.forms].some(f=>normal(f)===q);const prefix=normal(lex.term).startsWith(q);
  return {lex,senses,score:q?(exact?0:prefix?1:2):0};
 }).filter(Boolean).sort((a,b)=>a.score-b.score||a.lex.term.localeCompare(b.lex.term,'en'));
}
export function compareSignatures(db,ids){
 const fields=['operator','inputs','outputs','obligations','contractRef','definition','origin','source','axis','evidence','statusRule','closureRule'];
 const senses=ids.map(id=>db.bySignature.get(id)||(()=>{throw new Error('Unknown signature: '+id);})());
 return fields.map(key=>({key,values:senses.map(s=>s[key]),different:new Set(senses.map(s=>JSON.stringify(s[key]))).size>1}));
}
export function inspectPrompt(db,prompt){
 if(typeof prompt!=='string'||prompt.length>20000)throw new Error('Prompt limit is 20,000 characters.');
 const occurrences=[];
 // Match original offsets, separators may vary; collect all lexical alternatives per span.
 const spans=new Map();
 for(const lex of db.lexemes){for(const form of new Set([lex.term,...lex.forms])){
  const escaped=form.trim().split(/[\s_-]+/).map(s=>s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')).join('[\\s_-]+');
  if(!escaped)continue;
  const re=new RegExp('(?<![\\p{L}\\p{N}_])'+escaped+'(?![\\p{L}\\p{N}_])','giu');
  for(const m of prompt.matchAll(re)){
   const key=m.index+':'+(m.index+m[0].length);if(!spans.has(key))spans.set(key,{start:m.index,end:m.index+m[0].length,text:m[0],lexemeIds:[]});
   const x=spans.get(key);if(!x.lexemeIds.includes(lex.id))x.lexemeIds.push(lex.id);
  }
 }}
 const sorted=[...spans.values()].sort((a,b)=>a.start-b.start||b.end-a.end);
 for(const m of sorted){
  // Longest non-overlapping display match; retain overlapping/nested candidates explicitly.
  if(occurrences.some(x=>m.start<x.end))continue;
  const nested=sorted.filter(x=>x!==m&&x.start>=m.start&&x.end<=m.end);
  occurrences.push({...m,signatureIds:m.lexemeIds.flatMap(id=>db.byLexeme.get(id).signatureIds),nested});
 }
 return {occurrences,unmatched:prompt.length&&!occurrences.length,limitations:'Lexical matches only. Negation, scope, applicability, intent, and semantic equivalence are not inferred.'};
}
export function validateProject(db,p){
 if(!p||p.version!==1||!p.bindings||typeof p.bindings!=='object'||!Array.isArray(p.steps)||p.steps.length>100)throw new Error('Invalid project (maximum 100 steps).');
 for(const k of ['objective','target','scope','actor','revision'])if(typeof p.bindings[k]!=='string'||p.bindings[k].length>4000)throw new Error('Invalid binding: '+k);
 for(const s of p.steps){if(!s||!db.bySignature.has(s.signatureId)||typeof s.evidence!=='string'||s.evidence.length>4000||typeof s.property!=='string'||s.property.length>4000)throw new Error('Invalid or unknown step.');}
 return p;
}
export function compileProject(db,project,sourceHash='unrecorded'){
 validateProject(db,project);const warnings=[];const requirements=['objective','target','scope','actor','revision'];
 const missing=requirements.filter(k=>!project.bindings[k].trim());
 if(missing.length)warnings.push({code:'UNBOUND',message:'Bind '+missing.join(', ')+'.'});
 if(!project.steps.length)warnings.push({code:'EMPTY',message:'Add at least one explicit signature.'});
 const steps=project.steps.map((step,i)=>{
  const s=db.bySignature.get(step.signatureId);const parent=db.contracts[s.contractRef];
  if(!step.evidence.trim())warnings.push({code:'EVIDENCE_PLAN',step:i+1,message:'Specify what evidence will be collected for step '+(i+1)+'.'});
  if(!step.property.trim())warnings.push({code:'TARGET_PROPERTY',step:i+1,message:'Specify the property or output required for step '+(i+1)+'.'});
  if(i){const prev=db.bySignature.get(project.steps[i-1].signatureId);if(!s.inputs.some(x=>prev.outputs.includes(x)))warnings.push({code:'ROLE_HANDOFF',step:i+1,message:`Step ${i} outputs ${prev.outputs.join(', ')}; step ${i+1} expects ${s.inputs.join(', ')}. Bind an adapter or another operand. Roles are views, not disjoint physical types.`});}
  return {position:i+1,signatureId:s.id,term:s.term,operator:s.operator,origin:s.origin,source:s.source,sourceSpan:{start:s.start,end:s.end},inputRoles:s.inputs,outputRoles:s.outputs,obligations:s.obligations,transition:s.definition,property:step.property,evidencePlan:step.evidence,localEvidenceRequirement:s.evidence,localStatusRule:s.statusRule,localClosureRule:s.closureRule,contractRef:s.contractRef,inheritedContract:parent.fields,inheritedContractProse:parent.prose};
 });
 const status=warnings.some(w=>['UNBOUND','EMPTY','EVIDENCE_PLAN','TARGET_PROPERTY'].includes(w.code))?'UNBOUND_DRAFT':'BOUND_DRAFT';
 const result={version:1,status,sourceHash,bindings:structuredClone(project.bindings),steps,warnings,execution:'NOT_EXECUTED',assessment:'Binding completeness only; no authority, truth, semantic compatibility, or closure certification is established.'};
 let text=`# Bound instruction draft\n\nStatus: ${status}\nExecution: NOT_EXECUTED\nDictionary SHA-256: ${sourceHash}\n\n`;
 for(const [k,v] of Object.entries(project.bindings))text+=`${k}: ${v.trim()||'[UNBOUND]'}\n`;
 text+='\nInherited contracts and local refinements both apply. If they conflict materially, preserve the conflict rather than silently overriding either.\n';
 for(const s of steps){text+=`\n## ${s.position}. ${s.term}\nSignature: ${s.signatureId}\nOrigin: ${s.origin}\nSource: ${s.source}\nDictionary lines: ${s.sourceSpan.start}-${s.sourceSpan.end}\nInput roles: ${s.inputRoles.join(', ')}\nOutput roles: ${s.outputRoles.join(', ')}\nObligations: ${s.obligations.join(', ')}\nTransition: ${s.transition}\nRequired property: ${s.property||'[UNBOUND]'}\nEvidence plan: ${s.evidencePlan||'[UNBOUND]'}\n`;
  for(const [k,v] of [['Local evidence requirement',s.localEvidenceRequirement],['Local status rule',s.localStatusRule],['Local closure rule',s.localClosureRule]])if(v)text+=`${k}: ${v}\n`;
 }
 for(const ref of new Set(steps.map(s=>s.contractRef))){text+=`\n## Inherited contract: ${ref}\n`;for(const [k,v] of Object.entries(db.contracts[ref].fields))text+=`${k}: ${v}\n`;if(db.contracts[ref].prose)text+=db.contracts[ref].prose+'\n';}
 text+='\n## Binding checks\n'+(warnings.length?warnings.map(w=>`- ${w.code}: ${w.message}`).join('\n'):'No missing required bindings detected.')+'\n\n'+result.assessment+'\n';
 return {result,text};
}
export const emptyProject=()=>({version:1,bindings:{objective:'',target:'',scope:'',actor:'',revision:''},steps:[]});
export function auditDictionary(db){
 const signatureHeadings=(db.source.match(/^#### SIG-/gm)||[]).length;const lexicalRecords=(db.source.match(/^ID: `LEX-/gm)||[]).length;
 const unknownOrigins=[...new Set(db.signatures.map(s=>s.origin))].filter(x=>!['SOURCE_MAPPED_CANDIDATE','AUTHORED_MIGRATION_PROPOSAL'].includes(x));
 return {lexemes:db.lexemes.length,signatures:db.signatures.length,contracts:Object.keys(db.contracts).length,signatureHeadings,lexicalRecords,unknownOrigins,coverage:signatureHeadings===db.signatures.length&&lexicalRecords===db.lexemes.length&&unknownOrigins.length===0,limits:['Referenced V1 source and data/dictionary_v2.json were not supplied.','Source references are retained claims from the uploaded V2, not independently resolved V1 spans.','Lexical coverage is not semantic completeness.']};
}
