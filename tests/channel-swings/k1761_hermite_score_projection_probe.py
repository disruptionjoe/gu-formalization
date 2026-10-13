#!/usr/bin/env python3
"""Hostile theorem and scope mutations for K1761."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1761_hermite_score_projection.py"
s=importlib.util.spec_from_file_location("producer",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text());muts=[
 (("theorem","score_moment"),"E[(rho+Y)H_n]=0"),
 (("theorem","finite_test"),"J(Y)<=2 alpha^T b-alpha^T G alpha for every real alpha"),
 (("theorem","optimized_test"),"J(Y)=b^T G^(-1)b always"),
 (("decision","nested_odd_degree_hierarchy_is_monotone"),False),
 (("decision","finite_projection_equals_full_fisher_in_general"),True),
 (("decision","two_radius_global_optimizer_proved"),True)]
def setp(d,path,val):
 for k in path[:-1]:d=d[k]
 d[path[-1]]=val
for i,(path,val) in enumerate(muts,1):
 d=copy.deepcopy(base);setp(d,path,val);assert not all(ok for _,ok in m.validate(d)),path;print(f"PASS {i:02d}: rejected {'.'.join(path)}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
