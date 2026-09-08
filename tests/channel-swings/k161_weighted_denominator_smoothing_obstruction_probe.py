#!/usr/bin/env python3
"""Baseline-first exact and hostile controls for K161."""

from __future__ import annotations

import copy
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k161-weighted-denominator-smoothing-obstruction-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k161-weighted-denominator-smoothing-obstruction-wave-2026-09-08.md"


def load_solver():
    path = Path(__file__).with_name("k161_weighted_denominator_smoothing_obstruction.py")
    spec = importlib.util.spec_from_file_location("k161_solver_runtime", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SOLVER = load_solver()


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    scope = data.get("scope", {})
    if scope.get("target_claim") != "INTERNAL_TARGET:K160_WEIGHTED_BOUNDARY_INVERSE_SMOOTHING":
        failures.append("target")
    if scope.get("target_claim_verdict") != "COMPLETE_WEIGHTED_ERROR_CLOSES__INVERSE_SMOOTHING_ROUTE_KILLED__REGULAR_K152_ROUTE_SELECTED":
        failures.append("verdict")
    if scope.get("source_claim_ids") != [] or scope.get("physics_row_changes") != []:
        failures.append("source_or_ledger_promotion")

    weighted = data.get("complete_weighted_denominator", {})
    required_weighted = (
        "two_active_edges", "unit_equal_couplings",
        "matrix_unit_contractions_norm_at_most_one",
        "diagonal_spectator_tail_included", "diagonal_Pauli_occupation_tail_included",
        "exchange_pp_included", "exchange_pm_included", "exchange_mp_included", "exchange_mm_included",
        "complete_K157_rectangle_covered", "complete_native_weighted_denominator_error_serialized",
    )
    if weighted.get("weight") != "(1+S)^(-1)" or any(weighted.get(k) is not True for k in required_weighted):
        failures.append("weighted_components")
    if weighted.get("n4096_outward_upper") != "79277/319488" or weighted.get("rate") != "O(Lambda^(-1/2))":
        failures.append("weighted_exact")

    smoothing = data.get("inverse_smoothing_discriminator", {})
    required_smoothing = (
        "active_edge_vacuum_high_spectator_sequence_exists",
        "exchange_blocks_vanish_on_test_sequence",
        "finite_extension_contributes_only_a_bounded_term",
    )
    denied_smoothing = (
        "reference_inverse_smoothing_finite", "weighted_Neumann_parameter_finite",
        "low_energy_separation_test_needed_for_weighted_route", "weighted_boundary_route_closed",
        "singular_boundary_operator_killed",
    )
    if any(smoothing.get(k) is not True for k in required_smoothing):
        failures.append("smoothing_premises")
    if any(smoothing.get(k) is not False for k in denied_smoothing):
        failures.append("smoothing_ceiling")
    if smoothing.get("denominator_growth_on_test_sequence") != "O(log(1+S))":
        failures.append("smoothing_growth")

    regular = data.get("regular_K152_switch", {})
    if regular.get("selected") is not True:
        failures.append("regular_switch")
    for key in ("regular_core_bound_B_serialized", "total_form_dual_residual_serialized", "coercivity_serialized", "next_distinct_spectrum_serialized", "native_left_floor_serialized", "signed_charge_intertwiner_complete", "native_K152_interval_emitted"):
        if regular.get(key) is not False:
            failures.append(f"regular:{key}")
    if regular.get("free_H0_graph_chart_required") is not False or regular.get("boundary_inverse_smoothing_required") is not False:
        failures.append("regular_wrong_topology")

    count = data.get("count_boundary", {})
    if any(count.get(k) is not False for k in count):
        failures.append("count")
    denied = data.get("boundaries", {})
    if any(denied.get(k) is not False for k in ("threshold_or_Gram_closure", "full_Fock_scattering_or_NESS", "physical_or_source_selection", "Born_rule_derived", "held_out_scored", "prediction_or_confirmation_credit")):
        failures.append("denied")
    if denied.get("canon_verdict_change") != "none" or denied.get("paper_release_or_public_posture_change") != "none":
        failures.append("denied_metadata")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("all five", "O(Lambda^-1/2)", "infinite", "kills the weighted Neumann", "not the singular extension", "regular K152", "No native count", "Born"):
        if token not in ceiling:
            failures.append(f"ceiling:{token}")
    return failures


def exact_checks() -> list[tuple[str, bool]]:
    status = SOLVER.native_route_status()
    n4 = status["complete_weighted_tail_n4096"]
    n16 = status["complete_weighted_tail_n65536"]
    witnesses = status["inverse_smoothing_witnesses"]
    artifact = ARTIFACT.read_text(encoding="utf-8")

    complete_regular = SOLVER.regular_k152_admission(
        diagonal_tail_ref="d", exchange_pp_ref="pp", exchange_pm_ref="pm",
        exchange_mp_ref="mp", exchange_mm_ref="mm", regular_core_bound_ref="B",
        form_dual_residual_ref="r", coercivity_ref="c", next_spectrum_ref="g",
        native_left_floor_ref="f", signed_charge_intertwiner_ref="u",
    )
    rejected = []
    for kwargs in (
        dict(spectator_energy=255, logarithmic_power=7),
        dict(spectator_energy=255, logarithmic_power=8, c1=0),
    ):
        try:
            SOLVER.inverse_smoothing_obstruction(**kwargs)
        except SOLVER.CertificateError:
            rejected.append(True)
        else:
            rejected.append(False)

    lower = [Fraction(row["inverse_smoothing_norm_lower"]) for row in witnesses]
    return [
        ("one-energy weight retained", n4["weight"] == "(1+S)^(-1)"),
        ("point graph-dual tail exact", n4["point_graph_dual_tail_square_upper"] == "1/12288"),
        ("dressed creation tail exact", n4["dressed_creation_tail_square_upper"] == "1/12288"),
        ("two-edge diagonal exact", n4["matched_two_edge_diagonal_upper"] == "1049/24576"),
        ("Pauli occupation exact", n4["Pauli_occupation_tail_upper"] == "1/3072"),
        ("diagonal total exact", n4["diagonal_Pauli_spectator_total_upper"] == "1057/24576"),
        ("four edge pairs", n4["ordered_edge_pairs"] == 4),
        ("four polarity blocks", n4["polarity_blocks"] == ["++", "+-", "-+", "--"]),
        ("exchange rational outward", Fraction(n4["exchange_pair_upper"]) ** 2 >= Fraction(n4["exchange_pair_square_target"])),
        ("n4096 exchange upper", n4["all_exchange_blocks_upper"] == "8/39"),
        ("n4096 complete upper", n4["complete_weighted_denominator_error_upper"] == "79277/319488"),
        ("n65536 complete upper", n16["complete_weighted_denominator_error_upper"] == "6622297/123076608"),
        ("complete bound decreases", Fraction(n16["complete_weighted_denominator_error_upper"]) < Fraction(n4["complete_weighted_denominator_error_upper"])),
        ("all five components included", n4["all_five_normal_ordered_components_included"] is True),
        ("complete contour covered", n4["complete_K157_rectangle_covered"] is True),
        ("weighted tail converges", n4["converges_to_zero"] is True),
        ("spectator witness energies exact", [row["spectator_energy"] for row in witnesses] == [255, 65535, 4294967295]),
        ("logarithmic denominators exact", [row["denominator_vector_norm_upper"] for row in witnesses] == ["9", "17", "33"]),
        ("smoothing lower bounds exact", [row["inverse_smoothing_norm_lower"] for row in witnesses] == ["256/9", "65536/17", "4294967296/33"]),
        ("smoothing lower bounds grow", lower[0] < lower[1] < lower[2]),
        ("exchange vanishes on witness", all(row["active_edge_vacuum_exchange_blocks_vanish"] for row in witnesses)),
        ("inverse smoothing refused", all(row["full_energy_inverse_smoothing_finite"] is False for row in witnesses)),
        ("weighted route killed", status["weighted_route_verdict"] == "INVERSE_SMOOTHING_ROUTE_KILLED"),
        ("singular extension preserved", status["singular_boundary_extension_killed"] is False),
        ("regular switch selected", status["regular_K152_route_selected"] is True),
        ("native regular packet rejected", "regular core bound B" in status["regular_K152_native_admission_error"]),
        ("abstract complete regular packet accepted", complete_regular["regular_K152_interface_complete"] is True),
        ("regular path drops graph chart", complete_regular["free_H0_graph_chart_required"] is False),
        ("regular path drops inverse smoothing", complete_regular["boundary_inverse_smoothing_required"] is False),
        ("bad witness inputs rejected", all(rejected)),
        ("native count refused", status["native_ground_count_emitted"] is False),
        ("native interval refused", status["native_energy_interval_emitted"] is False),
        ("artifact states logarithmic obstruction", "(1+s)/(C0+C1 log(1+s))" in artifact),
        ("artifact keeps topology scope", "does not kill the singular boundary operator" in artifact),
        ("artifact routes regular branch", "regular-representative/K152" in artifact),
        ("artifact refuses source promotion", "SC-META-53" in artifact and "LT-SM8" in artifact and "Born" in artifact),
    ]


def selftest(data: dict, baseline: list[tuple[str, bool]]) -> int:
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    updates = (
        ("erase diagonal spectator", lambda d: d["complete_weighted_denominator"].__setitem__("diagonal_spectator_tail_included", False)),
        ("erase Pauli tail", lambda d: d["complete_weighted_denominator"].__setitem__("diagonal_Pauli_occupation_tail_included", False)),
        ("erase exchange pp", lambda d: d["complete_weighted_denominator"].__setitem__("exchange_pp_included", False)),
        ("erase exchange pm", lambda d: d["complete_weighted_denominator"].__setitem__("exchange_pm_included", False)),
        ("erase exchange mp", lambda d: d["complete_weighted_denominator"].__setitem__("exchange_mp_included", False)),
        ("erase exchange mm", lambda d: d["complete_weighted_denominator"].__setitem__("exchange_mm_included", False)),
        ("wrong exact bound", lambda d: d["complete_weighted_denominator"].__setitem__("n4096_outward_upper", "1/100")),
        ("invent faster rate", lambda d: d["complete_weighted_denominator"].__setitem__("rate", "O(Lambda^-1)")),
        ("erase high spectator", lambda d: d["inverse_smoothing_discriminator"].__setitem__("active_edge_vacuum_high_spectator_sequence_exists", False)),
        ("invent exchange action", lambda d: d["inverse_smoothing_discriminator"].__setitem__("exchange_blocks_vanish_on_test_sequence", False)),
        ("invent smoothing", lambda d: d["inverse_smoothing_discriminator"].__setitem__("reference_inverse_smoothing_finite", True)),
        ("invent Neumann parameter", lambda d: d["inverse_smoothing_discriminator"].__setitem__("weighted_Neumann_parameter_finite", True)),
        ("keep weighted route", lambda d: d["inverse_smoothing_discriminator"].__setitem__("weighted_boundary_route_closed", True)),
        ("kill singular operator", lambda d: d["inverse_smoothing_discriminator"].__setitem__("singular_boundary_operator_killed", True)),
        ("skip regular switch", lambda d: d["regular_K152_switch"].__setitem__("selected", False)),
        ("invent B", lambda d: d["regular_K152_switch"].__setitem__("regular_core_bound_B_serialized", True)),
        ("invent residual", lambda d: d["regular_K152_switch"].__setitem__("total_form_dual_residual_serialized", True)),
        ("invent coercivity", lambda d: d["regular_K152_switch"].__setitem__("coercivity_serialized", True)),
        ("invent next spectrum", lambda d: d["regular_K152_switch"].__setitem__("next_distinct_spectrum_serialized", True)),
        ("invent left floor", lambda d: d["regular_K152_switch"].__setitem__("native_left_floor_serialized", True)),
        ("invent charge", lambda d: d["regular_K152_switch"].__setitem__("signed_charge_intertwiner_complete", True)),
        ("restore killed graph", lambda d: d["regular_K152_switch"].__setitem__("free_H0_graph_chart_required", True)),
        ("restore killed smoothing", lambda d: d["regular_K152_switch"].__setitem__("boundary_inverse_smoothing_required", True)),
        ("invent interval", lambda d: d["regular_K152_switch"].__setitem__("native_K152_interval_emitted", True)),
        ("invent count", lambda d: d["count_boundary"].__setitem__("native_ground_count_certified", True)),
        ("invent physical selection", lambda d: d["boundaries"].__setitem__("physical_or_source_selection", True)),
        ("invent Born", lambda d: d["boundaries"].__setitem__("Born_rule_derived", True)),
        ("score holdout", lambda d: d["boundaries"].__setitem__("held_out_scored", True)),
        ("promote canon", lambda d: d["boundaries"].__setitem__("canon_verdict_change", "changed")),
        ("invent source claim", lambda d: d["scope"].__setitem__("source_claim_ids", ["SC-META-53"])),
        ("move ledger row", lambda d: d["scope"].__setitem__("physics_row_changes", ["LT-SM8"])),
        ("erase ceiling", lambda d: d.__setitem__("claim_ceiling", "A physical GU Hamiltonian derives Born predictions.")),
    )
    caught = []
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught.append((name, bool(manifest_failures(mutant))))
    for name, ok in caught:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in caught)}/{len(caught)} caught")
    return 0 if all(ok for _, ok in caught) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    checks = exact_checks()
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    failures = manifest_failures(data)
    for failure in failures:
        print(f"[FAIL] manifest {failure}")
    print(f"K161 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data, checks)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
