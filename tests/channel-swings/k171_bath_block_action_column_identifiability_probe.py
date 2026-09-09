#!/usr/bin/env python3
"""Baseline-first exact and hostile controls for K171."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k171_bath_block_action_column_identifiability.py")
MANIFEST = ROOT / "lab/process/k171-bath-block-action-column-identifiability-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k171-bath-block-action-column-identifiability-wave-2026-09-09.md"


def load_solver():
    spec = importlib.util.spec_from_file_location("k171_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K171 solver")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K171 = load_solver()


def q(value: str) -> Fraction:
    return Fraction(value)


def rejects(call) -> bool:
    try:
        call()
    except K171.CertificateError:
        return True
    return False


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    formula = data.get("bath_block_formula", {})
    counter = data.get("identifiability_counterexample", {})
    interface = data.get("minimum_native_column_interface", {})
    release = data.get("release_test", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    for key in (
        "G_raises_bath_number_by_exactly_one",
        "base_regular_core_preserves_bath_number",
        "G_star_lowers_bath_number_by_exactly_one",
        "K170_scalar_word_orthogonality_determines_Gram",
    ):
        if formula.get(key) is not True:
            failures.append(key)
    if formula.get("K170_scalar_word_orthogonality_determines_action_column") is not False:
        failures.append("scalar action inference")
    for key in (
        "same_boundary_map_and_word_norms", "same_physical_Gram",
        "same_seed_base_form_and_generalized_Rayleigh", "same_reference_shape_data",
        "different_complete_base_action_columns", "different_matched_M_inverse_residuals",
        "finite_algebraic_control_only",
    ):
        if counter.get(key) is not True:
            failures.append(key)
    for key in ("requires_vector_blocks_W_n_Gn_phi", "requires_complete_sum_norm_tail"):
        if interface.get(key) is not True:
            failures.append(key)
    for key in ("scalar_word_norms_or_form_expectations_are_sufficient", "finite_regulator_column_is_native_without_cofinal_transfer"):
        if interface.get(key) is not False:
            failures.append(key)
    if release.get("K170_physical_Gram_seed_entries_evaluated") is not True or release.get("K156_limiting_normal_ordered_base_core_exists") is not True:
        failures.append("predecessor release")
    for key in (
        "native_vector_blocks_W_n_Gn_phi_serialized",
        "complete_native_vector_block_tail_serialized",
        "coefficient_complete_base_R0_action_column_serialized",
        "complete_R_ref_form_dual_residual_serialized",
        "positive_complete_M_orthogonal_complement_or_flux_floor_serialized",
        "native_left_floor_at_selected_scalar_center_serialized",
        "native_K152_interval_emitted",
    ):
        if release.get(key) is not False:
            failures.append(key)
    boundaries = data.get("boundaries", {})
    if any(boundaries.get(key) is not False for key in (
        "physical_extension_or_scalar_center_selected", "first_threshold_identified",
        "source_or_ledger_status_moved", "Born_rule_derived",
        "prediction_or_confirmation_credit", "canon_paper_release_or_public_posture_move",
    )):
        failures.append("boundaries")
    return failures


def checks(data: dict, text: str) -> list[tuple[str, bool]]:
    result = K171.demo()
    release_failure = " ".join(result["scalar_only_native_release_failure"].split())
    control = result["identifiability_control"]
    positive = result["vector_tail_positive_control"]
    release = result["native_release_audit"]
    bad_boundary = [[0, 1], [0, 0]]
    bad_core = [[0, 1], [1, 0]]
    return [
        ("schema", result.get("schema_version") == "1.0"),
        ("manifest", not manifest_failures(data)),
        ("formula", result["exact_component_formula"] == "P_k R0 phi=P_k A phi+sum_(n>=k) P_k (G*)^(n-k) W_n G^n phi"),
        ("G raises", result["bath_number_roles"]["G"] == "raises exactly one"),
        ("W preserves", result["bath_number_roles"]["W"] == "preserves bath number"),
        ("Gstar lowers", result["bath_number_roles"]["Gstar"] == "lowers exactly one"),
        ("Gram determined", result["bath_number_roles"]["K170_word_orthogonality_determines_Gram"] is True),
        ("column not determined", result["bath_number_roles"]["K170_word_orthogonality_diagonalizes_action_column"] is False),
        ("word norms", list(map(q, control["word_norm_sq"])) == [1, Fraction(1, 16), Fraction(1, 400)]),
        ("same Gram", control["same_physical_Gram"] is True),
        ("same form", q(control["same_seed_base_form"]) == Fraction(227, 200)),
        ("same Rayleigh", q(control["same_generalized_rayleigh"]) == Fraction(227, 213)),
        ("same shape", control["same_reference_shape_data"] is True),
        ("columns differ", control["action_columns_differ"] is True and control["baseline_action_column"] != control["rotated_action_column"]),
        ("orthogonal component", q(control["baseline_action_column"][2]) == 0 and q(control["rotated_action_column"][2]) == Fraction(1, 4)),
        ("residuals differ", control["matched_residuals_differ"] is True),
        ("dual residual values", q(control["baseline_matched_M_dual_residual_sq"]) == Fraction(137, 1704) and q(control["rotated_matched_M_dual_residual_sq"]) == Fraction(487, 3408)),
        ("finite fence", control["finite_algebraic_control_only"] is True),
        ("scalar native rejected", "scalar word norms do not identify" in release_failure),
        ("adjoint inverse factor", q(positive["inverse_adjoint_norm_upper"]) == Fraction(8, 5)),
        ("tail factor", q(positive["unresolved_column_tail_upper"]) == Fraction(1, 40)),
        ("positive interface", positive["complete_action_column_certified"] is True),
        ("native vector missing", release["native_vectors_W_n_Gn_phi_serialized"] is False),
        ("native tail missing", release["complete_sum_norm_tail_for_those_vectors_serialized"] is False),
        ("K152 closed", release["complete_R0_action_column_serialized"] is False and release["native_K152_interval_emitted"] is False),
        ("reject wrong G grading", rejects(lambda: K171.graded_action_column(boundary_rows=bad_boundary, regular_core_rows=[[1, 0], [0, 1]], shifted_free_rows=[[1, 0], [0, 1]], seed_values=[1, 0], sectors=[0, 1]))),
        ("reject W mixing sectors", rejects(lambda: K171.graded_action_column(boundary_rows=[[0, 0], [1, 0]], regular_core_rows=bad_core, shifted_free_rows=[[1, 0], [0, 1]], seed_values=[1, 0], sectors=[0, 1]))),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification prose", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("component identity prose", "P_k R_0 phi" in text and "(G*)^(n-k) W_n g_n" in text),
        ("interference prose", "Terms\nwith different `n` can land in the same output sector `k` and interfere." in text),
        ("native finite fence prose", "countercontrols, not native continuum" in text),
        ("next vector gate", "Serialize the coefficient-specific continuum vectors `W_n G^n phi`" in text),
        ("threshold fence", "does not\nidentify the first threshold" in text),
        ("no physical selection", result["physical_or_source_selection"] is False),
        ("no export credit", result["Born_prediction_or_confirmation_credit"] is False),
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
        print(f"PASS {len(baseline)}/{len(baseline)} K171 exact controls")
        return 0

    manifest_mutations = [
        lambda d: d.__setitem__("classification", "SOURCE_NATIVE"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["bath_block_formula"].__setitem__("G_raises_bath_number_by_exactly_one", False),
        lambda d: d["bath_block_formula"].__setitem__("base_regular_core_preserves_bath_number", False),
        lambda d: d["bath_block_formula"].__setitem__("K170_scalar_word_orthogonality_determines_action_column", True),
        lambda d: d["identifiability_counterexample"].__setitem__("same_physical_Gram", False),
        lambda d: d["identifiability_counterexample"].__setitem__("different_complete_base_action_columns", False),
        lambda d: d["identifiability_counterexample"].__setitem__("different_matched_M_inverse_residuals", False),
        lambda d: d["minimum_native_column_interface"].__setitem__("requires_vector_blocks_W_n_Gn_phi", False),
        lambda d: d["minimum_native_column_interface"].__setitem__("scalar_word_norms_or_form_expectations_are_sufficient", True),
        lambda d: d["release_test"].__setitem__("coefficient_complete_base_R0_action_column_serialized", True),
        lambda d: d["release_test"].__setitem__("native_K152_interval_emitted", True),
        lambda d: d["boundaries"].__setitem__("physical_extension_or_scalar_center_selected", True),
        lambda d: d["boundaries"].__setitem__("prediction_or_confirmation_credit", True),
    ]
    prose_mutations = [
        text.replace("GU-COMPARATOR-ROUTING", "ROUTING", 1),
        text.replace("Classification: INTERNAL_STRUCTURAL_ONLY.", "", 1),
        text.replace("```gu-typed-objects", "```text", 1),
        text.replace("P_k R_0 phi", "P_k phi", 1),
        text.replace("Terms\nwith different `n` can land in the same output sector `k` and interfere.", "Terms remain orthogonal after adjoint lowering.", 1),
        text.replace("countercontrols, not native continuum", "native continuum", 1),
        text.replace("Serialize the coefficient-specific continuum vectors `W_n G^n phi`", "Reuse scalar word norms", 1),
        text.replace("does not\nidentify the first threshold", "identifies the first threshold", 1),
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
