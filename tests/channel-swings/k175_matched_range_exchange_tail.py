#!/usr/bin/env python3
"""K175 matched-range tail audit and scalar-metric resummation.

The K172 resolvent difference controls the diagonal Pauli/spectator block on
the K174 quarter graph.  It does not, by itself, control the four exchange
blocks: their isolated point traces are unbounded and an all-order estimate
must be proved only after the complete coefficient-level cancellation is
written.  This certificate keeps those two statements separate.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Any


Q_D = Fraction(131, 300)
Q_H = Fraction(3, 8)


class CertificateError(ValueError):
    """Raised when an action-tail claim omits a required native premise."""


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def matched_difference_identity() -> dict[str, Any]:
    """Serialize the exact K172 subtraction and its quarter-weight bound."""
    return {
        "identity": "1/(a+e)-1/a=-e/(a*(a+e))",
        "a": "omega(k)+256",
        "D_definition": "D_256(e)=int_R e/((omega(k)+256)*(omega(k)+256+e)) dk/(2*pi)",
        "pointwise_upper": "D_256(e)<=(1/pi)*e^(1/4)<=(1/3)*e^(1/4)",
        "matched_before_limit": True,
        "isolated_exchange_trace_bounded": False,
    }


def diagonal_tail(resolved_order: int, multiplicity: int = 2) -> Fraction:
    """Post-left-adjoint tail for the matched diagonal remainder.

    K172 gives D_256(e)<=e^(1/4)/pi.  K174 gives the graph-orbit bound
    ||A_(1/4) G^n phi|| <= q_D^n for either normalized zero-bath K162 seed.
    With multiplicity at most two and pi>3, beta=2/3 is rigorous.
    """
    if resolved_order < 0:
        raise CertificateError("resolved order must be nonnegative")
    if not 1 <= multiplicity <= 2:
        raise CertificateError("native diagonal multiplicity must be one or two")
    beta = Fraction(multiplicity, 3)
    return beta * Q_D ** (resolved_order + 1) / ((1 - Q_D) * (1 - Q_H))


def metric_tail(word_order: int, scalar_size: int = 256) -> Fraction:
    """Bound |-scalar_size*(M-S_J* S_J)| for S=(1-G)^-1.

    ||S-S_J||<=q_H^(J+1)/(1-q_H) and both inverse sums are bounded by
    1/(1-q_H), hence ||M-S_J* S_J||<=2q_H^(J+1)/(1-q_H)^2.
    """
    if word_order < 0 or scalar_size <= 0:
        raise CertificateError("nonnegative word order and positive scalar size required")
    return 2 * scalar_size * Q_H ** (word_order + 1) / (1 - Q_H) ** 2


def validate_exchange_tail_certificate(certificate: dict[str, Any]) -> Fraction:
    """Accept only a complete coefficient-level exchange cancellation proof."""
    required = (
        "seed_ids",
        "coefficient_family_id",
        "first_unresolved_order",
        "beta",
        "ratio",
        "q_H",
        "complete_coefficient_formula_all_orders",
        "matched_counterterm_before_limit",
        "cross_exchange_cancellation_identity",
        "sector_uniform_CAR_bound",
    )
    if any(key not in certificate for key in required):
        raise CertificateError("complete exchange-coefficient provenance and estimates are required")
    gates = (
        "complete_coefficient_formula_all_orders",
        "matched_counterterm_before_limit",
        "cross_exchange_cancellation_identity",
        "sector_uniform_CAR_bound",
    )
    if any(certificate[key] is not True for key in gates):
        raise CertificateError("isolated or finitely checked exchange blocks do not certify the native tail")
    beta = Fraction(str(certificate["beta"]))
    ratio = Fraction(str(certificate["ratio"]))
    q_h = Fraction(str(certificate["q_H"]))
    order = int(certificate["first_unresolved_order"])
    if beta <= 0 or not 0 <= ratio < 1 or not 0 <= q_h < 1 or order < 0:
        raise CertificateError("positive beta, geometric ratios below one and a nonnegative order are required")
    return beta * ratio**order / ((1 - ratio) * (1 - q_h))


def demo() -> dict[str, Any]:
    positive = {
        "seed_ids": ["abstract_vacuum"],
        "coefficient_family_id": "abstract_complete_exchange_family",
        "first_unresolved_order": 2,
        "beta": "1/64",
        "ratio": "3/8",
        "q_H": "3/8",
        "complete_coefficient_formula_all_orders": True,
        "matched_counterterm_before_limit": True,
        "cross_exchange_cancellation_identity": True,
        "sector_uniform_CAR_bound": True,
    }
    positive_tail = validate_exchange_tail_certificate(positive)
    rejected: dict[str, bool] = {}
    for key in (
        "complete_coefficient_formula_all_orders",
        "cross_exchange_cancellation_identity",
        "sector_uniform_CAR_bound",
    ):
        try:
            validate_exchange_tail_certificate({**positive, key: False})
        except CertificateError:
            rejected[key] = True

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "auxiliary_chart_shift": 256,
            "quarter_graph_ratio": qstr(Q_D),
            "Hilbert_ratio": qstr(Q_H),
            "seed_graph_norm": "1 for each normalized K162 zero-bath seed",
        },
        "matched_range": matched_difference_identity(),
        "diagonal_orbit_tail": {
            "multiplicity_upper": 2,
            "coefficient_beta_upper": "2/3",
            "tail_after_order_1": qstr(diagonal_tail(1)),
            "tail_after_order_1_expected": "68644/190125",
            "all_order_diagonal_tail_serialized": True,
        },
        "scalar_metric_resummation": {
            "identity": "-256*S* S",
            "finite_approximant": "-256*S_J* S_J, S_J=sum_(j=0)^J G^j",
            "error_at_J_12": qstr(metric_tail(12)),
            "error_at_J_12_expected": "1594323/419430400",
            "convergent": True,
        },
        "exchange_tail_audit": {
            "componentwise_four_over_pi_shortcut_valid": False,
            "reason": "the K172 D_256 multiplier is the diagonal matched block; each isolated exchange point trace remains unbounded by K174",
            "required_cross_term_identity_serialized": False,
            "required_sector_uniform_CAR_bound_serialized": False,
            "abstract_positive_control_tail": qstr(positive_tail),
            "abstract_positive_control_expected": "9/1600",
            "missing_native_premises_rejected": all(rejected.values()),
            "native_complete_exchange_tail_serialized": False,
        },
        "release_test": {
            "scalar_core_action_column_convergent": True,
            "matched_diagonal_action_column_convergent": True,
            "coefficient_complete_exchange_action_column_serialized": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
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
