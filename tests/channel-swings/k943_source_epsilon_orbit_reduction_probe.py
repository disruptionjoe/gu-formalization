#!/usr/bin/env python3
"""Hostile mutations for K943."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k943_source_epsilon_orbit_reduction.py";s=importlib.util.spec_from_file_location("k943",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("theorem","regular_stabilizer_dimension",21),("theorem","fixed_mu_quotient_dimension",70),("theorem","orbit_dimension",70),("theorem","fixed_mu_reduction_is_coadjoint_orbit",False),("theorem","orbit_reduction_is_same_coadjoint_orbit",False),("theorem","nonzero_reduction_is_point",True),("theorem","seven_independent_invariants_must_be_locked",False),("decision","current_action_locks_all_seven_invariants",True),("decision","physical_cohomology_constructed",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K943 hostile mutations rejected 10/10")
