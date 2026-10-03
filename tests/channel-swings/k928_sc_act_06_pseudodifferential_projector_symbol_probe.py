#!/usr/bin/env python3
"""Hostile mutations for K928."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k928_sc_act_06_pseudodifferential_projector_symbol.py";s=importlib.util.spec_from_file_location("k928",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("theorem","constant_rank_makes_moore_penrose_smooth",False),("theorem","G_pseudoinverse_degree",0),("theorem","projector_homogeneous_degree",1),("theorem","projector_rank",0),("theorem","order_zero_pseudodifferential_quantization_exists",False),("theorem","exact_operator_idempotence_after_arbitrary_quantization",True),("theorem","lower_order_recursive_correction_required",False),("decision","pseudodifferential_principal_symbol_row_closed",False),("decision","complete_owned_pseudodifferential_action_constructed",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K928 hostile mutations rejected 10/10")
