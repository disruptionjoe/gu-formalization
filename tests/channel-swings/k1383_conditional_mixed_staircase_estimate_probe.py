#!/usr/bin/env python3
"""Data-mutation probe for K1383."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1383-conditional-mixed-staircase-estimate.json").read_text())
def validate(x):
 c,q=x["conditional_staircase"],x["decision"];e=[]
 if "H^(3/p)" not in c["mixed_norm"]:e.append("norm")
 if "E_n^(1/2)" not in c["electric_bound"]:e.append("electric")
 if "dE_n/dt" not in c["energy_inequality"]:e.append("energy")
 if "time-integrable" not in c["integrability"]:e.append("integrability")
 if "assumes rather than derives" not in c["boundary"]:e.append("boundary")
 if not q["conditional_finite_p_estimate"]:e.append("estimate")
 if not q["exact_missing_norm_named"]:e.append("named")
 if q["mixed_norm_derived_from_E_n"]:e.append("derivation overclaim")
 if q["global_large_data_theorem_proved"]:e.append("global overclaim")
 if q["nonlinear_KT_BV_BFV_properness_proved"]:e.append("BV overclaim")
 return e
assert not validate(D),validate(D)
mutations=[("norm",lambda x:x["conditional_staircase"].__setitem__("mixed_norm","L2")),("electric",lambda x:x["conditional_staircase"].__setitem__("electric_bound","zero")),("energy",lambda x:x["conditional_staircase"].__setitem__("energy_inequality","conserved")),("integrability",lambda x:x["conditional_staircase"].__setitem__("integrability","none")),("boundary",lambda x:x["conditional_staircase"].__setitem__("boundary","global")),("estimate",lambda x:x["decision"].__setitem__("conditional_finite_p_estimate",False)),("named",lambda x:x["decision"].__setitem__("exact_missing_norm_named",False)),("derivation overclaim",lambda x:x["decision"].__setitem__("mixed_norm_derived_from_E_n",True)),("global overclaim",lambda x:x["decision"].__setitem__("global_large_data_theorem_proved",True)),("BV overclaim",lambda x:x["decision"].__setitem__("nonlinear_KT_BV_BFV_properness_proved",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
