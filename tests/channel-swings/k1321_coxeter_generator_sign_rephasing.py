#!/usr/bin/env python3
"""Exact controls for K1321's Coxeter-generator sign rephasing law."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1321-coxeter-generator-sign-rephasing.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
R=D["rephasing_law"]; Q=D["decision"]
check("sign defects",R["defect_values"]==[-1,1])
for beta in (-1,1):
 for ei in (-1,1):
  for ej in (-1,1):
   left=ei*ei*ej; right=beta*ej*ej*ei
   check(f"law beta={beta} ei={ei} ej={ej}",(left==right)==(ei*ej==beta))
check("involutions and unitarity preserved",R["involutions_preserved"] and R["unitarity_preserved"])
check("commutation preserved",R["nonadjacent_commutation_preserved"])
check("K1319 defect gauge-dependent",Q["k1319_minus_one_defect_is_normalization_dependent"])
check("ceiling preserved",not Q["every_projective_unitary_representation_is_trivialized"] and not Q["analytic_intertwiner_existence_proved"] and not Q["source_or_physical_status_moves"])
assert n==14; print("RESULT: PASS 14/14")
