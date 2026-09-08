#!/usr/bin/env python3
"""Baseline-first probe and hostile mutations for the K164 certificates."""

from __future__ import annotations

import argparse
import importlib.util
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent


def _load():
    path = HERE / "k164_selfadjoint_half_weight_form_transfer.py"
    spec = importlib.util.spec_from_file_location("k164_solver", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K164 solver")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K164 = _load()


def expect_error(callable_, token: str) -> None:
    try:
        callable_()
    except K164.CertificateError as exc:
        if token not in str(exc):
            raise AssertionError(f"wrong failure: {exc}") from exc
    else:
        raise AssertionError(f"expected failure containing {token!r}")


def baseline() -> list[str]:
    checks: list[str] = []
    counter = K164.nonselfadjoint_right_weight_counterexample(root_scale=10, epsilon=Fraction(1, 100))
    assert counter["right_weight_norm"] == "1/100"; checks.append("right endpoint exact")
    assert counter["half_weight_norm"] == "1/10"; checks.append("half weight amplification exact")
    assert counter["amplification"] == "10"; checks.append("amplification exact")
    assert counter["selfadjoint"] is False; checks.append("nonselfadjoint typed")
    assert counter["one_sided_bound_controls_half_weight"] is False; checks.append("one-sided refusal")

    promoted = K164.selfadjoint_half_weight_transfer(
        right_weight_bound=Fraction(1, 7), selfadjoint=True, common_positive_weight=True
    )
    assert promoted["epsilon"] == "1/7"; checks.append("epsilon preserved")
    assert promoted["selfadjointness_used"] is True; checks.append("adjoint endpoint used")
    assert "A^(-1/2)" in promoted["interpolation"]; checks.append("half weight emitted")
    assert promoted["complex_contour_transfer_allowed"] is False; checks.append("contour fenced")

    packet = K164.form_transfer_thresholds(
        epsilon=Fraction(1, 20), anchor_coercivity=Fraction(1, 2), shift=6,
        anchor_ground_upper=-1, anchor_next_lower=2, anchor_left_floor=-4,
        threshold=0, anchor_residual_dual=Fraction(1, 20), trial_weight_norm=1,
    )
    assert packet["relative_form_delta"] == "1/10"; checks.append("delta exact")
    assert packet["transferred_coercivity_in_A"] == "9/20"; checks.append("coercivity exact")
    assert packet["true_residual_dual_upper"] == "1/10"; checks.append("residual exact")
    assert packet["transferred_ground_upper"] == "-1/2"; checks.append("ground upper exact")
    assert packet["transferred_next_lower"] == "6/5"; checks.append("next floor exact")
    assert packet["transferred_left_floor"] == "-21/5"; checks.append("left floor exact")
    assert packet["exactly_one_below_threshold_transfers"] is True; checks.append("count gap transfers")
    assert packet["native_floor_above_minus_five"] is True; checks.append("minus-five floor transfers")

    required = K164.required_anchor_coercivity(
        epsilon=Fraction(1, 20), shift=6, ground_upper=-1, next_lower=2,
        left_floor=-4, threshold=0, desired_left=-5,
    )
    assert required["strict_kappa_lower_bounds"]["ground_below_threshold"] == "1/4"; checks.append("ground threshold exact")
    assert required["strict_kappa_lower_bounds"]["next_above_threshold"] == "1/5"; checks.append("next threshold exact")
    assert required["strict_kappa_lower_bounds"]["left_floor_above_desired"] == "1/10"; checks.append("left threshold exact")
    assert required["combined_strict_kappa_lower_bound"] == "1/4"; checks.append("combined threshold exact")

    demo = K164.demo()
    assert demo["conditional_anchor_example_4096_verdict"] == "margin fails"; checks.append("4096 margin refusal")
    assert demo["conditional_anchor_example_65536"]["exactly_one_below_threshold_transfers"] is True; checks.append("65536 count example")
    assert demo["conditional_anchor_example_65536"]["native_floor_above_minus_five"] is True; checks.append("65536 left-floor example")
    assert demo["native_K152_replay"]["native_K152_interface_complete"] is False; checks.append("native replay fails closed")
    assert "same-family anchor" in demo["native_K152_replay"]["missing_native_references"]; checks.append("anchor absence named")
    assert "self-adjoint regular-tail identification" not in demo["native_K152_replay"]["missing_native_references"]; checks.append("regular-tail topology closed")
    assert demo["physical_or_source_selection"] is False; checks.append("physical selection fenced")
    assert demo["Born_prediction_or_confirmation_credit"] is False; checks.append("prediction credit fenced")
    return checks


def hostile() -> list[str]:
    caught: list[str] = []
    cases = [
        (lambda: K164.nonselfadjoint_right_weight_counterexample(root_scale=0, epsilon=1), "positive"),
        (lambda: K164.nonselfadjoint_right_weight_counterexample(root_scale=1, epsilon=0), "positive"),
        (lambda: K164.selfadjoint_half_weight_transfer(right_weight_bound=-1, selfadjoint=True, common_positive_weight=True), "nonnegative"),
        (lambda: K164.selfadjoint_half_weight_transfer(right_weight_bound=1, selfadjoint=False, common_positive_weight=True), "T=T*"),
        (lambda: K164.selfadjoint_half_weight_transfer(right_weight_bound=1, selfadjoint=True, common_positive_weight=False), "common positive"),
        (lambda: K164.form_transfer_thresholds(epsilon=-1, anchor_coercivity=1, shift=1, anchor_ground_upper=0, anchor_next_lower=1, anchor_left_floor=0, threshold=Fraction(1,2), anchor_residual_dual=0, trial_weight_norm=0), "nonnegative"),
        (lambda: K164.form_transfer_thresholds(epsilon=1, anchor_coercivity=0, shift=1, anchor_ground_upper=0, anchor_next_lower=1, anchor_left_floor=0, threshold=Fraction(1,2), anchor_residual_dual=0, trial_weight_norm=0), "positive"),
        (lambda: K164.form_transfer_thresholds(epsilon=1, anchor_coercivity=1, shift=0, anchor_ground_upper=0, anchor_next_lower=1, anchor_left_floor=0, threshold=Fraction(1,2), anchor_residual_dual=0, trial_weight_norm=0), "positive"),
        (lambda: K164.form_transfer_thresholds(epsilon=1, anchor_coercivity=2, shift=1, anchor_ground_upper=-1, anchor_next_lower=1, anchor_left_floor=0, threshold=0, anchor_residual_dual=0, trial_weight_norm=0), "shifted"),
        (lambda: K164.form_transfer_thresholds(epsilon=1, anchor_coercivity=1, shift=2, anchor_ground_upper=0, anchor_next_lower=1, anchor_left_floor=0, threshold=Fraction(1,2), anchor_residual_dual=0, trial_weight_norm=0), "epsilon <"),
        (lambda: K164.required_anchor_coercivity(epsilon=1, shift=6, ground_upper=0, next_lower=2, left_floor=-4, threshold=0, desired_left=-5), "straddle"),
        (lambda: K164.required_anchor_coercivity(epsilon=1, shift=6, ground_upper=-1, next_lower=0, left_floor=-4, threshold=0, desired_left=-5), "straddle"),
        (lambda: K164.required_anchor_coercivity(epsilon=1, shift=6, ground_upper=-1, next_lower=2, left_floor=-5, threshold=0, desired_left=-5), "straddle"),
    ]
    for index, (case, token) in enumerate(cases, start=1):
        expect_error(case, token)
        caught.append(f"hostile {index} caught")
    return caught


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    checks = baseline()
    print(f"K164 baseline: {len(checks)}/{len(checks)} pass")
    if args.selftest:
        caught = hostile()
        print(f"K164 hostile: {len(caught)}/{len(caught)} caught")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
