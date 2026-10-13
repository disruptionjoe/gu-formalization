#!/usr/bin/env python3
"""Hostile partition-accounting and promotion mutations for K1768."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1768_bernstein_sublevel_partition.py";s=importlib.util.spec_from_file_location("producer",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text());got=m.summary(m.replay());muts=[(("partition","pruned_leaves"),0),(("partition","retained_leaves"),0),(("partition","unresolved_leaves"),1),(("partition","partition_digest"),"0"*64),(("decision","complete_partition_emitted"),False),(("decision","every_pruned_leaf_has_positive_bernstein_lower_bound"),False),(("decision","retained_leaf_means_below_threshold"),True),(("decision","global_optimizer_proved"),True)]
def setp(d,path,val):
 for k in path[:-1]:d=d[k]
 d[path[-1]]=val
def validate(d):
 return [("partition replay",d["partition"]==got),("complete",d["decision"]["complete_partition_emitted"]),("bernstein",d["decision"]["every_pruned_leaf_has_positive_bernstein_lower_bound"]),("retained fence",not d["decision"]["retained_leaf_means_below_threshold"]),("global fence",not d["decision"]["global_optimizer_proved"])]
for i,(path,val) in enumerate(muts,1):
 d=copy.deepcopy(base);setp(d,path,val);assert not all(ok for _,ok in validate(d)),path;print(f"PASS {i:02d}: rejected {'.'.join(path)}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
