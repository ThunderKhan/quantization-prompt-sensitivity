# Research Question

## Working Title

**Does Quantization Amplify Prompt Sensitivity in Small Language Models?**

### Proposed subtitle

*A Controlled Study of Semantics-Preserving Prompt Perturbations*

## Central Research Question

Does lower-precision inference increase the sensitivity of small language models to semantics-preserving changes in prompt wording?

## Research Questions

### RQ1
Do semantics-preserving prompt variations change task performance?

### RQ2
Which types of prompt perturbations cause the greatest instability?

### RQ3
Does quantization increase prompt sensitivity?

### RQ4
Can standard average accuracy hide substantial prompt instability?

## Initial Hypotheses

**H1.** Semantics-preserving prompt variations will produce measurable performance differences.

**H2.** Different perturbation categories will produce different levels of sensitivity.

**H3.** Lower-precision models will exhibit greater prompt sensitivity.

**H4.** Average task accuracy will not completely characterize prompt robustness.

These are empirical hypotheses. The study must be able to support, reject, or fail to resolve them.

## Initial Metrics

### Accuracy

`accuracy = correct / total`

### Prompt spread

`ΔA = max(A_p) - min(A_p)`

where `A_p` is accuracy for prompt variant `p`.

### Item flip rate

Fraction of items whose correctness changes across at least two prompt variants.

### Robust accuracy

Fraction of items answered correctly under **all** prompt variants.

## Experimental principle

The dependent task must remain fixed while prompt wording changes.

Prompt transformations should be categorized and validated rather than generated ad hoc.

## Important threats to validity

- A model may fail because of limited capability rather than prompt sensitivity.
- Sampling randomness can be confused with prompt effects.
- Supposedly equivalent prompts may not actually be semantically equivalent.
- Lower accuracy after quantization does not by itself prove increased prompt sensitivity.
- Dataset contamination and benchmark artifacts can affect results.

## Current pilot

The pilot intentionally uses one very simple arithmetic item to validate the software pipeline.

It is **not** evidence for or against the research hypotheses.
