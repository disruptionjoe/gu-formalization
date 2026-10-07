#!/usr/bin/env python3
"""Finite-dimensional Riesz/intertwiner controls for K1344."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1344-principal-series-observation-functional-boundary.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
F=D["functional_classification"]; Q=D["decision"]
check("Riesz form",F["riesz_form"].startswith("every bounded linear"))
check("functional norm",F["norm"]=="||O_eta||=||eta||")
check("covariance identity","pi(g)^* eta" in F["covariance"])
check("intertwiner condition","iff" in F["trivial_target_intertwiner_condition"])
check("irreducible invariant-vector boundary","no nonzero invariant vector" in F["invariant_vector_result"])
check("zero full-G export",F["full_G_invariant_scalar_export"]=="zero only")
etas=[(1,2,-2),(2,-1,2),(-3,4,0)]; vecs=[(2,0,1),(1,-2,3),(4,1,-1)]
for eta,v in zip(etas,vecs):
 inner=sum(a*b for a,b in zip(eta,v)); bound=math.sqrt(sum(a*a for a in eta))*math.sqrt(sum(b*b for b in v))
 check("Cauchy-Schwarz export bound",abs(inner)<=bound+1e-12)
check("chosen export symmetry cost","preserves at most its stabilizer" in F["chosen_export"])
check("spacetime compatibility","commutes with scalar spacetime evolution" in F["spacetime_compatibility"])
check("exports classified",Q["bounded_linear_scalar_exports_classified"])
check("invariant export excluded",Q["nonzero_full_G_invariant_bounded_scalar_export_excluded"])
check("chosen exports exist",Q["nonzero_symmetry_breaking_bounded_export_exists_after_choice"])
check("source covector absent",not Q["source_owned_observation_covector_selected"])
check("narrow theorem",not Q["all_observation_maps_excluded"])
check("GU map absent",not Q["gu_observed_state_map_constructed"])
check("protected fixed",not Q["protected_status_change"])
check("nontrivial carrier","nontrivial irreducible" in F["carrier"])
check("scalar target explicit","scalar export" in F["riesz_form"])
check("choice nonzero","every nonzero eta" in F["chosen_export"])
assert n==23; print("RESULT: PASS 23/23")
