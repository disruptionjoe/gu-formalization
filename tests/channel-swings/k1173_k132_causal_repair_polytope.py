#!/usr/bin/env python3
"""K1173: K132 causal repair-resource polytope."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1173-k132-causal-repair-polytope.json"
N, G0, C0 = 229386, 4, 98


def row(h):
    deficit = N - h - G0 - C0
    return {
        "field_dimension": N, "current_hessian_rank": h,
        "current_gauge_rank": G0, "favorable_joint_constraint_ceiling": C0,
        "best_case_repair_deficit": deficit,
        "constraint_only_total_rank_floor": N-h-G0,
        "gauge_only_total_rank_floor": N-h-C0,
        "changed_parent_hessian_rank_floor": N-G0-C0,
        "single_axis_added_rank_floor": deficit,
    }


def build():
    return {
        "schema_version": "1.0", "result_id": "K1173-K132-CAUSAL-REPAIR-POLYTOPE",
        "status": "working_draft_verified", "created": "2026-10-05",
        "inputs": ["K1171-REPAIR-RESOURCE-CONSERVATION-LAW", "K1172-SHARP-REPAIR-ALLOCATION-CONTROLS", "K1168-SOURCE-EPSILON-JOINT-CHANNEL-BOUNDARY"],
        "favorable_baseline": "grant the joint finite epsilon channel its unproved full rank-98 transport; actual rank or overlap can only increase the floors",
        "causal": {"timelike": row(130912), "spacelike": row(130912), "null": row(122748)},
        "tradeoff": "Delta h+Delta g+Delta c>=best_case_repair_deficit, where Delta c is genuinely independent actual rank beyond the favorable joint ceiling",
        "decision": "K132 needs at least 98372/98372/106536 added directions allocated among changed-parent Hessian rank, independent gauge image, and independent constraint rank",
        "necessity_not_sufficiency": "meeting the polytope floor supplies no ownership, Qd=0, negative capture, propagation, radical equality, common domains, closed range, uniform positivity or maximal generator",
        "protected_disposition": "SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "target_claim": "SC-ACT-06",
    }


def validate(d):
    assert len(d["inputs"]) == 3
    assert "unproved full rank-98" in d["favorable_baseline"]
    c = d["causal"]
    assert [c[x]["best_case_repair_deficit"] for x in ("timelike", "spacelike", "null")] == [98372, 98372, 106536]
    assert c["timelike"]["constraint_only_total_rank_floor"] == 98470
    assert c["null"]["constraint_only_total_rank_floor"] == 106634
    assert c["timelike"]["gauge_only_total_rank_floor"] == 98376
    assert c["null"]["gauge_only_total_rank_floor"] == 106540
    assert all(r["changed_parent_hessian_rank_floor"] == 229284 for r in c.values())
    assert "Delta h+Delta g+Delta c" in d["tradeoff"]
    assert "98372/98372/106536" in d["decision"]
    assert "supplies no ownership" in d["necessity_not_sufficiency"]
    assert d["protected_disposition"].startswith("SC-ACT-01/02/06 remain ASSERTS")
    assert d["target_claim"] == "SC-ACT-06"


if __name__ == "__main__":
    data = build(); validate(data); assert json.loads(OUTPUT.read_text()) == data
    print("K1173 controls: 12/12")
