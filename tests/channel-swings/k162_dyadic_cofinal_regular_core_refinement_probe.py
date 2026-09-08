#!/usr/bin/env python3
"""Baseline-first exact and hostile controls for K162."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k162-dyadic-cofinal-regular-core-refinement-wave.json"
SOLVER = Path(__file__).with_name("k162_dyadic_cofinal_regular_core_refinement.py")


def load_solver():
    spec = importlib.util.spec_from_file_location("k162_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K162 solver")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K162 = load_solver()


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    family = data.get("dyadic_common_carrier", {})
    exterior = data.get("exterior_refinement", {})
    regular = data.get("regular_K152_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    required_family = (
        "delta_j_is_2_to_minus_j", "Lambda_j_is_2_to_j", "literal_nested_cell_ranges",
        "unnormalized_indicator_refinement_exact", "physical_refinement_is_Gram_isometric",
    )
    if any(family.get(key) is not True for key in required_family):
        failures.append("family")
    if family.get("K157_zero_fill_is_physical_cell_refinement") is not False:
        failures.append("zero_fill")
    required_exterior = (
        "hard_core_preserved", "charge_preserved", "CAR_signs_exact",
        "Fock_Gram_isometry", "signed_flavor_swap_complete",
    )
    if any(exterior.get(key) is not True for key in required_exterior):
        failures.append("exterior")
    proved = (
        "true_nested_cofinal_family", "same_family_Gram_transport",
        "same_family_form_basis_rule", "signed_charge_intertwiner_complete",
        "K161_five_tail_bounds_family_compatible",
    )
    denied = (
        "regular_core_bound_B_serialized", "total_form_dual_residual_serialized",
        "coercivity_serialized", "next_distinct_spectrum_serialized",
        "native_left_floor_serialized", "native_ground_count_emitted",
        "native_K152_interval_emitted", "physical_or_source_selection",
        "Born_prediction_or_confirmation_credit", "canon_paper_release_or_public_posture_move",
    )
    if any(regular.get(key) is not True for key in proved) or any(regular.get(key) is not False for key in denied):
        failures.append("regular_boundary")
    for token in ("dyadic", "zero-fill", "exterior", "Gram", "five", "no native", "Born"):
        if token not in str(data.get("claim_ceiling", "")):
            failures.append("ceiling:" + token)
    return failures


def exact_checks() -> list[tuple[str, bool]]:
    demo = K162.demo()
    one = demo["one_particle"]
    blocks = demo["exterior_charge_blocks"]
    form = demo["form_transport_control"]
    ready = demo["native_K152_readiness"]
    return [
        ("coarse and fine mesh are dyadic", one["coarse_delta"] == "1" and one["fine_delta"] == "1/2"),
        ("physical cutoff expands", one["coarse_cutoff"] == "1" and one["fine_cutoff"] == "2"),
        ("cell census expands", one["coarse_cell_count"] == 2 and one["fine_cell_count"] == 8),
        ("cell support refines literally", one["literal_support_refinement"] is True),
        ("one particle Gram isometry", one["physical_refinement_gram_isometry"] is True),
        ("zero fill halves one-cell norm", one["zero_fill_gram_factor"] == "1/2"),
        ("zero fill is rejected", one["zero_fill_is_physical_refinement"] is False),
        ("three charge representatives tested", [row["charge"] for row in blocks] == [[0, 0], [1, 0], [0, 1]]),
        ("hard core preserved", all(row["hard_core_preserved"] for row in blocks)),
        ("charge preserved", all(row["charge_preserved"] for row in blocks)),
        ("CAR signs exact", all(row["exterior_power_CAR_signs_exact"] for row in blocks)),
        ("Fock Gram isometry", all(row["fock_gram_isometry"] for row in blocks)),
        ("signed flavor transport", all(row["signed_flavor_swap_commutes"] for row in blocks)),
        ("nontrivial wedge expansion", max(row["maximum_expansion_terms"] for row in blocks) >= 16),
        ("nondiagonal form basis law", form["works_for_nondiagonal_form"] is True),
        ("zero fill changes pulled form", form["zero_fill_gives_same_pullback"] is False),
        ("native form values not invented", form["native_form_entries_supplied"] is False),
        ("cofinal family complete", ready["true_nested_cofinal_family"] is True),
        ("five tails family-compatible", ready["K161_five_tail_bounds_compatible_with_family"] is True),
        ("B remains open", ready["regular_core_bound_B_serialized"] is False),
        ("residual remains open", ready["total_shifted_form_dual_residual_serialized"] is False),
        ("gap remains open", ready["next_distinct_spectrum_floor_serialized"] is False),
        ("left floor remains open", ready["native_left_floor_serialized"] is False),
        ("no native count", ready["native_ground_count_emitted"] is False),
        ("no native K152 interval", ready["native_K152_interval_emitted"] is False),
    ]


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    mutations = (
        ("accept_zero_fill", lambda d: d["dyadic_common_carrier"].__setitem__("K157_zero_fill_is_physical_cell_refinement", True)),
        ("erase_gram", lambda d: d["dyadic_common_carrier"].__setitem__("physical_refinement_is_Gram_isometric", False)),
        ("erase_car", lambda d: d["exterior_refinement"].__setitem__("CAR_signs_exact", False)),
        ("erase_flavor", lambda d: d["exterior_refinement"].__setitem__("signed_flavor_swap_complete", False)),
        ("invent_B", lambda d: d["regular_K152_boundary"].__setitem__("regular_core_bound_B_serialized", True)),
        ("invent_residual", lambda d: d["regular_K152_boundary"].__setitem__("total_form_dual_residual_serialized", True)),
        ("invent_coercivity", lambda d: d["regular_K152_boundary"].__setitem__("coercivity_serialized", True)),
        ("invent_gap", lambda d: d["regular_K152_boundary"].__setitem__("next_distinct_spectrum_serialized", True)),
        ("invent_floor", lambda d: d["regular_K152_boundary"].__setitem__("native_left_floor_serialized", True)),
        ("invent_count", lambda d: d["regular_K152_boundary"].__setitem__("native_ground_count_emitted", True)),
        ("invent_interval", lambda d: d["regular_K152_boundary"].__setitem__("native_K152_interval_emitted", True)),
        ("invent_source", lambda d: d["regular_K152_boundary"].__setitem__("physical_or_source_selection", True)),
        ("invent_Born", lambda d: d["regular_K152_boundary"].__setitem__("Born_prediction_or_confirmation_credit", True)),
        ("promote", lambda d: d["regular_K152_boundary"].__setitem__("canon_paper_release_or_public_posture_move", True)),
        ("break_routing", lambda d: d.__setitem__("classification", "SOURCE_NATIVE_ROUTE")),
    )
    caught = 0
    for _, mutate in mutations:
        candidate = copy.deepcopy(data)
        mutate(candidate)
        caught += bool(manifest_failures(candidate))
    print(f"K162 HOSTILE SELFTEST: {caught}/{len(mutations)} mutations caught")
    return 0 if caught == len(mutations) else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text())
    checks = exact_checks()
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + " " + name)
    failures = manifest_failures(data)
    if failures:
        print("MANIFEST FAILURES: " + ", ".join(failures))
    print(f"K162 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if args.selftest:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
