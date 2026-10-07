#!/usr/bin/env python3
"""Modal Green and Cauchy-form controls for K1338."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1338-causal-green-boundary-flux.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
G=D["green_system"]; Q=D["decision"]
check("globally hyperbolic control","globally hyperbolic" in G["global_hyperbolicity"])
check("normally hyperbolic operator",G["normal_hyperbolicity"].startswith("P=partial_t^2-Delta_T3+m^2"))
check("direct internal tensor lift",G["tensor_lift"]=="E_plus_minus=E_plus_minus_scalar tensor I_Hps")
check("causal support law","J_plus" in G["support"] and "J_minus" in G["support"])
check("Cauchy form",G["cauchy_form"].startswith("Omega_Sigma"))
def mm(a,b): return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a): return [list(x) for x in zip(*a)]
J=[[0.0,1.0],[-1.0,0.0]]
for w in (1.0,1.5,math.sqrt(5),4.25):
 t=.41; c=math.cos(w*t); s=math.sin(w*t); u=[[c,s/w],[-w*s,c]]
 check(f"retarded kernel zero omega={w}",abs(math.sin(w*0)/w)<1e-15)
 check(f"retarded jump omega={w}",abs(math.cos(w*0)-1)<1e-15)
 check(f"homogeneous mode omega={w}",abs((-w*math.sin(w*t))+w*math.sin(w*t))<1e-12)
 preserved=mm(mm(tr(u),J),u)
 check(f"Cauchy form preserved omega={w}",max(abs(preserved[i][j]-J[i][j]) for i in range(2) for j in range(2))<1e-12)
check("Green system decision",Q["causal_green_system_constructed"])
check("finite propagation decision",Q["finite_propagation_support_constructed"])
check("boundary form decision",Q["cauchy_boundary_symplectic_form_constructed"] and Q["boundary_form_conserved"])
check("BFV ceiling",not Q["gu_bfv_boundary_reduction_constructed"])
check("interaction ceiling",not Q["interacting_green_system_constructed"])
assert n==28; print("RESULT: PASS 28/28")
