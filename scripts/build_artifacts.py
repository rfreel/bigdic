from __future__ import annotations
import csv, json
from pathlib import Path
from dataclasses import asdict

from operator_compiler.budget import BudgetAllocator
from operator_compiler.contracts import OPERATORS, compile_contracts
from operator_compiler.external import external_evidence_state
from operator_compiler.interactions import InteractionModel
from operator_compiler.measurements import MeasurementStore
from operator_compiler.motifs import mine_motifs, induce_macros
from operator_compiler.planner.greedy import GreedyPlanner
from operator_compiler.planner.beam import BeamPlanner
from operator_compiler.planner.astar import AStarPlanner
from operator_compiler.planner.branch_bound import BranchBoundPlanner
from operator_compiler.replay import counterfactual_replay
from operator_compiler.runtime.controller import OperatorController
from operator_compiler.state import OperatorState
from operator_compiler.transfer import evaluate_transfer
from operator_compiler.value import ValueEstimator, ApplicabilityModel

ROOT=Path(__file__).parents[1]
DATA=ROOT/'data'
M=DATA/'measurements'
OUT=ROOT/'results'
OUT.mkdir(exist_ok=True)
store=MeasurementStore.from_directory(M)
est=ValueEstimator(store)
inter=InteractionModel(store)
app=ApplicabilityModel()

# 1/2 contracts and state schema
contracts=compile_contracts(DATA/'contracts_seed.json')
(OUT/'contracts.json').write_text(json.dumps({k:v.to_dict() for k,v in contracts.items()},indent=2,sort_keys=True)+'\n')
state_schema={
  '$schema':'https://json-schema.org/draft/2020-12/schema',
  'title':'OperatorState','type':'object','required':['target','objective','budget'],
  'properties':{
    'target':{'type':'string'},'objective':{'type':'string'},
    'live_alternatives':{'type':'array','items':{'type':'string'}},
    'evidence':{'type':'array','items':{'type':'string'}},
    'decision_partition':{'type':'array','items':{'type':'array','items':{'type':'string'}}},
    'requirements':{'type':'array','items':{'type':'string'}},
    'discriminators':{'type':'array','items':{'type':'string'}},
    'budget':{'type':'number','minimum':0},
    'authority':{'type':'array','items':{'type':'string'},'uniqueItems':True},
    'capabilities':{'type':'array','items':{'type':'string'},'uniqueItems':True},
    'history':{'type':'array','items':{'enum':list(OPERATORS)}},
    'representation':{'type':'string'},'closure_state':{'type':'string'},
    'required_operators':{'type':'array','items':{'enum':list(OPERATORS)}}
  }
}
(OUT/'state_schema.json').write_text(json.dumps(state_schema,indent=2)+'\n')

# 3-7 conditional tensor across canonical states
states={
 'UNRESOLVED_DISCRIMINATOR':OperatorState(target='benchmark',objective='resolve',live_alternatives=('a','b'),decision_partition=(('a',),('b',)),discriminators=('probe',),budget=2.0,authority=frozenset({'read','test','act'}),capabilities=frozenset({'inspect','test','verify'})),
 'UNRESOLVED_NO_DISCRIMINATOR':OperatorState(target='benchmark',objective='resolve',live_alternatives=('a','b'),decision_partition=(('a',),('b',)),budget=2.0,authority=frozenset({'read','test','act'}),capabilities=frozenset({'inspect','test','verify'})),
 'RESOLVED_OPEN':OperatorState(target='benchmark',objective='close',live_alternatives=('a',),decision_partition=(('a',),),budget=2.0,authority=frozenset({'read','test','act'}),capabilities=frozenset({'inspect','test','verify'})),
 'SOLVED':OperatorState(target='benchmark',objective='done',live_alternatives=('a',),decision_partition=(('a',),),budget=2.0,authority=frozenset({'read','test','act'}),capabilities=frozenset({'inspect','test','verify'}),closure_state='SOLVED'),
}
with (OUT/'conditional_value_tensor.csv').open('w',newline='') as f:
    w=csv.writer(f); w.writerow(['state','operator','applicability','marginal_gain','cost','marginal_net','voc_net','evsi_net'])
    for sname,s in states.items():
        for op in OPERATORS:
            m=est.marginal_value(op,s); voc=est.value_of_computation(op,s); evsi=est.evsi(op,s)
            w.writerow([sname,op,app.assess(op,s).status,m.expected_gain,m.expected_cost,m.net_value,voc.net_value,evsi.net_value])

# 8/9 motifs and induced macros
motifs=mine_motifs(M/'chain_search.csv',2,4)
(OUT/'motifs.json').write_text(json.dumps([{'sequence':list(x.sequence),'support':x.support} for x in motifs],indent=2)+'\n')
macros=induce_macros(M/'chain_search.csv',M/'marginal_deletion_value.csv')
(OUT/'induced_macros.json').write_text(json.dumps([{'macro_id':x.macro_id,'sequence':list(x.sequence),'measured_value':x.measured_value,'min_deletion_value':x.min_deletion_value} for x in macros],indent=2)+'\n')

