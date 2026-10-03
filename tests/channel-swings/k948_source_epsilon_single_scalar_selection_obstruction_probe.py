#!/usr/bin/env python3
"""Hostile mutations for K948."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k948_source_epsilon_single_scalar_selection_obstruction.py";s=importlib.util.spec_from_file_location("k948",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("theorem","ambient_invariant_dimension",6),("theorem","regular_scalar_constraint_rank",2),("theorem","regular_scalar_level_dimension",0),("theorem","regular_scalar_level_is_locally_isolated",True),("theorem","one_regular_scalar_locks_all_seven_values",True),("theorem","six_local_invariant_directions_remain",False),("theorem","singular_isolating_case_is_regular_constraint",True),("decision","single_energy_or_boundary_value_is_sufficient",True),("decision","current_action_supplies_either_route",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K948 hostile mutations rejected 10/10")
