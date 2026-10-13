#!/usr/bin/env python3
"""Exact rational producer for K1751's rectangular two-radius chart."""
import json
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1751-two-radius-rectangular-compactification.json"


def inverse(c, z):
    p = c / (c + z*z)
    a = 1-z
    b = 1+c/z
    return p, a, b, 2-c


def forward(p, a):
    b = (1-p*a)/(1-p)
    m4 = p*a*a+(1-p)*b*b
    return 3-m4, 1-a, b


def validate(data):
    checks = [("schema", data["schema_version"] == "1.0"),
              ("claim", data["claim_id"] == "K1751")]
    samples = [(Q(1,3), Q(1,4)), (Q(7,5), Q(2,3)), (Q(199,100), Q(1,100))]
    for i, (c,z) in enumerate(samples,1):
        p,a,b,u = inverse(c,z)
        u2,z2,b2 = forward(p,a)
        checks += [(f"p interior {i}", 0<p<1), (f"a interior {i}", 0<a<1),
                   (f"b outer {i}", b>1), (f"variance {i}", p*a+(1-p)*b == 1),
                   (f"m4 {i}", p*a*a+(1-p)*b*b == 1+c),
                   (f"u {i}", u == 2-c == u2), (f"z roundtrip {i}", z == z2),
                   (f"b roundtrip {i}", b == b2)]
    chart=data["chart"]; decision=data["decision"]
    checks += [("inverse serialized", "p=c/(c+z^2)" in chart["inverse"]),
               ("rectangle serialized", "(0,2-q)x(0,1)" in chart["bijection"]),
               ("exact decision", decision["exact_rectangular_chart_proved"]),
               ("not global", not decision["global_optimizer_proved"]),
               ("scope", "not a Fisher minimization" in data["scope_guard"])]
    return checks


def main():
    checks=validate(json.loads(ARTIFACT.read_text()))
    for i,(label,ok) in enumerate(checks,1): assert ok,label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
