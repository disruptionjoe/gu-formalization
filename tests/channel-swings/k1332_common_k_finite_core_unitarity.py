#!/usr/bin/env python3
"""Domain and unitary-axis controls for K1332."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1332-common-k-finite-core-unitarity.json").read_text()); ncheck=0
def check(label,value):
 global ncheck; assert value,label; ncheck+=1; print(f"PASS {ncheck:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["common_domain"]; U=D["regular_imaginary_axis"]; Q=D["decision"]
check("compact Hilbert space",C["compact_picture_hilbert_space"]=="H=L2(K/M,dk)")
check("K-finite core",C["algebraic_core"]=="H_Kfin=C[K/M]_K-finite")
check("parameter independent",C["parameter_independent"])
check("dense",C["dense_in_H"])
check("simple preservation",C["preserved_by_every_simple_operator"])
def a(mode,z):
 out=1+0j
 for k in range(1,abs(mode)+1): out*=((2*k-1)-z)/((2*k-1)+z)
 return out
for t in (0.0,0.25,1.0,7.5):
 check(f"unit modulus t={t}",max(abs(abs(a(mode,1j*t))-1) for mode in range(25))<1e-12)
for t in (0.25,2.0,9.0):
 check(f"inverse t={t}",max(abs(a(mode,-1j*t)*a(mode,1j*t)-1) for mode in range(25))<1e-12)
check("zero identity",max(abs(a(mode,0)-1) for mode in range(25))<1e-12 and U["zero_parameter"].startswith("R_0=I"))
check("operator norm",U["operator_norm"]==1)
check("unitary extension","unique bounded unitary" in U["hilbert_extension"])
check("regular D7 consequence","all 42" in U["regular_charge_consequence"])
check("domain decision",Q["common_dense_compact_picture_core_constructed"] and Q["all_simple_operators_share_core"])
check("unitarity decision",Q["regular_imaginary_unitary_extension_constructed"] and not Q["regular_imaginary_operator_kernel_or_pole"])
check("physical ceiling",not Q["physical_domain_constructed"] and not Q["protected_status_change"])
assert ncheck==20; print("RESULT: PASS 20/20")
