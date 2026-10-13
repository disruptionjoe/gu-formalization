#!/usr/bin/env python3
"""Hostile survivor-accounting and promotion mutations for K1769."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1769_degree_seven_survivor_refinement.py";s=importlib.util.spec_from_file_location("producer",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text());got=m.summary(m.replay());muts=[(("refinement","newly_pruned_leaves"),0),(("refinement","retained_leaves"),61),(("refinement","unresolved_leaves"),1),(("refinement","refinement_digest"),"0"*64),(("decision","degree_seven_strictly_contracts_degree_five_cover"),False),(("decision","full_fisher_interval_newton_completed"),True),(("decision","stationarity_proved"),True),(("decision","global_optimizer_proved"),True)]
def setp(d,path,val):
 for k in path[:-1]:d=d[k]
 d[path[-1]]=val
def validate(d):
 z=d["decision"];return [("replay",d["refinement"]==got),("contracts",z["degree_seven_strictly_contracts_degree_five_cover"]),("replayable",z["survivor_union_is_replayable"]),("Fisher fence",not z["full_fisher_interval_newton_completed"]),("stationary fence",not z["stationarity_proved"]),("global fence",not z["global_optimizer_proved"])]
for i,(path,val) in enumerate(muts,1):
 d=copy.deepcopy(base);setp(d,path,val);assert not all(ok for _,ok in validate(d)),path;print(f"PASS {i:02d}: rejected {'.'.join(path)}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
