#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,sys
from pathlib import Path
P=Path(__file__).with_name("k1209_projector_parent_functional_boundary.py");s=importlib.util.spec_from_file_location("k1209",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
p=m.build();m.validate_payload(p);rejected=0
for f,k,v in [("release_test","k1145_nonzero_cohomology_gate_fails",False),("exact_control","rank_jump",0),("exact_control","failed_gate_count",6),("decision","literal_projector_is_continuous_cross_null_family",True),("decision","native_parent_admitted",True)]:
 q=copy.deepcopy(p);q[f][k]=v
 try:m.validate_payload(q)
 except AssertionError:rejected+=1
if rejected!=5:raise AssertionError("K1209 hostile mutation escaped")
print("K1209 probe: 5/5 hostile mutations rejected")
