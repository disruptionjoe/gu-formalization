#!/usr/bin/env python3
"""Hostile mutations for K942."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k942_source_epsilon_zero_reduction.py";s=importlib.util.spec_from_file_location("k942",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("theorem","group_dimension",70),("theorem","zero_level_dimension",182),("theorem","zero_stabilizer_dimension",7),("theorem","zero_level_is_regular",False),("theorem","action_on_zero_level_is_free_and_transitive",False),("theorem","reduced_dimension",84),("theorem","reduced_space_is_one_point",False),("theorem","nontrivial_edge_modes_after_full_zero_gauging",True),("decision","full_zero_constraint_is_selected_by_source_action",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K942 hostile mutations rejected 10/10")
