#!/usr/bin/env python3
"""Hostile mutations for K899."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];S=R/"tests/channel-swings/k899_sc_act_06_torsion_hessian_gauge_restriction.py"
s=importlib.util.spec_from_file_location("k899",S);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("restriction_theorem","K_is_action_owned",False),("restriction_theorem","K_is_symmetric_hessian",False),("restriction_theorem","K_is_involution",False),("restriction_theorem","K_is_injective",False),("restriction_theorem","G_is_injective",False),("restriction_theorem","radial_domain_dimension",8192),("restriction_theorem","rank_KG",8191),("restriction_theorem","kernel_KG_dimension",1),("restriction_theorem","nonzero_kappa_K_is_gauge_basic",True),("comparison","selected_A_restriction_rank",0),("comparison","torsion_K_restriction_rank",8191),("comparison","torsion_block_cancels_selected_A_on_radial_image",True),("decision","released_torsion_hessian_is_admissible_nonzero_S",True),("decision","torsion_action_parent_closed_as_gauge_basic_completion",False),("decision","new_symmetric_action_parent_or_new_germ_still_open",False),("","classification","CONVENTIONAL_COMPARATOR")]
n=0
for a,k,v in M:
 x=copy.deepcopy(b);(x[a] if a else x)[k]=v
 try:m.validate(x)
 except AssertionError:n+=1
assert n==16
print("PASS K899 hostile mutations rejected 16/16")
