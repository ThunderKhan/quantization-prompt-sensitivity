# Quantization Prompt Sensitivity

Research code and documentation for studying whether lower-precision inference changes the robustness of small language models to semantics-preserving prompt variations.

## Working research question

> Does lower-precision inference change the sensitivity of small language models to semantics-preserving changes in prompt wording?

The word **change** is intentional. We will not assume that quantization increases sensitivity; the experiment is designed to test the direction and magnitude of any effect.

## Repository structure

```text
quantization-prompt-sensitivity/
│
├── README.md
│
├── research/
│   ├── CONTEXT.md
│   ├── RESEARCH_QUESTION.md
│   ├── LITERATURE_REVIEW.md
│   ├── HYPOTHESES.md
│   ├── EXPERIMENT_PROTOCOL.md
│   ├── EXPERIMENT_LOG.md
│   ├── RESULTS.md
│   ├── DISCUSSION.md
│   ├── LIMITATIONS.md
│   └── REPRODUCIBILITY.md
│
├── experiments/
├── src/
├── scripts/
├── data/
├── results/
├── figures/
├── requirements.txt
└── pyproject.toml
```

## Current phase

**Phase 0 — pipeline validation**

The current implementation uses Ollama and `qwen3:0.6b` to validate the experiment pipeline.

The pilot is not a scientific result. It verifies:

- reproducible prompt loading,
- Ollama API connectivity,
- fixed decoding parameters,
- raw-response preservation,
- result serialization,
- evaluation plumbing.

## Initial research questions

- **RQ1:** Do semantics-preserving prompt variations change task performance?
- **RQ2:** Which prompt perturbation categories produce the greatest instability?
- **RQ3:** Does quantization change prompt sensitivity?
- **RQ4:** Can aggregate accuracy conceal substantial prompt instability?

## Development workflow

Pull the latest repository state:

```powershell
git pull origin main
```

Create a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
```

Verify the local model:

```powershell
ollama list
ollama run qwen3:0.6b --think=false
```

Run the pilot:

```powershell
python -m qps.run_pilot
```

## Reproducibility rules

- Never modify raw experiment outputs after collection.
- Record the exact prompt text and configuration for each run.
- Record model, precision, dataset, prompt-set version, decoding settings, and run ID.
- Never overwrite previous runs.
- Document protocol changes in `research/EXPERIMENT_LOG.md`.
- Treat hypotheses as testable claims, not expected outcomes.

## Research workflow

```text
Literature
    ↓
Research Question
    ↓
Hypotheses
    ↓
Experiment Protocol
    ↓
Pilot
    ↓
Protocol Lock
    ↓
Full Experiments
    ↓
Statistical Analysis
    ↓
Results
    ↓
Discussion / Limitations
    ↓
Paper
```

## Status

Research protocol is being developed. No scientific conclusions should be inferred from pilot results until the full experimental design and evaluation procedure are finalized.
