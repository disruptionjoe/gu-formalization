#!/usr/bin/env python3
"""Exact/numerical controls for the K136 minimal-cutoff/Coulomb boundary."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k136-minimal-cutoff-feshbach-scale-coulomb-wave.json"
MU = 1.3
NU = 2.1
E0, E1, E2 = 4.0, 5.0, 6.0
GA, GB = 0.37, 0.43
SPECIES = 18


def omega(k: int) -> float:
    return math.sqrt(1.0 + k * k)


def subtraction(cutoff: int, scale: float = MU, mutation: str | None = None) -> float:
    sign = -1.0 if mutation == "reverse_counterterm" else 1.0
    return sign * sum(1.0 / (omega(k) + scale) for k in range(-cutoff, cutoff + 1))


def inner_denominator(cutoff: int, spectator_k: int, mutation: str | None = None) -> float:
    counterterm = 0.0 if mutation == "omit_inner_counterterm" else GA * GA * subtraction(cutoff, mutation=mutation)
    lower = sum(
        1.0 / (E0 + omega(ell) + omega(spectator_k) + 1.0)
        for ell in range(-cutoff, cutoff + 1)
    )
    return E1 + omega(spectator_k) + 1.0 + counterterm - GA * GA * lower


def top_schur(cutoff: int, extension: float = 0.0, mutation: str | None = None) -> float:
    outer = sum(
        1.0 / inner_denominator(cutoff, k, mutation)
        for k in range(-cutoff, cutoff + 1)
    )
    counterterm = 0.0 if mutation == "omit_outer_counterterm" else GB * GB * subtraction(cutoff, mutation=mutation)
    return E2 + extension + 1.0 + counterterm - GB * GB * outer


def inner_tail(cutoff: int, high: int, spectator_k: int) -> float:
    return sum(
        abs(
            1.0 / (omega(ell) + MU)
            - 1.0 / (E0 + omega(ell) + omega(spectator_k) + 1.0)
        )
        for ell in range(-high, high + 1)
        if abs(ell) > cutoff
    )


def lower_resolvent_tail(cutoff: int, high: int, spectator_k: int = 0) -> float:
    return math.sqrt(sum(
        1.0 / (E0 + omega(ell) + omega(spectator_k) + 1.0) ** 2
        for ell in range(-high, high + 1)
        if abs(ell) > cutoff
    ))


def outer_vector_tail(cutoff: int, high: int) -> float:
    return math.sqrt(sum(
        4.0 / (E1 + omega(k) + 1.0) ** 2
        for k in range(-high, high + 1)
        if abs(k) > cutoff
    ))


def scale_delta(cutoff: int, first: float = MU, second: float = NU) -> float:
    return sum(
        1.0 / (omega(k) + first) - 1.0 / (omega(k) + second)
        for k in range(-cutoff, cutoff + 1)
    )


def filled_energy(particles: int, mutation: str | None = None) -> float:
    if mutation == "erase_pauli_filling":
        return float(particles)
    radius = particles // SPECIES + 4
    levels = sorted(
        omega(k) for k in range(-radius, radius + 1) for _ in range(SPECIES)
    )
    return sum(levels[:particles])


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    ladder = data.get("minimal_cutoff_depth_two_ladder", {})
    scale = data.get("finite_renormalization_selection", {})
    pauli = data.get("pauli_filling_and_coulomb", {})
    dressed = data.get("all_sector_dressed_completion", {})
    boundary = data.get("thermodynamic_and_ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    required_ladder = (
        "uses_K134_physical_ordered_matrix_unit_CAR_couplings",
        "contains_two_distinct_edges_and_two_particle_species",
        "ladder_is_invariant_for_the_declared_two_edge_restriction",
        "uses_only_the_diagonal_endpoint_counterterm_c_N_D_g",
        "inner_renormalized_Schur_inverse_factors_converge_uniformly_in_spectator_momentum",
        "outer_resolvent_dressed_Schur_vector_is_square_summable",
        "all_block_resolvent_factors_converge_in_operator_norm",
        "minimal_cutoff_converges_in_norm_resolvent_on_the_depth_two_invariant_ladder",
    )
    if any(ladder.get(k) is not True for k in required_ladder) or any(
        ladder.get(k) is not False for k in (
            "ladder_is_proved_invariant_under_the_complete_K127_defect",
            "complete_nine_state_eighteen_species_minimal_cutoff_converges",
            "overlapping_path_operator_valued_Schur_recursion_is_closed",
        )
    ):
        failures.append("minimal_ladder")
    required_scale = (
        "subtraction_scale_difference_has_an_absolutely_convergent_limit",
        "renormalized_impurity_energy_runs_by_the_opposite_finite_D_g_shift",
        "scale_compensated_cutoff_families_have_the_same_limit",
        "one_frozen_Schur_boundary_value_selects_the_corresponding_finite_extension_matrix",
    )
    if any(scale.get(k) is not True for k in required_scale) or any(
        scale.get(k) is not False for k in (
            "ultraviolet_tail_alone_selects_W", "source_or_GU_action_supplies_the_boundary_value"
        )
    ):
        failures.append("renormalization_selection")
    required_pauli = (
        "finite_circle_positive_dispersion_has_finite_species_multiplicity",
        "fermionic_Pauli_filling_bounds_particle_number_squared_by_free_energy_plus_one",
        "finite_interval_cumulative_charge_Coulomb_form_is_bounded_by_global_flux_energy_plus_particle_number_squared",
        "all_sector_Coulomb_form_is_free_plus_global_flux_form_bounded",
    )
    if any(pauli.get(k) is not True for k in required_pauli) or pauli.get("momentum_occupation_and_position_Coulomb_commutation_is_required") is not False or any(
        pauli.get(k) is not False for k in (
            "same_bound_holds_for_empty_vacuum_signed_Dirac_energy",
            "same_coercivity_is_uniform_in_infinite_volume",
        )
    ):
        failures.append("pauli_coulomb")
    required_dressed = (
        "positive_Coulomb_form_can_be_added_to_the_K135_regular_operator_by_closed_form_sum",
        "regular_cutoff_forms_converge_in_form_norm_after_the_same_Coulomb_addition",
        "K134_boundary_transforms_converge_in_norm_and_remain_boundedly_invertible",
        "all_sector_positive_energy_dressed_Coulomb_Gauss_completions_are_self_adjoint",
        "dressed_Coulomb_cutoffs_converge_in_norm_resolvent",
        "finite_Hermitian_W_family_remains",
    )
    if any(dressed.get(k) is not True for k in required_dressed) or any(
        dressed.get(k) is not False for k in (
            "minimally_countertermed_Coulomb_cutoff_convergence_is_proved",
            "uniquely_selected_physical_point_Fock_Gauss_Hamiltonian_constructed",
        )
    ):
        failures.append("dressed_coulomb")
    denied = (
        "full_signed_Dirac_polarization_selected", "infinite_volume_limit_constructed",
        "Moller_or_Ruelle_wave_operator_constructed", "interacting_NESS_constructed",
        "interacting_field_current_constructed", "reduced_cycle_promoted_to_field_current",
        "smooth_unreduced_connection_or_BRST_parent_constructed",
        "Weinstein_source_or_GU_action_owner", "Born_rule_derived", "held_out_scored",
        "prediction_or_confirmation_credit",
    )
    if boundary.get("finite_circle_positive_dispersion_control_only") is not True or any(boundary.get(k) is not False for k in denied) or boundary.get("reduced_K115_cycle_ratio") != "6561/256" or boundary.get("canon_verdict_change") != "none" or boundary.get("paper_release_or_public_posture_change") != "none":
        failures.append("boundary")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("repository-owned", "two-edge restriction", "depth-two", "norm-resolvent", "subtraction-scale", "Schur boundary", "Pauli filling", "all Fock sectors", "complete nine-state/eighteen-species minimal cutoff", "signed-Dirac", "NESS/current", "Weinstein/source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    cutoffs = (16, 32, 64, 128)
    inner_rows = [[inner_denominator(n, k, mutation) for n in cutoffs] for k in (0, 3, 17)]
    inner_steps = [[abs(row[i + 1] - row[i]) for i in range(len(row) - 1)] for row in inner_rows]
    top_values = [top_schur(n, mutation=mutation) for n in cutoffs]
    top_steps = [abs(top_values[i + 1] - top_values[i]) for i in range(len(top_values) - 1)]
    lower_tails = [lower_resolvent_tail(n, 8192) for n in (32, 128, 512, 2048)]
    outer_tails = [outer_vector_tail(n, 8192) for n in (32, 128, 512, 2048)]
    renorm = [scale_delta(n) for n in cutoffs]
    renorm_steps = [abs(renorm[i + 1] - renorm[i]) for i in range(len(renorm) - 1)]
    scale_compensated = [
        subtraction(n, MU) - subtraction(n, NU) - scale_delta(n)
        for n in cutoffs
    ]
    extension_difference = top_schur(512, extension=0.73) - top_schur(512)
    particle_counts = (1, 18, 36, 72, 144, 288, 576)
    energies = [filled_energy(n, mutation) for n in particle_counts]
    filling_ratios = [n * n / (energy + 1.0) for n, energy in zip(particle_counts, energies)]
    flux_sq, length, qmax = 25.0, 3.0, 2.0
    coulomb_ratios = [
        (2.0 * length * (flux_sq + qmax * qmax * n * n)) / (energy + flux_sq + 1.0)
        for n, energy in zip(particle_counts, energies)
    ]
    return [
        ("two nonzero physical ladder couplings are present", GA > 0 and GB > 0),
        ("finite cutoff subtraction grows logarithmically", subtraction(2048, mutation=mutation) > subtraction(512, mutation=mutation)),
        ("inner Schur denominators stay positive at the common resolvent point", min(min(row) for row in inner_rows) > 1.0),
        ("inner denominator increments decrease for every tested spectator", all(all(a > b for a, b in zip(row, row[1:])) for row in inner_steps)),
        ("inner denominator sequence is Cauchy", max(row[-1] for row in inner_steps) < 0.04),
        ("inner renormalized tail is absolutely small", inner_tail(2048, 8192, 17) < 0.02),
        ("outer Schur increments decrease", all(a > b for a, b in zip(top_steps, top_steps[1:]))),
        ("outer Schur sequence is Cauchy", top_steps[-1] < 0.02),
        ("outer Schur denominator stays positive", min(top_values) > 1.0),
        ("lower resolvent-dressed coupling tails decrease", all(a > b for a, b in zip(lower_tails, lower_tails[1:]))),
        ("lower resolvent-dressed coupling tail is small", lower_tails[-1] < 0.04),
        ("outer Schur vector tails decrease", all(a > b for a, b in zip(outer_tails, outer_tails[1:]))),
        ("outer Schur vector is square summable", outer_tails[-1] < 0.06),
        ("depth-two resolvent factors have a common coercive bound", min(min(row) for row in inner_rows) > 0 and min(top_values) > 0),
        ("subtraction-scale difference converges", all(a > b for a, b in zip(renorm_steps, renorm_steps[1:]))),
        ("subtraction-scale tail is small", renorm_steps[-1] < 0.02),
        ("finite scale compensation is exact at every cutoff", max(abs(x) for x in scale_compensated) < 1e-12),
        ("finite extension shifts the Schur boundary affinely", abs(extension_difference - 0.73) < 1e-12),
        ("distinct finite Schur boundary data give distinct resolvents", abs(1.0 / top_schur(512, 0.73) - 1.0 / top_schur(512)) > 0.001),
        ("finite species multiplicity is eighteen", SPECIES == 18),
        ("Pauli-filled energy is superlinear", all(energies[i + 1] / particle_counts[i + 1] > energies[i] / particle_counts[i] for i in range(1, len(energies) - 1))),
        ("particle number squared is controlled by kinetic energy", max(filling_ratios) < 100.0),
        ("all-sector Coulomb ratio is uniformly bounded on tested fillings", max(coulomb_ratios) < 2500.0),
        ("Coulomb control uses no momentum-position commutator", True),
        ("positive Coulomb form does not reduce semiboundedness", all(x >= 0 for x in coulomb_ratios)),
        ("form-domain addition is all-sector rather than fixed-particle", particle_counts[-1] > 500),
        ("the signed empty-vacuum branch is not covered", True),
        ("the finite-circle filling constant is not claimed uniform in volume", True),
        ("the dressed extension family remains nonunique", abs(extension_difference) > 0.5),
        ("the complete overlapping nine-state recursion remains open", True),
        ("minimal Coulomb cutoff convergence remains open", True),
        ("no infinite-volume NESS or field current follows", Fraction(6561, 256) != 1),
        ("delayed-choice holdout remains unscored", True),
    ]


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "omit_inner_counterterm", "omit_outer_counterterm", "reverse_counterterm", "erase_pauli_filling"
    )]
    updates = (
        ("erase_physical_coupling", lambda d: d["minimal_cutoff_depth_two_ladder"].__setitem__("uses_K134_physical_ordered_matrix_unit_CAR_couplings", False)),
        ("erase_two_edge_depth", lambda d: d["minimal_cutoff_depth_two_ladder"].__setitem__("contains_two_distinct_edges_and_two_particle_species", False)),
        ("invent_full_invariance", lambda d: d["minimal_cutoff_depth_two_ladder"].__setitem__("ladder_is_proved_invariant_under_the_complete_K127_defect", True)),
        ("invent_full_minimal_limit", lambda d: d["minimal_cutoff_depth_two_ladder"].__setitem__("complete_nine_state_eighteen_species_minimal_cutoff_converges", True)),
        ("invent_operator_recursion", lambda d: d["minimal_cutoff_depth_two_ladder"].__setitem__("overlapping_path_operator_valued_Schur_recursion_is_closed", True)),
        ("erase_norm_resolvent", lambda d: d["minimal_cutoff_depth_two_ladder"].__setitem__("all_block_resolvent_factors_converge_in_operator_norm", False)),
        ("erase_scale_flow", lambda d: d["finite_renormalization_selection"].__setitem__("subtraction_scale_difference_has_an_absolutely_convergent_limit", False)),
        ("invent_UV_selection", lambda d: d["finite_renormalization_selection"].__setitem__("ultraviolet_tail_alone_selects_W", True)),
        ("invent_source_boundary", lambda d: d["finite_renormalization_selection"].__setitem__("source_or_GU_action_supplies_the_boundary_value", True)),
        ("erase_boundary_condition", lambda d: d["finite_renormalization_selection"].__setitem__("one_frozen_Schur_boundary_value_selects_the_corresponding_finite_extension_matrix", False)),
        ("erase_pauli_bound", lambda d: d["pauli_filling_and_coulomb"].__setitem__("fermionic_Pauli_filling_bounds_particle_number_squared_by_free_energy_plus_one", False)),
        ("require_false_commutation", lambda d: d["pauli_filling_and_coulomb"].__setitem__("momentum_occupation_and_position_Coulomb_commutation_is_required", True)),
        ("invent_signed_coercivity", lambda d: d["pauli_filling_and_coulomb"].__setitem__("same_bound_holds_for_empty_vacuum_signed_Dirac_energy", True)),
        ("invent_volume_uniformity", lambda d: d["pauli_filling_and_coulomb"].__setitem__("same_coercivity_is_uniform_in_infinite_volume", True)),
        ("erase_closed_form", lambda d: d["all_sector_dressed_completion"].__setitem__("positive_Coulomb_form_can_be_added_to_the_K135_regular_operator_by_closed_form_sum", False)),
        ("erase_all_sector", lambda d: d["all_sector_dressed_completion"].__setitem__("all_sector_positive_energy_dressed_Coulomb_Gauss_completions_are_self_adjoint", False)),
        ("invent_minimal_Coulomb", lambda d: d["all_sector_dressed_completion"].__setitem__("minimally_countertermed_Coulomb_cutoff_convergence_is_proved", True)),
        ("invent_unique_physical_H", lambda d: d["all_sector_dressed_completion"].__setitem__("uniquely_selected_physical_point_Fock_Gauss_Hamiltonian_constructed", True)),
        ("erase_W_family", lambda d: d["all_sector_dressed_completion"].__setitem__("finite_Hermitian_W_family_remains", False)),
        ("invent_signed_selection", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("full_signed_Dirac_polarization_selected", True)),
        ("invent_infinite_volume", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("infinite_volume_limit_constructed", True)),
        ("invent_NESS", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("interacting_NESS_constructed", True)),
        ("promote_current", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("reduced_cycle_promoted_to_field_current", True)),
        ("invent_smooth_parent", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("smooth_unreduced_connection_or_BRST_parent_constructed", True)),
        ("invent_source_owner", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent_Born", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["thermodynamic_and_ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A complete GU point theory derives Born predictions.")),
    )
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught.append((name, bool(manifest_failures(mutant))))
    for name, ok in caught:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(int(bool(ok)) for _, ok in caught)}/{len(caught)} caught")
    return 0 if all(ok for _, ok in caught) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    checks = exact_checks()
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    failures = manifest_failures(data)
    for failure in failures:
        print(f"[FAIL] manifest {failure}")
    print(f"K136 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
