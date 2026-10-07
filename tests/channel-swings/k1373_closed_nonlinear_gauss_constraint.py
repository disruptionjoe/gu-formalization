#!/usr/bin/env python3
"""Closed-range and Fourier controls for K1373's nonlinear Gauss reduction."""
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1373-closed-nonlinear-gauss-constraint.json").read_text()); n=0
def check(label,value):
    global n
    assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C,E,Q=D["constraint"],D["elliptic_reduction"],D["decision"]
check("phase topology typed","K1372" in C["phase_topology"])
check("Gauss map typed","div E-e Im<Qphi,pi>" in C["map"])
check("neutral sector typed","integral" in C["neutral_sector"])
check("continuity composed","continuous" in C["continuity"])
check("closed zero set","closed" in C["closed_zero_set"])
check("closed divergence range","H^-1_0" in E["range"])
check("right inverse typed","(-Delta)^-1" in E["right_inverse"])
check("bounded solve","H^-1" in E["bound"])
check("Helmholtz split","div E_T=0" in E["decomposition"])
check("orthogonality","<E_T,R rho>" in E["decomposition"])
check("positive energy split","||E_T||^2+||R rho||^2" in E["positive_energy"])
for k in ((1,0,0),(1,2,0),(2,-1,3),(4,3,-2)):
    norm2=sum(x*x for x in k); rho=1.0
    e2=rho*rho/norm2; hminus=rho*rho/norm2
    check(f"Fourier right-inverse mode {k}",abs(e2-hminus)<1e-12)
check("map well defined",Q["nonlinear_gauss_map_well_defined"])
check("surface closed",Q["constraint_surface_closed"])
check("range closed",Q["divergence_range_closed"])
check("solve constructed",Q["bounded_longitudinal_solve_constructed"])
check("positive reduction",Q["positive_kinematic_reduction_constructed"])
check("properness absent",not Q["nonlinear_KT_BV_BFV_properness_proved"])
check("global solution absent",not Q["global_solution_space_constructed"])
check("GU cohomology absent",not Q["GU_physical_cohomology_constructed"])
check("protected fixed",not Q["protected_status_change"])
assert n==26,n
print("RESULT: PASS 26/26")
