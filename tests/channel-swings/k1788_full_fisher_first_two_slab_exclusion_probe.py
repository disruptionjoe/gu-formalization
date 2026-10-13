#!/usr/bin/env python3
"""Hostile mutations for K1788's local boundary KKT boxes."""
import copy, importlib.util, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1788_full_fisher_first_two_slab_exclusion.py"
s=importlib.util.spec_from_file_location("k1788_probe_target",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text());got=m.compute()
muts=[
 (("certificate","boundary_boxes",0,"strict_inclusion"),False),
 (("certificate","boundary_boxes",0,"strict_kkt_inward_sign"),False),
 (("certificate","boundary_boxes",1,"strict_inclusion"),False),
 (("certificate","boundary_boxes",1,"strict_kkt_inward_sign"),False),
 (("decision","unique_local_boundary_kkt_points"),1),
 (("decision","slabs_one_and_two_globally_excluded"),True),
]
def setp(d,p,v):
 for key in p[:-1]:d=d[key]
 d[p[-1]]=v
for i,(p,v) in enumerate(muts,1):
 d=copy.deepcopy(base);setp(d,p,v);assert not all(ok for _,ok in m.validate(d,got)),p;print(f"REJECT {i:02d}: {p}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
