#!/usr/bin/env python3
"""Hostile mutations for K909."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];S=R/"tests/channel-swings/k909_sc_act_06_surplus_complement_compression.py";s=importlib.util.spec_from_file_location("k909",S);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("theorem","orthogonal_split","none"),("theorem","kernel_isomorphism","false"),("theorem","full_block_nondegenerate_iff","always"),("theorem","minimal_target_has_K_dimension",1),("theorem","minimal_target_full_block_nondegenerate_for_every_D",False),("theorem","surplus_dimension_formula","zero"),("theorem","surplus_cross_rank_does_not_control_D_KK",False),("synthetic_controls","minimal_case","singular"),("decision","minimum_budget_plus_injective_B_suffices_for_block_nondegeneracy",False),("decision","surplus_target_requires_action_owned_complement_self_block",False),("decision","target_character_and_cross_rank_alone_suffice_in_surplus_case",True),("decision","full_deformation_complex_proved",True),("","classification","CONVENTIONAL_COMPARATOR"),("","target_claim","SC-ACT-01"),("","status","accepted"),("controls","controls_passed",42),("controls","hostile_mutations_rejected",19),("gu_typed_objects","cross_map","zero"),("gu_typed_objects","surplus_complement","none"),("gu_typed_objects","compression","none")]
n=0
for a,k,v in M:
 x=copy.deepcopy(b);(x[a] if a else x)[k]=v
 try:m.validate(x)
 except AssertionError:n+=1
assert n==20
print("PASS K909 hostile mutations rejected 20/20")
