#!/usr/bin/env python3
"""Exact/reporting and hostile controls for the K181 order-three certificate."""

from __future__ import annotations

import argparse
import copy
import json
from decimal import Decimal
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k181-order-three-determinant-exchange-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k181-order-three-determinant-exchange-wave-2026-09-09.md"
K179 = ROOT / "tests/channel-swings/k179_matched_normal_order_coefficient_family.py"


def manifest_failures(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    family = data.get("order_three_family", {})
    outward = data.get("outward_evaluation", {})
    control = data.get("same_family_quadrature_control", {})
    seeds = data.get("seedwise_exchange_vectors", {})
    replay = data.get("scale_replay", {})
    release = data.get("release_test", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY": failures.append("classification")
    if data.get("fixed_control", {}).get("coefficient_family_sha256") != "ee24469ef5c6bb8d606efe1d529b294cbc7097b14adc51df80a51627aa7eb686": failures.append("K179_pin")
    if data.get("fixed_control", {}).get("resolved_order") != 3: failures.append("resolved_order")
    if family.get("terms") != 8 or family.get("rank_one_terms") != 4 or family.get("repeated_species_terms") != 4: failures.append("family_census")
    if family.get("distinct_seed_output_groups") != 8: failures.append("order_three_grouping")
    if family.get("all_repeated_pairs_use_p1_p3") is not True: failures.append("repeated_pair_provenance")
    rows = family.get("rows", [])
    if len(rows) != 8 or len({row.get("contraction_id") for row in rows}) != 8: failures.append("row_identity")
    if len({(row.get("seed_impurity"), row.get("output_signature")) for row in rows}) != 8: failures.append("row_orthogonality")
    if any(row.get("coefficient") not in {"-1", "1"} for row in rows): failures.append("coefficient")
    if outward.get("whole_difference_enclosed_before_squaring") is not True: failures.append("whole_difference")
    if outward.get("coincident_face_zero_preserved") is not True: failures.append("coincident_face")
    for prefix in ("rank", "determinant"):
        lower = Decimal(outward.get(f"{prefix}_norm_squared_lower", "NaN"))
        upper = Decimal(outward.get(f"{prefix}_norm_squared_upper", "NaN"))
        if not Decimal(0) < lower < upper: failures.append(f"{prefix}_interval")
    if control.get("rank_fine_inside_outward_enclosure") is not True: failures.append("rank_control")
    if control.get("determinant_fine_inside_outward_enclosure") is not True: failures.append("determinant_control")
    if not 0 <= control.get("rank_coarse_fine_relative_difference", 1) < 1e-3: failures.append("rank_convergence")
    if not 0 <= control.get("determinant_coarse_fine_relative_difference", 1) < 1e-3: failures.append("determinant_convergence")
    if seeds.get("seed_0_kernel_counts") != {"determinant": 2, "rank_one": 2}: failures.append("seed0_counts")
    if seeds.get("seed_1_kernel_counts") != {"determinant": 1, "rank_one": 1}: failures.append("seed1_counts")
    if seeds.get("seed_2_kernel_counts") != {"determinant": 1, "rank_one": 1}: failures.append("seed2_counts")
    if seeds.get("all_eight_output_groups_orthogonal") is not True: failures.append("seed_orthogonality")
    if seeds.get("signed_coefficients_preserved_in_action_coordinates") is not True: failures.append("signs")
    rank_low = Decimal(outward.get("rank_norm_squared_lower", "NaN"))
    rank_high = Decimal(outward.get("rank_norm_squared_upper", "NaN"))
    det_low = Decimal(outward.get("determinant_norm_squared_lower", "NaN"))
    det_high = Decimal(outward.get("determinant_norm_squared_upper", "NaN"))
    if Decimal(seeds.get("seed_0_norm_squared_lower", "NaN")) != 2 * (rank_low + det_low): failures.append("seed0_lower")
    if Decimal(seeds.get("seed_0_norm_squared_upper", "NaN")) != 2 * (rank_high + det_high): failures.append("seed0_upper")
    if Decimal(seeds.get("seed_1_and_2_norm_squared_lower", "NaN")) != rank_low + det_low: failures.append("seed12_lower")
    if Decimal(seeds.get("seed_1_and_2_norm_squared_upper", "NaN")) != rank_high + det_high: failures.append("seed12_upper")
    if replay.get("order_four_terms") != 24 or replay.get("order_four_coherent_output_groups") != 13: failures.append("order_four_census")
    if replay.get("order_four_multi_path_groups") != 7 or replay.get("order_four_maximum_group_size") != 4: failures.append("order_four_collisions")
    if replay.get("rank_one_plus_single_determinant_engine_scales_through_order_twelve") is not False: failures.append("scale_fence")
    required_true = ("complete_order_three_family_evaluated", "four_rank_one_controls_evaluated", "four_whole_2x2_determinants_evaluated", "same_family_independent_control_passed")
    required_false = ("order_four_through_twelve_coherent_cross_terms_evaluated", "coefficient_complete_base_action_column_evaluated", "complete_R_ref_form_dual_residual_serialized", "positive_complete_M_orthogonal_complement_or_flux_floor_serialized", "scalar_center_left_floor_serialized", "native_K152_interval_emitted")
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
        ("K179 exists", K179.exists()),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("whole determinant formula", "(f(p_1,p_3,p_4)-f(p_3,p_1,p_4))/sqrt(2)" in text),
        ("coincident face", "coincident face" in text),
        ("rank interval", "1.712815441542719e-11" in text),
        ("determinant interval", "1.515601509941604e-17" in text),
        ("quadrature rank", "2.785886906990316e-11" in text),
        ("quadrature determinant", "1.060231347943765e-11" in text),
        ("order four groups", "seven multi-path groups" in text),
        ("action fenced", "K171/K168 action columns" in text),
        ("ledger unchanged", "SC-META-53" in text and "remain unchanged" in text),
    ] + [(f"no {failure}", False) for failure in failures]


def hostile_checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    mutations = []
    updates = (
        ("change_K179_pin", lambda d: d["fixed_control"].__setitem__("coefficient_family_sha256", "0" * 64)),
        ("drop_term", lambda d: d["order_three_family"].__setitem__("terms", 7)),
        ("erase_rank_control", lambda d: d["order_three_family"].__setitem__("rank_one_terms", 3)),
        ("erase_determinant", lambda d: d["order_three_family"].__setitem__("repeated_species_terms", 3)),
        ("merge_output", lambda d: d["order_three_family"].__setitem__("distinct_seed_output_groups", 7)),
        ("wrong_pair", lambda d: d["order_three_family"].__setitem__("all_repeated_pairs_use_p1_p3", False)),
        ("entrywise_interval", lambda d: d["outward_evaluation"].__setitem__("whole_difference_enclosed_before_squaring", False)),
        ("lose_face_zero", lambda d: d["outward_evaluation"].__setitem__("coincident_face_zero_preserved", False)),
        ("invert_rank", lambda d: d["outward_evaluation"].__setitem__("rank_norm_squared_lower", "9")),
        ("invert_determinant", lambda d: d["outward_evaluation"].__setitem__("determinant_norm_squared_lower", "9")),
        ("break_rank_control", lambda d: d["same_family_quadrature_control"].__setitem__("rank_fine_inside_outward_enclosure", False)),
        ("break_det_control", lambda d: d["same_family_quadrature_control"].__setitem__("determinant_fine_inside_outward_enclosure", False)),
        ("break_seed", lambda d: d["seedwise_exchange_vectors"].__setitem__("seed_0_kernel_counts", {"rank_one": 4, "determinant": 0})),
        ("erase_signs", lambda d: d["seedwise_exchange_vectors"].__setitem__("signed_coefficients_preserved_in_action_coordinates", False)),
        ("erase_order4_collision", lambda d: d["scale_replay"].__setitem__("order_four_multi_path_groups", 0)),
        ("invent_scale", lambda d: d["scale_replay"].__setitem__("rank_one_plus_single_determinant_engine_scales_through_order_twelve", True)),
        ("invent_action", lambda d: d["release_test"].__setitem__("coefficient_complete_base_action_column_evaluated", True)),
        ("invent_residual", lambda d: d["release_test"].__setitem__("complete_R_ref_form_dual_residual_serialized", True)),
        ("invent_K152", lambda d: d["release_test"].__setitem__("native_K152_interval_emitted", True)),
        ("move_ledger", lambda d: d["ledger_effect"].__setitem__("SC-META-53", "RESOLVED")),
        ("invent_physical", lambda d: d.__setitem__("physical_or_source_selection", True)),
        ("invent_Born", lambda d: d.__setitem__("Born_prediction_or_confirmation_credit", True)),
        ("invent_public", lambda d: d.__setitem__("canon_paper_release_or_public_posture_move", True)),
    )
    for name, update in updates:
        broken = copy.deepcopy(data)
        update(broken)
        mutations.append((name, bool(manifest_failures(broken))))
    return mutations


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
