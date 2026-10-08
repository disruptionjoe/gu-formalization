#!/usr/bin/env python3
"""Controls for K1483's exact Wick third-moment triangle bound."""
import hashlib, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1483-wick-third-moment-triangle-bound.json").read_text())


def validate(d):
    a, q = d["third_moment_triangle"], d["decision"]
    return [
        d["schema_version"] == "1.0",
        d["claim_id"] == "K1483",
        "two edges between each pair" in a["unique_contraction_graph"],
        "(4!)^3/(2!)^3=1728" in a["contraction_count"],
        "1728 integral integral" in a["exact_formula"],
        "m3_N>=0" in a["positivity"],
        "||f_N||_1||f_N||_2^2" in a["young_bound"],
        "m3_N/sigma_N^2<=72 S_N" in a["ratio_bound"],
        "m3_N=O(N^6)" in a["three_dimensional_order"],
        q["unique_triangle_contraction_proved"],
        q["exact_contraction_coefficient"] == 1728,
        q["third_moment_nonnegative"],
        q["third_moment_order_upper"] == "N^6",
        q["third_moment_to_variance_ratio_order_upper"] == "N",
        not q["generic_hypercontractive_N_seven_halves_order_is_sharp"],
        not q["matching_third_moment_asymptotic_proved"],
        not q["protected_status_change"],
    ]


def main():
    checks = []
    for name, pin in D["pinned_inputs"].items():
        checks.append((f"{name} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]))
    checks.extend((f"serialized invariant {i}", ok) for i, ok in enumerate(validate(D), 1))
    contraction_count = math.factorial(4) ** 3 // math.factorial(2) ** 3
    checks.append(("labeled triangle contraction count", contraction_count == 1728))
    c = [1.0, 0.5, -0.25, 0.125, -0.0625]
    f = [x * x for x in c]
    size = len(f)
    conv = [sum(f[y] * f[(x - y) % size] for y in range(size)) / size for x in range(size)]
    triangle = sum(conv[x] * f[x] for x in range(size)) / size
    norm1 = sum(f) / size
    norm2sq = sum(x * x for x in f) / size
    sigma2 = 24 * norm2sq
    m3 = 1728 * triangle
    checks.extend([
        ("toy triangle is nonnegative", triangle >= 0),
        ("Young convolution bound", triangle <= norm1 * norm2sq + 1e-14),
        ("exact ratio bound", m3 / sigma2 <= 72 * norm1 + 1e-12),
        ("N6 over N5 leaves N", all((n ** 6) / (n ** 5) == n for n in (2, 4, 8, 16))),
    ])
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
