#!/usr/bin/env python3
"""Hostile mutations for K1777."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1777_full_fisher_boundary_exclusion.py"
s=importlib.util.spec_from_file_location("k1777",P);k=importlib.util.module_from_spec(s);s.loader.exec_module(k)
d=json.loads(k.ARTIFACT.read_text());mutations=[
 (("certificate","input_partition_digest"),"bad"),(("certificate","c_upper"),"0"),
 (("certificate","full_fisher_penalty_upper"),"0"),(("certificate","threshold_above_k1763_candidate"),"0"),(("certificate","residual_gap_lower"),"[-1 +/- 0]"),
 (("decision","both_boundary_cells_excluded"),False),(("decision","boundary_piece_count_remaining"),2),
 (("decision","full_fisher_interval_newton_completed"),True),(("decision","global_optimizer_proved"),True)]
for i,(path,value) in enumerate(mutations,1):
 m=copy.deepcopy(d);x=m
 for key in path[:-1]:x=x[key]
 x[path[-1]]=value
 assert not all(ok for _,ok in k.validate(m));print(f"PASS {i:02d}: rejected {'.'.join(path)}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
