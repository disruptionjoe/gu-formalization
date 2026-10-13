#!/usr/bin/env python3
"""Hostile mutations for K1789's local candidate comparison."""
import copy, importlib.util, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1789_full_fisher_global_comparison.py"
s=importlib.util.spec_from_file_location("k1789_probe_target",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text());got=m.compute()
muts=[
 (("certificate","slab_three_candidate_value"),"0"),
 (("certificate","comparisons",0,"lower_gap_above_slab_three_local_point"),"0"),
 (("certificate","comparisons",1,"lower_gap_above_slab_three_local_point"),"0"),
 (("decision","three_local_candidates_strictly_ordered"),False),
 (("decision","global_optimizer_proved"),True),
]
def setp(d,p,v):
 for key in p[:-1]:d=d[key]
 d[p[-1]]=v
for i,(p,v) in enumerate(muts,1):
 d=copy.deepcopy(base);setp(d,p,v);assert not all(ok for _,ok in m.validate(d,got)),p;print(f"REJECT {i:02d}: {p}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
