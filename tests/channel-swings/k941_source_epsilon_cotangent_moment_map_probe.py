#!/usr/bin/env python3
"""Hostile mutations for K941."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k941_source_epsilon_cotangent_moment_map.py";s=importlib.util.spec_from_file_location("k941",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("theorem","group_dimension",70),("theorem","parent_dimension",140),("theorem","vertical_derivative_rank",70),("theorem","fiber_dimension",70),("theorem","moment_map_is_surjective_submersion",False),("theorem","fiber_over_mu_is_diffeomorphic_to_group",False),("theorem","left_action_is_free",False),("theorem","frozen_distortion_rank70_is_same_map",True),("decision","functional_boundary_domain_constructed",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K941 hostile mutations rejected 10/10")
