#!/usr/bin/env python3
"""Hostile pilot accounting and scope mutations for K1764."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1764_interval_cover_pilot.py"
s=importlib.util.spec_from_file_location("producer",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text());muts=[
 (("rare_face_limit","formula"),"lim L5=0"),
 (("fail_closed_pilot","pruned_leaves"),1000000),
 (("fail_closed_pilot","coverage_complete"),True),
 (("fail_closed_pilot","scientific_exclusions_claimed_from_pilot"),True),
 (("decision","naive_independent_ball_global_engine_rejected"),False),
 (("decision","rare_face_is_a_mathematical_singularity_of_L5"),True),
 (("decision","global_interval_cover_completed"),True)]
def setp(d,path,val):
 for k in path[:-1]:d=d[k]
 d[path[-1]]=val
for i,(path,val) in enumerate(muts,1):
 d=copy.deepcopy(base);setp(d,path,val);assert not all(ok for _,ok in m.validate(d)),path;print(f"PASS {i:02d}: rejected {'.'.join(path)}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
