#!/usr/bin/env python3
"""Baseline and hostile controls for K158."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k158-generalized-pencil-contour-budget-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k158-generalized-pencil-contour-budget-wave-2026-09-08.md"


def load_solver():
    path = Path(__file__).with_name("k158_generalized_pencil_contour_budget.py")
    spec = importlib.util.spec_from_file_location("k158_solver_runtime", path)
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
    if scope.get("target_claim") != "INTERNAL_TARGET:K156_FREE_OPERATOR_GRAPH_CONTOUR_TRANSFER":
        failures.append("target")
    if scope.get("target_claim_verdict") != "ROUTE_KILLED_AS_FORMULATED":
        failures.append("verdict")
    pencil = data.get("generalized_pencil", {})
    for key in (
        "chart_metric_and_outer_inverse_errors_are_required",
        "exact_rational_finite_identity_passes_in_q00_and_q10",
    ):
        if pencil.get(key) is not True:
            failures.append(f"pencil:{key}")
    for key in ("H_and_R_are_called_isospectral", "regular_action_error_alone_controls_the_singular_resolvent"):
        if pencil.get(key) is not False:
            failures.append(f"pencil:{key}")
    reference = data.get("finite_reference_rectangles", {})
    if reference.get("q00_uniform_resolvent_upper") != "2" or reference.get("q10_uniform_resolvent_upper") != "4":
        failures.append("reference:bounds")
    for key in ("two_mode_reference_is_a_member_of_the_cofinal_K141_family", "cofinal_reference_rank_is_certified"):
        if reference.get(key) is not False:
            failures.append(f"reference:{key}")
    boundary = data.get("boundary_tail", {})
    for key in (
        "K157_cutoff_tail_is_only_the_high_momentum_piece",
        "K141_cell_error_must_also_be_added",
        "complete_Hilbert_d_G_bound_is_available",
        "point_boundary_vector_h_is_L2",
        "every_finite_cutoff_tail_has_infinite_free_operator_graph_norm",
    ):
        if boundary.get(key) is not True:
            failures.append(f"boundary:{key}")
    for key in (
        "omega_h_is_L2",
        "K156_d_GD_is_finite_on_the_free_operator_graph",
        "particle_number_graph_bound_can_substitute_for_free_operator_graph_bound",
    ):
        if boundary.get(key) is not False:
            failures.append(f"boundary:{key}")
    regular = data.get("regular_core_tail", {})
    if regular.get("qualitative_normal_ordered_convergence_survives") is not True:
        failures.append("regular:qualitative")
    for key in (
        "outward_diagonal_Pauli_spectator_constant_is_serialized",
        "outward_four_exchange_constants_are_serialized",
        "uniform_regular_core_graph_bound_B_is_serialized",
        "complete_d_W_is_serialized",
    ):
        if regular.get(key) is not False:
            failures.append(f"regular:{key}")
    count = data.get("count_boundary", {})
    if count.get("perimeter_ten_contour_can_transfer_local_island_rank_when_all_premises_hold") is not True:
        failures.append("count:local")
    for key in (
        "local_island_rank_alone_is_total_rank_below_minus_one",
        "native_no_spectrum_below_minus_five_is_serialized",
        "native_rank_one_count_certified",
        "native_next_distinct_floor_certified",
        "native_energy_interval_emitted",
    ):
        if count.get(key) is not False:
            failures.append(f"count:{key}")
    denied = data.get("boundaries", {})
    for key in (
        "native_ground_count_certified", "native_energy_interval_emitted",
        "threshold_or_Gram_closure", "full_Fock_scattering_or_NESS",
        "physical_or_source_selection", "Born_rule_derived", "held_out_scored",
        "prediction_or_confirmation_credit",
    ):
        if denied.get(key) is not False:
            failures.append(f"denied:{key}")
    if denied.get("canon_verdict_change") != "none" or denied.get("paper_release_or_public_posture_change") != "none":
        failures.append("denied:metadata")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("generalized pencil", "omega h is not L2", "not identified", "below -5", "No native count", "Born"):
        if token not in ceiling:
            failures.append(f"ceiling:{token}")
    return failures


def exact_checks() -> list[tuple[str, bool]]:
    demo = SOLVER.demo()
    q00, q10 = demo["pencil_identities"]
    r00, r10 = demo["reference_rectangles"]
    graph = demo["free_graph_boundary_obstruction"]
    ledger = demo["K157_partial_ledger_n4096"]
    artifact = ARTIFACT.read_text(encoding="utf-8")
    return [
        ("q00 pencil identity", q00["pencil_identity_exact"] is True),
        ("q10 pencil identity", q10["pencil_identity_exact"] is True),
        ("H and R not called isospectral", not q00["H_and_R_called_isospectral"] and not q10["H_and_R_called_isospectral"]),
        ("q00 right guard", r00["right_edge_empty_guard"] == ["-3/2", "-1/2"]),
        ("q10 right guard", r10["right_edge_empty_guard"] == ["-5/4", "-3/4"]),
        ("q00 reference bound", r00["uniform_reference_resolvent_upper"] == "2"),
        ("q10 reference bound", r10["uniform_reference_resolvent_upper"] == "4"),
        ("q00 pencil bounds", r00["reference_pencil_inverse_integer_upper"] == 3 and r00["reference_pencil_graph_integer_upper"] == 552),
        ("q10 pencil bounds", r10["reference_pencil_inverse_integer_upper"] == 5 and r10["reference_pencil_graph_integer_upper"] == 1103),
        ("point vector Hilbert bounded", graph["point_vector_h_is_L2"] is True),
        ("point vector graph divergent", graph["omega_times_h_is_L2"] is False),
        ("finite tails graph divergent", graph["every_finite_cutoff_free_graph_tail_is_infinite"] is True),
        ("particle graph not substituted", graph["particle_number_graph_bound_substitutes_for_free_graph_bound"] is False),
        ("cell error included", ledger["cell_Hilbert_error_sq_upper_per_channel"] == "1/12884901888"),
        ("complete dG emitted", ledger["complete_d_G_upper"] is not None),
        ("dGD infinite", ledger["complete_d_GD_upper"] == "infinite_in_the_free_operator_graph_topology"),
        ("dW stays null", ledger["complete_d_W_upper"] is None),
        ("tau stays null", ledger["complete_tau_upper"] is None),
        ("native contour not attempted", ledger["contour_budget_attempted"] is False),
        ("abstract q00 compiler nonvacuous", demo["abstract_positive_controls"][0]["rank_transfer_certified"] is True),
        ("abstract q10 compiler nonvacuous", demo["abstract_positive_controls"][1]["rank_transfer_certified"] is True),
        ("native count refused", demo["native_count_emitted"] is False),
        ("artifact names generalized pencil", "generalized pencil" in artifact),
        ("artifact proves infinite graph tail", "infinite measure" in artifact and "fails the free-energy graph domain" in artifact),
        ("artifact refuses ground count", "does not rule out native" in artifact and "spectrum below `-5`" in artifact),
    ]


def rejection_checks() -> list[tuple[str, bool]]:
    cases = (
        ("chart bootstrap fails", dict(reference_chart_inverse_upper=2, hilbert_chart_error="1/2", regular_action_error=0, reference_pencil_inverse_upper=2, reference_pencil_graph_upper=10)),
        ("pencil bootstrap fails", dict(reference_chart_inverse_upper=1, hilbert_chart_error="1/100", regular_action_error=1, reference_pencil_inverse_upper=2, reference_pencil_graph_upper=10, require_rank_transfer=True)),
        ("rank gap fails", dict(reference_chart_inverse_upper=1, hilbert_chart_error="1/10", regular_action_error=0, reference_pencil_inverse_upper=100, reference_pencil_graph_upper=1, require_rank_transfer=True)),
    )
    out = []
    for name, kwargs in cases:
        try:
            SOLVER.pencil_resolvent_budget(**kwargs)
        except SOLVER.CertificateError:
            out.append((name, True))
        else:
            out.append((name, False))
    try:
        SOLVER.rectangle_reference_bound((2, 0))
    except SOLVER.CertificateError:
        out.append(("unsupported charge", True))
    else:
        out.append(("unsupported charge", False))
    return out


def selftest(data: dict, baseline: list[tuple[str, bool]] | None = None) -> int:
    baseline = exact_checks() if baseline is None else baseline
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    updates = (
        ("erase pencil metric", lambda d: d["generalized_pencil"].__setitem__("chart_metric_and_outer_inverse_errors_are_required", False)),
        ("invent isospectrality", lambda d: d["generalized_pencil"].__setitem__("H_and_R_are_called_isospectral", True)),
        ("identify arbitrary reference", lambda d: d["finite_reference_rectangles"].__setitem__("two_mode_reference_is_a_member_of_the_cofinal_K141_family", True)),
        ("invent cofinal rank", lambda d: d["finite_reference_rectangles"].__setitem__("cofinal_reference_rank_is_certified", True)),
        ("erase cell error", lambda d: d["boundary_tail"].__setitem__("K141_cell_error_must_also_be_added", False)),
        ("invent graph membership", lambda d: d["boundary_tail"].__setitem__("omega_h_is_L2", True)),
        ("invent finite dGD", lambda d: d["boundary_tail"].__setitem__("K156_d_GD_is_finite_on_the_free_operator_graph", True)),
        ("substitute particle graph", lambda d: d["boundary_tail"].__setitem__("particle_number_graph_bound_can_substitute_for_free_operator_graph_bound", True)),
        ("invent Pauli tail", lambda d: d["regular_core_tail"].__setitem__("outward_diagonal_Pauli_spectator_constant_is_serialized", True)),
        ("invent exchange tails", lambda d: d["regular_core_tail"].__setitem__("outward_four_exchange_constants_are_serialized", True)),
        ("invent B", lambda d: d["regular_core_tail"].__setitem__("uniform_regular_core_graph_bound_B_is_serialized", True)),
        ("invent local-to-total count", lambda d: d["count_boundary"].__setitem__("local_island_rank_alone_is_total_rank_below_minus_one", True)),
        ("invent left floor", lambda d: d["count_boundary"].__setitem__("native_no_spectrum_below_minus_five_is_serialized", True)),
        ("invent native count", lambda d: d["boundaries"].__setitem__("native_ground_count_certified", True)),
        ("invent energy", lambda d: d["boundaries"].__setitem__("native_energy_interval_emitted", True)),
        ("invent source", lambda d: d["boundaries"].__setitem__("physical_or_source_selection", True)),
        ("invent Born", lambda d: d["boundaries"].__setitem__("Born_rule_derived", True)),
        ("score holdout", lambda d: d["boundaries"].__setitem__("held_out_scored", True)),
        ("promote canon", lambda d: d["boundaries"].__setitem__("canon_verdict_change", "changed")),
        ("erase ceiling", lambda d: d.__setitem__("claim_ceiling", "native ground and physical prediction proved")),
    )
    caught = []
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught.append((name, bool(manifest_failures(mutant))))
    caught.extend(rejection_checks())
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
    print(f"K158 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data, checks)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
