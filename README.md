# bigdic

`bigdic` is an executable operator dictionary and measurement workspace. This branch adds **Operator Compiler v1**, a transparent state-conditioned controller over the 18 canonical operator families in the Dictionary V2 working draft.

## What is implemented

The compiler turns the dictionary and frozen measurement artifacts into:

```text
Dictionary V2
  -> typed operator contracts
  -> OperatorState IR
  -> applicability model
  -> marginal value / VOC / EVSI estimators
  -> conditional interaction model
  -> motif + macro induction
  -> greedy / beam / A* / branch-and-bound planners
  -> adaptive budget frontier
  -> counterfactual replay
  -> cross-regime transfer report
  -> runtime controller
```

The epistemic kernel is not optimized away. Source distinctions, authority/capability boundaries, unresolved branches, and the external evidence boundary remain explicit.

## Evidence status

Operator Compiler v1 is grounded in the previously executed **FINITE_EXACT** operator measurement lane. The external causal-model lane remains `BLOCKED_EXTERNAL_MODEL`: Hugging Face Jobs returned HTTP 402 before inference, so model trials executed = 0. The controller never imputes that missing evidence.

Current generated report:

- 18/18 common contracts compiled
- 72 conditional value cells
- 195 mined motifs
- 20 induced macros with positive marginal deletion value
- 80 planner/workflow evaluations, 80/80 covering required operators
- 216 counterfactual replay rows
- 18/18 canonical controller self-consistency selections
- 20/20 tests passing

These are implementation and finite-model results, not evidence of universal cross-model generalization.

## Layout

```text
data/
  contracts_seed.json       normalized source-derived contract seed
  dictionary_provenance.json full dictionary hash and extraction provenance
  measurements/           frozen measurement inputs
src/operator_compiler/
  contracts.py             dictionary -> typed common contracts
  state.py                 OperatorState IR
  value.py                 applicability, marginal value, VOC, EVSI
  interactions.py          conditional pair/order effects
  motifs.py                motif mining and macro induction
  budget.py                value-per-cost frontier
  replay.py                deletion/reordering counterfactuals
  transfer.py              regime-separated transfer metrics
  external.py              external evidence boundary
  planner/                 greedy, beam, A*, branch-and-bound
  runtime/controller.py    next-operation policy
scripts/build_artifacts.py reproducible evidence generation
results/                   compiled contracts and benchmark outputs
tests/                     15-task coverage and invariants
```

## Run

```bash
python -m pytest -q
PYTHONPATH=src python scripts/build_artifacts.py
python -m compileall -q src tests scripts
```

## Runtime example

```python
from pathlib import Path
from operator_compiler.measurements import MeasurementStore
from operator_compiler.runtime.controller import OperatorController
from operator_compiler.state import OperatorState

store = MeasurementStore.from_directory(Path("data/measurements"))
controller = OperatorController(store)

state = OperatorState(
    target="candidate decision",
    objective="resolve",
    live_alternatives=("A", "B"),
    decision_partition=(("A",), ("B",)),
    discriminators=("probe",),
    budget=2.0,
    authority=frozenset({"read", "test"}),
    capabilities=frozenset({"inspect", "test", "verify"}),
)

step = controller.next(state)
print(step.operator, step.expected_value, step.expected_cost)
```

The returned `NextStep` includes alternatives, bindings, the current discriminator, a stopping rule, and evidence provenance.
