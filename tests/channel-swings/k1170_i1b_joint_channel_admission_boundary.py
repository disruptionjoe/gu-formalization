#!/usr/bin/env python3
"""K1170: compile the joint finite-channel exclusion into I1B admission."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1170-i1b-joint-channel-admission-boundary.json"


def build():
    return {
      "schema_version":"1.0","result_id":"K1170-I1B-JOINT-CHANNEL-ADMISSION-BOUNDARY",
      "status":"working_draft_verified","created":"2026-10-05",
      "inputs":["K1165-I1B-PROLONGATION-ADMISSION-BOUNDARY","K1166-STACKED-CONSTRAINT-RANK-SPLIT","K1167-INDEPENDENT-OVERLAP-CHANNEL-CONTROLS","K1168-SOURCE-EPSILON-JOINT-CHANNEL-BOUNDARY","K1169-MIXED-CHANNEL-MULTIPLICITY-BOUNDARY"],
      "classes_now_excluded_for_current_k132_parent":[
        "all linear Euler-row postprocessors Q=L H",
        "either retained finite source-epsilon target used singly",
        "the strongest favorable direct sum of the 91-component moment map and seven-invariant lock",
        "every finite fixed-covector descendant stack factoring through any of those finite channels"
      ],
      "best_case_joint_shortfalls":{"timelike":98372,"spacelike":98372,"null":106536},
      "current_candidates_meeting_full_packet":0,
      "next_condition":"derive a source-owned bulk-boundary or constraint symbol with at least 98372/98372/106536 directions outside the strongest joint finite epsilon channel on the K132 causal radical, source-own the complementary enlarged closed gauge/KT image, or supply a changed stationary parent and recompute every gate",
      "protected_disposition":"SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
      "scope_boundary":"current K132 finite causal symbols and favorable joint transport of the two retained epsilon targets only; no actual coupling, genuinely independent field-valued map, arbitrary boundary operator, SC-ACT-06, GU, physical state, prediction, confirmation, canon, paper or public verdict is excluded",
      "scorable_rows_added":0,"target_claim":"SC-ACT-06",
    }


def validate(d):
    assert len(d["inputs"])==5 and len(d["classes_now_excluded_for_current_k132_parent"])==4
    assert "Euler-row" in d["classes_now_excluded_for_current_k132_parent"][0]
    assert "used singly" in d["classes_now_excluded_for_current_k132_parent"][1]
    assert "strongest favorable direct sum" in d["classes_now_excluded_for_current_k132_parent"][2]
    assert "factoring through" in d["classes_now_excluded_for_current_k132_parent"][3]
    assert d["best_case_joint_shortfalls"]=={"timelike":98372,"spacelike":98372,"null":106536}
    assert d["current_candidates_meeting_full_packet"]==0
    assert "98372/98372/106536" in d["next_condition"]
    assert d["protected_disposition"].startswith("SC-ACT-01/02/06 remain ASSERTS")
    assert "no actual coupling" in d["scope_boundary"]
    assert d["scorable_rows_added"]==0 and d["target_claim"]=="SC-ACT-06"


if __name__=="__main__":
    data=build(); validate(data); assert json.loads(OUTPUT.read_text())==data
    print("K1170 controls: 11/11")
