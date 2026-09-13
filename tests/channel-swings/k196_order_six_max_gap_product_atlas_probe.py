#!/usr/bin/env python3
"""Probe and hostile self-test for the K196 max-gap product atlas."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[2]
SOLVER_PATH = ROOT / "tests/channel-swings/k196_order_six_max_gap_product_atlas.py"
MANIFEST_PATH = ROOT / "lab/process/k196-order-six-max-gap-product-atlas-wave.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SOLVER = load_module("k196_probe_solver", SOLVER_PATH)


def checks(result: dict[str, Any]) -> list[tuple[str, bool]]:
    atlas = result["exact_max_gap_atlas"]
    product = result["certified_open_product_blocks"]
    sizes = product["sizes"]
    shell = result["outer_shell_dependency_loss"]
    handoff = result["atlas_chain_rule_handoff"]
    release = result["release_test"]
    return [
        ("classification", result["classification"] == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", result["direction"] == "observed_to_native"),
        ("patterns", result["fixed_control"]["source_patterns"] == 53),
        ("occurrences", result["fixed_control"]["source_nontrivial_occurrences"] == 468),
        ("entries", result["fixed_control"]["source_time_gram_entries"] == 234),
        ("groups", result["fixed_control"]["source_coherent_groups"] == 18),
        ("dilation", result["fixed_control"]["product_dilation"] == 7),
        ("atlas exact", atlas["exact"]),
        ("atlas cover", "every r0,c0>0" in atlas["cover"]),
        ("atlas overlap", atlas["overlap"] == "r0=c0 iff q=1; both charts agree there"),
        ("row Jacobian", atlas["row_dominant"]["oriented_jacobian"] == "t^3*q/1048576"),
        ("column Jacobian", atlas["column_dominant"]["oriented_jacobian"] == "-t^3*q/1048576"),
        ("absolute Jacobians", atlas["positive_absolute_jacobians"]),
        ("transpose", "swapping row and column gaps" in atlas["transpose_symmetry"]),
        ("all cells", product["all_cells_strictly_positive"]),
        ("unique cell count", product["unique_outward_cells"] == 5120),
        ("two-chart instances", product["chart_cell_instances_by_exact_transpose"] == 10240),
        ("size two count", sizes["2"]["unique_outward_cells"] == 1024),
        ("size three count", sizes["3"]["unique_outward_cells"] == 4096),
        ("size two lower", sizes["2"]["minimum_R_lower"] > 0),
        ("size three lower", sizes["3"]["minimum_R_lower"] > 0),
        ("contiguous two", sizes["2"]["scale_and_radial_cells_contiguous"]),
        ("contiguous three", sizes["3"]["scale_and_radial_cells_contiguous"]),
        ("K195 strict extension", product["k195_star_strictly_inside_row_block"]),
        ("mirrored block", product["mirrored_column_block_new"]),
        ("outer dilation", shell["dilation"] == 8),
        ("outer witnesses", len(shell["witnesses"]) == 2 and all(row["strict_positivity_lost"] for row in shell["witnesses"])),
        ("adaptive recovery", all(row["adaptive_bisection"]["subcells"] == 8 and row["adaptive_bisection"]["all_strictly_positive"] and row["adaptive_bisection"]["minimum_R_lower"] > 0 for row in shell["witnesses"])),
        ("controls", result["independent_controls"]["all_contained"]),
        ("control count", len(result["independent_controls"]["rows"]) == 20),
        ("chain coordinates", handoff["coordinate_derivative_matrices_exact"]),
        ("chain overlap", handoff["seam_and_extended_transition_exact"]),
        ("regularizer derivatives withheld", not handoff["regularizer_derivative_envelopes"]),
        ("family patterns", result["complete_family_propagation"]["all_53_patterns_retain_the_same_formula"]),
        ("family occurrences", result["complete_family_propagation"]["all_468_occurrences_retain_the_same_formula"]),
        ("common cell", release["all_entries_use_one_shared_scale_radial_and_three_shape_cell_before_complete_determinant_enclosure"]),
        ("product blocks", release["row_and_column_open_product_blocks_outwardly_certified"]),
        ("coordinate atlas", release["full_max_gap_coordinate_atlas_exact"]),
        ("full determinant atlas withheld", not release["complete_transverse_arbitrary_gap_ratio_domain_covered"]),
        ("Duffy withheld", not release["duffy_jacobi_chain_rule_envelopes_serialized"]),
        ("prefix withheld", not release["accurate_order_six_prefix_released"]),
        ("action withheld", not release["complete_base_action_column_evaluated"]),
        ("physical withheld", result["physical_or_source_selection"] is False),
        ("canon withheld", result["canon_paper_release_or_public_posture_move"] is False),
    ]


def verify(result: dict[str, Any]) -> None:
    failed = [name for name, passed in checks(result) if not passed]
    if failed:
        raise AssertionError("K196 probe failures: " + ", ".join(failed))


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
        mutate(("fixed_control", "product_dilation"), 8),
        mutate(("exact_max_gap_atlas", "exact"), False),
        mutate(("exact_max_gap_atlas", "cover"), "partial"),
        mutate(("exact_max_gap_atlas", "overlap"), "unknown"),
        mutate(("exact_max_gap_atlas", "row_dominant", "oriented_jacobian"), "0"),
        mutate(("exact_max_gap_atlas", "column_dominant", "oriented_jacobian"), "0"),
        mutate(("exact_max_gap_atlas", "positive_absolute_jacobians"), False),
        mutate(("exact_max_gap_atlas", "transpose_symmetry"), "none"),
        mutate(("certified_open_product_blocks", "all_cells_strictly_positive"), False),
        mutate(("certified_open_product_blocks", "unique_outward_cells"), 5119),
        mutate(("certified_open_product_blocks", "chart_cell_instances_by_exact_transpose"), 10239),
        mutate(("certified_open_product_blocks", "sizes", "2", "unique_outward_cells"), 1023),
        mutate(("certified_open_product_blocks", "sizes", "3", "unique_outward_cells"), 4095),
        mutate(("certified_open_product_blocks", "sizes", "2", "minimum_R_lower"), -1.0),
        mutate(("certified_open_product_blocks", "sizes", "3", "minimum_R_lower"), -1.0),
        mutate(("certified_open_product_blocks", "sizes", "2", "scale_and_radial_cells_contiguous"), False),
        mutate(("certified_open_product_blocks", "sizes", "3", "scale_and_radial_cells_contiguous"), False),
        mutate(("certified_open_product_blocks", "k195_star_strictly_inside_row_block"), False),
        mutate(("certified_open_product_blocks", "mirrored_column_block_new"), False),
        mutate(("outer_shell_dependency_loss", "dilation"), 7),
        mutate(("outer_shell_dependency_loss", "witnesses"), []),
        mutate(("outer_shell_dependency_loss", "witnesses", 0, "adaptive_bisection", "all_strictly_positive"), False),
        mutate(("independent_controls", "all_contained"), False),
        mutate(("independent_controls", "rows"), []),
        mutate(("atlas_chain_rule_handoff", "coordinate_derivative_matrices_exact"), False),
        mutate(("atlas_chain_rule_handoff", "seam_and_extended_transition_exact"), False),
        mutate(("atlas_chain_rule_handoff", "regularizer_derivative_envelopes"), True),
        mutate(("complete_family_propagation", "all_53_patterns_retain_the_same_formula"), False),
        mutate(("complete_family_propagation", "all_468_occurrences_retain_the_same_formula"), False),
        mutate(("release_test", "all_entries_use_one_shared_scale_radial_and_three_shape_cell_before_complete_determinant_enclosure"), False),
        mutate(("release_test", "row_and_column_open_product_blocks_outwardly_certified"), False),
        mutate(("release_test", "full_max_gap_coordinate_atlas_exact"), False),
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
        raise AssertionError(f"K196 hostile selftest caught {caught}/{len(mutations)}")
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
        replayed = SOLVER.build()
        verify(replayed)
        if replayed != manifest:
            raise AssertionError("K196 deterministic replay differs from the tracked manifest")
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
