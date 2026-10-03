#!/usr/bin/env python3
"""Hostile mutations for K955."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k955_source_epsilon_singular_selector_disposition.py";s=importlib.util.spec_from_file_location("k955",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("certificate","row_count",12),("certificate","satisfied_row_count",4),("certificate","closed_insufficient_row_count",1),("certificate","missing_row_count",4),("certificate","SC_ACT_06_status","PROVED"),("decision","regular_single_scalar_route_closed",False),("decision","singular_single_scalar_proper_local_BFV_route_closed",False),("decision","global_arbitrary_singular_selectors_excluded",True),("decision","charged_boundary_symmetry_remains_honest_horn",False),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K955 hostile mutations rejected 10/10")
