#!/usr/bin/env python3
"""Hostile mutations for K1776."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1776_full_fisher_semiconvexity.py"
s=importlib.util.spec_from_file_location("k1776",P);k=importlib.util.module_from_spec(s);s.loader.exec_module(k)
d=json.loads(k.ARTIFACT.read_text());mutations=[
 (("schema_version",),"0"),(("claim_id",),"K0"),(("theorem","semiconvexity"),"F''>=0"),
 (("two_radius_identity","centered_second_moment"),"0"),(("decision","global_semiconvexity_proved"),False),
 (("decision","raw_c_over_z_required"),True),(("decision","full_fisher_global_optimizer_proved"),True)]
for i,(path,value) in enumerate(mutations,1):
 m=copy.deepcopy(d);x=m
 for key in path[:-1]:x=x[key]
 x[path[-1]]=value
 assert not all(ok for _,ok in k.validate(m));print(f"PASS {i:02d}: rejected {'.'.join(path)}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
