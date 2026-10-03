#!/usr/bin/env python3
"""Hostile mutations for K933."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k933_sc_act_06_sobolev_hodge_domain.py";s=importlib.util.spec_from_file_location("k933",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("theorem","bounded_on_every_real_sobolev_order",False),("theorem","range_closed",False),("theorem","moore_penrose_inverse_equals_operator",False),("theorem","gauge_image_in_kernel",False),("theorem","Pi_d0_zero",False),("theorem","kernel_and_cokernel_infinite_dimensional",False),("theorem","fredholm_realization",True),("theorem","retarded_or_advanced_green_operator_constructed",True),("decision","hodge_generalized_inverse_constructed",False),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K933 hostile mutations rejected 10/10")
