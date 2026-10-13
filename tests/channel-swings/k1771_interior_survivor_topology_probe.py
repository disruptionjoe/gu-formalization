#!/usr/bin/env python3
"""Hostile topology, accounting and promotion mutations for K1771."""
import copy, importlib.util, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; P=ROOT/"tests/channel-swings/k1771_interior_survivor_topology.py"
s=importlib.util.spec_from_file_location("producer",P);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
base=json.loads(m.ARTIFACT.read_text()); got=m.replay()
muts=[(("topology","input_interior_cells"),58),(("topology","slab_count"),4),(("topology","topology_digest"),"0"*64),(("topology","all_z_intervals_contiguous"),False),(("decision","stationarity_proved"),True),(("decision","full_fisher_exclusion_proved"),True)]
def setp(d,p,v):
 for k in p[:-1]: d=d[k]
 d[p[-1]]=v
def valid(d): return d["topology"]==got and d["topology"]["cell_count_conserved"] and not d["decision"]["stationarity_proved"] and not d["decision"]["full_fisher_exclusion_proved"]
for i,(p,v) in enumerate(muts,1):
 d=copy.deepcopy(base);setp(d,p,v);assert not valid(d),p;print(f"PASS {i:02d}: rejected {'.'.join(p)}")
print(f"RESULT: PASS {len(muts)}/{len(muts)}")
