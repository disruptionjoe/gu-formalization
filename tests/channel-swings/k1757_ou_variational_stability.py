#!/usr/bin/env python3
"""Exact arithmetic audit of K1757's OU variational stability modulus."""
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1757-ou-variational-stability.json"
def validate(d):
 e=d["derivative_envelope"];z=d["decision"]
 k0=2*e["A_bound"]+2*e["second_derivative_bound"]+2*e["A_bound"]*e["first_derivative_bound"]
 k1=2*e["C_bound"]+2*e["first_derivative_bound"]+2*e["C_bound"]*e["first_derivative_bound"]
 return [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1757"),
  ("variational","sup_f" in d["setting"]["variational_identity"]),("coupling","same-sign" in d["setting"]["rare_chart_coupling"]),
  ("W2","<=2z" in d["setting"]["wasserstein_bound"]),("t range",d["setting"]["parameter_range"]=="t<=31/32 and v>=1/32"),
  ("A",e["A_bound"]==32),("C",e["C_bound"]==31),("D1",e["first_derivative_bound"]>=1023),
  ("D2",e["second_derivative_bound"]>=65536),("k0",e["constant_term_bound"]>=k0),
  ("k1",e["linear_term_bound"]>=k1),("rounded",e["rounded_stability_constant"]>=k0+2*k1),
  ("theorem","400000 sqrt(2z)" in d["theorem"]),("proved",z["explicit_stability_modulus_proved"]),
  ("uniform",z["uniform_in_c_on_declared_t_range"]),("second moment",z["uses_only_second_moments_after_test_selection"]),
  ("continuity fenced",not z["rare_atom_face_identified_with_pointwise_continuity"]),("global fenced",not z["global_optimizer_proved"])]
def main():
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
