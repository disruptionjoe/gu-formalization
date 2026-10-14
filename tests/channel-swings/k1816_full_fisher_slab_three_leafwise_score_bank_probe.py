#!/usr/bin/env python3
"""Hostile mutations for K1816's calibrated leafwise bank."""
import copy, importlib.util, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1816_full_fisher_slab_three_leafwise_score_bank.py";s=importlib.util.spec_from_file_location("k1816_probe_base",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);base=json.loads(m.ARTIFACT.read_text())
mutations=[("invent full bank",lambda d:d["decision"].__setitem__("complete_compact_leaf_bank_computed",True)),("erase production leaf",lambda d:d["certificate"].__setitem__("completed_order_seven_leaf_ids",[0])),("invent global",lambda d:d["decision"].__setitem__("global_optimizer_proved",True))]
for i,(name,change) in enumerate(mutations,1):
 d=copy.deepcopy(base);change(d);assert not all(ok for _,ok in m.validate(d)),name;print(f"PASS {i:02d}: reject {name}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
