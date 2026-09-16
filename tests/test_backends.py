import json

from operator_compiler.backends import TrialRequest, ReplayBackend, BackendRegistry
from operator_compiler.experiments import build_conditions, run_trial


def test_replay_backend_is_deterministic_and_hashes_response():
    req = TrialRequest(prompt="2+2?", model="fixture")
    backend = ReplayBackend({"2+2?": "4"}, name="replay")
    out = backend.invoke(req)
    assert out.text == "4"
    assert out.provider == "replay"
    assert len(out.response_sha256) == 64
    assert out.error is None


def test_registry_skips_unconfigured_providers_without_blocking_replay():
    reg = BackendRegistry.from_env({"BIGDIC_REPLAY_JSON": json.dumps({"x": "y"})})
    assert reg.names() == ("replay",)
    assert reg.get("replay").invoke(TrialRequest(prompt="x", model="fixture")).text == "y"


def test_conditions_are_control_placebo_operator_and_check():
    conditions = build_conditions("Solve X", "TEST", "Execute a defined check.")
    assert [c.name for c in conditions] == ["control", "placebo", "operator", "operator_check"]
    assert "TEST" not in conditions[0].prompt
    assert "TEST" in conditions[2].prompt


def test_run_trial_records_condition_and_prompt_hash():
    backend = ReplayBackend({"Solve X": "answer"}, name="replay")
    row = run_trial(backend, TrialRequest(prompt="Solve X", model="fixture"), condition="control")
    assert row["condition"] == "control"
    assert len(row["prompt_sha256"]) == 64
    assert row["provider"] == "replay"
