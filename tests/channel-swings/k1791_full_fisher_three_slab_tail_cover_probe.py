#!/usr/bin/env python3
"""Hostile mutations for K1791's exact partition boundary."""
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];P=ROOT/"tests/channel-swings/k1791_full_fisher_three_slab_tail_cover.py"
s=importlib.util.spec_from_file_location("k1791_probe_target",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);base=json.loads(m.ARTIFACT.read_text());got=copy.deepcopy(base["partition"])
muts=[(("partition","pruned_leaves"),127),(("partition","retained_leaves"),24),(("partition","unresolved_leaves"),1),(("partition","partition_digest"),"0"*64),(("decision","complete_adaptive_partition_emitted"),False),(("decision","every_pruned_leaf_has_positive_bernstein_lower_bound"),False),(("decision","retained_leaf_means_below_threshold"),True),(("decision","complete_full_fisher_complement_excluded"),True),(("decision","global_optimizer_proved"),True)]
def setp(d,p,v):
 for key in p[:-1]:d=d[key]
 d[p[-1]]=v
for i,(p,v) in enumerate(muts,1):
 d=copy.deepcopy(base);setp(d,p,v);assert not all(ok for _,ok in m.validate(d,got)),p;print(f"REJECT {i:02d}: {p}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
