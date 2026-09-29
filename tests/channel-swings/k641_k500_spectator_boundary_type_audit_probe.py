#!/usr/bin/env python3
"""Independent baseline and hostile controls for K641."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k641-k500-spectator-boundary-type-audit.json"


def load_solver():
    path = Path(__file__).with_name("k641_k500_spectator_boundary_type_audit.py")
    spec = importlib.util.spec_from_file_location("k641_probe_solver", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


SOLVER = load_solver()


def failures(data: dict) -> list[str]:
    bad: list[str] = []
    replay = data.get("complete_family_replay", {})
    theorem = data.get("native_type_theorem", {})
    reconcile = data.get("K640_reconciliation", {})
    decision = data.get("decision", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        bad.append("routing")
    if replay.get("term_count") != 2958 or replay.get("surviving_monomial_count") != 6:
        bad.append("census")
    if replay.get("orders_covered") != list(range(2, 13)):
        bad.append("orders")
    if replay.get("remaining_variable_arity_by_order") != {str(order): order for order in range(2, 13)}:
        bad.append("arity")
    if replay.get("every_surviving_monomial_occurs_at_every_order") is not True:
        bad.append("all_order_recurrence")
    required_true = (
        "K639_algebraic_rank_six_preserved",
        "K179_output_kernels_retain_spectator_variables",
        "K179_kernel_arity_grows_from_two_through_twelve",
        "K148_native_self_energy_acts_on_full_bath_Fock_space",
        "K159_operator_valued_spectator_denominator_required",
        "constant_6x6_native_identification_rejected_by_current_typing",
        "finite_six_channel_model_remains_valid_as_parameterized_control",
    )
    if any(theorem.get(key) is not True for key in required_true):
        bad.append("theorem_true")
    if theorem.get("K639_separating_functionals_identify_physical_channel_ranges") is not False:
        bad.append("physical_ranges")
    if theorem.get("native_complete_boundary_operator_identified_with_constant_6x6_matrix") is not False:
        bad.append("finite_identification")
    if theorem.get("minimal_corrected_coefficient_space") != "C^6 tensor H_spec":
        bad.append("coefficient_space")
    if reconcile.get("parameterized_scalar_matrix_theorem_retracted") is not False:
        bad.append("K640_retraction")
    if reconcile.get("direct_native_substitution_of_scalar_B_rejected") is not True:
        bad.append("native_substitution")
    if reconcile.get("reference_control_is_native_floor") is not False:
        bad.append("reference_floor")
    if any(reconcile.get(key) is not True for key in ("spectator_amplification_required", "operator_valued_lower_bound_required", "same_domain_remainder_control_required")):
        bad.append("requirements")
    if decision.get("finite_matrix_native_route_closed") is not True or decision.get("operator_valued_graph_route_open") is not True:
        bad.append("decision")
    if data.get("source_and_ledger_effect") != "none":
        bad.append("ledger")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("spectator", "6x6", "K640 remains", "No numerical complete-sector floor"):
        if token not in ceiling:
            bad.append(f"ceiling:{token}")
    return bad


def exact_checks(data: dict) -> list[tuple[str, bool]]:
    fresh = SOLVER.build()
    replay = data["complete_family_replay"]
    theorem = data["native_type_theorem"]
    rows = replay["channel_census"]
    checks = [
        ("fresh replay matches manifest", fresh["complete_family_replay"] == replay),
        ("term count", replay["term_count"] == 2958),
        ("digest", replay["family_sha256"] == "ee24469ef5c6bb8d606efe1d529b294cbc7097b14adc51df80a51627aa7eb686"),
        ("six monomials", len(replay["surviving_operator_monomials"]) == 6),
        ("eleven orders", len(replay["orders_covered"]) == 11),
        ("orders two through twelve", replay["orders_covered"] == list(range(2, 13))),
        ("arity matches order", replay["remaining_variable_arity_by_order"] == {str(n): n for n in range(2, 13)}),
        ("all rows retained", len(rows) == 6),
        ("every row all orders", all(row["orders_present"] == list(range(2, 13)) for row in rows)),
        ("all row totals positive", all(row["total_terms"] > 0 for row in rows)),
        ("kernel formulas nontrivial", all(row["distinct_ordered_kernel_formulas"] > 1 for row in rows)),
        ("no scalar row", all(row["single_scalar_channel_coefficient"] is False for row in rows)),
        ("algebraic rank retained", theorem["K639_algebraic_rank_six_preserved"] is True),
        ("physical range withheld", theorem["K639_separating_functionals_identify_physical_channel_ranges"] is False),
        ("spectator variables retained", theorem["K179_output_kernels_retain_spectator_variables"] is True),
        ("arity growth retained", theorem["K179_kernel_arity_grows_from_two_through_twelve"] is True),
        ("full Fock self energy", theorem["K148_native_self_energy_acts_on_full_bath_Fock_space"] is True),
        ("occupation dependence", theorem["K148_native_self_energy_commutes_with_every_bath_occupation"] is False),
        ("operator Weyl denominator", theorem["K159_operator_valued_spectator_denominator_required"] is True),
        ("finite identification refused", theorem["native_complete_boundary_operator_identified_with_constant_6x6_matrix"] is False),
        ("finite route rejected", theorem["constant_6x6_native_identification_rejected_by_current_typing"] is True),
        ("correct coefficient space", theorem["minimal_corrected_coefficient_space"] == "C^6 tensor H_spec"),
        ("K640 control preserved", theorem["finite_six_channel_model_remains_valid_as_parameterized_control"] is True),
        ("native floor withheld", data["K640_reconciliation"]["reference_control_is_native_floor"] is False),
        ("operator route open", data["decision"]["operator_valued_graph_route_open"] is True),
        ("ledger unchanged", data["source_and_ledger_effect"] == "none"),
    ]
    return checks


def hostile_checks(data: dict) -> list[tuple[str, bool]]:
    updates = (
        ("invent physical ranges", lambda d: d["native_type_theorem"].__setitem__("K639_separating_functionals_identify_physical_channel_ranges", True)),
        ("erase spectator variables", lambda d: d["native_type_theorem"].__setitem__("K179_output_kernels_retain_spectator_variables", False)),
        ("erase arity growth", lambda d: d["native_type_theorem"].__setitem__("K179_kernel_arity_grows_from_two_through_twelve", False)),
        ("collapse Fock self energy", lambda d: d["native_type_theorem"].__setitem__("K148_native_self_energy_acts_on_full_bath_Fock_space", False)),
        ("erase Weyl operator", lambda d: d["native_type_theorem"].__setitem__("K159_operator_valued_spectator_denominator_required", False)),
        ("invent finite identification", lambda d: d["native_type_theorem"].__setitem__("native_complete_boundary_operator_identified_with_constant_6x6_matrix", True)),
        ("erase type rejection", lambda d: d["native_type_theorem"].__setitem__("constant_6x6_native_identification_rejected_by_current_typing", False)),
        ("wrong coefficient space", lambda d: d["native_type_theorem"].__setitem__("minimal_corrected_coefficient_space", "C^6")),
        ("retract K640", lambda d: d["K640_reconciliation"].__setitem__("parameterized_scalar_matrix_theorem_retracted", True)),
        ("allow native substitution", lambda d: d["K640_reconciliation"].__setitem__("direct_native_substitution_of_scalar_B_rejected", False)),
        ("erase amplification", lambda d: d["K640_reconciliation"].__setitem__("spectator_amplification_required", False)),
        ("erase operator bound", lambda d: d["K640_reconciliation"].__setitem__("operator_valued_lower_bound_required", False)),
        ("erase remainder", lambda d: d["K640_reconciliation"].__setitem__("same_domain_remainder_control_required", False)),
        ("open finite route", lambda d: d["decision"].__setitem__("finite_matrix_native_route_closed", False)),
        ("close operator route", lambda d: d["decision"].__setitem__("operator_valued_graph_route_open", False)),
        ("move ledger", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
        ("wrong term count", lambda d: d["complete_family_replay"].__setitem__("term_count", 2957)),
        ("wrong monomial count", lambda d: d["complete_family_replay"].__setitem__("surviving_monomial_count", 16)),
        ("truncate orders", lambda d: d["complete_family_replay"].__setitem__("orders_covered", list(range(2, 12)))),
        ("flatten arity", lambda d: d["complete_family_replay"].__setitem__("remaining_variable_arity_by_order", {str(n): 1 for n in range(2, 13)})),
        ("erase all-order recurrence", lambda d: d["complete_family_replay"].__setitem__("every_surviving_monomial_occurs_at_every_order", False)),
        ("invent native floor", lambda d: d["K640_reconciliation"].__setitem__("reference_control_is_native_floor", True)),
        ("erase ceiling", lambda d: d.__setitem__("claim_ceiling", "native floor proved")),
    )
    caught = []
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught.append((name, bool(failures(mutant))))
    return caught


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    baseline = exact_checks(data)
    manifest_failures = failures(data)
    for name, ok in baseline:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    for failure in manifest_failures:
        print(f"[FAIL] manifest {failure}")
    print(f"K641 EXACT CONTROL: {sum(int(ok) for _, ok in baseline)}/{len(baseline)} pass")
    if "--selftest" in sys.argv:
        hostile = hostile_checks(data)
        for name, ok in hostile:
            print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
        print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in hostile)}/{len(hostile)} caught")
        return 0 if all(ok for _, ok in baseline + hostile) and not manifest_failures else 1
    return 0 if all(ok for _, ok in baseline) and not manifest_failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
