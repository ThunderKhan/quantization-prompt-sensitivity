# Hypotheses

## Primary hypotheses

### H1 — Prompt sensitivity exists

Semantics-preserving prompt variations will produce measurable variation in task performance for at least some model/task combinations.

### H2 — Perturbation categories differ

Different perturbation categories will not produce identical sensitivity profiles.

### H3 — Quantization changes sensitivity

Changing inference precision will change prompt sensitivity after controlling for the model/task configuration.

### H4 — Accuracy is insufficient

Aggregate accuracy will not fully describe prompt robustness; models/configurations with similar mean accuracy can differ in cross-prompt stability.

## Optional exploratory hypotheses

These are exploratory and should not be elevated to primary hypotheses without sufficient power and evidence.

### H5 — Smaller models are more variable

Within a single model family, smaller models may show larger cross-prompt variation.

### H6 — Reasoning-heavy tasks are more sensitive

Tasks requiring multi-step reasoning may show greater prompt-induced instability than simpler tasks.

## Null possibilities

The study must explicitly allow:

- no measurable prompt sensitivity,
- no meaningful difference between perturbation categories,
- no quantization effect on prompt sensitivity,
- quantization lowering accuracy without changing sensitivity,
- quantization changing sensitivity only for particular tasks or models.

## Hypothesis discipline

Before running the full experiment, we will define:

- primary outcome metrics,
- comparison groups,
- statistical tests,
- exclusion criteria,
- sample sizes.

These decisions should not be changed after inspecting the main results except through a documented protocol revision.
