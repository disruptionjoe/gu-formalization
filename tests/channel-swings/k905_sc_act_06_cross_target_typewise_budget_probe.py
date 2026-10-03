#!/usr/bin/env python3
"""Hostile mutations for K905."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];S=R/"tests/channel-swings/k905_sc_act_06_cross_target_typewise_budget.py";s=importlib.util.spec_from_file_location("k905",S);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("budget","minimum_total_real_dimension",90127),("budget","minimum_total_real_multiplicity",168),("budget","occupied_real_type_count",39),("budget","all_forty_types_required",False),("budget","injectivity_required_for_complete_old_submodule_repair",False),("theorem","dimension_condition","dim(Y*)>=1"),("theorem","necessity_not_sufficiency",False),("theorem","partial_cross_rank_can_only_repair_its_actual_image",False),("theorem","raw_target_dimension_without_intertwiners_is_not_capacity",False),("decision","cross_only_complete_repair_requires_all_forty_types",False),("decision","cross_only_complete_repair_minimum_dimension",1),("decision","cross_only_complete_repair_minimum_real_multiplicity",1),("decision","current_released_zero_fermion_mixed_blocks_meet_budget",True),("","classification","CONVENTIONAL_COMPARATOR"),("","target_claim","SC-ACT-01"),("","status","accepted"),("controls","controls_passed",43),("controls","hostile_mutations_rejected",19),("gu_typed_objects","map","zero"),("theorem","schur_multiplicity_condition","none")]
n=0
for a,k,v in M:
 x=copy.deepcopy(b);(x[a] if a else x)[k]=v
 try:m.validate(x)
 except AssertionError:n+=1
assert n==20
print("PASS K905 hostile mutations rejected 20/20")
