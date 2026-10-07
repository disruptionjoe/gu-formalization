#!/usr/bin/env python3
"""Spectral controls for K1377's free charge-lift energy."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1377-free-charge-lift-energy.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
L,Q=D["lift"],D["decision"]
for label,key,needle in [
 ("lift variable","variable","psi=Qphi"),("lift equation","equation","mu Q^2"),
 ("energy","energy","||Qpi||_2^2"),("phase domain","phase_domain","Qpi in L2"),
 ("spectral form","spectral_form","||Omega Qphi||_2^2"),("conservation","conservation","spectral calculus"),
 ("topology control","topology_control","charged momentum"),("boundary","boundary","Q^2phi")]:check(label,needle in L[key])
for omega in (1.5,2.0,3.25,7.0):
 q0,p0,t=.3,.7,.37;c,s=math.cos(omega*t),math.sin(omega*t)
 q=q0*c+p0*s/omega;p=-q0*omega*s+p0*c
 check(f"modal energy conserved omega={omega}",abs((p*p+omega*omega*q*q)-(p0*p0+omega*omega*q0*q0))<1e-12)
 check(f"spectral energy positive omega={omega}",p*p+omega*omega*q*q>0)
check("lift constructed",Q["free_charge_lift_constructed"])
check("lift conserved",Q["free_charge_lift_conserved"])
check("domain invariant",Q["invariant_free_phase_domain_constructed"])
check("one-sided rejected",not Q["k1372_one_sided_phase_space_sufficient"])
check("coupled theorem absent",not Q["coupled_nonlinear_propagation_proved"])
check("source selection absent",not Q["source_selected_domain"])
check("protected fixed",not Q["protected_status_change"])
assert n==25,n
print("RESULT: PASS 25/25")
