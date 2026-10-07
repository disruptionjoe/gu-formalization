#!/usr/bin/env python3
"""Symmetry and normalization controls for K1368."""
import hashlib,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1368-regularizer-symmetry-normalization-boundary.json").read_text()); n=0
def check(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():
    check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
S,N,Q=D["symmetry_classification"],D["normalization_classification"],D["decision"]
check("invariance group typed","U*Q^2U=Q^2" in S["invariance_group"])
check("Schur test typed","Schur" in S["full_G_test"])
check("unbounded contradiction typed","unbounded" in S["contradiction"])
check("commutant price typed","Q-squared commutant" in S["symmetry_price"])
check("full G absent","not the full split group" in S["symmetry_price"])
for q,mu,c in ((1,2.0,3.0),(2,0.5,-2.0),(4,1.25,0.5),(7,0.2,5.0),(11,3.0,-4.0)):
    check(f"rescaling degeneracy q={q}",abs(mu*q*q-(mu/(c*c))*(c*q)**2)<1e-12)
for q in (0,2,4,12):
    check(f"sign degeneracy q={q}",q*q==(-q)*(-q))
check("rescaling prose","mu/c^2" in N["rescaling_degeneracy"])
check("sign prose","Q and -Q" in N["sign_degeneracy"])
check("selection limit prose","does not select" in N["selection_limit"])
check("classification decision",Q["exact_Q_squared_invariance_group_classified"])
check("circle decision",Q["selected_circle_preserved"])
check("full G decision",not Q["full_split_G_invariance"])
check("sign decision",not Q["charge_sign_selected"])
check("normalization decision",not Q["charge_normalization_selected"])
check("source/canonicity fixed",not Q["primitive_compact_generator_source_selected"] and not Q["regularizer_reduces_canonicity_distance"] and not Q["protected_status_change"])
assert n==25,n
print("RESULT: PASS 25/25")
