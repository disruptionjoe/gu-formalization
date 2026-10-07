#!/usr/bin/env python3
"""Data-mutation probe for K1373."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1373-closed-nonlinear-gauss-constraint.json").read_text())
def validate(x):
 c,e,q=x["constraint"],x["elliptic_reduction"],x["decision"];r=[]
 if "div E-e Im<Qphi,pi>" not in c["map"]:r.append("map")
 if "closed" not in c["closed_zero_set"]:r.append("closedness")
 if "H^-1_0" not in e["range"]:r.append("range")
 if "(-Delta)^-1" not in e["right_inverse"]:r.append("inverse")
 if "||E_T||^2+||R rho||^2" not in e["positive_energy"]:r.append("energy")
 if not q["constraint_surface_closed"]:r.append("decision")
 if not q["bounded_longitudinal_solve_constructed"]:r.append("solve")
 if q["nonlinear_KT_BV_BFV_properness_proved"]:r.append("properness overclaim")
 if q["global_solution_space_constructed"]:r.append("solution overclaim")
 if q["GU_physical_cohomology_constructed"]:r.append("cohomology overclaim")
 return r
assert not validate(D),validate(D)
mutations=[
 ("map",lambda x:x["constraint"].__setitem__("map","free div E")),
 ("closedness",lambda x:x["constraint"].__setitem__("closed_zero_set","unknown")),
 ("range",lambda x:x["elliptic_reduction"].__setitem__("range","all distributions")),
 ("inverse",lambda x:x["elliptic_reduction"].__setitem__("right_inverse","none")),
 ("energy",lambda x:x["elliptic_reduction"].__setitem__("positive_energy","indefinite")),
 ("decision",lambda x:x["decision"].__setitem__("constraint_surface_closed",False)),
 ("solve",lambda x:x["decision"].__setitem__("bounded_longitudinal_solve_constructed",False)),
 ("properness overclaim",lambda x:x["decision"].__setitem__("nonlinear_KT_BV_BFV_properness_proved",True)),
 ("solution overclaim",lambda x:x["decision"].__setitem__("global_solution_space_constructed",True)),
 ("cohomology overclaim",lambda x:x["decision"].__setitem__("GU_physical_cohomology_constructed",True))]
for i,(label,mutate) in enumerate(mutations,1):
 x=copy.deepcopy(D);mutate(x);errors=validate(x);assert errors,label;print(f"PASS {i:02d}: rejects {label} via [FAIL] {errors[0]}")
print("RESULT: PASS 10/10")
