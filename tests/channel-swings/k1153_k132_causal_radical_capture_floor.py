#!/usr/bin/env python3
"""K1153: apply the radical-capture floor to K132's causal symbols."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1153-k132-causal-radical-capture-floor.json"


def load(name): return json.loads((ROOT / "lab/process" / name).read_text())


def build():
    k132 = load("selected-k132-native-i1b-t0-all-grade-noether-complex.json")
    carrier = k132["coupled_dn_symbol"]["carrier_dimension"]
    ranks = k132["coupled_dn_symbol"]["ranks"]
    gauge = k132["minimal_bv_kt_bfv"]["metric_diffeomorphism_generator_rank"]
    strata = {}
    for name in ("timelike", "spacelike", "null"):
        kernel = carrier - ranks[name]
        strata[name] = {
            "field_dimension": carrier,
            "hessian_rank": ranks[name],
            "hessian_kernel_dimension": kernel,
            "owned_gauge_rank": gauge,
            "required_rank_on_hessian_kernel": kernel - gauge,
            "euler_factor_rank_on_hessian_kernel": 0,
            "euler_factor_passes_positive_cohomology_gate": False,
        }
    return {
        "schema_version": "1.0",
        "result_id": "K1153-K132-CAUSAL-RADICAL-CAPTURE-FLOOR",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "source_owner": "K132 selected source-native I1B coupled DN Hessian with rank-four metric diffeomorphism image",
        "strata": strata,
        "causal_rank_floors": {k: v["required_rank_on_hessian_kernel"] for k, v in strata.items()},
        "conclusion": "every Euler-factor constraint Q=L H fails the positive-nonzero-cohomology radical gate on all three K132 causal strata",
        "repair_requirement": "a successful current-Hessian constraint must detect ker(H)/im(d) at the stated rank, or a source-owned enlarged gauge image or changed parent must be supplied",
        "protected_effect": "none",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    s = d["strata"]
    assert d["source_owner"].startswith("K132 selected source-native I1B")
    assert s["timelike"]["hessian_kernel_dimension"] == 98474
    assert s["spacelike"]["hessian_kernel_dimension"] == 98474
    assert s["null"]["hessian_kernel_dimension"] == 106638
    assert d["causal_rank_floors"] == {"timelike": 98470, "spacelike": 98470, "null": 106634}
    assert all(v["owned_gauge_rank"] == 4 for v in s.values())
    assert all(v["euler_factor_rank_on_hessian_kernel"] == 0 for v in s.values())
    assert not any(v["euler_factor_passes_positive_cohomology_gate"] for v in s.values())
    assert "all three K132 causal strata" in d["conclusion"]
    assert "detect ker(H)/im(d)" in d["repair_requirement"]
    assert d["protected_effect"] == "none" and d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    assert json.loads(OUTPUT.read_text()) == data
    print("K1153 controls: 12/12")
