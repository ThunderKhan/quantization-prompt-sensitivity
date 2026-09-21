# Discussion

## Status

This document is a scaffold for interpretation after the main experiments are complete.

## Questions to answer

### 1. What changed under quantization?

Does precision change:

- average task accuracy,
- prompt spread,
- item flip rate,
- robust accuracy,
- output agreement?

### 2. Is the effect general or task-specific?

Do the observed effects hold across task families, or are they concentrated in a particular capability?

### 3. Is the effect practically meaningful?

A statistically detectable difference is not automatically operationally important.

Discuss effect magnitude and deployment relevance separately.

### 4. Does model size modify the effect?

Within any model family tested, examine whether sensitivity differs by model size without assuming a monotonic relationship.

### 5. What alternative explanations remain?

Consider:

- base model capability,
- decoding behavior,
- tokenizer differences,
- quantization method,
- evaluator artifacts,
- prompt-validation errors,
- benchmark contamination,
- hardware/runtime differences.

## Interpretation rule

Do not claim that quantization *causes* a specific internal mechanism unless the experiment directly measures that mechanism.

The default language should be observational:

> “Under the tested configurations, quantization was associated with ...”

rather than mechanistic unless supported by evidence.

## Potential practical implication

If average accuracy remains similar while prompt stability changes materially, local-model deployment evaluations may benefit from robustness measurements in addition to standard benchmark scores.

Whether that implication holds will depend on the final evidence.
