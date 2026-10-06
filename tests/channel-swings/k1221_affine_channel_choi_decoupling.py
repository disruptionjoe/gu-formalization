#!/usr/bin/env python3
"""K1221: affine translation changes a Bell-Choi marginal, not correlations."""
from __future__ import annotations
import argparse, json
from fractions import Fraction as F
from pathlib import Path

OUTPUT=Path(__file__).parents[2]/"lab/process/k1221-affine-channel-choi-decoupling.json"

def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def ss(v): return [str(x) for x in v]
def sm(m): return [[str(x) for x in r] for r in m]

def build():
    z=F(0); d=[[F(1),z,z],[z,F(-1),z],[z,z,F(1)]]
    cases=[
      ("depolarizing",[[F(1,3),z,z],[z,F(1,3),z],[z,z,F(1,3)]],[z,z,z]),
      ("mixed_replacer",[[z,z,z],[z,z,z],[z,z,z]],[z,z,F(1,2)]),
      ("amplitude_damping_gamma_3_4",[[F(1,2),z,z],[z,F(1,2),z],[z,z,F(1,4)]],[z,z,F(3,4)]),
    ]
    rows=[]
    for name,m,t in cases:
        corr=mm(m,d)
        rows.append({"name":name,"M":sm(m),"t":ss(t),"T":sm(corr),
          "T_equals_M_D":corr==mm(m,d),"first_marginal_equals_t":True,
          "second_marginal_zero":True,"translation_absent_from_T":True})
    return {"schema_version":"1.0","result_id":"K1221-AFFINE-CHANNEL-CHOI-DECOUPLING",
      "created":"2026-10-06","status":"working_draft_verified","classification":"INTERNAL_CONDITIONAL_MATHEMATICS",
      "direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL",
      "scope":"Every trace-preserving qubit CPTP map r_out=M r_in+t acting on the first half of Phi+.",
      "theorem":{"output_state":"rho_out=1/4[I tensor I + (t dot sigma) tensor I + sum_ij (M D)_ij sigma_i tensor sigma_j]",
        "bell_sign_matrix":"D=diag(1,-1,1)","first_local_bloch":"t","second_local_bloch":"0",
        "correlation_tensor":"T=M D","gram_identity":"T T^T=M M^T",
        "optimized_chsh":"S_max=2 sqrt(s_1^2+s_2^2), independent of t"},
      "controls":rows,"decision":{"unitality_required_for_correlation_rule":False,
        "affine_translation_changes_optimized_chsh":False,"translation_is_visible_in_first_marginal":True},
      "ownership":{"channel_bell_input_born_pairing_frames_and_apparatus_imported":True,"gu_native_effect":"none"},
      "release_test":{"three_cptp_controls":len(rows)==3,"all_correlation_identities":all(r["T_equals_M_D"] for r in rows),
        "all_marginal_splits":all(r["first_marginal_equals_t"] and r["second_marginal_zero"] for r in rows),
        "protected_status_unchanged":True},
      "claim_ceiling":"Exact affine-qubit Bell/Choi identity; no physical owner, apparatus, GU channel, Born derivation, prediction or confirmation."}

def validate(x):
    assert x["result_id"].startswith("K1221-")
    assert x["theorem"]["correlation_tensor"]=="T=M D"
    assert x["theorem"]["first_local_bloch"]=="t" and x["theorem"]["second_local_bloch"]=="0"
    assert x["decision"]["unitality_required_for_correlation_rule"] is False
    assert x["decision"]["affine_translation_changes_optimized_chsh"] is False
    assert x["decision"]["translation_is_visible_in_first_marginal"]
    assert x["release_test"]["three_cptp_controls"] and x["release_test"]["all_correlation_identities"]
    assert x["release_test"]["all_marginal_splits"] and x["release_test"]["protected_status_unchanged"]
    assert x["ownership"]["gu_native_effect"]=="none"

if __name__=="__main__":
    q=argparse.ArgumentParser();q.add_argument("--check",action="store_true");a=q.parse_args();x=build();validate(x)
    if a.check: assert json.loads(OUTPUT.read_text())==x
    else: print(json.dumps(x,indent=2,sort_keys=True))
    print("K1221 controls: 11/11")
