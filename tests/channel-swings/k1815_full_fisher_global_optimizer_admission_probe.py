#!/usr/bin/env python3
"""Hostile mutations for K1815's protected admission."""
import copy,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1815_full_fisher_global_optimizer_admission.py";s=importlib.util.spec_from_file_location("k1815_probe_base",P);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);base=json.loads(m.ARTIFACT.read_text());got=base["certificate"]
mutations=[("reopen slab two",lambda d:d["certificate"].__setitem__("slab_two_excluded",False)),("invent global",lambda d:d["decision"].__setitem__("global_optimizer_proved",True)),("invent physics",lambda d:d["decision"].__setitem__("source_owned_physical_theory",True))]
for i,(name,change) in enumerate(mutations,1):d=copy.deepcopy(base);change(d);assert not all(ok for _,ok in m.validate(d,got)),name;print(f"PASS {i:02d}: reject {name}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
