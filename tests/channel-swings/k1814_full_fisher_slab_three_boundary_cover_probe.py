#!/usr/bin/env python3
"""Hostile mutations for K1814's boundary status."""
import copy,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1814_full_fisher_slab_three_boundary_cover.py";s=importlib.util.spec_from_file_location("k1814_probe_base",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);base=json.loads(m.ARTIFACT.read_text());got=base["certificate"]
mutations=[("drop retained",lambda d:d["certificate"].__setitem__("retained_leaves",0)),("invent parent sign",lambda d:d["certificate"].__setitem__("first_parent_margin_certified_positive",True)),("invent boundary",lambda d:d["decision"].__setitem__("all_slab_three_faces_and_vertices_certified",True))]
for i,(name,change) in enumerate(mutations,1):d=copy.deepcopy(base);change(d);assert not all(ok for _,ok in m.validate(d,got)),name;print(f"PASS {i:02d}: reject {name}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
