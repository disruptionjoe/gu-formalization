#!/usr/bin/env python3
"""Hostile mutations for K907."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];S=R/"tests/channel-swings/k907_sc_act_06_cross_adjoint_rank_equivalence.py";s=importlib.util.spec_from_file_location("k907",S);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("theorem","rank_identity","rank(B)=0"),("theorem","old_kernel_eliminated_iff","never"),("theorem","old_cokernel_eliminated_iff","never"),("theorem","injective_iff_adjoint_surjective",False),("theorem","injective_rank",1),("theorem","minimum_target_dimension",1),("theorem","adjoint_kernel_dimension_formula","zero"),("theorem","symmetric_cross_pair_controls_both_old_sides",False),("decision","one_sided_rank_check_sufficient_for_old_pair",False),("decision","raw_target_dimension_alone_sufficient",True),("decision","action_owned_cross_map_still_required",False),("decision","full_coupled_nondegeneracy_decided",True),("","classification","CONVENTIONAL_COMPARATOR"),("","target_claim","SC-ACT-01"),("","status","accepted"),("controls","controls_passed",37),("controls","hostile_mutations_rejected",19),("gu_typed_objects","cross_map","zero"),("gu_typed_objects","adjoint","zero"),("gu_typed_objects","pairings","degenerate")]
n=0
for a,k,v in M:
 x=copy.deepcopy(b);(x[a] if a else x)[k]=v
 try:m.validate(x)
 except AssertionError:n+=1
assert n==20
print("PASS K907 hostile mutations rejected 20/20")
