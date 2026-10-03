#!/usr/bin/env python3
"""Hostile mutations for K949."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k949_source_epsilon_seven_lock_boundary_contract.py";s=importlib.util.spec_from_file_location("k949",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("theorem","lock_component_count",1),("theorem","required_jacobian_rank",6),("theorem","selected_invariant_level_dimension",6),("theorem","selected_charge_orbit_dimension",0),("theorem","constraint_functions_are_gauge_invariant",False),("theorem","quotient_by_full_group_is_separate_declared_step",False),("theorem","formal_multiplier_action_is_source_owned",True),("certificate","missing_row_count",3),("decision","physical_boundary_law_constructed",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K949 hostile mutations rejected 10/10")
