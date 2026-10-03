#!/usr/bin/env python3
"""Hostile mutations for K929."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k929_sc_act_06_local_projector_obstruction.py";s=importlib.util.spec_from_file_location("k929",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("theorem","order_zero_differential_symbol_is_covector_independent",False),("theorem","gauge_images_span_connection_carrier",False),("theorem","forced_local_candidate_rank",1),("theorem","desired_projector_rank",0),("theorem","exact_local_order_zero_realization_exists",True),("theorem","pseudodifferential_realization_remains_open_at_full_operator_grade",False),("theorem","higher_order_or_different_parent_classes_excluded",True),("decision","same_projector_local_differential_route_closed",False),("decision","all_local_action_parents_refuted",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K929 hostile mutations rejected 10/10")
