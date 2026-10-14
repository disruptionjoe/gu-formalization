#!/usr/bin/env python3
"""Hostile mutations for K1817's order-eight parent scout."""
import copy, importlib.util, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1817_full_fisher_slab_three_whole_line_value_cover.py";s=importlib.util.spec_from_file_location("k1817_probe_base",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);base=json.loads(m.ARTIFACT.read_text())
mutations=[("invent parent sign",lambda d:d["certificate"]["parent_zero"]["decision"].__setitem__("compact_cross_margin_positive",True)),("deny subdivision",lambda d:d["decision"].__setitem__("leaf_subdivision_required",False)),("invent cover",lambda d:d["decision"].__setitem__("complete_whole_line_value_cover",True))]
for i,(name,change) in enumerate(mutations,1):
 d=copy.deepcopy(base);change(d);assert not all(ok for _,ok in m.validate(d)),name;print(f"PASS {i:02d}: reject {name}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
