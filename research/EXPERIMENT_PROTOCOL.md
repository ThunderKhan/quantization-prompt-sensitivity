# Experiment Protocol

## Status

**Draft protocol — pilot stage**

This protocol will be revised after the software pilot and literature review, with revisions recorded in the experiment log.

## Objective

Measure whether semantics-preserving prompt perturbations cause performance variation in small language models, and test whether inference precision changes that variation.

## Independent variables

### 1. Model

Initial model:

- `qwen3:0.6b`

Candidate final model family:

- Qwen small-model variants, subject to hardware and availability.

### 2. Inference precision

Candidate conditions:

- higher-precision reference,
- 8-bit,
- 4-bit.

The exact formats/tooling must be locked before the final experiment because different quantization methods at the same nominal bit-width are not necessarily equivalent.

### 3. Prompt perturbation

Initial categories:

- lexical,
- syntactic,
- politeness,
- framing,
- formatting.

Only transformations judged to preserve task meaning will enter the final evaluation set.

### 4. Task

Initial task families:

- mathematical reasoning,
- instruction following,
- code generation.

The final task set will be narrowed if the pilot shows that a task family cannot be evaluated reliably.

## Controlled variables

Keep fixed within each comparison:

- model checkpoint,
- tokenizer,
- system prompt,
- task item,
- prompt content outside the perturbation,
- decoding parameters,
- seed where supported,
- maximum output length,
- stop behavior,
- evaluation code,
- hardware/software environment where possible.

## Pilot

### Stage 0 — software sanity check

One simple arithmetic question × five prompts.

Purpose: verify the pipeline.

**Evaluation note:** Stage 0 uses a task-specific numeric-token evaluator. It records both the extracted candidate numbers and the complete raw response. This evaluator is not sufficient for the final multi-task experiment.

### Stage 1 — small pilot

20 task items × five prompt variants.

Purpose:

- identify bad prompt transformations,
- estimate runtime,
- discover evaluator failures,
- inspect output variability,
- validate raw-result storage.

### Stage 2 — protocol lock

After Stage 1, freeze:

- prompt templates,
- item sample,
- evaluation rules,
- model configurations,
- decoding settings,
- output schema.

### Stage 3 — primary experiment

Candidate design:

`3 model sizes × 3 precision conditions × 3 task families × N items × K prompt variants`

The exact N and K will be set after pilot runtime and power considerations are evaluated.

## Prompt construction

Prompts should be generated from explicit transformation rules where possible.

Example:

**Base:**

> Calculate the result of the following problem: {QUESTION}

**Lexical variant:**

> Determine the result of the following problem: {QUESTION}

**Syntactic variant:**

> What is the result for the following problem? {QUESTION}

The task semantics must remain constant.

Human validation should be used on a sample of prompt pairs. Reviewers independently judge whether the variants request the same task.

## Decoding

Initial pilot:

- temperature = 0.0,
- seed = 0 where supported,
- thinking disabled for the Ollama Qwen pilot.

The final protocol may include a separate stochastic robustness experiment, but deterministic inference is the first priority.

## Primary outcome measures

1. Mean task accuracy.
2. Prompt spread.
3. Item flip rate.
4. Robust accuracy.

Secondary outcomes:

- response length,
- latency,
- token usage where available,
- output agreement.

## Statistical analysis

Candidate analyses:

- paired comparisons across prompt variants,
- bootstrap confidence intervals,
- McNemar tests for paired correctness outcomes,
- regression or mixed-effects models for factorial analyses.

The exact primary statistical model will be locked after the final experimental design is known.

## Quantization comparison

A quantized condition should be compared against a higher-precision reference using the same:

- prompts,
- items,
- decoding settings,
- evaluator,
- hardware/software measurement procedure as far as practical.

We should not attribute general accuracy loss to increased prompt sensitivity without separately measuring stability.

## Reproducibility

Every generation should retain:

- run ID,
- timestamp,
- model identifier,
- precision identifier,
- prompt ID,
- task/item ID,
- exact prompt text,
- decoding parameters,
- raw response,
- parsed answer,
- correctness,
- evaluation mode,
- latency,
- software/version metadata where available.

## Stopping rule

Do not stop the main experiment early because an intermediate result supports or contradicts a hypothesis. Complete the predeclared evaluation set unless a technical failure requires a documented protocol change.
