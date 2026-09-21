# Research Context

## Project

**Repository:** `ThunderKhan/quantization-prompt-sensitivity`

**Working title:** *Does Quantization Amplify Prompt Sensitivity in Small Language Models?*

**Project goal:** Conduct a reproducible empirical study of whether lower-precision inference changes the stability of small language models under semantics-preserving prompt perturbations.

## Why this question

Prompt sensitivity is already an established research problem: prior studies have shown that meaning-preserving changes in wording or formatting can alter LLM behavior. Recent 2026 work studies the mechanisms and large-scale empirical patterns of this sensitivity.

Quantization is a separate, well-established deployment technique. Recent work evaluates its effects on efficiency and task performance, including in small language models.

Our working research direction is the intersection:

`small/local LLMs × prompt sensitivity × quantization × reliability`

The goal is **not** to assume that quantization makes models less robust. The experiment must be capable of finding increased sensitivity, no meaningful change, or a decrease.

## Current evidence base

The initial literature scan identified:

1. Earlier work on sensitivity to prompt formatting and other meaning-preserving changes.
2. Work that benchmarks prompt sensitivity and attempts to predict it.
3. 2026 work studying mechanisms, lexical sensitivity, syntax, and robustness to perturbations.
4. Separate studies of quantization and capability/efficiency trade-offs in small and larger LLMs.

The exact novelty claim will remain provisional until the literature review is expanded and checked against the final experimental design.

## Current implementation state

The repository contains:

- a minimal Ollama API client,
- a deterministic pilot runner,
- a pilot prompt set,
- answer normalization for the arithmetic sanity check,
- structured raw-result storage.

The first local model is `qwen3:0.6b`.

## What the pilot is for

The arithmetic pilot is a **software sanity check**, not a scientific result. It tests:

- API connectivity,
- prompt loading,
- deterministic inference settings,
- raw-response preservation,
- result serialization,
- evaluation plumbing.

## Research discipline

The project follows these rules:

- Separate hypotheses from observed results.
- Preserve raw outputs.
- Record the complete experimental configuration.
- Do not edit raw result files after collection.
- Do not turn an observed correlation into a causal claim.
- Verify literature claims against the original papers.
- Report null results and failed hypotheses.
- Keep the final novelty claim narrower than the evidence warrants.

## Current phase

**Phase 0: Pipeline validation**

Next:

**Phase 1: 20-item pilot**

Then:

**Phase 2: Final prompt taxonomy and validation**

Then:

**Phase 3: Quantization experiments**

Then:

**Phase 4: Statistical analysis and manuscript preparation**
