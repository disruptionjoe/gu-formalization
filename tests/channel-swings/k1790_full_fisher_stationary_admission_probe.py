#!/usr/bin/env python3
"""Hostile mutations for K1790's admission ceiling."""
import copy, importlib.util, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1790_full_fisher_stationary_admission.py"
s=importlib.util.spec_from_file_location("k1790_probe_target",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);base=json.loads(m.ARTIFACT.read_text())
muts=[
 (("bridge_census","total"),491),
 (("protected_state","canon_changed"),True),
 (("entry_state","whole_line_local_parameter_jet_available"),False),
 (("entry_state","complete_complement_cover_available"),True),
 (("decision","slabs_one_and_two_globally_excluded"),True),
 (("decision","unique_stationary_point_on_complete_slab_three"),True),
 (("decision","global_optimizer_proved"),True),
 (("decision","source_owned_physical_theory"),True),
]
def setp(d,p,v):
 for key in p[:-1]:d=d[key]
 d[p[-1]]=v
for i,(p,v) in enumerate(muts,1):
 d=copy.deepcopy(base);setp(d,p,v);assert not all(ok for _,ok in m.validate(d)),p;print(f"REJECT {i:02d}: {p}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
