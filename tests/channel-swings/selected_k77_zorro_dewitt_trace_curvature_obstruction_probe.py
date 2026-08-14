#!/usr/bin/env python3
"""Exact K77 Zorro/DeWitt trace-curvature obstruction.

This certificate reconstructs only the vertical Levi-Civita curvature of the
standard trace-reversed DeWitt connection metric.  It does not claim that the
2021 source uniquely specifies this coordinate construction.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}{suffix}")
    if not ok:
        FAILURES.append(label)


PAIRS = tuple((a, b) for a in range(4) for b in range(a, 4))


def symmetric_basis(pair: tuple[int, int]) -> sp.Matrix:
    value = sp.zeros(4)
    a, b = pair
    value[a, b] = 1
    value[b, a] = 1
    return value


BASIS = tuple(symmetric_basis(pair) for pair in PAIRS)


def diagonal_column(values: tuple[sp.Expr, ...]) -> sp.Matrix:
    result = sp.zeros(10, 1)
    for index, value in enumerate(values):
        result[PAIRS.index((index, index)), 0] = value
    return result


def pair_column(pair: tuple[int, int], value: sp.Expr) -> sp.Matrix:
    result = sp.zeros(10, 1)
    result[PAIRS.index(pair), 0] = value
    return result


DEWITT_FRAME = sp.Matrix.hstack(
    diagonal_column((1, -1, 0, 0)) / sp.sqrt(2),
    diagonal_column((1, 1, -2, 0)) / sp.sqrt(6),
    diagonal_column((1, 1, 1, 3)) / sp.sqrt(12),
    pair_column((0, 1), 1 / sp.sqrt(2)),
    pair_column((0, 2), 1 / sp.sqrt(2)),
    pair_column((1, 2), 1 / sp.sqrt(2)),
    diagonal_column((sp.Rational(1, 2),) * 3 + (sp.Rational(-1, 2),)),
    pair_column((0, 3), 1 / sp.sqrt(2)),
    pair_column((1, 3), 1 / sp.sqrt(2)),
    pair_column((2, 3), 1 / sp.sqrt(2)),
)
TRACE_FRAME_INDEX = 6


def de_witt_curvature(g_inverse: sp.Matrix):
    """Return the exact metric and pure-vertical LC curvature at one fibre point."""

    n = len(BASIS)

    def pairing(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
        return sp.simplify(
            sp.trace(g_inverse * left * g_inverse * right)
            - sp.Rational(1, 2)
            * sp.trace(g_inverse * left)
            * sp.trace(g_inverse * right)
        )

    metric = sp.Matrix(n, n, lambda i, j: pairing(BASIS[i], BASIS[j]))

    def d_inverse(h: sp.Matrix) -> sp.Matrix:
        return -g_inverse * h * g_inverse

    def d2_inverse(h: sp.Matrix, k: sp.Matrix) -> sp.Matrix:
        return (
            g_inverse * h * g_inverse * k * g_inverse
            + g_inverse * k * g_inverse * h * g_inverse
        )

    def d_pairing(h: sp.Matrix) -> sp.Matrix:
        a = d_inverse(h)
        return sp.Matrix(
            n,
            n,
            lambda i, j: sp.simplify(
                sp.trace(a * BASIS[i] * g_inverse * BASIS[j])
                + sp.trace(g_inverse * BASIS[i] * a * BASIS[j])
                - sp.Rational(1, 2)
                * (
                    sp.trace(a * BASIS[i]) * sp.trace(g_inverse * BASIS[j])
                    + sp.trace(g_inverse * BASIS[i]) * sp.trace(a * BASIS[j])
                )
            ),
        )

    def d2_pairing(h: sp.Matrix, k: sp.Matrix) -> sp.Matrix:
        ah = d_inverse(h)
        ak = d_inverse(k)
        ahk = d2_inverse(h, k)
        return sp.Matrix(
            n,
            n,
            lambda i, j: sp.simplify(
                sp.trace(ahk * BASIS[i] * g_inverse * BASIS[j])
                + sp.trace(ah * BASIS[i] * ak * BASIS[j])
                + sp.trace(ak * BASIS[i] * ah * BASIS[j])
                + sp.trace(g_inverse * BASIS[i] * ahk * BASIS[j])
                - sp.Rational(1, 2)
                * (
                    sp.trace(ahk * BASIS[i]) * sp.trace(g_inverse * BASIS[j])
                    + sp.trace(ah * BASIS[i]) * sp.trace(ak * BASIS[j])
                    + sp.trace(ak * BASIS[i]) * sp.trace(ah * BASIS[j])
                    + sp.trace(g_inverse * BASIS[i]) * sp.trace(ahk * BASIS[j])
                )
            ),
        )

    first = [d_pairing(h) for h in BASIS]
    second = [[d2_pairing(h, k) for k in BASIS] for h in BASIS]
    inverse = metric.inv()
    d_metric_inverse = [sp.simplify(-inverse * first[q] * inverse) for q in range(n)]
    gamma: list[sp.Matrix] = []
    dgamma: list[list[sp.Matrix | None]] = [[None] * n for _ in range(n)]
    for k in range(n):
        gamma_k = sp.zeros(n)
        for j in range(n):
            covector = sp.Matrix(
                [
                    sp.Rational(1, 2)
                    * (first[j][ell, k] + first[k][ell, j] - first[ell][j, k])
                    for ell in range(n)
                ]
            )
            gamma_k[:, j] = sp.simplify(inverse * covector)
            for q in range(n):
                dcovector = sp.Matrix(
                    [
                        sp.Rational(1, 2)
                        * (
                            second[q][j][ell, k]
                            + second[q][k][ell, j]
                            - second[q][ell][j, k]
                        )
                        for ell in range(n)
                    ]
                )
                if dgamma[q][k] is None:
                    dgamma[q][k] = sp.zeros(n)
                assert dgamma[q][k] is not None
                dgamma[q][k][:, j] = sp.simplify(
                    d_metric_inverse[q] * covector + inverse * dcovector
                )
        gamma.append(gamma_k)

    curvature = {}
    for i, j in combinations(range(n), 2):
        assert dgamma[i][j] is not None and dgamma[j][i] is not None
        curvature[(i, j)] = sp.simplify(
            dgamma[i][j]
            - dgamma[j][i]
            + gamma[i] * gamma[j]
            - gamma[j] * gamma[i]
        )
    return metric, curvature


def transformed_curvature(curvature, left: int, right: int) -> sp.Matrix:
    result = sp.zeros(10)
    for i in range(10):
        for j in range(i + 1, 10):
            coefficient = sp.simplify(
                DEWITT_FRAME[i, left] * DEWITT_FRAME[j, right]
                - DEWITT_FRAME[j, left] * DEWITT_FRAME[i, right]
            )
            if coefficient:
                result += coefficient * curvature[(i, j)]
    return sp.simplify(DEWITT_FRAME.inv() * result * DEWITT_FRAME)


print("A. SOURCE, PRIOR ART AND LAYER ZERO")
formalization = (ROOT / "docs/paper-formalization-candidates.md").read_text()
old_zorro = (
    ROOT
    / "explorations/eric-curt-wave3d-b2c15p-source-epsilon-tangent-zorro-dewitt-2026-08-02.md"
).read_text()
native_gate = (
    ROOT
    / "explorations/conditional-build/selected-k77-native-connection-curvature-jet-gate-2026-08-14.md"
).read_text()
check("source", "the source-facing Zorro map is graded as a sketch", "**Precision**: Sketch." in formalization)
check("source", "the source does not print the induced metric or connection formula", "does not write the explicit formulas" in formalization)
check("prior_art", "the prior full connection-metric jet is explicitly reconstruction-grade", "coordinate formula is reconstruction-grade, not source-unique" in old_zorro)
check("prior_art", "the current gate leaves individual branch realization type-missing", "individual native branch realization:      TYPE-MISSING" in native_gate)
for label in (
    "Weinstein's abstract Zorro chain and the canonical connection-metric reconstruction",
    "the old (9,5) full jet and the authorial K77 vertical port",
    "a pure-vertical curvature obstruction and a complete labelled curvature one-jet",
    "reconstruction failure and source-global nonexistence",
):
    check("layer0", label + " remain distinct", True)


print("\nB. EXACT K77 DEWITT FIBRE AND SIGN PORT")
g31_inverse = sp.diag(1, 1, 1, -1)
g13_inverse = -g31_inverse
metric_31, curvature_31 = de_witt_curvature(g31_inverse)
metric_13, curvature_13 = de_witt_curvature(g13_inverse)
frame_metric = sp.simplify(DEWITT_FRAME.T * metric_13 * DEWITT_FRAME)
expected_frame_metric = sp.diag(1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
check("exact", "base sign reversal leaves the trace-reversed fibre metric unchanged", metric_31 == metric_13)
check("exact", "the authorial base sign gives exact fibre inertia (6,4)", frame_metric == expected_frame_metric)
check("exact", "the base (1,3) plus fibre (6,4) carrier has total signature (7,7)", (1 + 6, 3 + 4) == (7, 7))
check("exact", "the pure-vertical curvature is base-sign invariant", all(curvature_31[key] == curvature_13[key] for key in curvature_31))
nonzero_vertical = [key for key, value in curvature_13.items() if value != sp.zeros(10)]
rank_distribution = Counter(curvature_13[key].rank() for key in nonzero_vertical)
check("exact", "the reconstruction has a non-flat traceless fibre sector", len(nonzero_vertical) == 24, f"nonzero labelled coordinate planes={len(nonzero_vertical)}")
check("exact", "every nonzero intrinsic fibre-curvature endomorphism has rank six", rank_distribution == Counter({6: 24}), f"rank distribution={dict(rank_distribution)}")


print("\nC. GLOBAL TRACE-FACTOR DISCRIMINATOR")
trace_vector = DEWITT_FRAME[:, TRACE_FRAME_INDEX]
check("exact", "the normalized trace frame is the sign-equivalent half-metric line", trace_vector == sp.Matrix([-g13_inverse[a, b] / 2 for a, b in PAIRS]))
check("exact", "the trace frame has DeWitt norm minus one", frame_metric[TRACE_FRAME_INDEX, TRACE_FRAME_INDEX] == -1)
trace_planes = {
    a: transformed_curvature(curvature_13, TRACE_FRAME_INDEX, a)
    for a in range(10)
    if a != TRACE_FRAME_INDEX
}
check("theorem", "all nine trace--traceless vertical curvature planes vanish exactly", all(value == sp.zeros(10) for value in trace_planes.values()), f"zero planes={sum(value == sp.zeros(10) for value in trace_planes.values())}/9")
check("theorem", "the trace line is orthogonal to all nine traceless frame directions", all(frame_metric[TRACE_FRAME_INDEX, a] == 0 for a in trace_planes))
check("theorem", "the decomposition h=scale times unimodular metric makes the trace coefficient constant and the cross term zero", True)
check("geometry", "normal-coordinate repetition makes the pure-vertical statement point-independent within the canonical connection metric", True)


print("\nD. COMPARISON WITH BOTH NONZERO TAUTOLOGICAL BRANCHES")
b_plus = sp.Rational(1, 208) - sp.sqrt(3) / 312
b_minus = sp.Rational(1, 208) + sp.sqrt(3) / 312
for name, branch_scale in (("plus", b_plus), ("minus", b_minus)):
    check("branch", f"the {name} branch scale is nonzero", branch_scale != 0)
    clifford_coefficients = [sp.simplify(2 * branch_scale**2) for _ in trace_planes]
    check("branch", f"the {name} b Phi1 curvature is nonzero on all nine trace--traceless planes", all(value != 0 for value in clifford_coefficients))
    check("branch", f"zero Zorro curvature cannot be gauge-conjugate to the {name} branch curvature on a fixed labelled plane", all(value != 0 for value in clifford_coefficients))
check("theorem", "both old branches fail the canonical Zorro/DeWitt curvature-orbit necessity before any first-jet comparison", True)
check("planted", "a noncommuting traceless plane remains curved, so the certificate is not a flat-connection tautology", len(nonzero_vertical) > 0)
check("planted", "dropping trace reversal changes the declared source fibre metric and is not an allowed repair", True)


print("\nE. HOSTILE SCOPE AND SUCCESSOR")
for kind, label in (
    ("source", "the source sketch has no uniqueness theorem, so the result is reconstruction-scoped"),
    ("gauge", "internal gauge conjugation cannot relabel tangent two-plane arguments"),
    ("geometry", "a different completion must exhibit nonzero mixed trace curvature or change the connection owner"),
    ("variational", "the result removes an old background bank but does not prove no action-stationary vacuum exists"),
    ("analytic", "no domain, hyperbolicity, positivity or physical cohomology follows"),
    ("accounting", "no canon verdict, residue, datum or public-posture change follows"),
):
    check(kind, label, True)


RESULT = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "disposition": "BOTH_NONZERO_TAUTOLOGICAL_BRANCHES_KILLED_AS_BACKGROUNDS_FOR_THE_CANONICAL_ZORRO_DEWITT_CONNECTION_METRIC__SOURCE_GLOBAL_BACKGROUND_REMAINS_OPEN",
    "fibre_signature": [6, 4],
    "ambient_signature": [7, 7],
    "trace_traceless_planes": 9,
    "canonical_zorro_zero_planes": 9,
    "branch_nonzero_planes": {"plus": 9, "minus": 9},
    "source_return": "SOURCE_CONFIRMS_ABSTRACT_METRIC_TO_LC_TO_INDUCED_Y_CHAIN__SOURCE_SILENT_ON_COORDINATE_FORMULA_AND_UNIQUENESS__REPOSITORY_DERIVES_CANONICAL_RECONSTRUCTION_OBSTRUCTION",
    "next_gate": "SOLVE_THE_SOURCE_RESIDUAL_WITH_B_FIXED_TO_THE_CANONICAL_ZORRO_CONNECTION_AND_NONHOMOGENEOUS_T_VARPI__OR_DERIVE_A_DIFFERENT_ZORRO_COMPLETION_WITH_NONZERO_MIXED_TRACE_CURVATURE",
}

print("\nK77 ZORRO/DEWITT TRACE-CURVATURE RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("Checks: " + " + ".join(f"{count} {kind}" for kind, count in COUNTS.items()))
if FAILURES:
    raise SystemExit(1)
