#!/usr/bin/env python3
"""Hostile interval, ordering and scope mutations for K1763."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1763_hermite_degree_escalation.py"
s=importlib.util.spec_from_file_location("producer",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text());muts=[
 (("backend",),"binary-float quadrature"),
 (("certificate","candidate_upper"),"[1e-8 +/- 1e-30]"),
 (("certificate","projections","rademacher","5"),"[1e-8 +/- 1e-30]"),
 (("certificate","projections","near_control","9"),"[1e-8 +/- 1e-30]"),
 (("decision","degree_escalation_certified_at_named_controls"),False),
 (("decision","global_interval_cover_completed"),True),
 (("decision","global_optimizer_proved"),True)]
def setp(d,path,val):
 for k in path[:-1]:d=d[k]
 d[path[-1]]=val
for i,(path,val) in enumerate(muts,1):
 d=copy.deepcopy(base);setp(d,path,val);assert not all(ok for _,ok in m.validate(d)),path;print(f"PASS {i:02d}: rejected {'.'.join(path)}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
