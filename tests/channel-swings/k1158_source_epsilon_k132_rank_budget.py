#!/usr/bin/env python3
"""K1158: strongest-grant source-epsilon target test against K132."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1158-source-epsilon-k132-rank-budget.json"


def load(name): return json.loads((ROOT / "lab/process" / name).read_text())


def row(kernel_dim, target_dim):
    gauge=4
    required=kernel_dim-gauge
    return {
        "kernel_dimension": kernel_dim,
        "owned_gauge_rank": gauge,
        "constraint_target_dimension": target_dim,
        "maximum_constraint_rank_on_kernel": target_dim,
        "required_constraint_rank_on_kernel": required,
        "rank_shortfall": required-target_dim,
        "budget_passes": gauge+target_dim >= kernel_dim,
    }


def build():
    k941=load("k941-source-epsilon-cotangent-moment-map.json")
    k949=load("k949-source-epsilon-seven-lock-boundary-contract.json")
    k1153=load("k1153-k132-causal-radical-capture-floor.json")
    return {
        "schema_version": "1.0",
        "result_id": "K1158-SOURCE-EPSILON-K132-RANK-BUDGET",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "inputs": [k941["result_id"], k949["result_id"], k1153["result_id"]],
        "strongest_grant": "grant an arbitrary linear transport of the source-epsilon target to the K132 carrier with maximally favorable image placement; no native bridge is claimed",
        "targets": {
            "full_moment_map_91": {"timelike": row(98474,91), "spacelike": row(98474,91), "null": row(106638,91)},
            "seven_invariant_lock": {"timelike": row(98474,7), "spacelike": row(98474,7), "null": row(106638,7)},
        },
        "direct_port_passes": False,
        "decision": "neither one 91-component cotangent moment map nor one seven-invariant lock can be the missing current-parent K132 constraint, even under the strongest favorable transport grant",
        "scope_boundary": "dimension-only direct-port exclusion; the source-epsilon parent is distinct from the K132 bulk carrier and no actual coupling, trace, domain, or physical quotient is supplied",
        "target_claim": "SC-ACT-06",
    }


def validate(d):
    assert len(d["inputs"]) == 3
    assert "maximally favorable" in d["strongest_grant"] and "no native bridge" in d["strongest_grant"]
    m=d["targets"]["full_moment_map_91"]
    s=d["targets"]["seven_invariant_lock"]
    assert m["timelike"]["rank_shortfall"] == 98379 and m["null"]["rank_shortfall"] == 106543
    assert s["timelike"]["rank_shortfall"] == 98463 and s["null"]["rank_shortfall"] == 106627
    assert all(not r["budget_passes"] for group in d["targets"].values() for r in group.values())
    assert not d["direct_port_passes"]
    assert "can be the missing" in d["decision"]
    assert "dimension-only direct-port exclusion" in d["scope_boundary"]
    assert d["target_claim"] == "SC-ACT-06"


if __name__ == "__main__":
    data=build(); validate(data)
    assert json.loads(OUTPUT.read_text()) == data
    print("K1158 controls: 12/12")
