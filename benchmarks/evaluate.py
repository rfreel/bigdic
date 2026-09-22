"""Analyze real paired run records. Synthetic examples must be labeled separately.

Input: JSONL with one row per task and condition. This script never generates
responses or treats the dictionary's proxy ratings as observed performance.
"""
from __future__ import annotations
import argparse, collections, json, random, statistics
from pathlib import Path

REQUIRED = {'task_id','condition','domain','success','false_completion',
            'input_tokens','output_tokens','tool_calls','wall_seconds','provenance'}

def load(path: Path):
    records={}
    for number,line in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
        if not line.strip():continue
        try: row=json.loads(line)
        except json.JSONDecodeError as e:raise ValueError(f'line {number}: invalid JSON: {e}') from e
        missing=REQUIRED-row.keys()
        if missing:raise ValueError(f'line {number}: missing {sorted(missing)}')
        if row['success'] not in (True,False,None) or row['false_completion'] not in (True,False,None):
            raise ValueError(f'line {number}: invalid result type')
        for key in ('input_tokens','output_tokens','tool_calls','wall_seconds'):
            value=row[key]
            if not isinstance(value,(int,float)) or isinstance(value,bool) or value<0:
                raise ValueError(f'line {number}: invalid {key}')
        if not all(isinstance(row[k],str) and row[k] for k in ('task_id','condition','domain','provenance')):
            raise ValueError(f'line {number}: unbound identity or provenance')
        key=(row['task_id'],row['condition'])
        if key in records:raise ValueError(f'line {number}: duplicate task-treatment record {key}')
        records[key]=row
    if not records:raise ValueError('No observations: no score can be calculated')
    return records

def interval(values,seed=20260922,reps=2000):
    """Percentile paired bootstrap; undefined if fewer than two complete pairs."""
    if len(values)<2:return None
    rng=random.Random(seed)
    samples=sorted(sum(rng.choice(values) for _ in values)/len(values) for _ in range(reps))
    return [samples[int(.025*(reps-1))],samples[int(.975*(reps-1))]]

def analyze(records,baseline='baseline',candidate='candidate'):
    bycondition=collections.defaultdict(list)
    for row in records.values():bycondition[row['condition']].append(row)
    summary={}
    for condition,rows in sorted(bycondition.items()):
        known=[r for r in rows if r['success'] is not None]
        false=[r for r in rows if r['false_completion'] is True]
        summary[condition]={'runs':len(rows),'known_outcomes':len(known),
            'missing_outcomes':len(rows)-len(known), 'successful':sum(r['success'] for r in known),
            'success_rate':sum(r['success'] for r in known)/len(known) if known else None,
            'false_completion_count':len(false),
            'median_total_tokens':statistics.median(r['input_tokens']+r['output_tokens'] for r in rows),
            'median_tool_calls':statistics.median(r['tool_calls'] for r in rows),
            'median_wall_seconds':statistics.median(r['wall_seconds'] for r in rows)}
    ids=sorted({t for t,c in records if c in (baseline,candidate)})
    complete=[];missing=[];incomplete=[]
    for task in ids:
        a=records.get((task,baseline));b=records.get((task,candidate))
        if not a or not b:missing.append(task);continue
        if a['success'] is None or b['success'] is None:incomplete.append(task);continue
        if a['domain']!=b['domain']:raise ValueError(f'Domain mismatch on task {task}')
        complete.append((task,a,b))
    differences=[int(b['success'])-int(a['success']) for _,a,b in complete]
    domain={}
    for d in sorted({a['domain'] for _,a,_ in complete}):
        v=[int(b['success'])-int(a['success']) for _,a,b in complete if a['domain']==d]
        domain[d]={'pairs':len(v),'mean_success_difference':sum(v)/len(v),
                   'paired_interval':interval(v)}
    return {'conditions':summary,'paired':{'baseline':baseline,'candidate':candidate,
        'complete_pairs':len(complete),'missing_partner_task_ids':missing,
        'unresolved_outcome_task_ids':incomplete,
        'mean_success_difference':sum(differences)/len(differences) if differences else None,
        'paired_interval':interval(differences),'by_domain':domain},
        'method':'Observed outcomes only; seeded percentile bootstrap of complete task pairs; no causal inference without controlled assignment'}

def main():
    p=argparse.ArgumentParser();p.add_argument('input',type=Path)
    p.add_argument('--baseline',default='baseline');p.add_argument('--candidate',default='candidate')
    a=p.parse_args();print(json.dumps(analyze(load(a.input),a.baseline,a.candidate),indent=2,sort_keys=True))
if __name__=='__main__':main()
