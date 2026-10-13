#!/usr/bin/env python3
"""Hostile recurrence, formula and scope mutations for K1762."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1762_two_radius_hermite_moments.py"
s=importlib.util.spec_from_file_location("producer",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text());muts=[
 (("central_moment_recurrence",),"mu_r=(c/z+z)mu_(r-1)"),
 (("closed_forms","h6"),"t^3*(c^2+c*z^2)/z"),
 (("closed_forms","h10"),"0"),
 (("decision","degree_nine_gram_data_closed_exactly"),False),
 (("decision","moment_lower_bounds_require_density_quadrature"),True),
 (("decision","moments_determine_full_fisher_exactly"),True)]
def setp(d,path,val):
 for k in path[:-1]:d=d[k]
 d[path[-1]]=val
for i,(path,val) in enumerate(muts,1):
 d=copy.deepcopy(base);setp(d,path,val);assert not all(ok for _,ok in m.validate(d)),path;print(f"PASS {i:02d}: rejected {'.'.join(path)}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
