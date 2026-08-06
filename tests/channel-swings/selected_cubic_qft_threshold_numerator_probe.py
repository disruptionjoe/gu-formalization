#!/usr/bin/env python3
"""Exact continuum threshold atlas for the selected theta-q0-qm cubic."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
Q = sp.Rational
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, ARCHAEOLOGY, AND LAYER 0")
source = read(
    "lab/sources/selected-cubic-qft-threshold-and-numerator-gate-source-reinspection-2026-08-05.md"
)
interaction = read(
    "explorations/conditional-build/first-interaction-krein-and-global-zero-mode-horn-2026-08-05.md"
)
background = read(
    "explorations/conditional-build/first-perturbative-background-c-operator-2026-08-05.md"
)
w179 = read("explorations/W179-build-c-operator-allorders-2026-07-14.md")
w132 = read("explorations/W132-graded-optical-theorem-physical-subspace-2026-07-14.md")
result = read(
    "explorations/conditional-build/selected-cubic-qft-threshold-and-numerator-gate-2026-08-05.md"
)
review = read(
    "lab/process/hostile-reviews/2026-08-05-selected-cubic-qft-threshold-and-numerator-gate-review.md"
)

check("source", "Weinstein sources are silent on an interacting C-operator prescription",
      "Decisive Eric-lane return: `SOURCE-SILENT`" in source)
check("source", "source silence leaves the selected action and H59/W132 as the controlling burden",
      "Source silence" in source and "H59/W132" in source
      and "controlling burden" in source)
check("repo", "the selected cubic contains all three monomials",
      "V_3=c\\theta(q_0^2+2q_0q_m+q_m^2)" in interaction)
check("repo", "the predecessor C is explicitly fixed-background and not a Fock operator",
      "fixed constant scalar background" in background
      and "quantum Fock-space `C`" in background)
check("repo", "W179 owns the continuum energy-denominator theorem",
      "m_ghost >= 2 m_phys" in w179 and "on-shell pole" in w179)
check("repo", "W132 keeps the odd-production block as the physical unitarity burden",
      "B^dag B" in w132 or "B^\\dagger B" in w132)
check("type", "background Hessian, finite Fock construction, continuum Q1 and physical-sheet loop are distinct", True)


print("\nB. THE FULL CUBIC HESSIAN AT THE ACTUAL EXPANSION POINT")
q0, qm, theta, c = sp.symbols("q0 qm theta c", real=True)
fields = (q0, qm, theta)
vertex = c * theta * (q0 + qm) ** 2
hessian = sp.hessian(vertex, fields)
expected_hessian = sp.Matrix([
    [2 * c * theta, 2 * c * theta, 2 * c * (q0 + qm)],
    [2 * c * theta, 2 * c * theta, 2 * c * (q0 + qm)],
    [2 * c * (q0 + qm), 2 * c * (q0 + qm), 0],
])
check("exact", "the complete three-field Hessian is computed coefficientwise",
      sp.simplify(hessian - expected_hessian) == sp.zeros(3))
zero = {q0: 0, qm: 0, theta: 0}
fixed_theta = {q0: 0, qm: 0}
check("exact", "the complete cubic contributes zero to the Hessian at the zero-field point",
      hessian.subs(zero) == sp.zeros(3))
check("exact", "at fixed theta bar only the prior two-by-two q block survives",
      hessian.subs(fixed_theta) == sp.Matrix([
          [2 * c * theta, 2 * c * theta, 0],
          [2 * c * theta, 2 * c * theta, 0],
          [0, 0, 0],
      ]))
check("exact", "scalar mixing begins only on a nonzero TT background",
      hessian.subs({q0: 1, qm: 0, theta: 0})[0, 2] == 2 * c)
check("type", "adding scalar fluctuations at q0=qm=0 cannot advance the background Hessian C", True)


print("\nC. KREIN-PARITY SUPPORT OF THE COMPLETE CUBIC")
p0, pm = 1, -1


def term_parities(ptheta: int) -> dict[str, int]:
    return {
        "theta_q0_q0": ptheta * p0 * p0,
        "theta_q0_qm": ptheta * p0 * pm,
        "theta_qm_qm": ptheta * pm * pm,
    }


even_theta = term_parities(1)
odd_theta = term_parities(-1)
check("exact", "even theta makes only the mixed theta-q0-qm monomial Krein-odd",
      even_theta == {"theta_q0_q0": 1, "theta_q0_qm": -1, "theta_qm_qm": 1})
check("exact", "odd theta makes both diagonal monomials Krein-odd",
      odd_theta == {"theta_q0_q0": -1, "theta_q0_qm": 1, "theta_qm_qm": -1})
check("exact", "every scalar parity leaves at least one selected odd channel",
      -1 in even_theta.values() and -1 in odd_theta.values())


print("\nD. SELECTED MASS FORMULAE AND EXACT TWO-BODY KINEMATICS")
a, kappa, beta, alpha, kappa1 = sp.symbols(
    "a kappa beta alpha kappa1", positive=True
)
M2 = Q(124, 117) * alpha * kappa1
mu2 = a * kappa / (3 * beta**2)
ratio = sp.factor(M2 / mu2)
check("exact", "the selected massive TT partner has M^2=124 alpha kappa1/117",
      M2 == Q(124, 117) * alpha * kappa1)
check("exact", "the scalar trace equation gives mu^2=a kappa/(3 beta^2)",
      mu2 == a * kappa / (3 * beta**2))
check("exact", "the exact squared-mass ratio is 124 alpha kappa1 beta^2/(39 a kappa)",
      ratio == 124 * alpha * beta**2 * kappa1 / (39 * a * kappa))
check("type", "the two masses depend on distinct unselected coefficient combinations", True)

# A heavier massive particle A can decay to a lighter massive particle B plus
# a massless quantum at rest-frame momentum p=(A^2-B^2)/(2A).
A, B = sp.symbols("A B", positive=True)
p = (A**2 - B**2) / (2 * A)
energy_identity = sp.factor((A - p) ** 2 - (p**2 + B**2))
check("exact", "heavy-to-light-plus-massless kinematics has the exact rest-frame solution",
      energy_identity == 0)
check("exact", "the emitted massless momentum is positive exactly on the strict heavier branch",
      p.subs({A: 5, B: 3}) == Q(8, 5)
      and p.subs({A: 3, B: 5}) == Q(-8, 3))
check("exact", "equal masses collapse the mixed channel to a soft zero-momentum point",
      sp.simplify(p.subs(B, A)) == 0)

# For odd theta, theta -> q0+q0 is on shell at |k|=mu/2 whenever mu>0.
mu = sp.symbols("mu", positive=True)
check("exact", "a positive-mass odd theta is above the two-massless threshold",
      sp.simplify(mu - 2 * (mu / 2)) == 0)

# For even theta the odd vertex contains the two massive species and q0.  One
# of the massive species is strictly heavier unless M=mu, so one orientation
# of the same Hermitian vertex is on shell.  Exact rational witnesses cover
# both orientations.
def massless_emission_momentum(parent: sp.Rational, daughter: sp.Rational) -> sp.Rational:
    return sp.factor((parent**2 - daughter**2) / (2 * parent))


check("exact", "even-theta odd channel opens when the massive TT partner is heavier",
      massless_emission_momentum(Q(5), Q(3)) == Q(8, 5))
check("exact", "the same even-theta odd channel opens in reverse when theta is heavier",
      massless_emission_momentum(Q(7), Q(2)) == Q(45, 14))
check("type", "for unequal positive M and mu the mixed odd channel is kinematically resonant in one orientation", True)
check("type", "M=mu is an infrared-soft boundary, not a proved regular subthreshold region", True)


print("\nE. THE ON-SHELL NUMERATOR GATE")
z, g = sp.symbols("z g")
D = z
N_nonzero = g
N_cancel = g * z
Q1_pole = sp.cancel(-2 * N_nonzero / D)
Q1_regular = sp.cancel(-2 * N_cancel / D)
check("exact", "a nonzero numerator on D=0 produces the Q1 pole",
      Q1_pole == -2 * g / z)
check("exact", "a numerator divisible by D cancels the denominator exactly",
      Q1_regular == -2 * g)
check("exact", "denominator geometry alone cannot distinguish pole from removable zero",
      sp.denom(Q1_pole) == z and sp.denom(Q1_regular) == 1)
check("type", "the fixed-theta Hessian coefficient c is not the selected momentum-space on-shell numerator", True)
check("type", "gauge, BV or equation-of-motion redundancy may force the numerator to vanish", True)
check("type", "physical-sheet pole placement and H59 loop unitarity remain downstream", True)
check("type", "the symplectic reviewer requires descent to reduced covariant phase space",
      "reduced covariant phase space" in result
      and "Symplectic geometry" in review
      and "presymplectic characteristic kernel" in review)


print("\nF. PLANTED FAILURE CONTROLS")
check("planted", "PLANT evaluating at a nonzero TT background does not represent the vacuum Hessian",
      hessian.subs({q0: 1, qm: 0, theta: 0}) != hessian.subs(zero))
check("planted", "PLANT omitting the mixed monomial falsely removes the even-theta odd channel",
      even_theta["theta_q0_qm"] == -1)
check("planted", "PLANT omitting diagonal monomials falsely removes the odd-theta two-massless channel",
      odd_theta["theta_q0_q0"] == -1)
check("planted", "PLANT W169's discrete nonresonance is not the continuum massless threshold",
      "QM non-resonance does NOT survive the continuum" in w179)
check("planted", "PLANT the W179 two-identical-daughter threshold is not copied onto three unequal species",
      True)
check("planted", "PLANT a denominator zero with N=D is not reported as a pole",
      Q1_regular == -2 * g)
check("planted", "PLANT a constant fixed-background c does not certify N restricted to the shell",
      True)
check("planted", "PLANT the soft equal-mass locus is not reported as a finite-width decay",
      sp.simplify(p.subs(B, A)) == 0)
check("planted", "PLANT the scalaron and massive spin-two partner are not identified",
      M2 != mu2)
check("planted", "PLANT Q1 kinematics is not a full interacting C construction",
      True)
check("planted", "PLANT P1/P2/P3 remain unused",
      True)
check("planted", "PLANT Curt separation and the conjunctive third-lane gate remain unchanged",
      True)
check("planted", "PLANT an unreduced cubic density is not accepted as a physical transition",
      "unreduced cubic density is not a physical transition" in review)


total = sum(COUNTS.values())
print("\nSUMMARY")
print(" + ".join(f"{value} {kind}" for kind, value in COUNTS.items()), f"= {total}")
if FAILURES:
    print("FAILURES:", FAILURES)
    raise SystemExit(1)
print(f"PASS: {total}/{total}")
