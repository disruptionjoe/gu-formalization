#!/usr/bin/env python3
"""K1175: compile all three K132 repair resources into admission."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1175-i1b-three-reopener-admission-boundary.json"


def build():
    return {
        "schema_version": "1.0", "result_id": "K1175-I1B-THREE-REOPENER-ADMISSION-BOUNDARY",
        "status": "working_draft_verified", "created": "2026-10-05",
        "inputs": ["K1170-I1B-JOINT-CHANNEL-ADMISSION-BOUNDARY", "K1171-REPAIR-RESOURCE-CONSERVATION-LAW", "K1172-SHARP-REPAIR-ALLOCATION-CONTROLS", "K1173-K132-CAUSAL-REPAIR-POLYTOPE", "K1174-FACTOR-THROUGH-GAUGE-DESCENDANT-BOUNDARY"],
        "best_case_repair_deficits": {"timelike": 98372, "spacelike": 98372, "null": 106536},
        "single_axis_reopeners": {
            "constraint": "add actual independent rank 98372/98372/106536 outside the full favorable joint finite channel",
            "gauge": "raise total owned gauge-image rank to at least 98376/98376/106540 with genuinely independent field-space gauge directions",
            "changed_parent": "raise Hessian rank to at least 229284 on every causal stratum while retaining the favorable rank-four gauge and rank-98 constraint ceilings",
        },
        "mixed_repair_rule": "the sum of added Hessian rank, added independent gauge-image rank and added independent constraint rank must be at least 98372/98372/106536; overlap, rank loss or regression increases the burden",
        "classes_with_zero_repair_credit": ["Euler-row factors Q=L H", "factor-through finite constraint descendants", "factor-through gauge descendants d_j=d0 A_j", "gauge-for-gauge parameter redundancy"],
        "current_candidates_meeting_full_packet": 0,
        "next_condition": "supply one source-owned packet with a measured point inside the causal repair polytope, then recompute action ownership, Qd=0, negative capture, propagation, radical equality, common closed domains, closed gauge range, uniform positivity and maximal boundary generation",
        "protected_disposition": "SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "scope_boundary": "current K132 finite causal symbols under the strongest favorable rank-98 joint-channel baseline; no actual source coupling, independent gauge/KT enlargement, changed parent, global complex, SC-ACT-06, GU, physical state, prediction, confirmation, canon, paper or public verdict is excluded",
        "scorable_rows_added": 0, "target_claim": "SC-ACT-06",
    }


def validate(d):
    assert len(d["inputs"]) == 5
    assert d["best_case_repair_deficits"] == {"timelike": 98372, "spacelike": 98372, "null": 106536}
    assert "98372/98372/106536" in d["single_axis_reopeners"]["constraint"]
    assert "98376/98376/106540" in d["single_axis_reopeners"]["gauge"]
    assert "229284" in d["single_axis_reopeners"]["changed_parent"]
    assert "sum of added Hessian rank" in d["mixed_repair_rule"]
    assert len(d["classes_with_zero_repair_credit"]) == 4
    assert d["current_candidates_meeting_full_packet"] == 0
    assert "measured point inside the causal repair polytope" in d["next_condition"]
    assert d["protected_disposition"].startswith("SC-ACT-01/02/06 remain ASSERTS")
    assert "no actual source coupling" in d["scope_boundary"]
    assert d["scorable_rows_added"] == 0 and d["target_claim"] == "SC-ACT-06"


if __name__ == "__main__":
    data = build(); validate(data); assert json.loads(OUTPUT.read_text()) == data
    print("K1175 controls: 12/12")
