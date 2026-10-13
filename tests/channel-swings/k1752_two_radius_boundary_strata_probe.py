#!/usr/bin/env python3
"""Hostile boundary omissions and promotions for K1752."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1752_two_radius_boundary_strata.py"
s=importlib.util.spec_from_file_location("producer",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text()); muts=[]
d=copy.deepcopy(base);del d["boundary_strata"]["z_zero"];muts.append(("omit rare atom",d))
for path,val in [(("boundary_strata","c_two_minus_q","fisher_type"),"finite interior formula"),
                 (("boundary_strata","joint_corner","warning"),"Each face settles the corner."),
                 (("decision","all_boundary_collars_excluded"),True),
                 (("scope_guard",),"All collars are globally excluded.")]:
 d=copy.deepcopy(base);x=d
 for k in path[:-1]:x=x[k]
 x[path[-1]]=val;muts.append((".".join(path),d))
def rejected(d):
 try:return not all(ok for _,ok in m.validate(d))
 except (KeyError,TypeError,ValueError):return True
for i,(label,d) in enumerate(muts,1):assert rejected(d),label;print(f"PASS {i:02d}: rejected {label}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
