#!/usr/bin/env python3
"""Probe and hostile controls for the K156 common-carrier/count packet."""

from __future__ import annotations

import copy
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k156-common-carrier-regular-core-exterior-count-criterion-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k156-common-carrier-regular-core-exterior-count-criterion-wave-2026-09-08.md"


def load_solver():
    path = Path(__file__).with_name("k156_common_carrier_regular_core.py")
    spec = importlib.util.spec_from_file_location("k156_solver_runtime", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load solver {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SOLVER = load_solver()


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    core = data.get("normal_ordered_regular_core", {})
    tail = data.get("total_action_tail", {})
    count = data.get("exterior_count_criterion", {})
    boundary = data.get("boundaries", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    required_core = (
        "vacuum_contraction_equals_c_N_D",
        "raw_endpoint_counterterm_c_N_D_diverges_logarithmically",
        "endpoint_contraction_cancels_exactly_before_the_limit",
        "K141_common_carrier_applies_to_X_N",
        "normal_ordered_finite_remainder_coefficients_converge_on_cylinder_vectors",
        "normal_ordered_finite_remainder_converges_in_free_graph_relative_norm",
        "one_identified_regular_R_256_limit_exists_on_the_supplied_positive_carrier",
        "finite_and_continuum_signed_flavor_intertwiners_are_compatible",
    )
    for key in required_core:
        if core.get(key) is not True:
            failures.append(f"core:{key}")
    if core.get("raw_V_N_converges_separately") is not False:
        failures.append("core:raw_counterterm_overclaim")
    required_tail = (
        "free_multiplier_error_is_graph_relative",
        "boundary_map_error_is_Hilbert_operator_norm",
        "boundary_map_error_is_also_required_on_the_free_graph",
        "inverse_chart_errors_use_the_resolvent_identity",
        "renormalized_core_error_is_graph_to_Hilbert",
        "propagated_bound_controls_R_N_minus_R_times_the_shifted_free_resolvent",
        "the_bound_includes_both_inverse_chart_sides",
        "the_total_bound_tends_to_zero_from_K139_K141_component_limits",
        "fixed_cylinder_core_action_columns_have_total_Hilbert_tails",
    )
    for key in required_tail:
        if tail.get(key) is not True:
            failures.append(f"tail:{key}")
    if tail.get("raw_point_field_Hilbert_norm_is_used") is not False:
        failures.append("tail:raw_point_norm")
    if count.get("trial_projection_rank") != 1 or count.get("criterion") != "trial_rayleigh < b < complete_exterior_floor":
        failures.append("count:criterion")
    if count.get("criterion_implies_exactly_one_spectral_value_below_b") is not True or count.get("finite_exact_positive_control_passes") is not True:
        failures.append("count:theorem")
    denied_count = (
        "complete_native_charge_sector_exterior_floor_is_serialized",
        "K148_HVZ_essential_edge_is_used_as_the_complete_exterior_floor",
        "finite_regulator_second_eigenvalue_is_used_as_the_native_floor",
        "native_ground_count_is_certified",
        "native_next_distinct_spectrum_lower_bound_is_certified",
    )
    if any(count.get(key) is not False for key in denied_count):
        failures.append("count:native_overclaim")
    if boundary.get("native_regular_operator_identified_at_the_graph_relative_level") is not True or boundary.get("native_regular_action_tail_formula_serialized") is not True:
        failures.append("boundary:missing_regular_result")
    denied = (
        "native_numerical_residual_upper_bound_emitted",
        "native_energy_interval_emitted",
        "complete_native_threshold_or_Gram_margins",
        "native_full_Fock_Mourre_or_scattering",
        "NESS_or_current",
        "physical_parameter_or_state_selection",
        "Weinstein_source_or_GU_action_owner",
        "Born_rule_derived",
        "held_out_scored",
        "prediction_or_confirmation_credit",
    )
    if any(boundary.get(key) is not False for key in denied):
        failures.append("boundary:overclaim")
    if boundary.get("canon_verdict_change") != "none" or boundary.get("paper_release_or_public_posture_change") != "none":
        failures.append("boundary:metadata")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("held_out")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("raw endpoint counterterm", "cancels exactly", "graph-relative R_256", "complete orthogonal", "no native count", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    cancellation = SOLVER.exact_normal_ordered_cancellation(["5/4", "3/2"], [1, 1], (0, 0), 256)
    tail = SOLVER.propagated_regular_action_tail(
        free_graph_error="1/32",
        boundary_hilbert_error="1/64",
        boundary_graph_error="1/48",
        regular_core_graph_error="1/40",
        chart_contraction="3/8",
        graph_chart_contraction="1/2",
        regular_core_graph_bound=3,
    )
    if mutation == "erase_left_tail":
        tail["left_chart_contribution"] = Fraction(0)
    if mutation == "erase_right_tail":
        tail["right_chart_contribution"] = Fraction(0)
    contributions = (
        tail["free_contribution"]
        + tail["left_chart_contribution"]
        + tail["regular_core_contribution"]
        + tail["right_chart_contribution"]
    )
    finite = SOLVER.finite_count_control()
    count = SOLVER.rank_one_exterior_count_certificate(
        trial_rayleigh=0,
        count_threshold=1,
        complete_exterior_floor=2,
        exterior_floor_ref="abstract-positive-control#QHQ-ge-2",
        complete_charge_compression=True,
    )
    artifact = ARTIFACT.read_text(encoding="utf-8")
    return [
        ("exact endpoint cancellation", cancellation["exact_endpoint_cancellation"] is True),
        ("two-mode q00 cancellation block is nonempty", cancellation["dimension"] == 84),
        ("renormalized core retains a finite Pauli/spectator/exchange remainder", any(any(value for value in row) for row in cancellation["finite_remainder"])),
        ("vacuum endpoint contraction is exact", cancellation["vacuum_remainder_diagonal"] == 0),
        ("Hilbert inverse error is positive", tail["hilbert_inverse_error"] > 0),
        ("graph inverse error is positive", tail["graph_inverse_error"] > 0),
        ("left inverse-chart contribution retained", tail["left_chart_contribution"] > 0),
        ("right inverse-chart contribution retained", tail["right_chart_contribution"] > 0),
        ("total tail is the sum of all contributions", contributions == tail["total_graph_relative_action_error"]),
        ("total propagated tail is positive finite", 0 < tail["total_graph_relative_action_error"] < 10),
        ("rank-one criterion returns one", count["spectral_count_below_threshold"] == 1),
        ("rank-one threshold has no kernel", count["threshold_is_not_spectrum"] is True),
        ("exact finite inertia control returns one", finite["spectral_count"] == 1),
        ("exact finite threshold avoids spectrum", finite["threshold_multiplicity"] == 0),
        ("finite control is not native", finite["native_continuum_count"] is False),
        ("artifact names raw divergence", "raw counterterm cannot converge separately" in artifact),
        ("artifact states complete propagated formula", "=: tau_N" in artifact),
        ("artifact proves Schur count", "exactly one negative direction" in artifact),
        ("artifact refuses native count", "complete native exterior" in artifact and "premise is not" in artifact),
        ("artifact preserves holdout boundary", "held-out score" in artifact),
    ]


def input_rejections() -> list[tuple[str, bool]]:
    caught: list[tuple[str, bool]] = []
    cases = (
        ("Hilbert contraction reaches one", dict(
            free_graph_error=0, boundary_hilbert_error=0, boundary_graph_error=0,
            regular_core_graph_error=0, chart_contraction=1,
            graph_chart_contraction="1/2", regular_core_graph_bound=1)),
        ("graph contraction reaches one", dict(
            free_graph_error=0, boundary_hilbert_error=0, boundary_graph_error=0,
            regular_core_graph_error=0, chart_contraction="1/2",
            graph_chart_contraction=1, regular_core_graph_bound=1)),
        ("negative tail", dict(
            free_graph_error="-1", boundary_hilbert_error=0, boundary_graph_error=0,
            regular_core_graph_error=0, chart_contraction="1/2",
            graph_chart_contraction="1/2", regular_core_graph_bound=1)),
    )
    for name, kwargs in cases:
        try:
            SOLVER.propagated_regular_action_tail(**kwargs)
        except SOLVER.CertificateError:
            caught.append((name, True))
        else:
            caught.append((name, False))
    count_cases = (
        ("trial not below threshold", dict(trial_rayleigh=1, count_threshold=1, complete_exterior_floor=2, exterior_floor_ref="x", complete_charge_compression=True)),
        ("threshold not below exterior", dict(trial_rayleigh=0, count_threshold=2, complete_exterior_floor=2, exterior_floor_ref="x", complete_charge_compression=True)),
        ("finite core masquerades as complete", dict(trial_rayleigh=0, count_threshold=1, complete_exterior_floor=2, exterior_floor_ref="x", complete_charge_compression=False)),
        ("missing exterior proof", dict(trial_rayleigh=0, count_threshold=1, complete_exterior_floor=2, exterior_floor_ref="", complete_charge_compression=True)),
    )
    for name, kwargs in count_cases:
        try:
            SOLVER.rank_one_exterior_count_certificate(**kwargs)
        except SOLVER.CertificateError:
            caught.append((name, True))
        else:
            caught.append((name, False))
    return caught


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in ("erase_left_tail", "erase_right_tail")]
    updates = (
        ("erase endpoint cancellation", lambda d: d["normal_ordered_regular_core"].__setitem__("endpoint_contraction_cancels_exactly_before_the_limit", False)),
        ("invent raw V convergence", lambda d: d["normal_ordered_regular_core"].__setitem__("raw_V_N_converges_separately", True)),
        ("erase common carrier", lambda d: d["normal_ordered_regular_core"].__setitem__("K141_common_carrier_applies_to_X_N", False)),
        ("erase graph convergence", lambda d: d["normal_ordered_regular_core"].__setitem__("normal_ordered_finite_remainder_converges_in_free_graph_relative_norm", False)),
        ("erase graph boundary error", lambda d: d["total_action_tail"].__setitem__("boundary_map_error_is_also_required_on_the_free_graph", False)),
        ("erase both chart sides", lambda d: d["total_action_tail"].__setitem__("the_bound_includes_both_inverse_chart_sides", False)),
        ("invent raw point norm", lambda d: d["total_action_tail"].__setitem__("raw_point_field_Hilbert_norm_is_used", True)),
        ("invent native exterior floor", lambda d: d["exterior_count_criterion"].__setitem__("complete_native_charge_sector_exterior_floor_is_serialized", True)),
        ("substitute HVZ", lambda d: d["exterior_count_criterion"].__setitem__("K148_HVZ_essential_edge_is_used_as_the_complete_exterior_floor", True)),
        ("substitute finite gap", lambda d: d["exterior_count_criterion"].__setitem__("finite_regulator_second_eigenvalue_is_used_as_the_native_floor", True)),
        ("invent native count", lambda d: d["exterior_count_criterion"].__setitem__("native_ground_count_is_certified", True)),
        ("invent residual", lambda d: d["boundaries"].__setitem__("native_numerical_residual_upper_bound_emitted", True)),
        ("invent energy", lambda d: d["boundaries"].__setitem__("native_energy_interval_emitted", True)),
        ("invent scattering", lambda d: d["boundaries"].__setitem__("native_full_Fock_Mourre_or_scattering", True)),
        ("invent source owner", lambda d: d["boundaries"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent Born", lambda d: d["boundaries"].__setitem__("Born_rule_derived", True)),
        ("score holdout", lambda d: d["boundaries"].__setitem__("held_out_scored", True)),
        ("promote canon", lambda d: d["boundaries"].__setitem__("canon_verdict_change", "changed")),
        ("erase ceiling", lambda d: d.__setitem__("claim_ceiling", "A unique physical GU Hamiltonian predicts observations.")),
    )
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught.append((name, bool(manifest_failures(mutant))))
    caught.extend(input_rejections())
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
    print(f"K156 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
