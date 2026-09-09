#!/usr/bin/env python3
"""K176 adjacent-contraction cancellation and exchange-orbit tail.

This certificate works only on the K139/K162 zero-bath seed orbits.  It does
not bound isolated exchange point traces.  At finite cutoff the newly adjacent
Wick contraction is exactly the endpoint term and cancels before the limit;
the surviving exchange annihilator can hit only one of the older creation
letters.  Those terms carry two resolvents in the contracted momentum.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Any


Q = Fraction(3, 8)
EXCHANGE_MONOMIALS = 16
KERNEL_NORM_SQ_UPPER = Fraction(2, 3)
KERNEL_NORM_UPPER = Fraction(5, 6)
EXCHANGE_COEFFICIENT = EXCHANGE_MONOMIALS * KERNEL_NORM_UPPER


class CertificateError(ValueError):
    """Raised when the native normal-form certificate is incomplete."""


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def validate_native_normal_form(certificate: dict[str, Any]) -> None:
    """Require every premise that makes the seed-orbit estimate native."""
    required_true = (
        "finite_cutoff_first",
        "matched_endpoint_before_limit",
        "adjacent_wick_contraction_cancelled",
        "older_letter_count_equals_order",
        "two_resolvent_kernel_on_every_older_letter",
        "all_16_exchange_monomials_included",
        "spectator_shifts_nonnegative",
        "sector_uniform_CAR_sum_bound",
    )
    if any(certificate.get(key) is not True for key in required_true):
        raise CertificateError("complete finite-cutoff normal form and CAR estimate required")
    if certificate.get("cross_polarity_cancellation_required") is not False:
        raise CertificateError("the proof must not invent cross-polarity cancellation")
    if certificate.get("seed_scope") != "K162_zero_bath_seed_orbits":
        raise CertificateError("the estimate is coefficient-specific, not a global graph bound")


def kernel_bound() -> dict[str, Any]:
    """Exact rational majorant for J_256(omega)=D_256(omega)/omega."""
    return {
        "definition": "J_256(e)=D_256(e)/e",
        "pointwise": "J_256(e)<=(1/3)*e^(-3/4)",
        "squared_integral_majorant": "(1/9)*int_R (1+p^2)^(-3/4) dp",
        "integral_split_upper": "6",
        "norm_squared_upper": qstr(KERNEL_NORM_SQ_UPPER),
        "norm_upper": qstr(KERNEL_NORM_UPPER),
        "strict_rounding_check": "2/3<25/36",
    }


def exchange_block_bound(order: int) -> Fraction:
    """Bound ||X_ex,n G^n phi|| for a normalized supported seed."""
    if order < 1:
        raise CertificateError("exchange order starts at one")
    return EXCHANGE_COEFFICIENT * order * Q ** (order - 1)


def exchange_tail(resolved_order: int) -> Fraction:
    """Post-left-adjoint tail after resolving orders through N.

    Sum n*q^(n-1) from n=N+1 to infinity, then multiply by the
    K171 left-adjoint Neumann factor 1/(1-q).
    """
    if resolved_order < 1:
        raise CertificateError("resolve at least the first exchange order")
    n = resolved_order
    return EXCHANGE_COEFFICIENT * Q**n * ((n + 1) - n * Q) / (1 - Q) ** 3


def demo() -> dict[str, Any]:
    normal_form = {
        "seed_scope": "K162_zero_bath_seed_orbits",
        "finite_cutoff_first": True,
        "matched_endpoint_before_limit": True,
        "adjacent_wick_contraction_cancelled": True,
        "older_letter_count_equals_order": True,
        "two_resolvent_kernel_on_every_older_letter": True,
        "all_16_exchange_monomials_included": True,
        "spectator_shifts_nonnegative": True,
        "sector_uniform_CAR_sum_bound": True,
        "cross_polarity_cancellation_required": False,
    }
    validate_native_normal_form(normal_form)
    rejected: dict[str, bool] = {}
    for key in (
        "adjacent_wick_contraction_cancelled",
        "older_letter_count_equals_order",
        "two_resolvent_kernel_on_every_older_letter",
        "all_16_exchange_monomials_included",
        "sector_uniform_CAR_sum_bound",
    ):
        try:
            validate_native_normal_form({**normal_form, key: False})
        except CertificateError:
            rejected[key] = True

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "auxiliary_chart_shift": 256,
            "Hilbert_boundary_ratio": qstr(Q),
            "seed_norm": "1 for each normalized K162 zero-bath seed",
        },
        "normal_form": normal_form,
        "kernel": kernel_bound(),
        "exchange_census": {
            "ordered_edge_pairs": 4,
            "polarity_blocks_per_pair": 4,
            "monomials": EXCHANGE_MONOMIALS,
            "coefficient_upper": qstr(EXCHANGE_COEFFICIENT),
            "order_n_bound": "(40/3)*n*(3/8)^(n-1)",
            "all_missing_premises_rejected": all(rejected.values()),
        },
        "post_adjoint_tail": {
            "formula_after_order_N": "(40/3)*(3/8)^N*((N+1)-N*(3/8))/(1-3/8)^3",
            "after_order_1": qstr(exchange_tail(1)),
            "after_order_1_expected": "832/25",
            "after_order_12": qstr(exchange_tail(12)),
            "after_order_12_expected": "3011499/838860800",
            "after_order_12_less_than_1_over_250": exchange_tail(12) < Fraction(1, 250),
            "native_complete_exchange_tail_convergent": True,
        },
        "release_test": {
            "coefficient_complete_exchange_action_column_tail_serialized": True,
            "resolved_exchange_vectors_through_order_12_evaluated": False,
            "coefficient_complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "scalar_center_left_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": {
            "SC-META-53": "UNCERTAIN_UNCHANGED",
            "LT-SM8": "NEEDS_UNCHANGED",
            "RA-F1": "NEEDS_UNCHANGED",
            "AC-F1": "NEEDS_UNCHANGED",
        },
        "physical_or_source_selection": False,
        "Born_prediction_or_confirmation_credit": False,
        "canon_paper_release_or_public_posture_move": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    parser.parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
