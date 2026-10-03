#!/usr/bin/env python3
"""Hostile mutations for K952."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k952_source_epsilon_principal_ideal_fat_point.py";s=importlib.util.spec_from_file_location("k952",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("theorem","ambient_regular_local_dimension",6),("theorem","principal_quotient_krull_dimension",0),("theorem","cotangent_dimension_of_principal_quotient",0),("theorem","linear_coordinate_survives_principal_quotient",False),("theorem","ordinary_principal_ideal_is_maximal_ideal",True),("theorem","principal_quotient_is_reduced_point_algebra",True),("theorem","real_radical_of_principal_ideal_is_maximal_ideal",False),("decision","real_set_isolation_equals_constraint_algebra_selection",True),("decision","single_scalar_degree_zero_quotient_is_point_observable_algebra",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K952 hostile mutations rejected 10/10")
