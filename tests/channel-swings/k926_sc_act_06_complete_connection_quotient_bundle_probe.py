#!/usr/bin/env python3
"""Hostile mutations for K926."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k926_sc_act_06_complete_connection_quotient_bundle.py";s=importlib.util.spec_from_file_location("k926",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("composition","field_dimension",1),("composition","response_rank",1),("composition","response_nullity",1),("composition","gauge_rank",1),("composition","cohomology_rank",1),("composition","response_rank_constant_on_all_orbits",False),("composition","JG_zero_on_flat_zero_locus",False),("decision","complete_connection_sector_cosphere_bundle_established",False),("decision","complete_full_field_cohomology_computed",True),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K926 hostile mutations rejected 10/10")
