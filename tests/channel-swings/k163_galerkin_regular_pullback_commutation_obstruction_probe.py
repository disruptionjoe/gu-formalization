#!/usr/bin/env python3
"""Baseline-first exact and hostile controls for K163."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k163-galerkin-regular-pullback-commutation-obstruction-wave.json"
SOLVER = Path(__file__).with_name("k163_galerkin_regular_pullback_commutation_obstruction.py")


def load_solver():
    spec = importlib.util.spec_from_file_location("k163_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K163 solver")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K163 = load_solver()


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    discriminator = data.get("galerkin_discriminator", {})
    columns = data.get("fixed_cylinder_enclosure", {})
    source = data.get("source_and_physics", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    if discriminator.get("free_form_Galerkin_congruence") is not True:
        failures.append("free_form")
    denied_discriminator = (
        "raw_cutoff_Hamiltonian_congruence",
        "regular_pullback_congruence",
        "independent_coarse_rediscretization_is_native_anchor",
    )
    if any(discriminator.get(key) is not False for key in denied_discriminator):
        failures.append("commutation")
    if discriminator.get("first_raw_defect") != "2/105":
        failures.append("raw_defect")
    if columns.get("K161_all_five_weighted_components_used") is not True:
        failures.append("five_tails")
    if columns.get("same_family_anchor_required") is not True or columns.get("K162_refinement_Gram_proof_required") is not True:
        failures.append("anchor_requirements")
    denied_columns = (
        "native_same_family_anchor_supplied",
        "complete_shifted_form_dual_residual_serialized",
        "coercivity_serialized",
        "next_distinct_spectrum_serialized",
        "native_left_floor_serialized",
        "native_ground_count_emitted",
        "native_K152_interval_emitted",
    )
    if any(columns.get(key) is not False for key in denied_columns):
        failures.append("native_boundary")
    denied_source = (
        "ledger_changed",
        "source_register_changed",
        "physical_or_source_selection",
        "Born_prediction_or_confirmation_credit",
        "canon_paper_release_or_public_posture_move",
    )
    if any(source.get(key) is not False for key in denied_source):
        failures.append("source_boundary")
    for token in ("free form", "2/105", "same-family", "residual", "coercivity", "spectral floor", "no physical/source", "Born"):
        if token not in str(data.get("claim_ceiling", "")):
            failures.append("ceiling:" + token)
    return failures


def exact_checks() -> list[tuple[str, bool]]:
    demo = K163.demo()
    discriminator = demo["commutation_discriminator"]
    c4096 = demo["conditional_fixed_cylinder_n4096"]
    c65536 = demo["conditional_fixed_cylinder_n65536"]
    ready = demo["native_K152_readiness"]
    return [
        ("quadratic field is exact", (K163.Q2(0, 1) * K163.Q2(0, 1)).exact() == "2"),
        ("physical cell widths", discriminator["cell_widths"] == {"coarse": "2", "fine": "1"}),
        ("free energy averages", discriminator["fine_energies"] == ["1", "3"] and discriminator["coarse_free_energy"] == "2"),
        ("point coupling scales with cell norm", discriminator["point_couplings"] == {"coarse": "sqrt(2)", "fine": ["1", "1"]}),
        ("representative dimensions", discriminator["coarse_dimension"] == 8 and discriminator["fine_dimension"] == 84),
        ("free form compresses", discriminator["free_form_galerkin_congruence"] is True),
        ("raw cutoff does not commute", discriminator["raw_cutoff_hamiltonian_congruence"] is False),
        ("raw defect is exact", discriminator["first_raw_defect"]["difference"] == "2/105"),
        ("regular pullback does not commute", discriminator["regular_pullback_congruence"] is False),
        ("regular defect is nonzero", discriminator["first_regular_defect"]["difference"] != "0"),
        ("independent anchor rejected", discriminator["independent_coarse_rediscretization_is_native_anchor"] is False),
        ("missing same-family anchor fails", demo["native_anchor_failure"] == "fixed-cylinder enclosure requires a same-family finite anchor"),
        ("K161 n4096 tail reused", c4096["complete_weighted_tail_upper"] == "79277/319488"),
        ("n4096 fixed-column bound", c4096["fixed_cylinder_action_column_error_upper"] == "396385/319488"),
        ("K161 n65536 tail reused", c65536["complete_weighted_tail_upper"] == "6622297/123076608"),
        ("n65536 fixed-column bound", c65536["fixed_cylinder_action_column_error_upper"] == "33111485/123076608"),
        ("larger cutoff improves column bound", K163.q(c65536["fixed_cylinder_action_column_error_upper"]) < K163.q(c4096["fixed_cylinder_action_column_error_upper"])),
        ("all five components used", c4096["all_five_K161_components_used"] is True),
        ("column is not complete residual", c4096["complete_form_dual_residual"] is False),
        ("column is not a floor", c4096["coercivity_or_spectral_floor"] is False),
        ("five K152 seams remain", len(ready["missing_native_references"]) == 5),
        ("K152 remains closed", ready["native_K152_interface_complete"] is False),
        ("no native count", ready["native_ground_count_emitted"] is False),
        ("no native interval", ready["native_K152_interval_emitted"] is False),
        ("no source selection", demo["physical_or_source_selection"] is False),
        ("no Born credit", demo["Born_prediction_or_confirmation_credit"] is False),
    ]


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    mutations = (
        ("erase_free", lambda d: d["galerkin_discriminator"].__setitem__("free_form_Galerkin_congruence", False)),
        ("invent_raw", lambda d: d["galerkin_discriminator"].__setitem__("raw_cutoff_Hamiltonian_congruence", True)),
        ("invent_regular", lambda d: d["galerkin_discriminator"].__setitem__("regular_pullback_congruence", True)),
        ("invent_anchor", lambda d: d["galerkin_discriminator"].__setitem__("independent_coarse_rediscretization_is_native_anchor", True)),
        ("change_defect", lambda d: d["galerkin_discriminator"].__setitem__("first_raw_defect", "0")),
        ("drop_tail", lambda d: d["fixed_cylinder_enclosure"].__setitem__("K161_all_five_weighted_components_used", False)),
        ("drop_family", lambda d: d["fixed_cylinder_enclosure"].__setitem__("same_family_anchor_required", False)),
        ("drop_gram", lambda d: d["fixed_cylinder_enclosure"].__setitem__("K162_refinement_Gram_proof_required", False)),
        ("invent_native_anchor", lambda d: d["fixed_cylinder_enclosure"].__setitem__("native_same_family_anchor_supplied", True)),
        ("invent_residual", lambda d: d["fixed_cylinder_enclosure"].__setitem__("complete_shifted_form_dual_residual_serialized", True)),
        ("invent_coercivity", lambda d: d["fixed_cylinder_enclosure"].__setitem__("coercivity_serialized", True)),
        ("invent_gap", lambda d: d["fixed_cylinder_enclosure"].__setitem__("next_distinct_spectrum_serialized", True)),
        ("invent_floor", lambda d: d["fixed_cylinder_enclosure"].__setitem__("native_left_floor_serialized", True)),
        ("invent_count", lambda d: d["fixed_cylinder_enclosure"].__setitem__("native_ground_count_emitted", True)),
        ("invent_interval", lambda d: d["fixed_cylinder_enclosure"].__setitem__("native_K152_interval_emitted", True)),
        ("invent_source", lambda d: d["source_and_physics"].__setitem__("physical_or_source_selection", True)),
        ("invent_born", lambda d: d["source_and_physics"].__setitem__("Born_prediction_or_confirmation_credit", True)),
        ("promote", lambda d: d["source_and_physics"].__setitem__("canon_paper_release_or_public_posture_move", True)),
        ("break_routing", lambda d: d.__setitem__("classification", "SOURCE_NATIVE_ROUTE")),
    )
    caught = 0
    for _, mutate in mutations:
        candidate = copy.deepcopy(data)
        mutate(candidate)
        caught += bool(manifest_failures(candidate))
    print(f"K163 HOSTILE SELFTEST: {caught}/{len(mutations)} mutations caught")
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
    print(f"K163 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if args.selftest:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
