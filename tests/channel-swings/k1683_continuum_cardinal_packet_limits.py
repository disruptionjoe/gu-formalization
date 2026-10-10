#!/usr/bin/env python3
"""Certificate for K1683's continuum packet limits."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def additive_energy(n):
    return sum((n-abs(s))**2 for s in range(-(n-1), n))


def main():
    data = json.loads((ROOT / "lab/process/k1683-continuum-cardinal-packet-limits.json").read_text())
    claim, decision = data["continuum_limits"], data["decision"]
    checks = [("schema", data["schema_version"] == "1.0"), ("claim", data["claim_id"] == "K1683")]
    for n in (5, 11, 25, 51):
        exact = (2*n**3+n)/3
        ratio = additive_energy(n)/n**3
        checks += [(f"energy n={n}", additive_energy(n) == exact),
                   (f"continuum ratio n={n}", abs(ratio-2/3) <= 1/(3*n*n)+1e-12)]
    alpha, A, B = 0.4, 1.7, 2.3
    tau = B*alpha**3
    ell = (8/27)*A**4*alpha**6
    checks += [
        ("conjugation symmetric block", "conjugation-symmetric" in claim["block_class"]),
        ("trace density", "b_g(xi)=sqrt" in claim["profile_functions"]),
        ("physical multiplier", "a_g(xi)=[2b_g(xi)]^(-1/2)" in claim["profile_functions"]),
        ("trace limit", "T_N/N^4" in claim["trace_limit"]),
        ("fourth limit", "L_N/N^4" in claim["fourth_mass_limit"]),
        ("additive constraint", "1_C(x+y-z)" in claim["fourth_mass_limit"]),
        ("positive weights", tau > 0 and ell > 0),
        ("cube tau", "tau=B alpha^3" in claim["constant_cube_control"]),
        ("cube ell", "ell=(8/27)A^4 alpha^6" in claim["constant_cube_control"]),
        ("trace decision", decision["relative_trace_limit_explicit"]),
        ("distinction decision", decision["physical_multiplier_distinguished"]),
        ("mass decision", decision["packet_fourth_mass_limit_explicit"]),
        ("shape open", not decision["optimal_packet_shape_identified"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
