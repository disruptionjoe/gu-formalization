#!/usr/bin/env python3
"""Hostile mutations for K932."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k932_sc_act_06_toroidal_exact_projector.py";s=importlib.util.spec_from_file_location("k932",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("theorem","finite_low_modes_do_not_change_symbol_class",False),("theorem","full_lower_symbol_explicit",False),("theorem","pointwise_self_adjoint",False),("theorem","pointwise_idempotent",False),("theorem","operator_self_adjoint",False),("theorem","operator_idempotent",False),("theorem","source_or_native_compactification_owned",True),("decision","exact_auxiliary_pseudodifferential_projection_constructed",False),("decision","native_or_source_owned_complete_operator_constructed",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K932 hostile mutations rejected 10/10")
