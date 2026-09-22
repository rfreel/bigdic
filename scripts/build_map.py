import re,json,hashlib,collections,html
from pathlib import Path
root=Path(__file__).resolve().parents[1]
bench=(root/'data/dictionary_benchmark.html').read_text(encoding='utf-8')
source=(root/'data/dictionary-v2.md').read_text(encoding='utf-8')
rows=json.loads(re.search(r'const rows=(\[.*?\]); const summary=',bench,re.S).group(1))
lex=source.split('## Lexical dictionary',1)[1]
heads=list(re.finditer(r'^### (.+?)\s*$',lex,re.M))
blocks={m.group(1):lex[m.end():heads[i+1].start() if i+1<len(heads) else len(lex)] for i,m in enumerate(heads)}
assert len(rows)==794 and len(blocks)>=794
family_defaults={
 'COMPILE':(4,5,5,3,'Frame'), 'ACQUIRE':(3,4,4,4,'Evidence'), 'INSPECT':(4,4,4,4,'Evidence'),
 'REPRESENT':(4,5,5,3,'Representation'),'SPLIT':(4,5,5,3,'Representation'),
 'EXPAND':(4,4,5,2,'Alternatives'),'COMPARE':(5,5,5,4,'Alternatives'),
 'INFER':(4,5,4,3,'Reasoning'),'CHALLENGE':(5,4,4,4,'Challenge'),
 'TEST':(5,4,4,5,'Challenge'),'UPDATE':(4,4,4,4,'State'),
 'EVALUATE':(5,5,4,4,'Decision'),'SELECT':(5,5,4,3,'Decision'),
 'TRANSFORM':(4,5,5,3,'Action'),'ACT':(5,5,5,3,'Action'),
 'VERIFY':(5,5,5,5,'Verification'),'CONTROL':(4,5,5,3,'Control'),
 'CLOSE':(3,4,3,3,'Closure'),'MODIFIER':(2,3,3,1,'Control'),
 'STATUS':(2,4,3,3,'State')}
# User-provided/locally compiled terms absent from V2. No historical-source attribution is inferred.
local={
 'ACCRETIVE':('CONTROL','State','Retain validated evidence and reusable capability so a fresh run benefits.'),
 'PREWALK':('CONTROL','Control','Simulate a plan’s dependencies, effects, and failure routes before execution.'),
 'DISINHIBITIZE':('CONTROL','Control','Remove an unsupported self-imposed restriction while retaining real constraints.'),
 'REIFY':('REPRESENT','Representation','Expose an object’s type, role, properties, relations, and boundaries.'),
 'RIVALIZE':('COMPARE','Alternatives','Expose a silent default, produce rival outputs, and seek a separator.'),
 'DOWN-COMPILE':('ACT','Action','Translate an abstract choice into concrete authorized actions.'),
 'LIFT':('UPDATE','State','Extract a reusable candidate rule from a local result and check its scope.'),
 'ACCRETE':('UPDATE','State','Add one supported capability to a durable versioned release.'),
 'BUILD':('ACT','Action','Create and check the requested artifact through an actual execution path.')}
# These dimensions are openly chosen default priors, not measured effects.
level_names=['Surface','Assessment','Typed move','Contextual sense','Macro','Control plane']
frontier_names=['Frame','Evidence','Representation','Alternatives','Reasoning','Challenge','Decision','Action','Verification','State','Control','Closure']

def score(item):
 ops=item['ops']; class_=item['kind']; sig=item['signatures']
 vec=[family_defaults[o][:4] for o in ops if o in family_defaults]
 if not vec: vec=[(2,3,2,2)]
 if class_=='STATUS_ASSESSMENT': vec=[(1,3,2,2)]
 # Strongest supported affordance on each dimension, not a sum of duplicate senses.
 d,t,c,e=(max(v[k] for v in vec) for k in range(4))
 base=4*(d+t+c+e)
 macro=8 if item['macro'] else 0
 sense=min(4,max(0,sig-1))
 ambiguity=min(12,3*max(0,sig-1))
 context=3 if item['context'] else 0
 authority=3 if item['authority'] else 0
 pseudo=10 if 'DANGEROUS_PSEUDO_STRENGTH' in item.get('axes','') else 0
 # bonuses reflect routing affordances; penalties reflect binding effort/risk.
 raw=base+macro+sense-ambiguity-context-authority-pseudo
 return dict(D=d,T=t,C=c,E=e,macro=macro,sense=sense,ambiguity=ambiguity,context=context,authority=authority,pseudo=pseudo,score=max(0,min(100,raw)))

