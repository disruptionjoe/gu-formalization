#!/usr/bin/env python3
"""Exhaustive controls for K1322's D7 tree sign trivialization."""
import hashlib,itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1322-d7-tree-braid-sign-trivialization.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
E=[tuple(e) for e in D["graph"]["edges"]]
check("D7 vertices",D["graph"]["vertices"]==7)
check("six edges",len(E)==6)
check("tree Euler count",len(E)==D["graph"]["vertices"]-1)
solutions=[]
for bits in itertools.product((-1,1),repeat=len(E)):
 beta=dict(zip(E,bits)); eps={1:1}
 pending=True
 while pending:
  pending=False
  for (u,v),b in beta.items():
   if u in eps and v not in eps: eps[v]=b*eps[u]; pending=True
   elif v in eps and u not in eps: eps[u]=b*eps[v]; pending=True
 assert len(eps)==7 and all(eps[u]*eps[v]==b for (u,v),b in beta.items())
 count=sum(all(e[u]*e[v]==b for (u,v),b in beta.items()) for e in ({i:s[i-1] for i in range(1,8)} for s in itertools.product((-1,1),repeat=7)))
 solutions.append(count)
check("all assignments enumerated",len(solutions)==64==D["theorem"]["defect_assignment_count"])
check("two solutions each",set(solutions)=={2} and D["theorem"]["solutions_per_assignment"]==2)
check("all coboundaries",D["theorem"]["every_edge_sign_assignment_is_a_vertex_coboundary"])
check("global-sign uniqueness",D["theorem"]["uniqueness_modulo_global_sign"])
check("exact braids",D["theorem"]["all_adjacent_braids_become_exact"])
Q=D["decision"]
check("K1319 defect not intrinsic",not Q["k1319_displayed_minus_one_is_intrinsic_D7_holonomy"])
check("finite sign obstruction closed",not Q["finite_D7_sign_normalization_obstruction_remains"])
check("analytic ceiling",not Q["non_sign_or_analytic_obstruction_excluded"])
check("no status move",not Q["source_or_physical_status_moves"])
check("connected acyclic",D["graph"]["connected"] and D["graph"]["acyclic"])
assert n==14; print("RESULT: PASS 14/14")
