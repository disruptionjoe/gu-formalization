#!/usr/bin/env python3
"""Hostile composition and claim-ceiling mutations for K1774."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1774_full_fisher_preconditioner.py";s=importlib.util.spec_from_file_location("p",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);base=json.loads(m.ARTIFACT.read_text())
muts=[(("preconditioner","effective_search_pieces"),4),(("preconditioner","boundary_retained_cells"),0),(("decision","geometric_preconditioner_completed"),False),(("decision","boundary_strip_excluded"),True),(("decision","full_fisher_interval_newton_completed"),True),(("decision","global_optimizer_proved"),True)]
def setp(d,p,v):
 for k in p[:-1]:d=d[k]
 d[p[-1]]=v
for i,(p,v) in enumerate(muts,1):d=copy.deepcopy(base);setp(d,p,v);assert not all(ok for _,ok in m.validate(d)),p;print(f"PASS {i:02d}: rejected {'.'.join(p)}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
