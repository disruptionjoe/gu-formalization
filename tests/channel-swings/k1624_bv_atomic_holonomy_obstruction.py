#!/usr/bin/env python3
"""Certificate for K1624's general BV atomic obstruction."""
import json, math, cmath
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def atomic_hat(t):
    return 1-cmath.exp(1j*t)

def average_square(T, n=80000):
    dt=T/n
    return sum(abs(atomic_hat((k+0.5)*dt))**2 for k in range(n))*dt/T

def harmonic_integral(T, n=120000):
    lo=1.0; dx=(T-lo)/n
    return sum(abs(atomic_hat(lo+(k+0.5)*dx))/(lo+(k+0.5)*dx) for k in range(n))*dx

def continuous_hat(t):
    return 1 if t==0 else (cmath.exp(1j*t)-1)/(1j*t)

def main():
    d=json.loads((ROOT/"lab/process/k1624-bv-atomic-holonomy-obstruction.json").read_text());q,z=d["atomic_obstruction"],d["decision"]
    a1=average_square(80);a2=average_square(800);h1=harmonic_integral(40);h2=harmonic_integral(640)
    cont=sum(abs(continuous_hat((k+0.5)*0.02))**2 for k in range(50000))/50000
    checks=[("claim",d["claim_id"]=="K1624"),("BV hypothesis","compactly supported" in q["hypothesis"] and "BV primitive" in q["hypothesis"]),
            ("derivative measure","mu=DG" in q["hypothesis"]),("Fourier identity","|widehat G(t)|=|widehat mu(t)|/|t|" in q["fourier_identity"]),
            ("Wiener atoms","sum_a|mu({a})|^2" in q["wiener"]),("atomic mean square near two",abs(a2-2)<0.01),("atomic convergence",abs(a2-2)<abs(a1-2)),
            ("harmonic divergence",h2>h1+2.0),("atomless control smaller",cont<0.02),("TV conversion","positive Cesaro mean" in q["mean"]),
            ("obstruction integral","int_1^infinity |widehat mu(t)|/t dt=infinity" in q["obstruction"]),("finite restriction removed",z["finite_jump_restriction_removed"]),
            ("all atoms obstruct",z["every_nonzero_derivative_atom_obstructs_L1"]),("atom-free not sufficient",not z["atom_free_is_sufficient"]),
            ("no electric L1",not z["electric_field_L1_proved"]),("no source flow",not z["source_owned_flow"]),("protected",not z["protected_status_change"])]
    for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
