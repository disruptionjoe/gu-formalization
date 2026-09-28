#!/usr/bin/env python3
"""Propagate K457's exact tail through K569's complete finite-square enclosure."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from math import isqrt
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
K569 = ROOT / "lab/process/k569-complete-finite-gram-square-enclosure.json"
K457 = ROOT / "lab/process/k457-k152-shifted-residual-gram-reduction.json"
OUTPUT = ROOT / "lab/process/k570-complete-m-dual-residual-enclosure.json"
SQRT_SCALE = 10**80


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def scientific(value: Fraction, digits: int = 17) -> str:
    if value == 0:
        return "0"
    with localcontext() as context:
        context.prec = digits + 16
        return f"{Decimal(value.numerator) / Decimal(value.denominator):.{digits}e}"


def floor_sqrt_fraction(value: Fraction, scale: int = SQRT_SCALE) -> Fraction:
    if value < 0:
        raise ValueError("square-root input must be nonnegative")
    scaled_floor = value.numerator * scale * scale // value.denominator
    return Fraction(isqrt(scaled_floor), scale)


def ceil_sqrt_fraction(value: Fraction, scale: int = SQRT_SCALE) -> Fraction:
    if value < 0:
        raise ValueError("square-root input must be nonnegative")
    numerator = value.numerator * scale * scale
    scaled_ceil = (numerator + value.denominator - 1) // value.denominator
    root = isqrt(scaled_ceil)
    if root * root < scaled_ceil:
        root += 1
    return Fraction(root, scale)


def build() -> dict[str, Any]:
    k569 = json.loads(K569.read_text())
    k457 = json.loads(K457.read_text())
    finite_lower, finite_upper = (
        Fraction(value) for value in k569["finite_square_Q_12"]["interval_exact"]
    )
    tail = Fraction(k457["tail_budget"]["epsilon"])
    root_lower = floor_sqrt_fraction(finite_lower)
    root_upper = ceil_sqrt_fraction(finite_upper)
    residual_lower = max(Fraction(0), root_lower - tail) ** 2
    residual_upper = (root_upper + tail) ** 2
    return {
        "schema_version": "1.0",
        "result_id": "K570-COMPLETE-M-DUAL-RESIDUAL-ENCLOSURE",
        "created": "2026-09-28",
        "classification": "INTERNAL_CONDITIONAL_MATHEMATICS",
        "direction": "observed_to_native",
        "scope": "Complete rigorous numerical enclosure of K457's M-dual residual norm square using K569's full Q_12 interval and K457's exact post-order-twelve norm tail.",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K569, K457)],
            "resolved_vectors": k569["fixed_control"]["resolved_vectors"],
            "coherent_groups": k569["fixed_control"]["coherent_groups"],
            "self_and_cross_entries": k569["fixed_control"]["self_and_cross_entries"],
            "post_order_twelve_tail_epsilon": q(tail),
            "sqrt_rational_scale_digits": 80,
        },
        "finite_square_input": {
            "interval_exact": [q(finite_lower), q(finite_upper)],
            "interval_scientific": [scientific(finite_lower), scientific(finite_upper)],
            "sqrt_interval_exact": [q(root_lower), q(root_upper)],
            "sqrt_interval_scientific": [scientific(root_lower), scientific(root_upper)],
            "sqrt_lower_is_outward": root_lower * root_lower <= finite_lower,
            "sqrt_upper_is_outward": root_upper * root_upper >= finite_upper,
        },
        "tail_composition": {
            "identity": k457["residual_identity"]["complete_residual"],
            "two_sided_bound": k457["residual_identity"]["two_sided_bound"],
            "tail_norm_upper_exact": q(tail),
            "tail_is_post_left_adjoint": k457["tail_budget"]["post_left_adjoint"],
            "tail_applied_once": True,
            "finite_lower_norm_does_not_exceed_tail": root_lower <= tail,
        },
        "complete_M_dual_residual_norm_square": {
            "interval_exact": [q(residual_lower), q(residual_upper)],
            "interval_scientific": [scientific(residual_lower), scientific(residual_upper)],
            "lower_endpoint_zero_because_tail_can_cancel_certified_finite_lower_norm": residual_lower == 0,
            "upper_endpoint_finite": True,
            "metric_type": k457["residual_identity"]["metric_type"],
            "K152_shifted_form_dual_type": k457["residual_identity"]["K152_shifted_form_dual_type"],
        },
        "decision": {
            "complete_M_dual_residual_numerically_enclosed": True,
            "complete_M_dual_residual_sign_or_positive_floor_decided": residual_lower > 0,
            "useful_downstream_spectral_margin_emitted": False,
            "K152_shifted_form_dual_residual_serialized": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "supply a quantitative K466 shifted-coercivity bridge and a useful complete-complement or action-flux floor before transferring any residual budget to K152",
        },
        "release_test": {
            "all_2958_vectors_retained": k569["fixed_control"]["resolved_vectors"] == 2958,
            "all_201_groups_retained": k569["fixed_control"]["coherent_groups"] == 201,
            "all_59586_entries_retained": k569["fixed_control"]["self_and_cross_entries"] == 59586,
            "sqrt_lower_outward": root_lower * root_lower <= finite_lower,
            "sqrt_upper_outward": root_upper * root_upper >= finite_upper,
            "tail_applied_once": True,
            "complete_M_dual_residual_enclosed": residual_lower <= residual_upper,
            "shifted_metric_not_substituted": True,
            "useful_margin_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k569["ledger_effect"],
        "source_routing": k569["source_routing"],
        "claim_ceiling": "Rigorous complete numerical enclosure of the M-dual/Hilbert residual norm square after all 59,586 finite Gram entries and the exact post-order-twelve tail. The lower endpoint is zero and the upper endpoint is extremely coarse, so this proves conditional finiteness but no useful residual margin. K465's metric correction remains binding: this is not K152's shifted form-dual residual, and no coercivity, next spectrum, native K152, source, ledger, canon, paper, public, novelty or physical claim moves.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["resolved_vectors"], fixed["coherent_groups"], fixed["self_and_cross_entries"], fixed["post_order_twelve_tail_epsilon"], fixed["sqrt_rational_scale_digits"]) != (2958, 201, 59586, "3011499/838860800", 80):
        raise AssertionError("K570 fixed control changed")
    finite = payload["finite_square_input"]
    finite_lower, finite_upper = (Fraction(value) for value in finite["interval_exact"])
    root_lower, root_upper = (Fraction(value) for value in finite["sqrt_interval_exact"])
    if root_lower * root_lower > finite_lower or root_upper * root_upper < finite_upper or not finite["sqrt_lower_is_outward"] or not finite["sqrt_upper_is_outward"]:
        raise AssertionError("K570 square-root enclosure changed")
    lower, upper = (Fraction(value) for value in payload["complete_M_dual_residual_norm_square"]["interval_exact"])
    if lower < 0 or lower > upper or not payload["complete_M_dual_residual_norm_square"]["upper_endpoint_finite"]:
        raise AssertionError("K570 residual enclosure changed")
    tail = payload["tail_composition"]
    if not tail["tail_is_post_left_adjoint"] or not tail["tail_applied_once"]:
        raise AssertionError("K570 tail composition changed")
    decision = payload["decision"]
    if not decision["complete_M_dual_residual_numerically_enclosed"] or decision["useful_downstream_spectral_margin_emitted"] or decision["K152_shifted_form_dual_residual_serialized"] or decision["native_K152_interval_emitted"]:
        raise AssertionError("K570 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K570 release boundary changed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate_payload(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
