#!/usr/bin/env python3
"""Hostile mutations for K1793's slab-two frontier."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1793_full_fisher_slab_two_global_kkt.py";s=importlib.util.spec_from_file_location("k1793_probe_target",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);base=json.loads(m.ARTIFACT.read_text())
muts=[(("certificate","retained_leaves"),0),(("certificate","degree_nine_partition_digest"),"0"*64),(("decision","local_boundary_kkt_isolated"),False),(("decision","complete_slab_two_sublevel_excluded"),True),(("decision","every_slab_two_face_and_corner_closed"),True),(("decision","global_optimizer_proved"),True)]
def setp(d,p,v):
 for k in p[:-1]:d=d[k]
 d[p[-1]]=v
for i,(p,v) in enumerate(muts,1):d=copy.deepcopy(base);setp(d,p,v);assert not all(ok for _,ok in m.validate(d)),p;print(f"REJECT {i:02d}: {p}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
