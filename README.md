# Quantization Prompt Sensitivity

Research code for studying whether lower-precision inference changes the robustness of small language models to semantics-preserving prompt variations.

## Working research question

> Does lower-precision inference increase the sensitivity of small language models to semantics-preserving changes in prompt wording?

### Initial research questions

- **RQ1:** Do semantics-preserving prompt variations change task performance?
- **RQ2:** Which prompt perturbation categories produce the greatest instability?
- **RQ3:** Does quantization increase prompt sensitivity?
- **RQ4:** Can average task accuracy hide substantial prompt instability?

## Current phase

**Phase 0 — pipeline validation**

We start with a tiny deterministic pilot against Ollama and `qwen3:0.6b`.

The first goal is not to produce a publishable result. It is to verify that:

1. prompts are loaded reproducibly,
2. Ollama inference is reachable,
3. raw responses are preserved,
4. evaluation metadata is recorded,
5. the experiment can be rerun without changing the protocol.

## Planned experiment

`Model × Precision × Prompt Variant × Task`

The broader study will compare small models and inference precisions after the pilot is stable.

## Local requirements

- Python 3.10+
- Ollama
- `qwen3:0.6b`
- Git

The first pilot uses the Ollama HTTP API at `http://localhost:11434`.

## Setup

### 1. Pull the repository

```powershell
git pull
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
```

### 3. Verify Ollama

```powershell
ollama list
ollama run qwen3:0.6b --think=false
```

### 4. Run the first pilot

```powershell
python -m qps.run_pilot
```

By default this runs the five-prompt arithmetic sanity check and writes raw JSONL plus a summary CSV under `results/`.

## Reproducibility rules

- Do not edit raw outputs after an experiment.
- Keep the exact prompt text used for every generation.
- Record model, experiment configuration, timestamp, and run ID.
- Never overwrite a previous run.
- Treat hypotheses as testable claims, not expected outcomes.

## Repository structure

```text
quantization-prompt-sensitivity/
├── analysis/
├── data/
├── experiments/
├── figures/
├── literature/
├── paper/
├── prompts/
│   └── pilot.json
├── results/
│   └── raw/
├── src/
│   └── qps/
│       ├── __init__.py
│       ├── evaluation.py
│       ├── ollama_client.py
│       └── run_pilot.py
├── pyproject.toml
├── research_question.md
└── .gitignore
```

## Status

Research protocol is being developed. No scientific conclusions should be inferred from the pilot until the full protocol and evaluation suite are finalized.
