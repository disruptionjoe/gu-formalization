#!/usr/bin/env python3
"""Data-mutation probe for K1384."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1384-finite-rectangle-nonclosure.json").read_text())
def validate(x):
 f,q=x["finite_rectangle"],x["decision"];e=[]
 if "finite S,N" not in f["assumed_hierarchy"]:e.append("hierarchy")
 if "S+3/p" not in f["top_corner"]:e.append("corner")
 if "beyond" not in f["outside"]:e.append("outside")
 if "moves the exposed corner" not in f["iteration"]:e.append("iteration")
 if "null-form" not in f["surviving_routes"]:e.append("survivors")
 if q["finite_rectangle_bare_holder_closed"]:e.append("closure overclaim")
 if not q["top_corner_loss_exact"]:e.append("loss")
 if q["null_form_closure_excluded"]:e.append("null-form overclaim")
 if q["weighted_infinite_hierarchy_excluded"]:e.append("hierarchy overclaim")
 if q["all_weaker_invariant_topologies_excluded"]:e.append("topology overclaim")
 return e
assert not validate(D),validate(D)
mutations=[("hierarchy",lambda x:x["finite_rectangle"].__setitem__("assumed_hierarchy","infinite")),("corner",lambda x:x["finite_rectangle"].__setitem__("top_corner","inside")),("outside",lambda x:x["finite_rectangle"].__setitem__("outside","inside")),("iteration",lambda x:x["finite_rectangle"].__setitem__("iteration","closes")),("survivors",lambda x:x["finite_rectangle"].__setitem__("surviving_routes","none")),("closure overclaim",lambda x:x["decision"].__setitem__("finite_rectangle_bare_holder_closed",True)),("loss",lambda x:x["decision"].__setitem__("top_corner_loss_exact",False)),("null-form overclaim",lambda x:x["decision"].__setitem__("null_form_closure_excluded",True)),("hierarchy overclaim",lambda x:x["decision"].__setitem__("weighted_infinite_hierarchy_excluded",True)),("topology overclaim",lambda x:x["decision"].__setitem__("all_weaker_invariant_topologies_excluded",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
