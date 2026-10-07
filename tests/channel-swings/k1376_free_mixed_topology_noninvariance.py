#!/usr/bin/env python3
"""Exact modal controls for K1376's free-topology obstruction."""
import hashlib, json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1376-free-mixed-topology-noninvariance.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
F,Q=D["free_flow"],D["decision"]
check("free operator typed","Omega^2=-Delta" in F["equation"])
check("one-sided data typed","no Qpi_0" in F["k1372_phase_data"])
check("actual charge ladder","Qe_(4N)=4N" in F["mode"])
check("frequency exact","mu(4N)^2" in F["frequency"])
check("times tend to zero","t_N tends to zero" in F["test_time"])
check("output exact","(4N)^2/omega_N" in F["output"])
check("linear divergence stated","4N/sqrt(1+mu)" in F["divergence"])
m,mu=2.0,3.0
for N in (4,8,16,32):
 q=k=4*N;omega=math.sqrt(k*k+m*m+mu*q*q);t=math.pi/(2*omega);out=k*q/omega
 check(f"positive frequency N={N}",omega>0)
 check(f"shrinking test time N={N}",0<t<1/N)
 check(f"linear output lower N={N}",out/N>1.9)
check("initial topology bounded",Q["initial_k1372_topology_bounded"])
check("output unbounded",Q["free_output_k1372_norm_unbounded"])
check("strong continuity rejected",not Q["strong_continuity_on_one_sided_topology"])
check("momentum charge required",Q["momentum_charge_control_required_for_this_flow_space"])
check("nonlinear theorem absent",not Q["global_nonlinear_evolution_proved"])
check("source absent",not Q["source_action_identified"])
check("protected fixed",not Q["protected_status_change"])
assert n==28,n
print("RESULT: PASS 28/28")
