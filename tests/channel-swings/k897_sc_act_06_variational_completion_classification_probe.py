#!/usr/bin/env python3
"""Hostile mutations for K897."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SOURCE=ROOT/"tests/channel-swings/k897_sc_act_06_variational_completion_classification.py"
spec=importlib.util.spec_from_file_location("k897",SOURCE);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);base=m.build();m.validate(base)
mutations=[
 ("classification_theorem","hypotheses",["A^T=A"]),("classification_theorem","completion_decomposition","C=S"),
 ("classification_theorem","surviving_map","T=A"),("classification_theorem","symmetric_condition","S^T=-S"),
 ("classification_theorem","gauge_condition","AG=0"),("classification_theorem","forced_skew_correction","skew(C)=0"),
 ("classification_theorem","forced_skew_correction_rank",8191),("classification_theorem","selected_skew_map_survives_in_completed_hessian",True),
 ("classification_theorem","minimal_variational_completion","C_min=0"),("classification_theorem","minimal_completed_hessian","T_min=A"),
 ("classification_theorem","minimal_completion_repairs_old_quotient",True),("classification_theorem","nonzero_quotient_map_requires_new_symmetric_block",False),
 ("proof","symmetry_step","automatic"),("proof","decomposition_step","C=S"),("proof","descent_step","AG=0"),("proof","converse_step","none"),
 ("decision","selected_i1b_skew_map_has_independent_variational_quotient_capacity",True),("decision","current_variational_repair_capacity_known",True),
 ("decision","quotient_ranks_now_admissible",True),("","classification","CONVENTIONAL_COMPARATOR"),]
rejected=0
for section,key,value in mutations:
 packet=copy.deepcopy(base);(packet[section] if section else packet)[key]=value
 try:m.validate(packet)
 except AssertionError:rejected+=1
assert rejected==20
print("PASS K897 hostile mutations rejected 20/20")
