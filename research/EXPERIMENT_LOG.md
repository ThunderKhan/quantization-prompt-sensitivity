# Experiment Log

This file records protocol decisions, experiment runs, failures, and changes.

## 2026-09-21 — Project initialization

- Repository created and made public.
- Initial working question selected.
- Local inference target: `qwen3:0.6b` through Ollama.
- Initial pilot designed as a software sanity check.
- Important observation: the interactive Ollama session had thinking enabled and produced unstable/incorrect arithmetic reasoning. The automated runner therefore uses the Ollama API with thinking disabled and temperature 0 for the initial pilot.
- No scientific conclusion was drawn from this observation.

## 2026-09-22 — Evaluator hardening

- The first automated pilot completed successfully but reported 0.000 accuracy.
- Because raw responses had not yet been inspected, the 0.000 score was **not interpreted as a model result**.
- The evaluator was changed from strict whole-response equality to an auditable numeric-token evaluator for the arithmetic sanity check.
- Exact-match evaluation remains available via `--evaluation-mode exact`.
- The raw response, normalized response, extracted candidate answers, and evaluation mode are now recorded.
- This is a pipeline correction, not a scientific result.

## Protocol revisions

Use this format for every substantive revision:

### [DATE] — [CHANGE]

**Change:**

**Reason:**

**Affected files:**

**Does this change invalidate previous results?**

- [ ] Yes
- [ ] No

## Experiment runs

Use this format for every completed run:

### Run: [RUN_ID]

**Date/time UTC:**

**Commit SHA:**

**Experiment configuration:**

**Model:**

**Precision:**

**Dataset/version:**

**Prompt-set version:**

**Temperature:**

**Seed:**

**Hardware/software:**

**Result file:**

**Notes:**

## Failed runs

Do not delete failed runs from this log.

Record what failed, why, and whether any outputs should be excluded from analysis.
