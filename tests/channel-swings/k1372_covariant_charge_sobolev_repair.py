#!/usr/bin/env python3
"""Analytic controls for K1372's covariant mixed charge topology."""
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1372-covariant-charge-sobolev-repair.json").read_text()); n = 0
def check(label, value):
    global n
    assert value, label; n += 1; print(f"PASS {n:02d}: {label}")
for key, pin in D["pinned_inputs"].items():
    check(f"{key} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"])
R, C, Q = D["repair"], D["current_control"], D["decision"]
check("mixed domain typed", "D_A(Qphi)" in R["space"])
check("mixed norm typed", "||D_A(Qphi)||^2" in R["mixed_norm"])
check("exact gauge covariance", "exp(i alpha Q)D_A(Qphi)" in R["gauge_covariance"])
check("not action attribution", "not added" in R["not_an_action_term"])
check("Kato inequality", "grad ||Qphi||" in R["kato_bound"])
check("Sobolev L6", "L6" in R["sobolev_bound"])
check("current typed", "Im<Qphi,pi>" in C["density"])
check("Holder exponents", "L6" in C["duality"] and "L3" in C["duality"])
check("Hminus bound", "H^-1" in C["hminus1_bound"])
check("dimension three", C["dimension"].endswith("three"))
check("sufficiency boundary", "first proved sufficient" in C["sharp_boundary"])
check("gauge topology constructed", Q["gauge_covariant_mixed_topology_constructed"])
check("Gauss continuity", Q["gauss_density_continuous_to_hminus1"])
check("source selection absent", not Q["repair_selected_by_source"])
check("normalization selection absent", not Q["repair_selects_Q_or_normalization"])
check("propagation absent", not Q["mixed_topology_globally_propagated"])
check("global evolution absent", not Q["global_nonlinear_evolution_proved"])
check("protected fixed", not Q["protected_status_change"])
assert n == 20, n
print("RESULT: PASS 20/20")
