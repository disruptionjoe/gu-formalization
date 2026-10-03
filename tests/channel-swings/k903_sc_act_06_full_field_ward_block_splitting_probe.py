#!/usr/bin/env python3
"""Hostile mutations for K903."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];S=R/"tests/channel-swings/k903_sc_act_06_full_field_ward_block_splitting.py";s=importlib.util.spec_from_file_location("k903",S);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("theorem","old_supported_gauge","G_full=(G,J)"),("theorem","ward_product","T G_full=0"),("theorem","ward_iff","S G+B G=0"),("theorem","off_diagonal_cannot_cancel_old_euler_defect",False),("theorem","new_self_block_D_is_irrelevant_to_gauge_restriction",False),("theorem","converse",False),("decision","coupled_cross_blocks_can_cancel_nonzero_SG",True),("decision","coupled_cross_blocks_can_carry_independent_old_quotient_response",False),("decision","future_cross_block_must_annihilate_gauge_image",False),("proof","source_application","no source"),("proof","direct_sum","same summand"),("proof","necessity","cancellation allowed"),("","classification","CONVENTIONAL_COMPARATOR"),("","target_claim","SC-ACT-01"),("","status","accepted"),("controls","controls_passed",35),("controls","hostile_mutations_rejected",17),("gu_typed_objects","gauge","unknown")]
n=0
for a,k,v in M:
 x=copy.deepcopy(b);(x[a] if a else x)[k]=v
 try:m.validate(x)
 except AssertionError:n+=1
assert n==18
print("PASS K903 hostile mutations rejected 18/18")
