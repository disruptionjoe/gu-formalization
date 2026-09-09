#!/usr/bin/env python3
"""K174 diagonal-weight/point-trace reciprocity obstruction.

The K139 boundary chart creates the dressed point profile
``h=(2*pi)^(-1/2)/(omega+256)``.  A nonzero K156 exchange block contains an
unsmeared point annihilation trace.  On a one-particle multiplication-weight
graph these requirements are reciprocal and cannot both be bounded.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from typing import Any


class CertificateError(ValueError):
    """Raised when a direct orbit-tail claim omits a required premise."""


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def quarter_graph_boundary_certificate() -> dict[str, Any]:
    """Rigorous conservative contraction bound in one fixed graph norm.

    Use A=(dGamma(omega))^(1/4)+N+1 and ||psi||_D=||A psi||.  For one
    dressed creation channel, pull-through and subadditivity give the bound
    3||h||+||omega^(1/4)h||.  The two-edge C3 control has at most two
    mutually orthogonal outgoing channels.
    """
    # ||h||^2 <= 1/(256*pi) < 1/768 < (1/27)^2.
    if not Fraction(1, 768) < Fraction(1, 27) ** 2:
        raise AssertionError("unweighted outward comparison changed")
    # ||omega^(1/4)h||^2 < 1/(2*sqrt(255)) < 1/31 < (9/50)^2.
    if not Fraction(31, 2) ** 2 < 255 or not Fraction(1, 31) < Fraction(9, 50) ** 2:
        raise AssertionError("quarter-weight outward comparison changed")
    h_upper = Fraction(1, 27)
    weighted_h_upper = Fraction(9, 50)
    sqrt_two_upper = Fraction(3, 2)
    contraction_upper = sqrt_two_upper * (3 * h_upper + weighted_h_upper)
    if contraction_upper != Fraction(131, 300) or contraction_upper >= 1:
        raise AssertionError("quarter-graph contraction arithmetic changed")
    return {
        "domain": "Dom((dGamma(omega))^(1/4)+N+1)",
        "norm": "||(dGamma(omega))^(1/4)psi+(N+1)psi||",
        "h_norm_upper": qstr(h_upper),
        "quarter_weighted_h_norm_upper": qstr(weighted_h_upper),
        "outgoing_channel_multiplicity_upper": 2,
        "sqrt_two_upper": qstr(sqrt_two_upper),
        "G_graph_contraction_upper": qstr(contraction_upper),
        "G_graph_contraction_strict": True,
    }


def reciprocity_lower(radius: float, start: float = 257.0) -> float:
    """Lower bound for the product of boundary and trace integrals.

    For p>=257, omega(p)+256 <= 2p.  Cauchy--Schwarz on [257,R]
    gives H_R*T_R >= log(R/257)^2/4 for every positive weight a.
    """
    if radius <= start or start < 257:
        raise CertificateError("use R>start>=257")
    return math.log(radius / start) ** 2 / 4


def power_weight_classification(exponent: Fraction) -> dict[str, Any]:
    if exponent < 0:
        raise CertificateError("nonnegative exponents only")
    return {
        "exponent": qstr(exponent),
        "boundary_profile_in_graph": exponent < Fraction(1, 2),
        "point_trace_continuous": exponent > Fraction(1, 2),
        "both": False,
        "endpoint_half_has_two_logarithmic_divergences": exponent == Fraction(1, 2),
    }


def validate_orbit_tail_certificate(certificate: dict[str, Any]) -> Fraction:
    """Return K171's post-adjoint tail from a supplied native sequence bound."""
    required = (
        "seed_id", "operator_id", "coefficient_family_id", "first_unresolved_order",
        "beta", "ratio", "q_H", "all_orders_proved", "cancellation_complete",
    )
    if any(key not in certificate for key in required):
        raise CertificateError("complete coefficient-specific provenance and tail data are required")
    if certificate["all_orders_proved"] is not True or certificate["cancellation_complete"] is not True:
        raise CertificateError("finite prefixes or uncancelled exchange factors do not certify the native tail")
    beta = Fraction(str(certificate["beta"]))
    ratio = Fraction(str(certificate["ratio"]))
    q_h = Fraction(str(certificate["q_H"]))
    order = int(certificate["first_unresolved_order"])
    if beta <= 0 or not 0 <= ratio < 1 or not 0 <= q_h < 1 or order < 0:
        raise CertificateError("positive beta, geometric ratios below one and a nonnegative order are required")
    return beta * ratio**order / ((1 - ratio) * (1 - q_h))


def demo() -> dict[str, Any]:
    quarter = quarter_graph_boundary_certificate()
    radii = [257.0 * math.exp(k) for k in (2, 4, 8)]
    product_lowers = [reciprocity_lower(radius) for radius in radii]
    if not product_lowers[0] < product_lowers[1] < product_lowers[2]:
        raise AssertionError("reciprocity product must diverge")

    positive_control = {
        "seed_id": "abstract_seed",
        "operator_id": "abstract_W_G",
        "coefficient_family_id": "abstract_geometric_family",
        "first_unresolved_order": 2,
        "beta": "1/64",
        "ratio": "3/8",
        "q_H": "3/8",
        "all_orders_proved": True,
        "cancellation_complete": True,
    }
    positive_tail = validate_orbit_tail_certificate(positive_control)
    native_rejected = False
    try:
        validate_orbit_tail_certificate({**positive_control, "all_orders_proved": False})
    except CertificateError:
        native_rejected = True

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "auxiliary_chart_shift": 256,
            "boundary_profile": "h=(2*pi)^(-1/2)/(omega+256)",
            "nonzero_exchange_factor": "a*(h) a(delta) on an isolated edge/polarity channel",
        },
        "quarter_graph": {
            **quarter,
            "named_diagonal_self_energy_block_bounded": True,
            "point_trace_continuous": False,
            "complete_W_graph_to_Hilbert_bounded": False,
        },
        "weight_trace_reciprocity": {
            "boundary_requirement": "a*h in L2",
            "exchange_trace_requirement": "1/a in L2",
            "finite_interval_product_lower": "H_R*T_R >= log(R/257)^2/4",
            "sample_radii": [f"257*exp({k})" for k in (2, 4, 8)],
            "sample_product_lowers": [f"{value:.12f}" for value in product_lowers],
            "no_positive_diagonal_weight_satisfies_both": True,
            "power_controls": [
                power_weight_classification(Fraction(1, 4)),
                power_weight_classification(Fraction(1, 2)),
                power_weight_classification(Fraction(3, 4)),
            ],
            "finite_logarithmic_weights_admit_boundary_but_not_trace": True,
            "non_diagonal_or_cancellation_adapted_domains_ruled_out": False,
        },
        "orbit_tail_interface": {
            "requires_complete_renormalized_vectors_not_separate_singular_factors": True,
            "abstract_positive_control_tail": qstr(positive_tail),
            "abstract_positive_control_expected": "9/1600",
            "native_finite_prefix_rejected": native_rejected,
            "native_all_order_coefficient_tail_serialized": False,
        },
        "release_test": {
            "coefficient_complete_base_R0_action_column_serialized": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "native_left_floor_at_selected_scalar_center_serialized": False,
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
