# Consequence-first operator map

The old tower ranked words using weights assigned to their dictionary families. That score measures its own formula. It cannot tell whether a proposed move changes a claim, decision, authorization, artifact, or stopping condition. A high-ranked word could merely ask for more prose. The [consequence map](consequence-map.html) starts with the change a move would have to make and includes the supplied frontier and domain vocabulary as a working proposal. V2 membership does not select or rank its terms.

## What an operator must bind

For a task state `S`, a candidate move has a type, operands, precondition, method, possible observation, permitted state change, failure state, and cost. A word alone supplies none of the missing bindings. Distinguish five common roles:

| Role | Example | What admission requires |
| --- | --- | --- |
| Intervention | `SEVERE-TEST` | A claim, risky prediction, test method, and possible result that would count against the claim |
| Decision rule | `KILL-CRITERION` | A criterion fixed before seeing the result, an owner, and the action it licenses |
| Constraint | `PRECONDITION-LOCK` | The exact action, required condition, observation method, and effect if the condition fails |
| State label | `INCONCLUSIVE` | The checked property, scope, and evidence that leaves the question unresolved |
| Technical concept | `DO-CALCULUS`, `STARE-DECISIS`, `NNT` | The field's actual assumptions and method; a borrowed name does not execute that method |

The domain panels are vocabulary lenses. Several of their entries name measures, doctrines, conditions, or failure modes, rather than actions. Moving them into a generic prompt as verbs would lose the conditions that give them meaning. Newly combined labels in the map are mnemonic handles; they are not established technical terms by virtue of appearing here.

## High-use handles for general agent work

These are useful when their stated condition holds. The rows are arranged by the work they affect, not by a universal score.

| Handle | Consequential change | Required basis |
| --- | --- | --- |
| `SUCCESS-PREDICATE` | Turns an open request into a checkable output contract | The user's actual goal and protected requirements |
| `COUNTERMODEL` | Keeps a materially different account live | It fits the current observations and changes a possible output |
| `CRUX` | Finds where live rivals require different continuations | Rival predictions and a reachable discriminator |
| `INCOMPATIBLE-PREDICTION` | Exposes a test that cannot confirm both rivals under the same assumptions | A common measurement method and a stated auxiliary basis |
| `FALSIFIER` | Names a result that would defeat a scoped claim | Claim, scope, and rejection rule fixed before observation |
| `SEVERE-TEST` | Runs a test capable of producing that result | Valid method, meaningful failure opportunity, and actual observation |
| `INDEPENDENT-WITNESS` | Cuts a shared error path | Distinct acquisition and failure dependencies, not just a different model name |
| `REVERSAL-CONDITION` | Keeps a commitment responsive to new evidence | A specific event, owner, and changed decision |
| `INVARIANT-ENFORCE` | Blocks an action outside a protected boundary | An observable precondition and enforced stop or recovery behavior |
| `IDEMPOTENT-APPLY` | Makes a repeated action converge on the same target state | Identity key, duplicate-effect check, and external side-effect analysis |
| `INVALIDATE-DOWNSTREAM` | Reopens dependent claims after a changed basis | Versioned dependency edges and the exact change |
| `SCOPED-PASS` | Permits only the claim actually checked | Matched property, target revision, checker, and retained receipt |
| `REOPEN-PREDICATE` | Gives a closed result a concrete future trigger | A detectable condition and the claims it invalidates |

`FALSIFIER` is a specified defeating result; `SEVERE-TEST` is an attempted observation; `KILL-CRITERION` is a decision rule. None entails the other without a binding. `INCONCLUSIVE` and `CEREMONIAL-DONE` are state or failure labels, not commands. Their separation matters more than where they rank in a word list.

## Conditional dominance

Say `a` dominates `b` only after binding the same task and protected criteria. Both must be admissible. For each live interpretation and required outcome, `a` must preserve mandatory constraints and do at least as well on the governing dimensions, with a strict improvement somewhere. Cost, delay, reversibility, harm, and evidential strength matter when the task makes them governing. If these comparisons are unavailable or trade off, keep both on the frontier. A word cannot dominate another merely by being more specific, more severe, or higher in this document.

For example, a specified `SEVERE-TEST` can dominate generic `REVIEW` when the task is to retire a risky claim, the claim has a precommitted failure criterion, and the test can discriminate it at acceptable cost. If the review would discover a missing safety requirement that the proposed test ignores, dominance is not established. A `STOPPING-RULE` can bound expenditure without establishing the truth of a claim. `AUTHORIZE` describes a decision governed by an actual grant; typing it confers no authority.

## A stronger composition

1. State the exact claim or required output and its governing criteria.
2. Represent the live hypotheses and the set of acceptable actions under each, including protected constraints.
3. If the intersection of those sets contains an acceptable action, treat it as a robust candidate. Check authorization, acceptance, and bounded effects; separately assess whether an available probe could change the decision or materially improve its outcome.
4. Probe when it is admissible, within budget, can change a decision-relevant outcome, and its expected or bounded benefit justifies its cost. If the comparison is unknown, preserve the uncertainty rather than treating a shared action as proof that probing is wasteful.
5. If no common acceptable action exists, find a crux: an observation for which the live classes require different continuations.
6. Set a discriminating test and its failure, inconclusive, and stop conditions before observing the outcome. Choose a severe test when retiring a claim is the governing job.
7. Run only an available, authorized test. Keep the raw observation, method, and scope.
8. Update the live alternatives. If the result licenses disposition, record the rule and its owner; otherwise retain the unresolved alternatives.
9. Carry a reopen predicate into the result. A later source, environment, or contract change triggers only the dependent recheck.

Write `A(h)` for actions that satisfy the request and protected constraints if live hypothesis `h` is true. When `⋂ A(h)` is nonempty, the intersection supplies a candidate robust action; it does not establish that acting now is optimal. Probe value depends on whether information can change a governed decision, the consequences and reversibility of acting under uncertainty, and probe cost. A numeric value-of-information estimate requires a probability model, utility, and probe cost. Without them, use explicit bounds or qualitative comparisons, retain incomparable options, and defer when the unresolved comparison matters. The reusable `continuation.choose_continuation` helper applies this conservative policy and returns a recommendation only; callers still own evidence, authority, execution, and result checking.

The 12 [parametric additions](consequence-map.html#additions) name useful missing cuts such as `DECISION-PARTITION`, `ASSUMPTION-CUTSET`, and `INVALIDATION-CONE`. They are proposed composite handles. Their presence does not establish novelty, empirical gain, or universal superiority.

## Three corrections to the supplied wording

- `DISAMBIGUATE-TO-EXHAUSTION` would require an exhaustive universe. For an open-world request, use **disambiguate until the remaining interpretations lead to the same action**, or record the live branch and its discriminator.
- `ROLLBACK-GUARANTEE` is a claim that needs a tested restore path, including side effects outside the artifact. Without that receipt, call it a **rollback plan**.
- `NO-INFORMATION-LOSS` must name the task-relevant distinctions and the inverse or witness that preserves them. A projection generally drops information; it may still be sufficient for a declared decision.
- Closure needs an acceptance predicate, residual uncertainty, and a reopen trigger. The relative cost of reopening alone cannot certify a result. `CEREMONIAL-DONE` is a failure label, not a completion procedure.

## Current implementation boundary

The map is a browsable parametric classification. Its lanes describe the job a term could do, not a per-term empirical effect, executable semantic contract, universal ordering, or promotion to verified capability. The original 803-entry [V2 index](operator-towers.html) remains available for source study, with its numerical prior clearly separate from this map. The current `operator_system.py` router still makes lexical proposals only.
