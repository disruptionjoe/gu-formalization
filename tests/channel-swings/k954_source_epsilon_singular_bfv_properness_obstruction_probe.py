#!/usr/bin/env python3
"""Hostile mutations for K954."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k954_source_epsilon_singular_bfv_properness_obstruction.py";s=importlib.util.spec_from_file_location("k954",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("theorem","constraint_conormal_rank_at_target",7),("theorem","desired_point_conormal_rank",1),("theorem","hamiltonian_constraint_vector_field_rank_at_target",1),("theorem","koszul_H0_equals_point_algebra",True),("theorem","koszul_H1_vanishes_for_nonzero_divisor",False),("theorem","new_degree_one_constraint_generators_needed",1),("theorem","point_selection_properness_passes",True),("decision","exact_koszul_resolution_of_wrong_ideal_counts_as_point_selector",True),("decision","higher_stage_ghosts_without_new_degree_one_constraints_repair_H0",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K954 hostile mutations rejected 10/10")
