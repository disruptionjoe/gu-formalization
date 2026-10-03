#!/usr/bin/env python3
"""Hostile mutations for K944."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k944_source_epsilon_regular_bfv_boundary.py";s=importlib.util.spec_from_file_location("k944",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("theorem","constraint_rank",70),("theorem","first_stage_reducibility",21),("theorem","minimal_ghost_count",70),("theorem","master_equation_closes",False),("theorem","koszul_tate_is_proper_at_zero",False),("theorem","frozen_distortion_rank70_nonregularity_transfers",True),("decision","finite_zero_level_BFV_nontrivial_physics",True),("decision","current_nonzero_endpoint_admitted_by_zero_BFV",True),("decision","functional_field_space_BV_BFV_constructed",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K944 hostile mutations rejected 10/10")
