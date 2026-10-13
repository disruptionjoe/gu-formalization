#!/usr/bin/env python3
"""Hostile mutations for K1792's slab-one exclusion."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1792_full_fisher_slab_one_global_kkt.py";s=importlib.util.spec_from_file_location("k1792_probe_target",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);base=json.loads(m.ARTIFACT.read_text())
muts=[(("certificate","slab_one_retained_leaves"),1),(("certificate","degree_nine_partition_digest"),"0"*64),(("decision","slab_one_complete_sublevel_excluded"),False),(("decision","slab_one_local_boundary_kkt_is_global_optimizer"),True),(("decision","slab_two_complete_sublevel_excluded"),True),(("decision","global_optimizer_proved"),True)]
def setp(d,p,v):
 for k in p[:-1]:d=d[k]
 d[p[-1]]=v
for i,(p,v) in enumerate(muts,1):d=copy.deepcopy(base);setp(d,p,v);assert not all(ok for _,ok in m.validate(d)),p;print(f"REJECT {i:02d}: {p}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
