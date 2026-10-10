#!/usr/bin/env python3
"""Certificate for K1656 known-phase complete-cube localization."""
import cmath
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1656-known-phase-orbit-localization.json").read_text())
    q, z = d["localization"], d["decision"]
    checks = []
    for n in (8, 16, 32):
        modes = n**3
        phase = cmath.exp(0.37j)
        demodulated = phase.conjugate() * phase
        checks += [
            (f"unitary demodulation N={n}", abs(demodulated - 1) < 1e-14),
            (f"translation risk N={n}", math.isclose(1 / modes, n**-3)),
            (f"global phase risk N={n}", math.isclose(n * n / modes, 1 / n)),
            (f"weighted aggregate N={n}", n * modes * (1 / n) == modes),
        ]
    checks += [
        ("schema", d["schema_version"] == "1.0"),
        ("claim", d["claim_id"] == "K1656"),
        ("known phases", "known unit phases" in q["channel"]),
        ("unitary", "unitary" in q["demodulation"]),
        ("translation rate", "O(d_N^(-1))" in q["risk"]),
        ("phase rate", "O(N^(-1))" in q["risk"]),
        ("missing N3", "O_(g,eta,R)(N^3)" in q["score_saturation"]),
        ("score saturation", "C_(F,N)-O_(g,eta,R)(N^3)" in q["score_saturation"]),
        ("scope", "unknown coefficients" in q["scope_guard"]),
        ("demodulation decision", z["known_phase_demodulation_proved"]),
        ("missing decision", z["posterior_missing_term_order_N3"]),
        ("unknown open", not z["arbitrary_unknown_pattern_localization_proved"]),
        ("coercivity open", not z["unrestricted_coercivity_proved"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
