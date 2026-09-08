#!/usr/bin/env python3
"""K164 self-adjoint half-weight and form-transfer certificates.

This module separates two operator topologies that the K161/K163 chain must
not conflate.  A one-sided estimate ``||T A^-1|| <= eps`` does not control the
half-weight sandwich for a general non-normal operator.  If ``T=T*`` and
``A>=1`` is the common positive weight, the adjoint supplies the opposite
endpoint and the three-lines/Heinz interpolation theorem gives
``||A^-1/2 T A^-1/2|| <= eps``.  The resulting symmetric form bound supports
residual, coercivity and min--max transfer, but only after a same-family anchor
supplies the remaining native data.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent


def _load(name: str):
    path = HERE / name
    spec = importlib.util.spec_from_file_location(f"k164_{path.stem}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load sibling {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K161 = _load("k161_weighted_denominator_smoothing_obstruction.py")


class CertificateError(ValueError):
    """Raised when a form-transfer premise is absent or inconsistent."""


def q(value: Any) -> Fraction:
    if isinstance(value, Fraction):
        return value
    try:
        return Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise CertificateError(f"invalid rational input: {value!r}") from exc


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def nonselfadjoint_right_weight_counterexample(*, root_scale: int, epsilon: Any) -> dict[str, Any]:
    """Exact 2x2 counterexample to one-sided half-weight promotion.

    Let ``A=diag(1,n^2)`` and ``T=[[0,eps*n^2],[0,0]]``.  Then
    ``||T A^-1||=eps`` while
    ``||A^-1/2 T A^-1/2||=eps*n``.  The latter is unbounded with ``n``.
    """
    eps = q(epsilon)
    if root_scale < 1 or eps <= 0:
        raise CertificateError("root scale and epsilon must be positive")
    return {
        "weight_A": ["1", str(root_scale * root_scale)],
        "operator_T": [["0", qstr(eps * root_scale * root_scale)], ["0", "0"]],
        "right_weight_norm": qstr(eps),
        "half_weight_norm": qstr(eps * root_scale),
        "amplification": str(root_scale),
        "selfadjoint": False,
        "one_sided_bound_controls_half_weight": False,
    }


def selfadjoint_half_weight_transfer(
    *, right_weight_bound: Any, selfadjoint: bool, common_positive_weight: bool
) -> dict[str, Any]:
    """Compile the self-adjoint endpoint interpolation theorem."""
    eps = q(right_weight_bound)
    if eps < 0:
        raise CertificateError("right-weight bound must be nonnegative")
    if not selfadjoint:
        raise CertificateError("half-weight promotion requires T=T*")
    if not common_positive_weight:
        raise CertificateError("half-weight promotion requires one common positive weight")
    return {
        "right_endpoint": "||T A^(-1)||<=epsilon",
        "left_endpoint": "||A^(-1) T||<=epsilon by adjointness",
        "interpolation": "||A^(-1/2) T A^(-1/2)||<=epsilon",
        "symmetric_form_bound": "|t[x,y]|<=epsilon ||x||_A ||y||_A",
        "epsilon": qstr(eps),
        "selfadjointness_used": True,
        "complex_contour_transfer_allowed": False,
    }


def form_transfer_thresholds(
    *,
    epsilon: Any,
    anchor_coercivity: Any,
    shift: Any,
    anchor_ground_upper: Any,
    anchor_next_lower: Any,
    anchor_left_floor: Any,
    threshold: Any,
    anchor_residual_dual: Any,
    trial_weight_norm: Any,
) -> dict[str, Any]:
    """Transfer residual, coercivity and spectral margins from one anchor.

    Premises are ``a_N+c >= kappa A`` and ``|t|<=epsilon A``.  Hence
    ``a+c >= (kappa-epsilon)A`` and, with ``delta=epsilon/kappa<1``,
    ``(1-delta)(a_N+c) <= a+c <= (1+delta)(a_N+c)``.  Min--max then
    transports every complete anchor eigenvalue bound.
    """
    eps = q(epsilon)
    kappa = q(anchor_coercivity)
    c = q(shift)
    ground = q(anchor_ground_upper)
    next_floor = q(anchor_next_lower)
    left_floor = q(anchor_left_floor)
    b = q(threshold)
    residual = q(anchor_residual_dual)
    trial_norm = q(trial_weight_norm)
    if eps < 0 or kappa <= 0 or c <= 0 or residual < 0 or trial_norm < 0:
        raise CertificateError("bounds must be nonnegative and coercivity/shift positive")
    if min(ground + c, next_floor + c, left_floor + c) <= 0:
        raise CertificateError("all shifted anchor spectral bounds must be positive")
    delta = eps / kappa
    if delta >= 1:
        raise CertificateError("form transfer requires epsilon < anchor coercivity")

    true_ground_upper = (1 + delta) * (ground + c) - c
    true_next_lower = (1 - delta) * (next_floor + c) - c
    true_left_floor = (1 - delta) * (left_floor + c) - c
    true_residual = residual + eps * trial_norm
    one_below = true_ground_upper < b < true_next_lower
    return {
        "epsilon": qstr(eps),
        "anchor_coercivity_in_A": qstr(kappa),
        "transferred_coercivity_in_A": qstr(kappa - eps),
        "relative_form_delta": qstr(delta),
        "anchor_residual_dual_upper": qstr(residual),
        "trial_A_norm": qstr(trial_norm),
        "true_residual_dual_upper": qstr(true_residual),
        "shift": qstr(c),
        "anchor_ground_upper": qstr(ground),
        "transferred_ground_upper": qstr(true_ground_upper),
        "anchor_next_lower": qstr(next_floor),
        "transferred_next_lower": qstr(true_next_lower),
        "anchor_left_floor": qstr(left_floor),
        "transferred_left_floor": qstr(true_left_floor),
        "threshold": qstr(b),
        "exactly_one_below_threshold_transfers": one_below,
        "native_floor_above_minus_five": true_left_floor > -5,
    }


def required_anchor_coercivity(
    *, epsilon: Any, shift: Any, ground_upper: Any, next_lower: Any,
    left_floor: Any, threshold: Any, desired_left: Any,
) -> dict[str, Any]:
    """Return strict kappa thresholds for each desired transfer margin."""
    eps = q(epsilon)
    c = q(shift)
    ground = q(ground_upper)
    next_floor = q(next_lower)
    left_floor_q = q(left_floor)
    b = q(threshold)
    desired = q(desired_left)
    if not (ground < b < next_floor and desired < left_floor_q):
        raise CertificateError("anchor margins must already straddle the thresholds")
    values = {
        "coercivity": eps,
        "ground_below_threshold": eps * (ground + c) / (b - ground),
        "next_above_threshold": eps * (next_floor + c) / (next_floor - b),
        "left_floor_above_desired": eps * (left_floor_q + c) / (left_floor_q - desired),
    }
    return {
        "strict_kappa_lower_bounds": {key: qstr(value) for key, value in values.items()},
        "combined_strict_kappa_lower_bound": qstr(max(values.values())),
    }


def native_k152_replay(
    *, selfadjoint_regular_tail_ref: str | None, same_family_anchor_ref: str | None,
    anchor_coercivity_ref: str | None, anchor_residual_ref: str | None,
    anchor_next_floor_ref: str | None, anchor_left_floor_ref: str | None,
    signed_charge_intertwiner_ref: str | None,
) -> dict[str, Any]:
    required = {
        "self-adjoint regular-tail identification": selfadjoint_regular_tail_ref,
        "same-family anchor": same_family_anchor_ref,
        "anchor coercivity": anchor_coercivity_ref,
        "anchor residual": anchor_residual_ref,
        "anchor next-distinct floor": anchor_next_floor_ref,
        "anchor native left floor": anchor_left_floor_ref,
        "signed charge intertwiner": signed_charge_intertwiner_ref,
    }
    missing = [name for name, ref in required.items() if not ref]
    return {
        "native_K152_interface_complete": not missing,
        "missing_native_references": missing,
        "native_ground_count_emitted": False,
        "native_energy_interval_emitted": False,
    }


def demo() -> dict[str, Any]:
    eps_4096 = q(K161.complete_weighted_tail(4096)["complete_weighted_denominator_error_upper"])
    eps_65536 = q(K161.complete_weighted_tail(65536)["complete_weighted_denominator_error_upper"])
    common = {
        "anchor_coercivity": Fraction(1, 2),
        "shift": 6,
        "anchor_ground_upper": -1,
        "anchor_next_lower": 2,
        "anchor_left_floor": -4,
        "threshold": 0,
        "anchor_residual_dual": Fraction(1, 20),
        "trial_weight_norm": 1,
    }
    coarse_failure: str
    try:
        coarse = form_transfer_thresholds(epsilon=eps_4096, **common)
    except CertificateError as exc:
        coarse_failure = str(exc)
        coarse = None
    else:
        coarse_failure = "margin fails" if not coarse["exactly_one_below_threshold_transfers"] else "unexpected pass"
    fine = form_transfer_thresholds(epsilon=eps_65536, **common)
    return {
        "schema_version": "1.0",
        "nonselfadjoint_counterexample": nonselfadjoint_right_weight_counterexample(
            root_scale=1024, epsilon=Fraction(1, 1000)
        ),
        "selfadjoint_interpolation_4096": selfadjoint_half_weight_transfer(
            right_weight_bound=eps_4096, selfadjoint=True, common_positive_weight=True
        ),
        "selfadjoint_interpolation_65536": selfadjoint_half_weight_transfer(
            right_weight_bound=eps_65536, selfadjoint=True, common_positive_weight=True
        ),
        "conditional_anchor_thresholds_4096": required_anchor_coercivity(
            epsilon=eps_4096, shift=6, ground_upper=-1, next_lower=2,
            left_floor=-4, threshold=0, desired_left=-5,
        ),
        "conditional_anchor_thresholds_65536": required_anchor_coercivity(
            epsilon=eps_65536, shift=6, ground_upper=-1, next_lower=2,
            left_floor=-4, threshold=0, desired_left=-5,
        ),
        "conditional_anchor_example_4096": coarse,
        "conditional_anchor_example_4096_verdict": coarse_failure,
        "conditional_anchor_example_65536": fine,
        "native_K152_replay": native_k152_replay(
            selfadjoint_regular_tail_ref="K156#normal-ordered-self-adjoint-core+K161#five-tail-bound",
            same_family_anchor_ref=None,
            anchor_coercivity_ref=None,
            anchor_residual_ref=None,
            anchor_next_floor_ref=None,
            anchor_left_floor_ref=None,
            signed_charge_intertwiner_ref="K162#signed-flavor-transport",
        ),
        "route_verdict": "SELFADJOINT_FORM_PROMOTION_CONDITIONAL__COMPLEX_CONTOUR_PROMOTION_REFUSED__NATIVE_ANCHOR_STILL_REQUIRED",
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
