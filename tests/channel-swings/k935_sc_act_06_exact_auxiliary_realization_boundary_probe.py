#!/usr/bin/env python3
"""Hostile mutations for K935."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k935_sc_act_06_exact_auxiliary_realization_boundary.py";s=importlib.util.spec_from_file_location("k935",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("certificate","row_count",12),("certificate","satisfied_row_count",7),("certificate","closed_negative_row_count",0),("certificate","missing_row_count",3),("certificate","connection_fiber_rank",0),("certificate","SC_ACT_06_status","VERIFIED"),("certificate","full_GU_repair_credit",True),("decision","native_source_owned_complete_operator_exists",True),("decision","native_fredholm_or_causal_green_exists",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K935 hostile mutations rejected 10/10")
