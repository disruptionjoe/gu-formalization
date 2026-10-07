#!/usr/bin/env python3
"""Exact countercontrol for K1319's projective braid holonomy."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1319-projective-chamber-holonomy-boundary.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
I=tuple(tuple(int(i==j) for j in range(7)) for i in range(7))
def mm(a,b): return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(7)) for j in range(7)) for i in range(7))
def tr(a): return tuple(tuple(a[j][i] for j in range(7)) for i in range(7))
def smul(s,a): return tuple(tuple(s*z for z in r) for r in a)
def simple(k):
 m=[list(r) for r in I]
 if k<7: m[k-1][k-1]=m[k][k]=0; m[k-1][k]=m[k][k-1]=1
 else: m[5][5]=m[6][6]=0; m[5][6]=m[6][5]=-1
 return tuple(tuple(r) for r in m)
S5=simple(5); S6=simple(6); T5=S5; T6=smul(-1,S6)
L=mm(mm(T5,T6),T5); R=mm(mm(T6,T5),T6); C=D["countercontrol"]; Q=D["decision"]
check("base braid",mm(mm(S5,S6),S5)==mm(mm(S6,S5),S6))
check("T5 unitary",mm(tr(T5),T5)==I)
check("T6 unitary",mm(tr(T6),T6)==I)
check("T5 involutive",mm(T5,T5)==I)
check("T6 involutive",mm(T6,T6)==I)
check("exact braid fails",L!=R and not C["exact_braid_relation_holds"])
check("relative minus phase",L==smul(-1,R) and C["relative_phase"]==-1)
check("projective braid holds",C["projective_braid_relation_holds"])
check("no exact path independence",not C["path_independent_exact_transport"])
check("unitarity not flatness",not Q["edge_unitarity_and_positivity_imply_flatness"])
check("projective not exact",not Q["projective_equivalence_is_exact_chamber_descent"])
check("trivialization required and no status move",Q["relator_phase_must_be_trivialized"] and not Q["source_or_physical_status_moves"])
assert n==14; print("RESULT: PASS 14/14")
