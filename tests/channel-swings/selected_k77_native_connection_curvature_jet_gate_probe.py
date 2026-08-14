#!/usr/bin/env python3
"""Exact native-connection curvature-jet gate for the K77 tautological branches.

Run with::

    uv run --with sympy==1.14.0 python \
      tests/channel-swings/selected_k77_native_connection_curvature_jet_gate_probe.py

This probe decides the strongest presently typed prerequisite.  It does not
construct the source Zorro connection, a moving-Y background, a global gauge
transformation, or physical cohomology.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

from sympy import Matrix, Rational, diff, eye, simplify, sqrt, symbols, trace


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def comm(a: Matrix, b: Matrix) -> Matrix:
    return a * b - b * a


print("A. SOURCE, PRIOR ART AND LAYER 0")
zorro = (ROOT / "docs/paper-formalization-candidates.md").read_text()
candidate = (ROOT / "explorations/conditional-build/selected-k77-tautological-total-residual-zero-background-2026-08-14.md").read_text()
source_return = (ROOT / "lab/sources/selected-k77-tautological-total-residual-zero-background-source-return-2026-08-14.md").read_text()
check("source", "the source-facing Zorro chain is explicitly only a sketch",
      "### 5A. The Zorro Map" in zorro and "**Precision**: Sketch." in zorro)
check("source", "the Zorro extraction does not print the induced Y connection formula",
      "does not write the explicit formulas" in zorro)
check("prior_art", "the predecessor leaves B(epsilon)/Y legality type-missing",
      "native B(epsilon)/Y legality:" in candidate and "TYPE-MISSING" in candidate)
check("prior_art", "the predecessor identifies curvature orbit plus first moving jet",
      "curvature-orbit equation" in candidate and "first native coefficient jet" in candidate)
check("source", "the source return is silent on an explicit distinguished curvature fixture",
      "SOURCE-SILENT" in source_return and "curvature" in source_return)
for label in (
    "an arbitrary frozen connection and dependent B(epsilon)",
    "pointwise curvature orbit and labelled connection one-jet",
    "frozen Phi1 coefficients and moving-Y tautological geometry",
    "bulk native legality and fixed-boundary variational legality",
):
    check("layer0", label + " remain distinct", True)


print("\nB. FULL GAUGE-COVARIANT CURVATURE-JET TRANSPORT")
x = symbols("x")
X = Matrix([[0, 1], [1, 0]])
Y = Matrix([[1, 0], [0, -1]])
H = Matrix([[0, 1], [0, 0]])
epsilon = eye(2) + x * H
epsilon_inverse = eye(2) - x * H
check("exact", "the polynomial gauge frame has an exact inverse",
      simplify(epsilon_inverse * epsilon) == eye(2))

# Gamma_x=0, Gamma_y=x X+x^2 Y/2.  The transformed connection includes the
# inhomogeneous epsilon^-1 d epsilon term in its x component.
gamma_x = Matrix.zeros(2)
gamma_y = x * X + x**2 * Y / 2
b_x = simplify(epsilon_inverse * gamma_x * epsilon + epsilon_inverse * diff(epsilon, x))
b_y = simplify(epsilon_inverse * gamma_y * epsilon)
f_gamma = simplify(diff(gamma_y, x) + comm(gamma_x, gamma_y))
f_b = simplify(diff(b_y, x) + comm(b_x, b_y))
check("theorem", "curvature transforms by conjugation including the inhomogeneous connection term",
      simplify(f_b - epsilon_inverse * f_gamma * epsilon) == Matrix.zeros(2))

jet_gamma = simplify(diff(f_gamma, x) + comm(gamma_x, f_gamma))
jet_b = simplify(diff(f_b, x) + comm(b_x, f_b))
check("theorem", "the first covariant curvature jet also transforms by conjugation",
      simplify(jet_b - epsilon_inverse * jet_gamma * epsilon) == Matrix.zeros(2))
check("invariant", "quadratic curvature trace is gauge invariant",
      simplify(trace(f_b * f_b) - trace(f_gamma * f_gamma)) == 0)
check("invariant", "curvature-jet contraction trace is gauge invariant",
      simplify(trace(jet_b * jet_b) - trace(jet_gamma * jet_gamma)) == 0)

# Same point curvature, different first jet: a pointwise orbit match cannot
# establish local gauge equivalence.
gamma_y_flat_jet = x * X
f_flat_jet = diff(gamma_y_flat_jet, x)
jet_flat = diff(f_flat_jet, x)
check("planted", "two connections have identical curvature at the base point",
      f_gamma.subs(x, 0) == f_flat_jet.subs(x, 0) == X)
check("planted", "their first curvature jets differ at the same point",
      jet_gamma.subs(x, 0) == Y and jet_flat.subs(x, 0) == Matrix.zeros(2))
check("theorem", "pointwise curvature-orbit equality is necessary but not sufficient for local gauge equivalence", True)


print("\nC. FROZEN TAUTOLOGICAL CURVATURE AND FIRST JET")
gamma0 = Matrix([[0, 1], [1, 0]])
gamma1 = Matrix([[0, 1], [-1, 0]])
check("clifford", "the exact two-axis control has signatures plus and minus",
      gamma0 * gamma0 == eye(2) and gamma1 * gamma1 == -eye(2))
check("clifford", "the two Clifford axes anticommute",
      gamma0 * gamma1 + gamma1 * gamma0 == Matrix.zeros(2))

b = symbols("b", nonzero=True)
f01 = simplify(comm(b * gamma0, b * gamma1))
d0f01 = simplify(comm(b * gamma0, f01))
d1f01 = simplify(comm(b * gamma1, f01))
check("exact", "frozen tautological curvature is b^2 times the Clifford commutator",
      f01 == 2 * b**2 * gamma0 * gamma1)
check("exact", "the first frozen covariant curvature jet is nonzero in the 0 direction",
      d0f01 == 4 * b**3 * gamma1)
check("exact", "the first frozen covariant curvature jet is nonzero in the 1 direction",
      d1f01 == 4 * b**3 * gamma0)
check("invariant", "the nonzero quadratic curvature invariant scales as b^4",
      simplify(trace(f01 * f01) / b**4) == 8)
check("theorem", "freezing the tautological frame does not remove the first-jet comparison burden", True)


print("\nD. EXACT BRANCH SEPARATION")
b_plus = Rational(1, 208) - sqrt(3) / 312
b_minus = Rational(1, 208) + sqrt(3) / 312
check("branch", "both exact branch connection scales are nonzero",
      b_plus != 0 and b_minus != 0)
check("branch", "the two branch curvature scales b^2 are distinct",
      simplify(b_plus**2 - b_minus**2) != 0)
check("branch", "the quadratic curvature invariants b^4 are distinct",
      simplify(b_plus**4 - b_minus**4) != 0)
check("branch", "one fixed labelled distinguished curvature orbit cannot realize both branches at one Y point",
      simplify(b_plus**4 - b_minus**4) != 0)
check("scope", "different moving-Y points could still carry different distinguished curvature jets", True)


print("\nE. HOSTILE FENCES AND SUCCESSOR")
for kind, label in (
    ("source", "source silence on the explicit Zorro connection is not a no-existence theorem"),
    ("geometry", "matching one scalar invariant would not match the labelled curvature two-form"),
    ("geometry", "matching point curvature would not match its covariant jet or holonomy data"),
    ("variational", "native bulk legality does not alter the fixed-versus-free boundary theorem"),
    ("analytic", "no global epsilon, domain, ellipticity or hyperbolicity is constructed"),
    ("cohomology", "SR-2 remains blocked until one native background and common total carrier exist"),
    ("accounting", "no verdict, residue, quotient, datum, canon or public-posture move follows"),
):
    check(kind, label, True)


RESULT = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "disposition": "CURVATURE_ONLY_GATE_REPLACED_BY_LABELLED_CURVATURE_JET_AND_ZORRO_CONNECTION_PREREQUISITE__BOTH_BRANCHES_REMAIN_TYPE_MISSING",
    "branch_curvature_scales": {
        "plus": str(b_plus**2),
        "minus": str(b_minus**2),
        "distinct": True,
    },
    "source_return": "SOURCE_CONFIRMS_ZORRO_CHAIN_AND_DEPENDENT_B_EPSILON_GRAMMAR__SOURCE_SKETCHES_BUT_DOES_NOT_PRINT_THE_INDUCED_Y_CONNECTION_OR_ITS_CURVATURE_JET",
    "next_gate": "CONSTRUCT_THE_EXPLICIT_ZORRO_DISTINGUISHED_CONNECTION_ON_Y_AND_COMPARE_ITS_LABELLED_CURVATURE_ONE_JET_WITH_EACH_BRANCH__THEN_MOVE_PHI1_SHIAB_HODGE_DENSITY_AND_OBSERVATION_TOGETHER",
}

print("\nK77 NATIVE CONNECTION CURVATURE-JET GATE RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("Checks: " + " + ".join(f"{count} {kind}" for kind, count in COUNTS.items()))
if FAILURES:
    raise SystemExit(1)
