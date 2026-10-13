#!/usr/bin/env python3
"""Hostile mutations for K1779."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1779_z1_atom_chart.py"
s=importlib.util.spec_from_file_location("k1779",P);k=importlib.util.module_from_spec(s);s.loader.exec_module(k)
d=json.loads(k.ARTIFACT.read_text());mutations=[
 (("chart","q"),"1/512"),(("chart","variance"),"0"),(("chart","first_slab_c_interval"),["0","1"]),
 (("chart","first_slab_p_lower"),"0"),(("chart","positive_denominator"),"unknown"),
 (("decision","z1_chart_regularized"),False),(("decision","raw_b_or_c_over_z_required"),True),(("decision","global_optimizer_proved"),True)]
for i,(path,value) in enumerate(mutations,1):
 m=copy.deepcopy(d);x=m
 for key in path[:-1]:x=x[key]
 x[path[-1]]=value
 assert not all(ok for _,ok in k.validate(m));print(f"PASS {i:02d}: rejected {'.'.join(path)}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
