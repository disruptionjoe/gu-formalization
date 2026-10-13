#!/usr/bin/env python3
"""Hostile mutations for K1795's admission ceiling."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1795_full_fisher_global_optimizer_admission.py";s=importlib.util.spec_from_file_location("k1795_probe_target",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);base=json.loads(m.ARTIFACT.read_text())
muts=[(("bridge_census","total"),496),(("protected_state","canon_changed"),True),(("entry_state","degree_nine_exact_partition_replayed"),False),(("entry_state","complete_complement_cover_available"),True),(("decision","slab_one_globally_excluded"),False),(("decision","slab_two_globally_excluded"),True),(("decision","unique_stationary_point_on_complete_slab_three"),True),(("decision","global_optimizer_proved"),True),(("decision","source_owned_physical_theory"),True)]
def setp(d,p,v):
 for k in p[:-1]:d=d[k]
 d[p[-1]]=v
for i,(p,v) in enumerate(muts,1):d=copy.deepcopy(base);setp(d,p,v);assert not all(ok for _,ok in m.validate(d)),p;print(f"REJECT {i:02d}: {p}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
