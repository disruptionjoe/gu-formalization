#!/usr/bin/env python3
"""K1159: quantify source-epsilon copy and gauge-enlargement necessities."""
import json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1159-source-epsilon-repair-multiplicity-boundary.json"


def row(kernel_dim,target_dim):
    required=kernel_dim-4
    return {
        "kernel_dimension": kernel_dim,
        "target_dimension_per_copy": target_dim,
        "minimum_copies_with_rank4_gauge": math.ceil(required/target_dim),
        "minimum_gauge_rank_with_one_copy": kernel_dim-target_dim,
        "minimum_added_gauge_rank_over_current": kernel_dim-target_dim-4,
    }


def build():
    return {
        "schema_version":"1.0",
        "result_id":"K1159-SOURCE-EPSILON-REPAIR-MULTIPLICITY-BOUNDARY",
        "status":"working_draft_verified",
        "created":"2026-10-05",
        "full_moment_map_91":{"timelike":row(98474,91),"spacelike":row(98474,91),"null":row(106638,91)},
        "seven_invariant_lock":{"timelike":row(98474,7),"spacelike":row(98474,7),"null":row(106638,7)},
        "ownership_status":"no source-owned 1083/1172-copy moment-map constraint, 14068/15234-copy invariant lock, or complementary enlarged closed gauge/KT image is serialized",
        "necessity_not_sufficiency":"meeting a copy or gauge rank floor would still require Qd=0, negative capture, propagation, radical equality, common domains, closed range, uniform positivity, and a maximal boundary generator",
        "target_claim":"SC-ACT-06",
    }


def validate(d):
    m=d["full_moment_map_91"]; s=d["seven_invariant_lock"]
    assert m["timelike"]["minimum_copies_with_rank4_gauge"]==1083
    assert m["null"]["minimum_copies_with_rank4_gauge"]==1172
    assert m["timelike"]["minimum_gauge_rank_with_one_copy"]==98383
    assert m["null"]["minimum_gauge_rank_with_one_copy"]==106547
    assert s["timelike"]["minimum_copies_with_rank4_gauge"]==14068
    assert s["null"]["minimum_copies_with_rank4_gauge"]==15234
    assert s["timelike"]["minimum_gauge_rank_with_one_copy"]==98467
    assert s["null"]["minimum_gauge_rank_with_one_copy"]==106631
    assert "no source-owned 1083/1172-copy" in d["ownership_status"]
    assert "would still require" in d["necessity_not_sufficiency"]
    assert d["target_claim"]=="SC-ACT-06"


if __name__=="__main__":
    data=build();validate(data)
    assert json.loads(OUTPUT.read_text())==data
    print("K1159 controls: 11/11")
