#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,sys
from pathlib import Path
P=Path(__file__).with_name("k1201_order_ten_to_q12_lineage_replay.py");s=importlib.util.spec_from_file_location("k1201",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
p=m.build();m.validate_payload(p);rejected=0
for f,k,v in [("release_test","K553_consumed_exactly",False),("lineage","complete_Q12_emitted",False),("decision","K152_shifted_form_residual_emitted",True),("decision","protected_status_moves",True)]:
 q=copy.deepcopy(p);q[f][k]=v
 try:m.validate_payload(q)
 except AssertionError:rejected+=1
if rejected!=4:raise AssertionError("K1201 hostile mutation escaped")
print("K1201 probe: 4/4 hostile mutations rejected")
