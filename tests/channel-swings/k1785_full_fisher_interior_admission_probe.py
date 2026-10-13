#!/usr/bin/env python3
"""Hostile mutations for K1785's admission ceiling."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1785_full_fisher_interior_admission.py";s=importlib.util.spec_from_file_location("k1785",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);base=json.loads(m.ARTIFACT.read_text())
muts=[(("bridge_census","total"),486),(("protected_state","canon_changed"),True),(("entry_state","whole_line_parameter_jet_available"),True),(("decision","slabs_one_and_two_excluded"),True),(("decision","stationary_box_isolated"),True),(("decision","global_optimizer_proved"),True),(("decision","source_owned_physical_theory"),True)]
def setp(d,p,v):
 for k in p[:-1]:d=d[k]
 d[p[-1]]=v
for i,(p,v) in enumerate(muts,1):d=copy.deepcopy(base);setp(d,p,v);assert not all(x for _,x in m.validate(d)),p;print(f"REJECT {i:02d}: {p}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
