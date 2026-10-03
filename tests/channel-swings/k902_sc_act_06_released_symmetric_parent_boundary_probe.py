#!/usr/bin/env python3
"""Hostile mutations for K902."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];S=R/"tests/channel-swings/k902_sc_act_06_released_symmetric_parent_boundary.py";s=importlib.util.spec_from_file_location("k902",S);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("boundary","released_parent_span","span{K}"),("boundary","torsion_disposition","admitted"),("boundary","residual_square_disposition","nonzero quotient"),("boundary","gauge_basic_released_span","{K,H_Q}"),("boundary","forty_released_quotient_ranks","nonzero"),("boundary","repaired_old_types",1),("boundary","remaining_old_types",39),("boundary","old_obstruction_dimension",0),("boundary","old_total_real_multiplicity",168),("boundary","corrected_completion_gate_satisfied_rows",6),("boundary","corrected_completion_gate_total_rows",10),("decision","released_symmetric_action_parent_span_closed",False),("decision","selected_i1b_completed_by_released_span",True),("decision","complete_flat_packet_refuted",True),("decision","all_action_parents_exhausted",True),("decision","SC_ACT_06_proved_or_refuted",True),("","classification","CONVENTIONAL_COMPARATOR"),("","target_claim","SC-ACT-01"),("controls","controls_passed",39),("controls","hostile_mutations_rejected",19)]
n=0
for a,k,v in M:
 x=copy.deepcopy(b);(x[a] if a else x)[k]=v
 try:m.validate(x)
 except AssertionError:n+=1
assert n==20
print("PASS K902 hostile mutations rejected 20/20")
