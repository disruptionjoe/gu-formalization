#!/usr/bin/env python3
r"""Exact controls for the conditional vertical-connection reduction.

This probe does not model the GU Hessian.  It tests three pieces of algebra
that any proposed reduction must preserve:

1. the mixed curvature in an adapted, possibly non-holonomic frame contains
   both the vertical derivative and the frame-structure term;
2. restricting a Hessian to a named scalar line is not a consistent
   truncation unless the full Hessian preserves that line; and
3. an adjoint commutator Hessian has an exact gauge-null direction, while a
   planted gauge-breaking mass lifts it.

Pre-registered kill controls (before execution):

* deleting ``-C_AB^C A_C`` must turn a planted zero mixed curvature nonzero;
* deleting ``-e_i A_mu`` must turn a second planted zero mixed curvature
  nonzero;
* the proposed scalar line must leak for a deliberately misaligned
  background, while an aligned control must not leak; and
* adding an identity mass must lift the exact null direction.

All arithmetic is ``fractions.Fraction``.  Exit 0 means the comparator and its
planted controls work; it is not evidence that the missing GU reduction map or
physical Hessian exists.
"""

from __future__ import annotations

from fractions import Fraction
import json
from typing import Iterable


Q = Fraction
Matrix = tuple[tuple[Q, ...], ...]
Vector = tuple[Q, ...]


def matrix(rows: Iterable[Iterable[int | Q]]) -> Matrix:
    return tuple(tuple(Q(value) for value in row) for row in rows)


def zeros(size: int) -> Matrix:
    return tuple(tuple(Q(0) for _ in range(size)) for _ in range(size))


def add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][col] + right[row][col] for col in range(len(left)))
        for row in range(len(left))
    )


def sub(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[row][col] - right[row][col] for col in range(len(left)))
        for row in range(len(left))
    )


def scale(value: Q, item: Matrix) -> Matrix:
    return tuple(tuple(value * entry for entry in row) for row in item)


def multiply(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    return tuple(
        tuple(
            sum((left[row][mid] * right[mid][col] for mid in range(size)), Q(0))
            for col in range(size)
        )
        for row in range(size)
    )


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return sub(multiply(left, right), multiply(right, left))


def structure_sum(terms: Iterable[tuple[Q, Matrix]], size: int) -> Matrix:
    out = zeros(size)
    for coefficient, component in terms:
        out = add(out, scale(coefficient, component))
    return out


def curvature_component(
    derivative_a_of_b: Matrix,
    derivative_b_of_a: Matrix,
    connection_a: Matrix,
    connection_b: Matrix,
    structure_terms: Iterable[tuple[Q, Matrix]],
) -> Matrix:
    """F_AB = e_A A_B - e_B A_A + [A_A,A_B] - C_AB^C A_C."""
    return sub(
        add(
            sub(derivative_a_of_b, derivative_b_of_a),
            commutator(connection_a, connection_b),
        ),
        structure_sum(structure_terms, len(connection_a)),
    )


def dot(left: Vector, right: Vector) -> Q:
    return sum((a * b for a, b in zip(left, right, strict=True)), Q(0))


def vector_sub(left: Vector, right: Vector) -> Vector:
    return tuple(a - b for a, b in zip(left, right, strict=True))


def vector_scale(value: Q, vector: Vector) -> Vector:
    return tuple(value * entry for entry in vector)


def commutator_hessian(background: Vector, fluctuation: Vector) -> Vector:
    """The exact so(3) operator -ad_q^2 v = |q|^2 v - q(q.v)."""
    return vector_sub(
        vector_scale(dot(background, background), fluctuation),
        vector_scale(dot(background, fluctuation), background),
    )


def line_leak(vector: Vector) -> Vector:
    """Complement of span((1,0,0))."""
    return (Q(0), vector[1], vector[2])


CHECKS: dict[str, bool] = {}


def check(label: str, condition: bool) -> None:
    CHECKS[label] = bool(condition)
    print(f"{'PASS' if condition else 'FAIL'}: {label}")


ZERO = zeros(2)
HALF_H = matrix(((Q(1, 2), 0), (0, Q(-1, 2))))
E = matrix(((0, 1), (0, 0)))

# Plant 1: [H/2,E] = E is cancelled exactly by [e_h,e_v] = e_v.
full_nonholonomic = curvature_component(
    ZERO,
    ZERO,
    HALF_H,
    E,
    ((Q(1), E),),
)
expanded_nonholonomic = sub(
    commutator(HALF_H, E),  # D^0_h Phi_v
    E,  # C_hv^v Phi_v
)
naive_without_structure = curvature_component(
    ZERO,
    ZERO,
    HALF_H,
    E,
    (),
)
coordinate_frame_control = curvature_component(
    ZERO,
    ZERO,
    HALF_H,
    E,
    ((Q(0), E),),
)
changed_structure_control = curvature_component(
    ZERO,
    ZERO,
    HALF_H,
    E,
    ((Q(2), E),),
)

check("direct and background-split curvature formulas agree", full_nonholonomic == expanded_nonholonomic)
check("non-holonomic cancellation plant is exactly zero", full_nonholonomic == ZERO)
check("omitting -C_AB^C A_C is detected", naive_without_structure == E)
check("coordinate-frame control retains the commutator", coordinate_frame_control == E)
check("changed structure coefficient produces the expected leak", changed_structure_control == scale(Q(-1), E))

# Plant 2: e_h A_v and e_v A_h cancel.  Dropping the vertical derivative
# falsely leaves E.
mixed_derivative_exact = curvature_component(E, E, ZERO, ZERO, ())
mixed_derivative_naive = curvature_component(E, ZERO, ZERO, ZERO, ())
check("mixed derivative cancellation plant is exactly zero", mixed_derivative_exact == ZERO)
check("omitting -e_i A_mu is detected", mixed_derivative_naive == E)

# A toy adjoint commutator Hessian.  This is a comparator for closure and
# gauge-null bookkeeping, not the GU Hessian.
q_misaligned: Vector = (Q(1), Q(1), Q(0))
q_aligned: Vector = (Q(1), Q(0), Q(0))
scalar_line: Vector = (Q(1), Q(0), Q(0))

misaligned_image = commutator_hessian(q_misaligned, scalar_line)
aligned_image = commutator_hessian(q_aligned, scalar_line)
gauge_null_image = commutator_hessian(q_misaligned, q_misaligned)
planted_broken_image = tuple(
    h_entry + q_entry
    for h_entry, q_entry in zip(gauge_null_image, q_misaligned, strict=True)
)

check(
    "restricted scalar line is nonclosed for a misaligned background",
    line_leak(misaligned_image) != (Q(0), Q(0), Q(0)),
)
check(
    "aligned positive control preserves the scalar line",
    line_leak(aligned_image) == (Q(0), Q(0), Q(0)),
)
check(
    "commutator Hessian has the exact gauge-null direction",
    gauge_null_image == (Q(0), Q(0), Q(0)),
)
check(
    "planted identity mass lifts the gauge-null direction",
    planted_broken_image == q_misaligned,
)

passed = sum(CHECKS.values())
total = len(CHECKS)
verdict = (
    "COMPARATOR-PASSES; VERTICAL-CARRIER-EXISTS; "
    "X4-RETENTION-MAP-AND-PHYSICAL-HESSIAN-UNBUILT"
)
print(
    json.dumps(
        {
            "passed": passed,
            "total": total,
            "verdict": verdict,
            "scope": "exact algebraic comparator only",
        },
        sort_keys=True,
    )
)

if passed != total:
    raise SystemExit(1)
