# Limitations

## 1. Small models

Early experiments focus on small models for practical compute reasons. Results should not automatically be generalized to frontier-scale models.

## 2. Model family dependence

If the main experiment uses primarily one model family, architecture and training-family effects remain unresolved.

## 3. Quantization-method dependence

“4-bit” or “8-bit” is not a complete description of a quantized model. Quantization algorithm, calibration, backend, and format can affect behavior.

## 4. Prompt-equivalence validation

Semantics-preserving transformations are difficult to guarantee automatically. Human validation reduces the risk but does not eliminate it.

## 5. Benchmark dependence

A small set of task datasets cannot characterize all LLM use cases.

## 6. Local inference environment

Latency and some runtime measurements may depend on the specific machine, backend, drivers, and software versions.

## 7. Deterministic decoding

A temperature-0 pilot isolates prompt effects from sampling variability, but it does not characterize stochastic generation behavior.

## 8. Evaluator limitations

Automatic answer extraction can introduce errors. Task-specific evaluation should be inspected manually on a sample.

## 9. Statistical power

The one-month scope may limit the number of models, tasks, and repeated measurements. The final manuscript should report the actual sample sizes and uncertainty rather than implying broad generality.

## 10. Literature gap uncertainty

The current literature review is preliminary. The final paper must avoid a “first study” claim unless a sufficiently comprehensive search supports it.
