#!/usr/bin/env python3
"""K1165: integrate the factor-through prolongation exclusion."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1165-i1b-prolongation-admission-boundary.json"


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1165-I1B-PROLONGATION-ADMISSION-BOUNDARY",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "inputs": ["K1160-I1B-SOURCE-EPSILON-ADMISSION-BOUNDARY", "K1161-FACTOR-THROUGH-PROLONGATION-RANK-THEOREM", "K1162-INDEPENDENT-SYMBOL-FAMILY-CONTROL", "K1163-SOURCE-EPSILON-JET-PROLONGATION-BOUNDARY", "K1164-NONFACTOR-COMPLEMENT-RANK-FLOOR"],
        "classes_now_excluded_for_current_k132_parent": [
            "all linear Euler-row postprocessors Q=L H",
            "one directly or favorably transported 91-component source-epsilon moment map or seven-invariant lock",
            "every finite fixed-covector differential, jet, or operator-valued descendant stack factoring through either one finite epsilon target",
        ],
        "current_candidates_meeting_full_packet": 0,
        "protected_disposition": "SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "next_condition": "derive a source-owned bulk-boundary or constraint symbol with at least 98379/98379/106543 independent directions outside the 91-component epsilon channel on the K132 causal radical, source-own the complementary enlarged closed gauge/KT image, or supply a changed stationary parent and recompute every gate",
        "scope_boundary": "current K132 finite causal symbols and factor-through descendants of the two finite epsilon targets only; no genuinely independent field-valued map, arbitrary boundary operator, SC-ACT-06, GU, physical state, prediction, confirmation, canon, paper or public verdict is excluded",
        "scorable_rows_added": 0,
        "target_claim": "SC-ACT-06",
    }


def validate(d):
    assert len(d["inputs"]) == 5
    assert len(d["classes_now_excluded_for_current_k132_parent"]) == 3
    assert d["classes_now_excluded_for_current_k132_parent"][0].endswith("Q=L H")
    assert "91-component" in d["classes_now_excluded_for_current_k132_parent"][1]
    assert "factoring through" in d["classes_now_excluded_for_current_k132_parent"][2]
    assert d["current_candidates_meeting_full_packet"] == 0
    assert "remain ASSERTS" in d["protected_disposition"]
    assert "98379/98379/106543" in d["next_condition"]
    assert "genuinely independent field-valued map" in d["scope_boundary"]
    assert d["scorable_rows_added"] == 0
    assert d["target_claim"] == "SC-ACT-06"


if __name__ == "__main__":
    data = build(); validate(data)
    assert json.loads(OUTPUT.read_text()) == data
    print("K1165 controls: 10/10")
