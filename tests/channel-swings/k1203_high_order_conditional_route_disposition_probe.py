#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,sys
from pathlib import Path
P=Path(__file__).with_name("k1203_high_order_conditional_route_disposition.py");s=importlib.util.spec_from_file_location("k1203",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
p=m.build();m.validate_payload(p);rejected=0
for f,k,v in [("release_test","zero_targets_met",False),("route","current_route_emits_K152",True),("decision","K218_K152_route_globally_killed",True),("decision","protected_status_moves",True)]:
 q=copy.deepcopy(p);q[f][k]=v
 try:m.validate_payload(q)
 except AssertionError:rejected+=1
if rejected!=4:raise AssertionError("K1203 hostile mutation escaped")
print("K1203 probe: 4/4 hostile mutations rejected")
