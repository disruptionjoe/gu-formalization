#!/usr/bin/env python3
"""Independent exact, replay, reporting, and hostile controls for K191."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import itertools
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k191-order-six-near-coalescent-taylor-box-wave.json"
SOLVER = ROOT / "tests/channel-swings/k191_order_six_near_coalescent_taylor_box.py"
K186 = ROOT / "lab/process/k186-order-six-bessel-vandermonde-wave.json"


def load_solver():
    spec = importlib.util.spec_from_file_location("k191_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K191 solver")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K191 = load_solver()


def determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def newton_matrix(function, rows, columns):
    matrix = [[function(row + column) for column in columns] for row in rows]
    size = len(rows)
    for order in range(1, size):
        for row in range(size - 1, order - 1, -1):
            for column in range(size):
                matrix[row][column] = (
                    matrix[row][column] - matrix[row - 1][column]
                ) / (rows[row] - rows[row - order])
    for order in range(1, size):
        for column in range(size - 1, order - 1, -1):
            for row in range(size):
                matrix[row][column] = (
                    matrix[row][column] - matrix[row][column - 1]
                ) / (columns[column] - columns[column - order])
    return matrix


def exact_cauchy_controls() -> bool:
    cases = {
        2: [
            ([Fraction(1, 32), Fraction(0)], [Fraction(1, 64), Fraction(0)], Fraction(1, 80)),
            ([Fraction(1, 128), Fraction(0)], [Fraction(1, 96), Fraction(0)], Fraction(1, 40)),
        ],
        3: [
            (
                [Fraction(1, 32), Fraction(1, 80), Fraction(0)],
                [Fraction(1, 48), Fraction(1, 96), Fraction(0)],
                Fraction(1, 64),
            ),
            (
                [Fraction(1, 100), Fraction(1, 125), Fraction(0)],
                [Fraction(1, 90), Fraction(1, 140), Fraction(0)],
                Fraction(1, 50),
            ),
        ],
    }
    for size, rows in cases.items():
        for row_nodes, column_nodes, radial in rows:
            matrix = newton_matrix(
                lambda value: Fraction(1, 1) / (1 + radial + value),
                row_nodes,
                column_nodes,
            )
            product = Fraction(1)
            for row in row_nodes:
                for column in column_nodes:
                    product *= 1 + radial + row + column
            if determinant(matrix) * product != 1:
                return False
    return True


def check(data: dict, replay: bool = True) -> list[tuple[str, bool]]:
    source = json.loads(K186.read_text())
    fixed = data.get("fixed_control", {})
    identity = data.get("normalized_identity", {})
    theorem = data.get("taylor_theorem", {})
    outward = data.get("outward_certificate", {})
    family = data.get("complete_family_propagation", {})
    controls = data.get("independent_controls", {})
    decision = data.get("decision", {})
    release = data.get("release_test", {})
    sizes = outward.get("sizes", {})
    size2 = sizes.get("2", [])
    size3 = sizes.get("3", [])
    checks = [
        ("classification", data.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("exact Cauchy controls", exact_cauchy_controls()),
        ("normalized identity", identity.get("common_radial_scale_cancelled_before_interval_evaluation") is True),
        ("correlation retained", identity.get("row_column_correlations_retained_through_complete_divided_difference_entries") is True),
        ("Taylor order", fixed.get("taylor_order") == K191.TAYLOR_ORDER == 16),
        ("tail theorem", "monotone" in theorem.get("tail_basis", "")),
        ("radial cells mirrored", outward.get("radial_cells") == len(size2) == len(size3) and len(size2) > 0),
        ("radial endpoints", size2[0].get("base_x") == f"1/{2**200}" and size2[-1].get("upper_x") == "1/4"),
        ("radial adjacency", all(a["upper_x"] == b["base_x"] for a, b in zip(size2, size2[1:]))),
        ("strict positivity", outward.get("all_cells_strictly_positive") is True and min(row["R_lower"] for row in size3) > 0),
        ("53 patterns", fixed.get("source_patterns") == len(source["unique_patterns"]) == 53 and family.get("all_53_patterns_covered_conditionally_on_spread_box") is True),
        ("468 occurrences", fixed.get("source_nontrivial_occurrences") == 468 and family.get("all_468_occurrences_covered_conditionally_on_spread_box") is True),
        ("independent controls", controls.get("all_controls_contained") is True and all(row.get("contained") for row in controls.get("rows", []))),
        ("local release boundary", decision.get("nonzero_gap_outward_region_certified") is True and decision.get("arbitrary_gap_ratio_coverage_complete") is False),
        ("downstream held", release.get("duffy_jacobi_chain_rule_envelopes_serialized") is False and release.get("accurate_order_six_prefix_released") is False and release.get("complete_base_action_column_evaluated") is False),
        ("no physical effect", data.get("physical_or_source_selection") is False and data.get("canon_paper_release_or_public_posture_move") is False),
    ]
    if replay:
        checks.append(("deterministic replay", K191.build() == data))
    return checks


def mutations(data: dict):
    candidates = []

    def add(name, mutate):
        candidate = copy.deepcopy(data)
        mutate(candidate)
        candidates.append((name, candidate))

    add("classification", lambda d: d.__setitem__("classification", "PROVED"))
    add("scale", lambda d: d["normalized_identity"].__setitem__("common_radial_scale_cancelled_before_interval_evaluation", False))
    add("correlation", lambda d: d["normalized_identity"].__setitem__("row_column_correlations_retained_through_complete_divided_difference_entries", False))
    add("Taylor", lambda d: d["fixed_control"].__setitem__("taylor_order", 8))
    add("tail", lambda d: d["taylor_theorem"].__setitem__("tail_basis", "sampled"))
    add("cell count", lambda d: d["outward_certificate"].__setitem__("radial_cells", 1))
    add("endpoint", lambda d: d["outward_certificate"]["sizes"]["2"][0].__setitem__("base_x", "1/2"))
    add("adjacency", lambda d: d["outward_certificate"]["sizes"]["2"][1].__setitem__("base_x", "1/3"))
    add("positivity flag", lambda d: d["outward_certificate"].__setitem__("all_cells_strictly_positive", False))
    add("positive lower", lambda d: d["outward_certificate"]["sizes"]["3"][0].__setitem__("R_lower", -1))
    add("patterns", lambda d: d["fixed_control"].__setitem__("source_patterns", 52))
    add("occurrences", lambda d: d["fixed_control"].__setitem__("source_nontrivial_occurrences", 467))
    add("control", lambda d: d["independent_controls"].__setitem__("all_controls_contained", False))
    add("local result", lambda d: d["decision"].__setitem__("nonzero_gap_outward_region_certified", False))
    add("global overclaim", lambda d: d["decision"].__setitem__("arbitrary_gap_ratio_coverage_complete", True))
    add("cubature overclaim", lambda d: d["release_test"].__setitem__("duffy_jacobi_chain_rule_envelopes_serialized", True))
    add("prefix overclaim", lambda d: d["release_test"].__setitem__("accurate_order_six_prefix_released", True))
    add("physical overclaim", lambda d: d.__setitem__("physical_or_source_selection", True))
    return candidates


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text())
    baseline = check(data)
    failed = [name for name, passed in baseline if not passed]
    if failed:
        print("FAIL baseline:", ", ".join(failed))
        return 1
    print(f"PASS {len(baseline)}/{len(baseline)}")
    if not args.selftest:
        return 0
    caught = 0
    for name, candidate in mutations(data):
        if any(not passed for _, passed in check(candidate, replay=False)):
            caught += 1
        else:
            print("MISS hostile mutation:", name)
    print(f"hostile {caught}/{len(mutations(data))} caught")
    return 0 if caught == len(mutations(data)) else 1


if __name__ == "__main__":
    raise SystemExit(main())
