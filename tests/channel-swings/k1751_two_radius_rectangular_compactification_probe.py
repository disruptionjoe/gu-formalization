#!/usr/bin/env python3
"""Hostile formula and scope mutations for K1751."""
import copy, importlib.util, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/"tests/channel-swings/k1751_two_radius_rectangular_compactification.py"
s=importlib.util.spec_from_file_location("producer",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text())
mutations=[
    (("chart","inverse"),"p=c/(c+z), a=1-z, b=1+c/z, u=2-c"),
    (("chart","bijection"),"The complete chart is all of R2."),
    (("decision","exact_rectangular_chart_proved"),False),
    (("decision","global_optimizer_proved"),True),
    (("scope_guard",),"This proves the physical global optimizer."),
]
def setp(d,path,val):
    for k in path[:-1]:d=d[k]
    d[path[-1]]=val
for i,(path,val) in enumerate(mutations,1):
    d=copy.deepcopy(base);setp(d,path,val)
    assert not all(ok for _,ok in m.validate(d)),path
    print(f"PASS {i:02d}: rejected {'.'.join(path)}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
