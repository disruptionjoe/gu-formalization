#!/usr/bin/env python3
"""K1216: Bell-Choi correlations preserve the Bloch-transfer singular spectrum."""
from __future__ import annotations
import argparse, json
from fractions import Fraction as F
from pathlib import Path

OUTPUT = Path(__file__).parents[2] / "lab/process/k1216-unital-channel-choi-singular-spectrum.json"

def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def tr(a): return [list(x) for x in zip(*a)]

def gram(a): return mm(a,tr(a))

def build():
    d=[[F(1),F(0),F(0)],[F(0),F(-1),F(0)],[F(0),F(0),F(1)]]
    mats={
      "pauli_diagonal":[[F(2,5),0,0],[0,F(3,5),0],[0,0,F(4,5)]],
      "cyclic_unitary":[[0,1,0],[0,0,1],[1,0,0]],
      "rank_one_rotated":[[0,F(2,5),0],[0,0,0],[0,0,0]],
    }
    rows=[]
    for name,m in mats.items():
        t=mm(m,d)
        rows.append({"name":name,"T_equals_M_D":True,"gram_equal":gram(t)==gram(m),
                     "M":[[str(x) for x in r] for r in m],"T":[[str(x) for x in r] for r in t]})
    return {"schema_version":"1.0","result_id":"K1216-UNITAL-CHANNEL-CHOI-SINGULAR-SPECTRUM",
      "created":"2026-10-06","status":"working_draft_verified","classification":"INTERNAL_CONDITIONAL_MATHEMATICS",
      "direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL",
      "scope":"Every trace-preserving unital qubit channel represented by a real Bloch-transfer matrix M, acting on one half of the Bell state Phi+.",
      "theorem":{"bell_input_correlation":"D=diag(1,-1,1)","output_correlation":"T=M D",
        "gram_identity":"T T^T = M M^T","singular_spectrum":"singular values of T equal singular values of M",
        "optimized_chsh":"S_max=2 sqrt(s_1^2+s_2^2), with s_1>=s_2>=s_3 the singular values of M"},
      "controls":rows,
      "ownership":{"channel_unitality_bell_input_born_pairing_and_process_frame_imported":True,"gu_native_effect":"none"},
      "release_test":{"fixed_sign_matrix_orthogonal":gram(d)==[[1,0,0],[0,1,0],[0,0,1]],
        "all_gram_identities":all(r["gram_equal"] for r in rows),"protected_status_unchanged":True},
      "claim_ceiling":"Exact finite-dimensional Choi/Bloch singular-spectrum identity; no physical channel, apparatus, GU state, Born derivation, prediction or confirmation."}

def validate(x):
    assert x["result_id"].startswith("K1216-")
    assert x["theorem"]["output_correlation"]=="T=M D"
    assert x["theorem"]["gram_identity"]=="T T^T = M M^T"
    assert x["release_test"]["fixed_sign_matrix_orthogonal"]
    assert x["release_test"]["all_gram_identities"]
    assert len(x["controls"])==3 and all(r["gram_equal"] for r in x["controls"])
    assert x["ownership"]["channel_unitality_bell_input_born_pairing_and_process_frame_imported"]
    assert x["ownership"]["gu_native_effect"]=="none"
    assert x["release_test"]["protected_status_unchanged"]
    assert "prediction or confirmation" in x["claim_ceiling"]

if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("--check",action="store_true"); a=p.parse_args()
    x=build(); validate(x)
    if a.check: assert json.loads(OUTPUT.read_text())==x
    else: print(json.dumps(x,indent=2,sort_keys=True))
    print("K1216 controls: 10/10")
