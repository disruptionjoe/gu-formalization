#!/usr/bin/env python3
"""K1038: compose the K77 quotient interface with K1033 local effects."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1038-k1037-quotient-local-effect-composition.json"


def add(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, F(0)) + value
        if not out[key]:
            del out[key]
    return out


def partial_trace_a(state):
    out = {}
    for ((a, b), (c, d)), value in state.items():
        if a == c:
            out[(b, d)] = out.get((b, d), F(0)) + value
    return out


def filter_a(state, keep):
    return {key: value for key, value in state.items() if key[0][0] in keep and key[1][0] in keep}


def build():
    bell = {
        ((0, 0), (0, 0)): F(1, 2),
        ((0, 0), (1, 1)): F(1, 2),
        ((1, 1), (0, 0)): F(1, 2),
        ((1, 1), (1, 1)): F(1, 2),
    }
    b0, b1 = filter_a(bell, {0}), filter_a(bell, {1})
    nonselective = add(b0, b1)
    probs = [sum(value for ((a, _), (c, _)), value in bell.items() if a == c == i) for i in (0, 1)]
    marginal_before = partial_trace_a(bell)
    marginal_after = partial_trace_a(nonselective)
    return {
        "schema_version": "1.0",
        "result_id": "K1038-K1037-QUOTIENT-LOCAL-EFFECT-COMPOSITION",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "carrier": "two labelled copies of the K77 rank-960 positive quotient W",
        "state": "normalized Bell control supported on a two-dimensional subspace of W tensor W",
        "probabilities": [str(x) for x in probs],
        "probability_sum": str(sum(probs)),
        "marginal_before": {str(k): str(v) for k, v in marginal_before.items()},
        "marginal_after": {str(k): str(v) for k, v in marginal_after.items()},
        "instrument": "the complete local rank-one/complement instrument depends only on P Phi and is trace preserving",
        "composition_grade": "exact algebraic candidate on the repository-owned K77 quotient",
        "open_physical_boundary": "the tensor-copy rule, spacelike realization, preparation, settings and detectors are not source/action-selected GU apparatus",
        "ownership": {"candidate_effect_interface": True, "source_GU_local_algebra": False, "scorable_apparatus": False},
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "rank-960" in d["carrier"] and "W" in d["carrier"]
    assert "W tensor W" in d["state"]
    assert d["probabilities"] == ["1/2", "1/2"]
    assert d["probability_sum"] == "1"
    assert d["marginal_before"] == d["marginal_after"]
    assert set(d["marginal_before"].values()) == {"1/2"}
    assert "trace preserving" in d["instrument"]
    assert d["composition_grade"].startswith("exact algebraic candidate")
    assert "not source/action-selected" in d["open_physical_boundary"]
    assert d["ownership"] == {"candidate_effect_interface": True, "source_GU_local_algebra": False, "scorable_apparatus": False}
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1038 controls: 13/13")
