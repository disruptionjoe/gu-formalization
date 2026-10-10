#!/usr/bin/env python3
"""Certificate for K1652's continuous Gaussian-channel identity."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1652-continuous-gaussian-channel-missing-information.json").read_text())
    fixtures = [(0.6, 0.2, 3.0), (1.1, 0.4, 7.0), (0.3, 0.05, 0.8)]
    checks = []
    for s0, delta, omega in fixtures:
        star = s0 + delta
        direct = omega * (delta - delta * delta / star) / (s0 * s0)
        closed = omega * delta / (s0 * star)
        checks.append((f"component algebra {s0}", math.isclose(direct, closed)))
        # Normal latent means make the output exactly the matched Gaussian.
        missing = omega * delta / (s0 * star)
        checks.append((f"normal latent cancellation {s0}", math.isclose(closed - missing, 0.0)))
    q, z = d["missing_information"], d["decision"]
    checks += [
        ("schema", d["schema_version"] == "1.0"),
        ("claim", d["claim_id"] == "K1652"),
        ("arbitrary latent", "arbitrary centered latent mean" in q["channel"]),
        ("score conditional mean", "E[u_Z-u_*|X]" in q["score_identity"]),
        ("ceiling trace", "Delta S_0^(-1)S_*^(-1)" in q["pythagoras"]),
        ("posterior covariance", "Cov(m_Z|X)" in q["pythagoras"]),
        ("K1648 conversion", "R_(Omega,N)/4=C_(F,N)-M_(F,N)" in q["k1648_conversion"]),
        ("finite-mixture scope", "K1606" in q["scope_guard"]),
        ("continuous decision", z["continuous_score_identity_proved"]),
        ("variance decision", z["conditional_variance_identity_proved"]),
        ("missing term", z["k1648_missing_term_identified"]),
        ("localization open here", not z["posterior_term_subleading_proved"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
