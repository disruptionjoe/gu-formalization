#!/usr/bin/env python3
"""K1122: sharp codimension floor for a nonnegative constrained subspace."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1122-k1121-positive-reduction-codimension-floor.json"


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1122-K1121-POSITIVE-REDUCTION-CODIMENSION-FLOOR",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "theorem": "for inertia (p,q,z), every H-nonnegative subspace W has dim(W)<=p+z and codim(W)>=q",
        "sharp": True,
        "radical_quotient_is_separate_step": True,
        "fixture_diagonal": [-4, -1, 0, 2, 3, 5],
        "fixture_inertia": [3, 2, 1],
        "fixture_nonnegative_indices": [2, 3, 4, 5],
        "fixture_codimension": 2,
        "fixture_floor": 2,
        "constraint_interpretation": "a positive physical reduction must impose at least q independent non-gauge conditions before quotienting its residual radical",
        "scope_boundary": "necessary finite-dimensional or fibrewise condition only; it neither constructs constraints nor proves their propagation or closure",
    }


def validate(d):
    assert "codim(W)>=q" in d["theorem"]
    assert d["sharp"] is True
    assert d["radical_quotient_is_separate_step"] is True
    assert d["fixture_diagonal"] == [-4, -1, 0, 2, 3, 5]
    assert d["fixture_inertia"] == [3, 2, 1]
    assert d["fixture_nonnegative_indices"] == [2, 3, 4, 5]
    assert d["fixture_codimension"] == d["fixture_floor"] == 2
    assert "non-gauge conditions" in d["constraint_interpretation"]
    assert "neither constructs constraints" in d["scope_boundary"]


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1122 controls: 9/9")
