#!/usr/bin/env python3
"""Hostile mutations for K945."""
import copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[2];P=R/"tests/channel-swings/k945_source_epsilon_gauge_ownership_boundary.py";s=importlib.util.spec_from_file_location("k945",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);b=m.build();m.validate(b)
M=[("certificate","row_count",10),("certificate","satisfied_row_count",6),("certificate","missing_row_count",4),("certificate","SC_ACT_06_status","PROVED"),("decision","projector_parent_not_retried",False),("decision","full_zero_gauging_leaves_nontrivial_edge_sector",True),("decision","regular_nonzero_orbit_leaves_dimension",0),("decision","current_action_selects_fixed_nonzero_orbit",True),("decision","charged_boundary_symmetry_retains_zero_import_primacy",False),("decision","SC_ACT_06_proved_or_refuted",True)]
n=0
for a,k,v in M:
 d=copy.deepcopy(b);d[a][k]=v
 try:m.validate(d)
 except AssertionError:n+=1
assert n==10
print("PASS K945 hostile mutations rejected 10/10")
