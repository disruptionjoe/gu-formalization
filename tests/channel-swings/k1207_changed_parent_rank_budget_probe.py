#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,sys
from pathlib import Path
P=Path(__file__).with_name("k1207_changed_parent_rank_budget.py");s=importlib.util.spec_from_file_location("k1207",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
p=m.build();m.validate_payload(p);rejected=0
for f,k,v in [("release_test","rank_nullity_bound_applied_on_full_joint_kernel",False),("exact_control","minimum_correction_restriction_ranks",[8191,8191,8191]),("decision","k1189_rank8191_is_full_native_parent_cost",True),("decision","source_owned_parent_constructed",True),("decision","protected_status_moves",True)]:
 q=copy.deepcopy(p);q[f][k]=v
 try:m.validate_payload(q)
 except AssertionError:rejected+=1
if rejected!=5:raise AssertionError("K1207 hostile mutation escaped")
print("K1207 probe: 5/5 hostile mutations rejected")
