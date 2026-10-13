#!/usr/bin/env python3
"""Hostile census, protected-state and frontier mutations for K1755."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1755_two_radius_rectangular_admission.py"
s=importlib.util.spec_from_file_location("producer",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text());mutations=[
 (("bridge_census","total"),450),(("bridge_census","new_satisfied_rows"),["K1755"]),
 (("protected_state","source_claim_register_changed"),True),(("protected_state","k1145_score"),"7/7"),
 (("decision","whole_chart_optimizer_admitted"),True),(("decision","all_seed_or_physical_result_admitted"),True),
 (("next_frontier","incumbent"),"Continue the local coefficient ladder."),
 (("next_frontier","lower_principle_boundary"),"Fourth cumulants already prove the unrestricted lower bound.")]
def setp(d,path,val):
 for k in path[:-1]:d=d[k]
 d[path[-1]]=val
for i,(path,val) in enumerate(mutations,1):
 d=copy.deepcopy(base);setp(d,path,val);assert not all(ok for _,ok in m.validate(d)),path;print(f"PASS {i:02d}: rejected {'.'.join(path)}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
