# bigdic

`bigdic` is an executable operator dictionary and measurement workspace. This branch adds **Operator Compiler v1** and the first **BiggestDic** expansion layer: a transparent state-conditioned controller plus provider-neutral causal experimentation over the 18 canonical operator families.

## What is implemented

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
  -> provider-neutral causal backends
  -> lexeme / pair / triple experiment frontier
```

The epistemic kernel is not optimized away. Source distinctions, authority/capability boundaries, unresolved branches, and external evidence boundaries remain explicit.

## Evidence lanes

- `FINITE_EXACT`: deterministic operator measurements under `data/measurements/`.
- `REPLAY`: deterministic provider-neutral causal fixtures used by GitHub Actions.
- `LOCAL_TRANSFORMERS`: isolated GitHub-hosted CPU inference. It downloads open weights directly and does not use Hugging Face Jobs.
- `OPENAI_COMPATIBLE`: optional OpenRouter, Groq, and Gemini-compatible transports when their API-key environment variables are supplied.

Hugging Face Jobs previously returned HTTP 402 before inference. That transport is no longer required. The old failed attempt remains historical evidence, not a global blocker.

## Current verified finite results

- 18/18 common contracts compiled
- 72 conditional value cells
- 195 mined motifs
- 20 induced macros with positive marginal deletion value
- 80 planner/workflow evaluations, 80/80 covering required operators
- 216 counterfactual replay rows
- 18/18 canonical controller self-consistency selections
- 20/20 original compiler tests passing before the BiggestDic extension
- provider-neutral backend/frontier tests added under `tests/test_backends.py`
- independent GitHub Actions verification enabled

These are implementation and finite-model results, not evidence of universal cross-model generalization.

## BiggestDic expansion

See `docs/BIGGESTDIC.md`.

The expansion hierarchy is:

```text
18 families
-> 794 lexemes
-> 1,000 signatures
-> parameter bindings
-> ordered pairs
-> ordered triples
-> conditional macros
-> candidate residual operators
```

`import_lexeme_manifest.py` consumes the exhaustive dictionary benchmark and refuses a source that does not contain exactly 794 lexemes. `frontier.py` preserves operator order for pair/triple experiments and provides a transparent structural prior until empirical EVSI can replace it.

## Layout

```text
data/
  contracts_seed.json
  dictionary_provenance.json
  measurements/
src/operator_compiler/
  contracts.py
  state.py
  value.py
  interactions.py
  motifs.py
  budget.py
  replay.py
  transfer.py
  external.py
  backends.py
  experiments.py
  frontier.py
  planner/
  runtime/controller.py
scripts/
  build_artifacts.py
  import_lexeme_manifest.py
  run_local_model_smoke.py
results/
tests/
.github/workflows/
  ci.yml
  external-local.yml
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
