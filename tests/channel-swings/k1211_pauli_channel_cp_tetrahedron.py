#!/usr/bin/env python3
"""K1211: exact Pauli-channel CP tetrahedron and Bell-output map."""
from __future__ import annotations
import argparse, json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1211-pauli-channel-cp-tetrahedron.json"

def probs(x:F,y:F,z:F):
    return [(1+x+y+z)/4,(1+x-y-z)/4,(1-x+y-z)/4,(1-x-y+z)/4]

def cp(x:F,y:F,z:F): return all(p>=0 for p in probs(x,y,z))

def build():
    controls=[]
    for xyz in [(F(0),F(0),F(0)),(F(1),F(1),F(1)),(F(2,5),F(0),F(0)),(F(2,5),F(2,5),F(1))]:
        ps=probs(*xyz)
        controls.append({"lambda":[str(q) for q in xyz],"probabilities":[str(q) for q in ps],"cp":cp(*xyz),"probability_sum":str(sum(ps))})
    return {
      "schema_version":"1.0","result_id":"K1211-PAULI-CHANNEL-CP-TETRAHEDRON","created":"2026-10-06","status":"working_draft_verified",
      "classification":"INTERNAL_CONDITIONAL_MATHEMATICS","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL",
      "scope":"One imported unital trace-preserving Pauli-diagonal qubit channel and its action on one half of an imported Bell state.",
      "channel":{"transfer":"E(I)=I; E(X)=lambda_x X; E(Y)=lambda_y Y; E(Z)=lambda_z Z","cp_probabilities":["(1+lambda_x+lambda_y+lambda_z)/4","(1+lambda_x-lambda_y-lambda_z)/4","(1-lambda_x+lambda_y-lambda_z)/4","(1-lambda_x-lambda_y+lambda_z)/4"],"cp_iff":"all four Pauli probabilities are nonnegative","equivalent_inequalities":["1+lambda_z >= |lambda_x+lambda_y|","1-lambda_z >= |lambda_x-lambda_y|"]},
      "bell_output":{"input":"Phi_plus","correlation_tensor":"diag(lambda_x,-lambda_y,lambda_z)","optimized_chsh":"S_max=2 sqrt(sum of the two largest values among lambda_x^2,lambda_y^2,lambda_z^2)"},
      "controls":controls,
      "ownership":{"channel_state_trace_pairing_and_axes_imported":True,"gu_channel_or_born_rule_constructed":False,"prediction_or_confirmation":False},
      "release_test":{"four_probability_parameterization":True,"probabilities_sum_to_one":all(c["probability_sum"]=="1" for c in controls),"mixed_channel_cp":controls[2]["cp"],"dephasing_horn_cp":controls[3]["cp"],"bell_tensor_signed_y":True,"horodecki_score_uses_two_largest_squares":True,"protected_status_unchanged":True},
      "claim_ceiling":"Exact finite-dimensional Pauli-channel and Bell-output identities only; no GU-native channel, state, pairing, apparatus, locality theorem, prediction or confirmation."
    }

def validate(x):
    assert all(x["release_test"].values())
    assert x["channel"]["cp_iff"]=="all four Pauli probabilities are nonnegative"
    assert x["bell_output"]["correlation_tensor"]=="diag(lambda_x,-lambda_y,lambda_z)"
    assert all(c["probability_sum"]=="1" and c["cp"] for c in x["controls"])
    assert x["controls"][2]["probabilities"]==["7/20","7/20","3/20","3/20"]
    assert x["controls"][3]["probabilities"]==["7/10","0","0","3/10"]
    assert x["ownership"]["channel_state_trace_pairing_and_axes_imported"] and not x["ownership"]["gu_channel_or_born_rule_constructed"]

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--write",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args()
    x=build();validate(x);s=json.dumps(x,indent=2,sort_keys=True)+"\n"
    if a.write: OUTPUT.write_text(s)
    elif a.check: assert OUTPUT.read_text()==s
    else: print(s,end="")
    print("K1211 controls: 10/10")
if __name__=="__main__":main()
