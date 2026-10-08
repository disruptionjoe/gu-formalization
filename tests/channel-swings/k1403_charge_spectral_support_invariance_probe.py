#!/usr/bin/env python3
"""Mutation probe for K1403."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1403-charge-spectral-support-invariance.json").read_text())
def validate(x):
 f,q=x["spectral_invariance"],x["decision"];e=[]
 for key,needle in (("projectors","commutes"),("projected_equation","P_B phi"),("zero_data_uniqueness","uniqueness"),("support_statement","time invariant"),("cutoff_compatibility","M<=N"),("gauge_compatibility","exp(i alpha Q)"),("boundary","does not bound")):
  if needle not in f[key]:e.append(key)
 if not q["charge_spectral_support_invariant"]:e.append("support decision")
 if q["cutoff_uniform_completed_global_bound_constructed"]:e.append("uniform overclaim")
 return e
assert not validate(D)
mutations=[("commutation",lambda x:x["spectral_invariance"].__setitem__("projectors","none")),("equation",lambda x:x["spectral_invariance"].__setitem__("projected_equation","none")),("uniqueness",lambda x:x["spectral_invariance"].__setitem__("zero_data_uniqueness","none")),("support",lambda x:x["spectral_invariance"].__setitem__("support_statement","mixes")),("cutoff",lambda x:x["spectral_invariance"].__setitem__("cutoff_compatibility","none")),("gauge",lambda x:x["spectral_invariance"].__setitem__("gauge_compatibility","none")),("boundary",lambda x:x["spectral_invariance"].__setitem__("boundary","global completion")),("decision",lambda x:x["decision"].__setitem__("charge_spectral_support_invariant",False)),("overclaim",lambda x:x["decision"].__setitem__("cutoff_uniform_completed_global_bound_constructed",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 9/9")
