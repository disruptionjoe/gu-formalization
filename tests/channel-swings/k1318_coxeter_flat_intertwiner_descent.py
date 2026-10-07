#!/usr/bin/env python3
"""Exact controls for K1318's D7 Coxeter-flat transport criterion."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1318-coxeter-flat-intertwiner-descent.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
I=tuple(tuple(int(i==j) for j in range(7)) for i in range(7))
def mm(a,b): return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(7)) for j in range(7)) for i in range(7))
def tr(a): return tuple(tuple(a[j][i] for j in range(7)) for i in range(7))
S=[]
for k in range(6):
 m=[list(r) for r in I]; m[k][k]=m[k+1][k+1]=0; m[k][k+1]=m[k+1][k]=1; S.append(tuple(tuple(r) for r in m))
m=[list(r) for r in I]; m[5][5]=m[6][6]=0; m[5][6]=m[6][5]=-1; S.append(tuple(tuple(r) for r in m))
edges={tuple(e) for e in D["coxeter_data"]["simple_edges"]}
check("D7 rank",D["coxeter_data"]["rank"]==len(S)==7)
check("W(D7) order",D["coxeter_data"]["weyl_group_order"]==2**6*math.factorial(7)==322560)
check("six Dynkin edges",len(edges)==6)
check("orthogonal generators",all(mm(tr(s),s)==I for s in S))
check("involutions",all(mm(s,s)==I for s in S))
check("adjacent braids",all(mm(mm(S[i-1],S[j-1]),S[i-1])==mm(mm(S[j-1],S[i-1]),S[j-1]) for i,j in edges))
nonedges=[(i,j) for i in range(1,8) for j in range(i+1,8) if (i,j) not in edges]
check("nonadjacent commute",all(mm(S[i-1],S[j-1])==mm(S[j-1],S[i-1]) for i,j in nonedges))
C=D["descent"]; Q=D["decision"]
check("relations required",C["all_coxeter_relations_required"])
check("path independence",C["path_independent_transport_follows"])
check("coherent W action",C["coherent_W_action_follows"])
check("edge G intertwining conditional",C["K1317_common_transported_G_action_follows_if_each_edge_is_a_G_intertwiner"])
check("analytic family absent",not C["analytic_normalized_intertwiners_constructed_here"])
check("simple-edge reduction",Q["finite_coherence_problem_reduces_to_simple_edges_and_relators"])
check("one path insufficient",not Q["checking_one_path_or_one_chamber_is_sufficient"])
check("conditional not physical",Q["exact_chamber_blind_G_descent_is_conditional"] and not Q["physical_chamber_selection_resolved"] and not Q["source_or_physical_status_moves"])
assert n==17; print("RESULT: PASS 17/17")
