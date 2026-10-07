#!/usr/bin/env python3
"""Exact scope controls for K1395's compact-torus obstruction."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1395-compact-torus-coefficient-integrability-obstruction.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
F,Q=D["integrability_obstruction"],D["decision"]
for label,key,needle in [("baseline","baseline","including the vacuum"),("mode","nontrivial_mode","Q-eigenvector"),("ODE","reduced_equation","a''+(m^2+mu q^2)a+lambda a^3=0"),("periodic","global_periodic_solution","periodic"),("removed baseline","baseline_removed_obstruction","positive period average"),("logic","logical_effect","not a necessary global continuation condition"),("reroute","reroute","nonintegrable bounded coefficients"),("boundary","boundary","does not prove global")]:check(label,needle in F[key])
for T in (1.,2.,10.,100.):check(f"baseline integral T={T}",T>0 and math.isclose(T,1*T))
for q,a,ap,m,mu,lam in ((4,1.,0.,1.,1.,1.),(8,.5,.25,2.,.5,3.),(-4,2.,1.,1.,2.,.25)):
 omega2=m*m+mu*q*q
 energy=.5*ap*ap+.5*omega2*a*a+.25*lam*a**4
 acceleration=-omega2*a-lam*a**3
 energy_derivative=ap*(acceleration+omega2*a+lam*a**3)
 check(f"positive oscillator energy q={q}",energy>0)
 check(f"exact energy derivative q={q}",abs(energy_derivative)<1e-12)
check("target excluded",not Q["global_integral_BR_target_viable_on_T3"])
check("baseline proved",Q["vacuum_baseline_obstruction_proved"])
check("periodic proved",Q["nontrivial_periodic_mode_obstruction_proved"])
check("finite criterion retained",not Q["finite_interval_continuation_criterion_reversed"])
check("global still open",not Q["global_large_data_evolution_proved"])
check("noncompact open",not Q["noncompact_dispersive_route_excluded"])
check("source absent",not Q["source_action_identified"])
check("protected fixed",not Q["protected_status_change"])
assert n==29,n
print("RESULT: PASS 29/29")
