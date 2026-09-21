# Reproducibility

## Objective

A third party should be able to determine exactly which code, prompts, model configuration, and evaluation procedure produced each reported result.

## Environment

Record:

- operating system,
- CPU,
- GPU,
- RAM,
- Ollama version,
- Python version,
- repository commit SHA,
- installed Python dependencies,
- model identifier/checksum where available.

## Experiment configuration

Every run must record:

- run ID,
- UTC timestamp,
- model,
- precision/quantization format,
- dataset and version,
- item/sample IDs,
- prompt-set version,
- exact prompt text,
- temperature,
- seed,
- max output tokens,
- thinking setting,
- evaluation mode,
- backend/runtime settings where available.

## Raw-data policy

Raw outputs are immutable research artifacts.

The repository should not store large generated outputs in Git if they exceed practical repository limits. Instead:

- retain them locally,
- archive them using a documented release/artifact mechanism,
- publish hashes or manifests where appropriate,
- keep derived tables reproducible.

## Determinism

The pilot uses:

- temperature 0.0,
- a fixed seed where supported,
- fixed prompt order.

The seed should not be treated as a universal determinism guarantee because runtime/backend implementations can still differ.

## Software

Install the project in a clean environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
```

Run the pilot:

```powershell
python -m qps.run_pilot
```

For strict whole-response matching:

```powershell
python -m qps.run_pilot --evaluation-mode exact
```

## Data provenance

For every external dataset, record:

- source URL,
- dataset name/version,
- retrieval date,
- license,
- preprocessing steps,
- sample-selection rule.

## Prompt provenance

Prompt sets should be versioned and immutable once a main experiment begins.

Recommended identifier:

`promptset-v1`

If prompts are revised after pilot inspection, create:

`promptset-v2`

and document the reason in `EXPERIMENT_LOG.md`.

## Analysis provenance

Derived figures and tables must state which raw run IDs they came from.

A result should be traceable:

`paper table → analysis script → derived dataset → raw run IDs`

## Release checklist

Before public release:

- [ ] clean environment installation tested,
- [ ] experiment command documented,
- [ ] dataset provenance recorded,
- [ ] prompt-set version recorded,
- [ ] model identifiers recorded,
- [ ] raw-data policy documented,
- [ ] all reported numbers regenerated from code,
- [ ] failed runs documented,
- [ ] limitations updated,
- [ ] commit/tag recorded.
