#!/usr/bin/env python3
"""Hostile cover omissions and computed-grade promotions for K1754."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1754_two_radius_domain_certification_scaffold.py"
s=importlib.util.spec_from_file_location("producer",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text());muts=[]
d=copy.deepcopy(base);d["cover_contract"]["partition"]=d["cover_contract"]["partition"][:-1];muts.append(("omit core",d))
for path,val in [(("cover_contract","corner_rule"),"Each face separately proves the corner."),
 (("cover_contract","core_method"),"Discard omitted tails even when upper bounding."),
 (("cover_contract","acceptance"),"Unresolved boxes may be ignored."),
 (("decision","global_branch_and_bound_completed"),True),
 (("decision","boundary_collars_completed"),True),
 (("scope_guard",),"The locator is a global certificate.")]:
 d=copy.deepcopy(base);x=d
 for k in path[:-1]:x=x[k]
 x[path[-1]]=val;muts.append((".".join(path),d))
for i,(label,d) in enumerate(muts,1):assert not all(ok for _,ok in m.validate(d)),label;print(f"PASS {i:02d}: rejected {label}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
