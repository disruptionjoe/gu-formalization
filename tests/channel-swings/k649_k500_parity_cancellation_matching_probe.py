#!/usr/bin/env python3
"""Independent exact and hostile controls for K649."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k649-k500-parity-cancellation-matching.json"


def load_solver():
    path = Path(__file__).with_name("k649_k500_parity_cancellation_matching.py")
    spec = importlib.util.spec_from_file_location("k649_probe_solver", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


SOLVER = load_solver()


def failures(data: dict) -> list[str]:
    bad: list[str] = []
    theorem = data.get("parity_matching_theorem", {})
    route = data.get("quantitative_route_consequence", {})
    control = data.get("exact_control", {})
    native = data.get("native_interface_status", {})
    dep = data.get("dependency_reconciliation", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        bad.append("routing")
    required_theorem = (
        "each_mismatched_parity_component_has_harmonic_divergent_direction",
        "complete_matched_combination_remains_the_valid_object",
    )
    if any(theorem.get(key) is not True for key in required_theorem):
        bad.append("theorem_true")
    if theorem.get("cross_total_parity_subtraction_required") is not False or theorem.get("parity_change_makes_separate_singular_factors_bounded") is not False:
        bad.append("theorem_scope")
    if route.get("K644_raw_row_route_disproved") is not False or route.get("K644_raw_row_route_automatically_available_from_parity") is not False:
        bad.append("route_ceiling")
    if route.get("separate_channel_Hilbert_bounds_require_new_proof") is not True or route.get("cancellation_adapted_complete_parity_form_route_live") is not True:
        bad.append("route")
    required_control = (
        "T_T_transpose_equals_2I", "inverse_is_half_transpose", "identity_matching_is_basis_invariant",
        "parity_plus_block_identity", "parity_minus_block_identity", "cross_parity_matching_blocks_zero",
        "nonidentity_matching_remains_nonidentity", "mismatched_divergent_direction_exists",
    )
    if control.get("transform_rank") != 6 or any(control.get(key) is not True for key in required_control):
        bad.append("control")
    if native.get("native_parity_cancellation_matching_proved") is not True:
        bad.append("native_true")
    required_false = (
        "separated_singular_channel_bounds_identified", "actual_parity_block_floors_identified",
        "actual_uniform_parity_tails_identified", "native_global_m_identified",
        "native_remainder_alpha_delta_identified", "K473_released", "native_K152_interval_emitted",
    )
    if any(native.get(key) is not False for key in required_false):
        bad.append("native_ceiling")
    if dep.get("K638_matching_uniqueness_preserved") is not True or dep.get("K644_sufficient_Hilbert_block_theorem_retracted") is not False:
        bad.append("dependency")
    if data.get("source_and_ledger_effect") != "none":
        bad.append("ledger")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("unique identity subtraction remains the identity", "does not make separated singular channel factors bounded", "remain absent"):
        if token not in ceiling:
            bad.append("ceiling")
    return bad


def exact_checks(data: dict) -> list[tuple[str, bool]]:
    fresh = SOLVER.build()
    theorem = data["parity_matching_theorem"]
    route = data["quantitative_route_consequence"]
    control = data["exact_control"]
    native = data["native_interface_status"]
    return [
        ("fresh theorem", fresh["parity_matching_theorem"] == theorem),
        ("fresh control", fresh["exact_control"] == control),
        ("old identity", theorem["old_matching_condition"].startswith("Alpha=I_6")),
        ("new identity", theorem["new_matching_condition"].endswith("Alpha=I_6")),
        ("spectator extension", "spectator" in theorem["total_parity_extension"]),
        ("plus matching", theorem["plus_coordinate_matching"].count("I_3") == 2),
        ("minus matching", theorem["minus_coordinate_matching"].count("I_3") == 2),
        ("no cross subtraction", theorem["cross_total_parity_subtraction_required"] is False),
        ("mismatch diverges", theorem["each_mismatched_parity_component_has_harmonic_divergent_direction"] is True),
        ("raw unbounded", theorem["parity_change_makes_separate_singular_factors_bounded"] is False),
        ("matched object", theorem["complete_matched_combination_remains_the_valid_object"] is True),
        ("K644 retained", route["K644_raw_row_route_disproved"] is False),
        ("rows not automatic", route["K644_raw_row_route_automatically_available_from_parity"] is False),
        ("new proof needed", route["separate_channel_Hilbert_bounds_require_new_proof"] is True),
        ("cancelled route live", route["cancellation_adapted_complete_parity_form_route_live"] is True),
        ("basis no numbers", route["basis_rotation_alone_supplies_numeric_rows"] is False),
        ("dimension", control["dimension"] == control["transform_rank"] == 6),
        ("orthogonal scale", control["T_T_transpose_equals_2I"] is True),
        ("inverse", control["inverse_is_half_transpose"] is True),
        ("identity invariant", control["identity_matching_is_basis_invariant"] is True),
        ("plus identity", control["parity_plus_block_identity"] is True),
        ("minus identity", control["parity_minus_block_identity"] is True),
        ("cross zero", control["cross_parity_matching_blocks_zero"] is True),
        ("mismatch remains", control["nonidentity_matching_remains_nonidentity"] is True),
        ("witness exists", control["mismatched_divergent_direction_exists"] is True),
        ("three witnesses", len(control["partial_witnesses"]) == 3),
        ("native theorem", native["native_parity_cancellation_matching_proved"] is True),
        ("floors withheld", native["actual_parity_block_floors_identified"] is False),
        ("m withheld", native["native_global_m_identified"] is False),
        ("ledger unchanged", data["source_and_ledger_effect"] == "none"),
    ]


def hostile_checks(data: dict) -> list[tuple[str, bool]]:
    updates = (
        ("break routing", lambda d: d.__setitem__("direction", "native_to_observed")),
        ("lose mismatch", lambda d: d["parity_matching_theorem"].__setitem__("each_mismatched_parity_component_has_harmonic_divergent_direction", False)),
        ("lose matched", lambda d: d["parity_matching_theorem"].__setitem__("complete_matched_combination_remains_the_valid_object", False)),
        ("invent cross subtraction", lambda d: d["parity_matching_theorem"].__setitem__("cross_total_parity_subtraction_required", True)),
        ("invent bounded pieces", lambda d: d["parity_matching_theorem"].__setitem__("parity_change_makes_separate_singular_factors_bounded", True)),
        ("retract K644", lambda d: d["quantitative_route_consequence"].__setitem__("K644_raw_row_route_disproved", True)),
        ("automatic rows", lambda d: d["quantitative_route_consequence"].__setitem__("K644_raw_row_route_automatically_available_from_parity", True)),
        ("no proof", lambda d: d["quantitative_route_consequence"].__setitem__("separate_channel_Hilbert_bounds_require_new_proof", False)),
        ("close route", lambda d: d["quantitative_route_consequence"].__setitem__("cancellation_adapted_complete_parity_form_route_live", False)),
        ("rank loss", lambda d: d["exact_control"].__setitem__("transform_rank", 5)),
        ("break orthogonality", lambda d: d["exact_control"].__setitem__("T_T_transpose_equals_2I", False)),
        ("break inverse", lambda d: d["exact_control"].__setitem__("inverse_is_half_transpose", False)),
        ("break identity", lambda d: d["exact_control"].__setitem__("identity_matching_is_basis_invariant", False)),
        ("break plus", lambda d: d["exact_control"].__setitem__("parity_plus_block_identity", False)),
        ("break minus", lambda d: d["exact_control"].__setitem__("parity_minus_block_identity", False)),
        ("cross block", lambda d: d["exact_control"].__setitem__("cross_parity_matching_blocks_zero", False)),
        ("erase mismatch", lambda d: d["exact_control"].__setitem__("nonidentity_matching_remains_nonidentity", False)),
        ("erase witness", lambda d: d["exact_control"].__setitem__("mismatched_divergent_direction_exists", False)),
        ("erase native", lambda d: d["native_interface_status"].__setitem__("native_parity_cancellation_matching_proved", False)),
        ("invent blocks", lambda d: d["native_interface_status"].__setitem__("separated_singular_channel_bounds_identified", True)),
        ("invent floors", lambda d: d["native_interface_status"].__setitem__("actual_parity_block_floors_identified", True)),
        ("invent tails", lambda d: d["native_interface_status"].__setitem__("actual_uniform_parity_tails_identified", True)),
        ("invent m", lambda d: d["native_interface_status"].__setitem__("native_global_m_identified", True)),
        ("release K473", lambda d: d["native_interface_status"].__setitem__("K473_released", True)),
        ("move ledger", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    )
    caught = []
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught.append((name, bool(failures(mutant))))
    return caught


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    baseline = exact_checks(data)
    manifest_failures = failures(data)
    for name, ok in baseline:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    for failure in manifest_failures:
        print(f"[FAIL] manifest {failure}")
    print(f"K649 EXACT CONTROL: {sum(int(ok) for _, ok in baseline)}/{len(baseline)} pass")
    hostile = hostile_checks(data) if "--selftest" in sys.argv else []
    for name, ok in hostile:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    if hostile:
        print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in hostile)}/{len(hostile)} caught")
    return 0 if all(ok for _, ok in baseline + hostile) and not manifest_failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
