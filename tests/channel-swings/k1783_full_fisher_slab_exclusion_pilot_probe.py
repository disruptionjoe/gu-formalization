#!/usr/bin/env python3
"""Hostile mutations for K1783's computed-only ceiling."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1783_full_fisher_slab_exclusion_pilot.py";s=importlib.util.spec_from_file_location("k1783",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text());got=m.compute();muts=[(("computed_pilot","slabs",0,"compact_value"),"0"),(("decision","slabs_one_and_two_excluded"),True),(("decision","stationary_box_isolated"),True),(("decision","global_optimizer_proved"),True)]
def setp(d,p,v):
 for k in p[:-1]:d=d[k]
 d[p[-1]]=v
for i,(p,v) in enumerate(muts,1):d=copy.deepcopy(base);setp(d,p,v);assert not all(x for _,x in m.validate(d,got)),p;print(f"REJECT {i:02d}: {p}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
