#!/usr/bin/env python3
"""Exact/reporting and hostile controls for the K182 order-four certificate."""

from __future__ import annotations

import argparse
import copy
import json
from decimal import Decimal
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k182-order-four-coherent-gram-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k182-order-four-coherent-gram-wave-2026-09-09.md"
SOLVER = ROOT / "tests/channel-swings/k182_order_four_coherent_gram.py"


def first_key(mapping: dict[str, Any]) -> str:
    key = next(iter(mapping), None)
    if key is None:
        raise ValueError("hostile mutation requires a nonempty mapping")
    return key


def manifest_failures(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    family = data.get("canonical_order_four_family", {})
    gram = family.get("global_gram", {})
    localized = data.get("localized_interval_witnesses", {})
    intervals = data.get("certified_coherent_norm_squared_intervals", {})
    control = data.get("same_family_quadrature_control", {})
    replay = data.get("higher_order_replay", {})
    release = data.get("release_test", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY": failures.append("classification")
    if data.get("fixed_control", {}).get("coefficient_family_sha256") != "ee24469ef5c6bb8d606efe1d529b294cbc7097b14adc51df80a51627aa7eb686": failures.append("K179_pin")
    if data.get("fixed_control", {}).get("resolved_order") != 4: failures.append("resolved_order")
    census = (family.get("terms"), family.get("groups"), family.get("singleton_groups"), family.get("multi_path_groups"), family.get("maximum_group_size"))
    if census != (24, 13, 6, 7, 4): failures.append("family_census")
    rows = family.get("canonical_groups", [])
    if len(rows) != 13 or sum(row.get("path_count", 0) for row in rows) != 24: failures.append("group_rows")
    path_ids = [path.get("contraction_id") for row in rows for path in row.get("paths", [])]
    if len(path_ids) != 24 or len(set(path_ids)) != 24: failures.append("path_identity")
    if any(path.get("coefficient") not in (-1, 1) or path.get("old_position") not in (1, 3) for row in rows for path in row.get("paths", [])): failures.append("path_pin")
    if gram.get("all_thirteen_groups_enclosed") is not True: failures.append("gram_groups")
    if gram.get("unique_self_and_cross_entries_all_groups") != 40: failures.append("all_gram_count")
    if gram.get("unique_self_and_cross_entries_multi_path_groups") != 34: failures.append("multi_gram_count")
    if gram.get("all_bounds_applied_after_complete_specieswise_antisymmetrization") is not True: failures.append("cancellation_order")
    gram_groups = gram.get("groups", {})
    if len(gram_groups) != 13: failures.append("gram_rows")
    for group_id, row in gram_groups.items():
        if row.get("path_count", 0) < 1: failures.append(f"empty:{group_id}")
        lo, hi = row.get("coherent_norm_squared_interval", [None, None])
        if lo != 0.0 or not isinstance(hi, (int, float)) or not hi > 0: failures.append(f"global_interval:{group_id}")
        for entry in row.get("gram_intervals", []):
            if not entry.get("lower") <= entry.get("upper"): failures.append(f"gram_interval:{group_id}")
    if localized.get("groups_with_nonzero_local_witness") != 13: failures.append("localized_count")
    if localized.get("complete_coherent_coordinate_formed_before_interval_sum") is not True: failures.append("localized_order")
    if len(intervals) != 13: failures.append("certified_interval_count")
    for group_id, pair in intervals.items():
        lo, hi = map(Decimal, pair)
        if not Decimal(0) < lo < hi: failures.append(f"certified_interval:{group_id}")
    fine_groups = control.get("fine", {}).get("groups", {})
    coarse_groups = control.get("coarse", {}).get("groups", {})
    if len(fine_groups) != 13 or len(coarse_groups) != 13: failures.append("control_groups")
    for group_id, comparison in control.get("comparisons", {}).items():
        if comparison.get("fine_value_inside_global_outward_interval") is not True: failures.append(f"control_outward:{group_id}")
        if not 0 <= comparison.get("coarse_fine_relative_difference", 1) < 0.06: failures.append(f"control_convergence:{group_id}")
    seeds = control.get("seedwise_order_four_norms_squared", {})
    if set(seeds) != {"0", "1", "2"} or not all(value > 0 for value in seeds.values()): failures.append("seed_norms")
    if abs(seeds.get("1", 0) - seeds.get("2", 1)) > 1e-25: failures.append("seed_symmetry")
    order5 = replay.get("orders", {}).get("5", {})
    if (order5.get("terms"), order5.get("coherent_output_groups"), order5.get("multi_path_groups"), order5.get("unique_self_and_cross_gram_entries"), order5.get("contracted_positions")) != (32, 12, 12, 64, [2, 4]): failures.append("order5_replay")
    order12 = replay.get("orders", {}).get("12", {})
    if (order12.get("terms"), order12.get("unique_self_and_cross_gram_entries"), order12.get("total_exterior_summands_per_point")) != (1152, 35352, 19609920): failures.append("order12_replay")
    required_true = (
        "all_24_order_four_paths_mapped_to_canonical_exterior_coordinates",
        "all_13_output_groups_assembled",
        "all_34_multi_path_self_and_cross_gram_entries_outwardly_enclosed",
        "all_bounds_applied_after_complete_specieswise_antisymmetrization",
        "localized_nonzero_interval_witnesses_emitted",
        "complete_order_four_nonzero_norms_certified",
    )
    required_false = (
        "order_five_through_twelve_coherent_cross_terms_evaluated",
        "coefficient_complete_base_action_column_evaluated",
        "complete_R_ref_form_dual_residual_serialized",
        "positive_complete_M_orthogonal_complement_or_flux_floor_serialized",
        "scalar_center_left_floor_serialized",
        "native_K152_interval_emitted",
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
        ("manifest", not failures),
        ("artifact exists", ARTIFACT.exists()),
        ("solver exists", SOLVER.exists()),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("24 paths", "24 coefficient-complete paths" in text),
        ("13 groups", "13 canonical output groups" in text),
        ("34 Gram", "34 self/cross entries" in text),
        ("cancellation first", "before any interval operation" in text),
        ("all nonzero", "all 13 coherent groups are nonzero" in text),
        ("quadrature role", "not the outward proof" in text),
        ("order five gate", "contracted positions 2 and 4" in text),
        ("action fenced", "K171/K168 action columns" in text),
        ("ledger unchanged", "SC-META-53" in text and "remain unchanged" in text),
    ] + [(f"no {failure}", False) for failure in failures]


def hostile_checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    updates = (
        ("change_K179_pin", lambda d: d["fixed_control"].__setitem__("coefficient_family_sha256", "0" * 64)),
        ("drop_path", lambda d: d["canonical_order_four_family"].__setitem__("terms", 23)),
        ("merge_group", lambda d: d["canonical_order_four_family"].__setitem__("groups", 12)),
        ("erase_singleton", lambda d: d["canonical_order_four_family"].__setitem__("singleton_groups", 5)),
        ("erase_multipath", lambda d: d["canonical_order_four_family"].__setitem__("multi_path_groups", 6)),
        ("wrong_max", lambda d: d["canonical_order_four_family"].__setitem__("maximum_group_size", 5)),
        ("erase_gram", lambda d: d["canonical_order_four_family"]["global_gram"].__setitem__("unique_self_and_cross_entries_multi_path_groups", 33)),
        ("entrywise_before_cancel", lambda d: d["canonical_order_four_family"]["global_gram"].__setitem__("all_bounds_applied_after_complete_specieswise_antisymmetrization", False)),
        ("erase_witness", lambda d: d["localized_interval_witnesses"].__setitem__("groups_with_nonzero_local_witness", 12)),
        ("zero_lower", lambda d: d["certified_coherent_norm_squared_intervals"][first_key(d["certified_coherent_norm_squared_intervals"])].__setitem__(0, "0")),
        ("invert_interval", lambda d: d["certified_coherent_norm_squared_intervals"][first_key(d["certified_coherent_norm_squared_intervals"])].__setitem__(0, "9")),
        ("break_control", lambda d: d["same_family_quadrature_control"]["comparisons"][first_key(d["same_family_quadrature_control"]["comparisons"])].__setitem__("fine_value_inside_global_outward_interval", False)),
        ("break_convergence", lambda d: d["same_family_quadrature_control"]["comparisons"][first_key(d["same_family_quadrature_control"]["comparisons"])].__setitem__("coarse_fine_relative_difference", 1.0)),
        ("break_symmetry", lambda d: d["same_family_quadrature_control"]["seedwise_order_four_norms_squared"].__setitem__("2", 1.0)),
        ("invent_order5", lambda d: d["release_test"].__setitem__("order_five_through_twelve_coherent_cross_terms_evaluated", True)),
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
