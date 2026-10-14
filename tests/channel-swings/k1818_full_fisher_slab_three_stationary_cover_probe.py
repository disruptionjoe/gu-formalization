#!/usr/bin/env python3
"""Hostile mutations for K1818's selected route."""
import copy, importlib.util, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1818_full_fisher_slab_three_stationary_cover.py";s=importlib.util.spec_from_file_location("k1818_probe_base",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);base=json.loads(m.ARTIFACT.read_text());got=m.compute()
mutations=[("hide remaining leaves",lambda d:d["certificate"].__setitem__("remaining_leaf_count",0)),("invent stationary cover",lambda d:d["decision"].__setitem__("complete_stationary_cover",True)),("invent global",lambda d:d["decision"].__setitem__("global_optimizer_proved",True))]
for i,(name,change) in enumerate(mutations,1):
 d=copy.deepcopy(base);change(d);assert not all(ok for _,ok in m.validate(d,got)),name;print(f"PASS {i:02d}: reject {name}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
