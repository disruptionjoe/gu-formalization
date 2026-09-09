#!/usr/bin/env python3
"""K170 native one-vector Gram and reference-shape slice.

The fixed K139 boundary map raises bath-particle number by one.  Its Neumann
words are therefore mutually orthogonal on a fixed seed, which turns the
physical Gram into a sum of squared word norms.  This module evaluates the
first word for the native continuum point profile with exact rational outward
bounds and controls the untouched words by K153's q=3/8 contraction.

It evaluates the K168 reference-shape contribution, not the still-missing
combined K156 base regular form or complete K152 complement.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import isqrt
from typing import Any


class CertificateError(ValueError):
    """Raised when an interval or native-slice premise is malformed."""


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def decimal_outward(lower: Fraction, upper: Fraction, digits: int = 15) -> tuple[Fraction, Fraction]:
    """Coarsen a proved interval to compact decimal rationals, outward."""
    scale = 10**digits
    lower_integer = lower.numerator * scale // lower.denominator
    upper_integer = (upper.numerator * scale + upper.denominator - 1) // upper.denominator
    return Fraction(lower_integer, scale), Fraction(upper_integer, scale)


def sqrt_interval(value: Fraction, bits: int = 192) -> tuple[Fraction, Fraction]:
    if value <= 0 or bits < 8:
        raise CertificateError("positive radicand and at least eight bits are required")
    scale = 1 << bits
    floor_scaled = isqrt(value.numerator * scale * scale // value.denominator)
    while Fraction((floor_scaled + 1) ** 2, scale * scale) <= value:
        floor_scaled += 1
    while Fraction(floor_scaled**2, scale * scale) > value:
        floor_scaled -= 1
    lower = Fraction(floor_scaled, scale)
    upper = Fraction(floor_scaled + 1, scale)
    return decimal_outward(lower, upper)


def log_interval(value: Fraction, terms: int = 80) -> tuple[Fraction, Fraction]:
    """Bound log(value) by range reduction and the positive atanh series."""
    if value <= 0 or terms < 1:
        raise CertificateError("positive logarithm argument and terms are required")
    k = 0
    y = value
    while y >= 2:
        y /= 2
        k += 1
    while y < 1:
        y *= 2
        k -= 1

    def unit_log_bounds(argument: Fraction) -> tuple[Fraction, Fraction]:
        z = (argument - 1) / (argument + 1)
        if not 0 <= z <= Fraction(1, 3):
            raise AssertionError("range reduction left the convergent log interval")
        partial = 2 * sum((z ** (2 * n + 1) / (2 * n + 1) for n in range(terms)), Fraction())
        next_power = 2 * terms + 1
        remainder = 2 * z**next_power / (next_power * (1 - z * z))
        return partial, partial + remainder

    y_lower, y_upper = unit_log_bounds(y)
    two_lower, two_upper = unit_log_bounds(Fraction(2))
    if k >= 0:
        return y_lower + k * two_lower, y_upper + k * two_upper
    return y_lower + k * two_upper, y_upper + k * two_lower


def point_profile_norm_sq_interval() -> tuple[Fraction, Fraction]:
    """Bound one transition's ||(H0+256)^-1 delta||^2 on L2(R).

    With a=256 and d=sqrt(a^2-1), hyperbolic substitution gives

      (2*pi)^-1 int_R dp/(sqrt(1+p^2)+a)^2
        = (a*d-acosh(a))/(pi*d^3).
    """
    a = Fraction(256)
    d_lower, d_upper = sqrt_interval(a * a - 1)
    acosh_lower, _ = log_interval(a + d_lower)
    _, acosh_upper = log_interval(a + d_upper)
    pi_lower = Fraction(333, 106)
    pi_upper = Fraction(355, 113)
    numerator_lower = a * d_lower - acosh_upper
    numerator_upper = a * d_upper - acosh_lower
    if numerator_lower <= 0:
        raise AssertionError("profile integral lower numerator is not positive")
    lower = numerator_lower / (pi_upper * d_upper**3)
    upper = numerator_upper / (pi_lower * d_lower**3)
    if not 0 < lower < upper:
        raise AssertionError("invalid outward profile interval")
    return decimal_outward(lower, upper)


def seed_slice(*, charge: tuple[int, int], first_word_multiplicity: int) -> dict[str, Any]:
    if charge not in ((0, 0), (1, 0), (0, 1)):
        raise CertificateError("K170 supports only the native representative charge orbit")
    if first_word_multiplicity not in (1, 2):
        raise CertificateError("first-word multiplicity must be one or two")
    if charge == (0, 0) and first_word_multiplicity != 2:
        raise CertificateError("the vacuum has two allowed first impurity transitions")
    if charge != (0, 0) and first_word_multiplicity != 1:
        raise CertificateError("a one-impurity seed has one allowed first transition")

    one_lower, one_upper = point_profile_norm_sq_interval()
    g_lower = first_word_multiplicity * one_lower
    g_upper = first_word_multiplicity * one_upper
    contraction = Fraction(3, 8)
    tail = contraction**4 / (1 - contraction**2)
    gram_lower = 1 + g_lower
    gram_upper = 1 + g_upper + tail

    minority_lower = g_lower / (1 + g_lower + tail)
    minority_upper = (g_upper + tail) / (1 + g_upper + tail)
    if minority_upper >= Fraction(1, 2):
        raise AssertionError("minority-weight monotonicity branch changed")

    if charge == (0, 0):
        seed_impurity_value = -2
        first_word_impurity_value = 1
        rayleigh_lower = -2 + 3 * minority_lower
        rayleigh_upper = -2 + 3 * minority_upper
        form_lower = Fraction(-2) + g_lower - 2 * tail
        form_upper = Fraction(-2) + g_upper + tail
        minority = "occupied_impurity"
    else:
        seed_impurity_value = 1
        first_word_impurity_value = -2
        rayleigh_lower = 1 - 3 * minority_upper
        rayleigh_upper = 1 - 3 * minority_lower
        form_lower = Fraction(1) - 2 * g_upper - 2 * tail
        form_upper = Fraction(1) - 2 * g_lower + tail
        minority = "vacuum_impurity"

    residual_sq_upper = 9 * minority_upper * (1 - minority_upper)
    return {
        "charge": list(charge),
        "seed": "Omega" if charge == (0, 0) else ("d_1^*Omega" if charge == (1, 0) else "d_2^*Omega"),
        "K162_membership": "zero-bath seed belongs to every dyadic cylinder level",
        "first_word_multiplicity": first_word_multiplicity,
        "first_word_norm_sq_interval": [qstr(g_lower), qstr(g_upper)],
        "uncomputed_squared_word_tail_upper": qstr(tail),
        "physical_Gram_interval": [qstr(gram_lower), qstr(gram_upper)],
        "seed_impurity_value": seed_impurity_value,
        "first_word_impurity_value": first_word_impurity_value,
        "minority_weight_kind": minority,
        "minority_probability_interval": [qstr(minority_lower), qstr(minority_upper)],
        "reference_shape_form_interval": [qstr(form_lower), qstr(form_upper)],
        "dressed_reference_shape_Rayleigh_interval": [qstr(rayleigh_lower), qstr(rayleigh_upper)],
        "matched_M_inverse_residual_sq_upper": qstr(residual_sq_upper),
        "reference_shape_only": True,
        "complete_R_ref_residual": False,
    }


def demo() -> dict[str, Any]:
    profile = point_profile_norm_sq_interval()
    q00 = seed_slice(charge=(0, 0), first_word_multiplicity=2)
    q10 = seed_slice(charge=(1, 0), first_word_multiplicity=1)
    q01 = seed_slice(charge=(0, 1), first_word_multiplicity=1)
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "arithmetic": "exact_rational_outward_hyperbolic_integral_and_squared_Neumann_tail",
        "fixed_control": {
            "auxiliary_chart_shift": 256,
            "dispersion": "sqrt(1+p^2)+1/4",
            "reference_shape": "diag(-2,1,1)",
            "boundary_contraction_upper": "3/8",
            "one_transition_profile_norm_sq_interval": [qstr(profile[0]), qstr(profile[1])],
        },
        "orthogonal_word_theorem": {
            "G_raises_bath_particle_number_by_exactly_one": True,
            "distinct_Neumann_words_on_a_seed_are_orthogonal": True,
            "physical_Gram_identity": "<phi,S* S phi>=sum_(n>=0)||G^n phi||^2",
            "tail_type": "squared_geometric",
            "tail_from_word_two_upper": qstr(Fraction(81, 3520)),
            "compressed_finite_chart_used": False,
        },
        "native_seed_slices": [q00, q10, q01],
        "signed_flavor_transport": {
            "q10_equals_q01": q10 == {**q01, "charge": [1, 0], "seed": "d_1^*Omega"},
            "requires_complete_signed_flavor_intertwiner": True,
            "particle_hole_complement_used": False,
        },
        "release_test": {
            "physical_Gram_seed_entries_evaluated": True,
            "reference_shape_seed_form_evaluated": True,
            "trial_specific_shape_residual_evaluated": True,
            "coefficient_complete_base_R0_action_serialized": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "native_left_floor_at_selected_scalar_center_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "physical_or_source_selection": False,
        "Born_prediction_or_confirmation_credit": False,
        "canon_paper_release_or_public_posture_move": False,
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
