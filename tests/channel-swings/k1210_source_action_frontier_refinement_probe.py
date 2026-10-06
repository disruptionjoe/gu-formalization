#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,sys
from pathlib import Path
P=Path(__file__).with_name("k1210_source_action_frontier_refinement.py");s=importlib.util.spec_from_file_location("k1210",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
p=m.build();m.validate_payload(p);rejected=0
for f,k,v in [("release_test","alternative_parent_requires_joint_H_J_d_recomputation",False),("frontier","literal_projector_parent_route_open",True),("frontier","alternative_shiab_changed_parent_route_open",False),("decision","mix_new_J_with_selected_H_allowed",True),("decision","conditional_control_promoted_to_source_owner",True)]:
 q=copy.deepcopy(p);q[f][k]=v
 try:m.validate_payload(q)
 except AssertionError:rejected+=1
if rejected!=5:raise AssertionError("K1210 hostile mutation escaped")
print("K1210 probe: 5/5 hostile mutations rejected")
