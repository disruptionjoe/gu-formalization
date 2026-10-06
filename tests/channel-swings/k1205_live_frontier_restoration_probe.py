#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,sys
from pathlib import Path
P=Path(__file__).with_name("k1205_live_frontier_restoration.py");s=importlib.util.spec_from_file_location("k1205",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
p=m.build();m.validate_payload(p);rejected=0
for f,k,v in [("release_test","post_K553_not_reopened",False),("frontier","post_K553_join_open",True),("frontier","K500_current_custody_assembly_open",True),("decision","protected_status_moves",True)]:
 q=copy.deepcopy(p);q[f][k]=v
 try:m.validate_payload(q)
 except AssertionError:rejected+=1
if rejected!=4:raise AssertionError("K1205 hostile mutation escaped")
print("K1205 probe: 4/4 hostile mutations rejected")
