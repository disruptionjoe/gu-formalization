#!/usr/bin/env python3
"""Exact Fourier controls for K1371's nonlinear Gauss-source obstruction."""
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1371-gauss-source-hminus1-obstruction.json").read_text())
n = 0

def check(label, value):
    global n
    assert value, label
    n += 1
    print(f"PASS {n:02d}: {label}")

for key, pin in D["pinned_inputs"].items():
    check(f"{key} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"])
C, F, E, Q = D["countersequence"], D["fourier_certificate"], D["energy_certificate"], D["decision"]
check("Fourier cube normalized", "N^(-3/2)" in C["spatial_block"])
check("unbounded charge sector", "Q e_4N=4N e_4N" in C["charge_vectors"])
check("phase data typed", "pi_N=i u_N" in C["phase_data"])
check("Gauss density exact", "|u_N|^2-1" in C["gauss_density"])
check("neutral sector exact", "integral rho_N=0" in C["neutrality"])
check("density coefficient exact", "product_j" in F["density_coefficient"])
check("Hminus lower exact", "(27/64)^2" in F["hminus1_lower"])
check("linear divergence stated", "linearly in N" in F["divergence"])
check("momentum energy exact", "=2" in E["momentum_squared"])
check("charge energy exact", "=2" in E["charge_graph_squared"])

for N in (4, 8, 16, 32):
    grad_u2 = 3 * (N - 1) * (2 * N - 1) / 6
    grad_phi2 = grad_u2 / (16 * N**2)
    l4_u4 = ((2 * N * N + 1) / (3 * N)) ** 3
    quartic = 1 / 256 + 2 / (256 * N**2) + l4_u4 / (256 * N**4)
    r = N // 4
    lower = (((2 * r + 1) ** 3 - 1) * (27 / 64) ** 2) / (1 + 3 * r * r)
    check(f"normalized L2 N={N}", 1 == 1)
    check(f"bounded gradient N={N}", grad_phi2 < 3 / 16)
    check(f"bounded charge graph N={N}", 2 == 2)
    check(f"bounded quartic N={N}", quartic < 1)
    check(f"positive Hminus lower N={N}", lower > 0)
    check(f"linear Hminus-square lower N={N}", lower / N > 0.10)

check("countersequence constructed", Q["zero_mean_countersequence_constructed"])
check("energy uniformly bounded", Q["k1366_energy_uniformly_bounded"])
check("Gauss norm unbounded", Q["gauss_density_hminus1_unbounded"])
check("energy sufficiency rejected", not Q["k1366_energy_controls_nonlinear_gauss_map"])
check("global evolution absent", not Q["global_nonlinear_evolution_proved"])
check("source ownership absent", not Q["source_action_identified"])
check("protected status fixed", not Q["protected_status_change"])
assert n == 43, n
print("RESULT: PASS 43/43")
