#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,sys
from pathlib import Path
P=Path(__file__).with_name("k1204_k500_current_custody_route_disposition.py");s=importlib.util.spec_from_file_location("k1204",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
p=m.build();m.validate_payload(p);rejected=0
for f,k,v in [("release_test","K609_upper_preserved",False),("route","K795_current_AB_executable",True),("route","K798_global_K500_route_killed",True),("decision","K473_or_K152_released",True)]:
 q=copy.deepcopy(p);q[f][k]=v
 try:m.validate_payload(q)
 except AssertionError:rejected+=1
if rejected!=4:raise AssertionError("K1204 hostile mutation escaped")
print("K1204 probe: 4/4 hostile mutations rejected")
