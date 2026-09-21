# Research Question

## Working title

**Does Quantization Amplify Prompt Sensitivity in Small Language Models?**

### Subtitle

*A Controlled Study of Semantics-Preserving Prompt Perturbations*

## Central question

> Does lower-precision inference change the sensitivity of small language models to semantics-preserving changes in prompt wording?

The phrase **change the sensitivity** is intentional. We will not build the protocol around the assumption that sensitivity must increase.

## Research questions

### RQ1 — Baseline sensitivity

Do semantics-preserving prompt variations produce measurable differences in task performance for small language models?

### RQ2 — Perturbation type

Which controlled perturbation categories produce the largest changes in performance and output behavior?

### RQ3 — Quantization effect

Does quantization change prompt sensitivity after accounting for the model's overall task performance?

### RQ4 — Evaluation reliability

Can aggregate benchmark accuracy conceal meaningful instability across plausible prompt formulations?

## Unit of analysis

The primary unit is a **task item under a model/configuration and prompt variant**.

For each item, the underlying task remains fixed while the prompt wrapper changes.

## Key distinction

We need to separate:

`general capability degradation`

from:

`increased sensitivity to prompt wording`

A lower-precision model can have lower average accuracy without becoming more prompt-sensitive. Therefore both performance level and stability must be measured.

## Candidate operational metrics

### Prompt accuracy

`A_p = correct answers for prompt variant p / number of items`

### Prompt spread

`ΔA = max(A_p) - min(A_p)`

### Item flip rate

Fraction of task items for which correctness changes across prompt variants.

### Robust accuracy

Fraction of items answered correctly under every tested prompt variant.

### Output agreement

A task-level measure of how consistently outputs agree across prompt variants, to be defined carefully for each task type.

## Scope

The initial study is deliberately narrow:

- small open/instruction-tuned models,
- local inference,
- controlled prompt perturbations,
- low-precision versus higher-precision inference,
- a small number of task families,
- reproducible inference settings.

## Out of scope for the first paper

- training a new model,
- proposing a new quantization algorithm,
- broad prompt engineering optimization,
- claims about all LLMs,
- causal claims about the internal mechanism of quantization unless directly measured.

## Decision rule

The final paper should answer the research questions from the collected evidence. If the hypotheses are unsupported, the manuscript should say so explicitly rather than selecting favorable subsets of results.
