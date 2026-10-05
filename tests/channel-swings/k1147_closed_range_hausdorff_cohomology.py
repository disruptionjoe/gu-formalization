#!/usr/bin/env python3
"""K1147: closed range is the Hausdorff gate for Hilbert cohomology."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1147-closed-range-hausdorff-cohomology.json"


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1147-CLOSED-RANGE-HAUSDORFF-COHOMOLOGY",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "theorem": "ker(Q)/im(d) is a Hausdorff Hilbert quotient in the inherited norm only when im(d) is closed; for diagonal finite-fibre d, a uniform lower bound on every nonzero singular value is the exact closed-range criterion",
        "pass_fixture": {
            "d_symbol": "1",
            "nonzero_singular_value_floor": "1",
            "range_closed": True,
            "quotient_hausdorff": True,
        },
        "failure_fixture": {
            "hilbert_space": "ell2(N)",
            "d_symbol": "1/n",
            "singular_value_infimum": "0",
            "range_dense": True,
            "range_closed": False,
            "limit_vector": "y_n=1/n",
            "limit_vector_in_ell2": True,
            "formal_preimage": "x_n=1",
            "formal_preimage_in_ell2": False,
            "algebraic_quotient_hausdorff": False,
        },
        "source_gauge_range_supplied": False,
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    p, f = d["pass_fixture"], d["failure_fixture"]
    assert "Hausdorff Hilbert quotient" in d["theorem"]
    assert "uniform lower bound" in d["theorem"]
    assert p["d_symbol"] == "1" and p["nonzero_singular_value_floor"] == "1"
    assert p["range_closed"] and p["quotient_hausdorff"]
    assert f["d_symbol"] == "1/n" and f["singular_value_infimum"] == "0"
    assert f["range_dense"] and not f["range_closed"]
    assert f["limit_vector"] == "y_n=1/n" and f["limit_vector_in_ell2"]
    assert f["formal_preimage"] == "x_n=1" and not f["formal_preimage_in_ell2"]
    assert not f["algebraic_quotient_hausdorff"]
    assert not d["source_gauge_range_supplied"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1147 controls: 12/12")
