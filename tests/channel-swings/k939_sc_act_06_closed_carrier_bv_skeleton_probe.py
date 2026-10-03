#!/usr/bin/env python3
"""Hostile mutations for K939."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k939_sc_act_06_closed_carrier_bv_skeleton.py";s=importlib.util.spec_from_file_location("k939",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("theorem","Pi_d0_zero",False),("theorem","d0_adjoint_Pi_zero",False),("theorem","Q_squared_on_u_plus",1),("theorem","Q_squared_on_c_plus",1),("theorem","carrier_has_boundary",True),("theorem","bfv_boundary_phase_space_constructed",True),("theorem","local_preboundary_current_constructed",True),("theorem","retarded_or_advanced_support_constructed",True),("decision","native_or_source_owned_bv_row_closed",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K939 hostile mutations rejected 10/10")
