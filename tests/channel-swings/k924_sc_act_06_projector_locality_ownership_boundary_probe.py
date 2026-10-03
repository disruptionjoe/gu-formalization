#!/usr/bin/env python3
"""Hostile mutations for K924."""
import copy,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SOURCE=ROOT/"tests/channel-swings/k924_sc_act_06_projector_locality_ownership_boundary.py"
s=importlib.util.spec_from_file_location("k924",SOURCE);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);base=m.build();m.validate(base)
M=[("audit","row_count",7),("audit","satisfied_rows",2),("audit","missing_rows",6),("audit","formal_identity_row_only",False),("audit","finite_symbol_existence_implies_local_action",True),("audit","ordinary_bundle_triviality_implies_natural_action",True),("decision","formal_parent_rejected_as_algebraically_invalid",True),("decision","formal_parent_admitted_as_source_GU_action",True),("decision","locality_or_naturality_no_go_for_all_future_parents",True),("decision","remaining_obstruction_relocated_to_family_ownership_and_analysis",False),("decision","SC_ACT_06_proved_or_refuted",True),("","classification","CONVENTIONAL_COMPARATOR"),("","target_claim","SC-ACT-01"),("controls","controls_passed",37),("controls","hostile_mutations_rejected",19),("gu_typed_objects","target","UNTYPED"),("decision","next_exact_input","promote projector"),("audit","generalized_inverse_dependency","none"),("rows",0,True),("rows",7,False)]
r=0
for sec,k,v in M:
 d=copy.deepcopy(base)
 if sec=="rows":d["audit"]["rows"][k]["current"]=v
 else:(d[sec] if sec else d)[k]=v
 try:m.validate(d)
 except AssertionError:r+=1
assert r==20
print("PASS K924 hostile mutations rejected 20/20")
