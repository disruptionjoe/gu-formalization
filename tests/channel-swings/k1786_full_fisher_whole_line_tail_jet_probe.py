#!/usr/bin/env python3
"""Hostile mutations for K1786's whole-line tail jet."""
import copy, importlib.util, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1786_full_fisher_whole_line_tail_jet.py"
s=importlib.util.spec_from_file_location("k1786_probe_target",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text());got=m.compute()
muts=[
 (("certificate","denominator_floor"),"0"),
 (("certificate","absolute_two_tail_bounds","value"),"0"),
 (("certificate","absolute_two_tail_bounds","gradient","t"),"0"),
 (("certificate","absolute_two_tail_bounds","hessian","tt"),"0"),
 (("decision","whole_line_local_parameter_jet_certified"),False),
 (("decision","whole_slab_parameter_jet_certified"),True),
]
def setp(d,p,v):
 for key in p[:-1]:d=d[key]
 d[p[-1]]=v
for i,(p,v) in enumerate(muts,1):
 d=copy.deepcopy(base);setp(d,p,v);assert not all(ok for _,ok in m.validate(d,got)),p;print(f"REJECT {i:02d}: {'.'.join(p)}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
