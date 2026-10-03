#!/usr/bin/env python3
"""Hostile mutations for K937."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k937_sc_act_06_fredholm_essential_obstruction.py";s=importlib.util.spec_from_file_location("k937",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("theorem","nonzero_mode_range_dimension",0),("theorem","nonzero_mode_kernel_dimension",0),("theorem","range_infinite_dimensional",False),("theorem","kernel_infinite_dimensional",False),("theorem","cokernel_infinite_dimensional",False),("theorem","essential_spectrum",[1]),("theorem","zero_and_one_have_infinite_multiplicity",False),("theorem","every_Q0_extension_fredholm",True),("decision","native_fredholm_realization_constructed",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K937 hostile mutations rejected 10/10")
