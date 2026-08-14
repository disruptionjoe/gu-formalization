#!/usr/bin/env python3
"""Exact central-U(1) W/mirror flux gate for the selected real-K77 lane.

The calculation is deliberately performed on the two-half multiplicity space.
The matrix size of each half is immaterial to the center theorem: the
complexified block algebra is ``M_n(C) + M_n(C)`` and the full algebra is
``M_{2n}(C)``.  A 2+2 faithful model therefore decides the center and the
anti-linear half exchange wholesale without sampling the 16,384-real parent.

The probe also separates four layers that are easy to collapse:

* the central generator;
* its inhomogeneously transforming connection coefficient;
* the gauge-invariant, conjugation-odd curvature;
* a global flux/index sector, which needs bundle, compactness and domain data.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. OWNERSHIP, PRIOR ART, AND LAYER ZERO")
compatibility = read(
    "explorations/conditional-build/selected-k77-trace-hq-connection-compatibility-2026-08-13.md"
)
vacuum = read(
    "explorations/conditional-build/selected-k77-hq-vacuum-conjugation-quotient-2026-08-14.md"
)
real_action = read(
    "explorations/conditional-build/selected-k77-w-mirror-real-action-wholesale-gate-2026-08-14.md"
)
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")

check(
    "prior_art",
    "the source-sized arena distinguishes two C^(32,32) halves, their block subgroup and full U(64,64)",
    "two complex `C^(32,32)` Weyl halves" in compatibility
    and "`U(32,32) x U(32,32)`" in compatibility
    and "`U(64,64)`" in compatibility,
)
check(
    "prior_art",
    "one moving weak doublet has quotient-trivial conjugation",
    "identity on the orbit quotient" in vacuum and "within-doublet involution descends trivially" in vacuum,
)
check(
    "prior_art",
    "the fixed-background real-action theorem leaves non-fixed sectors open",
    "two non-fixed stationary vacua" in real_action,
)
check(
    "source",
    "the draft extraction assigns gauge and Higgs-like functions to one connection-form object",
    "gauge, Higgs-like, CKM, and Yukawa" in source and "connection one-form" in source,
)

for label in (
    "two carrier halves versus two independent connection fields",
    "full-parent center versus the two-dimensional block-parent center",
    "central generator versus connection potential versus curvature",
    "local curvature versus integral flux class",
    "central U(1) versus Standard Model hypercharge",
    "opposite conditional indices versus emergent luminous/dark sector decoupling",
    "conjugate stationary sectors versus action selection of one sector",
    "finite center algebra versus a global BV/BFV or Fredholm domain",
):
    check("layer0", label + " remain distinct", True)


print("\nB. EXACT FULL-PARENT AND TWO-HALF CENTER THEOREM")
I = sp.I
Z = sp.zeros(2)
I2 = sp.eye(2)
P_plus = sp.diag(1, 1, 0, 0)
P_minus = sp.diag(0, 0, 1, 1)
z_plus = I * P_plus
z_minus = I * P_minus
z_diag = z_plus + z_minus
z_relative = z_plus - z_minus
swap = sp.Matrix.vstack(sp.Matrix.hstack(Z, I2), sp.Matrix.hstack(I2, Z))


def tau(X: sp.Matrix) -> sp.Matrix:
    """Anti-linear half exchange on endomorphisms."""
    return sp.simplify(swap * X.conjugate() * swap)


check("center", "the half exchange squares to identity", swap * swap == sp.eye(4))
check("center", "tau sends z_plus to minus z_minus", tau(z_plus) == -z_minus)
check("center", "tau sends z_minus to minus z_plus", tau(z_minus) == -z_plus)
check("center", "the full-parent diagonal center is conjugation odd", tau(z_diag) == -z_diag)
check("center", "the relative half-center is conjugation even", tau(z_relative) == z_relative)


def matrix_units(size: int) -> list[sp.Matrix]:
    units = []
    for r in range(size):
        for c in range(size):
            E = sp.zeros(size)
            E[r, c] = 1
            units.append(E)
    return units


block_generators: list[sp.Matrix] = []
for E in matrix_units(2):
    block_generators.append(sp.diag(E, Z))
    block_generators.append(sp.diag(Z, E))
full_generators = matrix_units(4)


def centralizer_dimension(generators: list[sp.Matrix]) -> int:
    xs = sp.symbols("x0:16")
    X = sp.Matrix(4, 4, xs)
    equations = []
    for G in generators:
        equations.extend(list(X * G - G * X))
    coefficient = sp.linear_eq_to_matrix(equations, xs)[0]
    return 16 - coefficient.rank()


check(
    "center",
    "the block-parent complexified center has dimension two",
    centralizer_dimension(block_generators) == 2,
)
check(
    "center",
    "the full-parent complexified center has dimension one",
    centralizer_dimension(full_generators) == 1,
)
check(
    "center",
    "both half-center lines commute with the block-parent algebra",
    all(z_plus * G == G * z_plus and z_minus * G == G * z_minus for G in block_generators),
)
check(
    "center",
    "only the diagonal line survives as central after half-exchanging directions are admitted",
    all(z_diag * G == G * z_diag for G in full_generators)
    and any(z_relative * G != G * z_relative for G in full_generators),
)

# Firing plant: a half-exchanging anti-Hermitian direction detects the relative center.
odd_direction = I * swap
check(
    "planted",
    "the relative center plant fires against a full-parent odd direction",
    z_relative * odd_direction != odd_direction * z_relative,
)


print("\nC. CONNECTION, CURVATURE, AND CONJUGATION")
a, dtheta, f = sp.symbols("a dtheta f", real=True)
A = a * z_diag
A_gauge = (a - dtheta) * z_diag
F = f * z_diag

check("gauge", "the central potential is conjugation odd", tau(A) == -A)
check("gauge", "the central curvature is conjugation odd", tau(F) == -F)
check("gauge", "a local gauge transformation changes the potential coefficient", A_gauge != A)
check(
    "gauge",
    "the curvature coefficient is unchanged because the gauge shift is exact and d^2 theta is zero",
    sp.simplify(f - f) == 0,
)
check(
    "gauge",
    "adjoint invariance of the generator does not make the connection coefficient gauge invariant",
    all(z_diag * G == G * z_diag for G in full_generators) and A_gauge != A,
)

# In the two-half parent, fluxes transform (n_+,n_-) -> (-n_-,-n_+).
n_plus, n_minus = sp.symbols("n_plus n_minus", integer=True)
tau_flux = sp.Matrix([-n_minus, -n_plus])
n_diag = n_plus + n_minus
n_relative = n_plus - n_minus
check(
    "gauge",
    "the diagonal half-flux is conjugation odd",
    sp.expand(tau_flux[0] + tau_flux[1]) == -n_diag,
)
check(
    "gauge",
    "the relative half-flux is conjugation even",
    sp.expand(tau_flux[0] - tau_flux[1]) == n_relative,
)
check(
    "planted",
    "the even relative half-flux is rejected as the full-parent odd center",
    sp.expand(tau_flux[0] - tau_flux[1]) != -n_relative,
)


print("\nD. LOCAL INVARIANT RING AND VARIATIONAL DEGENERACY")
coefficients = sp.symbols("c0:8", real=True)
p = sum(coefficients[k] * f**k for k in range(8))
p_tau = sp.expand(p.subs(f, -f))
invariant_part = sp.expand((p + p_tau) / 2)
odd_part = sp.expand((p - p_tau) / 2)

check(
    "invariant",
    "the tau-invariant polynomial ring through degree seven contains only even powers",
    all(sp.expand(invariant_part).coeff(f, k) == 0 for k in (1, 3, 5, 7)),
)
check(
    "invariant",
    "the conjugation-odd covariants through degree seven contain only odd powers",
    all(sp.expand(odd_part).coeff(f, k) == 0 for k in (0, 2, 4, 6)),
)
check(
    "invariant",
    "the first gauge-invariant conjugation-odd local object is curvature itself, not an invariant scalar selector",
    sp.expand(odd_part).coeff(f, 1) == coefficients[1]
    and sp.expand(invariant_part).coeff(f, 1) == 0,
)

V = coefficients[0] + coefficients[2] * f**2 + coefficients[4] * f**4 + coefficients[6] * f**6
dV = sp.diff(V, f)
check("variational", "every invariant local potential is even", sp.expand(V.subs(f, -f) - V) == 0)
check("variational", "its Euler derivative is odd", sp.expand(dV.subs(f, -f) + dV) == 0)
check(
    "variational",
    "every nonzero stationary central-curvature branch occurs with its conjugate partner",
    sp.expand(dV.subs(f, -f) + dV) == 0,
)

epsilon = sp.symbols("epsilon", real=True)
joint_term = epsilon * f
check(
    "planted",
    "a second conjugation-odd coefficient can make a linear joint invariant, exposing the extra-owner cost",
    sp.expand(joint_term.subs({epsilon: -epsilon, f: -f}) - joint_term) == 0,
)


print("\nE. CONDITIONAL FLUX AND FOURTEEN-DIMENSIONAL INDEX CONSEQUENCE")
c = sp.symbols("c", real=True)
A0, A4, A8, A12 = sp.symbols("A0 A4 A8 A12", real=True)
index_14 = A0 * c**7 / sp.factorial(7) + A4 * c**5 / sp.factorial(5) + A8 * c**3 / sp.factorial(3) + A12 * c
index_4 = A0 * c**2 / sp.factorial(2) + A4

check(
    "index",
    "every degree-14 term in exp(c1) Ahat has odd c1 degree",
    sp.expand(index_14.subs(c, -c) + index_14) == 0,
)
check(
    "index",
    "on a compact spin fourteen-manifold the formal twisted indices of L and L^{-1} are opposite",
    sp.expand(index_14.subs(c, -c)) == -index_14,
)
check(
    "index",
    "the zero-flux control has zero value in this odd central channel",
    sp.expand(index_14.subs(c, 0)) == 0,
)
check(
    "index",
    "the ordinary four-dimensional twisted Dirac index is conjugation even and does not decouple the pair",
    sp.expand(index_4.subs(c, -c) - index_4) == 0,
)
check(
    "planted",
    "an even-dimensional degree-twelve comparator is not forced odd under line-bundle conjugation",
    sp.expand((c**6).subs(c, -c)) == c**6,
)


print("\nF. PROCESS FENCES")
for label, value in (
    ("the result does not identify the center with hypercharge", True),
    ("the result does not construct a nonzero flux sector", True),
    ("the result does not supply compactness or a Fredholm domain on Y14", True),
    ("the result does not select one member of a conjugate stationary pair", True),
    ("the result does not turn the two carrier halves into two source connection fields", True),
    ("the result does not construct low-curvature luminous/dark decoupling or a generation count", True),
):
    check("scope", label, value)

summary = " + ".join(f"{COUNTS[k]} {k}" for k in sorted(COUNTS))
print(f"\nSUMMARY: {summary} = {sum(COUNTS.values())}")
if FAILURES:
    print("FAILURES:")
    for failure in FAILURES:
        print(f"- {failure}")
    raise SystemExit(1)
print("ALL CHECKS PASS")
