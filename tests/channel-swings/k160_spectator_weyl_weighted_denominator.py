#!/usr/bin/env python3
"""K160 spectator-Weyl topology and weighted denominator certificates.

The native Weyl denominator is operator-valued on an unbounded spectator-Fock
space.  This module separates the false ordinary operator-norm cutoff premise
from a valid energy-weighted Neumann interface.  Abstract positive controls
are never promoted to native GU spectral data.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Any


class CertificateError(ValueError):
    """Raised when a requested certificate omits a required premise."""


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


def exact_power(cutoff: int, exponent: Fraction) -> Fraction:
    """Return cutoff**exponent for the exact display exponents used here."""
    if cutoff <= 0:
        raise CertificateError("cutoff must be positive")
    if exponent == 1:
        return Fraction(cutoff)
    if exponent == Fraction(1, 2):
        root = int(cutoff ** 0.5)
        if root * root == cutoff:
            return Fraction(root)
    if exponent == Fraction(1, 4):
        root = int(cutoff ** 0.25)
        while (root + 1) ** 4 <= cutoff:
            root += 1
        while root ** 4 > cutoff:
            root -= 1
        if root ** 4 == cutoff:
            return Fraction(root)
    raise CertificateError("exact display requires exponent 1, 1/2, or 1/4 and a perfect-power cutoff")


def unweighted_spectator_tail_obstruction(
    cutoff: int = 4096, subtraction_shift: Any = 256
) -> dict[str, Any]:
    """Certify that a matched sharp-cutoff Weyl tail is not norm small.

    At z=-1, on the active-edge vacuum and spectator-energy fiber s,

      T_Lambda(s)=int_|p|>Lambda [1/(omega+s+1)-1/(omega+mu)] dp/(2*pi).

    Put P=max(Lambda,mu+1,1).  For P<=p<=s/4, omega<=p+1,
    1/(omega+mu)>=1/(2p), and 1/(omega+s+1)<=1/s<=1/(4p).
    Hence |T_Lambda(s)| >= log(s/(4P))/(4*pi) for s>=4P.
    The spectator spectrum is unbounded, so every finite cutoff has infinite
    ordinary multiplier norm.  This is a topology obstruction, not a failure
    of pointwise convergence at fixed s.
    """
    mu = q(subtraction_shift)
    if cutoff <= 0 or mu <= 0 or mu.denominator != 1:
        raise CertificateError("use a positive cutoff and positive integral subtraction shift")
    pivot = max(cutoff, int(mu) + 1, 1)
    return {
        "cutoff": cutoff,
        "matched_subtraction_shift": qstr(mu),
        "test_spectral_point": "z=-1",
        "pivot_P": pivot,
        "lower_bound_family": "|T_Lambda(s)| >= log(s/(4P))/(4*pi) for s>=4P",
        "spectator_energy_unbounded": True,
        "fixed_s_tail_converges": True,
        "ordinary_operator_norm_tail_is_finite": False,
        "ordinary_operator_norm_convergence": False,
        "native_unweighted_dm_available": False,
    }


def weighted_diagonal_tail_bound(
    *,
    cutoff: int = 4096,
    weight_exponent: Any = 1,
    subtraction_shift: Any = 256,
    contour_modulus_upper: Any = "21/4",
) -> dict[str, Any]:
    """Give an exact outward bound after a spectator-energy weight.

    On the complete K157 rectangle Re(z)<=-1 and |z|<21/4,

      |T_Lambda(s)| <= pi^-1[log(1+s/Lambda)+(mu+|z|)/Lambda].

    For 0<alpha<=1, log(1+t)<=t^alpha/alpha.  Multiplication by
    (1+s)^(-alpha), together with 1/pi<1/3, yields

      ||T_Lambda(S)(1+S)^(-alpha)||
        <= 1/(3 alpha Lambda^alpha)+(mu+21/4)/(3 Lambda).

    This controls only the matched diagonal spectator term.  A native complete
    denominator error must additionally include Pauli and exchange pieces.
    """
    alpha = q(weight_exponent)
    mu = q(subtraction_shift)
    zmax = q(contour_modulus_upper)
    if not 0 < alpha <= 1 or mu <= 0 or zmax <= 0:
        raise CertificateError("invalid weight, subtraction shift, or contour bound")
    cutoff_power = exact_power(cutoff, alpha)
    bound = Fraction(1, 3) * (
        Fraction(1, 1) / (alpha * cutoff_power) + (mu + zmax) / cutoff
    )
    return {
        "cutoff": cutoff,
        "weight": f"(1+S)^(-{qstr(alpha)})",
        "complete_rectangle_real_part_at_most": "-1",
        "complete_rectangle_modulus_upper": qstr(zmax),
        "diagonal_weighted_tail_upper": qstr(bound),
        "bound_formula": "1/(3*alpha*Lambda^alpha)+(mu+|z|_max)/(3*Lambda)",
        "converges_to_zero": True,
        "Pauli_and_exchange_components_included": False,
        "complete_native_weighted_denominator_error_emitted": False,
    }


def weighted_denominator_resolvent_budget(
    *,
    free_resolvent_error: Any,
    gamma_norm_upper: Any,
    gamma_error_upper: Any,
    reference_denominator_inverse_upper: Any,
    weighted_denominator_error_upper: Any,
    reference_inverse_smoothing_upper: Any,
    contour_perimeter: Any = 10,
    require_rank_transfer: bool = False,
) -> dict[str, Any]:
    """Compile weighted Weyl data into an ordinary resolvent error.

    Let A=1+S, eps=||(D_n-D)A^-1|| and c1=||A D^-1||.  Then
    K=(D_n-D)D^-1 has norm at most theta=eps*c1.  If theta<1,
    D_n^-1=D^-1(1+K)^-1 and the ordinary inverse and Krein-resolvent
    differences follow.  The smoothing bound must be proved on the same
    complete contour; unweighted pointwise convergence cannot replace it.
    """
    r0 = q(free_resolvent_error)
    g = q(gamma_norm_upper)
    dg = q(gamma_error_upper)
    d0 = q(reference_denominator_inverse_upper)
    eps = q(weighted_denominator_error_upper)
    c1 = q(reference_inverse_smoothing_upper)
    perimeter = q(contour_perimeter)
    if min(r0, g, dg, d0, eps, c1) < 0 or perimeter <= 0:
        raise CertificateError("bounds and errors must be nonnegative")
    theta = eps * c1
    if theta >= 1:
        raise CertificateError("weighted denominator Neumann separation fails")
    dn = d0 / (1 - theta)
    inverse_error = d0 * theta / (1 - theta)
    eta = r0 + dg * dn * g + g * inverse_error * g + g * d0 * dg
    closes = perimeter * eta < 6
    if require_rank_transfer and not closes:
        raise CertificateError("complete-contour Riesz rank gap does not close")
    return {
        "weighted_neumann_parameter": qstr(theta),
        "approximant_denominator_inverse_upper": qstr(dn),
        "denominator_inverse_error_upper": qstr(inverse_error),
        "complete_resolvent_error_upper": qstr(eta),
        "contour_perimeter": qstr(perimeter),
        "rank_transfer_certified": closes,
        "ordinary_unweighted_denominator_error_required": False,
        "complete_weighted_denominator_error_required": True,
        "reference_inverse_smoothing_required": True,
    }


def native_count_admission(
    *,
    complete_weighted_denominator_ref: str | None,
    inverse_smoothing_ref: str | None,
    low_energy_denominator_ref: str | None,
    same_cofinal_rank: int | None,
    same_cofinal_rank_ref: str | None,
    complete_contour_error: Any | None,
    native_left_floor: Any | None,
    native_left_floor_ref: str | None,
    signed_charge_intertwiner_ref: str | None,
) -> dict[str, Any]:
    """Fail closed before converting the weighted interface to a count."""
    required = {
        "complete weighted denominator": complete_weighted_denominator_ref,
        "inverse smoothing": inverse_smoothing_ref,
        "low-energy denominator": low_energy_denominator_ref,
        "same-cofinal rank": same_cofinal_rank_ref,
        "native left floor": native_left_floor_ref,
        "signed charge intertwiner": signed_charge_intertwiner_ref,
    }
    missing = [name for name, ref in required.items() if not ref]
    if missing:
        raise CertificateError("missing native references: " + ", ".join(missing))
    if same_cofinal_rank is None or same_cofinal_rank < 0:
        raise CertificateError("same-cofinal rank must be a nonnegative integer")
    if complete_contour_error is None or q(complete_contour_error) * 10 >= 6:
        raise CertificateError("complete contour error must be below 3/5")
    if native_left_floor is None or q(native_left_floor) < -5:
        raise CertificateError("native floor must exclude spectrum left of -5")
    return {
        "native_spectral_count_below_minus_one": same_cofinal_rank,
        "weighted_boundary_route_closed": True,
        "left_floor": qstr(q(native_left_floor)),
        "signed_charge_transport_certified": True,
    }


def demo() -> dict[str, Any]:
    abstract = weighted_denominator_resolvent_budget(
        free_resolvent_error="1/1000",
        gamma_norm_upper=1,
        gamma_error_upper="1/1000",
        reference_denominator_inverse_upper=2,
        weighted_denominator_error_upper="1/1000",
        reference_inverse_smoothing_upper=2,
        require_rank_transfer=True,
    )
    return {
        "schema_version": "1.0",
        "unweighted_tail_obstruction_n4096": unweighted_spectator_tail_obstruction(),
        "weighted_diagonal_tail_n4096": weighted_diagonal_tail_bound(),
        "weighted_diagonal_tail_n65536": weighted_diagonal_tail_bound(cutoff=65536),
        "abstract_weighted_resolvent_positive_control": abstract,
        "native_complete_weighted_denominator_error_emitted": False,
        "native_inverse_smoothing_emitted": False,
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
