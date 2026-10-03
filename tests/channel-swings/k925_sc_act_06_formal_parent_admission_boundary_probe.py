#!/usr/bin/env python3
"""Hostile mutations for K925."""
import copy,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SOURCE=ROOT/"tests/channel-swings/k925_sc_act_06_formal_parent_admission_boundary.py"
s=importlib.util.spec_from_file_location("k925",SOURCE);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);base=m.build();m.validate(base)
M=[("boundary","abstract_symmetric_gauge_basic_parent_exists",False),("boundary","abstract_parent_is_variational",False),("boundary","authenticated_old_submodule_rank_repaired",0),("boundary","authenticated_old_real_types_repaired",39),("boundary","authenticated_old_multiplicity_repaired",168),("boundary","pure_finite_symbol_algebraic_impossibility",True),("boundary","source_action_owned_local_parent_exists_in_current_custody",True),("boundary","complete_cosphere_family_exists_in_current_custody",True),("boundary","common_green_preboundary_packet_exists_in_current_custody",True),("boundary","SC_ACT_06_status","VERIFIED"),("decision","K920_new_old_parent_route_instantiated_formally",False),("decision","formal_instantiation_earns_GU_repair_credit",True),("decision","do_not_retry_released_K_HQ_span",False),("decision","do_not_promote_auxiliary_projector_to_source_action",False),("decision","SC_ACT_06_proved_or_refuted",True),("controls","controls_passed",37),("controls","hostile_mutations_rejected",19),("gu_typed_objects","target","UNTYPED"),("decision","next_route","RETRY_K_HQ"),("","classification","CONVENTIONAL_COMPARATOR")]
r=0
for sec,k,v in M:
 d=copy.deepcopy(base);(d[sec] if sec else d)[k]=v
 try:m.validate(d)
 except AssertionError:r+=1
assert r==20
print("PASS K925 hostile mutations rejected 20/20")
