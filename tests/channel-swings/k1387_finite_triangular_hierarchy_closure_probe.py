#!/usr/bin/env python3
"""Data-mutation probe for K1387."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1387-finite-triangular-hierarchy-closure.json").read_text())
def validate(x):
 t,q=x["triangular_hierarchy"],x["decision"];e=[]
 if "|alpha|+n<=R" not in t["index_set"]:e.append("index")
 if "mu||Q D^alpha Q^n phi||_2^2" not in t["matter_energy"]:e.append("energy")
 if "<=R+1" not in t["principal_tier"]:e.append("tier")
 if "fixed combined order" not in t["comparison"]:e.append("comparison")
 if not q["finite_triangular_hierarchy_constructed"]:e.append("construction")
 if not q["commutator_terms_close_in_principal_tier"]:e.append("commutator")
 if q["finite_rectangular_bare_holder_claim_reversed"]:e.append("rectangle reversal")
 if q["coefficient_global_integrability_proved"]:e.append("global overclaim")
 if q["solution_existence_proved"]:e.append("existence overclaim")
 if q["source_action_identified"]:e.append("source overclaim")
 return e
assert not validate(D),validate(D)
mutations=[("index",lambda x:x["triangular_hierarchy"].__setitem__("index_set","rectangle")),("energy",lambda x:x["triangular_hierarchy"].__setitem__("matter_energy","base energy")),("tier",lambda x:x["triangular_hierarchy"].__setitem__("principal_tier","unbounded")),("comparison",lambda x:x["triangular_hierarchy"].__setitem__("comparison","same rectangle")),("construction",lambda x:x["decision"].__setitem__("finite_triangular_hierarchy_constructed",False)),("commutator",lambda x:x["decision"].__setitem__("commutator_terms_close_in_principal_tier",False)),("rectangle reversal",lambda x:x["decision"].__setitem__("finite_rectangular_bare_holder_claim_reversed",True)),("global overclaim",lambda x:x["decision"].__setitem__("coefficient_global_integrability_proved",True)),("existence overclaim",lambda x:x["decision"].__setitem__("solution_existence_proved",True)),("source overclaim",lambda x:x["decision"].__setitem__("source_action_identified",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
