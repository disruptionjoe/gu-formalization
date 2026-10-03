#!/usr/bin/env python3
"""Hostile mutations for K910."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];S=R/"tests/channel-swings/k910_sc_act_06_cross_completion_admission_boundary.py";s=importlib.util.spec_from_file_location("k910",S);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("admission","released_zero_fermion_mixed_capacity",1),("admission","released_inventory_admitted",True),("admission","corrected_completion_gate_satisfied_rows",6),("admission","corrected_completion_gate_total_rows",10),("decision","minimal_hypothetical_sufficiency_now_exact",False),("decision","surplus_hypothetical_sufficiency_now_exact",False),("decision","current_action_owned_B_available",True),("decision","current_action_owned_D_KK_available",True),("decision","cross_completion_constructed",True),("decision","SC_ACT_06_proved_or_refuted",True),("decision","distance_only_cross_budget_waves_exhausted",False),("","classification","CONVENTIONAL_COMPARATOR"),("","target_claim","SC-ACT-01"),("","status","accepted"),("controls","controls_passed",44),("controls","hostile_mutations_rejected",19),("gu_typed_objects","cross_map","zero"),("gu_typed_objects","old_quotient","zero"),("admission","common_requirements",["none","none","none","none"]),("decision","next_exact_input","repeat budget")]
n=0
for a,k,v in M:
 x=copy.deepcopy(b);(x[a] if a else x)[k]=v
 try:m.validate(x)
 except AssertionError:n+=1
assert n==20
print("PASS K910 hostile mutations rejected 20/20")
