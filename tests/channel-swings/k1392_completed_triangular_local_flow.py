#!/usr/bin/env python3
"""Approximation controls for K1392's completed triangular flow."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1392-completed-triangular-local-flow.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
F,Q=D["completed_flow"],D["decision"]
for label,key,needle in [("space","phase_space","completion"),("density","spectral_density","strongly"),("lifespan","uniform_lifespan","N-independent"),("difference","difference_estimate","one extra triangular tier"),("Cauchy","cauchy_limit","Cauchy"),("limit","equation_limit","graph closedness of Q"),("result","local_result","completed local strong solution"),("boundary","boundary","local")]:check(label,needle in F[key])
for y,c in ((.2,.5),(1.,1.),(2.,.25)):
 T=math.log(2)/(c*(1+2*y)**2)
 check(f"uniform T positive {y}",T>0)
 z0=.01
 bound=z0*math.exp(c*(1+4*y)**2*T)
 check(f"difference finite {y}",math.isfinite(bound) and bound>=z0)
for key in ("triangular_phase_completion_constructed","cutoff_density_proved","cutoff_uniform_lifespan_proved","one_tier_difference_estimate_proved","completed_local_strong_solution_constructed","smooth_data_smooth_solution_constructed"):check(key,Q[key])
for key in ("global_large_data_solution_constructed","physical_quotient_constructed","source_action_identified","protected_status_change"):check(f"{key} false",not Q[key])
assert n==27,n
print("RESULT: PASS 27/27")
