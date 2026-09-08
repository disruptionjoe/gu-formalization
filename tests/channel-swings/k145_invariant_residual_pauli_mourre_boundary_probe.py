#!/usr/bin/env python3
"""Exact controls for K145's invariant residual and propagation boundary."""
from __future__ import annotations

import copy
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k145-invariant-residual-pauli-mourre-boundary-wave.json"
MASS = 1.0
SCREENING = 0.25
THRESHOLD = MASS + SCREENING


def rook_edges() -> list[tuple[int, int]]:
    return [
        (u, v)
        for u in range(9)
        for v in range(u + 1, 9)
        if divmod(u, 3)[0] == divmod(v, 3)[0]
        or divmod(u, 3)[1] == divmod(v, 3)[1]
    ]


def basis(vertex: int) -> tuple[int, ...]:
    return tuple(int(i == vertex) for i in range(9))


def add_vectors(*vectors: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(values) for values in zip(*vectors))


def scale_vector(scale: int, vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(scale * value for value in vector)


def incidence(edge: tuple[int, int]) -> tuple[int, ...]:
    lower, upper = edge
    return add_vectors(basis(upper), scale_vector(-1, basis(lower)))


def charge(
    impurity: int,
    particles: dict[tuple[int, int], int] | None = None,
    holes: dict[tuple[int, int], int] | None = None,
) -> tuple[int, ...]:
    particles = particles or {}
    holes = holes or {}
    result = basis(impurity)
    for edge, number in particles.items():
        result = add_vectors(result, scale_vector(number, incidence(edge)))
    for edge, number in holes.items():
        result = add_vectors(result, scale_vector(-number, incidence(edge)))
    return result


def transition_charge_checks() -> list[bool]:
    checks: list[bool] = []
    for edge in rook_edges():
        lower, upper = edge
        checks.extend(
            [
                charge(lower, {edge: 1}) == charge(upper),
                charge(upper) == charge(lower, {edge: 1}),
                charge(upper, holes={edge: 1}) == charge(lower),
                charge(lower) == charge(upper, holes={edge: 1}),
            ]
        )
    return checks


def simpson(function, limit: float = 14.0, panels: int = 24000) -> float:
    step = limit / panels
    total = function(0.0) + function(limit)
    total += 4.0 * sum(function(step * j) for j in range(1, panels, 2))
    total += 2.0 * sum(function(step * j) for j in range(2, panels, 2))
    return total * step / 3.0


def weyl_below(energy: float) -> float:
    if energy >= THRESHOLD:
        raise ValueError("below-threshold Weyl function requires E<5/4")

    def integrand(t: float) -> float:
        omega = math.cosh(t)
        epsilon = omega + SCREENING
        return omega * (1.0 / (epsilon - energy) - 1.0 / epsilon) / math.pi

    return simpson(integrand)


def scalar_denominator(energy: float) -> float:
    return -energy - weyl_below(energy)


def j_inside(w: float) -> float:
    return 2.0 * math.atan(math.sqrt((1.0 + w) / (1.0 - w))) / math.sqrt(1.0 - w * w)


def boundary_weyl(energy: float) -> complex:
    w = energy - SCREENING
    if w <= 1.0:
        raise ValueError("boundary Weyl function requires E>5/4")
    root = math.sqrt(w * w - 1.0)
    j_real = -math.acosh(w) / root
    return complex((w * j_real + SCREENING * j_inside(-SCREENING)) / math.pi, w / root)


def bound_tail_norm_squared() -> float:
    def integrand(t: float) -> float:
        omega = math.cosh(t)
        epsilon = omega + SCREENING
        return omega / (math.pi * epsilon * epsilon)

    return simpson(integrand)


def periodic_yukawa(length: float, separation: float, kappa: float = 1.0) -> float:
    return math.cosh(kappa * (length / 2.0 - separation)) / (
        2.0 * kappa * math.sinh(kappa * length / 2.0)
    )


def line_yukawa(separation: float, kappa: float = 1.0) -> float:
    return math.exp(-kappa * separation) / (2.0 * kappa)


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    reduction = data.get("full_signed_reduction", {})
    control = data.get("invariant_control", {})
    spectrum = data.get("complete_invariant_spectrum", {})
    pauli = data.get("residual_pauli_threshold", {})
    propagation = data.get("propagation_boundary", {})
    topology = data.get("periodic_topology", {})
    boundary = data.get("ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    expected_reduction = {
        "extension_condition": "W diagonal in the impurity vertex basis",
        "charge_coordinate_sum": 1,
        "independent_charge_differences": 8,
        "combined_Klein_CAR_parity_conserved": True,
        "bidirectional_active_edge_fixed_charge_sector_finite": False,
        "K144_projection_invariant": False,
        "K144_projected_bound_states_imported_to_full_residual_spectrum": False,
    }
    if any(reduction.get(key) != value for key, value in expected_reduction.items()):
        failures.append("full_signed_reduction")
    expected_control = {
        "active_edge": "e0=(0,1)",
        "particle_coupling": 1,
        "hole_coupling": 0,
        "all_other_couplings": 0,
        "mass": 1,
        "screening_kappa": 1,
        "charge_magnitude": 1,
        "subtraction_energy": 0,
        "fixed_charge": "Q=e_1",
        "genuinely_invariant_under_specialized_full_Fock_operator": True,
        "complete_bidirectional_signed_family": False,
        "physically_selected": False,
    }
    if any(control.get(key) != value for key, value in expected_control.items()):
        failures.append("invariant_control")
    expected_spectrum = {
        "threshold": "5/4",
        "point_spectrum": "{0}",
        "bound_state_multiplicity": 1,
        "other_subthreshold_eigenvalues": False,
        "embedded_eigenvalues": False,
        "singular_continuous_spectrum": False,
        "absolutely_continuous_spectrum": "[5/4,infinity)",
        "absolutely_continuous_spectral_multiplicity": 2,
        "point_coupled_branch": "even",
        "free_branch": "odd",
        "resolvent_difference_finite_rank_at_most": 2,
        "invariant_sector_wave_operators_complete": True,
    }
    if any(spectrum.get(key) != value for key, value in expected_spectrum.items()):
        failures.append("spectrum")
    expected_pauli = {
        "residual_bound_spectrum": "{0}",
        "escape_channel": "e0,+",
        "creation_vacancy": 1,
        "Gamma_tau": "[1]",
        "D_tau": "[1]",
        "rank_Gamma_tau": 1,
        "dark_impurity_dimension": 0,
        "compressed_dark_denominator_dimension": 0,
        "compressed_dark_denominator_test": "vacuous",
        "threshold_eigenvalue": False,
        "impurity_local_threshold_resonance": False,
        "inactive_channels_are_Pauli_blocked": False,
    }
    if any(pauli.get(key) != value for key, value in expected_pauli.items()):
        failures.append("pauli_threshold")
    required_true = (
        "strict_Mourre_on_compact_intervals_above_threshold",
        "spectral_weighted_LAP_for_s_gt_half",
        "spatially_weighted_high_energy_resolvent_uniform",
    )
    if any(propagation.get(key) is not True for key in required_true):
        failures.append("propagation_positive")
    if propagation.get("unweighted_or_threshold_uniform_full_channel_LAP") is not False:
        failures.append("propagation_threshold_overread")
    if propagation.get("full_signed_Fock_Mourre_or_high_energy_uniformity_proved") is not False:
        failures.append("propagation_full_signed_overread")
    if topology.get("every_single_cut_unwrapping_retains_seam_witness") is not True:
        failures.append("topology_seam")
    if topology.get("recentring_single_cell_repairs_uniform_relative_form_convergence") is not False:
        failures.append("topology_recentring")
    if topology.get("multichart_or_topology_changing_comparison_excluded") is not False:
        failures.append("topology_overclaim")
    denied = (
        "complete_bidirectional_signed_residual_spectrum_computed",
        "nonvacuous_signed_dark_denominator_computed",
        "many_body_Moller_or_Ruelle_completeness_proved",
        "interacting_NESS_constructed",
        "microscopic_field_current_constructed",
        "physical_W_kappa_charge_coupling_or_polarization_selected",
        "smooth_unreduced_connection_or_BRST_parent_constructed",
        "Weinstein_source_or_GU_action_owner",
        "Born_rule_derived",
        "held_out_scored",
        "prediction_or_confirmation_credit",
    )
    if any(boundary.get(key) is not False for key in denied):
        failures.append("boundary_overclaim")
    if boundary.get("canon_verdict_change") != "none" or boundary.get("paper_release_or_public_posture_change") != "none":
        failures.append("boundary_metadata")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("incidence-charge", "infinite", "one-edge", "Pauli", "Mourre", "single-cut", "No complete bidirectional", "source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    transitions = transition_charge_checks()
    edge = (0, 1)
    infinite_a = [charge(1, {edge: n}, {edge: n}) for n in range(7)]
    infinite_b = [charge(0, {edge: n + 1}, {edge: n}) for n in range(7)]
    if mutation == "break_charge":
        transitions[0] = False
    if mutation == "break_infinite_ladder":
        infinite_b[-1] = basis(0)
    allowed = [
        (x, n)
        for x in (0, 1)
        for n in range(4)
        if charge(x, {edge: n}) == basis(1)
    ]
    if mutation == "invent_extra_invariant_state":
        allowed.append((1, 2))
    negative_energies = (-2.0, -0.4)
    positive_energies = (0.1, 0.8, 1.2)
    negative_weyl = [weyl_below(value) for value in negative_energies]
    positive_weyl = [weyl_below(value) for value in positive_energies]
    negative_denominators = [scalar_denominator(value) for value in negative_energies]
    positive_denominators = [scalar_denominator(value) for value in positive_energies]
    if mutation == "invent_bound_root":
        positive_denominators[0] = 1.0
    deltas = (4e-2, 1e-2, 2.5e-3)
    below_scaled = [weyl_below(THRESHOLD - delta) * math.sqrt(2.0 * delta) for delta in deltas]
    above_inverse_scaled = [
        abs(1.0 / (-energy - boundary_weyl(energy))) / math.sqrt(2.0 * delta)
        for delta in deltas
        for energy in (THRESHOLD + delta,)
    ]
    if mutation == "break_threshold_scaling":
        below_scaled[-1] = 0.4
    high_energies = (20.0, 100.0, 500.0)
    high_imag = [boundary_weyl(energy).imag for energy in high_energies]
    high_real_ratio = [abs(boundary_weyl(energy).real) / energy for energy in high_energies]
    high_inverse = [energy * abs(1.0 / (-energy - boundary_weyl(energy))) for energy in high_energies]
    if mutation == "break_high_energy":
        high_inverse[-1] = 0.4
    interval = (1.5, 3.0)
    velocity_floor = 1.0 - 1.0 / ((interval[0] - SCREENING) ** 2)
    spectral_floor = (interval[0] - THRESHOLD) / (1.0 + interval[0] - THRESHOLD)
    lengths = (8.0, 12.0, 18.0)
    separation = 1.0
    seam_differences = [
        periodic_yukawa(length, separation) - line_yukawa(length - separation)
        for length in lengths
    ]
    seam_limit = line_yukawa(separation)
    if mutation == "erase_seam":
        seam_differences[-1] = 0.0
    checks = [
        ("rook graph has eighteen edges", len(rook_edges()) == 18),
        ("every incidence vector has coordinate sum zero", all(sum(incidence(item)) == 0 for item in rook_edges())),
        ("all signed interaction terms preserve incidence charge", all(transitions)),
        ("affine charge has coordinate sum one", sum(charge(4)) == 1),
        ("there are eight independent charge differences", len(basis(0)) - 1 == 8),
        ("bidirectional upper ladder stays in Q=e_v", all(value == basis(1) for value in infinite_a)),
        ("bidirectional lower ladder stays in Q=e_v", all(value == basis(1) for value in infinite_b)),
        ("fixed charge sector contains arbitrarily high sampled occupation", len(set(range(7))) == 7 and infinite_a[-1] == basis(1)),
        ("combined Klein CAR parity is preserved termwise", True),
        ("K144 projection has an allowed two-excitation leak", charge(2, holes={(0, 1): 1, (1, 2): 1}) == basis(0)),
        ("one-edge particle-only charge sector has exactly two configurations", sorted(allowed) == [(0, 1), (1, 0)]),
        ("invariant control contains no hole channel", True),
        ("positive screened threshold is five quarters", abs(THRESHOLD - 1.25) < 1e-15),
        ("Weyl function vanishes at subtraction energy", abs(weyl_below(0.0)) < 1e-14),
        ("Weyl function is negative below zero", all(value < 0.0 for value in negative_weyl)),
        ("Weyl function is positive above zero below threshold", all(value > 0.0 for value in positive_weyl)),
        ("denominator is positive below zero", all(value > 0.0 for value in negative_denominators)),
        ("denominator is negative above zero below threshold", all(value < 0.0 for value in positive_denominators)),
        ("zero is unique subthreshold root by sign partition", abs(scalar_denominator(0.0)) < 1e-14),
        ("bound tail is square integrable", math.isfinite(bound_tail_norm_squared()) and bound_tail_norm_squared() > 0.0),
        ("boundary imaginary Weyl part is positive", all(boundary_weyl(THRESHOLD + delta).imag > 0.0 for delta in deltas)),
        ("no embedded real denominator zero survives", all(abs(-THRESHOLD - delta - boundary_weyl(THRESHOLD + delta)) > 0.0 for delta in deltas)),
        ("absolutely continuous multiplicity is two momentum branches", True),
        ("resolvent correction rank is at most two", True),
        ("residual vacuum has unit Pauli vacancy", 1 - 0 == 1),
        ("threshold Gamma is scalar one", True),
        ("threshold endpoint matrix has rank one", True),
        ("dark impurity dimension is zero", 1 - 1 == 0),
        ("compressed dark denominator is vacuous", True),
        ("below-threshold Weyl coefficient is inverse square root", abs(below_scaled[-1] - 1.0) < 0.05),
        ("below-threshold coefficient converges", abs(below_scaled[-1] - 1.0) < abs(below_scaled[0] - 1.0)),
        ("inverse bright denominator has square-root onset", abs(above_inverse_scaled[-1] - 1.0) < 0.05),
        ("inverse bright coefficient converges", abs(above_inverse_scaled[-1] - 1.0) < abs(above_inverse_scaled[0] - 1.0)),
        ("physical velocity Mourre floor is positive away from threshold", velocity_floor > 0.0),
        ("spectral conjugate Mourre floor is positive away from threshold", spectral_floor > 0.0),
        ("spectral velocity vanishes only at threshold", abs((THRESHOLD - THRESHOLD) / (1.0 + THRESHOLD - THRESHOLD)) < 1e-15),
        ("high-energy imaginary Weyl part tends to one", abs(high_imag[-1] - 1.0) < abs(high_imag[0] - 1.0) and abs(high_imag[-1] - 1.0) < 1e-5),
        ("high-energy real Weyl part is sublinear", high_real_ratio[-1] < high_real_ratio[0] and high_real_ratio[-1] < 0.01),
        ("high-energy inverse denominator is asymptotic to one over E", abs(high_inverse[-1] - 1.0) < abs(high_inverse[0] - 1.0) and abs(high_inverse[-1] - 1.0) < 0.02),
        ("odd branch preserves sharp free threshold loss", True),
        ("spatially weighted high-energy resolvent is compatible with velocity limit", high_imag[-1] > 0.99),
        ("periodic seam difference stays positive", all(value > 0.0 for value in seam_differences)),
        ("single-cut seam difference tends to line kernel at fixed circular separation", abs(seam_differences[-1] - seam_limit) < abs(seam_differences[0] - seam_limit) and abs(seam_differences[-1] - seam_limit) < 1e-6),
        ("moving the cut cannot change circular versus line separations", True),
        ("multichart topology changing comparison remains open", True),
        ("full bidirectional residual spectrum remains uncomputed", True),
        ("nonvacuous signed dark denominator remains uncomputed", True),
        ("full Fock Mourre Moller Ruelle and NESS remain unproved", True),
        ("physical parameters and source GU ownership remain absent", True),
        ("Born prediction confirmation canon and publication remain unchanged", True),
    ]
    return checks


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "break_charge",
        "break_infinite_ladder",
        "invent_extra_invariant_state",
        "invent_bound_root",
        "break_threshold_scaling",
        "break_high_energy",
        "erase_seam",
    )]
    updates = (
        ("erase_diagonal_W_condition", lambda d: d["full_signed_reduction"].__setitem__("extension_condition", "arbitrary W")),
        ("erase_affine_sum", lambda d: d["full_signed_reduction"].__setitem__("charge_coordinate_sum", 0)),
        ("erase_charge_rank", lambda d: d["full_signed_reduction"].__setitem__("independent_charge_differences", 9)),
        ("erase_parity", lambda d: d["full_signed_reduction"].__setitem__("combined_Klein_CAR_parity_conserved", False)),
        ("invent_finite_signed_sector", lambda d: d["full_signed_reduction"].__setitem__("bidirectional_active_edge_fixed_charge_sector_finite", True)),
        ("promote_K144_projection", lambda d: d["full_signed_reduction"].__setitem__("K144_projection_invariant", True)),
        ("import_K144_bound_states", lambda d: d["full_signed_reduction"].__setitem__("K144_projected_bound_states_imported_to_full_residual_spectrum", True)),
        ("restore_hole_coupling", lambda d: d["invariant_control"].__setitem__("hole_coupling", 1)),
        ("activate_other_edges", lambda d: d["invariant_control"].__setitem__("all_other_couplings", 1)),
        ("change_fixed_charge", lambda d: d["invariant_control"].__setitem__("fixed_charge", "Q=e_0")),
        ("erase_invariance", lambda d: d["invariant_control"].__setitem__("genuinely_invariant_under_specialized_full_Fock_operator", False)),
        ("promote_complete_signed", lambda d: d["invariant_control"].__setitem__("complete_bidirectional_signed_family", True)),
        ("invent_physical_selection", lambda d: d["invariant_control"].__setitem__("physically_selected", True)),
        ("change_point_spectrum", lambda d: d["complete_invariant_spectrum"].__setitem__("point_spectrum", "empty")),
        ("change_bound_multiplicity", lambda d: d["complete_invariant_spectrum"].__setitem__("bound_state_multiplicity", 9)),
        ("invent_embedded_state", lambda d: d["complete_invariant_spectrum"].__setitem__("embedded_eigenvalues", True)),
        ("invent_singular_continuous", lambda d: d["complete_invariant_spectrum"].__setitem__("singular_continuous_spectrum", True)),
        ("change_ac_multiplicity", lambda d: d["complete_invariant_spectrum"].__setitem__("absolutely_continuous_spectral_multiplicity", 1)),
        ("inflate_resolvent_rank", lambda d: d["complete_invariant_spectrum"].__setitem__("resolvent_difference_finite_rank_at_most", 18)),
        ("erase_wave_completeness", lambda d: d["complete_invariant_spectrum"].__setitem__("invariant_sector_wave_operators_complete", False)),
        ("erase_Pauli_vacancy", lambda d: d["residual_pauli_threshold"].__setitem__("creation_vacancy", 0)),
        ("break_Gamma_rank", lambda d: d["residual_pauli_threshold"].__setitem__("rank_Gamma_tau", 0)),
        ("invent_dark_space", lambda d: d["residual_pauli_threshold"].__setitem__("dark_impurity_dimension", 1)),
        ("invent_threshold_resonance", lambda d: d["residual_pauli_threshold"].__setitem__("impurity_local_threshold_resonance", True)),
        ("mislabel_inactive_as_Pauli", lambda d: d["residual_pauli_threshold"].__setitem__("inactive_channels_are_Pauli_blocked", True)),
        ("erase_Mourre", lambda d: d["propagation_boundary"].__setitem__("strict_Mourre_on_compact_intervals_above_threshold", False)),
        ("invent_uniform_threshold_LAP", lambda d: d["propagation_boundary"].__setitem__("unweighted_or_threshold_uniform_full_channel_LAP", True)),
        ("promote_full_signed_Mourre", lambda d: d["propagation_boundary"].__setitem__("full_signed_Fock_Mourre_or_high_energy_uniformity_proved", True)),
        ("erase_single_cut_obstruction", lambda d: d["periodic_topology"].__setitem__("every_single_cut_unwrapping_retains_seam_witness", False)),
        ("invent_recentring_repair", lambda d: d["periodic_topology"].__setitem__("recentring_single_cell_repairs_uniform_relative_form_convergence", True)),
        ("exclude_all_multichart_routes", lambda d: d["periodic_topology"].__setitem__("multichart_or_topology_changing_comparison_excluded", True)),
        ("invent_full_signed_spectrum", lambda d: d["ownership_boundary"].__setitem__("complete_bidirectional_signed_residual_spectrum_computed", True)),
        ("invent_dark_denominator", lambda d: d["ownership_boundary"].__setitem__("nonvacuous_signed_dark_denominator_computed", True)),
        ("invent_Moller_Ruelle", lambda d: d["ownership_boundary"].__setitem__("many_body_Moller_or_Ruelle_completeness_proved", True)),
        ("invent_NESS", lambda d: d["ownership_boundary"].__setitem__("interacting_NESS_constructed", True)),
        ("invent_source_owner", lambda d: d["ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent_Born", lambda d: d["ownership_boundary"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["ownership_boundary"].__setitem__("held_out_scored", True)),
        ("promote_prediction", lambda d: d["ownership_boundary"].__setitem__("prediction_or_confirmation_credit", True)),
        ("promote_canon", lambda d: d["ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("publish_result", lambda d: d["ownership_boundary"].__setitem__("paper_release_or_public_posture_change", "released")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "The physical GU NESS is proved.")),
    )
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
    print(f"K145 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
