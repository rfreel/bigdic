import {validateProject} from './core.mjs';
export const stable=v=>v===null||typeof v!=='object'?JSON.stringify(v):Array.isArray(v)?'['+v.map(stable).join(',')+']':'{'+Object.keys(v).sort().map(k=>JSON.stringify(k)+':'+stable(v[k])).join(',')+'}';
export async function digest(v){return [...new Uint8Array(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(stable(v))))].map(n=>n.toString(16).padStart(2,'0')).join('');}
export async function appendRecord(events,project,action){
 if(events.length>=2000)throw new Error('History limit reached. Export a backup before starting a new workspace.');
 const r={seq:events.length+1,previous:events.at(-1)?.hash||'0'.repeat(64),at:new Date().toISOString(),action,project:structuredClone(project)};
 return {...r,hash:await digest(r)};
}
export async function verifyJournal(db,pack,sourceHash){
 if(!pack||pack.format!=='bigdic-journal-v1'||pack.sourceHash!==sourceHash||!Array.isArray(pack.events)||!pack.events.length||pack.events.length>2000)throw new Error('Invalid backup or different dictionary revision.');
 let prev='0'.repeat(64);
 for(let i=0;i<pack.events.length;i++){
  const {hash,...r}=pack.events[i];
  if(r.seq!==i+1||r.previous!==prev||!Number.isFinite(Date.parse(r.at))||typeof r.action!=='string'||r.action.length>500||await digest(r)!==hash)throw new Error('History integrity check failed at event '+(i+1));
  validateProject(db,r.project);prev=hash;
 }
 if(pack.head!==prev)throw new Error('History head mismatch.');
 return structuredClone(pack.events.at(-1).project);
}
