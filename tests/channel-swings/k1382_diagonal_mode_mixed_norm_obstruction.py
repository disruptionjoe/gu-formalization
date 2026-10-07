#!/usr/bin/env python3
"""Diagonal charge-frequency controls for K1382."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1382-diagonal-mode-mixed-norm-obstruction.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
M,Q=D["diagonal_modes"],D["decision"]
for label,key,needle in [
 ("mode","mode","q_N=4N"),("amplitude","amplitude","q_N^(-n)"),
 ("energy","energy_normalization","=1"),("mixed norm","mixed_norm","asymptotic to (4N)^sigma/sqrt(2)"),
 ("finite p","finite_p","diverges"),("endpoint","endpoint","bounded"),
 ("jointness","jointness","both q_N")]:check(label,needle in M[key])
for sigma in (.25,.5,1.0):
 vals=[]
 for N in (4,16,64):
  q=4*N;k=q;a=q**(-2)/(k*k+q*q)**.5
  energy=(k*q**2*a)**2+(q**3*a)**2
  mixed=q**3*((1+k*k)**(sigma/2))*a
  check(f"normalized energy sigma={sigma:g} N={N}",abs(energy-1)<1e-12)
  vals.append(mixed)
 check(f"mixed norm grows sigma={sigma:g}",vals[2]>vals[1]>vals[0])
check("energy bounded",Q["same_lifted_energy_uniformly_bounded"])
check("mixed norm unbounded",Q["finite_p_mixed_norm_unbounded"])
check("same-energy bound absent",not Q["same_energy_finite_p_bound_exists"])
check("endpoint survives",not Q["endpoint_counterexample"])
check("other repairs open",not Q["all_dispersive_repairs_excluded"])
check("global theorem absent",not Q["global_nonlinear_evolution_proved"])
check("protected fixed",not Q["protected_status_change"])
assert n==27,n
print("RESULT: PASS 27/27")
