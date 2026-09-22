# Benchmark and trajectory contract

The current repo has structural checks, not evidence of task-level gain. The 794 V2 rows, nine local additions, score recomputation, and candidate-only routing checks are implemented. The numerical tower rating is a declared default prior for browsing, never an observed performance value per word.

## Unit and treatments

A run is one fresh request, treatment, model/tool environment, and seed if available. Keep stable task ID, request and criterion hashes, authorized effects, source revisions, chosen program, actual tool receipts, evaluator method, raw outcome, cost, exclusions, and failure reason. Split development, held-out, and untouched replication before inspecting outcomes. When a held-out case informs a revision, retire it from held-out use.

Compare: normal assistant baseline; equivalent short plain-language instructions; dictionary candidate routing; typed-program routing; typed program plus retained Rising Sea assets; single-move ablations; order changes; meaningless sham terms; ambiguous readings; and complete label replacement with ordinary language. Isolate conversation state. Pair runs on the same task when possible. Blind human judges to condition. Use deterministic oracles for exact artifacts and code.

## Scorecard

All targets below are aspirations to be preregistered before trials, not completed results. Report raw counts, task-stratified paired differences, uncertainty intervals, cost, and severe exceptions. Preserve multiobjective tradeoffs.

| Measure | Definition | 30-day target | 180-day target |
| --- | --- | --- | --- |
| Task success | Required output passes independently frozen acceptance | ≥75% across 60 diverse tasks | ≥90% across 200 new tasks |
| Lift over plain language | Paired accepted-result difference | Positive estimate, interval reported | Lower interval bound >0 on untouched replication |
| False completion | Claimed delivered/verified without matching receipt | Zero severe failures in pilot | ≤0.5% across ≥1,000 audited runs |
| Wrong-sense routing | Answer-changing sense selected incorrectly | ≤10% of 30 ambiguity fixtures | ≤2% of 100 new ambiguity cases |
| Requirement recall | Applicable mandatory constraints retained | ≥95% in compiler packet | ≥99% in protected task strata |
| Distinction retention | Consequential rivals retained to discrimination/common action | ≥90% | ≥98% |
| Unauthorized effect | Protected action without an actual grant | Zero in targeted tests | Zero observed, with exposure count reported |
| Verification correspondence | Checked property, target, and revision match claim | ≥95% | ≥99% |
| Fresh-agent lift | Paired success after deleting old selector and context | Record three reset runs | Positive lower interval bound across three fresh agents |
| Repair durability | Original and adjacent failure stay fixed | ≥80% in first repeat | ≥95% at 30-day follow-up |
| Cost per success | Tokens, calls, time, and money per accepted task | ≤1.2× baseline | ≥25% below baseline without more severe failures |
| First useful observation | Time until answer-changing evidence arrives | Establish baseline | ≥30% lower median on matched tasks |
| User steering | Clarifying turns and required code words | Zero required code words | ≥50% fewer corrective turns |
| Reopen precision | Dependent stale results reopened, independent work retained | ≥90% on fixture set | ≥98% after source/environment changes |
| Coverage | Distinct failure families with discriminating fixtures | ≥20 | ≥80, with marginal contribution recorded |
| Calibration | Claimed confidence matches observed correctness | Reliability diagram | No persistent overconfidence by task stratum |

Include facts, research, ambiguous interpretation, code repair, document delivery, multiobjective choice, external effects, conflicting evidence, do-nothing, and adversarial cases. Report failures and missing runs; never silently discard them. Repeat on day 90 with a new 200-task suite, day 180 with fresh agents and no old chat or selector, and day 365 under changed model/tool versions. Evaluate severe regressions separately from mean gain.

## Admission to a claim

A typed signature can be structurally checked. A finite policy can be proved optimal only for its complete declared transition model and objective. A word's causal effect needs an explicit comparator, paired observations, and a specified task distribution. Macro interaction requires combinations, not standalone scores. A PASS receipt promotes only the checked property under its versioned context. A reward cannot promote truth. Stop a lane when another run cannot change its declared decision within budget; preserve and name the remaining uncertainty.

## Run-record analyzer

`python3 benchmarks/evaluate.py runs.jsonl` consumes observed JSONL records with stable `task_id`, `condition`, `domain`, `provenance`, nullable `success` and `false_completion`, and nonnegative `input_tokens`, `output_tokens`, `tool_calls`, and `wall_seconds`. It reports per-condition counts, false completions, median costs, complete paired success differences with seeded bootstrap intervals when at least two pairs exist, and all missing or unresolved pairs. It rejects empty, duplicated, malformed, or domain-mismatched observations. A report does not certify randomized assignment or reliable judging; those are separate protocol requirements.
