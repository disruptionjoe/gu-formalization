#!/usr/bin/env python3
"""Data-mutation probe for K1378."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1378-coupled-charge-lift-gronwall.json").read_text())
def validate(x):
 c,q=x["coupled_identity"],x["decision"];e=[]
 if "psi=Qphi" not in c["lifted_variable"]:e.append("variable")
 if "Q commutes" not in c["commutation"]:e.append("commutation")
 if "E dot j_Q" not in c["energy_exchange"]:e.append("exchange")
 if "||E||_infinity" not in c["pointwise_bound"]:e.append("bound")
 if "integrable in time" not in c["assumptions"]:e.append("assumptions")
 if not q["conditional_coupled_charge_lift_estimate"]:e.append("estimate")
 if not q["exact_coefficient_integrability_named"]:e.append("coefficient")
 if q["base_energy_implies_coefficient_integrability"]:e.append("base overclaim")
 if q["global_large_data_theorem_proved"]:e.append("global overclaim")
 if q["nonlinear_KT_BV_BFV_properness_proved"]:e.append("BV overclaim")
 return e
assert not validate(D),validate(D)
mutations=[("variable",lambda x:x["coupled_identity"].__setitem__("lifted_variable","phi")),("commutation",lambda x:x["coupled_identity"].__setitem__("commutation","unknown")),("exchange",lambda x:x["coupled_identity"].__setitem__("energy_exchange","conserved")),("bound",lambda x:x["coupled_identity"].__setitem__("pointwise_bound","L2 only")),("assumptions",lambda x:x["coupled_identity"].__setitem__("assumptions","base energy")),("estimate",lambda x:x["decision"].__setitem__("conditional_coupled_charge_lift_estimate",False)),("coefficient",lambda x:x["decision"].__setitem__("exact_coefficient_integrability_named",False)),("base overclaim",lambda x:x["decision"].__setitem__("base_energy_implies_coefficient_integrability",True)),("global overclaim",lambda x:x["decision"].__setitem__("global_large_data_theorem_proved",True)),("BV overclaim",lambda x:x["decision"].__setitem__("nonlinear_KT_BV_BFV_properness_proved",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
