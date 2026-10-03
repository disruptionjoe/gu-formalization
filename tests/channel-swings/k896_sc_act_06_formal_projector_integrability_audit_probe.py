#!/usr/bin/env python3
"""Hostile mutations for K896."""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; SOURCE=ROOT/"tests/channel-swings/k896_sc_act_06_formal_projector_integrability_audit.py"
spec=importlib.util.spec_from_file_location("k896",SOURCE);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);base=m.build();m.validate(base)
mutations=[
 ("formal_projector_audit","projector_identity","P_R G=0"),("formal_projector_audit","formal_correction","C=0"),
 ("formal_projector_audit","formal_completed_map","T=A"),("formal_projector_audit","gauge_descent","TG!=0"),
 ("formal_projector_audit","gauge_descent_satisfied",False),("formal_projector_audit","completed_map_rank",122720),
 ("formal_projector_audit","completed_map_helmholtz_defect_rank",0),("formal_projector_audit","correction_symmetric_part_rank",16381),
 ("formal_projector_audit","selected_action_rank",130911),("formal_projector_audit","helmholtz_symmetry_satisfied",True),
 ("formal_projector_audit","formal_completion_is_same_domain_even_scalar_action_hessian",True),
 ("structural_reason","transpose","T^T=T"),("structural_reason","symmetry_condition","automatic"),
 ("structural_reason","equivalent_anticommutator_condition","0=0"),("structural_reason","condition_fails_exactly",False),
 ("decision","formal_projector_restores_linear_gauge_descent",False),("decision","formal_projector_supplies_variational_integrability",True),
 ("decision","formal_projector_may_be_credited_as_action_completion",True),("decision","quotient_ranks_now_admissible",True),
 ("","classification","CONVENTIONAL_COMPARATOR"),]
rejected=0
for section,key,value in mutations:
 packet=copy.deepcopy(base);(packet[section] if section else packet)[key]=value
 try:m.validate(packet)
 except AssertionError:rejected+=1
assert rejected==20
print("PASS K896 hostile mutations rejected 20/20")
