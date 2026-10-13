#!/usr/bin/env python3
"""Hostile mutations for K1780."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1780_full_fisher_entry_admission.py"
s=importlib.util.spec_from_file_location("k1780",P);k=importlib.util.module_from_spec(s);s.loader.exec_module(k)
d=json.loads(k.ARTIFACT.read_text());mutations=[
 (("bridge_census","total"),479),(("protected_state","source_register_changed"),True),
 (("rational_descent","q"),"1/512"),(("rational_descent","whole_line_gap"),"[-1 +/- 0]"),
 (("entry_state","boundary_cells_remaining"),2),(("entry_state","interior_slabs_remaining"),2),
 (("entry_state","compact_window_value_gradient_hessian_evaluator_available"),True),(("entry_state","full_fisher_interval_newton_completed"),True),
 (("decision","k1753_candidate_locally_optimal"),True),(("decision","stationary_point_proved"),True),
 (("decision","unique_component_proved"),True),(("decision","global_optimizer_proved"),True)]
for i,(path,value) in enumerate(mutations,1):
 m=copy.deepcopy(d);x=m
 for key in path[:-1]:x=x[key]
 x[path[-1]]=value
 assert not all(ok for _,ok in k.validate(m));print(f"PASS {i:02d}: rejected {'.'.join(path)}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
