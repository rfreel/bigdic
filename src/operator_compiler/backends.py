from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
import os
import urllib.request
from typing import Mapping


@dataclass(frozen=True)
class TrialRequest:
    prompt: str
    model: str
    temperature: float = 0.0
    max_tokens: int = 512


@dataclass(frozen=True)
class TrialResult:
    text: str
    provider: str
    model: str
    response_sha256: str
    error: str | None = None


class ReplayBackend:
    """Deterministic backend for CI, replay, and frozen causal fixtures."""

    def __init__(self, mapping: Mapping[str, str], name: str = "replay"):
        self.mapping = dict(mapping)
        self.name = name

    def invoke(self, request: TrialRequest) -> TrialResult:
        text = self.mapping.get(request.prompt, "")
        error = None if request.prompt in self.mapping else "REPLAY_MISS"
        return TrialResult(text, self.name, request.model, sha256(text.encode()).hexdigest(), error)


class OpenAICompatibleBackend:
    """Small stdlib-only adapter for OpenRouter, Groq, Gemini OpenAI compatibility, etc."""

    def __init__(self, *, name: str, base_url: str, api_key: str):
        self.name = name
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key

    def invoke(self, request: TrialRequest) -> TrialResult:
        payload = json.dumps({
            "model": request.model,
            "messages": [{"role": "user", "content": request.prompt}],
            "temperature": request.temperature,
            "max_tokens": request.max_tokens,
        }).encode()
        req = urllib.request.Request(
            self.base_url + "/chat/completions",
            data=payload,
            headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=90) as response:
                data = json.load(response)
            text = data["choices"][0]["message"]["content"]
            return TrialResult(text, self.name, request.model, sha256(text.encode()).hexdigest(), None)
        except Exception as exc:
            return TrialResult("", self.name, request.model, sha256(b"").hexdigest(), f"{type(exc).__name__}: {exc}")


class BackendRegistry:
    def __init__(self, backends):
        self._backends = dict(backends)

    @classmethod
    def from_env(cls, env=None):
        env = dict(os.environ if env is None else env)
        backends = {}
        if env.get("BIGDIC_REPLAY_JSON"):
            backends["replay"] = ReplayBackend(json.loads(env["BIGDIC_REPLAY_JSON"]))
        specs = [
            ("openrouter", "OPENROUTER_API_KEY", "https://openrouter.ai/api/v1"),
            ("groq", "GROQ_API_KEY", "https://api.groq.com/openai/v1"),
            ("gemini", "GEMINI_OPENAI_API_KEY", "https://generativelanguage.googleapis.com/v1beta/openai"),
        ]
        for name, key, url in specs:
            if env.get(key):
                backends[name] = OpenAICompatibleBackend(name=name, base_url=url, api_key=env[key])
        return cls(backends)

    def names(self):
        return tuple(sorted(self._backends))

    def get(self, name):
        return self._backends[name]
