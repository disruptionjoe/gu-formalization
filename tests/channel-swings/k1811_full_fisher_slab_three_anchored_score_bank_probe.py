#!/usr/bin/env python3
"""Hostile mutations for K1811's sixth-order method-limit bank."""
import copy,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1811_full_fisher_slab_three_anchored_score_bank.py";s=importlib.util.spec_from_file_location("k1811_probe_base",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);base=json.loads(m.ARTIFACT.read_text());got=base["certificate"]
mutations=[("invent rejection",lambda d:d["certificate"].__setitem__("rejected_leaf_count",78)),("invent uniqueness",lambda d:d["decision"].__setitem__("complete_stationary_uniqueness_proved",True)),("retention means point",lambda d:d["decision"].__setitem__("retained_leaf_means_additional_stationary_point",True))]
for i,(name,change) in enumerate(mutations,1):d=copy.deepcopy(base);change(d);assert not all(ok for _,ok in m.validate(d,got)),name;print(f"PASS {i:02d}: reject {name}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
