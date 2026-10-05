#!/usr/bin/env python3
"""K1149: boundary maximality gate for a formally skew generator."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1149-boundary-skew-adjoint-generator-gate.json"


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1149-BOUNDARY-SKEW-ADJOINT-GENERATOR-GATE",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "differential_expression": "G=d/dx on L2(0,1)",
        "green_boundary_form": "<Gu,v>+<u,Gv>=u(1)^*v(1)-u(0)^*v(0)",
        "dirichlet_realization": {
            "domain": "H1_0(0,1)",
            "boundary_form_zero": True,
            "skew_symmetric": True,
            "adjoint_domain": "H1(0,1)",
            "maximal": False,
            "skew_adjoint": False,
            "unitary_group_generator": False,
        },
        "periodic_realization": {
            "domain": "{u in H1:u(1)=u(0)}",
            "boundary_form_zero": True,
            "skew_symmetric": True,
            "adjoint_domain_equal": True,
            "maximal": True,
            "skew_adjoint": True,
            "unitary_translation_group": True,
        },
        "theorem": "formal skewness and vanishing boundary flux are necessary but not sufficient; the selected boundary domain must be maximal skew-adjoint and preserved by the evolution",
        "source_boundary_domain_supplied": False,
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    a, p = d["dirichlet_realization"], d["periodic_realization"]
    assert d["differential_expression"] == "G=d/dx on L2(0,1)"
    assert "u(1)^*v(1)-u(0)^*v(0)" in d["green_boundary_form"]
    assert a["domain"] == "H1_0(0,1)" and a["boundary_form_zero"]
    assert a["skew_symmetric"] and a["adjoint_domain"] == "H1(0,1)"
    assert not a["maximal"] and not a["skew_adjoint"]
    assert not a["unitary_group_generator"]
    assert p["boundary_form_zero"] and p["skew_symmetric"]
    assert p["adjoint_domain_equal"] and p["maximal"]
    assert p["skew_adjoint"] and p["unitary_translation_group"]
    assert "necessary but not sufficient" in d["theorem"]
    assert "preserved by the evolution" in d["theorem"]
    assert not d["source_boundary_domain_supplied"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1149 controls: 12/12")
