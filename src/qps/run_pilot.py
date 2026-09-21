from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path
import uuid

from qps.evaluation import accuracy, evaluate_answer
from qps.ollama_client import OllamaClient


ROOT = Path(__file__).resolve().parents[2]
PROMPT_FILE = ROOT / "prompts" / "pilot.json"
RESULTS_DIR = ROOT / "results"
RAW_DIR = RESULTS_DIR / "raw"


def load_prompt_file(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_summary(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "run_id",
        "timestamp_utc",
        "experiment_id",
        "model",
        "think",
        "temperature",
        "seed",
        "prompt_id",
        "category",
        "correct",
        "evaluation_mode",
        "candidate_answers",
        "latency_ms",
        "response",
    ]

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def run(args: argparse.Namespace) -> None:
    config = load_prompt_file(PROMPT_FILE)
    started_at = datetime.now(timezone.utc)
    run_id = started_at.strftime("%Y%m%dT%H%M%SZ") + "_" + uuid.uuid4().hex[:8]
    timestamp = started_at.isoformat()

    client = OllamaClient(timeout_seconds=args.timeout)

    raw_rows: list[dict] = []
    summary_rows: list[dict] = []

    for prompt in config["prompts"]:
        started = datetime.now(timezone.utc)

        result = client.chat(
            args.model,
            prompt["text"],
            think=args.think,
            temperature=args.temperature,
            seed=args.seed,
        )

        finished = datetime.now(timezone.utc)
        latency_ms = int((finished - started).total_seconds() * 1000)

        evaluation = evaluate_answer(
            result.response,
            config["expected_answer"],
            mode=args.evaluation_mode,
        )

        raw_rows.append(
            {
                "run_id": run_id,
                "timestamp_utc": timestamp,
                "experiment_id": config["experiment_id"],
                "model": result.model,
                "prompt_id": prompt["id"],
                "category": prompt["category"],
                "prompt": prompt["text"],
                "expected_answer": config["expected_answer"],
                "response": result.response,
                "correct": evaluation["correct"],
                "evaluation_mode": evaluation["evaluation_mode"],
                "candidate_answers": evaluation["candidate_answers"],
                "normalized_response": evaluation["normalized_response"],
                "latency_ms": latency_ms,
                "think": args.think,
                "temperature": args.temperature,
                "seed": args.seed,
                "ollama_raw": result.raw,
            }
        )

        summary_rows.append(
            {
                "run_id": run_id,
                "timestamp_utc": timestamp,
                "experiment_id": config["experiment_id"],
                "model": result.model,
                "think": args.think,
                "temperature": args.temperature,
                "seed": args.seed,
                "prompt_id": prompt["id"],
                "category": prompt["category"],
                "correct": int(evaluation["correct"]),
                "evaluation_mode": evaluation["evaluation_mode"],
                "candidate_answers": "|".join(evaluation["candidate_answers"]),
                "latency_ms": latency_ms,
                "response": result.response,
            }
        )

    raw_path = RAW_DIR / f"{run_id}.jsonl"
    summary_path = RESULTS_DIR / f"{run_id}_summary.csv"

    write_jsonl(raw_path, raw_rows)
    write_summary(summary_path, summary_rows)

    overall_accuracy = accuracy(row["correct"] for row in summary_rows)

    print(f"Run ID: {run_id}")
    print(f"Model: {args.model}")
    print(f"Prompts: {len(summary_rows)}")
    print(f"Evaluation: {args.evaluation_mode}")
    print(f"Accuracy: {overall_accuracy:.3f}")
    print(f"Raw results: {raw_path}")
    print(f"Summary: {summary_path}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the Phase 0 Ollama pilot.")
    parser.add_argument("--model", default="qwen3:0.6b")
    parser.add_argument("--think", action="store_true", help="Enable model thinking.")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument(
        "--evaluation-mode",
        choices=["numeric_token", "exact"],
        default="numeric_token",
        help="How to evaluate the pilot answer.",
    )
    return parser


if __name__ == "__main__":
    run(build_parser().parse_args())
