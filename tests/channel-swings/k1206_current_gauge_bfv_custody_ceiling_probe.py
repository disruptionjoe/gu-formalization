#!/usr/bin/env python3
from __future__ import annotations
import copy, importlib.util, sys
from pathlib import Path
P=Path(__file__).with_name("k1206_current_gauge_bfv_custody_ceiling.py");s=importlib.util.spec_from_file_location("k1206",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
p=m.build();m.validate_payload(p);rejected=0
for section,key,value in [("release_test","seven_lock_owner_missing",False),("exact_control","residual_after_full_u_overgrant",[0,0,0]),("exact_control","residual_after_full_u_and_rank98_overgrant",[0,0,0]),("decision","full_u_connection_map_promoted_to_independent_distortion_gauge",True),("decision","protected_status_moves",True)]:
    q=copy.deepcopy(p);q[section][key]=value
    try:m.validate_payload(q)
    except AssertionError:rejected+=1
if rejected!=5:raise AssertionError("K1206 hostile mutation escaped")
print("K1206 probe: 5/5 hostile mutations rejected")
