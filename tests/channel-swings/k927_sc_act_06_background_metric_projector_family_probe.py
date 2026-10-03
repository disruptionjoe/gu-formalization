#!/usr/bin/env python3
"""Hostile mutations for K927."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k927_sc_act_06_background_metric_projector_family.py";s=importlib.util.spec_from_file_location("k927",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("composition","background_positive_metric_exists",False),("composition","background_owns_metric_on_fixed_flat_germ",False),("composition","metric_is_globally_unique_or_full_native_invariant",True),("composition","projector_family_is_smooth",False),("composition","projector_family_rank",0),("composition","self_adjoint",False),("composition","idempotent",False),("decision","positive_auxiliary_metric_owner_row_closed_on_fixed_germ",False),("decision","global_or_source_action_ownership_follows",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K927 hostile mutations rejected 10/10")
