#!/usr/bin/env python3
"""Certificate for K1646's multidimensional Rudin--Shapiro flat block."""
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def shift(poly, v):
    return {tuple(a + b for a, b in zip(k, v)): c for k, c in poly.items()}


def add(a, b, sign=1):
    out = dict(a)
    for k, c in b.items():
        out[k] = out.get(k, 0) + sign * c
    return {k: c for k, c in out.items() if c}


def l4(poly):
    conv = defaultdict(int)
    items = list(poly.items())
    for k, a in items:
        for j, b in items:
            conv[tuple(x + y for x, y in zip(k, j))] += a * b
    return sum(v * v for v in conv.values())


def build(n):
    p = q = {(0, 0, 0): 1}
    lengths = [1, 1, 1]
    for step in range(n):
        axis = step % 3
        v = [0, 0, 0]
        v[axis] = lengths[axis]
        sq = shift(q, tuple(v))
        p, q = add(p, sq), add(p, sq, -1)
        lengths[axis] *= 2
    return p, q, lengths


def main():
    d = json.loads((ROOT / "lab/process/k1646-multidimensional-rudin-shapiro-flatness.json").read_text())
    q, z = d["flat_block"], d["decision"]
    p, r, lengths = build(6)
    size = len(p)
    total = l4(p) + l4(r)
    exact_t = Fraction(8 * size * size, 3) - Fraction(2 * size * size, 3) * Fraction(-1, 2) ** 6
    checks = [
        ("claim", d["claim_id"] == "K1646"),
        ("cube support", lengths == [4, 4, 4]),
        ("support size p", len(p) == 64),
        ("support size q", len(r) == 64),
        ("littlewood p", set(p.values()) <= {-1, 1}),
        ("littlewood q", set(r.values()) <= {-1, 1}),
        ("exact fourth recurrence solution", total == exact_t),
        ("selected ratio", min(l4(p), l4(r)) / size ** 2 <= 1.5),
        ("recursion recorded", "P_(n+1)" in q["recursion"]),
        ("support recorded", "complete" in q["support"]),
        ("complementarity recorded", "2d_n" in q["complementarity"]),
        ("recurrence recorded", "16d_n^2-2T_n" in q["fourth_recurrence"]),
        ("solution recorded", "8/3" in q["exact_solution"]),
        ("flatness recorded", "<=3/2" in q["selected_flatness"]),
        ("shell transfer", "fixed-ratio" in q["shell_transfer"]),
        ("cube decision", z["complete_macroscopic_cube_constructed"]),
        ("recurrence decision", z["exact_fourth_recurrence_proved"]),
        ("no independence", not z["probabilistic_independence_claimed"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
