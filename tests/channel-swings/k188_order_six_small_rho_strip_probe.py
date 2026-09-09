#!/usr/bin/env python3
"""Independent exact/reporting and hostile controls for K188."""

from __future__ import annotations

import argparse
import copy
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k188-order-six-small-rho-strip-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k188-order-six-small-rho-strip-wave-2026-09-09.md"
SOLVER = ROOT / "tests/channel-swings/k188_order_six_small_rho_strip.py"
K185 = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
K187 = ROOT / "lab/process/k187-order-six-radial-log-endpoint-wave.json"


def fraction(row: dict[str, Any]) -> Fraction:
    return Fraction(int(row["numerator"]), int(row["denominator"]))


def manifest_failures(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    source = json.loads(K185.read_text())
    endpoint = json.loads(K187.read_text())
    fixed = data.get("fixed_control", {})
    cert = data.get("small_radius_certificate", {})
    propagation = data.get("complete_group_propagation", {})
    cover = data.get("domain_cover", {})
    controls = data.get("independent_controls", {})
    release = data.get("release_test", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY": failures.append("classification")
    expected_fixed = (18, 234, 1864, 53, 468, 6, 256)
    actual_fixed = (
        fixed.get("source_coherent_groups"), fixed.get("source_time_gram_entries"),
        fixed.get("source_leibniz_terms"), fixed.get("source_nontrivial_patterns"),
        fixed.get("source_nontrivial_occurrences"), fixed.get("radial_shape"),
        fixed.get("radial_rate"),
    )
    if actual_fixed != expected_fixed: failures.append("fixed_census")
    epsilon = fraction(cert.get("selected_epsilon_fraction", {}))
    x = fraction(cert.get("x_equals_rate_times_epsilon", {}))
    ceiling = fraction(cert.get("normalized_lower_tail_fraction_ceiling", {}))
    expected_ceiling = x**6 / Fraction(720)
    if epsilon != Fraction(1, 2**20) or x != 256 * epsilon: failures.append("split")
    if ceiling != expected_ceiling: failures.append("tail_fraction")
    if not (cert.get("applies_to_all_angular_coordinates") is True and cert.get("depends_on_regularizer_radial_derivatives") is False and cert.get("consumes_k187_log_obstruction_without_differentiating_through_zero") is True): failures.append("endpoint_scope")
    source_groups = source.get("groups", {})
    rows = propagation.get("groups", {})
    if set(rows) != set(source_groups) or len(rows) != 18: failures.append("group_ids")
    small_values = []
    boundary_values = []
    for group_id, row in rows.items():
        if group_id not in source_groups:
            continue
        prior = source_groups[group_id]
        prior_bounds = prior["proof_safe_bounds"]
        whole = fraction(prior_bounds["whole_group_global_ceiling"])
        face = fraction(prior_bounds["any_simplex_coordinate_below_2^-180_group_ceiling"])
        tail = fraction(prior_bounds["rho_greater_than_one_quarter_group_ceiling"])
        small = whole * ceiling
        boundary = small + face + tail
        small_values.append(small)
        boundary_values.append(boundary)
        if row.get("weighted_leibniz_term_count") != prior.get("weighted_leibniz_term_count"): failures.append(f"count:{group_id}")
        if fraction(row.get("whole_group_global_ceiling", {})) != whole: failures.append(f"whole:{group_id}")
        if fraction(row.get("rho_below_2^-20_group_ceiling", {})) != small: failures.append(f"small:{group_id}")
        if fraction(row.get("k185_face_strip_group_ceiling", {})) != face: failures.append(f"face:{group_id}")
        if fraction(row.get("k185_rho_above_one_quarter_group_ceiling", {})) != tail: failures.append(f"tail:{group_id}")
        if fraction(row.get("combined_known_boundary_group_ceiling", {})) != boundary: failures.append(f"sum:{group_id}")
        if row.get("small_strip_below_face_bound") is not True or row.get("small_strip_below_radial_tail_bound") is not True: failures.append(f"comparison:{group_id}")
    if small_values:
        reported = propagation.get("small_radius_group_ceiling_range", {})
        if fraction(reported.get("minimum", {})) != min(small_values) or fraction(reported.get("maximum", {})) != max(small_values): failures.append("small_range")
        reported = propagation.get("combined_known_boundary_group_ceiling_range", {})
        if fraction(reported.get("minimum", {})) != min(boundary_values) or fraction(reported.get("maximum", {})) != max(boundary_values): failures.append("boundary_range")
    required_propagation = (
        "all_18_coherent_groups_covered", "all_234_time_gram_entries_covered",
        "all_1864_leibniz_terms_covered", "all_53_nontrivial_patterns_remain_in_scope",
        "all_468_nontrivial_occurrences_remain_in_scope",
        "every_small_strip_bound_below_face_and_tail_bounds",
    )
    if any(propagation.get(key) is not True for key in required_propagation): failures.append("propagation")
    regions = cover.get("regions", [])
    if [row.get("id") for row in regions] != [
        "small_radius_all_angles", "positive_radius_angular_faces",
        "positive_radius_face_stripped_core", "large_radius_all_angles",
    ]: failures.append("region_ids")
    if [row.get("status") for row in regions] != [
        "OUTWARD_BOUND_CLOSED", "OUTWARD_BOUND_CLOSED",
        "OPEN_DETERMINANT_PRESERVING_INTERVAL_ERROR", "OUTWARD_BOUND_CLOSED",
    ]: failures.append("region_status")
    if cover.get("covers_complete_positive_orthant_after_radialization") is not True or cover.get("only_open_region") != "positive_radius_face_stripped_core" or cover.get("determinants_remain_unexpanded_in_open_numerical_core") is not True: failures.append("cover")
    if controls.get("all_controls_strictly_below_rational_ceiling") is not True or len(controls.get("rows", [])) != 4 or not all(row.get("control_below_ceiling") is True for row in controls.get("rows", [])): failures.append("controls")
    required_true = (
        "outward_small_radius_strip_error_serialized", "positive_split_radius_selected",
        "all_18_groups_and_234_entries_covered", "k185_face_and_radial_tail_bounds_composed",
        "k187_zero_endpoint_derivative_premise_avoided",
        "positive_radius_face_stripped_core_is_only_remaining_order_six_integration_region",
    )
    required_false = (
        "determinant_preserving_positive_radius_core_error_serialized",
        "complete_outward_order_six_total_error_serialized", "accurate_order_six_prefix_released",
        "complete_base_action_column_evaluated", "complete_R_ref_form_dual_residual_serialized",
        "positive_complete_M_orthogonal_complement_or_flux_floor_serialized",
        "scalar_center_left_floor_serialized", "native_K152_interval_emitted",
    )
    if any(release.get(key) is not True for key in required_true): failures.append("release_true")
    if any(release.get(key) is not False for key in required_false): failures.append("release_false")
    if endpoint.get("release_test", {}).get("ordinary_smooth_endpoint_jacobi_remainder_applicable") is not False: failures.append("k187_dependency")
    next_input = data.get("next_exact_input", {})
    if next_input.get("domain") != "2^-20<=rho<=1/4 and z_i>=2^-180" or "without expanding determinants" not in next_input.get("first_gate", ""): failures.append("next_input")
    if not all(str(value).endswith("_UNCHANGED") for value in data.get("ledger_effect", {}).values()): failures.append("ledger")
    if data.get("physical_or_source_selection") is not False: failures.append("physical")
    if data.get("Born_prediction_or_confirmation_credit") is not False: failures.append("Born")
    if data.get("canon_paper_release_or_public_posture_move") is not False: failures.append("public")
    return failures


def exact_checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    text = ARTIFACT.read_text() if ARTIFACT.exists() else ""
    failures = manifest_failures(data)
    return [
        ("manifest", not failures), ("artifact exists", ARTIFACT.exists()),
        ("solver exists", SOLVER.exists()), ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("Gamma inequality", "x^6/720" in text), ("split radius", "2^-20" in text),
        ("complete census", "234 time-Gram entries" in text and "1,864 Leibniz terms" in text),
        ("four-region cover", "four-region" in text),
        ("core remains open", "positive-radius face-stripped core remains open" in text),
        ("prefix withheld", "accurate order-six prefix remains" in text),
        ("ledger unchanged", "SC-META-53" in text and "remain unchanged" in text),
    ] + [(f"no {failure}", False) for failure in failures]


def hostile_checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    mutations = (
        ("wrong_epsilon", lambda d: d["small_radius_certificate"]["selected_epsilon_fraction"].__setitem__("denominator", 2**19)),
        ("wrong_x", lambda d: d["small_radius_certificate"]["x_equals_rate_times_epsilon"].__setitem__("numerator", 2)),
        ("wrong_fraction", lambda d: d["small_radius_certificate"]["normalized_lower_tail_fraction_ceiling"].__setitem__("numerator", 2)),
        ("invent_derivative", lambda d: d["small_radius_certificate"].__setitem__("depends_on_regularizer_radial_derivatives", True)),
        ("drop_group", lambda d: d["complete_group_propagation"]["groups"].pop(next(iter(d["complete_group_propagation"]["groups"]), None))),
        ("wrong_group_bound", lambda d: next(iter(d["complete_group_propagation"]["groups"].values()), {})["rho_below_2^-20_group_ceiling"].__setitem__("numerator", 1)),
        ("wrong_boundary_sum", lambda d: next(iter(d["complete_group_propagation"]["groups"].values()), {})["combined_known_boundary_group_ceiling"].__setitem__("numerator", 1)),
        ("drop_entry_coverage", lambda d: d["complete_group_propagation"].__setitem__("all_234_time_gram_entries_covered", False)),
        ("move_core_status", lambda d: d["domain_cover"]["regions"][2].__setitem__("status", "OUTWARD_BOUND_CLOSED")),
        ("expand_determinants", lambda d: d["domain_cover"].__setitem__("determinants_remain_unexpanded_in_open_numerical_core", False)),
        ("fail_control", lambda d: d["independent_controls"].__setitem__("all_controls_strictly_below_rational_ceiling", False)),
        ("invent_core", lambda d: d["release_test"].__setitem__("determinant_preserving_positive_radius_core_error_serialized", True)),
        ("invent_total", lambda d: d["release_test"].__setitem__("complete_outward_order_six_total_error_serialized", True)),
        ("invent_prefix", lambda d: d["release_test"].__setitem__("accurate_order_six_prefix_released", True)),
        ("invent_action", lambda d: d["release_test"].__setitem__("complete_base_action_column_evaluated", True)),
        ("move_ledger", lambda d: d["ledger_effect"].__setitem__("SC-META-53", "RESOLVED")),
        ("invent_physical", lambda d: d.__setitem__("physical_or_source_selection", True)),
        ("invent_Born", lambda d: d.__setitem__("Born_prediction_or_confirmation_credit", True)),
        ("invent_public", lambda d: d.__setitem__("canon_paper_release_or_public_posture_move", True)),
    )
    results = []
    for name, mutate in mutations:
        broken = copy.deepcopy(data)
        mutate(broken)
        results.append((name, bool(manifest_failures(broken))))
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text())
    checks = exact_checks(data)
    failed = [name for name, ok in checks if not ok]
    if failed:
        print(f"FAIL {len(failed)}/{len(checks)}: {', '.join(failed)}")
        return 1
    if args.selftest:
        hostile = hostile_checks(data)
        missed = [name for name, caught in hostile if not caught]
        if missed:
            print(f"HOSTILE FAIL {len(missed)}/{len(hostile)}: {', '.join(missed)}")
            return 1
        print(f"PASS {len(checks)}/{len(checks)}; hostile {len(hostile)}/{len(hostile)} caught")
        return 0
    print(f"PASS {len(checks)}/{len(checks)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
