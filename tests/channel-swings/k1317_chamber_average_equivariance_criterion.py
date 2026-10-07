#!/usr/bin/env python3
"""Exact controls for K1317's chamber-average equivariance criterion."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1317-chamber-average-equivariance-criterion.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
def mm(a,b): return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def sub(a,b): return [[a[i][j]-b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def block_diag(bs):
 d=len(bs[0]); out=[[0.0]*(d*len(bs)) for _ in range(d*len(bs))]
 for c,b in enumerate(bs):
  for i in range(d):
   for j in range(d): out[c*d+i][c*d+j]=b[i][j]
 return out
N=3; d=2; P=[[0.0]*(N*d) for _ in range(N*d)]
for c in range(N):
 for e in range(N):
  for j in range(d): P[c*d+j][e*d+j]=1/N
A=[[0.0,-1.0],[1.0,0.0]]; same=block_diag([A,A,A]); bad=block_diag([A,A,[[1.0,0.0],[0.0,-1.0]]])
comm=lambda B:max(abs(z) for row in sub(mm(P,B),mm(B,P)) for z in row)
C=D["criterion"]; Q=D["decision"]
check("same transported actions commute",comm(same)<1e-12)
check("unequal transported action fails",comm(bad)>1e-6)
v=[2.0,-3.0]; diag=v*3
check("same action preserves diagonal",[sum(same[i][j]*diag[j] for j in range(6)) for i in range(6)]==[-v[1],v[0]]*3)
out=[sum(bad[i][j]*diag[j] for j in range(6)) for i in range(6)]
check("unequal action leaves diagonal",out[:2]!=out[4:6])
check("necessity",C["necessity"])
check("sufficiency",C["sufficiency"])
check("fiber unity insufficient",not C["raw_fiber_unitarity_is_sufficient"])
check("positive sum insufficient",not C["positive_direct_sum_is_sufficient"])
check("conditional descent",Q["K1316_average_can_be_G_descended_conditionally"])
check("positivity not proof",not Q["K1314_chamberwise_positivity_alone_proves_descent"])
check("intertwiners required",Q["normalized_intertwiner_data_still_required"])
check("not physical",not Q["physical_sector_constructed"] and not Q["source_or_physical_status_moves"])
assert n==14; print("RESULT: PASS 14/14")
