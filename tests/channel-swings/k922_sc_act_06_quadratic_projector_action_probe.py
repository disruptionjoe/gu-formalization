#!/usr/bin/env python3
"""Hostile mutations for K922."""
import copy,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SOURCE=ROOT/"tests/channel-swings/k922_sc_act_06_quadratic_projector_action.py"
s=importlib.util.spec_from_file_location("k922",SOURCE);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);base=m.build();m.validate(base)
M=[("variation","stationary_origin",False),("variation","helmholtz_symmetric",False),("variation","gauge_invariant_under_x_to_x+G lambda",False),("variation","ward_identity","P_H G=G"),("variation","hessian","D E_H=0"),("decision","formal_variational_parent_constructed",False),("decision","k897_symmetric_gauge_basic_class_instantiated",False),("decision","source_selected_action_constructed",True),("decision","local_field_action_constructed",True),("decision","SC_ACT_06_proved_or_refuted",True),("","classification","CONVENTIONAL_COMPARATOR"),("","target_claim","SC-ACT-01"),("controls","controls_passed",31),("controls","hostile_mutations_rejected",17),("gu_typed_objects","target","UNTYPED"),("gu_typed_objects","hessian","D2 A_H=0"),("decision","next_exact_input","promote action"),("variation","quotient_energy","zero")]
r=0
for sec,k,v in M:
 d=copy.deepcopy(base);(d[sec] if sec else d)[k]=v
 try:m.validate(d)
 except AssertionError:r+=1
assert r==18
print("PASS K922 hostile mutations rejected 18/18")
