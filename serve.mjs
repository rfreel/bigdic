import {createServer} from 'node:http';
import {readFile} from 'node:fs/promises';
const file=new URL('./dist/bigdic.html',import.meta.url);const port=Number(process.env.PORT||4173);
createServer(async(req,res)=>{if(!['GET','HEAD'].includes(req.method)){res.writeHead(405);res.end();return;}try{const content=await readFile(file);res.writeHead(200,{'Content-Type':'text/html; charset=utf-8','Cache-Control':'no-store','X-Content-Type-Options':'nosniff'});res.end(req.method==='HEAD'?undefined:content);}catch{res.writeHead(503);res.end('Run npm run build first.');}}).listen(port,'127.0.0.1',()=>console.log('BIGDIC http://127.0.0.1:'+port));
