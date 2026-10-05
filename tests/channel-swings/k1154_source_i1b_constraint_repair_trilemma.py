#!/usr/bin/env python3
"""K1154: classify the repairs left after the Euler-factor obstruction."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1154-source-i1b-constraint-repair-trilemma.json"


def load(name): return json.loads((ROOT / "lab/process" / name).read_text())


def build():
    app = load("k1153-k132-causal-radical-capture-floor.json")
    branches = [
        {
            "branch": "nonfactor_constraint",
            "necessary_input": "source-owned Q not factoring through H, with Qd=0 and injective action on ker(H)/im(d)",
            "current_status": "not_supplied",
            "causal_rank_on_kernel_floor": app["causal_rank_floors"],
        },
        {
            "branch": "enlarged_gauge_or_kt_image",
            "necessary_input": "source-owned closed image enlarging im(d) to the complete constrained radical on one common domain",
            "current_status": "not_supplied",
            "causal_rank_on_kernel_floor": None,
        },
        {
            "branch": "changed_parent_packet",
            "necessary_input": "different source-owned Hessian, pairing, stationary background, or bulk-boundary differential with every K1150 gate recomputed",
            "current_status": "not_supplied",
            "causal_rank_on_kernel_floor": None,
        },
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1154-SOURCE-I1B-CONSTRAINT-REPAIR-TRILEMMA",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "rejected_class": "Euler-row-only constraints Q=L H on the current K132 Hessian",
        "branches": branches,
        "branches_currently_supplied": 0,
        "prior_negative_capture_floor_retained": {"timelike": 6, "spacelike": 6, "null": 4},
        "stronger_radical_capture_floor": app["causal_rank_floors"],
        "functional_gates_retained": ["common_product_domain", "closed_gauge_range", "uniform_positive_gap", "skew_adjoint_boundary_generator", "common_trace_and_Green_form"],
        "claim_ceiling": "excludes only the current Euler-factor constraint class; it does not exclude a new source differential, enlarged gauge/KT owner, changed stationary parent, or actual boundary coupling",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["rejected_class"] == "Euler-row-only constraints Q=L H on the current K132 Hessian"
    assert [x["branch"] for x in d["branches"]] == ["nonfactor_constraint", "enlarged_gauge_or_kt_image", "changed_parent_packet"]
    assert all(x["current_status"] == "not_supplied" for x in d["branches"])
    assert d["branches"][0]["causal_rank_on_kernel_floor"] == {"timelike": 98470, "spacelike": 98470, "null": 106634}
    assert d["branches_currently_supplied"] == 0
    assert d["prior_negative_capture_floor_retained"] == {"timelike": 6, "spacelike": 6, "null": 4}
    assert d["stronger_radical_capture_floor"]["null"] == 106634
    assert len(d["functional_gates_retained"]) == 5
    assert "does not exclude a new source differential" in d["claim_ceiling"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    assert json.loads(OUTPUT.read_text()) == data
    print("K1154 controls: 11/11")
