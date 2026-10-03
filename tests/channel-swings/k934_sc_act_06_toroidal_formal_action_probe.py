#!/usr/bin/env python3
"""Hostile mutations for K934."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k934_sc_act_06_toroidal_formal_action.py";s=importlib.util.spec_from_file_location("k934",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("theorem","action_real_and_nonnegative",False),("theorem","action_bounded_on_L2",False),("theorem","gauge_invariant_for_lambda_in_H1",False),("theorem","cohomology_projector_range_not_critical_space",False),("theorem","exact_operator_identities_used",False),("theorem","source_action_owner","GU source"),("theorem","preboundary_or_bv_bfv_constructed",True),("decision","exact_auxiliary_variational_parent_constructed",False),("decision","formal_action_promoted_to_GU_source_action",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K934 hostile mutations rejected 10/10")
