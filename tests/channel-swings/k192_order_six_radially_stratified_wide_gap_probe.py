#!/usr/bin/env python3
"""Independent replay, reporting and hostile controls for K192."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k192-order-six-radially-stratified-wide-gap-wave.json"
SOLVER = ROOT / "tests/channel-swings/k192_order_six_radially_stratified_wide_gap.py"


def load_solver():
    spec = importlib.util.spec_from_file_location("k192_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K192 solver")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K192 = load_solver()


def check(data: dict, replay: bool = True) -> list[tuple[str, bool]]:
    fixed = data.get("fixed_control", {})
    theorem = data.get("retained_theorem", {})
    low = data.get("low_radial_wide_gap_certificate", {})
    high = data.get("retained_high_radial_certificate", {})
    union = data.get("stratified_union", {})
    controls = data.get("independent_controls", {})
    rejected = data.get("rejected_candidate_control", {})
    decision = data.get("decision", {})
    release = data.get("release_test", {})
    low2 = low.get("sizes", {}).get("2", [])
    low3 = low.get("sizes", {}).get("3", [])
    high2 = high.get("sizes", {}).get("2", [])
    high3 = high.get("sizes", {}).get("3", [])
    checks = [
        ("classification", data.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("retained algebra", theorem.get("algebra_or_tail_rule_changed") is False),
        ("wide radius", fixed.get("low_radial_maximum_row_spread_over_cell_base") == "1/48"),
        ("radial cells mirrored", low.get("radial_cells") == len(low2) == len(low3) and len(low2) > 0),
        ("low endpoints", low2[0].get("base_x") == f"1/{2**200}" and low2[-1].get("upper_x") == "1/8"),
        ("low adjacency", all(a["upper_x"] == b["base_x"] for a, b in zip(low2, low2[1:]))),
        ("low positivity", low.get("all_cells_strictly_positive") is True and min(row["R_lower"] for row in low3) > 0),
        ("high endpoints", high2[0].get("base_x") == "1/8" and high2[-1].get("upper_x") == "1/4"),
        ("high mirrored", len(high2) == len(high3) and len(high2) > 0),
        ("union gapless", union.get("radial_range_has_no_gap") is True and low2[-1]["upper_x"] == high2[0]["base_x"]),
        ("gain factor", Fraction(union.get("wide_gap_radius_gain_factor")) == Fraction(32, 3)),
        ("53 patterns", fixed.get("source_patterns") == 53 and union.get("all_53_patterns_covered_conditionally_on_the_stratified_spread_rule") is True),
        ("468 occurrences", fixed.get("source_nontrivial_occurrences") == 468 and union.get("all_468_occurrences_covered_conditionally_on_the_stratified_spread_rule") is True),
        ("independent controls", controls.get("all_controls_contained") is True and all(row.get("contained") for row in controls.get("rows", []))),
        ("rejected coarse candidate", rejected.get("candidate_gap_radius") == "1/32" and rejected.get("strict_positive_cell_rejected") is True),
        ("local release boundary", decision.get("radially_stratified_wide_gap_region_certified") is True and decision.get("arbitrary_gap_ratio_coverage_complete") is False),
        ("next chart explicit", decision.get("noncoalescent_face_recentering_required_next") is True),
        ("downstream held", release.get("duffy_jacobi_chain_rule_envelopes_serialized") is False and release.get("accurate_order_six_prefix_released") is False),
        ("no physical effect", data.get("physical_or_source_selection") is False and data.get("canon_paper_release_or_public_posture_move") is False),
    ]
    if replay:
        checks.append(("deterministic replay", K192.build() == data))
    return checks


def mutations(data: dict):
    candidates = []

    def add(name, mutate):
        candidate = copy.deepcopy(data)
        mutate(candidate)
        candidates.append((name, candidate))

    add("classification", lambda d: d.__setitem__("classification", "PROVED"))
    add("algebra", lambda d: d["retained_theorem"].__setitem__("algebra_or_tail_rule_changed", True))
    add("radius", lambda d: d["fixed_control"].__setitem__("low_radial_maximum_row_spread_over_cell_base", "1/4"))
    add("cell count", lambda d: d["low_radial_wide_gap_certificate"].__setitem__("radial_cells", 1))
    add("low endpoint", lambda d: d["low_radial_wide_gap_certificate"]["sizes"]["2"][0].__setitem__("base_x", "1/2"))
    add("low adjacency", lambda d: d["low_radial_wide_gap_certificate"]["sizes"]["2"][1].__setitem__("base_x", "1/3"))
    add("low positivity", lambda d: d["low_radial_wide_gap_certificate"]["sizes"]["3"][0].__setitem__("R_lower", -1))
    add("high endpoint", lambda d: d["retained_high_radial_certificate"]["sizes"]["2"][0].__setitem__("base_x", "1/7"))
    add("union", lambda d: d["stratified_union"].__setitem__("radial_range_has_no_gap", False))
    add("gain", lambda d: d["stratified_union"].__setitem__("wide_gap_radius_gain_factor", "1"))
    add("patterns", lambda d: d["fixed_control"].__setitem__("source_patterns", 52))
    add("occurrences", lambda d: d["fixed_control"].__setitem__("source_nontrivial_occurrences", 467))
    add("control", lambda d: d["independent_controls"].__setitem__("all_controls_contained", False))
    add("negative control", lambda d: d["rejected_candidate_control"].__setitem__("strict_positive_cell_rejected", False))
    add("local result", lambda d: d["decision"].__setitem__("radially_stratified_wide_gap_region_certified", False))
    add("global overclaim", lambda d: d["decision"].__setitem__("arbitrary_gap_ratio_coverage_complete", True))
    add("chart omitted", lambda d: d["decision"].__setitem__("noncoalescent_face_recentering_required_next", False))
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
