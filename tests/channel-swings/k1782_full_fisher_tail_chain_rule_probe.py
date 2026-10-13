#!/usr/bin/env python3
"""Hostile mutations for K1782's chain-rule boundary."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1782_full_fisher_tail_chain_rule.py";s=importlib.util.spec_from_file_location("k1782",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text());got=m.compute();muts=[(("chart_bounds","slabs",0,"minimum_p"),"0"),(("chart_bounds","slabs",1,"maximum_first_derivative_magnitude"),"0"),(("decision","chart_chain_rule_finite_on_three_slabs"),False),(("decision","whole_line_full_fisher_quotient_tail_composed"),True),(("decision","three_slab_interval_newton_completed"),True)]
def setp(d,path,v):
 for k in path[:-1]:d=d[k]
 d[path[-1]]=v
for i,(p,v) in enumerate(muts,1):
 d=copy.deepcopy(base);setp(d,p,v);assert not all(x for _,x in m.validate(d,got)),p;print(f"REJECT {i:02d}: {p}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
