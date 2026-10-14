#!/usr/bin/env python3
"""Hostile mutations for K1813's fixed-score method limit."""
import copy,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1813_full_fisher_slab_three_stationary_cover.py";s=importlib.util.spec_from_file_location("k1813_probe_base",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);base=json.loads(m.ARTIFACT.read_text());got=base["certificate"]
mutations=[("invent margin",lambda d:d["certificate"]["compact_bounds"].__setitem__("cross_margin_positive",True)),("deny limit",lambda d:d["decision"].__setitem__("sixth_order_parent_certificate_indeterminate",False)),("invent global",lambda d:d["decision"].__setitem__("global_optimizer_proved",True))]
for i,(name,change) in enumerate(mutations,1):d=copy.deepcopy(base);change(d);assert not all(ok for _,ok in m.validate(d,got)),name;print(f"PASS {i:02d}: reject {name}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