def frontier(ops,bench_row=None):
 if bench_row and bench_row['benchmark_class']=='AXIS_BOUND_MODIFIER':return 'Control'
 if bench_row and bench_row['benchmark_class']=='STATUS_ASSESSMENT':return 'State'
 for o in ['VERIFY','TEST','CHALLENGE','ACT','SELECT','EVALUATE','COMPARE','EXPAND','REPRESENT','SPLIT','INSPECT','ACQUIRE','INFER','UPDATE','CONTROL','COMPILE','CLOSE']:
  if o in ops:return family_defaults[o][4]
 return 'Control'

def level(row):
 c=row['benchmark_class']
 if c=='AXIS_BOUND_MODIFIER':return 0
 if c=='STATUS_ASSESSMENT':return 1
 if c=='MACRO_WORKFLOW':return 4
 if c=='MULTI_SENSE':return 3
 if row['roles']=='family':return 5
 return 2

items=[]
for r in rows:
 name=r['canonical_term'];b=blocks.get(name,'')
 transitions=re.findall(r'^Transition or retained definition: (.*)$',b,re.M)
 # Include distinct retained descriptions, never treat one sense as every sense.
 transitions=list(dict.fromkeys(transitions))[:5]
 macro_expr=re.findall(r'^Macro source expression: `([^`]+)`',b,re.M)
 ops=r['operators'].split('|') if r['operators'] else []
 item=dict(id=r['lexeme_id'],name=name,origin='V2',ops=ops,frontier=frontier(ops,r),level=level(r),
           kind=r['benchmark_class'],roles=r['roles'],axes=r['axes'],signatures=r['signature_count'],
           context=r['requires_context_binding'],authority=r['requires_authority_or_effect_check'],
           requires_context_binding=r['requires_context_binding'],
           requires_authority_or_effect_check=r['requires_authority_or_effect_check'],
           evidence_bound=r['requires_evidence_status_check'],macro=('MACRO_WORKFLOW' in r['review_flags']),
           descriptions=transitions or ['No single transition extracted; inspect the contextual signatures.'],
           macro_expr=macro_expr,neighbor=r['nearest_neighbor'],neighbor_similarity=r['nearest_similarity'],
           source_lines=[r['line_start'],r['line_end']],flags=r['review_flags'])
 item.update(score(item));items.append(item)
for name,(op,fr,desc) in local.items():
 item=dict(id='LOCAL-'+name.lower(),name=name,origin='LOCAL',ops=[op],frontier=fr,
           level=4 if name in ['REIFY','RIVALIZE','PREWALK'] else 2,
           kind='LOCAL_PROPOSED',roles='local extension',axes='',signatures=1,context=True,authority=False,
           requires_context_binding=True,requires_authority_or_effect_check=False,
           evidence_bound=False,macro=name in ['REIFY','RIVALIZE','PREWALK'],descriptions=[desc],macro_expr=[],
           neighbor='',neighbor_similarity=None,source_lines=None,flags='NOT_IN_V2')
 item.update(score(item));items.append(item)
assert len(items)==803 and len({x['name'] for x in items})==803
byname={x['name']:x for x in items}
# Links: explicit macro token links, benchmark's text-neighbor relation, same-family sampled edges.
for x in items:
 x['macro_links']=[n for expr in x['macro_expr'] for n in re.findall(r'[A-Z][A-Z0-9-]+',expr) if n in byname and n!=x['name']]
 x['macro_links']=list(dict.fromkeys(x['macro_links']))
 x['same_family']=[n['name'] for n in items if n['origin']=='V2' and n['name']!=x['name'] and n['frontier']==x['frontier'] and n['level']==x['level']][:7]
 x['neighbor']=x['neighbor'] if x['neighbor'] in byname else ''
