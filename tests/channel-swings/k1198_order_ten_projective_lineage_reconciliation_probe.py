#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,sys
from pathlib import Path
P=Path(__file__).with_name("k1198_order_ten_projective_lineage_reconciliation.py");s=importlib.util.spec_from_file_location("k1198",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
p=m.build();m.validate_payload(p);rejected=0
for f,k in [("release_test","all_shared_censuses_equal"),("release_test","stronger_lineage_retained"),("lineage_reconciliation","K543_executes_positive_width_projective_controls"),("lineage_reconciliation","K545_supplies_global_disjoint_ownership")]:
 q=copy.deepcopy(p);q[f][k]=False
 try:m.validate_payload(q)
 except AssertionError:rejected+=1
if rejected!=4:raise AssertionError("K1198 hostile mutation escaped")
print("K1198 probe: 4/4 hostile mutations rejected")
