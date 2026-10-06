#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,sys
from pathlib import Path
P=Path(__file__).with_name("k1199_order_ten_completion_chain_replay.py");s=importlib.util.spec_from_file_location("k1199",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
p=m.build();m.validate_payload(p);rejected=0
mut=[("release_test","prefactor_applied_once",False),("completion_chain","zero_inclusive_determinant_envelopes_complete",False),("decision","action_column_emitted",True),("decision","native_K152_interval_emitted",True)]
for f,k,v in mut:
 q=copy.deepcopy(p);q[f][k]=v
 try:m.validate_payload(q)
 except AssertionError:rejected+=1
if rejected!=4:raise AssertionError("K1199 hostile mutation escaped")
print("K1199 probe: 4/4 hostile mutations rejected")
