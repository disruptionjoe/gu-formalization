#!/usr/bin/env python3
"""Hostile mutations for K947."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k947_source_epsilon_invariant_hamiltonian_boundary.py";s=importlib.util.spec_from_file_location("k947",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("theorem","invariant_coordinate_count",6),("theorem","poisson_commutes_with_all_moment_map_components",False),("theorem","all_seven_invariant_values_are_conserved",False),("theorem","hamiltonian_generator_lies_in_charge_stabilizer",False),("theorem","hamiltonian_evolution_imposes_initial_value_equations",True),("theorem","arbitrary_initial_regular_invariant_values_remain_allowed",False),("decision","conservation_is_selection",True),("decision","invariant_hamiltonian_selects_a_fixed_nonzero_orbit",True),("decision","current_source_action_owns_h",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K947 hostile mutations rejected 10/10")
