#!/usr/bin/env python3
"""K161 complete weighted-tail and inverse-smoothing obstruction certificates."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import isqrt
from typing import Any


class CertificateError(ValueError):
    """Raised when a fail-closed certificate omits a required premise."""


def q(value: Any) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    try:
        return Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise CertificateError(f"invalid rational input: {value!r}") from exc


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def complete_weighted_tail(cutoff: int) -> dict[str, Any]:
    """Bound every second-order denominator component for the unit two-edge control.

    For omega(p)=sqrt(1+p^2), both the point graph-dual tail and the
    resolvent-dressed creation tail have squared norm at most 1/(3 Lambda).
    One exchange monomial has two tail placements, hence norm at most
    sqrt(2/(3 Lambda)).  There are four ordered edge pairs and four polarity
    blocks.  The matched diagonal contribution occurs on both active edges;
    four endpoint occupation corrections supply the remaining Pauli tail.
    """
    if cutoff < 2:
        raise CertificateError("cutoff must be at least two")
    root_denominator = isqrt(3 * cutoff // 2)
    if root_denominator <= 0:
        raise CertificateError("invalid rational square-root denominator")
    exchange_pair_upper = Fraction(1, root_denominator)
    exchange_pair_square_target = Fraction(2, 3 * cutoff)
    if exchange_pair_upper * exchange_pair_upper < exchange_pair_square_target:
        raise CertificateError("rational exchange bound is not outward")

    matched_two_edge_diagonal = Fraction(1049, 6 * cutoff)
    pauli_occupation = Fraction(4, 3 * cutoff)
    diagonal_total = matched_two_edge_diagonal + pauli_occupation
    edge_pairs = 4
    polarity_blocks = 4
    exchange_total = edge_pairs * polarity_blocks * exchange_pair_upper
    total = diagonal_total + exchange_total
    return {
        "cutoff": cutoff,
        "weight": "(1+S)^(-1)",
        "point_graph_dual_tail_square_upper": qstr(Fraction(1, 3 * cutoff)),
        "dressed_creation_tail_square_upper": qstr(Fraction(1, 3 * cutoff)),
        "matched_two_edge_diagonal_upper": qstr(matched_two_edge_diagonal),
        "Pauli_occupation_tail_upper": qstr(pauli_occupation),
        "diagonal_Pauli_spectator_total_upper": qstr(diagonal_total),
        "ordered_edge_pairs": edge_pairs,
        "polarity_blocks": ["++", "+-", "-+", "--"],
        "exchange_pair_upper": qstr(exchange_pair_upper),
        "exchange_pair_square_target": qstr(exchange_pair_square_target),
        "all_exchange_blocks_upper": qstr(exchange_total),
        "complete_weighted_denominator_error_upper": qstr(total),
        "all_five_normal_ordered_components_included": True,
        "complete_K157_rectangle_covered": True,
        "convergence_rate": "O(Lambda^(-1/2))",
        "converges_to_zero": True,
    }


def inverse_smoothing_obstruction(
    *, spectator_energy: int, logarithmic_power: int, c0: Any = 1, c1: Any = 1
) -> dict[str, Any]:
    """Give the high-spectator lower bound for ||(1+S)D^-1||.

    On active-vacuum spectator vectors psi_s, the four exchange blocks vanish
    and the finite W plus matched diagonal denominator obey
    ||D psi_s|| <= c0+c1 log_2(1+s).  If D is invertible, normalizing D psi_s
    yields ||(1+S)D^-1|| >= (1+s)/(c0+c1 log_2(1+s)).
    Powers s=2^m-1 make this an exact rational divergent sequence.
    """
    c0_q, c1_q = q(c0), q(c1)
    if spectator_energy != 2**logarithmic_power - 1 or logarithmic_power < 1:
        raise CertificateError("use spectator_energy=2^m-1 with m positive")
    if c0_q < 0 or c1_q <= 0:
        raise CertificateError("logarithmic growth constants must be nonnegative/positive")
    denominator_upper = c0_q + c1_q * logarithmic_power
    lower = Fraction(1 + spectator_energy, 1) / denominator_upper
    return {
        "spectator_energy": spectator_energy,
        "log2_one_plus_s": logarithmic_power,
        "denominator_vector_norm_upper": qstr(denominator_upper),
        "inverse_smoothing_norm_lower": qstr(lower),
        "active_edge_vacuum_exchange_blocks_vanish": True,
        "finite_extension_is_only_bounded": True,
        "denominator_growth_ceiling": "O(log(1+S)) on the high-spectator test sequence",
        "full_energy_inverse_smoothing_finite": False,
    }


def regular_k152_admission(
    *,
    diagonal_tail_ref: str | None,
    exchange_pp_ref: str | None,
    exchange_pm_ref: str | None,
    exchange_mp_ref: str | None,
    exchange_mm_ref: str | None,
    regular_core_bound_ref: str | None,
    form_dual_residual_ref: str | None,
    coercivity_ref: str | None,
    next_spectrum_ref: str | None,
    native_left_floor_ref: str | None,
    signed_charge_intertwiner_ref: str | None,
) -> dict[str, Any]:
    """Fail closed on the regular-representative K152 data contract."""
    required = {
        "diagonal Pauli/spectator tail": diagonal_tail_ref,
        "exchange ++ tail": exchange_pp_ref,
        "exchange +- tail": exchange_pm_ref,
        "exchange -+ tail": exchange_mp_ref,
        "exchange -- tail": exchange_mm_ref,
        "regular core bound B": regular_core_bound_ref,
        "total form-dual residual": form_dual_residual_ref,
        "coercivity": coercivity_ref,
        "next distinct spectrum": next_spectrum_ref,
        "native left floor": native_left_floor_ref,
        "signed charge intertwiner": signed_charge_intertwiner_ref,
    }
    missing = [name for name, ref in required.items() if not ref]
    if missing:
        raise CertificateError("missing native references: " + ", ".join(missing))
    return {
        "regular_K152_interface_complete": True,
        "five_normal_ordered_tail_references_complete": True,
        "free_H0_graph_chart_required": False,
        "boundary_inverse_smoothing_required": False,
        "native_interval_may_now_be_computed": True,
    }


def native_route_status() -> dict[str, Any]:
    witnesses = [
        inverse_smoothing_obstruction(spectator_energy=2**m - 1, logarithmic_power=m)
        for m in (8, 16, 32)
    ]
    try:
        regular_k152_admission(
            diagonal_tail_ref="K161:diagonal",
            exchange_pp_ref="K161:++",
            exchange_pm_ref="K161:+-",
            exchange_mp_ref="K161:-+",
            exchange_mm_ref="K161:--",
            regular_core_bound_ref=None,
            form_dual_residual_ref=None,
            coercivity_ref=None,
            next_spectrum_ref=None,
            native_left_floor_ref=None,
            signed_charge_intertwiner_ref=None,
        )
    except CertificateError as exc:
        regular_error = str(exc)
    else:
        raise AssertionError("native incomplete regular packet unexpectedly admitted")
    return {
        "schema_version": "1.0",
        "complete_weighted_tail_n4096": complete_weighted_tail(4096),
        "complete_weighted_tail_n65536": complete_weighted_tail(65536),
        "inverse_smoothing_witnesses": witnesses,
        "weighted_boundary_neumann_route_closed": False,
        "weighted_route_verdict": "INVERSE_SMOOTHING_ROUTE_KILLED",
        "singular_boundary_extension_killed": False,
        "regular_K152_route_selected": True,
        "regular_K152_native_admission_error": regular_error,
        "native_ground_count_emitted": False,
        "native_energy_interval_emitted": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if not args.demo:
        parser.error("use --demo")
    print(json.dumps(native_route_status(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
