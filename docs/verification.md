# Verification record

Revision: toolkit 0.1.0, 2026-09-15.

## Executed

- Node test suite: 18 passed, 0 failed. Full receipt: `receipts/tests.txt`.
- Parser audit: 794 lexical records, 1,000 signatures, 20 inherited contracts. Every signature retains an exact source span.
- SHA-256 comparison against the uploaded source passed. Bundled source text equals the original text.
- Single-file build completed; extracted JavaScript passed `node --check`.
- CLI example compilation produced `BOUND_DRAFT` and `NOT_EXECUTED`, preserving the difference between supplied fields and executed work.

Tests cover ambiguity, intersecting facets, nested lexical matches, Unicode offsets, deterministic compilation, malformed input, source mismatch, and journal tampering and truncation. Structural coverage is not semantic completeness.

## Failed probes and corrections

The first test run had 17 passes and one failed test fixture: it expected an expression absent from the dictionary. The fixture was corrected to the source's actual `independent evidence` expression. No unsupported alias was added. The subsequent 18-test run passed.

Browser navigation to the local preview was blocked. A local Playwright fallback lacked a Chromium executable; its download timed out and was cancelled. The browser's file URL policy also rejected navigation. No workaround was attempted after that explicit policy rejection.

## Unresolved

Rendered layout, browser interaction, clipboard, downloads, localStorage, and multi-tab behavior have not been verified in a running browser. The visual concept is a design reference, not a screenshot or test receipt. CI execution is not claimed by this local record.

Status: IMPLEMENTED; automated checks EXECUTED and passed within their stated scope. Browser validation remains BLOCKED. No independent verification, generalized semantic guarantee, or closure certification is claimed.

## Reopen triggers

A failing test, source revision, parser omission, malformed export, lost history event, browser failure, or evidence of meaning lost in compilation requires reopening the affected claim while preserving independent results.
