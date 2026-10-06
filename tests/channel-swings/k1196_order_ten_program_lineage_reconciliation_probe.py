#!/usr/bin/env python3
"""Hostile probe for K1196."""
from __future__ import annotations
import copy, importlib.util, sys
from pathlib import Path
P=Path(__file__).with_name("k1196_order_ten_program_lineage_reconciliation.py")
s=importlib.util.spec_from_file_location("k1196",P); m=importlib.util.module_from_spec(s); sys.modules[s.name]=m; s.loader.exec_module(m)
p=m.build(); m.validate_payload(p); rejected=0
for mutate in [
 lambda q:q["release_test"].__setitem__("ordered_ids_equal",False),
 lambda q:q["lineage_reconciliation"].__setitem__("program_bank_byte_digests_identical",True),
 lambda q:q["decision"].__setitem__("historical_K487_results_retracted",True),
 lambda q:q["release_test"].__setitem__("protected_status_unchanged",False)]:
 q=copy.deepcopy(p); mutate(q)
 try:m.validate_payload(q)
 except AssertionError:rejected+=1
if rejected!=4: raise AssertionError("K1196 hostile mutation escaped")
print("K1196 probe: 4/4 hostile mutations rejected")
