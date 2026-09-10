#!/usr/bin/env python3
"""Independent replay and hostile release-boundary controls for K193."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k193-order-six-shifted-face-entry-wave.json"
SOLVER = ROOT / "tests/channel-swings/k193_order_six_shifted_face_entry.py"


def load_solver():
    spec = importlib.util.spec_from_file_location("k193_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K193 solver")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K193 = load_solver()


def check(data: dict, replay: bool = True) -> list[tuple[str, bool]]:
    fixed = data.get("fixed_control", {})
    operator = data.get("shifted_operator", {})
    exact = operator.get("exact_translation_checks", {})
    charts = data.get("outward_face_charts", {})
    sizes = charts.get("sizes", {})
    size2 = sizes.get("2", [])
    size3 = sizes.get("3", [])
    controls = data.get("independent_controls", {})
    family = data.get("complete_family_propagation", {})
    decision = data.get("decision", {})
    release = data.get("release_test", {})
    checks = [
        ("classification", data.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("radial cell", fixed.get("radial_cell") == "31/256<=x<=1/8" and Fraction(fixed.get("relative_radial_width")) == Fraction(1, 31)),
        ("chart widths", fixed.get("active_coordinate_half_width") == "1/512" and fixed.get("inactive_coordinate_upper") == "1/512"),
        ("exact translation", exact.get("all_exact") is True and exact.get("matrix_entries_checked") == 221),
        ("shared dependencies", operator.get("shared_face_center_dependencies_retained") is True),
        ("Cauchy cofactors", operator.get("determinant_level_cauchy_cofactors_retained") is True),
        ("chart counts", charts.get("size_two_chart_count") == len(size2) == 3 and charts.get("size_three_chart_count") == len(size3) == 15),
        ("all masks unique", len({tuple(row.get("active", [])) for row in size3}) == 15),
        ("all charts positive", charts.get("all_18_charts_strictly_positive") is True and all(row.get("strictly_positive") for row in size2 + size3)),
        ("positive lower bounds", min(row.get("R_lower", -1) for row in size2 + size3) > 0),
        ("outward symmetry", all(row.get("R_lower") < 1 < row.get("R_upper") for row in size2 + size3)),
        ("entry geometry", all(len(row.get("entry_shifts", [])) == int(size) ** 2 and len(row.get("entry_radii", [])) == int(size) ** 2 for size, rows in sizes.items() for row in rows)),
        ("independent controls", controls.get("all_contained") is True and len(controls.get("rows", [])) == 2 and all(row.get("contained") for row in controls.get("rows", []))),
        ("53 patterns", fixed.get("source_patterns") == 53 and family.get("all_53_patterns_retain_the_same_formula") is True),
        ("468 occurrences", fixed.get("source_nontrivial_occurrences") == 468 and family.get("all_468_occurrences_retain_the_same_formula") is True),
        ("234 entries", fixed.get("source_time_gram_entries") == 234 and family.get("all_234_entries_and_18_groups_remain_in_scope") is True),
        ("18 groups", fixed.get("source_coherent_groups") == 18),
        ("operator released", decision.get("shifted_face_entry_operator_serialized") is True and decision.get("shared_center_and_cauchy_cofactor_requirements_closed") is True),
        ("face neighborhoods", decision.get("all_k192_face_centers_have_a_strict_outward_neighborhood_on_the_rejected_high_radial_cell") is True),
        ("local boundary", decision.get("residual_gap_simplex_union_complete") is False),
        ("next union explicit", "tile the ordered physical gap-ratio domain" in decision.get("next_exact_input", "")),
        ("shifted release", release.get("shifted_hermite_genocchi_entry_tail_serialized") is True and release.get("all_15_size_three_face_centers_outwardly_certified") is True),
        ("global release held", release.get("arbitrary_gap_ratio_domain_covered") is False and release.get("duffy_jacobi_chain_rule_envelopes_serialized") is False and release.get("accurate_order_six_prefix_released") is False),
        ("no physical effect", data.get("physical_or_source_selection") is False and data.get("Born_prediction_or_confirmation_credit") is False and data.get("canon_paper_release_or_public_posture_move") is False),
    ]
    if replay:
        checks.append(("deterministic replay", K193.build() == data))
    return checks


def mutations(data: dict):
    candidates = []

    def add(name, mutate):
        candidate = copy.deepcopy(data)
        mutate(candidate)
        candidates.append((name, candidate))

    add("classification", lambda d: d.__setitem__("classification", "PROVED"))
    add("radial cell", lambda d: d["fixed_control"].__setitem__("radial_cell", "0<=x<=1"))
    add("chart width", lambda d: d["fixed_control"].__setitem__("active_coordinate_half_width", "1/2"))
    add("translation", lambda d: d["shifted_operator"]["exact_translation_checks"].__setitem__("all_exact", False))
    add("translation count", lambda d: d["shifted_operator"]["exact_translation_checks"].__setitem__("matrix_entries_checked", 1))
    add("dependencies", lambda d: d["shifted_operator"].__setitem__("shared_face_center_dependencies_retained", False))
    add("cofactors", lambda d: d["shifted_operator"].__setitem__("determinant_level_cauchy_cofactors_retained", False))
    add("size2 count", lambda d: d["outward_face_charts"].__setitem__("size_two_chart_count", 2))
    add("size3 count", lambda d: d["outward_face_charts"].__setitem__("size_three_chart_count", 14))
    add("duplicate mask", lambda d: d["outward_face_charts"]["sizes"]["3"][1].__setitem__("active", d["outward_face_charts"]["sizes"]["3"][0]["active"]))
    add("chart positivity", lambda d: d["outward_face_charts"]["sizes"]["3"][0].__setitem__("strictly_positive", False))
    add("lower bound", lambda d: d["outward_face_charts"]["sizes"]["3"][0].__setitem__("R_lower", -1))
    add("entry geometry", lambda d: d["outward_face_charts"]["sizes"]["3"][0].__setitem__("entry_shifts", []))
    add("control", lambda d: d["independent_controls"].__setitem__("all_contained", False))
    add("patterns", lambda d: d["fixed_control"].__setitem__("source_patterns", 52))
    add("occurrences", lambda d: d["fixed_control"].__setitem__("source_nontrivial_occurrences", 467))
    add("entries", lambda d: d["fixed_control"].__setitem__("source_time_gram_entries", 233))
    add("groups", lambda d: d["fixed_control"].__setitem__("source_coherent_groups", 17))
    add("operator", lambda d: d["decision"].__setitem__("shifted_face_entry_operator_serialized", False))
    add("face neighborhoods", lambda d: d["decision"].__setitem__("all_k192_face_centers_have_a_strict_outward_neighborhood_on_the_rejected_high_radial_cell", False))
    add("global overclaim", lambda d: d["decision"].__setitem__("residual_gap_simplex_union_complete", True))
    add("next missing", lambda d: d["decision"].__setitem__("next_exact_input", "done"))
    add("shifted release", lambda d: d["release_test"].__setitem__("shifted_hermite_genocchi_entry_tail_serialized", False))
    add("cubature overclaim", lambda d: d["release_test"].__setitem__("duffy_jacobi_chain_rule_envelopes_serialized", True))
    add("physical overclaim", lambda d: d.__setitem__("physical_or_source_selection", True))
    return candidates


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--no-replay", action="store_true")
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text())
    baseline = check(data, replay=not args.no_replay)
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
