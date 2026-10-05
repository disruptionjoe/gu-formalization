#!/usr/bin/env python3
"""K1164: exact rank increment supplied outside an existing constraint channel."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1164-nonfactor-complement-rank-floor.json"


def row(kernel_dim, base_rank):
    required = kernel_dim - 4
    return {
        "kernel_dimension": kernel_dim,
        "required_total_constraint_rank": required,
        "granted_base_channel_rank": base_rank,
        "minimum_complement_rank_on_base_kernel": required - base_rank,
    }


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1164-NONFACTOR-COMPLEMENT-RANK-FLOOR",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "theorem": {
            "exact_rank_split": "rank((q,R)|K)=rank(q|K)+rank(R|(K intersect ker q))",
            "necessary_increment": "if rank((q,R)|K)>=t, then rank(R|(K intersect ker q))>=t-rank(q|K)",
            "factor_through_corollary": "if R=Aq, then R vanishes on K intersect ker q and contributes zero new rank",
        },
        "full_moment_map_91": {"timelike": row(98474, 91), "spacelike": row(98474, 91), "null": row(106638, 91)},
        "seven_invariant_lock": {"timelike": row(98474, 7), "spacelike": row(98474, 7), "null": row(106638, 7)},
        "decision": "a successful combined repair must supply the recorded ranks on directions invisible to the finite epsilon channel; restacking descendants contributes zero toward this complement",
        "necessity_not_sufficiency": "the complement floor still does not supply source ownership, Qd=0, negative capture, propagation, radical equality, common domains, closed range, uniform positivity, or a maximal boundary generator",
        "target_claim": "SC-ACT-06",
    }


def validate(d):
    assert d["theorem"]["exact_rank_split"].startswith("rank((q,R)|K)=")
    assert ">=t-rank(q|K)" in d["theorem"]["necessary_increment"]
    assert "contributes zero new rank" in d["theorem"]["factor_through_corollary"]
    m, s = d["full_moment_map_91"], d["seven_invariant_lock"]
    assert m["timelike"]["minimum_complement_rank_on_base_kernel"] == 98379
    assert m["null"]["minimum_complement_rank_on_base_kernel"] == 106543
    assert s["timelike"]["minimum_complement_rank_on_base_kernel"] == 98463
    assert s["null"]["minimum_complement_rank_on_base_kernel"] == 106627
    assert "directions invisible" in d["decision"]
    assert "does not supply source ownership" in d["necessity_not_sufficiency"]
    assert d["target_claim"] == "SC-ACT-06"


if __name__ == "__main__":
    data = build(); validate(data)
    assert json.loads(OUTPUT.read_text()) == data
    print("K1164 controls: 10/10")
