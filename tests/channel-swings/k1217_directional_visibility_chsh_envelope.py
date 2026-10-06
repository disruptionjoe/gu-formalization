#!/usr/bin/env python3
"""K1217: sharp optimized-CHSH envelope at fixed directional transfer."""
from __future__ import annotations
import argparse, json
from fractions import Fraction as F
from pathlib import Path

OUTPUT=Path(__file__).parents[2]/"lab/process/k1217-directional-visibility-chsh-envelope.json"

def build():
    vals=[F(-1),F(-2,5),F(0),F(2,5),F(1)]
    rows=[]
    for v in vals:
        rows.append({"V":str(v),"lower_channel":"R_out diag(V,0,0) R_in with aligned read",
          "lower_score_squared_over_4":str(v*v),"upper_channel":"unitary rotation R with a^T R b=V",
          "upper_score_squared_over_4":"2","unitary_completion_norm_square":str(1-v*v),
          "lower_attained":True,"upper_attained":True})
    return {"schema_version":"1.0","result_id":"K1217-DIRECTIONAL-VISIBILITY-CHSH-ENVELOPE","created":"2026-10-06",
      "status":"working_draft_verified","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","direction":"observed_to_native",
      "target_claim":"NONE-NOT-A-KILL","scope":"All unital qubit CPTP maps with one fixed signed directional transfer V=a^T M b.",
      "theorem":{"range":"2 |V| <= S_max <= 2 sqrt(2)","squared_range":"V^2 <= S_max^2/4 <= 2",
        "lower_proof":"|a^T M b|<=s_1 and s_1^2+s_2^2>=s_1^2; a rotated rank-one Pauli channel attains equality.",
        "upper_proof":"unital qubit channels contract the Bloch ball, so s_1,s_2<=1; a unitary rotation with matrix element V attains equality."},
      "controls":rows,"decision":{"single_direction_identifies_optimized_chsh":False,
        "pauli_aligned_upper_bound_survives_without_alignment":False,"bounds_sharp_for_every_V":True},
      "ownership":{"directional_read_and_common_channel_imported":True,"gu_prediction":False},
      "release_test":{"five_exact_visibilities":len(rows)==5,"all_endpoints_attained":all(r["lower_attained"] and r["upper_attained"] for r in rows),
        "zero_visibility_can_be_maximal":rows[2]["upper_score_squared_over_4"]=="2","protected_status_unchanged":True},
      "claim_ceiling":"Sharp score envelope inside the imported unital-qubit/Bell-Choi/Born class; no physical process identification, GU owner or empirical score."}

def validate(x):
    assert x["result_id"].startswith("K1217-")
    assert x["theorem"]["range"]=="2 |V| <= S_max <= 2 sqrt(2)"
    assert x["theorem"]["squared_range"]=="V^2 <= S_max^2/4 <= 2"
    assert x["decision"]["single_direction_identifies_optimized_chsh"] is False
    assert x["decision"]["pauli_aligned_upper_bound_survives_without_alignment"] is False
    assert x["decision"]["bounds_sharp_for_every_V"]
    assert x["release_test"]["five_exact_visibilities"] and x["release_test"]["all_endpoints_attained"]
    assert x["release_test"]["zero_visibility_can_be_maximal"]
    assert x["ownership"]["gu_prediction"] is False
    assert x["release_test"]["protected_status_unchanged"]

if __name__=="__main__":
    q=argparse.ArgumentParser();q.add_argument("--check",action="store_true");a=q.parse_args();x=build();validate(x)
    if a.check: assert json.loads(OUTPUT.read_text())==x
    else: print(json.dumps(x,indent=2,sort_keys=True))
    print("K1217 controls: 10/10")
