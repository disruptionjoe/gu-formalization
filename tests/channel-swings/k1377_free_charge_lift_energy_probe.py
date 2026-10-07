#!/usr/bin/env python3
"""Data-mutation probe for K1377."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1377-free-charge-lift-energy.json").read_text())
def validate(x):
 l,q=x["lift"],x["decision"];e=[]
 if "psi=Qphi" not in l["variable"]:e.append("variable")
 if "||Qpi||_2^2" not in l["energy"]:e.append("energy")
 if "Qpi in L2" not in l["phase_domain"]:e.append("domain")
 if "Q^2phi" not in l["boundary"]:e.append("boundary")
 if not q["free_charge_lift_constructed"]:e.append("construction")
 if not q["free_charge_lift_conserved"]:e.append("conservation")
 if not q["invariant_free_phase_domain_constructed"]:e.append("invariance")
 if q["k1372_one_sided_phase_space_sufficient"]:e.append("one-sided overclaim")
 if q["coupled_nonlinear_propagation_proved"]:e.append("coupled overclaim")
 if q["source_selected_domain"]:e.append("source overclaim")
 return e
assert not validate(D),validate(D)
mutations=[("variable",lambda x:x["lift"].__setitem__("variable","phi")),("energy",lambda x:x["lift"].__setitem__("energy","base energy")),("domain",lambda x:x["lift"].__setitem__("phase_domain","pi in L2")),("boundary",lambda x:x["lift"].__setitem__("boundary","no extra charge")),("construction",lambda x:x["decision"].__setitem__("free_charge_lift_constructed",False)),("conservation",lambda x:x["decision"].__setitem__("free_charge_lift_conserved",False)),("invariance",lambda x:x["decision"].__setitem__("invariant_free_phase_domain_constructed",False)),("one-sided overclaim",lambda x:x["decision"].__setitem__("k1372_one_sided_phase_space_sufficient",True)),("coupled overclaim",lambda x:x["decision"].__setitem__("coupled_nonlinear_propagation_proved",True)),("source overclaim",lambda x:x["decision"].__setitem__("source_selected_domain",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
