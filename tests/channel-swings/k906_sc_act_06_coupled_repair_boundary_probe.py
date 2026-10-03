#!/usr/bin/env python3
"""Hostile mutations for K906."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];S=R/"tests/channel-swings/k906_sc_act_06_coupled_repair_boundary.py";s=importlib.util.spec_from_file_location("k906",S);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("boundary","nonzero_kappa_cross_cancellation","possible"),("boundary","gauge_basic_released_diagonal","K"),("boundary","cross_block_admission","none"),("boundary","complete_cross_only_repair_budget","small"),("boundary","released_zero_fermion_mixed_capacity",1),("boundary","released_zero_fermion_cross_only_repair",True),("boundary","new_self_block_D_can_cancel_old_euler_gauge_defect",True),("boundary","cross_block_can_have_future_quotient_capacity",False),("decision","vague_coupled_field_cancellation_reopener_closed",False),("decision","specific_gauge_basic_cross_response_reopener_open",False),("decision","new_gauge_basic_old_old_block_reopener_open",False),("decision","source_owned_nonzero_fermion_germ_reopener_open",False),("decision","SC_ACT_06_proved_or_refuted",True),("","classification","CONVENTIONAL_COMPARATOR"),("","target_claim","SC-ACT-01"),("","status","accepted"),("controls","controls_passed",41),("controls","hostile_mutations_rejected",19),("boundary","corrected_completion_gate_satisfied_rows",11),("gu_typed_objects","gauge","unknown")]
n=0
for a,k,v in M:
 x=copy.deepcopy(b);(x[a] if a else x)[k]=v
 try:m.validate(x)
 except AssertionError:n+=1
assert n==20
print("PASS K906 hostile mutations rejected 20/20")
