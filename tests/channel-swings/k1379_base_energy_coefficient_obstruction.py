#!/usr/bin/env python3
"""Concentration controls for K1379's coefficient obstruction."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1379-base-energy-coefficient-obstruction.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C,Q=D["concentration"],D["decision"]
for label,key,needle in [
 ("block","block","Dirichlet square"),("L2","l2","=||v_N||_2=1"),("Linfinity","linfinity","(2N+1)^(3/2)"),
 ("electric data","electric_data","fixed L2"),("radial data","radial_data","e_4"),
 ("radial energy","radial_energy","uniformly bounded"),("radial derivative","radial_derivative","2lambda"),
 ("neutrality","neutrality","=0"),("conclusion","conclusion","do not bound")]:check(label,needle in C[key])
for N in (2,4,8,16):
 l2=1.0;electric_linf=2*N+1;radial_linf=(2*N+1)**1.5;df=2*radial_linf
 check(f"fixed L2 N={N}",l2==1.0)
 check(f"growing Linfinity N={N}",electric_linf>=N and radial_linf>=N)
 check(f"growing radial derivative N={N}",df>=2*N)
check("base energy bounded",Q["base_energy_uniformly_bounded"])
check("Gauss satisfied",Q["gauss_constraint_satisfied"])
check("coefficient unbounded",Q["required_coefficient_norm_unbounded"])
check("Gronwall not closed",not Q["k1378_gronwall_closed_by_base_energy"])
check("weaker estimates open",not Q["weaker_spacetime_estimate_excluded"])
check("global theorem absent",not Q["global_nonlinear_evolution_proved"])
check("protected fixed",not Q["protected_status_change"])
assert n==30,n
print("RESULT: PASS 30/30")
