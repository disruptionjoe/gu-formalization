#!/usr/bin/env python3
"""Hostile mutations for K936."""
import copy, importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2]; P=R/"tests/channel-swings/k936_sc_act_06_zero_mode_nonselection.py"
s=importlib.util.spec_from_file_location("k936",P); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); b=m.build(); m.validate(b)
M=[("theorem","field_fiber_dimension",0),("theorem","nonzero_mode_rank",0),("theorem","nonzero_mode_kernel_dimension",0),("theorem","allowed_zero_mode_ranks","only 0"),("theorem","every_Q0_gives_exact_self_adjoint_projection",False),("theorem","any_two_Q0_extensions_differ_by_finite_rank",False),("theorem","nonzero_principal_symbol_determines_Q0",True),("theorem","source_or_action_selects_Q0",True),("decision","native_zero_mode_owner_constructed",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b); d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K936 hostile mutations rejected 10/10")
