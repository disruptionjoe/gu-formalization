#!/usr/bin/env python3
"""Hostile density, positivity and scope mutations for K1767."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1767_hermite_gram_positivity.py";s=importlib.util.spec_from_file_location("producer",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text());rows=m.controls();muts=[(("theorem","density"),"Y is discrete"),(("theorem","quadratic_form"),"alpha^T G alpha=0"),(("orientation","degree_five_denominator_positive"),False),(("orientation","degree_seven_denominator_positive"),False),(("decision","cross_multiplication_by_normalized_denominator_is_valid"),False),(("decision","positivity_extends_to_the_singular_t_equals_one_face"),True),(("decision","positivity_identifies_the_full_fisher"),True)]
def setp(d,path,val):
 for k in path[:-1]:d=d[k]
 d[path[-1]]=val
for i,(path,val) in enumerate(muts,1):
 d=copy.deepcopy(base);setp(d,path,val);assert not all(ok for _,ok in m.validate(d,rows)),path;print(f"PASS {i:02d}: rejected {'.'.join(path)}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
