#!/usr/bin/env python3
"""Exact matched-path composition certificate for K1737."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/"lab/process/k1737-matched-half-order-cancellation.json").read_text());m=d["matched_path"];z=d["decision"]
 alpha=F(35,3);x0=F(35)
 q4=alpha**2/F(120)-F(7,36)*alpha+x0**2/F(5040)-x0/F(72)+F(71,48)
 half_beta=alpha/F(60)-F(7,36)
 half_x=2*x0/F(5040)-F(1,72)
 constant=alpha**2/F(12)-F(3,2)*alpha+F(2351160,362880)
 checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1737"),
  ("q4",q4==F(11,108)),("beta half cancels",half_beta==0),("x half cancels",half_x==0),
  ("constant",constant==F(139,432)),("coordinate","s=sqrt(q)" in m["coordinate"]),
  ("scaled r","r(s)=kappa_6/u^(3/2)" in m["scaled_invariants"]),("scaled x","x(s)=h_8/u^2" in m["scaled_invariants"]),
  ("equality","alpha=35/3" in m["quartic_equality"]),("law half","0*q^(9/2)" in m["law"]),
  ("law beta","beta^2/120" in m["law"]),("law xi","xi^2/5040" in m["law"]),
  ("law h10","y_0^2/362880" in m["law"]),("first varying","q^5" in m["first_tangent_varying_term"]),
  ("half false",not z["q_nine_halves_selects_tangent"]),("half zero",z["q_nine_halves_coefficient_exactly_zero"]),
  ("q5 first",z["q_five_is_first_tangent_varying_order"]),("beta optimum",z["second_order_scaled_sixth_optimum"]=="beta=0"),
  ("local guard","local regular" in d["scope_guard"])]
 assert len(checks)==20
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
