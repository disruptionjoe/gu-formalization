#!/usr/bin/env python3
"""Exact K165 generalized-form complement and count-route certificates.

The module distinguishes a conforming Galerkin space from a reducing spectral
subspace.  For the K139 boundary chart the physical eigenproblem is the
generalized pencil ``R-zM`` with ``M=S* S``; therefore the complement used by
a count proof is M-orthogonal, not the free Hilbert complement.  The module
also exposes the cancellation lost by separately norm-bounding the auxiliary
``lambda`` pieces and compiles an exact generalized Schur positive control.

It deliberately does not supply the still-missing native K139 anchor form,
absolute regular-core bound, form-dual residual, or complete complement floor.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence


HERE = Path(__file__).resolve().parent


def _load_k150():
    path = HERE / "k150_certified_schur_tail_solver.py"
    spec = importlib.util.spec_from_file_location("k165_k150", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load exact inertia kernel at {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K150 = _load_k150()


class CertificateError(ValueError):
    """Raised when a claimed same-form count omits a required premise."""


def q(value: Any) -> Fraction:
    try:
        return value if isinstance(value, Fraction) else Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise CertificateError(f"invalid rational input: {value!r}") from exc


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def symmetric(rows: Sequence[Sequence[Any]]) -> list[list[Fraction]]:
    matrix = [[q(value) for value in row] for row in rows]
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise CertificateError("matrix must be nonempty and square")
    if any(matrix[i][j] != matrix[j][i] for i in range(len(matrix)) for j in range(len(matrix))):
        raise CertificateError("matrix must be exactly symmetric")
    return matrix


def matvec(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [sum((value * vector[j] for j, value in enumerate(row)), Fraction()) for row in matrix]


def dot(left: list[Fraction], right: list[Fraction]) -> Fraction:
    return sum((x * y for x, y in zip(left, right, strict=True)), Fraction())


def bilinear(left: list[Fraction], matrix: list[list[Fraction]], right: list[Fraction]) -> Fraction:
    return dot(left, matvec(matrix, right))


def subtract_scaled(left: list[list[Fraction]], scale: Fraction, right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [
        [left[i][j] - scale * right[i][j] for j in range(len(left))]
        for i in range(len(left))
    ]


def congruence(matrix: list[list[Fraction]], columns: list[list[Fraction]]) -> list[list[Fraction]]:
    return [
        [bilinear(columns[i], matrix, columns[j]) for j in range(len(columns))]
        for i in range(len(columns))
    ]


def physical_cell_reduction_obstruction(left: Any, right: Any) -> dict[str, Any]:
    """Prove a positive-width dyadic indicator space does not reduce omega.

    ``omega(p)=sqrt(1+p^2)+1/4`` is strictly convex, hence nonconstant on
    every interval of positive width.  Multiplying a cell indicator by omega
    therefore leaves the piecewise-constant cell span and has a nonzero
    orthogonal residual.  Conformity and exact Gram transport survive.
    """
    a, b = q(left), q(right)
    if not a < b:
        raise CertificateError("cell must have positive width")
    return {
        "cell": [qstr(a), qstr(b)],
        "physical_dispersion": "omega(p)=sqrt(1+p^2)+1/4",
        "strict_convexity": "omega''(p)=(1+p^2)^(-3/2)>0",
        "cell_indicator_space_conforming": True,
        "cell_indicator_space_reduces_free_multiplication": False,
        "Q_H0_P_nonzero": True,
        "ritz_compression_supplies_upper_data_only": True,
        "free_complement_floor_alone_supplies_full_count": False,
    }


def chart_metric(*, contraction_upper: Any) -> dict[str, Any]:
    """Return exact physical Gram bounds for S=(1-G)^-1."""
    contraction = q(contraction_upper)
    if not 0 <= contraction < 1:
        raise CertificateError("chart contraction must lie in [0,1)")
    lower = 1 / (1 + contraction) ** 2
    upper = 1 / (1 - contraction) ** 2
    return {
        "regular_pencil": "R-zM",
        "physical_metric": "M=S* S",
        "metric_lower": qstr(lower),
        "metric_upper": qstr(upper),
        "physical_trial_space": "S times the free cylinder space",
        "physical_complement": "M-orthogonal complement in regular coordinates",
        "free_Hilbert_complement_is_substitutable": False,
    }


def separated_auxiliary_budget(
    *, auxiliary_shift: Any, inverse_chart_bound: Any, physical_shift: Any
) -> dict[str, Any]:
    """Expose the loss from norm-bounding the +/-lambda pieces separately.

    In ``R=(H0+lambda)+S*[-lambda I-X]S`` the displayed lower budget keeps
    only ``H0>=0`` and the identity-piece norm bound.  A nonpositive result
    proves only that this separated estimate cannot establish coercivity; it
    is not a lower bound sharp enough to diagnose the physical spectrum.
    """
    lam, alpha, shift = q(auxiliary_shift), q(inverse_chart_bound), q(physical_shift)
    if lam <= 0 or alpha < 1 or shift < 0:
        raise CertificateError("lambda must be positive, inverse bound at least one, and physical shift nonnegative")
    budget = lam + shift - lam * alpha * alpha
    return {
        "auxiliary_lambda": qstr(lam),
        "inverse_chart_bound": qstr(alpha),
        "physical_shift": qstr(shift),
        "identity_piece_only_lower_budget": qstr(budget),
        "separated_norm_route_certifies_positive_coercivity": budget > 0,
        "combined_fixed_form_must_preserve_lambda_cancellation": True,
        "negative_budget_proves_operator_unbounded_below": False,
    }


def m_orthogonal_complement(metric: list[list[Fraction]], trial: list[Fraction]) -> list[list[Fraction]]:
    normal = matvec(metric, trial)
    pivot = next((i for i, value in enumerate(normal) if value), None)
    if pivot is None:
        raise CertificateError("trial has zero metric norm")
    columns: list[list[Fraction]] = []
    for index in range(len(trial)):
        if index == pivot:
            continue
        vector = [Fraction(0) for _ in trial]
        vector[index] = normal[pivot]
        vector[pivot] = -normal[index]
        if dot(normal, vector) != 0:
            raise AssertionError("internal M-orthogonal complement construction failed")
        columns.append(vector)
    return columns


def generalized_complement_count(
    *, regular_form: Sequence[Sequence[Any]], metric: Sequence[Sequence[Any]],
    trial: Sequence[Any], threshold: Any,
) -> dict[str, Any]:
    """Certify one generalized eigenvalue below a threshold by congruence.

    If the trial Rayleigh quotient is below b and ``R-bM`` is positive on the
    M-orthogonal complement, exact Schur congruence gives inertia (1,0,n-1).
    """
    regular, gram = symmetric(regular_form), symmetric(metric)
    if len(regular) != len(gram):
        raise CertificateError("regular form and metric dimensions differ")
    vector = [q(value) for value in trial]
    if len(vector) != len(regular) or not any(vector):
        raise CertificateError("trial must be a nonzero vector of the pencil dimension")
    if K150.inertia(gram) != (0, 0, len(gram)):
        raise CertificateError("metric must be positive definite")
    b = q(threshold)
    gram_norm = bilinear(vector, gram, vector)
    rayleigh = bilinear(vector, regular, vector) / gram_norm
    if rayleigh >= b:
        raise CertificateError("trial Rayleigh quotient must lie strictly below threshold")
    shifted = subtract_scaled(regular, b, gram)
    complement = m_orthogonal_complement(gram, vector)
    exterior = congruence(shifted, complement)
    if K150.inertia(exterior) != (0, 0, len(exterior)):
        raise CertificateError("complete M-orthogonal complement is not positive at threshold")
    full_inertia = K150.inertia(shifted)
    if full_inertia != (1, 0, len(regular) - 1):
        raise AssertionError("generalized Schur count disagrees with exact full inertia")
    return {
        "threshold": qstr(b),
        "trial_generalized_rayleigh": qstr(rayleigh),
        "metric_positive_definite": True,
        "complement_kind": "M-orthogonal",
        "complement_shifted_inertia": list(K150.inertia(exterior)),
        "full_pencil_inertia": list(full_inertia),
        "generalized_eigenvalue_count_below_threshold": 1,
        "coupling_may_be_nonzero": True,
    }


def absolute_anchor_guard(*, cutoff_to_limit_tail_ref: str | None, absolute_anchor_ref: str | None) -> dict[str, Any]:
    if not cutoff_to_limit_tail_ref:
        raise CertificateError("a cutoff-to-limit tail reference is required")
    if not absolute_anchor_ref:
        raise CertificateError("K161 tail is not an absolute anchor regular-core bound")
    return {
        "cutoff_to_limit_tail_ref": cutoff_to_limit_tail_ref,
        "absolute_anchor_ref": absolute_anchor_ref,
        "roles_distinct": True,
    }


def same_form_packet(**refs: str | None) -> dict[str, Any]:
    required = (
        "fixed_regular_form_ref",
        "physical_metric_ref",
        "anchor_coercivity_ref",
        "trial_form_and_gram_ref",
        "form_dual_residual_ref",
        "M_orthogonal_complement_or_flux_ref",
        "next_distinct_floor_ref",
        "native_left_floor_ref",
        "signed_charge_intertwiner_ref",
    )
    missing = [name for name in required if not refs.get(name)]
    return {
        "required_native_references": list(required),
        "missing_native_references": missing,
        "native_same_form_packet_complete": not missing,
        "native_ground_count_emitted": False,
        "native_K152_interval_emitted": False,
    }


def demo() -> dict[str, Any]:
    regular = [[-2, 1, 1], [1, 6, 0], [1, 0, 5]]
    metric = [[2, 1, 0], [1, 2, 0], [0, 0, 1]]
    try:
        absolute_anchor_guard(
            cutoff_to_limit_tail_ref="K161#complete-five-tail-bound",
            absolute_anchor_ref=None,
        )
    except CertificateError as exc:
        tail_role_failure = str(exc)
    else:
        raise AssertionError("tail-only anchor unexpectedly admitted")
    return {
        "schema_version": "1.0",
        "arithmetic": "exact_rational_congruence_plus_analytic_strict_convexity",
        "dyadic_free_reduction": physical_cell_reduction_obstruction(0, 1),
        "K139_chart_metric": chart_metric(contraction_upper=Fraction(3, 8)),
        "auxiliary_cancellation_budget": separated_auxiliary_budget(
            auxiliary_shift=256, inverse_chart_bound=Fraction(8, 5), physical_shift=6
        ),
        "generalized_schur_positive_control": generalized_complement_count(
            regular_form=regular, metric=metric, trial=[1, 0, 0], threshold=0
        ),
        "K161_tail_role_failure": tail_role_failure,
        "native_same_form_replay": same_form_packet(
            fixed_regular_form_ref="K139+K156#fixed-normal-ordered-form",
            physical_metric_ref="K153#M=S-star-S",
            anchor_coercivity_ref=None,
            trial_form_and_gram_ref=None,
            form_dual_residual_ref=None,
            M_orthogonal_complement_or_flux_ref=None,
            next_distinct_floor_ref=None,
            native_left_floor_ref=None,
            signed_charge_intertwiner_ref="K162#signed-flavor-transport",
        ),
        "route_verdict": "FREE_GAP_PASTE_REFUSED__GENERALIZED_SAME_FORM_COMPLEMENT_OR_LEHMANN_GOERISCH_REQUIRED",
        "physical_or_source_selection": False,
        "Born_prediction_or_confirmation_credit": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if not args.demo:
        parser.error("use --demo")
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