# reverse link count across actual macro composition, not invented mathematical equivalence.
reverse=collections.Counter(n for x in items for n in x['macro_links'])
for x in items:x['macro_inbound']=reverse[x['name']]
counts=collections.Counter((x['level'],x['frontier']) for x in items)
ranked=sorted(items,key=lambda x:(-x['score'],-x['macro_inbound'],x['name']))
for i,x in enumerate(ranked,1):x['rank']=i
# Data hygiene: HTML script cannot be broken by content from dictionary.
payload=json.dumps(items,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
count_cells=''.join(f'<tr><th>{html.escape(level_names[l])}</th>'+''.join(f'<td data-l="{l}" data-f="{f}" tabindex="0">{counts[(l,f)]}</td>' for f in frontier_names)+'</tr>' for l in range(6))
front_heads=''.join(f'<th>{html.escape(f)}</th>' for f in frontier_names)
source_hash=hashlib.sha256(source.encode()).hexdigest()
html_out='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Operator Dictionary: Linked Towers and Frontiers</title><style>
:root{--paper:#f5f6f3;--ink:#1b2b31;--muted:#53666e;--line:#c5d0d1;--sea:#174e5a;--light:#e7f0ef}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:15px/1.52 system-ui,-apple-system,sans-serif}header{background:#182c34;color:white;padding:32px max(18px,calc((100vw - 1200px)/2))}h1{font-size:clamp(2rem,5vw,3.5rem);letter-spacing:-.035em;line-height:1.06;margin:0}header p{color:#d6e4e4;max-width:78ch}main{max-width:1240px;padding:18px 18px 80px;margin:auto}h2{border-top:2px solid var(--ink);padding-top:17px;margin-top:46px;font-size:1.65rem}h3{font-size:1.13rem;margin-top:26px}p,li{max-width:88ch}a{color:#125464}.meta{display:flex;gap:8px;flex-wrap:wrap;margin:16px 0}.pill{background:#e5eded;border:1px solid var(--line);padding:5px 8px;font-size:.83rem}.panel{background:white;border:1px solid var(--line);padding:18px 21px;margin:16px 0}.key{border-left:5px solid var(--sea)}nav{display:flex;flex-wrap:wrap;gap:7px;margin:16px 0}nav a{padding:7px 9px;background:white;border:1px solid var(--line);text-decoration:none;font-size:.85rem}table{border-collapse:collapse;width:100%;background:white;font-size:.84rem}th,td{border:1px solid var(--line);padding:8px;text-align:left;vertical-align:top}th{background:#e4eceb}.scroll{overflow:auto;margin:14px 0}input,select,button{min-height:46px;padding:8px;font:inherit;border:1px solid #849a9e;background:white;color:var(--ink)}button{cursor:pointer}input{width:100%}.controls{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:8px}.tower{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}.tower article{padding:12px 15px;background:white;border-left:4px solid #366574}.tower strong{display:block}.tower small{color:var(--muted)}.tower .abyss{border-color:#9c473b}.tower .summit{border-color:#1e6f59}.matrix td{text-align:center;cursor:pointer;min-width:65px}.matrix th:first-child{position:sticky;left:0;z-index:1}.matrix td:hover{background:#d7e9e5}.ranked th{position:sticky;top:0}.ranked td:nth-child(1){white-space:nowrap}tr[hidden]{display:none}.score{font-weight:750;font-variant-numeric:tabular-nums}.detail{position:sticky;bottom:0;max-height:42vh;overflow:auto;border:2px solid var(--sea);background:#fff;box-shadow:0 -8px 30px #0002;padding:14px 20px;margin-top:18px;display:none}.detail.open{display:block}.detail h3{margin:0 0 9px}.chips{display:flex;flex-wrap:wrap;gap:5px}.chips button{min-height:36px;font-size:.83rem}.mono,code,pre{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}code{background:#e6eeee;padding:2px 3px}pre{background:#182e36;color:white;padding:13px;white-space:pre-wrap;overflow:auto}.legend{font-size:.86rem;color:var(--muted)}@media(max-width:750px){.controls{grid-template-columns:1fr 1fr}.controls input{grid-column:1/-1}.tower{grid-template-columns:1fr}.ranked td{min-width:115px}.ranked td:first-child{min-width:60px}.detail{max-height:48vh}main{padding:14px 12px 70px}header{padding:26px 17px}}@media print{.detail,.controls,nav{display:none!important}body{background:white}}
</style></head><body><header><h1>The operator towers</h1><p>803 linked words across abstraction levels, intervention frontiers, and an abyss-to-summit capability path. Complete V2 lexical index plus nine explicitly marked local extensions. Every entry receives a transparent default routing prior, never a fabricated measured effect.</p></header><main><nav><a href="#read">Read the towers</a><a href="#math">Proxy mathematics</a><a href="#grid">Orthogonal map</a><a href="#all">All 803 words</a><a href="#links">Link semantics</a></nav><div class="meta"><span class="pill">794 V2 lexical records</span><span class="pill">1,000 V2 signatures</span><span class="pill">9 local extensions</span><span class="pill">18 source operator families</span><span class="pill">6 abstraction floors × 12 frontiers</span></div>
<section id="read"><h2>1. Read the towers</h2><p><strong>There are three independent coordinates.</strong> Abstraction says what kind of instruction object the word denotes. Frontier says which part of work it changes. Altitude says how far an invocation has actually advanced from a label to durable, evidenced capability. A high proxy score does not raise altitude. Neither a hierarchy nor the source benchmark makes an entry empirically effective.</p><div class="tower"><article class="abyss"><strong>−2 · Abyss: fabricated upgrade</strong><small>A word is treated as an observed result, authority, proof, or universal optimum. Example: “VERIFY” in a prompt becomes “verified” without a checker.</small></article><article class="abyss"><strong>−1 · Hidden default trap</strong><small>One interpretation, candidate, or constraint is silently assumed and then reinforced by downstream operations.</small></article><article><strong>0 · Surface</strong><small>A word or modifier has a lexical entry. This is an address, not a performed operation.</small></article><article><strong>1 · Typed</strong><small>Sense, operands, context, and requirements are bound to this task. The V2 migration supplies candidate structures; every invocation still needs binding.</small></article><article><strong>2 · Composed</strong><small>Conditions, dependencies, and alternative continuations form an admissible macro program.</small></article><article><strong>3 · Executed</strong><small>The actual action ran. A receipt identifies the target, version, method, and observed effects.</small></article><article><strong>4 · Verified</strong><small>A checker established a scoped required property. A structural check establishes structure; an external claim needs matching evidence.</small></article><article class="summit"><strong>5 · Summit: accretive capability</strong><small>A durable implementation, tests, and receipts improve a fresh run after old chat or selector state is removed. Invalidations remain versioned.</small></article></div><div class="panel key"><strong>Sea level is a boundary, not a score.</strong> The source corpus reaches lexical and typed candidate descriptions. This map composes them and calculates a proxy. It does not move all 803 words to “executed,” “verified,” or “summit.”</div></section>
<section id="math"><h2>2. Proxy rating: reproducible and conditional</h2><p>The ranking answers: <em>under a default mix of general assistant tasks, which words look most worth routing to or composing?</em> It is a transparent prior, not a universal performance measurement. The user explicitly requested a proxy derived from defaults. The default gives equal weight to decision leverage D, cross-task transfer T, compositional reach C, and evidence or checking potential E. Each is an integer from 1 to 5 assigned to the V2 operator families. A multi-sense entry takes its strongest family value on each dimension; this is an upper-envelope prior, with an ambiguity penalty. It cannot manufacture measured success.</p><pre>proxy(w) = clip₀₋₁₀₀ [ 4(D + T + C + E)
  + 8·I(macro) + min(4, signatures−1)
  − min(12, 3·(signatures−1))
  − 3·I(context binding) − 3·I(authority/effect binding)
  − 10·I(pseudo-strength axis) ]</pre><p>Scores are ordinal sorting aids: a 78 is not “twice as effective” as 39. Ties are broken by the number of incoming explicit macro references, then alphabetically. A multi-sense word can score well because it reaches several frontiers while still needing costly disambiguation. A modifier can rank lower because it usually tunes another action rather than producing one alone. The formula and every component are visible when a word is selected.</p><p><strong>Changing the default changes the ranking.</strong> For a legal review, evidence and scope may dominate; for design, representation and expansion may matter more. No criterion in the source assigns these weights. The map therefore preserves each word’s family and level independently of its numerical order.</p><div class="panel"><strong>Exact mathematical scope:</strong> type compatibility, prerequisite reachability, finite-program dominance under declared criteria, and the score formula can be calculated. A causal improvement per word needs paired tasks, a comparator including plain-language substitution, an outcome checker, and a specified task population. The V2 benchmark's 100% structural integrity does not give those causal effects.</div></section>
<section id="grid"><h2>3. The orthogonal map</h2><p>Rows are abstraction levels, columns are intervention frontiers. A cell reports how many words have that primary placement. Click a cell to filter the complete table. An entry can reference more than one operator; its detail view preserves every source-mapped operator and links to its nearest textual neighbor and macro components.</p><div class="scroll"><table class="matrix"><thead><tr><th>Level ↓ / frontier →</th>__HEADS__</tr></thead><tbody>__CELLS__</tbody></table></div><p class="legend">Primary placement is a navigational projection of the recorded roles and operator families. It does not assert disjoint semantic categories or prove that words in the same cell are synonyms.</p></section>
<section id="all"><h2>4. Complete linked index</h2><div class="controls"><input id="q" placeholder="Search all words, descriptions, roles, families" aria-label="Search words"><select id="frontier" aria-label="Filter frontier"><option value="">All frontiers</option></select><select id="level" aria-label="Filter level"><option value="">All levels</option></select><select id="origin" aria-label="Filter origin"><option value="">All origins</option><option>V2</option><option>LOCAL</option></select></div><p id="count" class="legend"></p><div class="scroll"><table class="ranked"><thead><tr><th>Rank</th><th>Word</th><th>Proxy</th><th>Abstraction</th><th>Frontier</th><th>Source role / senses</th></tr></thead><tbody id="rows"></tbody></table></div><div id="detail" class="detail" role="region" aria-live="polite"></div></section>
<section id="links"><h2>5. What the links mean</h2><div class="scroll"><table><thead><tr><th>Link</th><th>Evidence</th><th>What it permits</th></tr></thead><tbody><tr><td>Word → operator family</td><td>V2 source-mapped signature, or marked local proposal</td><td>Navigate a possible typed transition; bind context before action</td></tr><tr><td>Macro → component word</td><td>Explicit workflow expression extracted from V2</td><td>Follow a recorded composition; do not infer it executed</td></tr><tr><td>Word → nearest neighbor</td><td>V2 benchmark textual similarity</td><td>Find a review candidate; does not establish semantic equivalence</td></tr><tr><td>Word → same placement</td><td>Shared primary frontier and abstraction level</td><td>Browse adjacent entries; does not assert synonymy</td></tr><tr><td>Operation → verified capability</td><td>Would require execution plus property-matched receipt</td><td>No such link is automatically granted by this map</td></tr></tbody></table></div><p>“Full map” here means every one of the 794 V2 lexical records is represented once, plus the nine named extensions. It does not mean all English words or every conceivable future macro. The HTML uses no network resources and can be filtered offline.</p></section>
<section><h2>Provenance and limits</h2><p>Source: <em>data/dictionary-v2.md</em>, SHA-256 <code>__SHA__</code>; V2 benchmark table, 794 rows. Extracted descriptions are retained source transitions, up to five per word, not generated semantic completions. Nine LOCAL terms were compiled from the current conversation and the prior Rising Sea document; their presence in the V2 corpus is explicitly denied. Source line ranges refer to the V2 working draft. This map does not claim empirical per-word lift, semantic saturation, or a proof of globally optimal prompt behavior.</p></section></main><script>
const data=__DATA__;
const levels=__LEVELS__,frontiers=__FRONTIERS__;
const byName=new Map(data.map(x=>[x.name,x]));const q=document.getElementById('q'),fs=document.getElementById('frontier'),ls=document.getElementById('level'),os=document.getElementById('origin'),table=document.getElementById('rows'),detail=document.getElementById('detail');
function safe(s){return String(s??'').replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;')}
for(const x of frontiers)fs.add(new Option(x,x));for(let i=0;i<levels.length;i++)ls.add(new Option(levels[i],String(i)));
function button(name){return `<button type="button" data-word="${safe(name)}">${safe(name)}</button>`}
function show(x){if(!x)return;const comp=x.macro_links.map(button).join('')||'No explicit macro component links';const nearby=x.same_family.map(button).join('')||'None in this sample';const near=x.neighbor?button(x.neighbor)+` <small>text similarity ${x.neighbor_similarity}</small>`:'None recorded';detail.innerHTML=`<button id="closeDetail" type="button" style="float:right">Close</button><h3>${safe(x.name)} <small>rank ${x.rank} / 803</small></h3><p><strong>Proxy ${x.score}/100</strong> · ${safe(levels[x.level])} · ${safe(x.frontier)} · ${safe(x.origin)} · ${safe(x.kind)} · ${x.signatures} signature(s)</p><p><strong>Components:</strong> D ${x.D}, T ${x.T}, C ${x.C}, E ${x.E}; macro +${x.macro}, sense +${x.sense}; ambiguity −${x.ambiguity}, context −${x.context}, authority −${x.authority}, pseudo-strength −${x.pseudo}.</p><p><strong>Recorded operators:</strong> ${safe(x.ops.join(', '))}. <strong>Roles:</strong> ${safe(x.roles)}. <strong>Modifier axes:</strong> ${safe(x.axes||'none')}.</p><p><strong>Retained transitions:</strong></p><ol>${x.descriptions.map(v=>`<li>${safe(v)}</li>`).join('')}</ol><p><strong>Explicit macro components:</strong></p><div class="chips">${comp}</div><p><strong>Nearest textual neighbor:</strong> ${near}</p><p><strong>Same tower/frontier sample:</strong></p><div class="chips">${nearby}</div><p class="legend">${x.source_lines?'V2 lines '+x.source_lines.join('–'):'Local addition, absent from V2'}. Flags: ${safe(x.flags||'none')}. ${x.macro_inbound} incoming explicit macro references. No execution or empirical gain inferred.</p>`;detail.classList.add('open');detail.querySelector('#closeDetail').onclick=()=>detail.classList.remove('open');detail.scrollIntoView({block:'nearest'});}
function render(){const search=q.value.trim().toLowerCase();let filtered=data.filter(x=>(!fs.value||x.frontier===fs.value)&&(!ls.value||x.level===Number(ls.value))&&(!os.value||x.origin===os.value)&&(!search||[x.name,x.roles,x.frontier,x.ops.join(' '),x.descriptions.join(' ')].join(' ').toLowerCase().includes(search)));filtered.sort((a,b)=>a.rank-b.rank);document.getElementById('count').textContent=`${filtered.length} / ${data.length} words`;table.innerHTML=filtered.map(x=>`<tr><td>${x.rank}</td><td><button type="button" data-word="${safe(x.name)}">${safe(x.name)}</button></td><td class="score">${x.score}</td><td>${safe(levels[x.level])}</td><td>${safe(x.frontier)}</td><td>${safe(x.roles)} / ${x.signatures}</td></tr>`).join('')}
for(const x of [q,fs,ls,os])x.addEventListener('input',render);document.addEventListener('click',e=>{const b=e.target.closest('[data-word]');if(b)show(byName.get(b.dataset.word))});for(const td of document.querySelectorAll('.matrix td')){const go=()=>{ls.value=td.dataset.l;fs.value=td.dataset.f;render();document.getElementById('all').scrollIntoView()};td.onclick=go;td.onkeydown=e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();go()}}}render();
</script></body></html>'''
html_out=html_out.replace('__HEADS__',front_heads).replace('__CELLS__',count_cells).replace('__DATA__',payload).replace('__LEVELS__',json.dumps(level_names)).replace('__FRONTIERS__',json.dumps(frontier_names)).replace('__SHA__',source_hash)
out=root/'docs/operator-towers.html';out.write_text(html_out,encoding='utf-8')
catalog={'schema_version':'0.1.0','source_file':'dictionary-v2.md',
         'source_sha256':source_hash,'status':'INDEXED_NOT_BEHAVIORALLY_VERIFIED','entries':items}
(root/'data/catalog.json').write_text(json.dumps(catalog,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
print(json.dumps({'path':str(out),'bytes':out.stat().st_size,'records':len(items),'source':len(rows),'local':len(local),'top':[(x['name'],x['score'],x['frontier']) for x in ranked[:18]],'levels':dict(collections.Counter(level_names[x['level']] for x in items)),'matrix_total':sum(counts.values())}))
