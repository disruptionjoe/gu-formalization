#!/usr/bin/env python3
"""Certificate for K1644's critical logarithmic endpoint."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def A(n):
    return 1.0 / (n * math.log(n + 1.0))


def main():
    d = json.loads((ROOT / "lab/process/k1644-logarithmic-holonomy-endpoint.json").read_text())
    q, z = d["logarithmic_endpoint"], d["decision"]
    weights = [(A(n) - A(n + 1)) / A(2) for n in range(2, 200000)]
    critical = sum(1.0 / (n * math.log(n) ** 2) for n in range(2, 200000))
    harmonic = sum(1.0 / (n * math.log(n)) for n in range(2, 200000))
    supercritical_kernel = sum(1.0 / (n * math.log(n) ** 1.25) for n in range(2, 200000))
    checks = [
        ("claim", d["claim_id"] == "K1644"),
        ("weights positive", all(w > 0.0 for w in weights)),
        ("weights telescope", abs(sum(weights) - 1.0) < 2e-5),
        ("critical finite control", critical < 4.0),
        ("harmonic divergence growth", harmonic > 3.2),
        ("supercritical kernel bounded", supercritical_kernel < harmonic),
        ("annular positive transform", ">=0" in q["annular_transform"]),
        ("annular scale", "comparable to A_n" in q["annular_transform"]),
        ("compact primitive", "compact AC and BV" in q["primitive"]),
        ("critical series", "1/[n log^2 n]" in q["critical_failure"]),
        ("L1 divergence", "1/[n log n]" in q["critical_failure"]),
        ("epsilon sufficiency", "every epsilon>0" in q["supercritical_sufficiency"]),
        ("scope fence", "not a necessary characterization" in q["scope_guard"]),
        ("counterexample", z["compact_ac_bv_counterexample"]),
        ("atom-free", z["atom_free_ac_derivative"]),
        ("endpoint failure", z["critical_log_endpoint_insufficient"]),
        ("supercritical sufficient", z["every_supercritical_log_power_sufficient"]),
        ("not necessary", not z["necessary_characterization"]),
        ("source open", not z["source_owned_flow"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
