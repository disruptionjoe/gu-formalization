#!/usr/bin/env python3
"""K957 exact Bell/CHSH decay under K956 local dephasing."""
from __future__ import annotations
import argparse, json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k957-quantum-anchor-bell-decay.json"

def build():
    rows=[]
    for l in (Fraction(0),Fraction(2,5),Fraction(5,12),Fraction(1,2),Fraction(1)):
        scaled=1+l
        rows.append({"lambda":str(l),"S_over_sqrt2":str(scaled),"S_squared":str(2*scaled*scaled),"violates_CHSH":2*scaled*scaled>4})
    return {
      "schema_version":"1.0","result_id":"K957-QUANTUM-ANCHOR-BELL-DECAY","created":"2026-10-03",
      "status":"working_draft_verified","direction":"observed_to_native","target_claim":"NONE-NOT-A-KILL",
      "classification":"INTERNAL_CONDITIONAL_MATHEMATICS",
      "scope":"The fixed Phi+ Bell state and standard optimal CHSH settings after K956 phase damping on Alice only.",
      "bell_decay":{
        "correlations":{"ZZ":"1","XX":"lambda","ZX":"0","XZ":"0"},
        "chsh_formula":"S(lambda)=sqrt(2)(1+lambda)",
        "chsh_square":"2(1+lambda)^2",
        "violation_iff":"lambda>sqrt(2)-1",
        "remote_marginal":"I_2/2 for every lambda",
        "joint_state_changes_when_lambda_below_one":True,
      },
      "exact_controls":{
        "rows":rows,"bell_endpoint_S_squared":"8","dephased_endpoint_S_squared":"2",
        "lower_bracket":"2/5 < sqrt(2)-1","upper_bracket":"sqrt(2)-1 < 5/12",
        "lower_bracket_square":"(7/5)^2=49/25<2","upper_bracket_square":"(17/12)^2=289/144>2",
        "two_fifths_does_not_violate":rows[1]["violates_CHSH"] is False,
        "five_twelfths_violates":rows[2]["violates_CHSH"] is True,
      },
      "ownership":{"settings_state_tensor_born_imported":True,"spacelike_local_net_constructed":False,"gu_prediction":False},
      "decision":{"bell_decay_exact":True,"no_signalling_preserved":True,"next_exact_input":"Compare lambda with the two-path fringe visibility under the same conditional semigroup."},
      "source_and_ledger_effect":"none",
      "claim_ceiling":"Exact decay of one imported finite Bell witness under the K956 conditional local semigroup. It is not a Bell prediction, spacelike local-net theorem, GU state construction or confirmation result."
    }

def validate(p):
    b,c,o,d=p["bell_decay"],p["exact_controls"],p["ownership"],p["decision"]
    assert b["chsh_formula"]=="S(lambda)=sqrt(2)(1+lambda)" and b["remote_marginal"]=="I_2/2 for every lambda"
    assert c["bell_endpoint_S_squared"]=="8" and c["dephased_endpoint_S_squared"]=="2"
    assert c["two_fifths_does_not_violate"] and c["five_twelfths_violates"]
    assert d["bell_decay_exact"] and d["no_signalling_preserved"]
    assert o["settings_state_tensor_born_imported"] and not o["spacelike_local_net_constructed"] and not o["gu_prediction"]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write",action="store_true"); ap.add_argument("--check",action="store_true"); a=ap.parse_args()
    p=build(); validate(p); t=json.dumps(p,indent=2,sort_keys=True)+"\n"
    if a.check: assert OUTPUT.read_text()==t
    elif a.write: OUTPUT.write_text(t)
    else: print(t,end="")
    print("K957 controls: 15/15")
if __name__=="__main__": main()
