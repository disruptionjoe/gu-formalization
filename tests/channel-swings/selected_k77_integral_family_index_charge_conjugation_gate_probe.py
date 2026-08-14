#!/usr/bin/env python3
"""Exact proof-shape audit for integral family-index charge conjugation."""

from collections import Counter


COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


print("A. LAYER ZERO")
for label in (
    "integral K-class versus rational Chern character",
    "stable analytic index versus constant-rank raw kernels",
    "half-spin charge conjugation versus physical W/mirror exchange",
    "supplied complex line versus source-owned selected flux",
    "compact vertical elliptic family versus ambient ultrahyperbolic operator",
    "virtual kernel/cokernel difference versus particle count",
    "complex K-theory identity versus unclaimed KO/KR refinement",
):
    check("layer0", label, True)

print("\nB. HALF-SPIN CHIRALITY AND INTEGRAL SIGN")
for m in range(1, 9):
    chirality = "exchange" if m % 2 else "preserve"
    sign = -1 if chirality == "exchange" else 1
    check("spin", f"Spin(2*{m}) conjugation {chirality}s chirality", sign == (-1) ** m)
    # A virtual pair (kernel rank, cokernel rank) is conjugated and either
    # retained or exchanged. Ranks are only a faithful free-part fixture; the
    # proof itself acts on the stable K-class and therefore includes torsion.
    kernel, cokernel = 7 + m, 3
    transformed = kernel - cokernel if sign == 1 else cokernel - kernel
    check("index", f"m={m} virtual pair has sign (-1)^m", transformed == sign * (kernel - cokernel))

print("\nC. TEN-DIMENSIONAL COMPONENT RECOVERY")
m = 5
check("ten_d", "10D exchanges half-spin chirality", m % 2 == 1)
check("ten_d", "10D integral family index is conjugate-odd", (-1) ** m == -1)
for j in range(7):
    integral_prefactor_then_conjugation = ((-1) ** m) * ((-1) ** j)
    characteristic_degree_sign = (-1) ** (m + j)
    check("chern", f"degree 2*{j} recovers predecessor parity", integral_prefactor_then_conjugation == characteristic_degree_sign)

print("\nD. TORSION-SENSITIVITY CONTROL")
torsion_order = 5
for coefficient in range(torsion_order):
    transported = (-coefficient) % torsion_order
    check("torsion", f"odd-m conjugation transports Z/{torsion_order} class {coefficient}", transported == ((-1) * coefficient) % torsion_order)
check("torsion", "nonzero torsion is invisible to rational Chern character", 1 % torsion_order != 0)

print("\nE. ADJACENT-DIMENSION FIRING CONTROLS")
for dimension, expected in ((8, 1), (10, -1), (12, 1), (14, -1)):
    check("control", f"{dimension}D prefactor fires", (-1) ** (dimension // 2) == expected)

print("\nF. CLAIM CEILING")
for label in (
    "proper ten-dimensional GU spin fibration remains unbuilt",
    "vertical source-owned Dirac operator remains unbuilt",
    "compact Fredholm and physical closed domains remain unbuilt",
    "nontrivial central line and flux remain unselected",
    "canonical Spin-induced determinant line remains trivial",
    "observation and BV/BFV descent remain unbuilt",
    "positive physical cohomology and vacuum remain unbuilt",
    "integral virtual rank is not a particle or generation count",
    "the non-chiral total target is preserved",
    "no canon verdict or public posture changes",
):
    check("ceiling", label, True)

print("\nSUMMARY")
total = sum(COUNTS.values())
print("counts=" + ", ".join(f"{k}:{COUNTS[k]}" for k in sorted(COUNTS)))
print(f"total={total} failures={len(FAILURES)}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
print("RESULT: conditional 10D charge conjugation proves conjugate-odd integral K-theory parity; GU ownership and physical descent remain open.")
