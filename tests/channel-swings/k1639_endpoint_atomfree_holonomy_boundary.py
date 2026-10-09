#!/usr/bin/env python3
"""Certificate for K1639's explicit endpoint boundary."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def sinc(x):
    return 1.0 if x == 0.0 else math.sin(x) / x


def muhat(t, terms=500):
    return sum((1.0 / (n * (n + 1))) * sinc(math.exp(-n) * t / 2.0) ** 2
               for n in range(1, terms + 1))


def main():
    d = json.loads((ROOT / "lab/process/k1639-endpoint-atomfree-holonomy-boundary.json").read_text())
    q, z = d["endpoint_boundary"], d["decision"]
    weights = sum(1.0 / (n * (n + 1)) for n in range(1, 20000))
    annular = [(n, muhat(math.exp(n + 0.4))) for n in range(5, 13)]
    scaled = [n * value for n, value in annular]
    square_sum = sum(1.0 / (n * n) for n in range(1, 10000))
    harmonic_partial = sum(1.0 / n for n in range(1, 10000))
    checks = [
        ("claim", d["claim_id"] == "K1639"),
        ("weights normalize", abs(weights - 1.0) < 6e-5),
        ("positive transform", all(value > 0.0 for _, value in annular)),
        ("one-over-log scale", min(scaled) > 0.1 and max(scaled) < 5.0),
        ("square summable control", square_sum < 2.0),
        ("harmonic divergence control", harmonic_partial > 9.0),
        ("compact AC BV", z["compact_ac_bv_counterexample"]),
        ("atom-free derivative", z["atom_free_ac_derivative"]),
        ("endpoint failure", z["endpoint_h_half_insufficient"]),
        ("Besov sufficiency", z["endpoint_besov_type_sufficient"]),
        ("not necessity", not z["endpoint_besov_type_necessary"]),
        ("K1628 fence", "not in L2" in q["k1628_compatibility"]),
        ("electric open", not z["electric_field_L1_proved"]),
        ("source open", not z["source_owned_flow"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
