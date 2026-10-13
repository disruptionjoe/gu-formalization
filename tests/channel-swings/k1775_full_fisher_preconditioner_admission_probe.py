#!/usr/bin/env python3
"""Hostile census, protection and promotion mutations for K1775."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1775_full_fisher_preconditioner_admission.py";s=importlib.util.spec_from_file_location("p",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);base=json.loads(m.ARTIFACT.read_text())
muts=[(("bridge_census","total"),474),(("protected_state","source_register_changed"),True),(("protected_state","ledger_changed"),True),(("decision","five_piece_geometric_preconditioner_admitted"),False),(("decision","boundary_strip_exclusion_admitted"),True),(("decision","full_fisher_interval_newton_admitted"),True),(("decision","global_two_radius_optimizer_admitted"),True),(("decision","all_seed_or_physical_result_admitted"),True)]
def setp(d,p,v):
 for k in p[:-1]:d=d[k]
 d[p[-1]]=v
for i,(p,v) in enumerate(muts,1):d=copy.deepcopy(base);setp(d,p,v);assert not all(ok for _,ok in m.validate(d)),p;print(f"PASS {i:02d}: rejected {'.'.join(p)}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
