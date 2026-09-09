#!/usr/bin/env python3
"""K173 same-graph tail obstruction and fractional-domain replacement interface."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from typing import Any


class CertificateError(ValueError):
    """Raised when a claimed graph-tail certificate mixes incompatible data."""


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def self_energy_lower(e: float, auxiliary_shift: int = 256) -> float:
    """Rigorous lower bound for D_lambda(e), valid for e >= lambda + 1.

    On lambda <= |k| <= e, omega(k) <= |k|+1 and
    omega(k)+lambda+e <= 3e.  Symmetry then gives the displayed logarithm.
    """
    if auxiliary_shift <= 0 or e < auxiliary_shift + 1:
        raise CertificateError("lower bound requires e >= lambda+1 > 1")
    return math.log((e + auxiliary_shift + 1) / (2 * auxiliary_shift + 1)) / (3 * math.pi)


def self_energy_upper(e: float, auxiliary_shift: int = 256) -> float:
    """K172's pointwise upper bound."""
    if auxiliary_shift <= 0 or e < 1:
        raise CertificateError("positive shift and physical energy are required")
    return math.log1p(e / auxiliary_shift) / math.pi


def fractional_subblock_bound(*, multiplicity: int, exponent: Fraction = Fraction(1, 4),
                              auxiliary_shift: int = 256) -> dict[str, Any]:
    """Bound the K172 one-bath diagonal block on an omega^s graph.

    log(1+t) <= t^s/s for 0<s<=1.  At s=1/4 and lambda=256 this gives
    D_256(e) <= e^(1/4)/pi.  This covers only the named diagonal subblock;
    it is deliberately not promoted to a complete Fock-space W bound.
    """
    if not 0 < exponent <= 1:
        raise CertificateError("fractional exponent must lie in (0,1]")
    if multiplicity not in (1, 2):
        raise CertificateError("K173 covers the K172 multiplicities one and two")
    if exponent != Fraction(1, 4) or auxiliary_shift != 256:
        raise CertificateError("K173 fixes the K159 quarter graph at lambda=256")
    return {
        "exponent": qstr(exponent),
        "point_vector_in_domain": True,
        "D_weight_coefficient_upper": "1/pi",
        "one_bath_diagonal_block_bound": f"256+{multiplicity}/pi",
        "complete_Fock_W_bound": False,
        "complete_Fock_G_contraction": False,
    }


def validate_same_graph_certificate(certificate: dict[str, Any]) -> None:
    """Reject certificates that splice contraction and action bounds across graphs."""
    required = ("domain_id", "norm_id", "q_D", "B", "seed_graph_norm")
    if any(key not in certificate for key in required):
        raise CertificateError("same domain, norm, q_D, B and seed norm are required")
    if certificate.get("q_domain_id", certificate["domain_id"]) != certificate["domain_id"]:
        raise CertificateError("q_D comes from a different graph domain")
    if certificate.get("B_domain_id", certificate["domain_id"]) != certificate["domain_id"]:
        raise CertificateError("B comes from a different graph domain")
    q_d = Fraction(str(certificate["q_D"]))
    b = Fraction(str(certificate["B"]))
    c = Fraction(str(certificate["seed_graph_norm"]))
    if not 0 <= q_d < 1 or b <= 0 or c <= 0:
        raise CertificateError("finite positive B,c and q_D in [0,1) are required")


def demo() -> dict[str, Any]:
    sample_energies = [1024.0, 1048576.0, 1073741824.0]
    lowers = [self_energy_lower(e) for e in sample_energies]
    uppers = [self_energy_upper(e) for e in sample_energies]
    if not all(0 < lo < hi for lo, hi in zip(lowers, uppers)):
        raise AssertionError("self-energy sandwich control failed")
    if not all(a < b for a, b in zip(lowers, lowers[1:])):
        raise AssertionError("lower bound must expose logarithmic growth")

    valid_control = {
        "domain_id": "abstract_control_graph",
        "norm_id": "graph_norm_v1",
        "q_D": "1/2",
        "B": "2",
        "seed_graph_norm": "1",
    }
    validate_same_graph_certificate(valid_control)
    mixed_rejected = False
    try:
        validate_same_graph_certificate({
            **valid_control,
            "q_domain_id": "particle_number_graph",
            "B_domain_id": "free_energy_graph",
        })
    except CertificateError:
        mixed_rejected = True

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {"auxiliary_chart_shift": 256, "Hilbert_contraction_upper": "3/8"},
        "free_energy_graph": {
            "domain": "Dom(H0)",
            "point_profile": "h=(2*pi)^(-1/2)/(omega+256)",
            "omega_h_in_L2": False,
            "G_maps_domain_to_itself": False,
            "finite_q_D": False,
            "verdict": "K158_ROUTE_KILL_REPLAYED",
        },
        "particle_number_graph": {
            "domain": "Dom(N+1)",
            "G_contraction_upper": qstr(Fraction(3, 4)),
            "D_lower_bound": "D_256(e)>=(1/(3*pi))*log((e+257)/513) for e>=257",
            "lower_bound_unbounded": True,
            "one_bath_W_multiplier": "-256+m*D_256(omega)",
            "W_graph_to_H_bounded": False,
            "finite_B": False,
        },
        "self_energy_growth_control": {
            "energies": [str(int(e)) for e in sample_energies],
            "lower_values": [f"{value:.12f}" for value in lowers],
            "upper_values": [f"{value:.12f}" for value in uppers],
            "strictly_increasing_lower": True,
        },
        "same_graph_contract": {
            "requires_domain_id": True,
            "requires_norm_id": True,
            "mixing_q_D_and_B_across_graphs_rejected": mixed_rejected,
            "abstract_positive_control_accepted": True,
            "native_K172_tail_admitted": False,
        },
        "fractional_replacement": {
            "candidate_domain": "Dom(dGamma(omega)^(1/4)+N+1)",
            "vacuum_transition": fractional_subblock_bound(multiplicity=1),
            "one_impurity_transition": fractional_subblock_bound(multiplicity=2),
            "requires_complete_Fock_commutator_and_normal_ordered_block_bounds": True,
            "native_numerical_q_quarter_serialized": False,
            "native_complete_B_quarter_serialized": False,
        },
        "release_test": {
            "requested_native_q_D_and_B_on_one_proved_graph": False,
            "complete_native_all_order_vector_tail_serialized": False,
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
    args = parser.parse_args()
    if not args.demo:
        parser.error("use --demo")
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
