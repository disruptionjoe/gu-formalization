#!/usr/bin/env python3
"""Exhaustive controls for K1323's cycle-product obstruction."""
import hashlib,itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1323-cycle-product-obstruction-control.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
E=[tuple(e) for e in D["triangle_control"]["edges"]]; rows=[]
for bits in itertools.product((-1,1),repeat=3):
 beta=dict(zip(E,bits)); prod=bits[0]*bits[1]*bits[2]
 solved=any(all(e[u]*e[v]==b for (u,v),b in beta.items()) for e in ({i:s[i-1] for i in range(1,4)} for s in itertools.product((-1,1),repeat=3)))
 rows.append((bits,prod,solved)); assert solved==(prod==1)
T=D["triangle_control"]; Q=D["decision"]
check("eight assignments",len(rows)==T["assignment_count"]==8)
check("four solvable",sum(r[2] for r in rows)==T["solvable_count"]==4)
check("cycle criterion exact",all(s==(p==1) for _,p,s in rows))
check("one negative obstructed",T["one_negative_edge_product"]==-1 and not T["one_negative_edge_solvable"])
check("two negatives soluble",T["two_negative_edges_product"]==1 and T["two_negative_edges_solvable"])
check("intrinsic cycle sign",Q["cycle_sign_can_be_intrinsic_to_edge_rephasing_problem"])
check("no D7 graph cycle",not Q["D7_simple_graph_has_cycle_obstruction"])
check("general cocycle ceiling",not Q["arbitrary_projective_Coxeter_cocycle_classified"])
check("no status move",not Q["source_or_physical_status_moves"])
check("necessity recorded","twice" in D["general_theorem"]["necessity"])
check("sufficiency recorded","spanning tree" in D["general_theorem"]["sufficiency"])
check("triangle has one cycle",len(E)==3)
assert n==14; print("RESULT: PASS 14/14")
