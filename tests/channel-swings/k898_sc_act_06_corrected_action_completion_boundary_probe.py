#!/usr/bin/env python3
"""Hostile mutations for K898."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SOURCE=ROOT/"tests/channel-swings/k898_sc_act_06_corrected_action_completion_boundary.py"
spec=importlib.util.spec_from_file_location("k898",SOURCE);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);base=m.build();m.validate(base)
mutations=[
 ("admission_boundary","completion_form","C=S"),("admission_boundary","forced_skew_cancellation_rank",8191),
 ("admission_boundary","surviving_hessian","T=A"),("admission_boundary","helmholtz_identity","S^T=-S"),
 ("admission_boundary","gauge_identity","AG=0"),("current_disposition","selected_formal_A_rank",8191),
 ("current_disposition","selected_formal_A_action_hessian",True),("current_disposition","formal_projector_descends",False),
 ("current_disposition","formal_projector_variational",True),("current_disposition","released_owned_nonzero_S_present",True),
 ("current_disposition","forty_quotient_ranks_defined",True),("current_disposition","credited_quotient_repair_rows",1),
 ("current_disposition","corrected_completion_gate_satisfied_rows",6),("current_disposition","corrected_completion_gate_total_rows",10),
 ("current_disposition","SC_ACT_06_proved_or_refuted",True),("decision","current_selected_i1b_formal_map_closed_as_action_hessian",False),
 ("decision","all_completed_i1b_actions_exhausted",True),("decision","all_action_parents_exhausted",True),
 ("decision","global_no_go_claimed",True),("","classification","CONVENTIONAL_COMPARATOR"),]
rejected=0
for section,key,value in mutations:
 packet=copy.deepcopy(base);(packet[section] if section else packet)[key]=value
 try:m.validate(packet)
 except AssertionError:rejected+=1
assert rejected==20
print("PASS K898 hostile mutations rejected 20/20")
