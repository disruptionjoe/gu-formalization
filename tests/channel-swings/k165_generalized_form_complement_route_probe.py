#!/usr/bin/env python3
"""Baseline-first probe and hostile inputs for the K165 route certificate."""

from __future__ import annotations

import argparse
import importlib.util
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent


def _load():
    path = HERE / "k165_generalized_form_complement_route.py"
    spec = importlib.util.spec_from_file_location("k165_solver", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K165 solver")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K165 = _load()


def expect_error(callable_, token: str) -> None:
    try:
        callable_()
    except K165.CertificateError as exc:
        if token not in str(exc):
            raise AssertionError(f"wrong failure: {exc}") from exc
    else:
        raise AssertionError(f"expected failure containing {token!r}")


def baseline() -> list[str]:
    checks: list[str] = []
    reduction = K165.physical_cell_reduction_obstruction(0, 1)
    assert reduction["cell_indicator_space_conforming"] is True; checks.append("cell conformity retained")
    assert reduction["cell_indicator_space_reduces_free_multiplication"] is False; checks.append("free reduction refused")
    assert reduction["Q_H0_P_nonzero"] is True; checks.append("free cross block named")
    assert reduction["ritz_compression_supplies_upper_data_only"] is True; checks.append("Ritz role typed")
    assert reduction["free_complement_floor_alone_supplies_full_count"] is False; checks.append("free-gap paste refused")

    metric = K165.chart_metric(contraction_upper=Fraction(3, 8))
    assert metric["metric_lower"] == "64/121"; checks.append("metric lower exact")
    assert metric["metric_upper"] == "64/25"; checks.append("metric upper exact")
    assert metric["regular_pencil"] == "R-zM"; checks.append("generalized pencil typed")
    assert metric["physical_complement"].startswith("M-orthogonal"); checks.append("physical complement typed")
    assert metric["free_Hilbert_complement_is_substitutable"] is False; checks.append("free complement rejected")

    budget = K165.separated_auxiliary_budget(
        auxiliary_shift=256, inverse_chart_bound=Fraction(8, 5), physical_shift=6
    )
    assert budget["identity_piece_only_lower_budget"] == "-9834/25"; checks.append("cancellation loss exact")
    assert budget["separated_norm_route_certifies_positive_coercivity"] is False; checks.append("crude coercivity refused")
    assert budget["combined_fixed_form_must_preserve_lambda_cancellation"] is True; checks.append("combined form required")
    assert budget["negative_budget_proves_operator_unbounded_below"] is False; checks.append("spectral overclaim fenced")

    control = K165.generalized_complement_count(
        regular_form=[[-2, 1, 1], [1, 6, 0], [1, 0, 5]],
        metric=[[2, 1, 0], [1, 2, 0], [0, 0, 1]],
        trial=[1, 0, 0], threshold=0,
    )
    assert control["trial_generalized_rayleigh"] == "-1"; checks.append("generalized Rayleigh exact")
    assert control["complement_kind"] == "M-orthogonal"; checks.append("control complement exact")
    assert control["complement_shifted_inertia"] == [0, 0, 2]; checks.append("complement inertia exact")
    assert control["full_pencil_inertia"] == [1, 0, 2]; checks.append("full inertia exact")
    assert control["generalized_eigenvalue_count_below_threshold"] == 1; checks.append("generalized count exact")
    assert control["coupling_may_be_nonzero"] is True; checks.append("Schur coupling retained")

    demo = K165.demo()
    assert "not an absolute" in demo["K161_tail_role_failure"]; checks.append("tail role fail closed")
    replay = demo["native_same_form_replay"]
    assert replay["native_same_form_packet_complete"] is False; checks.append("native replay incomplete")
    assert "anchor_coercivity_ref" in replay["missing_native_references"]; checks.append("coercivity absence named")
    assert "M_orthogonal_complement_or_flux_ref" in replay["missing_native_references"]; checks.append("complement absence named")
    assert "physical_metric_ref" not in replay["missing_native_references"]; checks.append("metric identification closed")
    assert "signed_charge_intertwiner_ref" not in replay["missing_native_references"]; checks.append("charge transport closed")
    assert replay["native_ground_count_emitted"] is False; checks.append("native count fenced")
    assert replay["native_K152_interval_emitted"] is False; checks.append("K152 interval fenced")
    assert demo["physical_or_source_selection"] is False; checks.append("physical selection fenced")
    assert demo["Born_prediction_or_confirmation_credit"] is False; checks.append("prediction credit fenced")
    return checks


def hostile() -> list[str]:
    cases = [
        (lambda: K165.physical_cell_reduction_obstruction(1, 1), "positive width"),
        (lambda: K165.physical_cell_reduction_obstruction(2, 1), "positive width"),
        (lambda: K165.chart_metric(contraction_upper=-1), "[0,1)"),
        (lambda: K165.chart_metric(contraction_upper=1), "[0,1)"),
        (lambda: K165.separated_auxiliary_budget(auxiliary_shift=0, inverse_chart_bound=1, physical_shift=6), "lambda"),
        (lambda: K165.separated_auxiliary_budget(auxiliary_shift=1, inverse_chart_bound=Fraction(1, 2), physical_shift=6), "inverse"),
        (lambda: K165.separated_auxiliary_budget(auxiliary_shift=1, inverse_chart_bound=1, physical_shift=-1), "physical"),
        (lambda: K165.generalized_complement_count(regular_form=[[0, 1], [0, 1]], metric=[[1, 0], [0, 1]], trial=[1, 0], threshold=1), "symmetric"),
        (lambda: K165.generalized_complement_count(regular_form=[[0, 0], [0, 1]], metric=[[1, 0], [0, -1]], trial=[1, 0], threshold=1), "positive definite"),
        (lambda: K165.generalized_complement_count(regular_form=[[0, 0], [0, 1]], metric=[[1, 0], [0, 1]], trial=[0, 0], threshold=1), "nonzero"),
        (lambda: K165.generalized_complement_count(regular_form=[[2, 0], [0, 3]], metric=[[1, 0], [0, 1]], trial=[1, 0], threshold=1), "strictly below"),
        (lambda: K165.generalized_complement_count(regular_form=[[-1, 0], [0, -2]], metric=[[1, 0], [0, 1]], trial=[1, 0], threshold=0), "not positive"),
        (lambda: K165.absolute_anchor_guard(cutoff_to_limit_tail_ref=None, absolute_anchor_ref="x"), "tail reference"),
        (lambda: K165.absolute_anchor_guard(cutoff_to_limit_tail_ref="K161", absolute_anchor_ref=None), "not an absolute"),
    ]
    caught: list[str] = []
    for index, (case, token) in enumerate(cases, start=1):
        expect_error(case, token)
        caught.append(f"hostile {index} caught")
    return caught


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    checks = baseline()
    print(f"K165 baseline: {len(checks)}/{len(checks)} pass")
    if args.selftest:
        caught = hostile()
        print(f"K165 hostile: {len(caught)}/{len(caught)} caught")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
