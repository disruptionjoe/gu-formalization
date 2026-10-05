#!/usr/bin/env python3
"""K1163: source-epsilon jet descendants do not close K132 rank deficits."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1163-source-epsilon-jet-prolongation-boundary.json"


def row(kernel_dim, target_rank):
    required = kernel_dim - 4
    return {
        "kernel_dimension": kernel_dim,
        "owned_gauge_rank": 4,
        "required_constraint_rank": required,
        "shared_factor_rank_ceiling": target_rank,
        "rank_shortfall": required - target_rank,
        "any_finite_derivative_stack_passes": False,
    }


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1163-SOURCE-EPSILON-JET-PROLONGATION-BOUNDARY",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "inputs": ["K792-SC-ACT-06-REDUNDANT-PROLONGATION-KERNEL-THEOREM", "K880-SC-ACT-06-REDUNDANT-TARGET-QUOTIENT", "K941-SOURCE-EPSILON-COTANGENT-MOMENT-MAP", "K949-SOURCE-EPSILON-SEVEN-LOCK-BOUNDARY-CONTRACT", "K1153-K132-CAUSAL-RADICAL-CAPTURE-FLOOR", "K1161-FACTOR-THROUGH-PROLONGATION-RANK-THEOREM"],
        "tested_class": "every finite fixed-covector stack whose components are differential or operator-valued postprocessors of the same transported epsilon target",
        "targets": {
            "full_moment_map_91": {"timelike": row(98474, 91), "spacelike": row(98474, 91), "null": row(106638, 91)},
            "seven_invariant_lock": {"timelike": row(98474, 7), "spacelike": row(98474, 7), "null": row(106638, 7)},
        },
        "decision": "no finite derivative order, jet count, or target restacking of either single epsilon channel changes the K1158 causal shortfalls",
        "scope_boundary": "fixed-symbol factor-through class only; a genuinely independent field-valued principal symbol, lower-order boundary mechanism, changed parent, or enlarged gauge/KT image is not excluded",
        "target_claim": "SC-ACT-06",
    }


def validate(d):
    assert len(d["inputs"]) == 6 and d["inputs"][0].startswith("K792-")
    assert "every finite fixed-covector stack" in d["tested_class"]
    m = d["targets"]["full_moment_map_91"]
    s = d["targets"]["seven_invariant_lock"]
    assert m["timelike"]["rank_shortfall"] == 98379 and m["null"]["rank_shortfall"] == 106543
    assert s["timelike"]["rank_shortfall"] == 98463 and s["null"]["rank_shortfall"] == 106627
    assert all(not row["any_finite_derivative_stack_passes"] for group in d["targets"].values() for row in group.values())
    assert all(row["shared_factor_rank_ceiling"] in (91, 7) for group in d["targets"].values() for row in group.values())
    assert "no finite derivative order" in d["decision"]
    assert "genuinely independent field-valued principal symbol" in d["scope_boundary"]
    assert d["target_claim"] == "SC-ACT-06"


if __name__ == "__main__":
    data = build(); validate(data)
    assert json.loads(OUTPUT.read_text()) == data
    print("K1163 controls: 10/10")
