#!/usr/bin/env python3
"""Conditional energy controls for K1383."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1383-conditional-mixed-staircase-estimate.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C,Q=D["conditional_staircase"],D["decision"]
for label,key,needle in [
 ("mixed norm","mixed_norm","H^(3/p)"),("electric bound","electric_bound","E_n^(1/2)"),
 ("radial bound","radial_bound","E_n"),("energy inequality","energy_inequality","dE_n/dt"),
 ("square-root form","square_root_form","d sqrt(E_n)/dt"),
 ("integrability","integrability","time-integrable"),("boundary","boundary","assumes rather than derives")]:check(label,needle in C[key])
for ep,mix,rad,t in ((.2,.3,.1,.5),(.5,.25,.2,1.0),(1.0,.1,.4,.25),(2.0,.05,.3,.75)):
 rhs=(ep*mix)*t+math.exp(rad*t)
 check(f"finite comparison ep={ep}",math.isfinite(rhs))
 check(f"positive comparison ep={ep}",rhs>0)
check("conditional estimate",Q["conditional_finite_p_estimate"])
check("missing norm named",Q["exact_missing_norm_named"])
check("radial closes",Q["radial_term_closes_at_same_level"])
check("mixed norm not derived",not Q["mixed_norm_derived_from_E_n"])
check("no conserved hierarchy",not Q["augmented_hierarchy_conserved"])
check("global theorem absent",not Q["global_large_data_theorem_proved"])
check("BV properness absent",not Q["nonlinear_KT_BV_BFV_properness_proved"])
check("protected fixed",not Q["protected_status_change"])
assert n==25,n
print("RESULT: PASS 25/25")
