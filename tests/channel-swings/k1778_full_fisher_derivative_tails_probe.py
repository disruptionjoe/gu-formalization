#!/usr/bin/env python3
"""Hostile mutations for K1778."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1778_full_fisher_derivative_tails.py"
s=importlib.util.spec_from_file_location("k1778",P);k=importlib.util.module_from_spec(s);s.loader.exec_module(k)
d=json.loads(k.ARTIFACT.read_text());mutations=[
 (("contract","compact_window"),"[-10,10]"),(("contract","maximum_total_derivative_order"),2),
 (("contract","gaussian_tail_moment_uppers","M3"),"0"),(("contract","derivative_sup_uppers","tanh",2),"1/2"),
 (("contract","largest_admitted_tail"),"0"),(("decision","value_gradient_hessian_and_third_natural_derivative_tails_certified"),False),
 (("decision","compact_window_derivative_evaluator_completed"),True),(("decision","three_slab_interval_newton_completed"),True)]
for i,item in enumerate(mutations,1):
 path,value=item if len(item)==2 else (item[:-1],item[-1]);m=copy.deepcopy(d);x=m
 for key in path[:-1]:x=x[key]
 x[path[-1]]=value
 assert not all(ok for _,ok in k.validate(m));print(f"PASS {i:02d}: rejected {'.'.join(map(str,path))}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
