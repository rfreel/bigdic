# 100-check review record

These are 100 distinct source and projection checks on this revision. They are not 100 optimization cycles, behavioral trials, or a proof of task performance. The source samples cover 60 evenly spaced alphabetical entries; the 20 score samples cover evenly spaced ranks. Other checks cover whole collections. A passing sample does not certify every source span.

| # | Check | Result |
| ---: | --- | --- |
| 001 | Source digest matches catalog | PASS |
| 002 | 794 V2 records | PASS |
| 003 | Nine local records | PASS |
| 004 | 803 unique names | PASS |
| 005 | 803 unique record IDs | PASS |
| 006 | 1,000 V2 signatures | PASS |
| 007 | All ranks form one permutation | PASS |
| 008 | Every score is within 0–100 | PASS |
| 009 | Generated page has 803 records | PASS |
| 010 | Generated page has source hash | PASS |
| 011 | Source span 01: A/B-TEST | PASS |
| 012 | Source span 02: ADAPT | PASS |
| 013 | Source span 03: ALL | PASS |
| 014 | Source span 04: ARCHIVE | PASS |
| 015 | Source span 05: ATTRIBUTE | PASS |
| 016 | Source span 06: BARE-MINIMUM | PASS |
| 017 | Source span 07: BRANCH-CLOSE | PASS |
| 018 | Source span 08: CANONICAL-LEXICAL-OR-NUMERIC-ORDERING | PASS |
| 019 | Source span 09: CHAIN | PASS |
| 020 | Source span 10: CLOSURE-COMPLETE | PASS |
| 021 | Source span 11: COMPLETENESS | PASS |
| 022 | Source span 12: CONSIDER-EVERYTHING | PASS |
| 023 | Source span 13: COPY | PASS |
| 024 | Source span 14: CRAWL | PASS |
| 025 | Source span 15: DECIDE | PASS |
| 026 | Source span 16: DELETE | PASS |
| 027 | Source span 17: DESCRIPTION | PASS |
| 028 | Source span 18: DIFF | PASS |
| 029 | Source span 19: DIVERGENT | PASS |
| 030 | Source span 20: ECONOMICAL | PASS |
| 031 | Source span 21: EQUIVALENCE-CHECK | PASS |
| 032 | Source span 22: EXAMINE | PASS |
| 033 | Source span 23: EXPLAIN-CAUSALLY | PASS |
| 034 | Source span 24: FALSIFICATION-FIRST | PASS |
| 035 | Source span 25: FLEXIBLE | PASS |
| 036 | Source span 26: FORMALLY-VERIFIED | PASS |
| 037 | Source span 27: GENERATE | PASS |
| 038 | Source span 28: HARVEST | PASS |
| 039 | Source span 29: IF | PASS |
| 040 | Source span 30: INDEPENDENT-REPRODUCTION | PASS |
| 041 | Source span 31: INSPECT | PASS |
| 042 | Source span 32: INVALIDATE | PASS |
| 043 | Source span 33: LEAVE-NO-STONE-UNTURNED | PASS |
| 044 | Source span 34: LOW-COST | PASS |
| 045 | Source span 35: MECHANISM-HYPOTHESIS | PASS |
| 046 | Source span 36: MODIFY | PASS |
| 047 | Source span 37: NEVER-STOP-UNTIL-PERFECT | PASS |
| 048 | Source span 38: ONE-SOURCE-CLASS | PASS |
| 049 | Source span 39: ORTHOGONAL-VERIFY | PASS |
| 050 | Source span 40: PAUSE | PASS |
| 051 | Source span 41: PREDICATE-BY-PREDICATE | PASS |
| 052 | Source span 42: PROFESSIONAL | PASS |
| 053 | Source span 43: QUERY | PASS |
| 054 | Source span 44: RECOGNIZE | PASS |
| 055 | Source span 45: REGRESSION-TEST | PASS |
| 056 | Source span 46: RESEARCH | PASS |
| 057 | Source span 47: REVIEW | PASS |
| 058 | Source span 48: ROBUSTIFY | PASS |
| 059 | Source span 49: SATURATION-LEVEL | PASS |
| 060 | Source span 50: SENSITIVITY-ANALYSIS | PASS |
| 061 | Source span 51: SLICE | PASS |
| 062 | Source span 52: SPLIT | PASS |
| 063 | Source span 53: STRONGLY-PREFER | PASS |
| 064 | Source span 54: SYSTEM-TEST | PASS |
| 065 | Source span 55: TEST | PASS |
| 066 | Source span 56: TRANSACTIONAL | PASS |
| 067 | Source span 57: ULTRA-TERSE | PASS |
| 068 | Source span 58: UNTIL-NO-ANSWER-CHANGING-DEEPER-DISTINCTION-REMAINS | PASS |
| 069 | Source span 59: VISUALIZE | PASS |
| 070 | Source span 60: ZERO-DEVIATION-CONSTRAINT | PASS |
| 071 | Proxy recomputation 01: AUDIT | PASS |
| 072 | Proxy recomputation 02: DEPLOY | PASS |
| 073 | Proxy recomputation 03: LINT | PASS |
| 074 | Proxy recomputation 04: EXPORT | PASS |
| 075 | Proxy recomputation 05: BATCH | PASS |
| 076 | Proxy recomputation 06: ENCODE | PASS |
| 077 | Proxy recomputation 07: PROOFREAD | PASS |
| 078 | Proxy recomputation 08: UNTIL | PASS |
| 079 | Proxy recomputation 09: AUTONOMOUS-ON-REVERSIBLE-WORK | PASS |
| 080 | Proxy recomputation 10: COSTLY-ROLLBACK | PASS |
| 081 | Proxy recomputation 11: EXACTLY | PASS |
| 082 | Proxy recomputation 12: INDEPENDENT-IMPLEMENTATION | PASS |
| 083 | Proxy recomputation 13: NO-VERIFICATION | PASS |
| 084 | Proxy recomputation 14: RIGOR | PASS |
| 085 | Proxy recomputation 15: TESTED-MECHANISM | PASS |
| 086 | Proxy recomputation 16: CORRECT | PASS |
| 087 | Proxy recomputation 17: EXHAUSTIVE-WHERE-MATERIAL | PASS |
| 088 | Proxy recomputation 18: ACQUIRE | PASS |
| 089 | Proxy recomputation 19: NORMAL | PASS |
| 090 | Proxy recomputation 20: UNRESOLVED | PASS |
| 091 | No V2 claim on local records | PASS |
| 092 | V2 spans present | PASS |
| 093 | No broken neighbor targets | PASS |
| 094 | No broken macro targets | PASS |
| 095 | No self macro links | PASS |
| 096 | No duplicate macro links | PASS |
| 097 | Incoming macro counts agree | PASS |
| 098 | Same-placement targets agree | PASS |
| 099 | No self placement links | PASS |
| 100 | Ties use inbound links then name | PASS |

Run `python3 scripts/audit_100.py` from any directory. The source and generated index also require a byte-for-byte regeneration check before release.
