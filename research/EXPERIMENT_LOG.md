# Experiment Log

This file records protocol decisions, experiment runs, failures, and changes.

## 2026-09-21 — Project initialization

- Repository created and made public.
- Initial working question selected.
- Local inference target: `qwen3:0.6b` through Ollama.
- Initial pilot designed as a software sanity check.
- Important observation: the interactive Ollama session had thinking enabled and produced unstable/incorrect arithmetic reasoning. The automated runner therefore uses the Ollama API with thinking disabled and temperature 0 for the initial pilot.
- No scientific conclusion was drawn from this observation.

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
