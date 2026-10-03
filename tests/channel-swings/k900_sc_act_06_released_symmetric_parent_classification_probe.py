#!/usr/bin/env python3
"""Hostile mutations for K900."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];S=R/"tests/channel-swings/k900_sc_act_06_released_symmetric_parent_classification.py";s=importlib.util.spec_from_file_location("k900",S);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("classification_theorem","both_summands_symmetric",False),("classification_theorem","residual_square_gauge_identity","H_QG!=0"),("classification_theorem","torsion_restriction_identity","rank(KG)=8191"),("classification_theorem","family_gauge_restriction","0"),("classification_theorem","gauge_basic_iff","all kappa"),("classification_theorem","admissible_released_family","kappa K"),("classification_theorem","admissible_family_can_have_nonzero_raw_rank",False),("classification_theorem","induced_map_on_K879_old_cohomology","nonzero"),("classification_theorem","induced_quotient_rank",1),("decision","released_symmetric_action_owned_span_contains_nonzero_gauge_basic_raw_hessians",False),("decision","released_span_contains_nonzero_gauge_basic_quotient_capacity",True),("decision","released_span_repairs_any_old_type",True),("decision","all_action_parents_exhausted",True),("","classification","CONVENTIONAL_COMPARATOR"),("","target_claim","SC-ACT-01"),("","status","accepted"),("controls","controls_passed",35),("controls","hostile_mutations_rejected",17)]
n=0
for a,k,v in M:
 x=copy.deepcopy(b);(x[a] if a else x)[k]=v
 try:m.validate(x)
 except AssertionError:n+=1
assert n==18
print("PASS K900 hostile mutations rejected 18/18")