# 10 planner comparison over every source workflow
planners=[GreedyPlanner(est,inter),BeamPlanner(est,inter),AStarPlanner(est,inter),BranchBoundPlanner(est,inter)]
macro_rows=[]
with (M/'chain_search.csv').open(newline='') as f:
    for r in csv.DictReader(f):
        required=tuple(dict.fromkeys(x.strip() for x in r['required'].split('->') if x.strip()))
        s=OperatorState(target=f"macro:{r['macro_id']}",objective='workflow',required_operators=required,budget=10.0)
        source=tuple(x.strip() for x in r['required'].split('->') if x.strip())
        source_value=store.sequence_value(source)
        for p in planners:
            pr=p.plan(s)
            macro_rows.append([r['macro_id'],p.name,' -> '.join(pr.sequence),pr.total_value,pr.total_cost,source_value,set(required).issubset(pr.sequence)])
with (OUT/'planner_comparison.csv').open('w',newline='') as f:
    w=csv.writer(f); w.writerow(['macro_id','planner','sequence','net_value','cost','source_sequence_value','covers_required']); w.writerows(macro_rows)

# 11 budget frontier
budget_state=states['UNRESOLVED_DISCRIMINATOR']
frontier=BudgetAllocator(est).frontier(budget_state)
with (OUT/'budget_frontier.csv').open('w',newline='') as f:
    w=csv.writer(f); w.writerow(['rank','operator','net_value','cost','value_per_cost'])
    for i,x in enumerate(frontier,1): w.writerow([i,x.operator,x.expected_value,x.expected_cost,x.value_per_cost])

# 12 counterfactual replay for source workflows
replay_rows=[]
with (M/'chain_search.csv').open(newline='') as f:
    for r in csv.DictReader(f):
        seq=tuple(x.strip() for x in r['required'].split('->') if x.strip())
        rr=counterfactual_replay(seq,store)
        for i,d in enumerate(rr.deletions): replay_rows.append([r['macro_id'],'delete',i,' -> '.join(d.variant),d.delta])
        for i,d in enumerate(rr.reorderings): replay_rows.append([r['macro_id'],'swap_adjacent',i,' -> '.join(d.variant),d.delta])
with (OUT/'counterfactual_replay.csv').open('w',newline='') as f:
    w=csv.writer(f); w.writerow(['macro_id','kind','position','variant','delta']); w.writerows(replay_rows)

# 13 transfer
tr=evaluate_transfer(M/'transfer_by_regime.csv')
(OUT/'transfer_summary.json').write_text(json.dumps({'by_regime':tr.by_regime,'transfer_ratio':tr.transfer_ratio,'sign_reversal_rate':tr.sign_reversal_rate},indent=2)+'\n')

# 14 external boundary
ext=external_evidence_state(store)
(OUT/'external_evidence_state.json').write_text(json.dumps(asdict(ext),indent=2)+'\n')

# 15 controller benchmark for all 18 required-operator states
ctl=OperatorController(store)
controller_rows=[]
for op in OPERATORS:
    unresolved=op!='CLOSE'
    s=OperatorState(target=f'need:{op}',objective='select_next',live_alternatives=('a','b') if unresolved else ('a',),decision_partition=(('a',),('b',)) if unresolved else (('a',),),discriminators=('probe',) if op in {'ACQUIRE','INSPECT','TEST','VERIFY'} else (),budget=2.0,authority=frozenset({'read','test','act'}),capabilities=frozenset({'inspect','test','verify'}),required_operators=(op,))
    n=ctl.next(s)
    controller_rows.append([op,n.operator,n.operator==op,n.expected_value,n.expected_cost,'|'.join(n.evidence_basis)])
with (OUT/'controller_eval.csv').open('w',newline='') as f:
    w=csv.writer(f); w.writerow(['required','chosen','correct','expected_value','expected_cost','evidence_basis']); w.writerows(controller_rows)

# Report
correct=sum(1 for r in controller_rows if r[2])
planner_cover=sum(1 for r in macro_rows if r[-1])
report=f'''# Operator Compiler v1 Report\n\n## Scope\n\nTransparent state-conditioned controller over the 18 dictionary operator families using the frozen finite/deterministic measurement artifacts. External model evidence remains separate and is not imputed.\n\n## Generated evidence\n\n- Compiled contracts: {len(contracts)}/18\n- Canonical conditional states: {len(states)}\n- Conditional value cells: {len(states)*len(OPERATORS)}\n- Mined motifs: {len(motifs)}\n- Induced macros with positive deletion value: {len(macros)}\n- Planner workflow evaluations: {len(macro_rows)}\n- Planner evaluations covering all required operators: {planner_cover}/{len(macro_rows)}\n- Counterfactual replay rows: {len(replay_rows)}\n- Controller required-operator selections correct: {correct}/{len(controller_rows)}\n- External model lane: {ext.status}; trials executed={ext.trials_executed}\n\n## Evidence boundary\n\nThe runtime estimates are transparent transformations of FINITE_EXACT measurements and source-derived macro structure. They are not evidence that the same conditional values transfer to arbitrary models or real-world domains. The external causal lane is retained as `{ext.status}`.\n'''
(OUT/'REPORT.md').write_text(report)
print(report)
