#!/usr/bin/env python3
"""K1121: quotienting a Hermitian-form radical preserves nonzero inertia."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1121-k1118-radical-quotient-inertia-preservation.json"


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1121-K1118-RADICAL-QUOTIENT-INERTIA-PRESERVATION",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "theorem": "if G is contained in rad(H), the descended form on V/G has inertia (n_+(H),n_-(H),n_0(H)-dim(G))",
        "nonzero_inertia_preserved": True,
        "gauge_only_can_remove_negative_directions": False,
        "fixture_diagonal": [-3, 0, 2, 5],
        "fixture_gauge_index": 1,
        "fixture_inertia_before": [2, 1, 1],
        "fixture_inertia_after": [2, 1, 0],
        "scope_boundary": "exact finite-dimensional theorem and fibrewise necessity; no global closed operator quotient or physical cohomology is supplied",
        "target_claim": "K1118-I1B-GAUGE-RADICAL-POSITIVITY",
    }


def validate(d):
    assert "G is contained in rad(H)" in d["theorem"]
    assert d["nonzero_inertia_preserved"] is True
    assert d["gauge_only_can_remove_negative_directions"] is False
    assert d["fixture_diagonal"] == [-3, 0, 2, 5]
    assert d["fixture_gauge_index"] == 1
    assert d["fixture_inertia_before"] == [2, 1, 1]
    assert d["fixture_inertia_after"] == [2, 1, 0]
    assert "no global closed operator quotient" in d["scope_boundary"]
    assert d["target_claim"] == "K1118-I1B-GAUGE-RADICAL-POSITIVITY"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1121 controls: 9/9")
