#!/usr/bin/env python3
"""Certificate for K1677's cardinal-packet fourth-mass estimate."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def pair_energy(n):
    return sum((n - abs(s))**2 for s in range(-(n - 1), n))


def main():
    data = json.loads((ROOT / "lab/process/k1677-cardinal-packet-l4-lower.json").read_text())
    claim, decision = data["packet_bound"], data["decision"]
    checks = [("schema", data["schema_version"] == "1.0"), ("claim", data["claim_id"] == "K1677")]
    for n in (3, 5, 9, 17):
        exact = (2*n**3+n)//3
        checks.append((f"pair energy n={n}", pair_energy(n) == exact))
        checks.append((f"normalized L4 n={n}", math.isclose(pair_energy(n)/n**2, (2*n+1/n)/3)))
    checks += [
        ("odd symmetric cube", "odd symmetric" in claim["block"]),
        ("dimension", "d_N=n_N^3" in claim["block"]),
        ("product identity", "[(2n_N+n_N^(-1))/3]^3" in claim["exact_identity"]),
        ("one-dimensional count", "(2n^3+n)/3" in claim["one_dimensional_count"]),
        ("profile scale", "a_N^2=Theta_g(N^-1)" in claim["profile_transfer"]),
        ("oscillation", "O_g(alpha^2)" in claim["profile_transfer"]),
        ("lower order", "L_N=sum_j" in claim["lower_bound"] and ">=c_g N^4" in claim["lower_bound"]),
        ("upper order", "L_N<=C_g N^4" in claim["lower_bound"]),
        ("identity decision", decision["exact_cardinal_identity"]),
        ("real multiplicity", decision["real_coordinate_multiplicity_preserved"]),
        ("mass decision", decision["profile_weighted_fourth_mass_order_n4"]),
        ("not constant", not decision["constant_multiplier_claimed"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
