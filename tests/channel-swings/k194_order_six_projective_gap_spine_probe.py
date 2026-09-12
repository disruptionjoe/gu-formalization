#!/usr/bin/env python3
"""Probe and hostile self-test for the K194 projective-gap spine."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[2]
SOLVER_PATH = ROOT / "tests/channel-swings/k194_order_six_projective_gap_spine.py"
MANIFEST_PATH = ROOT / "lab/process/k194-order-six-projective-gap-spine-wave.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SOLVER = load_module("k194_probe_solver", SOLVER_PATH)


def checks(result: dict[str, Any]) -> list[tuple[str, bool]]:
    spine = result["correlated_projective_spine"]
    sizes = spine["sizes"]
    release = result["release_test"]
    return [
        ("classification", result["classification"] == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", result["direction"] == "observed_to_native"),
        ("patterns", result["fixed_control"]["source_patterns"] == 53),
        ("occurrences", result["fixed_control"]["source_nontrivial_occurrences"] == 468),
        ("entries", result["fixed_control"]["source_time_gram_entries"] == 234),
        ("groups", result["fixed_control"]["source_coherent_groups"] == 18),
        ("translated exact", result["translated_interval_operator"]["symbolic_identities_exact"]),
        ("translated count", result["translated_interval_operator"]["matrix_entries_checked"] == 221),
        ("translated overlap", result["translated_interval_operator"]["interval_evaluations_overlap"] == 221),
        ("all cells", spine["all_cells_strictly_positive"]),
        ("cell count", spine["total_outward_cells"] == 5120),
        ("size two count", sizes["2"]["total_cells"] == 1024),
        ("size three count", sizes["3"]["total_cells"] == 4096),
        ("size two lower", sizes["2"]["minimum_R_lower"] > 0),
        ("size three lower", sizes["3"]["minimum_R_lower"] > 0),
        ("contiguous", spine["all_scale_and_radial_cells_contiguous"]),
        ("join", spine["k193_fully_active_face_center_join"]["join_proved"]),
        ("join exact", spine["k193_fully_active_face_center_join"]["exact_coordinate_match"]),
        ("join radial", spine["k193_fully_active_face_center_join"]["radial_cell_equal"]),
        ("dependency control", result["dependency_loss_control"]["strict_positive_certificate_rejected"]),
        ("controls", result["independent_controls"]["all_contained"]),
        ("control count", len(result["independent_controls"]["rows"]) == 6),
        ("family patterns", result["complete_family_propagation"]["all_53_patterns_retain_the_same_formula"]),
        ("family occurrences", result["complete_family_propagation"]["all_468_occurrences_retain_the_same_formula"]),
        ("common scale cell", release["all_entries_use_one_shared_projective_scale_cell_before_complete_determinant_enclosure"]),
        ("transverse withheld", not release["transverse_arbitrary_gap_ratio_domain_covered"]),
        ("duffy withheld", not release["duffy_jacobi_chain_rule_envelopes_serialized"]),
        ("prefix withheld", not release["accurate_order_six_prefix_released"]),
        ("action withheld", not release["complete_base_action_column_evaluated"]),
        ("physical withheld", result["physical_or_source_selection"] is False),
        ("canon withheld", result["canon_paper_release_or_public_posture_move"] is False),
    ]


def verify(result: dict[str, Any]) -> None:
    failed = [name for name, passed in checks(result) if not passed]
    if failed:
        raise AssertionError("K194 probe failures: " + ", ".join(failed))


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
        mutate(("translated_interval_operator", "symbolic_identities_exact"), False),
        mutate(("translated_interval_operator", "matrix_entries_checked"), 220),
        mutate(("translated_interval_operator", "interval_evaluations_overlap"), 220),
        mutate(("correlated_projective_spine", "all_cells_strictly_positive"), False),
        mutate(("correlated_projective_spine", "total_outward_cells"), 5119),
        mutate(("correlated_projective_spine", "sizes", "2", "total_cells"), 1023),
        mutate(("correlated_projective_spine", "sizes", "3", "total_cells"), 4095),
        mutate(("correlated_projective_spine", "sizes", "2", "minimum_R_lower"), -1.0),
        mutate(("correlated_projective_spine", "sizes", "3", "minimum_R_lower"), -1.0),
        mutate(("correlated_projective_spine", "all_scale_and_radial_cells_contiguous"), False),
        mutate(("correlated_projective_spine", "k193_fully_active_face_center_join", "join_proved"), False),
        mutate(("correlated_projective_spine", "k193_fully_active_face_center_join", "exact_coordinate_match"), False),
        mutate(("correlated_projective_spine", "k193_fully_active_face_center_join", "radial_cell_equal"), False),
        mutate(("dependency_loss_control", "strict_positive_certificate_rejected"), False),
        mutate(("independent_controls", "all_contained"), False),
        mutate(("independent_controls", "rows"), []),
        mutate(("complete_family_propagation", "all_53_patterns_retain_the_same_formula"), False),
        mutate(("complete_family_propagation", "all_468_occurrences_retain_the_same_formula"), False),
        mutate(("release_test", "all_entries_use_one_shared_projective_scale_cell_before_complete_determinant_enclosure"), False),
        mutate(("release_test", "transverse_arbitrary_gap_ratio_domain_covered"), True),
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
        raise AssertionError(f"K194 hostile selftest caught {caught}/{len(mutations)}")
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
            raise AssertionError("K194 deterministic replay differs from the tracked manifest")
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
