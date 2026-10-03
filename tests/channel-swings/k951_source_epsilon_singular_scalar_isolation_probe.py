#!/usr/bin/env python3
"""Hostile mutations for K951."""
import copy, importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2]; P=R/"tests/channel-swings/k951_source_epsilon_singular_scalar_isolation.py"
s=importlib.util.spec_from_file_location("k951",P); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); b=m.build(); m.validate(b)
M=[("theorem","ambient_invariant_dimension",6),("theorem","constraint_nonnegative_over_reals",False),("theorem","real_zero_set_is_exactly_target",False),("theorem","real_zero_set_dimension",1),("theorem","first_jet_vanishes_at_target",False),("theorem","constraint_jacobian_rank_at_target",1),("theorem","constraint_hessian_rank_at_target",6),("theorem","regular_constraint",True),("decision","current_action_owns_the_scalar",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
    d=copy.deepcopy(b); d[a][k]=v
    try: m.validate(d)
    except AssertionError: n+=1
assert n==10
print("PASS K951 hostile mutations rejected 10/10")
