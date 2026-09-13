#!/usr/bin/env python3
"""Probe and hostile self-test for the K197 max-gap q corridor."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[2]
SOLVER_PATH = ROOT / "tests/channel-swings/k197_order_six_max_gap_q_corridor.py"
MANIFEST_PATH = ROOT / "lab/process/k197-order-six-max-gap-q-corridor-wave.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SOLVER = load_module("k197_probe_solver", SOLVER_PATH)


def checks(result: dict[str, Any]) -> list[tuple[str, bool]]:
    fixed = result["fixed_control"]
    corridor = result["certified_q_to_one_corridor"]
    sizes = corridor["sizes"]
    family = result["complete_family_propagation"]
    decision = result["decision"]
    release = result["release_test"]
    expected_unique = sizes["2"]["unique_outward_cells"] + sizes["3"]["unique_outward_cells"]
    return [
        ("classification", result["classification"] == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", result["direction"] == "observed_to_native"),
        ("patterns", fixed["source_patterns"] == 53),
        ("occurrences", fixed["source_nontrivial_occurrences"] == 468),
        ("entries", fixed["source_time_gram_entries"] == 234),
        ("groups", fixed["source_coherent_groups"] == 18),
        ("q start", fixed["q_corridor"][0] == "8227/10240"),
        ("q seam", fixed["q_corridor"][1] == "1/1"),
        ("size two base tiling", sizes["2"]["base_q_subdivisions"] == 1),
        ("size three base tiling", sizes["3"]["base_q_subdivisions"] == 32),
        ("size two tiles", sizes["2"]["accepted_q_tiles"] >= 1),
        ("size three tiles", sizes["3"]["accepted_q_tiles"] >= 32),
        ("adaptive depth bound two", sizes["2"]["maximum_adaptive_depth_used"] <= fixed["maximum_adaptive_depth"]),
        ("adaptive depth bound three", sizes["3"]["maximum_adaptive_depth_used"] <= fixed["maximum_adaptive_depth"]),
        ("size two positive", sizes["2"]["all_cells_strictly_positive"] and sizes["2"]["minimum_R_lower"] > 0),
        ("size three positive", sizes["3"]["all_cells_strictly_positive"] and sizes["3"]["minimum_R_lower"] > 0),
        ("size two contiguous", sizes["2"]["q_tiles_contiguous"]),
        ("size three contiguous", sizes["3"]["q_tiles_contiguous"]),
        ("full scale radial two", sizes["2"]["scale_and_radial_coverage_in_every_q_tile"]),
        ("full scale radial three", sizes["3"]["scale_and_radial_coverage_in_every_q_tile"]),
        ("unique accounting", corridor["unique_outward_cells"] == expected_unique),
        ("transpose accounting", corridor["chart_cell_instances_by_exact_transpose"] == 2 * expected_unique),
        ("all cells", corridor["all_cells_strictly_positive"]),
        ("common cell", "one shared" in corridor["common_cell_rule"]),
        ("K196 join", corridor["k196_join"].startswith("q=8227/10240")),
        ("q one seam", corridor["chart_seam"].startswith("q=1")),
        ("transpose", corridor["row_and_column_instances_related_by_exact_transpose"]),
        ("fixed ac complete", corridor["complete_for_fixed_a_c_block"]),
        ("controls", result["independent_controls"]["all_contained"]),
        ("controls nonempty", len(result["independent_controls"]["rows"]) > 0),
        ("family patterns", family["all_53_patterns_retain_the_same_formula"]),
        ("family occurrences", family["all_468_occurrences_retain_the_same_formula"]),
        ("family entries", family["all_234_entries_and_18_groups_remain_in_scope"]),
        ("corridor decision", decision["complete_q_to_one_corridor_for_fixed_a_c_block"]),
        ("connected", decision["k196_local_block_connected_to_q_one_seam"]),
        ("ac complement withheld", not decision["remaining_a_c_complement_covered"]),
        ("release corridor", release["q_to_one_corridor_outwardly_certified"]),
        ("release common cell", release["all_entries_use_one_shared_scale_radial_and_three_shape_cell_before_complete_determinant_enclosure"]),
        ("full shape withheld", not release["complete_transverse_arbitrary_gap_ratio_domain_covered"]),
        ("Duffy withheld", not release["duffy_jacobi_chain_rule_envelopes_serialized"]),
        ("prefix withheld", not release["accurate_order_six_prefix_released"]),
        ("action withheld", not release["complete_base_action_column_evaluated"]),
        ("physical withheld", result["physical_or_source_selection"] is False),
        ("canon withheld", result["canon_paper_release_or_public_posture_move"] is False),
    ]


def verify(result: dict[str, Any]) -> None:
    failed = [name for name, passed in checks(result) if not passed]
    if failed:
        raise AssertionError("K197 probe failures: " + ", ".join(failed))


def mutate(path: tuple[Any, ...], value: Any) -> Callable[[dict[str, Any]], None]:
    def apply(result: dict[str, Any]) -> None:
        cursor: Any = result
        for key in path[:-1]:
            cursor = cursor[key]
        cursor[path[-1]] = value
    return apply


def selftest(baseline: dict[str, Any]) -> int:
    mutations = [
        mutate(("classification",), "SOURCE_NATIVE_ROUTE"),
        mutate(("direction",), "native_to_observed"),
        mutate(("fixed_control", "source_patterns"), 52),
        mutate(("fixed_control", "source_nontrivial_occurrences"), 467),
        mutate(("fixed_control", "source_time_gram_entries"), 233),
        mutate(("fixed_control", "source_coherent_groups"), 17),
        mutate(("fixed_control", "q_corridor"), ["0/1", "1/1"]),
        mutate(("certified_q_to_one_corridor", "sizes", "2", "base_q_subdivisions"), 0),
        mutate(("certified_q_to_one_corridor", "sizes", "3", "base_q_subdivisions"), 16),
        mutate(("certified_q_to_one_corridor", "sizes", "2", "accepted_q_tiles"), 0),
        mutate(("certified_q_to_one_corridor", "sizes", "3", "accepted_q_tiles"), 31),
        mutate(("certified_q_to_one_corridor", "sizes", "2", "maximum_adaptive_depth_used"), 4),
        mutate(("certified_q_to_one_corridor", "sizes", "3", "maximum_adaptive_depth_used"), 4),
        mutate(("certified_q_to_one_corridor", "sizes", "2", "minimum_R_lower"), -1.0),
        mutate(("certified_q_to_one_corridor", "sizes", "3", "minimum_R_lower"), -1.0),
        mutate(("certified_q_to_one_corridor", "sizes", "2", "q_tiles_contiguous"), False),
        mutate(("certified_q_to_one_corridor", "sizes", "3", "q_tiles_contiguous"), False),
        mutate(("certified_q_to_one_corridor", "sizes", "2", "scale_and_radial_coverage_in_every_q_tile"), False),
        mutate(("certified_q_to_one_corridor", "sizes", "3", "scale_and_radial_coverage_in_every_q_tile"), False),
        mutate(("certified_q_to_one_corridor", "unique_outward_cells"), 0),
        mutate(("certified_q_to_one_corridor", "chart_cell_instances_by_exact_transpose"), 0),
        mutate(("certified_q_to_one_corridor", "all_cells_strictly_positive"), False),
        mutate(("certified_q_to_one_corridor", "common_cell_rule"), "independent entries"),
        mutate(("certified_q_to_one_corridor", "k196_join"), "missing"),
        mutate(("certified_q_to_one_corridor", "chart_seam"), "missing"),
        mutate(("certified_q_to_one_corridor", "row_and_column_instances_related_by_exact_transpose"), False),
        mutate(("certified_q_to_one_corridor", "complete_for_fixed_a_c_block"), False),
        mutate(("independent_controls", "all_contained"), False),
        mutate(("independent_controls", "rows"), []),
        mutate(("complete_family_propagation", "all_53_patterns_retain_the_same_formula"), False),
        mutate(("complete_family_propagation", "all_468_occurrences_retain_the_same_formula"), False),
        mutate(("complete_family_propagation", "all_234_entries_and_18_groups_remain_in_scope"), False),
        mutate(("decision", "complete_q_to_one_corridor_for_fixed_a_c_block"), False),
        mutate(("decision", "k196_local_block_connected_to_q_one_seam"), False),
        mutate(("decision", "remaining_a_c_complement_covered"), True),
        mutate(("release_test", "q_to_one_corridor_outwardly_certified"), False),
        mutate(("release_test", "all_entries_use_one_shared_scale_radial_and_three_shape_cell_before_complete_determinant_enclosure"), False),
        mutate(("release_test", "complete_transverse_arbitrary_gap_ratio_domain_covered"), True),
        mutate(("release_test", "duffy_jacobi_chain_rule_envelopes_serialized"), True),
        mutate(("release_test", "accurate_order_six_prefix_released"), True),
        mutate(("release_test", "complete_base_action_column_evaluated"), True),
        mutate(("physical_or_source_selection",), True),
        mutate(("canon_paper_release_or_public_posture_move",), True),
    ]
    caught = 0
    for apply in mutations:
        candidate = copy.deepcopy(baseline)
        apply(candidate)
        try:
            verify(candidate)
        except AssertionError:
            caught += 1
    if caught != len(mutations):
        raise AssertionError(f"K197 hostile selftest caught {caught}/{len(mutations)}")
    return caught


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-replay", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    manifest = json.loads(MANIFEST_PATH.read_text())
    verify(manifest)
    replayed = None
    if not args.no_replay:
        replayed = SOLVER.build(progress=True)
        verify(replayed)
        if replayed != manifest:
            raise AssertionError("K197 deterministic replay differs from the tracked manifest")
    caught = selftest(manifest) if args.selftest else 0
    print(
        json.dumps(
            {
                "checks_passed": len(checks(manifest)),
                "deterministic_replay": replayed is not None,
                "hostile_selftest_caught": caught,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
