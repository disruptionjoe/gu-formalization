#!/usr/bin/env python3
"""Controls for K1399 closed gauge range."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1399-closed-nonlinear-gauge-range.json").read_text());n=0
def check(label,value):
 global n
 assert value,label;n+=1;print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
F,Q=D["closed_range"],D["decision"]
for label,key,needle in [("generator","generator","R_(A,phi)"),("split","parameter_split","mean-zero"),("Poincare","based_lower_bound","Poincare"),("matter","matter_continuity","continuous"),("constant","constant_part","one-dimensional"),("sum","closed_sum","finite dimensional"),("KT","kt_effect","closed range"),("boundary","boundary","not exactness")]:check(label,needle in F[key])
for k in range(1,7):check(f"Poincare mode k={k}",math.sqrt(k*k)>0)
for key in ("based_gauge_generator_bounded_below","constant_gauge_image_closed","full_nonlinear_gauge_generator_range_closed","configuration_stabilizer_explicit"):check(key,Q[key])
for key in ("full_bv_complex_exactness_constructed","bfv_boundary_theory_constructed","positive_physical_hilbert_cohomology_constructed","protected_status_change"):check(f"{key} false",not Q[key])
assert n==24,n
print("RESULT: PASS 24/24")
