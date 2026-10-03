#!/usr/bin/env python3
"""Hostile mutations for K953."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k953_source_epsilon_seven_generator_lower_bound.py";s=importlib.util.spec_from_file_location("k953",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("theorem","ambient_regular_local_dimension",6),("theorem","cotangent_space_dimension",6),("theorem","minimal_generator_count_by_nakayama",1),("theorem","point_ideal_generator_lower_bound",1),("theorem","seven_coordinate_generators_are_sufficient",False),("theorem","one_principal_generator_is_sufficient",True),("theorem","source_selected_generator_count",1),("decision","minimal_reduced_local_selector_requires_seven_generators",False),("decision","higher_stage_data_can_make_one_degree_one_image_generate_the_point_ideal",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K953 hostile mutations rejected 10/10")
