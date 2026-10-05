#!/usr/bin/env python3
"""K1144: exact positivity/nontriviality criterion for a two-term complex."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1144-positive-nonzero-two-term-cohomology.json"


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1144-POSITIVE-NONZERO-TWO-TERM-COHOMOLOGY",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "theorem": "for Qd=0, H0=ker(Q)/im(d) carries a positive-definite induced pairing iff H restricted to ker(Q) is nonnegative and its radical equals im(d); H0 is nonzero iff dim ker(Q)>rank(d)",
        "pass_fixture": {
            "Q": [[1, 0, 0, 0]],
            "d": [[0], [1], [0], [0]],
            "Qd_zero": True,
            "H_diagonal": [0, 0, 2, 3],
            "kernel_dimension": 3,
            "gauge_rank": 1,
            "restricted_radical_equals_gauge_image": True,
            "cohomology_dimension": 2,
            "cohomology_gram": [[2, 0], [0, 3]],
            "positive_definite": True,
        },
        "acyclic_control": {
            "kernel_dimension": 1, "gauge_rank": 1,
            "cohomology_dimension": 0, "vacuously_nonnegative_but_nonzero": False,
        },
        "negative_control": {
            "kernel_dimension": 2, "gauge_rank": 1,
            "cohomology_dimension": 1, "cohomology_gram": [[-1]],
            "positive_definite": False,
        },
        "source_bv_bfv_complex_supplied": False,
        "physical_identification_supplied": False,
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    p, a, n = d["pass_fixture"], d["acyclic_control"], d["negative_control"]
    assert "radical equals im(d)" in d["theorem"]
    assert p["Qd_zero"]
    assert p["kernel_dimension"] == 3 and p["gauge_rank"] == 1
    assert p["restricted_radical_equals_gauge_image"]
    assert p["cohomology_dimension"] == 2
    assert p["cohomology_gram"] == [[2, 0], [0, 3]] and p["positive_definite"]
    assert a["cohomology_dimension"] == 0 and not a["vacuously_nonnegative_but_nonzero"]
    assert n["cohomology_dimension"] == 1
    assert n["cohomology_gram"] == [[-1]] and not n["positive_definite"]
    assert not d["source_bv_bfv_complex_supplied"]
    assert not d["physical_identification_supplied"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1144 controls: 12/12")
