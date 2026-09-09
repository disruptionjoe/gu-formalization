#!/usr/bin/env python3
"""Exact/reporting and hostile controls for the K184 order-six certificate."""

from __future__ import annotations

import argparse
import copy
import json
from decimal import Decimal
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k184-order-six-certified-low-rank-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k184-order-six-certified-low-rank-wave-2026-09-09.md"
SOLVER = ROOT / "tests/channel-swings/k184_order_six_certified_low_rank.py"


def first_key(mapping: dict[str, Any]) -> str:
    key = next(iter(mapping), None)
    if key is None:
        raise ValueError("hostile mutation requires a nonempty mapping")
    return key


def first_value(mapping: dict[str, Any]) -> Any:
    return mapping[first_key(mapping)]


def manifest_failures(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    family = data.get("canonical_order_six_family", {})
    global_certificate = family.get("global_certificate", {})
    formula = family.get("contracted_formula_control", {})
    time_gram = data.get("andreief_time_gram_certificate", {})
    witnesses = data.get("localized_interval_witnesses", {})
    projection = data.get("finite_rank_projection_certificate", {})
    intervals = data.get("certified_coherent_norm_squared_intervals", {})
    control = data.get("independent_numerical_control", {})
    release = data.get("release_test", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY": failures.append("classification")
    if data.get("fixed_control", {}).get("coefficient_family_sha256") != "ee24469ef5c6bb8d606efe1d529b294cbc7097b14adc51df80a51627aa7eb686": failures.append("K179_pin")
    if data.get("fixed_control", {}).get("resolved_order") != 6: failures.append("resolved_order")
    if (family.get("terms"), family.get("groups"), family.get("unique_self_and_cross_entries")) != (72, 18, 234): failures.append("family_census")
    if family.get("group_size_histogram") != {"1": 2, "2": 4, "3": 4, "4": 2, "5": 2, "7": 2, "9": 2}: failures.append("group_histogram")
    if family.get("contracted_position_histogram") != {"1": 24, "3": 24, "5": 24}: failures.append("position_histogram")
    rows = family.get("canonical_groups", [])
    path_ids = [path.get("contraction_id") for row in rows for path in row.get("paths", [])]
    if len(rows) != 18 or len(path_ids) != 72 or len(set(path_ids)) != 72: failures.append("path_identity")
    if any(path.get("coefficient") not in (-1, 1) or path.get("old_position") not in (1, 3, 5) for row in rows for path in row.get("paths", [])): failures.append("path_pin")
    if global_certificate.get("all_18_groups_enclosed") is not True: failures.append("global_groups")
    if global_certificate.get("unique_self_and_cross_entries_all_groups") != 234: failures.append("global_gram_count")
    if global_certificate.get("all_bounds_after_complete_specieswise_antisymmetrization") is not True: failures.append("cancellation_order")
    for group_id, row in global_certificate.get("groups", {}).items():
        if row.get("coherent_norm_squared_upper", 0) <= 0 or row.get("coherent_outside_symmetric_box_norm_squared_upper", 0) <= 0: failures.append(f"global_bound:{group_id}")
        for bound in row.get("path_majorants", {}).values():
            exponents = {int(key): float(value) for key, value in bound.get("energy_exponents", {}).items()}
            old = int(bound.get("old_position", -1))
            if exponents.get(old, 0) <= 1 or any(2 * value <= 1 for key, value in exponents.items() if key != old): failures.append(f"integrability:{group_id}")
            if bound.get("formed_after_complete_exterior_antisymmetrizer") is not True: failures.append(f"path_cancellation:{group_id}")
    if formula.get("maximum_relative_difference", 1) >= 1e-9 or len(formula.get("rows", [])) != 3: failures.append("contracted_formula")
    if time_gram.get("all_234_entries_reduced") is not True: failures.append("time_gram_count")
    if time_gram.get("all_factorial_normalizations_cancel") is not True: failures.append("factorial_cancel")
    if len(time_gram.get("gram_entries", [])) != 234: failures.append("time_gram_rows")
    if time_gram.get("maximum_control_relative_difference", 1) >= 1e-10: failures.append("andreief_control")
    if time_gram.get("radialization", {}).get("small_rho_power_after_eight_crude_bessel_factors") != 5: failures.append("small_rho_power")
    if time_gram.get("radialization", {}).get("small_rho_integrable_without_using_determinant_cancellation") is not True: failures.append("radial_integrability")
    if witnesses.get("groups_with_nonzero_local_witness") != 18: failures.append("witness_count")
    if witnesses.get("complete_coherent_coordinate_before_interval_sum") is not True: failures.append("witness_order")
    if projection.get("rank_per_group") != 729: failures.append("projection_rank")
    if projection.get("all_234_gram_entries_have_deterministic_error_intervals") is not True: failures.append("projection_gram")
    if len(projection.get("groups", {})) != 18: failures.append("projection_groups")
    for group_id, row in projection.get("groups", {}).items():
        if row.get("coherent_remainder_norm_squared_upper", 0) <= 0: failures.append(f"projection_error:{group_id}")
        if len(row.get("gram_entries", [])) != row.get("path_projections", {}).__len__() * (row.get("path_projections", {}).__len__() + 1) // 2: failures.append(f"projection_entries:{group_id}")
        for entry in row.get("gram_entries", []):
            lo, hi = entry.get("certified_interval", [1, 0])
            if not lo <= entry.get("projection_value", 0) <= hi or entry.get("absolute_error_upper", 0) < 0: failures.append(f"gram_interval:{group_id}")
    if len(intervals) != 18: failures.append("interval_count")
    for group_id, pair in intervals.items():
        lo, hi = map(Decimal, pair)
        if not Decimal(0) < lo < hi: failures.append(f"certified_interval:{group_id}")
    comparisons = control.get("comparisons", {})
    if len(comparisons) != 18: failures.append("control_groups")
    if any(row.get("fine_inside_certified_interval") is not True for row in comparisons.values()): failures.append("control_outward")
    if any(not 0 <= row.get("coarse_fine_relative_difference", 1) < 0.60 for row in comparisons.values()): failures.append("control_convergence")
    seeds = control.get("seedwise_order_six_norms_squared", {})
    if set(seeds) != {"0", "1", "2"} or not all(value > 0 for value in seeds.values()): failures.append("seed_norms")
    if abs(seeds.get("1", 0) - seeds.get("2", 1)) / max(seeds.get("1", 0), seeds.get("2", 0), 1e-300) >= 0.10: failures.append("seed_symmetry")
    required_true = (
        "all_72_order_six_paths_mapped", "all_18_output_groups_assembled",
        "all_234_gram_entries_have_deterministic_intervals",
        "all_group_norms_have_positive_local_witnesses",
        "finite_rank_projection_has_complete_remainder_bound",
        "all_234_gram_entries_reduced_to_factorial_free_time_determinants",
        "radial_time_integrand_has_proved_integrable_small_radius_power",
    )
    required_false = (
        "projection_error_is_decision_grade_for_action_columns",
        "coefficient_complete_base_action_column_evaluated",
        "complete_R_ref_form_dual_residual_serialized",
        "positive_complete_M_orthogonal_complement_or_flux_floor_serialized",
        "scalar_center_left_floor_serialized", "native_K152_interval_emitted",
    )
    if any(release.get(key) is not True for key in required_true): failures.append("release_true")
    if any(release.get(key) is not False for key in required_false): failures.append("release_false")
    if not all(str(value).endswith("_UNCHANGED") for value in data.get("ledger_effect", {}).values()): failures.append("ledger")
    if data.get("physical_or_source_selection") is not False: failures.append("physical")
    if data.get("Born_prediction_or_confirmation_credit") is not False: failures.append("Born")
    if data.get("canon_paper_release_or_public_posture_move") is not False: failures.append("public")
    return failures


def exact_checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    text = ARTIFACT.read_text()
    failures = manifest_failures(data)
    return [
        ("manifest", not failures), ("artifact exists", ARTIFACT.exists()), ("solver exists", SOLVER.exists()),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("72 paths", "72 coefficient-complete paths" in text),
        ("18 groups", "18 coherent output groups" in text),
        ("234 Gram", "234 unique self/cross Gram entries" in text),
        ("cancellation first", "before any interval operation" in text),
        ("all nonzero", "all 18 coherent groups are nonzero" in text),
        ("projection ceiling", "not decision-grade" in text),
        ("Andreief", "Andréief" in text),
        ("radial power", "rho^5" in text),
        ("control role", "not the outward proof" in text),
        ("action fenced", "K171/K168 action columns" in text),
        ("ledger unchanged", "SC-META-53" in text and "remain unchanged" in text),
    ] + [(f"no {failure}", False) for failure in failures]


def hostile_checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    updates = (
        ("change_pin", lambda d: d["fixed_control"].__setitem__("coefficient_family_sha256", "0" * 64)),
        ("drop_path", lambda d: d["canonical_order_six_family"].__setitem__("terms", 71)),
        ("merge_group", lambda d: d["canonical_order_six_family"].__setitem__("groups", 17)),
        ("erase_gram", lambda d: d["canonical_order_six_family"].__setitem__("unique_self_and_cross_entries", 233)),
        ("change_histogram", lambda d: d["canonical_order_six_family"]["group_size_histogram"].__setitem__("9", 1)),
        ("change_position", lambda d: d["canonical_order_six_family"]["contracted_position_histogram"].__setitem__("5", 23)),
        ("pre_cancel", lambda d: d["canonical_order_six_family"]["global_certificate"].__setitem__("all_bounds_after_complete_specieswise_antisymmetrization", False)),
        ("break_integrability", lambda d: first_value(first_value(d["canonical_order_six_family"]["global_certificate"]["groups"])["path_majorants"])["energy_exponents"].__setitem__("1", 0.4)),
        ("break_formula", lambda d: d["canonical_order_six_family"]["contracted_formula_control"].__setitem__("maximum_relative_difference", 1.0)),
        ("erase_time_gram", lambda d: d["andreief_time_gram_certificate"].__setitem__("all_234_entries_reduced", False)),
        ("break_factorial", lambda d: d["andreief_time_gram_certificate"].__setitem__("all_factorial_normalizations_cancel", False)),
        ("break_andreief", lambda d: d["andreief_time_gram_certificate"].__setitem__("maximum_control_relative_difference", 1.0)),
        ("break_radial", lambda d: d["andreief_time_gram_certificate"]["radialization"].__setitem__("small_rho_power_after_eight_crude_bessel_factors", -1)),
        ("erase_witness", lambda d: d["localized_interval_witnesses"].__setitem__("groups_with_nonzero_local_witness", 17)),
        ("change_rank", lambda d: d["finite_rank_projection_certificate"].__setitem__("rank_per_group", 1)),
        ("erase_projected_gram", lambda d: d["finite_rank_projection_certificate"].__setitem__("all_234_gram_entries_have_deterministic_error_intervals", False)),
        ("zero_lower", lambda d: d["certified_coherent_norm_squared_intervals"][first_key(d["certified_coherent_norm_squared_intervals"])].__setitem__(0, 0)),
        ("break_control", lambda d: d["independent_numerical_control"]["comparisons"][first_key(d["independent_numerical_control"]["comparisons"])].__setitem__("fine_inside_certified_interval", False)),
        ("invent_decision_grade", lambda d: d["release_test"].__setitem__("projection_error_is_decision_grade_for_action_columns", True)),
        ("invent_action", lambda d: d["release_test"].__setitem__("coefficient_complete_base_action_column_evaluated", True)),
        ("invent_residual", lambda d: d["release_test"].__setitem__("complete_R_ref_form_dual_residual_serialized", True)),
        ("invent_K152", lambda d: d["release_test"].__setitem__("native_K152_interval_emitted", True)),
        ("move_ledger", lambda d: d["ledger_effect"].__setitem__("SC-META-53", "RESOLVED")),
        ("invent_physical", lambda d: d.__setitem__("physical_or_source_selection", True)),
        ("invent_Born", lambda d: d.__setitem__("Born_prediction_or_confirmation_credit", True)),
        ("invent_public", lambda d: d.__setitem__("canon_paper_release_or_public_posture_move", True)),
    )
    results = []
    for name, update in updates:
        broken = copy.deepcopy(data)
        update(broken)
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
