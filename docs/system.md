# The agent's control tower

## The governing question

At any point, an agent must be able to answer: **What result is required? What is actually known? What can I do now? What observation would change the decision? What should the next fresh agent inherit?** Everything in this repository serves those five questions. A component that cannot change a continuation, preserve a needed distinction, or reduce future work should be removed or made optional.

The system is a conditional program over typed states, plus an append-only record of what really happened. The vocabulary is its index. The user supplies intent in ordinary language; an agent drives the machine.

## The linked abstraction tower

| Floor | Object | Admission condition | Common failure |
| --- | --- | --- | --- |
| Abyss −2 | False upgrade | Never admissible | Generated text called evidence or authority |
| Abyss −1 | Hidden default | Must be exposed when answer-changing | One reading silently becomes fact |
| 0 | Surface word | Source and spelling identified | More names mistaken for more capability |
| 1 | Bound sense | Input, context, roles, invariants specified | Polysemy silently collapsed |
| 2 | Conditional program | Prerequisites, branches, budget and effects expressed | Fixed checklist despite different observations |
| 3 | Executed action | Actual target and receipt recorded | Planned operation called performed |
| 4 | Verified result | Property-matched checker and scope retained | Structural check inflated to real-world proof |
| 5 | Accreted capability | Fresh agent can reconstruct and reuse it | Success lives only in old context |

**Abstraction**, **intervention frontier**, and **evidence altitude** are independent coordinates. A high-leverage word can remain unexecuted. A well-verified local action can be low-level. The [interactive index](operator-towers.html) displays the first two axes for all 803 entries and explains the third without fabricating per-entry promotion.

The [consequence map](consequence-map.html) is a separate parametric model. It organizes candidate moves by the result they could change and the facts needed to admit them. It does not use the V2 inventory or its family score to select the terms. The old tower rating cannot establish that one word dominates another under a task objective.

## Runtime state

Let `S=(goal,requirements,evidence,observations,rivals,artifacts,obligations,authority,budget,environment)`. An operator is a partial typed transition `o:(S,input,context)->(S',output,receipt|failure)`. It carries preconditions, read and write effects, protected invariants, and a failure continuation. A macro is a conditional composition, not a mandatory verb sequence.

A valid `o2 ∘ o1` requires compatible output and input types, satisfied preconditions, preserved invariants, and an admissible next action. When these cannot be established, branch, inspect, or stop. Do not invent a coercion. A task may have several admissible programs; compare them under the user's criteria, retaining a Pareto frontier if no ordering governs the tradeoff.

`packet` currently performs lexical candidate retrieval and returns `PROPOSED`. It is intentionally not an autonomous worker. The first production runtime must add: context binding; competing sense selection; dependency planning; tool dispatch; observed effect reconciliation; property-matched verification; and durable evidence writeback. Each new layer needs a contract and independent failure cases.

## Rising Sea

The evidence sea appends accepted attempts, including failed or blocked ones. The capability projection recomputes versioned applicable passes from that history. The shoreline is the set of unverified capabilities whose prerequisites are verified. Work targets the shoreline when it improves user outcomes, not merely because the graph contains another node.

```text
user request → bounded task state → candidate operator program
              ↓ execution, observation and check
        append-only attempt and receipt history
              ↓ deterministic versioned projection
        currently verified capability DAG
              ↓ minimal useful open successors
                  next agent action
```

A historical pass is immutable evidence. Its current applicability can decline when model, source, environment, checker, or contract changes; append a new invalidation. A score or reward may prioritize work but cannot promote truth. A fresh agent with the durable assets, and without an old conversation or learned selector, must be able to do better on matched tasks before claiming compounding capability.

## Semantic links

The catalog keeps source role, all recorded operator families, contextual signature count, source transition text, macro expressions when present, and local provenance. Four different links are shown in the UI: explicit macro component, nearest textual neighbor, common projected placement, and operator-family membership. Textual similarity never establishes equivalent behavior. A semantic equivalence merge requires a declared objective, continuation domain, and checked observation basis.

## Routing objective

For the current task, retain the vector `(requirement fit, correct outcome, preserved distinctions, evidential support, robustness, −cost, −latency, −side effects)`. A candidate dominates another only if it is no worse on each protected dimension and better on at least one. Exact optimization is possible in a finite model with a specified objective and complete transitions. The UI's 0–100 proxy is a conditional navigation prior; it is neither this task's utility nor an empirical effect size.

The expected work sequence is to bind the user's intended result, inspect current state, expose alternatives that would change action, choose a discriminating observation where useful, execute the smallest adequate action, check the actual result, and save durable evidence. Skip a stage when it cannot change the result. Add a stage when an observed dependency requires it.

## Coherence boundaries

- Dictionary text is source evidence about a proposed operator, not an authorization or a behavioral result.
- The planner may propose; the executor reports actual effects; the checker assesses a scoped property; the controller promotes only on a governing receipt.
- These boundaries prevent one model-generated paragraph from serving as proposal, execution report, and verification at once.
- A failed operation invalidates only claims dependent on it; independent supported work persists.
- User-facing explanations expose actionable uncertainty and actual limitations, not the entire internal state tree.
- Mutable views, cached rankings, and dashboards are reproducible projections. They are not historical authority.

## Repository layout and ownership

`data/catalog.json` is the current source-indexed snapshot; `operator_system.py` is the small baseline command surface; `docs/operator-towers.html` is a standalone exploratory projection; `AGENTS.md` is the operating contract; `docs/benchmarks.md` owns metrics and claims; `TODO.md` owns sequencing. Subsequent implementations should separate state models, router, executor adapters, checker interface, event store, and projection only when a tested transition requires it. Do not create a forest of empty modules.
