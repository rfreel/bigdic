# Agent instructions

Your first duty is to fulfill the user's ordinary-language request. Do not make them learn dictionary terms or operate this system. The dictionary and router are aids to your judgment, not authority over the request.

## On entry

1. Read `README.md` and run `python3 operator_system.py check` if using the catalog. Inspect only the words and source senses needed for the current task. Do not load all 803 entries into context.
2. State the required result and its external effects. Identify actual tools, authority, constraints, and current evidence. The presence of a verb never grants a tool or permission.
3. Use `packet REQUEST` only to discover candidate moves. It is a lexical baseline and can miss the right macro. Bind an operator's task-specific operands and outcome test yourself.
4. Prefer an available action that advances the user's result. Remove self-imposed requirements unsupported by the request. Preserve constraints that actually govern it.
5. Inspect real outputs. When an action fails, retain its effects and replan from observed state. Do not turn a plan, fixture, structural check, or simulated result into a completion claim.
6. Return the requested result and the few remaining distinctions that could change it. Save only durable repairs, examples, traces, checkers, and source-linked lessons.

## State and evidence

Keep separate: request, candidate interpretations, selected program, executed actions, observations, checks, decisions, and durable promotion. Use a versioned source basis and stable task identifiers. A changed basis invalidates only dependent conclusions. A failed probe is not evidence that its hypothesis was false.

For each consequential action record: request ID, target and revision, input and output, tool/method, time, cost where known, observed side effects, checker, scope, and unresolved alternatives. Never imply a tool call ran because a macro mentions it.

A capability can be called verified only for the exact target property, environment, checker, and contract version established by a retained receipt. Current applicability may expire while the historical receipt remains intact. No arbitrary word score promotes capability.

## Working set and stopping

Use the smallest working set that can change the outcome. Follow explicit macro links and neighboring senses only when a live distinction warrants them. Search wider when a missing alternative could change an action. Stop when further work cannot change the requested result within the user's scope or the declared budget. Do not stop at a proposal when the user authorized doing the work.

Keep user-facing terminology plain. `REIFY`, `RIVALIZE`, `PREWALK`, and `DISINHIBITIZE` are optional internal handles, not required incantations. New coined terms must be labeled LOCAL and defined by their actual transition.

## Changes to this repository

Treat `data/catalog.json` as a versioned source-indexed snapshot. Recompute its digest and every proxy value from the scoring rule when changing it. Never silently reclassify V2 source text as a measured result. Preserve the 794-to-9 provenance partition or document a versioned migration.

Change architecture, implementation, benchmarks, and agent instructions together when a new transition crosses their boundaries. Run `python3 -m unittest discover -s tests -v`. Run `python3 operator_system.py check`. Report the exact checks and their scope, plus unexecuted gates. Publication or deployment needs observed delivery evidence.
