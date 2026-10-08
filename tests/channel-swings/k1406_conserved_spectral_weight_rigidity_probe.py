#!/usr/bin/env python3
"""Mutation probe for K1406."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1406-conserved-spectral-weight-rigidity.json").read_text())
def validate(x):
 f,q=x["rigidity"],x["decision"];e=[]
 for key,needle in (("claim_class","Time-independent"),("sufficiency","w=c"),("current_test","q(w(q)-c)=0"),("radial_test","w(q)=c"),("necessity","full active spectral support"),("coercivity_consequence","unbounded"),("reopeners","additional structure"),("boundary","not for all")):
  if needle not in f[key]:e.append(key)
 if not q["constant_weight_necessary_for_universal_conservation"]:e.append("necessity decision")
 if q["nonlinear_or_time_dependent_modified_energy_excluded"]:e.append("overclaim")
 return e
assert not validate(D)
mutations=[("class",lambda x:x["rigidity"].__setitem__("claim_class","all energies")),("sufficiency",lambda x:x["rigidity"].__setitem__("sufficiency","none")),("current",lambda x:x["rigidity"].__setitem__("current_test","none")),("radial",lambda x:x["rigidity"].__setitem__("radial_test","none")),("necessity",lambda x:x["rigidity"].__setitem__("necessity","partial")),("coercivity",lambda x:x["rigidity"].__setitem__("coercivity_consequence","none")),("reopeners",lambda x:x["rigidity"].__setitem__("reopeners","none")),("boundary",lambda x:x["rigidity"].__setitem__("boundary","all modified energies")),("decision",lambda x:x["decision"].__setitem__("constant_weight_necessary_for_universal_conservation",False)),("overclaim",lambda x:x["decision"].__setitem__("nonlinear_or_time_dependent_modified_energy_excluded",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
