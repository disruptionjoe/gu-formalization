#!/usr/bin/env python3
"""Probe and hostile self-test for the K195 transverse coordinate star."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[2]
SOLVER_PATH = ROOT / "tests/channel-swings/k195_order_six_transverse_projective_chart.py"
MANIFEST_PATH = ROOT / "lab/process/k195-order-six-transverse-projective-chart-wave.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SOLVER = load_module("k195_probe_solver", SOLVER_PATH)


def checks(result: dict[str, Any]) -> list[tuple[str, bool]]:
    coordinates = result["compact_projective_coordinates"]
    star = result["transverse_coordinate_star"]
    sizes = star["sizes"]
    joins = star["joins"]
    release = result["release_test"]
    return [
        ("classification", result["classification"] == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", result["direction"] == "observed_to_native"),
        ("patterns", result["fixed_control"]["source_patterns"] == 53),
        ("occurrences", result["fixed_control"]["source_nontrivial_occurrences"] == 468),
        ("entries", result["fixed_control"]["source_time_gram_entries"] == 234),
        ("groups", result["fixed_control"]["source_coherent_groups"] == 18),
        ("jacobian", coordinates["jacobian_exact"]),
        ("jacobian value", coordinates["jacobian_determinant"] == "s^3*b/1048576"),
        ("jacobian positive", coordinates["positive_on_chart_interior"]),
        ("ray", coordinates["k194_ray"]["a"] == "1/2" and coordinates["k194_ray"]["b"] == "4/5" and coordinates["k194_ray"]["c"] == "1/2"),
        ("all cells", star["all_cells_strictly_positive"]),
        ("cell count", star["total_outward_cells"] == 13312),
        ("size two count", sizes["2"]["total_outward_cells"] == 1024),
        ("size three count", sizes["3"]["total_outward_cells"] == 12288),
        ("size two lower", sizes["2"]["minimum_R_lower"] > 0),
        ("size three lower", sizes["3"]["minimum_R_lower"] > 0),
        ("three sweeps", sorted(sizes["3"]["sweeps"]) == ["a", "b", "c"]),
        ("contiguous", joins["all_chart_axes_contiguous"]),
        ("K194 join", joins["k194_ray_is_exact_chart_section"]),
        ("ray interior", joins["k194_shape_point_inside_every_shape_axis"]),
        ("K193 join", joins["k193_face_center_exact"]),
        ("K192 join", joins["k192_join_inherited_through_k193"]),
        ("controls", result["independent_controls"]["all_contained"]),
        ("control count", len(result["independent_controls"]["rows"]) == 24),
        ("family patterns", result["complete_family_propagation"]["all_53_patterns_retain_the_same_formula"]),
        ("family occurrences", result["complete_family_propagation"]["all_468_occurrences_retain_the_same_formula"]),
        ("common cell", release["all_entries_use_one_shared_scale_and_shape_cell_before_complete_determinant_enclosure"]),
        ("chart", release["size_two_and_size_three_transverse_chart_outwardly_certified"]),
        ("full atlas withheld", not release["complete_transverse_arbitrary_gap_ratio_domain_covered"]),
        ("duffy withheld", not release["duffy_jacobi_chain_rule_envelopes_serialized"]),
        ("prefix withheld", not release["accurate_order_six_prefix_released"]),
        ("action withheld", not release["complete_base_action_column_evaluated"]),
        ("physical withheld", result["physical_or_source_selection"] is False),
        ("canon withheld", result["canon_paper_release_or_public_posture_move"] is False),
    ]


def verify(result: dict[str, Any]) -> None:
    failed = [name for name, passed in checks(result) if not passed]
    if failed:
        raise AssertionError("K195 probe failures: " + ", ".join(failed))


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
        mutate(("compact_projective_coordinates", "jacobian_exact"), False),
        mutate(("compact_projective_coordinates", "jacobian_determinant"), "0"),
        mutate(("compact_projective_coordinates", "positive_on_chart_interior"), False),
        mutate(("compact_projective_coordinates", "k194_ray", "a"), "2/3"),
        mutate(("transverse_coordinate_star", "all_cells_strictly_positive"), False),
        mutate(("transverse_coordinate_star", "total_outward_cells"), 13311),
        mutate(("transverse_coordinate_star", "sizes", "2", "total_outward_cells"), 1023),
        mutate(("transverse_coordinate_star", "sizes", "3", "total_outward_cells"), 12287),
        mutate(("transverse_coordinate_star", "sizes", "2", "minimum_R_lower"), -1.0),
        mutate(("transverse_coordinate_star", "sizes", "3", "minimum_R_lower"), -1.0),
        mutate(("transverse_coordinate_star", "sizes", "3", "sweeps"), {}),
        mutate(("transverse_coordinate_star", "joins", "all_chart_axes_contiguous"), False),
        mutate(("transverse_coordinate_star", "joins", "k194_ray_is_exact_chart_section"), False),
        mutate(("transverse_coordinate_star", "joins", "k194_shape_point_inside_every_shape_axis"), False),
        mutate(("transverse_coordinate_star", "joins", "k193_face_center_exact"), False),
        mutate(("transverse_coordinate_star", "joins", "k192_join_inherited_through_k193"), False),
        mutate(("independent_controls", "all_contained"), False),
        mutate(("independent_controls", "rows"), []),
        mutate(("complete_family_propagation", "all_53_patterns_retain_the_same_formula"), False),
        mutate(("complete_family_propagation", "all_468_occurrences_retain_the_same_formula"), False),
        mutate(("release_test", "all_entries_use_one_shared_scale_and_shape_cell_before_complete_determinant_enclosure"), False),
        mutate(("release_test", "size_two_and_size_three_transverse_chart_outwardly_certified"), False),
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
        raise AssertionError(f"K195 hostile selftest caught {caught}/{len(mutations)}")
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
            raise AssertionError("K195 deterministic replay differs from the tracked manifest")
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
