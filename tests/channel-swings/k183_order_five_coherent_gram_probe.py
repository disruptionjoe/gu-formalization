#!/usr/bin/env python3
"""Exact/reporting and hostile controls for the K183 order-five certificate."""

from __future__ import annotations

import argparse
import copy
import json
from decimal import Decimal
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k183-order-five-coherent-gram-compression-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k183-order-five-coherent-gram-compression-wave-2026-09-09.md"
SOLVER = ROOT / "tests/channel-swings/k183_order_five_coherent_gram.py"


def first_key(mapping: dict[str, Any]) -> str:
    key = next(iter(mapping), None)
    if key is None:
        raise ValueError("hostile mutation requires a nonempty mapping")
    return key


def first_value(mapping: dict[str, Any]) -> Any:
    return mapping[first_key(mapping)]


def manifest_failures(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    family = data.get("canonical_order_five_family", {})
    gram = family.get("global_gram", {})
    analytic = family.get("contracted_formula_control", {})
    compression = family.get("compression", {})
    localized = data.get("localized_interval_witnesses", {})
    intervals = data.get("certified_coherent_norm_squared_intervals", {})
    control = data.get("same_family_numerical_control", {})
    release = data.get("release_test", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY": failures.append("classification")
    if data.get("fixed_control", {}).get("coefficient_family_sha256") != "ee24469ef5c6bb8d606efe1d529b294cbc7097b14adc51df80a51627aa7eb686": failures.append("K179_pin")
    if data.get("fixed_control", {}).get("resolved_order") != 5: failures.append("resolved_order")
    census = (
        family.get("terms"), family.get("groups"), family.get("singleton_groups"),
        family.get("multi_path_groups"), family.get("maximum_group_size"),
    )
    if census != (32, 12, 0, 12, 4): failures.append("family_census")
    rows = family.get("canonical_groups", [])
    path_ids = [path.get("contraction_id") for row in rows for path in row.get("paths", [])]
    if len(rows) != 12 or len(path_ids) != 32 or len(set(path_ids)) != 32: failures.append("path_identity")
    if any(path.get("coefficient") not in (-1, 1) or path.get("old_position") not in (2, 4) for row in rows for path in row.get("paths", [])): failures.append("path_pin")
    if gram.get("all_twelve_groups_enclosed") is not True or gram.get("all_groups_multi_path") is not True: failures.append("gram_groups")
    if gram.get("unique_self_and_cross_entries_all_groups") != 64: failures.append("gram_count")
    if gram.get("all_bounds_applied_after_complete_specieswise_antisymmetrization") is not True: failures.append("cancellation_order")
    for group_id, row in gram.get("groups", {}).items():
        lo, hi = row.get("coherent_norm_squared_interval", [None, None])
        if lo != 0.0 or not isinstance(hi, (int, float)) or not hi > 0: failures.append(f"global_interval:{group_id}")
        for bound in row.get("path_bounds", {}).values():
            exponents = {int(key): float(value) for key, value in bound.get("energy_exponents", {}).items()}
            old = int(bound.get("old_position", -1))
            if exponents.get(old, 0) <= 1 or any(2 * value <= 1 for key, value in exponents.items() if key != old): failures.append(f"integrability:{group_id}")
    if analytic.get("maximum_relative_difference", 1) >= 1e-9 or len(analytic.get("rows", [])) != 2: failures.append("contracted_formula")
    if localized.get("groups_with_nonzero_local_witness") != 12: failures.append("localized_count")
    if localized.get("complete_coherent_coordinate_formed_before_interval_sum") is not True: failures.append("localized_order")
    if len(intervals) != 12: failures.append("interval_count")
    for group_id, pair in intervals.items():
        lo, hi = map(Decimal, pair)
        if not Decimal(0) < lo < hi: failures.append(f"certified_interval:{group_id}")
    comparisons = control.get("comparisons", {})
    if len(comparisons) != 12: failures.append("control_groups")
    for group_id, row in comparisons.items():
        if row.get("fine_value_inside_global_outward_interval") is not True: failures.append(f"control_outward:{group_id}")
        if not 0 <= row.get("coarse_fine_relative_difference", 1) < 0.03: failures.append(f"control_convergence:{group_id}")
    seeds = control.get("seedwise_order_five_norms_squared", {})
    if set(seeds) != {"0", "1", "2"} or not all(value > 0 for value in seeds.values()): failures.append("seed_norms")
    if abs(seeds.get("1", 0) - seeds.get("2", 1)) / max(seeds.get("1", 0), seeds.get("2", 0), 1e-300) >= 0.01: failures.append("seed_symmetry")
    if compression.get("order_five_identity_tests") != 96 or compression.get("all_order_five_paths_and_three_controls_agree") is not True: failures.append("compression_identity")
    if compression.get("maximum_absolute_identity_error", 1) >= 1e-12: failures.append("compression_error")
    if compression.get("first_dense_proxy_advantage_order") != 8: failures.append("compression_crossover")
    order12 = compression.get("replay", {}).get("12", {})
    if (order12.get("paths"), order12.get("literal_exterior_summands_per_time_point"), order12.get("dense_determinant_cubic_proxy_per_time_point")) != (1152, 19609920, 186624): failures.append("order12_replay")
    required_true = (
        "all_32_order_five_paths_mapped_to_canonical_exterior_coordinates",
        "all_12_output_groups_assembled", "all_64_self_and_cross_gram_entries_outwardly_enclosed",
        "all_bounds_applied_after_complete_specieswise_antisymmetrization",
        "complete_order_five_nonzero_norms_certified",
        "determinant_dag_representation_selected_and_identity_checked",
    )
    required_false = (
        "order_six_through_twelve_coherent_cross_terms_evaluated",
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
        ("32 paths", "32 coefficient-complete paths" in text),
        ("12 groups", "12 coherent output groups" in text),
        ("64 Gram", "64 unique self/cross Gram entries" in text),
        ("cancellation first", "before any interval operation" in text),
        ("all nonzero", "all 12 coherent groups are nonzero" in text),
        ("numerical role", "not the outward proof" in text),
        ("compression", "Laplace-simplex species determinants" in text),
        ("action fenced", "K171/K168 action columns" in text),
        ("ledger unchanged", "SC-META-53" in text and "remain unchanged" in text),
    ] + [(f"no {failure}", False) for failure in failures]


def hostile_checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    updates = (
        ("change_pin", lambda d: d["fixed_control"].__setitem__("coefficient_family_sha256", "0" * 64)),
        ("drop_path", lambda d: d["canonical_order_five_family"].__setitem__("terms", 31)),
        ("merge_group", lambda d: d["canonical_order_five_family"].__setitem__("groups", 11)),
        ("invent_singleton", lambda d: d["canonical_order_five_family"].__setitem__("singleton_groups", 1)),
        ("wrong_max", lambda d: d["canonical_order_five_family"].__setitem__("maximum_group_size", 5)),
        ("erase_gram", lambda d: d["canonical_order_five_family"]["global_gram"].__setitem__("unique_self_and_cross_entries_all_groups", 63)),
        ("pre_cancel", lambda d: d["canonical_order_five_family"]["global_gram"].__setitem__("all_bounds_applied_after_complete_specieswise_antisymmetrization", False)),
        ("break_integrability", lambda d: first_value(first_value(d["canonical_order_five_family"]["global_gram"]["groups"])["path_bounds"])["energy_exponents"].__setitem__("2", 0.4)),
        ("break_formula", lambda d: d["canonical_order_five_family"]["contracted_formula_control"].__setitem__("maximum_relative_difference", 1.0)),
        ("erase_witness", lambda d: d["localized_interval_witnesses"].__setitem__("groups_with_nonzero_local_witness", 11)),
        ("zero_lower", lambda d: d["certified_coherent_norm_squared_intervals"][first_key(d["certified_coherent_norm_squared_intervals"])].__setitem__(0, "0")),
        ("break_control", lambda d: d["same_family_numerical_control"]["comparisons"][first_key(d["same_family_numerical_control"]["comparisons"])].__setitem__("coarse_fine_relative_difference", 1.0)),
        ("break_symmetry", lambda d: d["same_family_numerical_control"]["seedwise_order_five_norms_squared"].__setitem__("2", 1.0)),
        ("erase_identity", lambda d: d["canonical_order_five_family"]["compression"].__setitem__("all_order_five_paths_and_three_controls_agree", False)),
        ("break_crossover", lambda d: d["canonical_order_five_family"]["compression"].__setitem__("first_dense_proxy_advantage_order", 7)),
        ("break_order12", lambda d: d["canonical_order_five_family"]["compression"]["replay"]["12"].__setitem__("literal_exterior_summands_per_time_point", 1)),
        ("invent_order6", lambda d: d["release_test"].__setitem__("order_six_through_twelve_coherent_cross_terms_evaluated", True)),
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
