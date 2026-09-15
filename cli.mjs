#!/usr/bin/env node
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {parseDictionary,searchDictionary,inspectPrompt,compileProject,auditDictionary} from './src/core.mjs';
const source=await readFile(new URL('./data/dictionary-v2.md',import.meta.url),'utf8');
const db=parseDictionary(source),sha=createHash('sha256').update(source).digest('hex');
const [cmd,...args]=process.argv.slice(2);
try{
 switch(cmd){
 case 'audit':{const a={...auditDictionary(db),sourceSHA256:sha};console.log(JSON.stringify(a,null,2));if(!a.coverage)process.exitCode=1;break;}
 case 'search':console.log(JSON.stringify(searchDictionary(db,{query:args.join(' ')}).slice(0,30).map(x=>({term:x.lex.term,id:x.lex.id,signatures:x.senses.map(s=>({id:s.id,definition:s.definition,origin:s.origin}))})),null,2));break;
 case 'show':{const s=db.bySignature.get(args[0]);if(!s)throw new Error('Use an exact signature ID from search.');console.log(JSON.stringify({...s,inheritedContract:db.contracts[s.contractRef]},null,2));break;}
 case 'inspect':console.log(JSON.stringify(inspectPrompt(db,args.join(' ')),null,2));break;
 case 'compile':{if(!args[0])throw new Error('Provide a project JSON file.');const p=JSON.parse(await readFile(args[0],'utf8'));const out=compileProject(db,p,sha);console.log(args.includes('--json')?JSON.stringify(out.result,null,2):out.text);break;}
 default:console.log('BIGDIC\nnode cli.mjs audit\nnode cli.mjs search VERIFY\nnode cli.mjs show SIG-verify-P-external\nnode cli.mjs inspect "Verify exactly two sources"\nnode cli.mjs compile project.json [--json]');
 }
}catch(e){console.error(e.message);process.exitCode=1;}
