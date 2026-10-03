#!/usr/bin/env python3
"""Hostile mutations for K946."""
import copy, importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2]; P=R/"tests/channel-swings/k946_source_epsilon_invariant_coordinate_chart.py"; s=importlib.util.spec_from_file_location("k946",P); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); b=m.build(); m.validate(b)
M=[("theorem","regular_rank",6),("theorem","primitive_generator_count",6),("theorem","invariant_differential_rank",6),("theorem","common_tangent_kernel_dimension",85),("theorem","regular_orbit_dimension",83),("theorem","orbit_tangent_equals_common_invariant_kernel_locally",False),("theorem","invariant_map_is_local_transverse_submersion",False),("decision","current_action_selects_values",True),("decision","global_orbit_separation_claimed",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b); d[a][k]=v
 try: m.validate(d)
 except AssertionError: n+=1
assert n==10
print("PASS K946 hostile mutations rejected 10/10")
