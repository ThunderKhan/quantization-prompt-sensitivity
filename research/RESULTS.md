# Results

## Status

**No scientific results yet.**

The repository currently contains only pipeline-validation code and an initial pilot configuration.

## How results will be reported

Results should be reported in layers.

### 1. Descriptive performance

For every model/configuration:

- mean accuracy,
- accuracy by prompt variant,
- prompt spread,
- item flip rate,
- robust accuracy.

### 2. Quantization comparison

Compare each quantized condition with its higher-precision reference.

Report:

- absolute accuracy difference,
- change in prompt spread,
- change in flip rate,
- change in robust accuracy,
- confidence intervals,
- effect sizes where appropriate.

### 3. Perturbation analysis

Break down sensitivity by:

- lexical,
- syntactic,
- formatting,
- framing,
- other validated categories.

### 4. Error analysis

Inspect representative disagreement cases.

The final paper should distinguish:

- wrong under every prompt,
- correct under every prompt,
- correct under some prompts and wrong under others.

## Result integrity rules

- Raw outputs are authoritative.
- Derived tables must be reproducible from raw outputs.
- No favorable subset selection.
- No result should appear in the manuscript before being traced to a recorded experiment run.

## Planned figures

1. Accuracy by precision.
2. Prompt spread by precision.
3. Robust accuracy by model/configuration.
4. Sensitivity by perturbation category.
5. Accuracy versus stability.
6. Item-level disagreement examples, where useful.
