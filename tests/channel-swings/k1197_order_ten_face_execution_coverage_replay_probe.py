#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,sys
from pathlib import Path
P=Path(__file__).with_name("k1197_order_ten_face_execution_coverage_replay.py");s=importlib.util.spec_from_file_location("k1197",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
p=m.build();m.validate_payload(p);rejected=0
for f,k,v in [("release_test","exactly_229_shards",False),("custody_replay","executed_ids_equal_plan",False),("custody_replay","all_direct_overlap_controls_pass",False),("decision","complete_order_ten_integral_enclosure_emitted",True)]:
 q=copy.deepcopy(p);q[f][k]=v
 try:m.validate_payload(q)
 except AssertionError:rejected+=1
if rejected!=4:raise AssertionError("K1197 hostile mutation escaped")
print("K1197 probe: 4/4 hostile mutations rejected")
