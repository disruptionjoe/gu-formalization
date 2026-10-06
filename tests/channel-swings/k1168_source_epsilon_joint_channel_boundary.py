#!/usr/bin/env python3
"""K1168: strongest favorable joint 91+7 epsilon-channel grant on K132."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1168-source-epsilon-joint-channel-boundary.json"


def row(kernel_dim):
    required=kernel_dim-4
    return {"kernel_dimension":kernel_dim,"gauge_rank":4,"required_constraint_rank":required,
            "joint_target_ceiling":98,"best_case_shortfall":required-98}


def build():
    return {
        "schema_version":"1.0","result_id":"K1168-SOURCE-EPSILON-JOINT-CHANNEL-BOUNDARY",
        "status":"working_draft_verified","created":"2026-10-05",
        "inputs":["K941 91-component cotangent moment map","K949 seven-invariant lock","K1166 stacked-channel theorem","K1167 overlap controls"],
        "favorable_grant":"transport both finite targets independently to the same K132 causal kernel and grant the full direct-sum rank 98",
        "causal":{"timelike":row(98474),"spacelike":row(98474),"null":row(106638)},
        "overlap_rule":"an actual overlap defect delta raises every recorded shortfall by delta",
        "decision":"even the unproved best-case independent joint channel misses the current radical-capture floor by 98372/98372/106536",
        "necessity_not_sufficiency":"rank 98 is only a favorable ceiling; it supplies neither a coupling nor Qd=0, negative capture, propagation, radical equality, common domains, closed range, uniform positivity, or a maximal generator",
        "protected_disposition":"SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "target_claim":"SC-ACT-06",
    }


def validate(d):
    assert len(d["inputs"])==4
    assert "full direct-sum rank 98" in d["favorable_grant"]
    c=d["causal"]
    assert c["timelike"]["best_case_shortfall"]==98372
    assert c["spacelike"]["best_case_shortfall"]==98372
    assert c["null"]["best_case_shortfall"]==106536
    assert all(x["joint_target_ceiling"]==98 and x["gauge_rank"]==4 for x in c.values())
    assert d["overlap_rule"].endswith("by delta")
    assert "98372/98372/106536" in d["decision"]
    assert "supplies neither a coupling" in d["necessity_not_sufficiency"]
    assert d["protected_disposition"].startswith("SC-ACT-01/02/06 remain ASSERTS")
    assert d["target_claim"]=="SC-ACT-06"


if __name__=="__main__":
    data=build(); validate(data); assert json.loads(OUTPUT.read_text())==data
    print("K1168 controls: 10/10")
