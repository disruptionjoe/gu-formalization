#!/usr/bin/env python3
"""Hostile mutations for K1794's slab-three frontier."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1794_full_fisher_slab_three_global_stationarity.py";s=importlib.util.spec_from_file_location("k1794_probe_target",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);base=json.loads(m.ARTIFACT.read_text())
muts=[(("certificate","retained_leaves"),0),(("certificate","degree_nine_partition_digest"),"0"*64),(("decision","local_interior_stationary_point_isolated"),False),(("decision","unique_stationary_point_on_complete_slab_three"),True),(("decision","every_slab_three_face_and_corner_closed"),True),(("decision","global_optimizer_proved"),True)]
def setp(d,p,v):
 for k in p[:-1]:d=d[k]
 d[p[-1]]=v
for i,(p,v) in enumerate(muts,1):d=copy.deepcopy(base);setp(d,p,v);assert not all(ok for _,ok in m.validate(d)),p;print(f"REJECT {i:02d}: {p}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
