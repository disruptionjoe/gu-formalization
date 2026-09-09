#!/usr/bin/env python3
"""Baseline-first exact and hostile controls for K170."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k170_direct_gram_reference_shape_slice.py")
MANIFEST = ROOT / "lab/process/k170-direct-gram-reference-shape-slice-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k170-direct-gram-reference-shape-slice-wave-2026-09-09.md"


def load_solver():
    spec = importlib.util.spec_from_file_location("k170_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K170 solver")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K170 = load_solver()


def q(value: str) -> Fraction:
    return Fraction(value)


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    theorem = data.get("orthogonal_word_theorem", {})
    release = data.get("release_test", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("classification")
    required_true = (
        "G_raises_bath_particle_number_by_exactly_one",
        "distinct_word_sectors_orthogonal",
        "squared_geometric_tail_valid",
        "limiting_physical_Gram_not_finite_chart",
    )
    if any(theorem.get(key) is not True for key in required_true):
        failures.append("orthogonal word theorem")
    for key in (
        "physical_Gram_seed_entries_evaluated",
        "reference_shape_seed_form_evaluated",
        "trial_specific_shape_residual_evaluated",
    ):
        if release.get(key) is not True:
            failures.append(key)
    for key in (
        "coefficient_complete_base_R0_action_serialized",
        "complete_R_ref_form_dual_residual_serialized",
        "positive_complete_M_orthogonal_complement_or_flux_floor_serialized",
        "native_left_floor_at_selected_scalar_center_serialized",
        "native_K152_interval_emitted",
    ):
        if release.get(key) is not False:
            failures.append(key)
    bounds = data.get("boundaries", {})
    if any(bounds.get(key) is not False for key in (
        "physical_extension_or_scalar_center_selected", "first_threshold_identified",
        "source_or_ledger_status_moved", "Born_rule_derived",
        "prediction_or_confirmation_credit", "canon_paper_release_or_public_posture_move",
    )):
        failures.append("boundaries")
    return failures


def checks(data: dict, text: str) -> list[tuple[str, bool]]:
    result = K170.demo()
    slices = {tuple(row["charge"]): row for row in result["native_seed_slices"]}
    q00, q10, q01 = slices[(0, 0)], slices[(1, 0)], slices[(0, 1)]
    profile = list(map(q, result["fixed_control"]["one_transition_profile_norm_sq_interval"]))
    a = 256
    numerical = (a * math.sqrt(a * a - 1) - math.acosh(a)) / (math.pi * (a * a - 1) ** 1.5)
    generic_low, generic_high = Fraction(64, 121), Fraction(64, 25)
    return [
        ("schema", result.get("schema_version") == "1.0"),
        ("manifest", not manifest_failures(data)),
        ("profile positive", 0 < profile[0] < profile[1]),
        ("profile encloses independent float", float(profile[0]) < numerical < float(profile[1])),
        ("profile interval narrow", profile[1] - profile[0] < Fraction(1, 10_000_000)),
        ("particle-number raising", result["orthogonal_word_theorem"]["G_raises_bath_particle_number_by_exactly_one"] is True),
        ("orthogonal Gram sum", result["orthogonal_word_theorem"]["physical_Gram_identity"] == "<phi,S* S phi>=sum_(n>=0)||G^n phi||^2"),
        ("squared tail exact", q(result["orthogonal_word_theorem"]["tail_from_word_two_upper"]) == Fraction(81, 3520)),
        ("no finite chart substitution", result["orthogonal_word_theorem"]["compressed_finite_chart_used"] is False),
        ("vacuum multiplicity", q00["first_word_multiplicity"] == 2),
        ("occupied multiplicity", q10["first_word_multiplicity"] == 1),
        ("vacuum first word doubled", q(q00["first_word_norm_sq_interval"][0]) == 2 * profile[0] and q(q00["first_word_norm_sq_interval"][1]) == 2 * profile[1]),
        ("q10/q01 symmetry", q10["physical_Gram_interval"] == q01["physical_Gram_interval"]),
        ("native Gram improves generic lower bound", generic_low < q(q00["physical_Gram_interval"][0]) < q(q00["physical_Gram_interval"][1]) < generic_high),
        ("q10 native Gram bounded", generic_low < q(q10["physical_Gram_interval"][0]) < q(q10["physical_Gram_interval"][1]) < generic_high),
        ("vacuum dressed shape fenced", -2 < q(q00["dressed_reference_shape_Rayleigh_interval"][0]) < q(q00["dressed_reference_shape_Rayleigh_interval"][1]) < 1),
        ("occupied dressed shape fenced", -2 < q(q10["dressed_reference_shape_Rayleigh_interval"][0]) < q(q10["dressed_reference_shape_Rayleigh_interval"][1]) < 1),
        ("shape residual improves worst case", q(q00["matched_M_inverse_residual_sq_upper"]) < 1 and q(q10["matched_M_inverse_residual_sq_upper"]) < 1),
        ("shape residual not complete", q00["complete_R_ref_residual"] is False and q10["complete_R_ref_residual"] is False),
        ("release remains closed", result["release_test"]["coefficient_complete_base_R0_action_serialized"] is False and result["release_test"]["native_K152_interval_emitted"] is False),
        ("no physical selection", result["physical_or_source_selection"] is False),
        ("no Born/export credit", result["Born_prediction_or_confirmation_credit"] is False),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification prose", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("exact Gram identity prose", "sum_(n>=0)||G^n phi||^2" in text),
        ("finite chart fence prose", "not a compressed finite-\nchart Gram" in text),
        ("reference-only fence prose", "not the complete `R_ref` residual" in text),
        ("next base gate prose", "coefficient-complete combined base action `R_0 phi`" in text),
        ("threshold fence prose", "does not identify the first threshold" in text),
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text())
    text = ARTIFACT.read_text()
    baseline = checks(data, text)
    failed = [name for name, ok in baseline if not ok]
    if failed:
        print(f"FAIL baseline {len(baseline)-len(failed)}/{len(baseline)}: {failed}")
        return 1
    if not args.selftest:
        print(f"PASS {len(baseline)}/{len(baseline)} K170 exact controls")
        return 0

    manifest_mutations = [
        lambda d: d.__setitem__("classification", "SOURCE_NATIVE"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["orthogonal_word_theorem"].__setitem__("G_raises_bath_particle_number_by_exactly_one", False),
        lambda d: d["orthogonal_word_theorem"].__setitem__("distinct_word_sectors_orthogonal", False),
        lambda d: d["orthogonal_word_theorem"].__setitem__("limiting_physical_Gram_not_finite_chart", False),
        lambda d: d["release_test"].__setitem__("physical_Gram_seed_entries_evaluated", False),
        lambda d: d["release_test"].__setitem__("coefficient_complete_base_R0_action_serialized", True),
        lambda d: d["release_test"].__setitem__("complete_R_ref_form_dual_residual_serialized", True),
        lambda d: d["release_test"].__setitem__("positive_complete_M_orthogonal_complement_or_flux_floor_serialized", True),
        lambda d: d["release_test"].__setitem__("native_K152_interval_emitted", True),
        lambda d: d["boundaries"].__setitem__("physical_extension_or_scalar_center_selected", True),
        lambda d: d["boundaries"].__setitem__("prediction_or_confirmation_credit", True),
    ]
    prose_mutations = [
        text.replace("GU-COMPARATOR-ROUTING", "ROUTING", 1),
        text.replace("Classification: INTERNAL_STRUCTURAL_ONLY.", "", 1),
        text.replace("```gu-typed-objects", "```text", 1),
        text.replace("sum_(n>=0)||G^n phi||^2", "1", 1),
        text.replace("not a compressed finite-\nchart Gram", "a finite-chart identity Gram", 1),
        text.replace("not the complete `R_ref` residual", "the complete `R_ref` residual", 1),
        text.replace("coefficient-complete combined base action `R_0 phi`", "finite cutoff", 1),
        text.replace("does not identify the first threshold", "identifies the first threshold", 1),
    ]
    caught = 0
    missed: list[str] = []
    for index, mutate in enumerate(manifest_mutations, start=1):
        trial = copy.deepcopy(data)
        mutate(trial)
        if any(not ok for _, ok in checks(trial, text)):
            caught += 1
        else:
            missed.append(f"manifest-{index}")
    for index, trial_text in enumerate(prose_mutations, start=1):
        if any(not ok for _, ok in checks(data, trial_text)):
            caught += 1
        else:
            missed.append(f"prose-{index}")
    total = len(manifest_mutations) + len(prose_mutations)
    if caught != total:
        print(f"FAIL hostile selftest caught {caught}/{total}; missed {missed}")
        return 1
    print(f"PASS hostile selftest caught {caught}/{total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
