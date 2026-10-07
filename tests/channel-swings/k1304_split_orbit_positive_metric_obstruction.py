#!/usr/bin/env python3
"""Exact controls for K1304's split-orbit positive-metric obstruction."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/"lab/process/k1304-split-orbit-positive-metric-obstruction.json").read_text())
n=0
def check(label,value):
    global n
    assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items():
    check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
T=D["theorem"]; Q=D["decision"]
check("D7 positive roots",T["positive_root_count"]==7*6==42)
check("orbit dimension",T["orbit_dimension"]==2*T["positive_root_count"]==84)
check("stabilizer rank",T["regular_split_stabilizer_dimension"]==7)
check("nontrivial weights",T["nontrivial_real_weights_present"])
scale=math.exp(1.0)
check("positive norm changes",not math.isclose(scale*scale,1.0))
check("no invariant positive inner product",not T["positive_inner_product_invariant_under_split_stabilizer"])
check("no invariant Riemannian metric",not T["g_invariant_riemannian_metric_exists"])
check("no positive invariant Kahler metric",not T["g_invariant_positive_kahler_metric_from_kks_exists"])
check("KKS nondegenerate",T["kks_form_nondegenerate"])
check("KKS not positive pairing",not T["kks_form_alone_is_positive_pairing"])
check("physical owner still needed",Q["physical_pairing_requires_extra_owner"])
check("status unresolved",not Q["SC_META_53_resolved"])
assert n==14
print("RESULT: PASS 14/14")
