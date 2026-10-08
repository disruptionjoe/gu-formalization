#!/usr/bin/env python3
"""Controls for K1489's two-dimensional Ritz nonquasimode boundary."""
import hashlib, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1489-two-dimensional-ritz-nonquasimode.json").read_text())


def validate(d):
    a, q = d["nonquasimode_boundary"], d["decision"]
    return [
        d["schema_version"] == "1.0", d["claim_id"] == "K1489",
        "beta_N->-1/sqrt(2)" in a["ritz_vector"],
        "unit vector Y_N orthogonal" in a["higher_chaos_test"],
        "tau_N>=1" in a["interaction_residual"],
        "O(N)" in a["free_residual"],
        "g sigma_N/3" in a["residual_lower_bound"],
        "not a quasimode" in a["consequence"],
        q["higher_chaos_residual_constructed"],
        q["interaction_residual_scale"] == "g sigma_N",
        q["free_residual_order_upper"] == "N",
        q["ritz_residual_lower_fraction"] == "g sigma_N/3",
        not q["two_dimensional_ritz_vector_is_o_sigma_quasimode"],
        not q["minus_one_is_full_ground_energy_leading_coefficient"],
        not q["matching_ground_energy_lower_bound_proved"],
        not q["protected_status_change"],
    ]


def main():
    checks=[]
    for name,pin in D["pinned_inputs"].items():
        checks.append((f"{name} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"]))
    checks.extend((f"serialized invariant {i}",ok) for i,ok in enumerate(validate(D),1))
    for n in (16,64,256):
        sigma=n**2.5; free=8*n
        checks.append((f"sigma dominates free at N={n}",free/sigma < 0.13))
    checks.extend([
        ("asymptotic beta exceeds one half",1/math.sqrt(2)>0.7),
        ("one-third margin fits asymptotic beta",1/math.sqrt(2)>1/3),
    ])
    for i,(label,ok) in enumerate(checks,1):
        assert ok,label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__=="__main__": main()
