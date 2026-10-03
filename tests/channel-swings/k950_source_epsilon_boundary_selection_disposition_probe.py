#!/usr/bin/env python3
"""Hostile mutations for K950."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k950_source_epsilon_boundary_selection_disposition.py";s=importlib.util.spec_from_file_location("k950",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("certificate","row_count",10),("certificate","satisfied_row_count",5),("certificate","missing_row_count",4),("certificate","SC_ACT_06_status","PROVED"),("decision","zero_reduction_not_promoted",False),("decision","invariant_conservation_not_misread_as_selection",False),("decision","singular_selector_globally_excluded",True),("decision","formal_seven_lock_is_source_owned",True),("decision","charged_boundary_symmetry_remains_honest_horn",False),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K950 hostile mutations rejected 10/10")
