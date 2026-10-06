#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,sys
from pathlib import Path
P=Path(__file__).with_name("k1200_order_ten_frontier_restoration.py");s=importlib.util.spec_from_file_location("k1200",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
p=m.build();m.validate_payload(p);rejected=0
for f,k,v in [("release_test","historical_completion_preserved",False),("decision","protected_status_moves",True),("frontier","order_ten_complete_conditional_integral_enclosure_open",True),("frontier","native_K152_interval_open",False)]:
 q=copy.deepcopy(p);q[f][k]=v
 try:m.validate_payload(q)
 except AssertionError:rejected+=1
if rejected!=4:raise AssertionError("K1200 hostile mutation escaped")
print("K1200 probe: 4/4 hostile mutations rejected")
