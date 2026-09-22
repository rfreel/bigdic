from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from .backends import TrialRequest


@dataclass(frozen=True)
class Condition:
    name: str
    prompt: str


def build_conditions(task: str, operator: str, contract: str):
    placebo = "Before answering, process the request carefully."
    treatment = f"{task}\n\nOPERATOR {operator}: {contract}"
    return (
        Condition("control", task),
        Condition("placebo", task + "\n\n" + placebo),
        Condition("operator", treatment),
        Condition("operator_check", treatment + "\nBefore committing, check for an answer-changing mistake."),
    )


def run_trial(backend, request: TrialRequest, *, condition: str):
    result = backend.invoke(request)
    return {
        "condition": condition,
        "provider": result.provider,
        "model": result.model,
        "prompt_sha256": sha256(request.prompt.encode()).hexdigest(),
        "response_sha256": result.response_sha256,
        "text": result.text,
        "error": result.error,
    }
