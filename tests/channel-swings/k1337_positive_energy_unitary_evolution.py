#!/usr/bin/env python3
"""Modewise energy and evolution controls for K1337."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1337-positive-energy-unitary-evolution.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
pin=D["pinned_inputs"]["k1336"]; check("k1336 pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
E=D["energy_system"]; Q=D["decision"]
check("energy space",E["energy_space"]=="E=D(A_m^(1/2)) direct_sum H")
check("generator domain",E["generator_domain"]=="D(G)=D(A_m) direct_sum D(A_m^(1/2))")
def mm(a,b): return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a): return [list(x) for x in zip(*a)]
for w2 in (1.0,2.25,5.0,19.25):
 g=[[0.0,1.0],[-w2,0.0]]; h=[[w2,0.0],[0.0,1.0]]
 defect=[[mm(tr(g),h)[i][j]+mm(h,g)[i][j] for j in range(2)] for i in range(2)]
 check(f"skew metric omega2={w2}",max(abs(x) for row in defect for x in row)<1e-12)
 t=.37; w=math.sqrt(w2); c=math.cos(w*t); s=math.sin(w*t)
 u=[[c,s/w],[-w*s,c]]
 conserved=mm(mm(tr(u),h),u)
 check(f"energy preserved omega2={w2}",max(abs(conserved[i][j]-h[i][j]) for i in range(2) for j in range(2))<1e-12)
 check(f"group inverse omega2={w2}",abs(u[0][0]*u[1][1]-u[0][1]*u[1][0]-1)<1e-12)
check("skew-adjoint decision",Q["generator_skew_adjoint_on_energy_space"])
check("unitary evolution",Q["unitary_strongly_continuous_evolution"])
check("positive energy",Q["positive_conserved_energy"])
check("frequency gap",Q["strict_frequency_gap"])
check("interaction ceiling",not Q["bounded_below_interacting_hamiltonian_constructed"])
check("physical-time ceiling",not Q["gu_physical_time_evolution_constructed"])
assert n==21; print("RESULT: PASS 21/21")
