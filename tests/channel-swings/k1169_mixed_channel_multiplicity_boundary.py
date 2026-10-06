#!/usr/bin/env python3
"""K1169: mixed independent-channel multiplicity budget."""
import json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1169-mixed-channel-multiplicity-boundary.json"


def row(required):
    return {"required_rank":required,"necessary_inequality":"91*p+7*s>=required_rank",
            "pure_moment_minimum":math.ceil(required/91),"pure_lock_minimum":math.ceil(required/7)}


def build():
    return {
      "schema_version":"1.0","result_id":"K1169-MIXED-CHANNEL-MULTIPLICITY-BOUNDARY",
      "status":"working_draft_verified","created":"2026-10-05",
      "theorem":"p independent 91-component channels and s independent seven-component channels can capture at most 91*p+7*s directions; every overlap lowers this ceiling",
      "causal":{"timelike":row(98470),"spacelike":row(98470),"null":row(106634)},
      "mixed_controls":{
        "nonnull_fail_by_one":{"p":1082,"s":1,"capacity":91*1082+7,"deficit":1},
        "nonnull_first_pass_nearby":{"p":1082,"s":2,"capacity":91*1082+14,"surplus":6},
        "null_fail_by_three":{"p":1171,"s":10,"capacity":91*1171+70,"deficit":3},
        "null_first_pass_nearby":{"p":1171,"s":11,"capacity":91*1171+77,"surplus":4},
      },
      "descendant_rule":"factor-through derivatives and postprocessors count as zero additional independent channels",
      "ownership_boundary":"no multiplicity in this arithmetic family is source-owned; satisfying the inequality would remain necessary, not sufficient",
      "target_claim":"SC-ACT-06",
    }


def validate(d):
    assert "91*p+7*s" in d["theorem"] and "overlap lowers" in d["theorem"]
    c=d["causal"]
    assert (c["timelike"]["pure_moment_minimum"],c["null"]["pure_moment_minimum"])==(1083,1172)
    assert (c["timelike"]["pure_lock_minimum"],c["null"]["pure_lock_minimum"])==(14068,15234)
    m=d["mixed_controls"]
    assert m["nonnull_fail_by_one"]["capacity"]==98469 and m["nonnull_fail_by_one"]["deficit"]==1
    assert m["nonnull_first_pass_nearby"]["capacity"]==98476 and m["nonnull_first_pass_nearby"]["surplus"]==6
    assert m["null_fail_by_three"]["capacity"]==106631 and m["null_fail_by_three"]["deficit"]==3
    assert m["null_first_pass_nearby"]["capacity"]==106638 and m["null_first_pass_nearby"]["surplus"]==4
    assert "zero additional independent channels" in d["descendant_rule"]
    assert d["ownership_boundary"].startswith("no multiplicity")
    assert d["target_claim"]=="SC-ACT-06"


if __name__=="__main__":
    data=build(); validate(data); assert json.loads(OUTPUT.read_text())==data
    print("K1169 controls: 11/11")
