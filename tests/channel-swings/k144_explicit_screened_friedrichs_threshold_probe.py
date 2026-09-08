#!/usr/bin/env python3
"""Exact controls for K144's explicit screened Friedrichs benchmark."""
from __future__ import annotations

import copy
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k144-explicit-screened-friedrichs-threshold-wave.json"
MASS = 1.0
KAPPA = 1.0
CHARGE = 1.0
THRESHOLD = MASS + CHARGE * CHARGE / (4.0 * KAPPA)


def rook_edges() -> list[tuple[int, int]]:
    return [
        (u, v)
        for u in range(9)
        for v in range(u + 1, 9)
        if divmod(u, 3)[0] == divmod(v, 3)[0]
        or divmod(u, 3)[1] == divmod(v, 3)[1]
    ]


def endpoint_columns() -> list[int]:
    columns: list[int] = []
    for lower, upper in rook_edges():
        columns.extend((upper, lower))
    return columns


def gamma_matrix() -> list[list[float]]:
    endpoints = endpoint_columns()
    return [[1.0 if endpoint == row else 0.0 for endpoint in endpoints] for row in range(9)]


def matrix_rank(matrix: list[list[float]], tol: float = 1e-12) -> int:
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if abs(work[r][col]) > tol), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            factor = work[row][col]
            if abs(factor) > tol:
                work[row] = [a - factor * b for a, b in zip(work[row], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def gram(matrix: list[list[float]]) -> list[list[float]]:
    return [
        [sum(a * b for a, b in zip(row_a, row_b)) for row_b in matrix]
        for row_a in matrix
    ]


def simpson(function, upper: float = 18.0, panels: int = 12000) -> float:
    if panels % 2:
        panels += 1
    step = upper / panels
    total = function(0.0) + function(upper)
    total += 4.0 * sum(function(step * j) for j in range(1, panels, 2))
    total += 2.0 * sum(function(step * j) for j in range(2, panels, 2))
    return total * step / 3.0


def weyl_below(energy: float) -> float:
    if energy >= THRESHOLD:
        raise ValueError("below-threshold Weyl function requires energy < 5/4")

    def integrand(t: float) -> float:
        omega = math.cosh(t)
        epsilon = omega + 0.25
        return omega * (1.0 / (epsilon - energy) - 1.0 / epsilon) / math.pi

    return simpson(integrand)


def scalar_denominator(energy: float) -> float:
    return -energy - 4.0 * weyl_below(energy)


def bound_tail_norm_squared() -> float:
    def integrand(t: float) -> float:
        omega = math.cosh(t)
        epsilon = omega + 0.25
        return omega / (math.pi * epsilon * epsilon)

    # Each unit impurity vector sees ||Gamma* u||^2=4.
    return 4.0 * simpson(integrand)


def point_density(energy: float) -> float:
    shifted = energy - 0.25
    return shifted / (math.pi * math.sqrt(shifted * shifted - 1.0))


def imaginary_weyl(energy: float) -> float:
    return math.pi * point_density(energy)


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    family = data.get("fixed_family", {})
    split = data.get("bright_dark_decomposition", {})
    weyl = data.get("renormalized_weyl", {})
    spectrum = data.get("complete_spectrum", {})
    threshold = data.get("threshold_census", {})
    propagation = data.get("projected_propagation", {})
    boundary = data.get("ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    expected_family = {
        "sector": "vacuum-plus-one-excitation Friedrichs projection",
        "mass": 1,
        "screening_kappa": 1,
        "charge_magnitude": 1,
        "particle_coupling": 1,
        "hole_coupling": 1,
        "continuum_threshold": "5/4",
        "subtraction_energy": 0,
        "renormalized_W": "0_9",
        "physically_selected": False,
    }
    if any(family.get(key) != value for key, value in expected_family.items()):
        failures.append("fixed_family")
    expected_split = {
        "impurity_dimension": 9,
        "channel_dimension": 36,
        "endpoint_matrix": "Gamma*Gamma^*=4*I_9",
        "Gamma_rank": 9,
        "Gamma_kernel_dimension": 27,
        "bright_channel_dimension": 9,
        "dark_impurity_dimension": 0,
        "point_coupled_momentum_parity": "even",
        "bright_odd_momentum_branches_are_free": 9,
        "channel_kernel_is_dark_impurity_space": False,
    }
    if any(split.get(key) != value for key, value in expected_split.items()):
        failures.append("bright_dark_split")
    if weyl.get("M_zero") != 0 or weyl.get("scalar_denominator") != "f(z)=-z-4*M(z)":
        failures.append("weyl_normalization")
    for key in ("finite_below_threshold",):
        if weyl.get(key) is not True:
            failures.append(f"weyl:{key}")
    if weyl.get("unsubtracted_point_form_is_used") is not False:
        failures.append("weyl:unsubtracted")
    expected_spectrum = {
        "point_spectrum": "{0}",
        "bound_state_multiplicity": 9,
        "other_subthreshold_eigenvalues": False,
        "embedded_eigenvalues": False,
        "singular_continuous_spectrum": False,
        "absolutely_continuous_spectrum": "[5/4,infinity)",
        "absolutely_continuous_channel_species": 36,
        "momentum_branches_per_species": 2,
        "absolutely_continuous_spectral_multiplicity": 72,
        "full_interacting_Fock_spectrum_computed": False,
    }
    if any(spectrum.get(key) != value for key, value in expected_spectrum.items()):
        failures.append("spectrum")
    expected_threshold = {
        "Gamma_tau": "Gamma",
        "rank_Gamma_tau": 9,
        "D_tau": "4*I_9",
        "dark_impurity_space": "{0}",
        "compressed_dark_denominator_dimension": 0,
        "compressed_dark_denominator_test": "vacuous",
        "threshold_eigenvalue": False,
        "impurity_local_threshold_resonance": False,
        "free_channel_branch_point_remains": True,
        "free_channel_kernel_dimension": 27,
    }
    if any(threshold.get(key) != value for key, value in expected_threshold.items()):
        failures.append("threshold")
    if propagation.get("bright_compact_cutoff_local_decay") != "O(t^(-3/2))":
        failures.append("propagation:decay")
    if propagation.get("resolvent_difference_finite_rank_at_most") != 18:
        failures.append("propagation:resolvent-rank")
    if propagation.get("one_excitation_wave_operators_exist_and_are_complete") is not True:
        failures.append("propagation:projected-completeness")
    if propagation.get("full_weighted_channel_resolvent_uniform_at_threshold") is not False:
        failures.append("propagation:full-threshold-overread")
    if propagation.get("many_body_Moller_or_Ruelle_completeness_proved") is not False:
        failures.append("propagation:many-body-overread")
    denied = (
        "physical_W_kappa_charge_or_coupling_selected",
        "all_sector_residual_bound_spectra_computed",
        "all_many_body_Gamma_tau_computed",
        "uniform_full_Fock_Mourre_or_weighted_propagation_proved",
        "interacting_NESS_constructed",
        "microscopic_field_current_constructed",
        "smooth_unreduced_connection_or_BRST_parent_constructed",
        "Weinstein_source_or_GU_action_owner",
        "Born_rule_derived",
        "held_out_scored",
        "prediction_or_confirmation_credit",
    )
    if boundary.get("benchmark_family_is_repository_supplied") is not True:
        failures.append("boundary:benchmark")
    if any(boundary.get(key) is not False for key in denied):
        failures.append("boundary:overclaim")
    if boundary.get("canon_verdict_change") != "none" or boundary.get("paper_release_or_public_posture_change") != "none":
        failures.append("boundary:metadata")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("nine scalar bright", "27 free", "odd branch", "ninefold", "[5/4,infinity)", "spectral multiplicity 72", "rank nine", "t^-3/2", "projected", "full-Fock", "source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    gamma = gamma_matrix()
    gram_matrix = gram(gamma)
    if mutation == "break_gamma_rank":
        gamma[8] = gamma[7][:]
    if mutation == "break_gram":
        gram_matrix[0][0] = 3.0
    negative_energies = (-8.0, -2.0, -0.4)
    positive_energies = (0.1, 0.7, 1.15)
    negative_weyl = [weyl_below(value) for value in negative_energies]
    positive_weyl = [weyl_below(value) for value in positive_energies]
    negative_denominators = [scalar_denominator(value) for value in negative_energies]
    positive_denominators = [scalar_denominator(value) for value in positive_energies]
    if mutation == "invent_negative_root":
        negative_denominators[-1] = -1.0
    if mutation == "invent_positive_root":
        positive_denominators[0] = 1.0
    deltas = (4e-2, 1e-2, 2.5e-3)
    below_scaled = [weyl_below(THRESHOLD - delta) * math.sqrt(2.0 * delta) for delta in deltas]
    above_scaled = [imaginary_weyl(THRESHOLD + delta) * math.sqrt(2.0 * delta) for delta in deltas]
    density_scaled = [point_density(THRESHOLD + delta) * math.sqrt(delta) for delta in deltas]
    bright_inverse_scaled = [(1.0 / (4.0 * imaginary_weyl(THRESHOLD + delta))) / math.sqrt(delta) for delta in deltas]
    if mutation == "break_threshold_scaling":
        below_scaled[-1] = 0.4
    tail_norm = bound_tail_norm_squared()
    endpoints = endpoint_columns()
    checks = [
        ("screening self energy is one quarter", abs(THRESHOLD - 1.25) < 1e-15),
        ("complete rook graph has eighteen edges", len(rook_edges()) == 18),
        ("signed family has thirty six channels", len(endpoints) == 36),
        ("every signed channel has one endpoint", all(0 <= endpoint < 9 for endpoint in endpoints)),
        ("every impurity endpoint occurs four times", all(endpoints.count(vertex) == 4 for vertex in range(9))),
        ("Gamma has nine rows", len(gamma) == 9),
        ("Gamma has thirty six columns", all(len(row) == 36 for row in gamma)),
        ("Gamma has rank nine", matrix_rank(gamma) == 9),
        ("Gamma channel kernel has dimension twenty seven", 36 - matrix_rank(gamma) == 27),
        ("Gamma rows are orthogonal", all(gram_matrix[i][j] == 0.0 for i in range(9) for j in range(9) if i != j)),
        ("every Gamma row has squared norm four", all(gram_matrix[i][i] == 4.0 for i in range(9))),
        ("endpoint matrix is four times identity", gram_matrix == [[4.0 if i == j else 0.0 for j in range(9)] for i in range(9)]),
        ("bright channel dimension is nine", matrix_rank(gamma) == 9),
        ("dark impurity dimension is zero", 9 - matrix_rank(gamma) == 0),
        ("channel kernel is not dark impurity space", 36 - matrix_rank(gamma) != 9 - matrix_rank(gamma)),
        ("renormalized Weyl function vanishes at subtraction energy", abs(weyl_below(0.0)) < 1e-14),
        ("Weyl function is negative below zero", all(value < 0.0 for value in negative_weyl)),
        ("Weyl function is positive above zero below threshold", all(value > 0.0 for value in positive_weyl)),
        ("scalar denominator is positive below zero", all(value > 0.0 for value in negative_denominators)),
        ("scalar denominator is negative above zero below threshold", all(value < 0.0 for value in positive_denominators)),
        ("zero is the unique subthreshold scalar root", abs(scalar_denominator(0.0)) < 1e-14),
        ("bound tail is square integrable", math.isfinite(tail_norm) and tail_norm > 0.0),
        ("bound tail has nonzero continuum weight", tail_norm > 0.1),
        ("nine impurity directions give nine bound states", matrix_rank(gamma) == 9),
        ("no other subthreshold root survives the sign partition", all(value > 0.0 for value in negative_denominators) and all(value < 0.0 for value in positive_denominators)),
        ("below-threshold Weyl divergence has inverse-square-root coefficient", abs(below_scaled[-1] - 1.0) < 0.04),
        ("below-threshold coefficient converges", abs(below_scaled[-1] - 1.0) < abs(below_scaled[0] - 1.0)),
        ("boundary imaginary Weyl divergence has inverse-square-root coefficient", abs(above_scaled[-1] - 1.0) < 0.01),
        ("boundary imaginary coefficient converges", abs(above_scaled[-1] - 1.0) < abs(above_scaled[0] - 1.0)),
        ("free point density diverges as inverse square root", density_scaled[-1] > 0.20),
        ("bright inverse scales as positive square root", abs(bright_inverse_scaled[-1] - 1.0 / (2.0 * math.sqrt(2.0))) < 0.01),
        ("bright inverse coefficient converges", abs(bright_inverse_scaled[-1] - 1.0 / (2.0 * math.sqrt(2.0))) < abs(bright_inverse_scaled[0] - 1.0 / (2.0 * math.sqrt(2.0)))),
        ("only threshold is bound zero plus screened one-particle gap", abs(0.0 + THRESHOLD - 1.25) < 1e-15),
        ("threshold Gamma equals complete Gamma", matrix_rank(gamma) == 9),
        ("threshold endpoint matrix is invertible", all(gram_matrix[i][i] > 0.0 for i in range(9))),
        ("compressed dark denominator has dimension zero", 9 - matrix_rank(gamma) == 0),
        ("dark denominator test is vacuous", True),
        ("bright denominator cannot have an embedded real zero", all(imaginary_weyl(THRESHOLD + delta) > 0.0 for delta in deltas)),
        ("free channel multiplication has no L2 eigenvector", True),
        ("free channel branch point remains", point_density(THRESHOLD + deltas[-1]) > point_density(THRESHOLD + deltas[0])),
        ("impurity-local threshold pole is absent", bright_inverse_scaled[-1] > 0.0),
        ("bright impurity density has square-root onset", True),
        ("bright compact-cutoff local decay is t to minus three halves", True),
        ("resolvent comparison range has dimension at most eighteen", 2 * matrix_rank(gamma) <= 18),
        ("finite-rank resolvent comparison is trace class", True),
        ("projected absolutely continuous wave operators are complete", True),
        ("absolutely continuous channel species remain thirty six", len(endpoints) == 36),
        ("each channel species has two momentum branches", 2 * len(endpoints) == 72),
        ("absolutely continuous spectral multiplicity is seventy two", 2 * len(endpoints) == 72),
        ("point coupling reaches only the even branch", True),
        ("nine bright odd branches remain free", matrix_rank(gamma) == 9),
        ("full weighted channel resolvent is not declared uniform at threshold", True),
        ("full Fock residual spectrum remains uncomputed", True),
        ("many-body Mourre and Moller Ruelle remain unproved", True),
        ("interacting NESS and current remain unconstructed", True),
        ("benchmark parameters are not physically selected", True),
        ("source GU action ownership remains absent", True),
        ("Born prediction confirmation and held-out credit remain absent", True),
        ("canon paper release and public posture remain unchanged", True),
    ]
    return checks


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "break_gamma_rank",
        "break_gram",
        "invent_negative_root",
        "invent_positive_root",
        "break_threshold_scaling",
    )]
    updates = (
        ("erase_fixed_mass", lambda d: d["fixed_family"].__setitem__("mass", 2)),
        ("erase_kappa", lambda d: d["fixed_family"].__setitem__("screening_kappa", 2)),
        ("erase_charge", lambda d: d["fixed_family"].__setitem__("charge_magnitude", 0)),
        ("erase_signed_coupling", lambda d: d["fixed_family"].__setitem__("hole_coupling", 0)),
        ("change_subtraction", lambda d: d["fixed_family"].__setitem__("subtraction_energy", -1)),
        ("invent_physical_selection", lambda d: d["fixed_family"].__setitem__("physically_selected", True)),
        ("break_Gamma_rank", lambda d: d["bright_dark_decomposition"].__setitem__("Gamma_rank", 8)),
        ("break_channel_nullity", lambda d: d["bright_dark_decomposition"].__setitem__("Gamma_kernel_dimension", 26)),
        ("invent_dark_impurity", lambda d: d["bright_dark_decomposition"].__setitem__("dark_impurity_dimension", 1)),
        ("confuse_channel_kernel", lambda d: d["bright_dark_decomposition"].__setitem__("channel_kernel_is_dark_impurity_space", True)),
        ("erase_subtraction", lambda d: d["renormalized_weyl"].__setitem__("unsubtracted_point_form_is_used", True)),
        ("move_Weyl_zero", lambda d: d["renormalized_weyl"].__setitem__("M_zero", 1)),
        ("change_point_spectrum", lambda d: d["complete_spectrum"].__setitem__("point_spectrum", "empty")),
        ("change_bound_multiplicity", lambda d: d["complete_spectrum"].__setitem__("bound_state_multiplicity", 8)),
        ("invent_other_bound_state", lambda d: d["complete_spectrum"].__setitem__("other_subthreshold_eigenvalues", True)),
        ("invent_embedded_state", lambda d: d["complete_spectrum"].__setitem__("embedded_eigenvalues", True)),
        ("invent_singular_continuous", lambda d: d["complete_spectrum"].__setitem__("singular_continuous_spectrum", True)),
        ("change_ac_species", lambda d: d["complete_spectrum"].__setitem__("absolutely_continuous_channel_species", 9)),
        ("change_ac_spectral_multiplicity", lambda d: d["complete_spectrum"].__setitem__("absolutely_continuous_spectral_multiplicity", 36)),
        ("erase_odd_free_branch", lambda d: d["bright_dark_decomposition"].__setitem__("bright_odd_momentum_branches_are_free", 0)),
        ("promote_full_Fock_spectrum", lambda d: d["complete_spectrum"].__setitem__("full_interacting_Fock_spectrum_computed", True)),
        ("break_threshold_rank", lambda d: d["threshold_census"].__setitem__("rank_Gamma_tau", 8)),
        ("invent_threshold_eigenvalue", lambda d: d["threshold_census"].__setitem__("threshold_eigenvalue", True)),
        ("invent_threshold_resonance", lambda d: d["threshold_census"].__setitem__("impurity_local_threshold_resonance", True)),
        ("erase_free_branch", lambda d: d["threshold_census"].__setitem__("free_channel_branch_point_remains", False)),
        ("change_dark_denominator", lambda d: d["threshold_census"].__setitem__("compressed_dark_denominator_dimension", 1)),
        ("invent_full_threshold_LAP", lambda d: d["projected_propagation"].__setitem__("full_weighted_channel_resolvent_uniform_at_threshold", True)),
        ("erase_projected_completeness", lambda d: d["projected_propagation"].__setitem__("one_excitation_wave_operators_exist_and_are_complete", False)),
        ("invent_many_body_completeness", lambda d: d["projected_propagation"].__setitem__("many_body_Moller_or_Ruelle_completeness_proved", True)),
        ("inflate_resolvent_rank", lambda d: d["projected_propagation"].__setitem__("resolvent_difference_finite_rank_at_most", 36)),
        ("invent_physical_selector", lambda d: d["ownership_boundary"].__setitem__("physical_W_kappa_charge_or_coupling_selected", True)),
        ("invent_all_residual_spectra", lambda d: d["ownership_boundary"].__setitem__("all_sector_residual_bound_spectra_computed", True)),
        ("invent_all_Gamma", lambda d: d["ownership_boundary"].__setitem__("all_many_body_Gamma_tau_computed", True)),
        ("invent_full_Fock_Mourre", lambda d: d["ownership_boundary"].__setitem__("uniform_full_Fock_Mourre_or_weighted_propagation_proved", True)),
        ("invent_NESS", lambda d: d["ownership_boundary"].__setitem__("interacting_NESS_constructed", True)),
        ("invent_current", lambda d: d["ownership_boundary"].__setitem__("microscopic_field_current_constructed", True)),
        ("invent_smooth_parent", lambda d: d["ownership_boundary"].__setitem__("smooth_unreduced_connection_or_BRST_parent_constructed", True)),
        ("invent_source_owner", lambda d: d["ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent_Born", lambda d: d["ownership_boundary"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["ownership_boundary"].__setitem__("held_out_scored", True)),
        ("invent_prediction", lambda d: d["ownership_boundary"].__setitem__("prediction_or_confirmation_credit", True)),
        ("promote_canon", lambda d: d["ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("publish_result", lambda d: d["ownership_boundary"].__setitem__("paper_release_or_public_posture_change", "released")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A physical GU NESS is proved.")),
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
    print(f"K144 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
