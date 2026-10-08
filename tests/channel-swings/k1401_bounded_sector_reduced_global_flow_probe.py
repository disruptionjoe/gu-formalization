#!/usr/bin/env python3
"""Mutation probe for K1401."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1401-bounded-sector-reduced-global-flow.json").read_text())
def validate(x):
 f,q=x["reduced_flow"],x["decision"];e=[]
 for key,needle in (("constraint_surface","closed neutral Gauss surface"),("equivariance","equivariant"),("global_representative_flow","global"),("descent","single-valued global flow"),("continuity","continuous reduced flow"),("positive_invariant","coercive invariant"),("cutoff_boundary","no cutoff-uniform"),("physical_boundary","not a BV-BFV quantization")):
  if needle not in f[key]:e.append(key)
 for key in ("fixed_sector_global_flow_descends","reduced_flow_single_valued","reduced_flow_continuous","positive_conserved_classical_invariant_descends"):
  if not q[key]:e.append(key)
 for key in ("cutoff_uniform_reduced_global_flow_constructed","positive_gu_physical_hilbert_cohomology_constructed","source_action_identified"):
  if q[key]:e.append(key)
 return e
assert not validate(D),validate(D)
mutations=[("constraint",lambda x:x["reduced_flow"].__setitem__("constraint_surface","open")),("equivariance",lambda x:x["reduced_flow"].__setitem__("equivariance","broken")),("global",lambda x:x["reduced_flow"].__setitem__("global_representative_flow","local")),("descent",lambda x:x["reduced_flow"].__setitem__("descent","multivalued")),("continuity",lambda x:x["reduced_flow"].__setitem__("continuity","discontinuous")),("positive",lambda x:x["reduced_flow"].__setitem__("positive_invariant","none")),("cutoff",lambda x:x["reduced_flow"].__setitem__("cutoff_boundary","uniform")),("physical",lambda x:x["reduced_flow"].__setitem__("physical_boundary","quantized")),("flow",lambda x:x["decision"].__setitem__("fixed_sector_global_flow_descends",False)),("uniform overclaim",lambda x:x["decision"].__setitem__("cutoff_uniform_reduced_global_flow_constructed",True)),("Hilbert overclaim",lambda x:x["decision"].__setitem__("positive_gu_physical_hilbert_cohomology_constructed",True)),("source overclaim",lambda x:x["decision"].__setitem__("source_action_identified",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 12/12")
