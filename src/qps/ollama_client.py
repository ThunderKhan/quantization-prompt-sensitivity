from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import requests


@dataclass(frozen=True)
class OllamaResponse:
    model: str
    response: str
    done: bool
    raw: dict[str, Any]


class OllamaClient:
    """Minimal client for the local Ollama chat API."""

    def __init__(
        self,
        base_url: str = "http://localhost:11434",
        timeout_seconds: int = 120,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout_seconds = timeout_seconds

    def chat(
        self,
        model: str,
        prompt: str,
        *,
        think: bool = False,
        temperature: float = 0.0,
        seed: int = 0,
    ) -> OllamaResponse:
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
            "think": think,
            "options": {
                "temperature": temperature,
                "seed": seed,
            },
        }

        response = requests.post(
            f"{self.base_url}/api/chat",
            json=payload,
            timeout=self.timeout_seconds,
        )
        response.raise_for_status()
        data = response.json()

        return OllamaResponse(
            model=data.get("model", model),
            response=data.get("message", {}).get("content", ""),
            done=bool(data.get("done", False)),
            raw=data,
        )
