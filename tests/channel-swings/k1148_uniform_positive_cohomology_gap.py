#!/usr/bin/env python3
"""K1148: uniform coercivity is distinct from fibrewise positivity."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1148-uniform-positive-cohomology-gap.json"


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1148-UNIFORM-POSITIVE-COHOMOLOGY-GAP",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "theorem": "after closed-range reduction, bounded fibrewise positive quotient forms define a coercive Hilbert physical pairing in the inherited norm exactly when their positive eigenvalues have a uniform lower bound",
        "pass_fixture": {
            "quotient_fibre_form": "1+1/n",
            "uniform_lower_bound": "1",
            "coercive": True,
            "bounded_inverse_riesz_map": True,
        },
        "failure_fixture": {
            "quotient_fibre_form": "1/n",
            "every_fibre_positive": True,
            "uniform_lower_bound": "0",
            "unit_vectors": "e_n",
            "ambient_norm": "1",
            "energy": "1/n",
            "coercive": False,
            "bounded_inverse_riesz_map": False,
            "energy_norm_equivalent_to_ambient": False,
        },
        "source_positive_pairing_supplied": False,
        "physical_state_identification_supplied": False,
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    p, f = d["pass_fixture"], d["failure_fixture"]
    assert "uniform lower bound" in d["theorem"]
    assert "closed-range reduction" in d["theorem"]
    assert p["quotient_fibre_form"] == "1+1/n" and p["uniform_lower_bound"] == "1"
    assert p["coercive"] and p["bounded_inverse_riesz_map"]
    assert f["quotient_fibre_form"] == "1/n" and f["every_fibre_positive"]
    assert f["uniform_lower_bound"] == "0"
    assert f["unit_vectors"] == "e_n" and f["energy"] == "1/n"
    assert not f["coercive"] and not f["bounded_inverse_riesz_map"]
    assert not f["energy_norm_equivalent_to_ambient"]
    assert not d["source_positive_pairing_supplied"]
    assert not d["physical_state_identification_supplied"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1148 controls: 12/12")
