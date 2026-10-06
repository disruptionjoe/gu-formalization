#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,sys
from pathlib import Path
P=Path(__file__).with_name("k1208_stratumwise_projector_parent_control.py");s=importlib.util.spec_from_file_location("k1208",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
p=m.build();m.validate_payload(p);rejected=0
for f,k,v in [("release_test","S_kernel_equals_retained_gauge",False),("exact_control","control_parent_ranks",[1,1,1]),("exact_control","control_parent_kernel_dimensions",[0,0,0]),("decision","native_changed_parent_constructed",True),("decision","nonzero_physical_cohomology_preserved",True)]:
 q=copy.deepcopy(p);q[f][k]=v
 try:m.validate_payload(q)
 except AssertionError:rejected+=1
if rejected!=5:raise AssertionError("K1208 hostile mutation escaped")
print("K1208 probe: 5/5 hostile mutations rejected")
