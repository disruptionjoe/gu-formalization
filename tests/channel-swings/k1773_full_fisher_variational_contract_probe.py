#!/usr/bin/env python3
"""Hostile direction, boundary and promotion mutations for K1773."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1773_full_fisher_variational_contract.py";s=importlib.util.spec_from_file_location("p",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);base=json.loads(m.ARTIFACT.read_text())
muts=[(("contract","inequality_direction"),"J<=V"),(("contract","boundary_sectors"),[]),(("contract","tail_control"),"omitted"),(("decision","sectorized_arb_cover_completed"),True),(("decision","boundary_strip_excluded"),True)]
def setp(d,p,v):
 for k in p[:-1]:d=d[k]
 d[p[-1]]=v
for i,(p,v) in enumerate(muts,1):d=copy.deepcopy(base);setp(d,p,v);assert not all(ok for _,ok in m.validate(d)),p;print(f"PASS {i:02d}: rejected {'.'.join(p)}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
