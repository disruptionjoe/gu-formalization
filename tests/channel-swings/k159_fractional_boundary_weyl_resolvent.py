#!/usr/bin/env python3
"""K159 fractional-domain and boundary/Weyl resolvent certificates.

The sharp point boundary is compared through operator-valued Weyl data.
Nothing in this module promotes an abstract positive control to native GU
spectral data.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Any


class CertificateError(ValueError):
    """Raised when a requested certificate is missing a required premise."""


def q(value: Any) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError, TypeError) as exc:
        raise CertificateError(f"invalid rational input: {value!r}") from exc


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def fractional_point_domain(exponent: Any, cutoff: int = 4096) -> dict[str, Any]:
    """Classify h=(omega+lambda)^-1 in the free Hilbert scale.

    In one momentum dimension, omega(p)^s h(p) is square integrable exactly
    when s<1/2.  For 0<=s<1/2 and Lambda>=1,

      ||1_|p|>Lambda omega^s h||^2
        <= 1/[3(1-2s)] Lambda^(2s-1),

    using 1/pi<1/3.  At s=1/2 a 1/p lower tail diverges; at s=1 the lower
    density is constant, recovering K158.
    """
    s = q(exponent)
    if s < 0 or cutoff < 1:
        raise CertificateError("use a nonnegative exponent and positive cutoff")
    admitted = s < Fraction(1, 2)
    result: dict[str, Any] = {
        "exponent": qstr(s),
        "sharp_membership": admitted,
        "threshold": "s<1/2",
        "free_form_domain_member": admitted if s == Fraction(1, 2) else None,
        "free_operator_domain_member": admitted if s == 1 else None,
        "tail_square_upper": None,
        "tail_asymptotic_power": qstr(2 * s - 1),
    }
    if admitted:
        power = 1 - 2 * s
        # Keep exact rational output for the two audit exponents used below.
        if s == 0:
            bound = Fraction(1, 3 * cutoff)
        elif s == Fraction(1, 4):
            root = int(cutoff ** 0.5)
            if root * root != cutoff:
                raise CertificateError("the exact s=1/4 display requires a square cutoff")
            bound = Fraction(2, 3 * root)
        else:
            result["tail_square_upper_formula"] = "1/[3(1-2s)] Lambda^(2s-1)"
            return result
        result["tail_square_upper"] = qstr(bound)
        result["tail_square_upper_formula"] = "1/[3(1-2s)] Lambda^(2s-1)"
    else:
        result["divergence"] = "logarithmic_at_s=1/2_and_power_for_s>1/2"
    return result


def fractional_cell_and_cutoff_ledger(index: int = 4096) -> dict[str, Any]:
    """Outward s=1/4 cofinal boundary ledger for delta=1/n, Lambda=n.

    The cell estimate is deliberately coarse but complete.  Lipschitz
    dispersion and lambda=256 give a per-channel H^(1/4) cell error square at
    most 2 delta^2.  The high-momentum tail is at most 2/(3 sqrt(Lambda)).
    Four signed edge/polarity coefficients are combined by the triangle
    inequality; no floating square root is represented as an exact bound.
    """
    if index <= 0:
        raise CertificateError("cofinal index must be positive")
    root = int(index ** 0.5)
    if root * root != index:
        raise CertificateError("exact ledger requires a square cofinal index")
    tail = Fraction(2, 3 * root)
    cell = Fraction(2, index * index)
    return {
        "index": index,
        "delta": qstr(Fraction(1, index)),
        "physical_cutoff": index,
        "fractional_exponent": "1/4",
        "high_momentum_tail_sq_per_channel_upper": qstr(tail),
        "cell_error_sq_per_channel_upper": qstr(cell),
        "combined_per_channel_sq_upper": qstr(tail + cell),
        "four_channel_norm_upper_formula": "4 sqrt(combined_per_channel_sq_upper)",
        "converges_to_zero": True,
        "free_form_exponent_one_half_available": False,
        "free_graph_exponent_one_available": False,
    }


def boundary_weyl_resolvent_budget(
    *,
    free_resolvent_error: Any,
    gamma_norm_upper: Any,
    gamma_error_upper: Any,
    reference_denominator_inverse_upper: Any,
    weyl_denominator_error_upper: Any,
    contour_perimeter: Any = 10,
    require_rank_transfer: bool = False,
) -> dict[str, Any]:
    """Compile a Krein-type boundary resolvent comparison.

    For R_n=R0_n+gamma_n D_n^-1 gamma_n* and
    R=R0+gamma D^-1 gamma*, assume both gamma norms are at most g, the
    reference inverse is at most d0, and ||D_n-D||<=dm. These may be bounded
    operators on a spectator-Fock boundary space; no finite-dimensional
    reduction is assumed. If d0*dm<1,
    ||D_n^-1||<=d0/(1-d0*dm), and an explicit three-term expansion gives the
    returned resolvent error.  Every bound is uniform on the complete contour.
    """
    r0 = q(free_resolvent_error)
    g = q(gamma_norm_upper)
    dg = q(gamma_error_upper)
    d0 = q(reference_denominator_inverse_upper)
    dm = q(weyl_denominator_error_upper)
    perimeter = q(contour_perimeter)
    if min(r0, g, dg, d0, dm) < 0 or perimeter <= 0:
        raise CertificateError("norm errors and bounds must be nonnegative")
    theta = d0 * dm
    if theta >= 1:
        raise CertificateError("Weyl denominator Neumann separation fails")
    dn = d0 / (1 - theta)
    inverse_error = d0 * dn * dm
    eta = r0 + dg * dn * g + g * inverse_error * g + g * d0 * dg
    closes = perimeter * eta < 6
    if require_rank_transfer and not closes:
        raise CertificateError("complete-contour Riesz rank gap does not close")
    return {
        "weyl_neumann_parameter": qstr(theta),
        "approximant_denominator_inverse_upper": qstr(dn),
        "denominator_inverse_error_upper": qstr(inverse_error),
        "complete_resolvent_error_upper": qstr(eta),
        "contour_perimeter": qstr(perimeter),
        "rank_transfer_certified": closes,
        "uses_free_graph_chart_error": False,
        "uses_free_form_chart_error": False,
    }


def native_count_admission(
    *,
    same_cofinal_family: bool,
    reference_rank: int | None,
    reference_rank_ref: str | None,
    complete_contour_error: Any | None,
    native_left_floor: Any | None,
    native_left_floor_ref: str | None,
) -> dict[str, Any]:
    """Fail closed before converting a local island into a native count."""
    if same_cofinal_family is not True:
        raise CertificateError("rank must be proved on the same cofinal reference family")
    if reference_rank is None or reference_rank < 0 or not reference_rank_ref:
        raise CertificateError("cofinal reference rank and proof reference are required")
    if complete_contour_error is None or q(complete_contour_error) * 10 >= 6:
        raise CertificateError("complete contour error must be below 3/5")
    if native_left_floor is None or not native_left_floor_ref:
        raise CertificateError("a native lower spectral floor and proof reference are required")
    floor = q(native_left_floor)
    if floor < -5:
        raise CertificateError("the supplied floor does not exclude spectrum left of -5")
    return {
        "native_spectral_count_below_minus_one": reference_rank,
        "same_cofinal_family": True,
        "local_island_rank_promoted_to_complete_count": True,
        "left_floor": qstr(floor),
        "reference_rank_ref": reference_rank_ref,
        "native_left_floor_ref": native_left_floor_ref,
    }


def demo() -> dict[str, Any]:
    positive = boundary_weyl_resolvent_budget(
        free_resolvent_error="1/1000",
        gamma_norm_upper=1,
        gamma_error_upper="1/1000",
        reference_denominator_inverse_upper=2,
        weyl_denominator_error_upper="1/1000",
        require_rank_transfer=True,
    )
    return {
        "schema_version": "1.0",
        "fractional_domains": [
            fractional_point_domain(0),
            fractional_point_domain("1/4"),
            fractional_point_domain("1/2"),
            fractional_point_domain(1),
        ],
        "cofinal_fractional_ledger_n4096": fractional_cell_and_cutoff_ledger(4096),
        "abstract_boundary_weyl_positive_control": positive,
        "normal_ordered_tails_required_for_boundary_weyl_transfer": False,
        "normal_ordered_tails_required_for_regular_representative_or_K152_route": True,
        "native_count_emitted": False,
        "native_energy_interval_emitted": False,
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
