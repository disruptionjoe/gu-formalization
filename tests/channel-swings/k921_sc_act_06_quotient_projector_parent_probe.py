#!/usr/bin/env python3
"""Hostile mutations for K921."""
import copy, importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SOURCE=ROOT/"tests/channel-swings/k921_sc_act_06_quotient_projector_parent.py"
s=importlib.util.spec_from_file_location("k921",SOURCE);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);base=m.build();m.validate(base)
M=[("theorem","self_adjoint",False),("theorem","idempotent",False),("theorem","gauge_basic","P_H G=G"),("theorem","response_annihilates_range","J P_H=J"),("theorem","range","E1"),("theorem","induced_map_on_H","zero"),("theorem","rank_on_authenticated_old_submodule",0),("decision","abstract_gauge_basic_old_old_parent_constructed",False),("decision","finite_symbol_algebra_forbids_diagonal_repair",True),("decision","source_or_action_owned_local_parent_constructed",True),("decision","SC_ACT_06_proved_or_refuted",True),("","classification","CONVENTIONAL_COMPARATOR"),("","target_claim","SC-ACT-01"),("controls","controls_passed",33),("controls","hostile_mutations_rejected",17),("gu_typed_objects","target","UNTYPED"),("theorem","projector_formula","P_H=0"),("decision","next_exact_input","repeat released span")]
r=0
for sec,k,v in M:
 d=copy.deepcopy(base);(d[sec] if sec else d)[k]=v
 try:m.validate(d)
 except AssertionError:r+=1
assert r==18
print("PASS K921 hostile mutations rejected 18/18")
