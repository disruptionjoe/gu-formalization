#!/usr/bin/env python3
"""Probe and hostile self-test for the K201 third enlarged a/c square."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[2]
SOLVER_PATH = ROOT / "tests/channel-swings/k201_order_six_third_ac_ring.py"
MANIFEST_PATH = ROOT / "lab/process/k201-order-six-third-ac-ring-wave.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SOLVER = load_module("k201_solver_for_probe", SOLVER_PATH)


def checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    fixed = data["fixed_control"]
    square = data["certified_third_enlarged_ac_square"]
    ring = square["size_three_row_chart_third_ring_cover"]
    inherited = data["inherited_size_two"]
    controls = data["independent_controls"]
    family = data["complete_family_propagation"]
    decision = data["decision"]
    release = data["release_test"]
    ledger = data["ledger_effect"]
    packet_ranges = ring["ring_packets"]
    accepted = [child for tile in ring["q_tiles"] for child in tile["accepted_ring_tiles"]]
    packet_ids = {row["packet_id"] for row in accepted}
    expected_packet_ids = {
        "lower_side", "upper_side", "lower_lower", "lower_upper",
        "upper_lower", "upper_upper",
    }
    expected_base_cells = 32 * 6 * 4096
    return [
        ("schema", data["schema_version"] == "1.0"),
        ("classification", data["classification"] == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", data["direction"] == "observed_to_native"),
        ("predecessor", fixed["predecessor_manifest"].endswith("k200-order-six-second-ac-ring-wave.json")),
        ("inner", fixed["k200_inner_a_c_range"] == ["503/1024", "521/1024"]),
        ("outer", fixed["third_expanded_a_c_range"] == ["495/1024", "529/1024"]),
        ("q corridor", fixed["q_corridor"] == ["8227/10240", "1/1"]),
        ("q subdivisions", fixed["q_subdivisions"] == 32),
        ("one thread", fixed["threads"] == 1),
        ("patterns", fixed["source_patterns"] == 53),
        ("occurrences", fixed["source_nontrivial_occurrences"] == 468),
        ("entries", fixed["source_time_gram_entries"] == 234),
        ("groups", fixed["source_coherent_groups"] == 18),
        ("width discriminator", fixed["shell_width_discriminator"]["selected_width_each_side"] == "8/1024" and fixed["shell_width_discriminator"]["selected_width_sample_minimum_R_lower"] > 0),
        ("parent rejected", fixed["shell_width_discriminator"]["first_rejected_parent_width_each_side"] == "16/1024" and fixed["shell_width_discriminator"]["first_rejected_parent_sample_minimum_R_lower"] < 0),
        ("size", ring["size"] == 3),
        ("ring ranges", ring["inner_a_c_range"] == ["503/1024", "521/1024"] and ring["outer_a_c_range"] == ["495/1024", "529/1024"]),
        ("six ranges", set(packet_ranges) == expected_packet_ids),
        ("lower side", packet_ranges["lower_side"]["a"] == ["495/1024", "503/1024"] and packet_ranges["lower_side"]["c"] == ["503/1024", "521/1024"]),
        ("upper side", packet_ranges["upper_side"]["a"] == ["521/1024", "529/1024"] and packet_ranges["upper_side"]["c"] == ["503/1024", "521/1024"]),
        ("lower lower", packet_ranges["lower_lower"]["a"] == ["495/1024", "503/1024"] and packet_ranges["lower_lower"]["c"] == ["495/1024", "503/1024"]),
        ("upper upper", packet_ranges["upper_upper"]["a"] == ["521/1024", "529/1024"] and packet_ranges["upper_upper"]["c"] == ["521/1024", "529/1024"]),
        ("q tiles", ring["accepted_q_tiles"] == 32 and len(ring["q_tiles"]) == 32),
        ("packet identities", packet_ids == expected_packet_ids),
        ("at least base tiles", ring["accepted_ring_tiles"] >= 192),
        ("at least base cells", ring["unique_outward_cells"] >= expected_base_cells),
        ("instances", ring["chart_cell_instances_by_exact_transpose"] == 2 * ring["unique_outward_cells"]),
        ("positive", ring["all_cells_strictly_positive"] and ring["minimum_R_lower"] > 0),
        ("contiguous", ring["q_tiles_contiguous"]),
        ("ring cover", ring["six_packets_exactly_cover_new_ring_with_transpose"]),
        ("outward cover", ring["scale_and_radial_coverage_in_every_ring_tile"]),
        ("transpose", square["size_three_column_chart_side_strips_are_exact_transpose"]),
        ("K200 inherited", square["k200_second_enlarged_square_inherited"]),
        ("six packets", square["two_side_strips_and_four_corners_covered"]),
        ("join", square["exact_join_to_k200_square"]),
        ("square complete", square["third_enlarged_a_c_square_complete"]),
        ("full domain withheld", not square["complete_a_c_domain_covered"]),
        ("count", square["unique_new_outward_cells"] == ring["unique_outward_cells"]),
        ("instance count", square["new_chart_cell_instances_by_exact_transpose"] == ring["chart_cell_instances_by_exact_transpose"]),
        ("common cell", "one shared" in square["common_cell_rule"]),
        ("size two inherited", inherited["shape_independent"] and inherited["not_recomputed"]),
        ("size two positive", inherited["k197_minimum_R_lower"] > 0),
        ("controls count", len(controls["rows"]) == 1056),
        ("controls", controls["all_contained"]),
        ("control transpose", controls["transpose_companions_exact_by_row_column_exchange"]),
        ("family", all(family.values())),
        ("decision sides", decision["two_eight_step_side_strips_certified"]),
        ("decision corners", decision["four_eight_by_eight_corner_boxes_certified"]),
        ("decision join", decision["k200_square_join_preserved"]),
        ("decision square", decision["third_enlarged_a_c_square_certified"]),
        ("decision complement", not decision["farther_a_c_complement_covered"]),
        ("square release", release["third_enlarged_a_c_square_outwardly_certified"]),
        ("atlas", release["full_max_gap_coordinate_atlas_exact"]),
        ("downstream withheld", not any(value for key, value in release.items() if key not in {
            "shifted_hermite_genocchi_entry_tail_retained",
            "all_entries_use_one_shared_scale_radial_and_three_shape_cell_before_complete_determinant_enclosure",
            "third_enlarged_a_c_square_outwardly_certified",
            "full_max_gap_coordinate_atlas_exact",
        })),
        ("ledger", ledger == {"SC-META-53": "UNCERTAIN_UNCHANGED", "LT-SM8": "NEEDS_UNCHANGED", "LT-GR6b": "NEEDS_UNCHANGED", "RA-F1": "NEEDS_UNCHANGED", "AC-F1": "NEEDS_UNCHANGED"}),
        ("selection withheld", not data["physical_or_source_selection"]),
        ("credit withheld", not data["Born_prediction_or_confirmation_credit"]),
        ("posture withheld", not data["canon_paper_release_or_public_posture_move"]),
    ]


def audit(data: dict[str, Any]) -> list[str]:
    return [name for name, ok in checks(data) if not ok]


def mutate(path: tuple[str, ...], value: Any) -> Callable[[dict[str, Any]], None]:
    def apply(data: dict[str, Any]) -> None:
        current = data
        for key in path[:-1]:
            current = current[key]
        current[path[-1]] = value
    return apply


MUTATIONS = [
    mutate(("fixed_control", "third_expanded_a_c_range"), ["503/1024", "521/1024"]),
    mutate(("fixed_control", "shell_width_discriminator", "selected_width_each_side"), "16/1024"),
    mutate(("fixed_control", "shell_width_discriminator", "first_rejected_parent_sample_minimum_R_lower"), 0.01),
    mutate(("fixed_control", "q_subdivisions"), 16),
    mutate(("certified_third_enlarged_ac_square", "size_three_row_chart_third_ring_cover", "accepted_q_tiles"), 31),
    mutate(("certified_third_enlarged_ac_square", "size_three_row_chart_third_ring_cover", "accepted_ring_tiles"), 191),
    mutate(("certified_third_enlarged_ac_square", "size_three_row_chart_third_ring_cover", "unique_outward_cells"), 786431),
    mutate(("certified_third_enlarged_ac_square", "size_three_row_chart_third_ring_cover", "minimum_R_lower"), -1.0),
    mutate(("certified_third_enlarged_ac_square", "size_three_row_chart_third_ring_cover", "q_tiles_contiguous"), False),
    mutate(("certified_third_enlarged_ac_square", "size_three_row_chart_third_ring_cover", "six_packets_exactly_cover_new_ring_with_transpose"), False),
    mutate(("certified_third_enlarged_ac_square", "size_three_column_chart_side_strips_are_exact_transpose"), False),
    mutate(("certified_third_enlarged_ac_square", "k200_second_enlarged_square_inherited"), False),
    mutate(("certified_third_enlarged_ac_square", "two_side_strips_and_four_corners_covered"), False),
    mutate(("certified_third_enlarged_ac_square", "exact_join_to_k200_square"), False),
    mutate(("certified_third_enlarged_ac_square", "third_enlarged_a_c_square_complete"), False),
    mutate(("certified_third_enlarged_ac_square", "complete_a_c_domain_covered"), True),
    mutate(("inherited_size_two", "shape_independent"), False),
    mutate(("independent_controls", "all_contained"), False),
    mutate(("independent_controls", "transpose_companions_exact_by_row_column_exchange"), False),
    mutate(("decision", "two_eight_step_side_strips_certified"), False),
    mutate(("decision", "four_eight_by_eight_corner_boxes_certified"), False),
    mutate(("decision", "third_enlarged_a_c_square_certified"), False),
    mutate(("decision", "farther_a_c_complement_covered"), True),
    mutate(("release_test", "third_enlarged_a_c_square_outwardly_certified"), False),
    mutate(("release_test", "complete_transverse_arbitrary_gap_ratio_domain_covered"), True),
    mutate(("release_test", "duffy_jacobi_chain_rule_envelopes_serialized"), True),
    mutate(("release_test", "accurate_order_six_prefix_released"), True),
    mutate(("ledger_effect", "SC-META-53"), "SATISFIED"),
    mutate(("physical_or_source_selection",), True),
    mutate(("canon_paper_release_or_public_posture_move",), True),
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-replay", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--progress", action="store_true")
    args = parser.parse_args()
    data = json.loads(MANIFEST_PATH.read_text())
    failures = audit(data)
    for name, ok in checks(data):
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if failures:
        return 1
    if not args.no_replay and SOLVER.build(args.progress) != data:
        print("[FAIL] independent source replay mismatch")
        return 1
    if not args.no_replay:
        print("[PASS] independent source replay exact")
    if args.selftest:
        caught = 0
        for index, mutation in enumerate(MUTATIONS, 1):
            planted = copy.deepcopy(data)
            mutation(planted)
            ok = bool(audit(planted))
            print(f"[{'PASS' if ok else 'FAIL'}] planted mutation {index}")
            caught += int(ok)
        print(f"caught {caught}/{len(MUTATIONS)} planted mutations")
        return 0 if caught == len(MUTATIONS) else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
