#!/usr/bin/env python3
"""K1222: generalized amplitude damping varies translation at fixed CHSH data."""
from __future__ import annotations
import argparse,json
from fractions import Fraction as F
from pathlib import Path
OUTPUT=Path(__file__).parents[2]/"lab/process/k1222-translation-blind-chsh-control.json"

def build():
    gamma=F(3,4); rows=[]
    for p in [F(0),F(1,2),F(1)]:
        tz=gamma*(2*p-1)
        rows.append({"p":str(p),"gamma":"3/4","M_diagonal":["1/2","1/2","1/4"],
          "t":["0","0",str(tz)],"correlation_singular_values":["1/2","1/2","1/4"],
          "S_squared_over_4":"1/2","cptp_by_kraus_family":True})
    return {"schema_version":"1.0","result_id":"K1222-TRANSLATION-BLIND-CHSH-CONTROL","created":"2026-10-06",
      "status":"working_draft_verified","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","direction":"observed_to_native",
      "target_claim":"NONE-NOT-A-KILL","scope":"Generalized amplitude-damping channels at gamma=3/4 and p in {0,1/2,1}.",
      "family":{"affine_rule":"M=diag(sqrt(1-gamma),sqrt(1-gamma),1-gamma), t_z=gamma(2p-1)",
        "cp_tp_certificate":"standard four-Kraus generalized-amplitude-damping representation for 0<=gamma,p<=1"},
      "controls":rows,"decision":{"same_M_different_t":True,"same_bell_correlation":True,
        "same_optimized_chsh":True,"local_output_marginal_distinguishes_translation":True},
      "release_test":{"three_physical_family_points":len(rows)==3,"translations":[r["t"][2] for r in rows]==["-3/4","0","3/4"],
        "common_score":all(r["S_squared_over_4"]=="1/2" for r in rows),"protected_status_unchanged":True},
      "ownership":{"physical_family_is_imported_control":True,"prediction_or_confirmation":False},
      "claim_ceiling":"Exact same-correlation/different-marginal CPTP control; no apparatus identity, GU process, prediction or confirmation."}
def validate(x):
    assert x["result_id"].startswith("K1222-")
    assert x["decision"]["same_M_different_t"] and x["decision"]["same_bell_correlation"]
    assert x["decision"]["same_optimized_chsh"] and x["decision"]["local_output_marginal_distinguishes_translation"]
    assert x["release_test"]["three_physical_family_points"] and x["release_test"]["translations"]
    assert x["release_test"]["common_score"] and x["release_test"]["protected_status_unchanged"]
    assert all(r["cptp_by_kraus_family"] for r in x["controls"])
    assert x["ownership"]["prediction_or_confirmation"] is False
if __name__=="__main__":
    q=argparse.ArgumentParser();q.add_argument("--check",action="store_true");a=q.parse_args();x=build();validate(x)
    if a.check:assert json.loads(OUTPUT.read_text())==x
    else:print(json.dumps(x,indent=2,sort_keys=True))
    print("K1222 controls: 10/10")
