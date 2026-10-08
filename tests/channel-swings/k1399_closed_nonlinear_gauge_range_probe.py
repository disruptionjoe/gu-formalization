#!/usr/bin/env python3
"""Mutation probe for K1399."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1399-closed-nonlinear-gauge-range.json").read_text())
def validate(x):
 f,q=x["closed_range"],x["decision"];e=[]
 for key,needle in (("generator","R_(A,phi)"),("parameter_split","mean-zero"),("based_lower_bound","Poincare"),("matter_continuity","continuous"),("constant_part","one-dimensional"),("closed_sum","finite dimensional"),("kt_effect","closed range")):
  if needle not in f[key]:e.append(key)
 for key in ("based_gauge_generator_bounded_below","constant_gauge_image_closed","full_nonlinear_gauge_generator_range_closed"):
  if not q[key]:e.append(key)
 for key in ("full_bv_complex_exactness_constructed","bfv_boundary_theory_constructed","positive_physical_hilbert_cohomology_constructed"):
  if q[key]:e.append(key)
 return e
assert not validate(D),validate(D)
mutations=[("generator",lambda x:x["closed_range"].__setitem__("generator","unknown")),("split",lambda x:x["closed_range"].__setitem__("parameter_split","none")),("Poincare",lambda x:x["closed_range"].__setitem__("based_lower_bound","none")),("matter",lambda x:x["closed_range"].__setitem__("matter_continuity","broken")),("constant",lambda x:x["closed_range"].__setitem__("constant_part","infinite")),("sum",lambda x:x["closed_range"].__setitem__("closed_sum","unknown")),("KT",lambda x:x["closed_range"].__setitem__("kt_effect","open")),("range",lambda x:x["decision"].__setitem__("full_nonlinear_gauge_generator_range_closed",False)),("BV overclaim",lambda x:x["decision"].__setitem__("full_bv_complex_exactness_constructed",True)),("BFV overclaim",lambda x:x["decision"].__setitem__("bfv_boundary_theory_constructed",True)),("Hilbert overclaim",lambda x:x["decision"].__setitem__("positive_physical_hilbert_cohomology_constructed",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 11/11")
