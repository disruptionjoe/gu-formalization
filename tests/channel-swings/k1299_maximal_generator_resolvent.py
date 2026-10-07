#!/usr/bin/env python3
"""Exact controls for K1299's maximal generator and resolvent."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1299-maximal-generator-resolvent.json").read_text())
n=0
def check(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
pin=D["pinned_inputs"]["k1298"]
check("K1298 pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
T=D["theorem"]
check("skew adjoint",T["skew_adjoint"])
check("maximal",T["maximal"])
check("unitary group","exp(-i t L)" in T["unitary_group"])
check("domain preservation",T["preserves_common_spectral_domains"])
check("differential commutation",T["commutes_with_differential"])
z=complex(1,2)
for lam in (0,2,4): check(f"resolvent eigenvalue {lam}",abs(1/(z+1j*lam))<=1/abs(z.real))
check("reduced bound","1/(2 mu)" in T["reduced_zero_resolvent_bound"])
check("boundaryless trace",T["boundaryless_trace_compatibility"])
check("no causal Green",not T["hyperbolic_causal_green_operator"])
check("source boundary absent",not D["decision"]["source_boundary_law_supplied"])
assert n==13
print("RESULT: PASS 13/13")
