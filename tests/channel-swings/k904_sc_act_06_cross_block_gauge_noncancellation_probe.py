#!/usr/bin/env python3
"""Hostile mutations for K904."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];S=R/"tests/channel-swings/k904_sc_act_06_cross_block_gauge_noncancellation.py";s=importlib.util.spec_from_file_location("k904",S);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("classification_theorem","ward_product","T G_full=0"),("classification_theorem","uses","H_QG!=0"),("classification_theorem","old_euler_condition","kappa KG+BG=0"),("classification_theorem","cross_euler_condition","none"),("classification_theorem","gauge_basic_iff","all kappa"),("classification_theorem","off_diagonal_B_cannot_rescue_nonzero_kappa",False),("classification_theorem","new_self_block_D_unconstrained_by_this_identity",False),("classification_theorem","cross_response_on_old_cohomology","zero"),("classification_theorem","cross_response_is_new_capacity_not_cancellation",False),("decision","released_nonzero_torsion_coefficient_reopened_by_cross_coupling",True),("decision","gauge_basic_cross_coupling_remains_open",False),("decision","cross_coupling_requires_independent_action_ownership",False),("","classification","CONVENTIONAL_COMPARATOR"),("","target_claim","SC-ACT-01"),("","status","accepted"),("controls","controls_passed",37),("controls","hostile_mutations_rejected",17),("gu_typed_objects","gauge","unknown")]
n=0
for a,k,v in M:
 x=copy.deepcopy(b);(x[a] if a else x)[k]=v
 try:m.validate(x)
 except AssertionError:n+=1
assert n==18
print("PASS K904 hostile mutations rejected 18/18")
