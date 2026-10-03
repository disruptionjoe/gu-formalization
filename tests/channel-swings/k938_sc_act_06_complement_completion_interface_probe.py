#!/usr/bin/env python3
"""Hostile mutations for K938."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k938_sc_act_06_complement_completion_interface.py";s=importlib.util.spec_from_file_location("k938",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("theorem","L_A_fredholm_iff_A_fredholm",False),("theorem","index_L_A_equals_index_A",False),("theorem","kernel_L_A_equals_kernel_A",False),("theorem","cokernel_L_A_isomorphic_to_cokernel_A",False),("theorem","projector_alone_specifies_A",True),("theorem","projector_alone_specifies_graph_domain",True),("theorem","auxiliary_choice_is_source_owned",True),("theorem","completion_changes_infinite_mode_dynamics",False),("decision","native_fredholm_row_closed",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K938 hostile mutations rejected 10/10")
