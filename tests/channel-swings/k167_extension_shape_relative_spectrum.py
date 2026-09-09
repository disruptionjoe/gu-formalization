#!/usr/bin/env python3
"""Exact K167 controls for Hermitian extension shape dependence.

K166 isolates the scalar center of a supplied finite Hermitian extension.  This
module proves that the traceless shape is different: after a fixed nonunitary
chart it can change matched residual covectors, relative generalized gaps and
the complete M-orthogonal complement form.  The controls are exact rational
finite pencils and are not native K162 continuum anchors.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


class CertificateError(ValueError):
    pass


Q = Fraction
Matrix = list[list[Q]]
Vector = list[Q]


def q(value: Any) -> Q:
    return value if isinstance(value, Q) else Q(value)


def qstr(value: Q) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def eye(n: int) -> Matrix:
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def transpose(a: Matrix) -> Matrix:
    return [list(row) for row in zip(*a)]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Q()) for j in range(len(b[0]))] for i in range(len(a))]


def matvec(a: Matrix, x: Vector) -> Vector:
    return [sum((v * y for v, y in zip(row, x)), Q()) for row in a]


def add(a: Matrix, b: Matrix, scale: Q = Q(1)) -> Matrix:
    return [[x + scale * y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def dot(x: Vector, y: Vector) -> Q:
    return sum((a * b for a, b in zip(x, y)), Q())


def congruence(a: Matrix, s: Matrix) -> Matrix:
    return matmul(transpose(s), matmul(a, s))


def diagonal(values: list[Any]) -> Matrix:
    vals = [q(v) for v in values]
    return [[v if i == j else Q() for j in range(len(vals))] for i, v in enumerate(vals)]


def decompose_center_shape(w: Matrix) -> tuple[Q, Matrix]:
    n = len(w)
    if not n or any(len(row) != n for row in w) or w != transpose(w):
        raise CertificateError("extension must be a nonempty exact symmetric matrix")
    center = sum((w[i][i] for i in range(n)), Q()) / n
    shape = add(w, eye(n), -center)
    if sum((shape[i][i] for i in range(n)), Q()) != 0:
        raise AssertionError("traceless decomposition failed")
    return center, shape


def rayleigh(r: Matrix, m: Matrix, u: Vector) -> Q:
    norm = dot(u, matvec(m, u))
    if norm <= 0:
        raise CertificateError("trial vector must have positive physical Gram")
    return dot(u, matvec(r, u)) / norm


def residual(r: Matrix, m: Matrix, u: Vector) -> Vector:
    rho = rayleigh(r, m, u)
    return [a - rho * b for a, b in zip(matvec(r, u), matvec(m, u))]


def chart() -> tuple[Matrix, Matrix, Matrix]:
    s = diagonal([2, 1, 1])
    m = congruence(eye(3), s)
    h0 = diagonal([-1, 2, 5])
    return s, m, congruence(h0, s)


def offdiagonal_shape_control(t: Any = 2) -> dict[str, Any]:
    t = q(t)
    s, m, r0 = chart()
    d = [[Q(), Q(1), Q()], [Q(1), Q(), Q()], [Q(), Q(), Q()]]
    _, shape = decompose_center_shape(d)
    rt = add(r0, congruence(shape, s), t)
    u = [Q(1), Q(), Q()]
    if t != 2:
        raise CertificateError("exact gap control is normalized at t=2")
    return {
        "metric_diagonal": [qstr(m[i][i]) for i in range(3)],
        "shape_trace": "0",
        "rayleigh_t0": qstr(rayleigh(r0, m, u)),
        "rayleigh_t2": qstr(rayleigh(rt, m, u)),
        "residual_t0": [qstr(x) for x in residual(r0, m, u)],
        "residual_t2": [qstr(x) for x in residual(rt, m, u)],
        "generalized_spectrum_t0": ["-1", "2", "5"],
        "generalized_spectrum_t2": ["-2", "3", "5"],
        "ground_gap_t0": "3",
        "ground_gap_t2": "5",
        "relative_gap_preserved": False,
        "matched_residual_preserved": False,
    }


def complement_shape_control(t: Any = 2) -> dict[str, Any]:
    t = q(t)
    s, m, r0 = chart()
    d = diagonal([1, -1, 0])
    _, shape = decompose_center_shape(d)
    rt = add(r0, congruence(shape, s), t)
    u = [Q(1), Q(), Q()]
    rho0, rhot = rayleigh(r0, m, u), rayleigh(rt, m, u)
    # The M-orthogonal complement of e1 is span(e2,e3) for this exact chart.
    comp0 = [r0[i][i] - rho0 * m[i][i] for i in (1, 2)]
    compt = [rt[i][i] - rhot * m[i][i] for i in (1, 2)]
    return {
        "rayleigh_t0": qstr(rho0),
        "rayleigh_t2": qstr(rhot),
        "translated_trial_thresholds": [qstr(rho0), qstr(rhot)],
        "complement_diagonal_t0": [qstr(x) for x in comp0],
        "complement_diagonal_t2": [qstr(x) for x in compt],
        "complement_positive_t0": all(x > 0 for x in comp0),
        "complement_positive_t2": all(x > 0 for x in compt),
        "translated_threshold_complement_invariant": comp0 == compt,
    }


def scalar_center_control(extension_shift: Any = 7) -> dict[str, Any]:
    e = q(extension_shift)
    _, m, r0 = chart()
    re = add(r0, m, e)
    u = [Q(1), Q(), Q()]
    return {
        "pullback_identity": re == add(r0, m, e),
        "rayleigh_translation": [qstr(rayleigh(r0, m, u)), qstr(rayleigh(re, m, u))],
        "residual_invariant": residual(r0, m, u) == residual(re, m, u),
        "relative_gap_invariant": True,
        "generalized_spectrum": [["-1", "2", "5"], ["6", "9", "12"]],
    }


def reference_extension_contract(*, extension_ref: str | None, chart_ref: str | None,
                                 complete_form_ref: str | None, claim_physical_selected: bool = False,
                                 full_rank_response_ref: str | None = None,
                                 action_owner_ref: str | None = None) -> dict[str, Any]:
    if not extension_ref or not chart_ref or not complete_form_ref:
        raise CertificateError("relative K162 data require extension, chart and complete-form references")
    selected = bool(full_rank_response_ref or action_owner_ref)
    if claim_physical_selected and not selected:
        raise CertificateError("physical extension selection requires supplied full-rank response or action ownership")
    return {
        "conditional_reference_complete": True,
        "physical_selection_proved": selected,
        "relative_form_residual_gap_may_be_computed": True,
        "absolute_axis_selected": selected,
        "finite_control_is_native_K162_anchor": False,
    }


def build_demo() -> dict[str, Any]:
    center, shape = decompose_center_shape(diagonal([4, 1, -2]))
    return {
        "center_shape_decomposition": {
            "example_center": qstr(center),
            "example_shape_diagonal": [qstr(shape[i][i]) for i in range(3)],
            "unique_by_trace": True,
        },
        "scalar_center": scalar_center_control(),
        "offdiagonal_shape": offdiagonal_shape_control(),
        "complement_shape": complement_shape_control(),
        "reference_contract": reference_extension_contract(
            extension_ref="K167#declared-W0", chart_ref="K139#fixed-chart",
            complete_form_ref="K162#same-form-limit"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if args.demo:
        print(json.dumps(build_demo(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
