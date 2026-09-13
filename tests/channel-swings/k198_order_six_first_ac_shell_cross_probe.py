#!/usr/bin/env python3
"""Probe and hostile self-test for the K198 first a/c-shell cross."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[2]
SOLVER_PATH = ROOT / "tests/channel-swings/k198_order_six_first_ac_shell_cross.py"
MANIFEST_PATH = ROOT / "lab/process/k198-order-six-first-ac-shell-cross-wave.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SOLVER = load_module("k198_solver_for_probe", SOLVER_PATH)


def checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    fixed = data["fixed_control"]
    cross = data["certified_first_ac_shell_cross"]
    band = cross["size_three_row_chart_expanded_a_band"]
    inherited = data["inherited_size_two"]
    controls = data["independent_controls"]
    family = data["complete_family_propagation"]
    decision = data["decision"]
    release = data["release_test"]
    ledger = data["ledger_effect"]
    return [
        ("schema", data["schema_version"] == "1.0"),
        ("classification", data["classification"] == "INTERNAL_STRUCTURAL_ONLY"),
        ("predecessor", fixed["predecessor_manifest"].endswith("k197-order-six-max-gap-q-corridor-wave.json")),
        ("core", fixed["k197_core_a_c_range"] == ["505/1024", "519/1024"]),
        ("expanded", fixed["expanded_a_range"] == ["63/128", "65/128"]),
        ("fixed c", fixed["fixed_c_range"] == ["505/1024", "519/1024"]),
        ("q corridor", fixed["q_corridor"] == ["8227/10240", "1/1"]),
        ("q subdivisions", fixed["q_subdivisions"] == 32),
        ("one thread", fixed["threads"] == 1),
        ("patterns", fixed["source_patterns"] == 53),
        ("occurrences", fixed["source_nontrivial_occurrences"] == 468),
        ("entries", fixed["source_time_gram_entries"] == 234),
        ("groups", fixed["source_coherent_groups"] == 18),
        ("size", band["size"] == 3),
        ("band range", band["a_range"] == ["63/128", "65/128"]),
        ("band c", band["c_range"] == ["505/1024", "519/1024"]),
        ("tiles", band["accepted_q_tiles"] == 32 and len(band["q_tiles"]) == 32),
        ("adaptive product tiles", band["accepted_product_tiles"] == 33),
        ("adaptive depth", band["maximum_a_adaptive_depth_used"] == 1),
        ("one rejected parent", len(band["rejected_parent_cells"]) == 1),
        ("unique cells", band["unique_outward_cells"] == 135168),
        ("instances", band["chart_cell_instances_by_exact_transpose"] == 270336),
        ("positive", band["all_cells_strictly_positive"] and band["minimum_R_lower"] > 0),
        ("contiguous", band["q_tiles_contiguous"]),
        ("outward cover", band["scale_and_radial_coverage_in_every_q_tile"]),
        ("transpose", cross["size_three_column_chart_expanded_c_band_is_exact_transpose"]),
        ("core contained", cross["k197_core_contained_in_joined_band"]),
        ("join", cross["exact_join_to_k197_core"]),
        ("cross count", cross["unique_outward_cells"] == 135168 and cross["chart_cell_instances_by_exact_transpose"] == 270336),
        ("corners withheld", not cross["corner_boxes_covered"]),
        ("full domain withheld", not cross["complete_a_c_domain_covered"]),
        ("size two inherited", inherited["shape_independent"] and inherited["not_recomputed"]),
        ("size two positive", inherited["k197_minimum_R_lower"] > 0),
        ("controls count", len(controls["rows"]) == 264),
        ("controls", controls["all_contained"]),
        ("control transpose", controls["transpose_companions_exact_by_row_column_exchange"]),
        ("family", all(family.values())),
        ("decision", decision["first_symmetric_a_c_shell_cross_certified"] and decision["k197_core_join_preserved"]),
        ("decision corners", not decision["corner_boxes_covered"]),
        ("decision complement", not decision["farther_a_c_complement_covered"]),
        ("common cell", release["all_entries_use_one_shared_scale_radial_and_three_shape_cell_before_complete_determinant_enclosure"]),
        ("shell release", release["first_symmetric_a_c_shell_cross_outwardly_certified"]),
        ("atlas", release["full_max_gap_coordinate_atlas_exact"]),
        ("downstream withheld", not any(value for key, value in release.items() if key not in {
            "shifted_hermite_genocchi_entry_tail_retained",
            "all_entries_use_one_shared_scale_radial_and_three_shape_cell_before_complete_determinant_enclosure",
            "first_symmetric_a_c_shell_cross_outwardly_certified",
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
    mutate(("fixed_control", "expanded_a_range"), ["505/1024", "519/1024"]),
    mutate(("fixed_control", "q_subdivisions"), 16),
    mutate(("certified_first_ac_shell_cross", "size_three_row_chart_expanded_a_band", "accepted_q_tiles"), 31),
    mutate(("certified_first_ac_shell_cross", "size_three_row_chart_expanded_a_band", "accepted_product_tiles"), 32),
    mutate(("certified_first_ac_shell_cross", "size_three_row_chart_expanded_a_band", "maximum_a_adaptive_depth_used"), 0),
    mutate(("certified_first_ac_shell_cross", "size_three_row_chart_expanded_a_band", "unique_outward_cells"), 135167),
    mutate(("certified_first_ac_shell_cross", "size_three_row_chart_expanded_a_band", "minimum_R_lower"), -1.0),
    mutate(("certified_first_ac_shell_cross", "size_three_row_chart_expanded_a_band", "q_tiles_contiguous"), False),
    mutate(("certified_first_ac_shell_cross", "size_three_column_chart_expanded_c_band_is_exact_transpose"), False),
    mutate(("certified_first_ac_shell_cross", "k197_core_contained_in_joined_band"), False),
    mutate(("certified_first_ac_shell_cross", "corner_boxes_covered"), True),
    mutate(("certified_first_ac_shell_cross", "complete_a_c_domain_covered"), True),
    mutate(("inherited_size_two", "shape_independent"), False),
    mutate(("independent_controls", "all_contained"), False),
    mutate(("independent_controls", "transpose_companions_exact_by_row_column_exchange"), False),
    mutate(("decision", "first_symmetric_a_c_shell_cross_certified"), False),
    mutate(("decision", "corner_boxes_covered"), True),
    mutate(("release_test", "first_symmetric_a_c_shell_cross_outwardly_certified"), False),
    mutate(("release_test", "complete_transverse_arbitrary_gap_ratio_domain_covered"), True),
    mutate(("release_test", "duffy_jacobi_chain_rule_envelopes_serialized"), True),
    mutate(("release_test", "accurate_order_six_prefix_released"), True),
    mutate(("ledger_effect", "SC-META-53"), "SATISFIED"),
    mutate(("physical_or_source_selection",), True),
    mutate(("Born_prediction_or_confirmation_credit",), True),
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
