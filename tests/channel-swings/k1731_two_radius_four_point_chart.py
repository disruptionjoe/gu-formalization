#!/usr/bin/env python3
"""Exact-chart and numerical algebra controls for K1731."""
import json
from pathlib import Path
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parents[2]


def chart(p, a):
    b = (1 - p * a) / (1 - p)
    m2 = p * a**2 + (1 - p) * b**2
    m3 = p * a**3 + (1 - p) * b**3
    m4 = p * a**4 + (1 - p) * b**4
    return b, 3 - m2, m3 - 15 * m2 + 30, m4 - 28 * m3 + 210 * m2 - 315


def main():
    d = json.loads((ROOT / "lab/process/k1731-two-radius-four-point-chart.json").read_text())
    u0 = brentq(lambda u: 17*u**3 - 38*u**2 + 84*u - 24, 0, 1)
    s = 2 * (6 - 7*u0) / (2 - u0); r = s - (3 - u0)
    a0 = (s - (s*s - 4*r)**0.5) / 2; b0 = (s + (s*s - 4*r)**0.5) / 2
    p0 = (b0 - 1) / (b0 - a0); b, u, k6, h8 = chart(p0, a0)
    checks = [
        ("schema", d["schema_version"] == "1.0"), ("claim", d["claim_id"] == "K1731"),
        ("root", 0 < u0 < 1), ("a order", 0 < a0 < 1), ("b order", b0 > 1),
        ("p order", 0 < p0 < 1), ("b chart", abs(b-b0) < 2e-14),
        ("variance", abs(p0*a0+(1-p0)*b0-1) < 2e-14),
        ("u", abs(u-u0) < 2e-13), ("k6", abs(k6) < 3e-13),
        ("h8", abs(h8-35*u0*u0) < 2e-12),
        ("p value", abs(p0-0.842798253731782) < 2e-15),
        ("a value", abs(a0-0.441384393880459) < 2e-15),
        ("b value", abs(b0-3.994879309683925) < 5e-15),
        ("parameters", "0<p<1" in d["chart"]["parameters"]),
        ("moment law", "p a^r" in d["chart"]["even_moments"]),
        ("complete", "Every symmetric four-point" in d["chart"]["completeness"]),
        ("scope symmetric", "symmetric" in d["scope_guard"]),
        ("scope continuous", "continuous" in d["scope_guard"]),
        ("scope field", "field-valued" in d["scope_guard"]),
    ]
    for p, a in ((0.4, 0.2), (0.7, 0.5), (0.9, 0.8)):
        bb, *_ = chart(p, a); checks.append((f"sample variance {p}", abs(p*a+(1-p)*bb-1) < 1e-14))
    for i, (label, ok) in enumerate(checks, 1): assert ok, label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
