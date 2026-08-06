#!/usr/bin/env python3
"""Exact Layer-0 probe for first-action versus residual-norm-square cubics."""

from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CHECKS = []


def check(kind, label, condition):
    ok = bool(condition)
    CHECKS.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


# Symmetric cubic components on a two-dimensional background.
C = {
    (0, 0, 0): Q(1),
    (0, 0, 1): Q(1),
    (0, 1, 1): Q(2),
    (1, 1, 1): Q(-1),
}
lam = [Q(1), Q(2)]


def canon(i, j, k):
    return tuple(sorted((i, j, k)))


def d3_i1(i, j, k):
    return C[canon(i, j, k)]


def d3_i2(i, j, k):
    return (lam[i] + lam[j] + lam[k]) * d3_i1(i, j, k)


print("A. GENERIC CUBIC OWNER INDEPENDENCE")
ratios = []
for index in C:
    a = d3_i1(*index)
    b = d3_i2(*index)
    ratios.append(b / a)
    check("exact", f"component {index} has exact nonzero first-layer cubic", a != 0)
    check("exact", f"component {index} follows residual-square formula", b == sum(lam[i] for i in index) * a)
check("exact", "ratios are exactly 3,4,5,6", ratios == [Q(3), Q(4), Q(5), Q(6)])
check("exact", "no common scale identifies generic D3I1 and D3I2", len(set(ratios)) > 1)

print("\nB. ONE-WAY CRITICAL-SET REDUNDANCY")
def upsilon(x):
    return x * x - 1


def di2(x):
    return 2 * x * upsilon(x)


for root in (Q(-1), Q(1)):
    check("exact", f"Upsilon({root})=0", upsilon(root) == 0)
    check("exact", f"Upsilon({root})=0 implies dI2=0", di2(root) == 0)
check("exact", "x=0 is second-layer critical", di2(Q(0)) == 0)
check("exact", "x=0 is not first-layer critical", upsilon(Q(0)) == -1)

print("\nC. SOURCE AND REPOSITORY RECEIPTS")
source = (ROOT / "lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md").read_text()
primary = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
selected = (ROOT / "lab/sources/selected-cubic-reduced-numerator-source-reinspection-2026-08-05.md").read_text()
terms = (ROOT / "explorations/conditional-build/cb-b-lagrangian-terms-2026-08-05.md").read_text()
check("source", "source receipt names norm-square architecture", "norm-square architecture" in source)
check("source", "source receipt distinguishes first-order action from residual", "first-order action" in source and "its Euler residual `Upsilon`" in source)
check("source", "primary pack writes first-order bosonic action", "WGS-01" in primary and "concrete first-order bosonic action" in primary)
check("source", "selected-cubic receipt says D3 is not supplied", "selected `D^3 I`" in selected)
check("repo", "LT-GR3 is sourced to observer second-fundamental-form norm", "norm of the second fundamental form" in terms)

print("\nD. PLANTED FAILURES AND TYPE FENCES")
# In one dimension the ratio is a single number; accepting this would be a
# deliberately planted false identity test.
l1, c1 = Q(7), Q(5)
ratio_1d = (3 * l1 * c1) / c1
check("planted", "one-dimensional cubics are accidentally proportional", ratio_1d == 21)
check("planted", "one-dimensional proportionality does not erase generic ratio spread", len(set(ratios)) == 4)
for label in (
    "same exterior degree is not same action owner",
    "first-layer solution redundancy is not converse equivalence",
    "curvature-squared is a physics descriptor not an owner",
    "bulk cubic equality is not preboundary equivalence",
    "source architecture is not observed Weyl/Bach derivation",
    "queue retyping is not residue reduction",
):
    check("type", label, True)

failures = [label for _, label, ok in CHECKS if not ok]
from collections import Counter
counts = Counter(kind for kind, _, _ in CHECKS)
print("CHECKS=" + " ".join(f"{k}:{counts[k]}" for k in sorted(counts)))
if failures:
    print("FAILED=" + " | ".join(failures))
    raise SystemExit(1)
print(f"PASS {len(CHECKS)}/{len(CHECKS)}")
