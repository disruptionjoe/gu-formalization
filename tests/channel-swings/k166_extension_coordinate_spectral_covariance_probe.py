#!/usr/bin/env python3
"""Baseline-first probe and hostile inputs for the K166 certificate."""

from __future__ import annotations

import argparse
import importlib.util
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent


def _load():
    path = HERE / "k166_extension_coordinate_spectral_covariance.py"
    spec = importlib.util.spec_from_file_location("k166_solver", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K166 solver")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K166 = _load()


def expect_error(callable_, token: str) -> None:
    try:
        callable_()
    except (K166.CertificateError, K166.K155.CertificateError, K166.K165.CertificateError) as exc:
        if token not in str(exc):
            raise AssertionError(f"wrong failure: {exc}") from exc
    else:
        raise AssertionError(f"expected failure containing {token!r}")


def baseline() -> list[str]:
    checks: list[str] = []
    finite = K166.regular_extension_covariance(
        energies=["5/4", "3/2"], couplings=[1, 1], charge=(0, 0),
        auxiliary_shift=256, extension_shift=7,
    )
    assert finite["dimension"] == 84; checks.append("complete K155 block used")
    assert finite["extension_shift"] == "7"; checks.append("extension shift exact")
    assert finite["chart_independent_of_scalar_extension"] is True; checks.append("chart fixed")
    assert finite["regular_form_identity"] == "R_E=R_0+E M"; checks.append("affine identity typed")
    assert finite["identity_exact"] is True; checks.append("finite identity exact")
    assert finite["finite_control_only"] is True; checks.append("finite scope fenced")

    regular = [[-2, 1, 1], [1, 6, 0], [1, 0, 5]]
    metric = [[2, 1, 0], [1, 2, 0], [0, 0, 1]]
    pencil = K166.pencil_covariance(
        regular_form=regular, metric=metric, extension_shift=7, base_parameter=0
    )
    assert pencil["translated_parameter"] == "7"; checks.append("threshold translated")
    assert pencil["identity"] == "R_E-(z+E)M=R_0-zM"; checks.append("pencil covariance typed")
    assert pencil["inertia"] == [1, 0, 2]; checks.append("translated inertia exact")

    trial = K166.trial_covariance(
        regular_form=regular, metric=metric, trial=[1, 0, 0], extension_shift=7
    )
    assert trial["metric_norm"] == "2"; checks.append("physical Gram exact")
    assert trial["base_rayleigh"] == "-1"; checks.append("base Rayleigh exact")
    assert trial["translated_rayleigh"] == "6"; checks.append("Rayleigh translation exact")
    assert trial["rayleigh_shift"] == "7"; checks.append("Rayleigh shift recorded")
    assert trial["matched_residual_covector_invariant"] is True; checks.append("residual invariant")
    assert trial["residual_covector"] == ["0", "2", "1"]; checks.append("residual covector exact")

    exterior = K166.complement_covariance(
        regular_form=regular, metric=metric, trial=[1, 0, 0],
        base_threshold=0, extension_shift=7,
    )
    assert exterior["complement_kind"] == "M-orthogonal"; checks.append("physical complement retained")
    assert exterior["complement_dimension"] == 2; checks.append("complement dimension exact")
    assert exterior["translated_threshold"] == "7"; checks.append("complement threshold translated")
    assert exterior["complement_form_invariant_at_translated_threshold"] is True; checks.append("complement form invariant")
    assert exterior["complement_inertia"] == [0, 0, 2]; checks.append("complement inertia retained")

    floors = K166.absolute_floor_nonidentifiability(base_floor=-4, absolute_threshold=-5)
    assert floors["below_extension"] == "-2"; checks.append("below witness exact")
    assert floors["below_translated_floor"] == "-6"; checks.append("below threshold crossed")
    assert floors["above_extension"] == "0"; checks.append("above witness exact")
    assert floors["above_translated_floor"] == "-4"; checks.append("above threshold crossed")
    assert floors["absolute_floor_selected_without_extension"] is False; checks.append("absolute floor refused")
    assert floors["spectral_gap_is_translation_invariant"] is True; checks.append("gap role preserved")

    selected = K166.selected_absolute_floor(
        base_floor=-4, extension_value=2, extension_selection_ref="response#full-rank-W"
    )
    assert selected["absolute_floor"] == "-2"; checks.append("selected floor translated")
    assert selected["extension_selection_ref"] == "response#full-rank-W"; checks.append("selection owner retained")

    replay = K166.k152_coordinate_replay(
        relative_form_and_gram_ref="relative-form",
        relative_residual_ref="relative-residual",
        relative_gap_ref="relative-gap",
        full_extension_selection_ref=None,
        absolute_anchor_coercivity_ref=None,
        absolute_next_distinct_floor_ref=None,
        absolute_native_left_floor_ref=None,
    )
    assert replay["coordinate_free_form_gram_may_proceed"] is True; checks.append("relative form work retained")
    assert replay["matched_form_dual_residual_may_proceed"] is True; checks.append("relative residual work retained")
    assert replay["relative_spectral_gap_may_proceed"] is True; checks.append("relative gap work retained")
    assert len(replay["missing_absolute_references"]) == 4; checks.append("absolute omissions complete")
    assert replay["native_absolute_packet_complete"] is False; checks.append("absolute packet fail closed")
    assert replay["native_K152_absolute_interval_emitted"] is False; checks.append("K152 interval fenced")

    demo = K166.demo()
    assert demo["physical_or_source_selection"] is False; checks.append("physical selection fenced")
    assert demo["Born_prediction_or_confirmation_credit"] is False; checks.append("prediction credit fenced")
    return checks


def hostile() -> list[str]:
    regular = [[-2, 1], [1, 3]]
    metric = [[2, 0], [0, 1]]
    cases = [
        (lambda: K166.pencil_covariance(regular_form=[[0, 1], [0, 1]], metric=metric, extension_shift=1, base_parameter=0), "symmetric"),
        (lambda: K166.pencil_covariance(regular_form=regular, metric=[[1, 0], [0, -1]], extension_shift=1, base_parameter=0), "positive definite"),
        (lambda: K166.pencil_covariance(regular_form=[[0]], metric=metric, extension_shift=1, base_parameter=0), "dimensions"),
        (lambda: K166.trial_covariance(regular_form=regular, metric=metric, trial=[0, 0], extension_shift=1), "nonzero"),
        (lambda: K166.trial_covariance(regular_form=regular, metric=metric, trial=[1], extension_shift=1), "match"),
        (lambda: K166.trial_covariance(regular_form=regular, metric=[[1, 0], [0, -1]], trial=[1, 0], extension_shift=1), "positive definite"),
        (lambda: K166.complement_covariance(regular_form=[[0, 1], [0, 1]], metric=metric, trial=[1, 0], base_threshold=0, extension_shift=1), "symmetric"),
        (lambda: K166.complement_covariance(regular_form=regular, metric=[[1, 0], [0, -1]], trial=[1, 0], base_threshold=0, extension_shift=1), "positive definite"),
        (lambda: K166.complement_covariance(regular_form=regular, metric=metric, trial=[0, 0], base_threshold=0, extension_shift=1), "nonzero"),
        (lambda: K166.selected_absolute_floor(base_floor=-4, extension_value=None, extension_selection_ref="x"), "selected extension"),
        (lambda: K166.selected_absolute_floor(base_floor=-4, extension_value=0, extension_selection_ref=None), "selected extension"),
        (lambda: K166.absolute_floor_nonidentifiability(base_floor="bad", absolute_threshold=-5), "invalid rational"),
        (lambda: K166.regular_extension_covariance(energies=[], couplings=[], charge=(0, 0), auxiliary_shift=256, extension_shift=1), "same nonzero"),
        (lambda: K166.regular_extension_covariance(energies=[1], couplings=[1], charge=(0, 0), auxiliary_shift=0, extension_shift=1), "positive"),
        (lambda: K166.regular_extension_covariance(energies=[1], couplings=[1, 1], charge=(0, 0), auxiliary_shift=256, extension_shift=1), "same nonzero"),
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
    print(f"K166 baseline: {len(checks)}/{len(checks)} pass")
    if args.selftest:
        caught = hostile()
        print(f"K166 hostile: {len(caught)}/{len(caught)} caught")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
