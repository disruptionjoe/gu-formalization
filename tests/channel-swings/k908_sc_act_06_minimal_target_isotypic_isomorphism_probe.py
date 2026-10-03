#!/usr/bin/env python3
"""Hostile mutations for K908."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];S=R/"tests/channel-swings/k908_sc_act_06_minimal_target_isotypic_isomorphism.py";s=importlib.util.spec_from_file_location("k908",S);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("minimal_target","total_real_dimension",1),("minimal_target","total_real_multiplicity",1),("minimal_target","occupied_real_type_count",39),("minimal_target","row_count",39),("minimal_target","all_type_multiplicities_saturated",False),("theorem","dimension_equality_plus_injectivity_implies_isomorphism",False),("theorem","equivariant_isomorphism_requires_every_type_block_invertible",False),("theorem","minimal_character_matches_old_quotient",False),("theorem","no_unused_target_complement",False),("theorem","adjoint_isomorphism",False),("decision","minimal_target_can_be_checked_typewise",False),("decision","mere_character_match_constructs_cross_map",True),("decision","action_ownership_and_BG_zero_still_required",False),("","classification","CONVENTIONAL_COMPARATOR"),("","target_claim","SC-ACT-01"),("","status","accepted"),("controls","controls_passed",41),("controls","hostile_mutations_rejected",19),("gu_typed_objects","cross_map","zero"),("gu_typed_objects","minimal_target_dual","unrelated")]
n=0
for a,k,v in M:
 x=copy.deepcopy(b);(x[a] if a else x)[k]=v
 try:m.validate(x)
 except AssertionError:n+=1
assert n==20
print("PASS K908 hostile mutations rejected 20/20")
