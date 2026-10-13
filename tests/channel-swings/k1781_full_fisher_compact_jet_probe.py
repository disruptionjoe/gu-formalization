#!/usr/bin/env python3
"""Hostile mutations for K1781's compact second-order jet."""
import copy, importlib.util, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1781_full_fisher_compact_jet.py"
s=importlib.util.spec_from_file_location("k1781",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text());got=m.compute()
muts=[
 (("certificate","value"),"0"),(("certificate","gradient","t"),"0"),
 (("certificate","hessian","tz"),"0"),(("certificate","compact_cell_count"),351),
 (("decision","compact_window_value_gradient_hessian_certified"),False),
 (("decision","whole_line_parameter_jet_certified"),True),
 (("decision","three_slab_interval_newton_completed"),True),
]
def setp(d,path,value):
 for key in path[:-1]:d=d[key]
 d[path[-1]]=value
for i,(path,value) in enumerate(muts,1):
 d=copy.deepcopy(base);setp(d,path,value)
 assert not all(ok for _,ok in m.validate(d,got)),path
 print(f"REJECT {i:02d}: {'.'.join(path)}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
