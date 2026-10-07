#!/usr/bin/env python3
"""ODE and scope controls for K1389's local continuation estimate."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1389-local-high-regularity-continuation.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
L,Q=D["local_continuation"],D["decision"]
for label,key,needle in [
 ("gauge","gauge_and_model","Lorenz gauge"),
 ("control norm","control_norm","triangular matter energy"),
 ("low coefficient","low_coefficient","||Qphi||_infinity"),
 ("tame inequality","tame_inequality","B_R<=C_R(1+Y_R)^2"),
 ("closed ODE","closed_ode","dY_R/dt<=C_R(1+Y_R)^2 Y_R"),
 ("local bound","local_bound","log(2)/(C_R(1+2Y_0)^2)"),
 ("criterion","continuation_criterion","integral B_R dt"),
 ("global boundary","global_boundary","does not prove global")]:check(label,needle in L[key])
for y0,C in ((.1,.5),(.5,1.0),(1.0,2.0),(3.0,.25)):
 T=math.log(2)/(C*(1+2*y0)**2)
 upper=y0*math.exp(C*(1+2*y0)**2*T)
 check(f"positive lifespan y0={y0}",T>0)
 check(f"bootstrap closes y0={y0}",math.isclose(upper,2*y0,rel_tol=1e-12))
check("local inequality",Q["closed_local_apriori_inequality_constructed"])
check("explicit bound",Q["explicit_local_bound_constructed"])
check("topology locally controlled",Q["finite_triangular_phase_topology_locally_controlled"])
check("existence not claimed",not Q["smooth_solution_existence_constructed"])
check("global not claimed",not Q["global_large_data_bound_constructed"])
check("BV-BFV open",not Q["closed_nonlinear_BV_BFV_quotient_constructed"])
check("source absent",not Q["source_action_identified"])
check("protected fixed",not Q["protected_status_change"])
assert n==26,n
print("RESULT: PASS 26/26")
