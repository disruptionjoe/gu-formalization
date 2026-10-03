#!/usr/bin/env python3
"""Hostile mutations for K923."""
import copy,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SOURCE=ROOT/"tests/channel-swings/k923_sc_act_06_forty_type_projector_repair.py"
s=importlib.util.spec_from_file_location("k923",SOURCE);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);base=m.build();m.validate(base)
M=[("composition","induced_operator","zero"),("composition","rank",0),("composition","real_type_count",39),("composition","total_real_multiplicity",168),("composition","rank_on_every_occupied_isotypic_block","partial"),("composition","kernel_on_H_old",1),("composition","released_residual_square_rank_on_H_old",1),("composition","strictly_new_formal_capacity_relative_to_released_span",False),("composition","gauge_descent","P_H G=G"),("decision","abstract_diagonal_repair_covers_authenticated_old_submodule",False),("decision","forty_type_capacity_obstruction_for_formal_parent",True),("decision","released_K_HQ_span_reopened",True),("decision","source_owned_GU_repair_constructed",True),("decision","SC_ACT_06_proved_or_refuted",True),("controls","controls_passed",33),("controls","hostile_mutations_rejected",17),("gu_typed_objects","target","UNTYPED"),("decision","next_exact_input","promote projector")]
r=0
for sec,k,v in M:
 d=copy.deepcopy(base);(d[sec] if sec else d)[k]=v
 try:m.validate(d)
 except AssertionError:r+=1
assert r==18
print("PASS K923 hostile mutations rejected 18/18")
