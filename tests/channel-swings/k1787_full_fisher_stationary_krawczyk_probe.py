#!/usr/bin/env python3
"""Hostile mutations for K1787's whole-line Krawczyk box."""
import copy, importlib.util, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1787_full_fisher_stationary_krawczyk.py"
s=importlib.util.spec_from_file_location("k1787_probe_target",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text());got=m.compute()
muts=[
 (("certificate","full_hessian_tt_on_box"),"0"),
 (("certificate","full_hessian_determinant_on_box"),"0"),
 (("certificate","stationary_value_enclosure"),"0"),
 (("certificate","strict_inclusion","t"),False),
 (("certificate","strict_inclusion","z"),False),
 (("decision","unique_whole_line_stationary_point_in_named_box"),False),
 (("decision","unique_stationary_point_on_complete_slab_three"),True),
 (("decision","global_optimizer_proved"),True),
]
def setp(d,p,v):
 for key in p[:-1]:d=d[key]
 d[p[-1]]=v
for i,(p,v) in enumerate(muts,1):
 d=copy.deepcopy(base);setp(d,p,v);assert not all(ok for _,ok in m.validate(d,got)),p;print(f"REJECT {i:02d}: {'.'.join(p)}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
