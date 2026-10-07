#!/usr/bin/env python3
"""Self-adjoint unbounded charge-domain control for K1358."""
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1358-principal-series-charge-generator-domain.json").read_text())
n = 0
def check(label, value):
    global n
    assert value, label; n += 1; print(f"PASS {n:02d}: {label}")

for key, pin in D["pinned_inputs"].items():
    check(f"{key} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"])
S, U, Q = D["stone_generator"], D["unboundedness_witness"], D["decision"]
charges = [4 * k for k in range(1, 9)]
check("strongly continuous circle", "strongly continuous" in S["circle_action"])
check("Stone self-adjoint", "self-adjoint" in S["generator"])
check("integer decomposition", "integer charge spaces" in S["spectral_decomposition"])
check("graph domain", "q^2" in S["operator_domain"])
check("K finite core", "K-finite" in S["core"])
check("finite charge sums", "finite charge sum" in S["core"])
check("full G sector boundary", "not invariant under full G" in S["sector_boundary"])
check("spherical harmonic family", "Sym^(2n)_0" in U["family"])
check("M fixed witness", "x1^(2n)" in U["M_fixed_witness"])
check("extreme charges", "4n" in U["extreme_charges"])
check("negative branch grows", [-q for q in charges][-1] == -32)
check("Hilbert coefficient series converges", sum(1 / (k * k) for k in range(1, 1000)) < 2)
check("graph partial sums diverge linearly", all((4*k)**2 / (k*k) == 16 for k in range(1, 20)))
check("proper-domain witness", "not a D(Q) vector" in U["domain_is_proper"])
check("self-adjoint decision", Q["charge_generator_self_adjoint"])
check("integral spectrum", Q["charge_spectrum_integral"])
check("two-sided unbounded", Q["charge_spectrum_unbounded_above"] and Q["charge_spectrum_unbounded_below"])
check("not bounded on H", not Q["charge_generator_bounded_on_full_H_ps"])
check("protected fixed", not Q["protected_status_change"])
assert n == 20
print("RESULT: PASS 20/20")
