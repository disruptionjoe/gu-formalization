#!/usr/bin/env python3
"""Hostile mutations for K940."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k940_sc_act_06_analytic_ownership_boundary.py";s=importlib.util.spec_from_file_location("k940",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("certificate","row_count",17),("certificate","satisfied_row_count",10),("certificate","closed_negative_row_count",1),("certificate","missing_row_count",4),("certificate","connection_fiber_rank",0),("certificate","SC_ACT_06_status","VERIFIED"),("certificate","full_GU_repair_credit",True),("decision","native_fredholm_or_causal_green_exists",True),("decision","source_action_owned_complete_operator_exists",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K940 hostile mutations rejected 10/10")
