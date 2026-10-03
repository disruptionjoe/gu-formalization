#!/usr/bin/env python3
"""Hostile mutations for K931."""
import copy, importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2]; P=R/"tests/channel-swings/k931_sc_act_06_low_frequency_extension_obstruction.py"
s=importlib.util.spec_from_file_location("k931",P); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); b=m.build(); m.validate(b)
M=[("theorem","projector_direction_dependent",False),("theorem","continuous_extension_at_zero_would_force_constant_sphere_value",False),("theorem","continuous_extension_at_zero_exists",True),("theorem","ordinary_global_s0_symbol_equal_to_P_on_every_nonzero_frequency_exists",True),("theorem","smooth_transition_cutoff_preserves_exact_idempotence",True),("theorem","homogeneous_or_discrete_low_frequency_calculus_remains_open",False),("decision","exact_euclidean_full_symbol_route_closed",False),("decision","toroidal_discrete_zero_mode_route_released",False),("decision","all_pseudodifferential_realizations_excluded",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b); d[a][k]=v
 try: m.validate(d)
 except AssertionError: n+=1
assert n==10
print("PASS K931 hostile mutations rejected 10/10")
