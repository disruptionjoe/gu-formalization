#!/usr/bin/env python3
"""Hostile census, protection and promotion mutations for K1770."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1770_correlated_cover_admission.py";s=importlib.util.spec_from_file_location("producer",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text());muts=[(("bridge_census","total"),471),(("protected_state","canon_changed"),True),(("protected_state","k1145_score"),"1/7"),(("decision","correlation_preserving_engine_admitted"),False),(("decision","zero_unresolved_partition_admitted"),False),(("decision","full_fisher_stationarity_or_uniqueness_admitted"),True),(("decision","global_two_radius_optimizer_admitted"),True),(("decision","all_seed_or_physical_result_admitted"),True)]
def setp(d,path,val):
 for k in path[:-1]:d=d[k]
 d[path[-1]]=val
for i,(path,val) in enumerate(muts,1):
 d=copy.deepcopy(base);setp(d,path,val);assert not all(ok for _,ok in m.validate(d)),path;print(f"PASS {i:02d}: rejected {'.'.join(path)}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
