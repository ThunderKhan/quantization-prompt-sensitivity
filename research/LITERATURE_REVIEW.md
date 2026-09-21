# Literature Review

## Purpose

This document tracks the evidence that informs the experiment design. It is an evolving research artifact, not a finished literature review.

## Initial literature map

### 1. Prompt formatting sensitivity

Sclar et al. introduced a systematic study of sensitivity to meaning-preserving prompt formatting and showed that apparently minor formatting choices can materially affect performance in prompting-based evaluation. Their work motivates measuring a range of plausible prompts rather than treating one prompt template as universally representative.

**Reference:** Sclar, M., Choi, Y., Tsvetkov, Y., & Suhr, A. (2023). *Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting.*

https://arxiv.org/abs/2310.11324

### 2. Prompt sensitivity prediction

Razavi et al. (2025) introduced PromptSET and framed prompt sensitivity prediction as a separate task, using prompt variations over QA datasets and multiple LLMs.

**Reference:** Razavi, A., et al. (2025). *Benchmarking Prompt Sensitivity in Large Language Models.*

https://arxiv.org/abs/2502.06065

### 3. Mechanistic analysis of prompt sensitivity

Liu & Chu (ACL 2026) analyze prompt sensitivity using a first-order Taylor expansion and relate meaning-preserving prompts, gradients, and next-token log probabilities. They also examine which prompt variants are associated with sensitivity and report a relationship between their theoretical bound and PromptSensiScore.

**Reference:** Liu, Y., & Chu, C. (2026). *Understanding the Prompt Sensitivity.* Proceedings of ACL 2026.

https://aclanthology.org/2026.acl-long.2053/

### 4. Lexical sensitivity

Xie et al. (Findings of ACL 2026) study lexical prompt sensitivity at large scale using 132,000 prompt variants and analyze token/n-gram mechanisms. Their results emphasize that surface-level lexical changes can affect performance.

**Reference:** Xie, Q., et al. (2026). *Beyond Prompt Engineering: A Systematic Analysis of Prompt Lexical Sensitivity and Its Impacts on Quality.*

https://aclanthology.org/2026.findings-acl.2084/

### 5. Lexical and syntactic perturbations in evaluation

Kostić et al. (LREC 2026) evaluate truth-conditionally equivalent lexical and syntactic perturbations across 23 LLMs and three benchmarks. Their study is directly relevant to our need for linguistically controlled prompt transformations.

**Reference:** Kostić, B., Fallon, C., Risch, J., & Loeser, A. (2026). *Same Meaning, Different Scores: Lexical and Syntactic Sensitivity in LLM Evaluation.*

https://aclanthology.org/2026.lrec-1.363/

### 6. Robustness to prompt perturbations

Hejabi et al. (ACL 2026) propose Flip-Flop Consistency, a training method aimed at reducing inconsistent responses across prompt perturbations. This motivates treating cross-prompt consistency as a first-class outcome rather than only reporting mean task performance.

**Reference:** Hejabi, P., Rahmati, E., Salkhordeh Ziabari, A., & Dehghani, M. (2026). *Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs.*

https://aclanthology.org/2026.acl-long.71/

### 7. Quantization of small language models

Recent work separately studies quantization as an efficiency mechanism for small language models and evaluates its capability trade-offs. One 2026 study reports capability-specific evaluation of 4-bit quantization across seven small instruction-tuned models.

**Reference:** Rahimov, E. (2026). *Capability-Specific Degradation Patterns in Quantized Small Language Models.*

https://doi.org/10.36079/lamintang.ijai-01301.1050

### 8. Quantization and long-context performance

Mekala et al. (EMNLP 2025) systematically evaluated multiple quantization methods and models on long-context tasks and reported that the effect of quantization varies by bit-width, method, model, and task.

**Reference:** Mekala, A., Atmakuru, A., Song, Y., Karpinska, M., & Iyyer, M. (2025). *Does quantization affect models' performance on long-context tasks?*

https://aclanthology.org/2025.emnlp-main.479/

## Emerging gap

The initial search suggests a useful separation in the literature:

`prompt sensitivity research`

and

`quantization/capability research`

are both active, but the direct intersection is less clearly established in the papers identified so far.

**Important:** this is only a provisional gap statement. We must expand the search before claiming that the proposed study is the first, or the first of any particular kind.

## What the literature changes about our design

The literature tells us to:

1. Use genuinely meaning-preserving transformations where possible.
2. Distinguish lexical, syntactic, formatting, and other perturbation types.
3. Report variability rather than only a single accuracy number.
4. Avoid conflating model capability with robustness.
5. Treat quantization configuration as more than a single binary label.
6. Compare against an unquantized or highest-precision reference.
7. Preserve a clear audit trail from prompt construction to final statistics.

## Literature review status

**Status:** Initial targeted review.

**Next action:** expand to a systematic table of at least 20–30 papers, including exact models, datasets, perturbation methods, metrics, quantization methods, and stated limitations before finalizing the novelty claim.
