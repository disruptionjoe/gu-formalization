#!/usr/bin/env python3
"""K1160: integrate the source-epsilon direct-port exclusion."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1160-i1b-source-epsilon-admission-boundary.json"


def load(name):return json.loads((ROOT/"lab/process"/name).read_text())


def build():
    prior=load("k1155-i1b-euler-factor-admission-boundary.json")
    theorem=load("k1156-constraint-gauge-rank-budget.json")
    sharp=load("k1157-sharp-rank-budget-control.json")
    app=load("k1158-source-epsilon-k132-rank-budget.json")
    repair=load("k1159-source-epsilon-repair-multiplicity-boundary.json")
    return {
        "schema_version":"1.0",
        "result_id":"K1160-I1B-SOURCE-EPSILON-ADMISSION-BOUNDARY",
        "status":"working_draft_verified",
        "created":"2026-10-05",
        "inputs":[prior["result_id"],theorem["result_id"],sharp["result_id"],app["result_id"],repair["result_id"]],
        "classes_now_excluded_for_current_k132_parent":["all linear Euler-row postprocessors Q=L H","one directly or favorably transported 91-component source-epsilon moment map","one directly or favorably transported seven-invariant lock"],
        "current_candidates_meeting_full_packet":0,
        "protected_disposition":"SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "next_condition":"derive an actual source-owned high-rank field-valued nonfactor bulk-boundary or constraint differential on the K132 carrier, source-own the enormous closed gauge/KT enlargement required by K1159, or supply a changed stationary parent and recompute the packet",
        "scope_boundary":"current K132 finite causal symbols and single finite source-epsilon targets only; no global arbitrary boundary map, SC-ACT-06, GU, physical state, prediction, confirmation, canon, paper or public verdict is excluded",
        "scorable_rows_added":0,
        "target_claim":"SC-ACT-06",
    }


def validate(d):
    assert len(d["inputs"])==5
    assert len(d["classes_now_excluded_for_current_k132_parent"])==3
    assert d["classes_now_excluded_for_current_k132_parent"][0].endswith("Q=L H")
    assert "91-component" in d["classes_now_excluded_for_current_k132_parent"][1]
    assert "seven-invariant" in d["classes_now_excluded_for_current_k132_parent"][2]
    assert d["current_candidates_meeting_full_packet"]==0
    assert "remain ASSERTS" in d["protected_disposition"]
    assert "high-rank field-valued nonfactor" in d["next_condition"]
    assert "single finite source-epsilon targets only" in d["scope_boundary"]
    assert d["scorable_rows_added"]==0 and d["target_claim"]=="SC-ACT-06"


if __name__=="__main__":
    data=build();validate(data)
    assert json.loads(OUTPUT.read_text())==data
    print("K1160 controls: 11/11")
