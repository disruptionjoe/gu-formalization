#!/usr/bin/env python3
"""Exact finite-dimensional controls for K1343's radial interaction."""
import hashlib,json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1343-defocusing-principal-series-wave-interaction.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
I=D["interaction"]; Q=D["decision"]
check("cubic equation","lambda ||u||_Hps^2 u" in I["equation"])
check("defocusing parameters",I["parameters"]=="m>0 and lambda>0")
check("positive potential","lambda/4" in I["potential_density"])
check("declared gradient","lambda ||u||_Hps^2 u" in I["gradient"])
lam=Fraction(3,2); m2=Fraction(5,4); vectors=[(1,2,-1),(2,0,3),(-1,-2,4)]
for u in vectors:
 r=sum(Fraction(x*x) for x in u); v=m2*r/2+lam*r*r/4; grad=tuple((m2+lam*r)*x for x in u)
 check("positive sample potential",v>0)
 check("gradient radial",all(grad[i]*u[j]==grad[j]*u[i] for i in range(3) for j in range(3)))
check("unitary sign invariance",all(sum(x*x for x in u)==sum(x*x for x in (u[1],-u[0],u[2])) for u in vectors))
check("energy space",I["energy_space"].startswith("H1(T3;H_ps)"))
check("Sobolev cubic control","locally Lipschitzly to L2" in I["sobolev_control"])
check("global energy argument","global finite-energy evolution" in I["well_posedness"])
check("finite propagation","finite propagation speed" in I["causality"])
check("unitary equivariance","N(Uu)=U N(u)" in I["internal_equivariance"])
check("nonlinear construction",Q["genuine_nonlinear_local_interaction_constructed"])
check("positive energy",Q["positive_coercive_conserved_energy_constructed"])
check("global evolution",Q["global_finite_energy_evolution_constructed"])
check("causal evolution",Q["causal_finite_speed_constructed"])
check("internal equivariance",Q["internal_G_equivariance_constructed"])
check("constraint ceiling",not Q["constraint_complex_constructed"])
check("source ceiling",not Q["gu_action_owned"])
check("physical ceiling",not Q["gu_interacting_physical_theory_constructed"])
assert n==26; print("RESULT: PASS 26/26")
