#!/usr/bin/env python3
"""Mutation probe for K1400."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1400-global-coulomb-slice-proper-quotient.json").read_text())
def validate(x):
 f,q=x["coulomb_quotient"],x["decision"];e=[]
 for key,needle in (("bundle_scope","trivial Abelian bundle"),("hodge_solve","Delta chi_0=-div A"),("based_uniqueness","chi_0=0"),("residual_group","compact U(1)"),("properness","proper"),("triangular_compatibility","bounded automorphisms"),("energy_descent","descend")):
  if needle not in f[key]:e.append(key)
 for key in ("global_coulomb_slice_constructed","based_gauge_orbit_representative_unique","residual_action_proper","classical_quotient_hausdorff"):
  if not q[key]:e.append(key)
 for key in ("source_observed_state_space_identified","bfv_boundary_phase_space_constructed"):
  if q[key]:e.append(key)
 return e
assert not validate(D),validate(D)
mutations=[("bundle",lambda x:x["coulomb_quotient"].__setitem__("bundle_scope","nontrivial")),("solve",lambda x:x["coulomb_quotient"].__setitem__("hodge_solve","none")),("unique",lambda x:x["coulomb_quotient"].__setitem__("based_uniqueness","many")),("residual",lambda x:x["coulomb_quotient"].__setitem__("residual_group","noncompact")),("proper",lambda x:x["coulomb_quotient"].__setitem__("properness","unknown")),("triangle",lambda x:x["coulomb_quotient"].__setitem__("triangular_compatibility","unbounded")),("energy",lambda x:x["coulomb_quotient"].__setitem__("energy_descent","lost")),("slice",lambda x:x["decision"].__setitem__("global_coulomb_slice_constructed",False)),("proper decision",lambda x:x["decision"].__setitem__("residual_action_proper",False)),("source overclaim",lambda x:x["decision"].__setitem__("source_observed_state_space_identified",True)),("BFV overclaim",lambda x:x["decision"].__setitem__("bfv_boundary_phase_space_constructed",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 11/11")
