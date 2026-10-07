#!/usr/bin/env python3
"""Data-mutation probe for K1352."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1352-uniform-phase-and-charge-sector-obstruction.json").read_text())
def validate(x):
 s,c,q=x["scalar_phase_theorem"],x["charge_sector_theorem"],x["decision"]; e=[]
 if "irreducible" not in s["representation"]: e.append("irreducibility")
 if "X=0 and q=0" not in s["result"]: e.append("trivial result")
 if "centralizer or normalizer" not in c["surviving_scope"]: e.append("surviving scope")
 if q["nontrivial_internal_uniform_scalar_phase_exists"]: e.append("uniform phase overclaim")
 if q["nonzero_fixed_charge_sector_full_G_invariant"]: e.append("charged sector overclaim")
 if not q["k1346_phase_is_external_commuting_u1_for_this_control"]: e.append("external typing")
 if q["nonuniform_subgroup_charge_decomposition_excluded"]: e.append("nonuniform overreach")
 if not q["symmetry_reduction_required_for_single_nonzero_charge_sector"]: e.append("reduction")
 if q["source_charge_selector_constructed"]: e.append("selector overclaim")
 return e
assert not validate(D),validate(D)
mutations=[
 ("irreducibility",lambda x:x["scalar_phase_theorem"].__setitem__("representation","reducible")),
 ("trivial result",lambda x:x["scalar_phase_theorem"].__setitem__("result","q nonzero")),
 ("surviving scope",lambda x:x["charge_sector_theorem"].__setitem__("surviving_scope","none")),
 ("uniform phase overclaim",lambda x:x["decision"].__setitem__("nontrivial_internal_uniform_scalar_phase_exists",True)),
 ("charged sector overclaim",lambda x:x["decision"].__setitem__("nonzero_fixed_charge_sector_full_G_invariant",True)),
 ("external typing",lambda x:x["decision"].__setitem__("k1346_phase_is_external_commuting_u1_for_this_control",False)),
 ("nonuniform overreach",lambda x:x["decision"].__setitem__("nonuniform_subgroup_charge_decomposition_excluded",True)),
 ("reduction",lambda x:x["decision"].__setitem__("symmetry_reduction_required_for_single_nonzero_charge_sector",False)),
 ("selector overclaim",lambda x:x["decision"].__setitem__("source_charge_selector_constructed",True)),
]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D); mutate(x); errors=validate(x); assert errors,label; print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 9/9")
