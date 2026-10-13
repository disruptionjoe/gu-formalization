#!/usr/bin/env python3
"""Hostile coordinate, cancellation and scope mutations for K1766."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1766_correlated_hermite_rational.py"
s=importlib.util.spec_from_file_location("producer",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text());rows=m.compute();muts=[
 (("coordinate","substitution"),"c=2-q/t"),(("cancelled_tests","degree_five_threshold_polynomial_terms"),70),(("cancelled_tests","degree_seven_threshold_polynomial_terms"),256),(("cancelled_tests","threshold"),"1/1"),(("decision","matched_coordinate_preserves_c_t_correlation"),False),(("decision","raw_moment_substitution_at_z_zero_is_allowed"),True),(("decision","full_fisher_computed_by_the_rational_tests"),True)]
def setp(d,path,val):
 for k in path[:-1]:d=d[k]
 d[path[-1]]=val
for i,(path,val) in enumerate(muts,1):
 d=copy.deepcopy(base);setp(d,path,val);assert not all(ok for _,ok in m.validate(d,rows)),path;print(f"PASS {i:02d}: rejected {'.'.join(path)}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
