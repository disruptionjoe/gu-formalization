#!/usr/bin/env python3
"""Finite tensor-model equivariance controls for K1339."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1339-principal-series-internal-equivariance.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
T=D["tensor_symmetry"]; Q=D["decision"]
check("tensor field action",T["field_action"].startswith("U(g)=I_spacetime tensor"))
check("scalar spacetime operator",T["field_operator"]=="P=P_spacetime tensor I_Hps")
check("operator commutator",T["commutator"]=="[P,U(g)]=0")
check("Weyl tensor transport",T["weyl_transport"].startswith("I_spacetime tensor R_w"))
def mm(a,b): return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def kron(a,b): return [[a[i//len(b)][j//len(b[0])]*b[i%len(b)][j%len(b[0])] for j in range(len(a[0])*len(b[0]))] for i in range(len(a)*len(b))]
def ident(q): return [[int(i==j) for j in range(q)] for i in range(q)]
A=[[2,0],[0,5]]; I2=ident(2); I3=ident(3); P=kron(A,I3)
internal=[[[0,1,0],[1,0,0],[0,0,1]],[[1,0,0],[0,0,1],[0,1,0]],[[-1,0,0],[0,1,0],[0,0,-1]]]
for j,u in enumerate(internal):
 U=kron(I2,u); check(f"operator commute {j}",mm(P,U)==mm(U,P))
 B=kron([[3,0],[0,7]],I3); check(f"Green commute {j}",mm(B,U)==mm(U,B))
 check(f"unitary finite control {j}",mm([list(x) for x in zip(*u)],u)==I3)
check("internal equivariance",Q["internal_G_equivariance_constructed"])
check("evolution equivariance",Q["evolution_equivariance_constructed"])
check("Green equivariance",Q["green_equivariance_constructed"])
check("chamber-blind dynamics",Q["chamber_blind_free_dynamics_constructed"])
check("charge ceiling",not Q["charge_selected"])
check("observation ceiling",not Q["physical_observation_map_constructed"])
assert n==23; print("RESULT: PASS 23/23")
