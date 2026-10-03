#!/usr/bin/env python3
"""Hostile mutations for K901."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];S=R/"tests/channel-swings/k901_sc_act_06_released_parent_typewise_capacity.py";s=importlib.util.spec_from_file_location("k901",S);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("typewise_capacity","row_count",39),("typewise_capacity","all_released_induced_ranks_zero",False),("typewise_capacity","all_occupied_types_unrepaired",False),("typewise_capacity","old_total_dimension",90127),("typewise_capacity","old_total_real_multiplicity",168),("typewise_capacity","released_total_quotient_rank",1),("typewise_capacity","remaining_type_deficit_count",39),("theorem","zero_map_is_equivariant",False),("theorem","raw_nonzero_hessian_rank_is_not_quotient_capacity",False),("theorem","forty_ranks_are_defined_for_released_admissible_class",False),("theorem","forty_ranks_are_all_zero",False),("decision","released_symmetric_parent_class_repairs_old_quotient",True),("decision","all_forty_old_types_remain_deficient",False),("decision","current_flat_packet_globally_refuted",True),("","classification","CONVENTIONAL_COMPARATOR"),("","target_claim","SC-ACT-01"),("","status","accepted"),("controls","controls_passed",43),("controls","hostile_mutations_rejected",19),("","direction","native_to_observed")]
n=0
for a,k,v in M:
 x=copy.deepcopy(b);(x[a] if a else x)[k]=v
 try:m.validate(x)
 except AssertionError:n+=1
assert n==20
print("PASS K901 hostile mutations rejected 20/20")
