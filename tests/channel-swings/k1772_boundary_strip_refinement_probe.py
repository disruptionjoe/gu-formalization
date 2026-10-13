#!/usr/bin/env python3
"""Hostile exact-partition and promotion mutations for K1772."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1772_boundary_strip_refinement.py";s=importlib.util.spec_from_file_location("p",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text());got=m.replay();muts=[(("refinement","pruned_leaves"),43),(("refinement","retained_leaves"),3),(("refinement","unresolved_leaves"),1),(("refinement","partition_digest"),"0"*64),(("decision","full_fisher_exclusion_proved"),True),(("decision","global_optimizer_proved"),True)]
def setp(d,p,v):
 for k in p[:-1]:d=d[k]
 d[p[-1]]=v
def valid(d):return d["refinement"]==got and not d["decision"]["full_fisher_exclusion_proved"] and not d["decision"]["global_optimizer_proved"]
for i,(p,v) in enumerate(muts,1):d=copy.deepcopy(base);setp(d,p,v);assert not valid(d),p;print(f"PASS {i:02d}: rejected {'.'.join(p)}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
