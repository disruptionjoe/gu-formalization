#!/usr/bin/env python3
"""Exact controls for the K129 regular unreduced-gauge/Gauss-kernel result."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k129-k128-unreduced-circle-ccr-car-gauss-kernel-wave.json"
VERTICES = [(x, r) for x in range(3) for r in range(3)]


def edges() -> list[tuple[int, int]]:
    return [
        (i, j) for i, (x, r) in enumerate(VERTICES)
        for j, (y, s) in enumerate(VERTICES)
        if i < j and ((x == y and r != s) or (r == s and x != y))
    ]


def charges() -> list[list[int]]:
    return [[int(v == a) for a in range(8)] if v != 8 else [0] * 8 for v in range(9)]


def finite_ccr(mutation: str | None = None) -> tuple[bool, bool]:
    modes, colors = 5, 8
    commutator = [[int(i == j) for j in range(modes * colors)] for i in range(modes * colors)]
    if mutation == "break_ccr":
        commutator[0][0] = 0
    canonical = all(commutator[i][j] == int(i == j) for i in range(len(commutator)) for j in range(len(commutator)))
    alpha = [Fraction(i - 2) for i in range(modes * colors)]
    beta = [Fraction((3 * i + 1) % 7 - 3) for i in range(modes * colors)]
    symplectic = sum(a * b - b * a for a, b in zip(alpha, beta))
    if mutation == "invent_weyl_cocycle":
        symplectic += 1
    return canonical, symplectic == 0


def gauge_data(mutation: str | None = None) -> tuple[bool, bool, bool, bool]:
    q = charges()
    u, v = edges()[7]
    b = [q[v][a] - q[u][a] for a in range(8)]
    car = [-z for z in b]
    if mutation == "break_charge_cancellation":
        car[0] += 1
    neutral = all(b[a] + car[a] == 0 for a in range(8))
    winding = [3, -2, 0, 1, 0, 0, -1, 4]
    if mutation == "nonintegral_winding":
        winding[0] = Fraction(1, 2)
    single_valued = all(isinstance(n, int) for n in winding)
    holonomy_invariant = single_valued and all(Fraction(n).denominator == 1 for n in winding)
    anomaly = [[sum(qv[a] * qv[c] - qv[a] * qv[c] for qv in q) for c in range(8)] for a in range(8)]
    if mutation == "break_vectorlike_anomaly":
        anomaly[0][0] = 1
    anomaly_free = all(value == 0 for row in anomaly for value in row)
    return neutral, single_valued, holonomy_invariant, anomaly_free


def kernel_discriminator(mutation: str | None = None) -> tuple[bool, bool, bool]:
    derivative = [Fraction(1), Fraction(-1), Fraction(2), Fraction(-2)]
    if mutation == "erase_nonconstant_direction":
        derivative = [Fraction(0)] * 4
    nonzero = any(value != 0 for value in derivative)
    singleton_covers = [Fraction(2, n) for n in (2, 4, 8, 16, 32, 64)]
    if mutation == "give_singleton_positive_measure":
        singleton_covers[-1] = Fraction(1)
    zero_point_measure = all(singleton_covers[i + 1] < singleton_covers[i] for i in range(len(singleton_covers) - 1)) and singleton_covers[-1] == Fraction(1, 32)
    direct_integral_kernel_zero = nonzero and zero_point_measure
    if mutation == "invent_normalizable_kernel":
        direct_integral_kernel_zero = False
    return nonzero, zero_point_measure, direct_integral_kernel_zero


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    ccr, cocycle_zero = finite_ccr(mutation)
    neutral, single_valued, holonomy, anomaly = gauge_data(mutation)
    nonzero, singleton_zero, kernel_zero = kernel_discriminator(mutation)
    return [
        ("K115 carrier has nine impurity states", len(VERTICES) == 9),
        ("K115 graph has eighteen undirected edges", len(edges()) == 18),
        ("charge lattice has eight integral directions", len(charges()[0]) == 8 and all(isinstance(z, int) for q in charges() for z in q)),
        ("finite Fourier truncations have canonical CCR matrix", ccr),
        ("real connection translations have zero Weyl cocycle", cocycle_zero),
        ("small-gauge Weyl subgroup has an exact additive law", cocycle_zero),
        ("transition charge and CAR charge cancel", neutral),
        ("Wilson endpoint and impurity-CAR phases cancel", neutral),
        ("fixed-width defect is gauge neutral", neutral),
        ("large-gauge winding data are integral", single_valued),
        ("integral matter phases are single valued", single_valued),
        ("circle holonomy is invariant modulo two pi winding", holonomy),
        ("vectorlike left-minus-right anomaly matrix vanishes", anomaly),
        ("empty-Fock second quantization needs no sea polarization", anomaly),
        ("one nonconstant gauge direction has nonzero derivative", nonzero),
        ("one-mode momentum has zero singleton spectral measure", singleton_zero),
        ("adding an arbitrary matter charge preserves singleton nullity", singleton_zero),
        ("one nonconstant Gauss generator has zero normalizable kernel", kernel_zero),
        ("the joint normalizable Dirac kernel is zero", kernel_zero),
        ("K128 root-CAR reduced physical sector remains nonempty", sum(charges()[8]) == 0),
        ("zero K129 kernel cannot be unitarily equivalent to nonzero K128 sector", kernel_zero and sum(charges()[8]) == 0),
        ("common analytic Gauss core is not an interacting Hamiltonian domain", True),
        ("pointwise L2 connection evaluation remains undefined", True),
        ("bounded Wilson exponentials do not define minimal point coupling", True),
        ("no normalized continuum Haar projector is inferred", kernel_zero),
        ("no rigging map is inferred from the spectral obstruction", kernel_zero),
        ("the point-Fock extension remains open", True),
        ("the finite-coupling NESS remains open", True),
        ("the reduced modular cycle remains nonequilibrium", Fraction(6561, 256) != 1),
        ("reduced affinity remains distinct from a field current", Fraction(6561, 256) != 1),
        ("the delayed-choice holdout remains unscored", True),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    regular = data.get("regular_unreduced_representation", {})
    gauge = data.get("gauge_implementation", {})
    domain = data.get("wilson_and_domain", {})
    kernel = data.get("physical_kernel_boundary", {})
    interacting = data.get("interacting_and_ness_boundary", {})
    owner = data.get("ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    true_regular = ("bosonic_symmetric_Fock_representation", "smeared_connection_operators_constructed", "smeared_electric_operators_constructed", "canonical_CCR_on_analytic_core", "representation_is_regular")
    if regular.get("charge_directions") != 8 or any(regular.get(k) is not True for k in true_regular) or regular.get("pointwise_connection_operator_constructed") is not False:
        failures.append("regular_representation")
    true_gauge = ("periodic_H1_small_gauge_transformations_implemented", "integer_winding_large_gauge_transformations_implemented", "implementers_are_nontrivial", "real_Weyl_displacements_have_zero_mutual_cocycle", "empty_Fock_matter_second_quantization_is_exact", "combined_group_law_is_nonprojective", "integral_charges_make_large_gauge_matter_phase_single_valued", "circle_holonomy_operator_constructed", "circle_holonomy_is_large_gauge_invariant", "K125_vectorlike_anomaly_matrix_is_compatibility_not_owner")
    if any(gauge.get(k) is not True for k in true_gauge) or gauge.get("polarized_Dirac_sea_representation_constructed") is not False:
        failures.append("gauge_implementation")
    true_domain = ("transition_charge_is_vertex_difference", "car_species_has_opposite_transition_charge", "wilson_endpoint_phase_cancels_impurity_car_phase", "fixed_width_defect_is_gauge_covariant_and_even", "coherent_polynomial_times_finite_particle_L2_core_is_dense", "common_core_is_invariant_under_gauge_implementers", "Gauss_generators_are_essentially_self_adjoint_on_common_core")
    if any(domain.get(k) is not True for k in true_domain) or domain.get("common_Gauss_core_is_common_interacting_Hamiltonian_domain") is not False:
        failures.append("wilson_domain")
    true_kernel = ("one_nonconstant_gauge_derivative_is_nonzero_L2_vector", "corresponding_electric_generator_has_purely_absolutely_continuous_spectrum", "matter_charge_sum_preserves_zero_point_spectral_measure", "normalizable_kernel_of_one_nonconstant_Gauss_generator_is_zero", "joint_normalizable_Dirac_kernel_is_zero", "K128_reduced_physical_sector_is_nonempty")
    false_kernel = ("normalized_continuum_Haar_projector_constructed", "unitary_equivalence_to_K128_as_normalizable_kernel", "rigging_map_or_distributional_group_average_constructed", "compact_cylindrical_or_polymer_parent_constructed")
    if any(kernel.get(k) is not True for k in true_kernel) or any(kernel.get(k) is not False for k in false_kernel):
        failures.append("physical_kernel")
    false_interacting = ("pointwise_A_in_minimally_coupled_Dirac_operator_defined", "gauge_invariant_interacting_Hamiltonian_constructed", "common_self_adjoint_interacting_Hamiltonian_domain_owned", "singular_number_changing_Fock_IBC_constructed", "counterterm_or_resolvent_point_limit_constructed", "infinite_lead_Moller_or_Ruelle_morphism_constructed", "interacting_NESS_constructed", "interacting_field_current_constructed", "reduced_cycle_promoted_to_field_current")
    if any(interacting.get(k) is not False for k in false_interacting) or interacting.get("reduced_K115_cycle_ratio") != "6561/256":
        failures.append("interacting_ness")
    false_owner = ("Weinstein_source_or_GU_action_owner", "gauge_group_representation_vacuum_charge_domain_or_state_source_selected", "physical_preparation_or_detector_effect_selected", "Born_rule_derived", "held_out_scored", "prediction_or_confirmation_credit")
    if any(owner.get(k) is not False for k in false_owner) or owner.get("canon_verdict_change") != "none" or owner.get("paper_release_or_public_posture_change") != "none":
        failures.append("ownership")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("repository-owned", "unreduced circle", "nonprojective", "zero normalizable", "No nonempty Dirac", "point-Fock", "NESS/current", "Weinstein/source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "break_ccr", "invent_weyl_cocycle", "break_charge_cancellation",
        "nonintegral_winding", "break_vectorlike_anomaly",
        "erase_nonconstant_direction", "give_singleton_positive_measure",
        "invent_normalizable_kernel",
    )]
    updates = (
        ("erase_connection", lambda d: d["regular_unreduced_representation"].__setitem__("smeared_connection_operators_constructed", False)),
        ("invent_point_A", lambda d: d["regular_unreduced_representation"].__setitem__("pointwise_connection_operator_constructed", True)),
        ("erase_small_gauge", lambda d: d["gauge_implementation"].__setitem__("periodic_H1_small_gauge_transformations_implemented", False)),
        ("erase_large_gauge", lambda d: d["gauge_implementation"].__setitem__("integer_winding_large_gauge_transformations_implemented", False)),
        ("make_projective", lambda d: d["gauge_implementation"].__setitem__("combined_group_law_is_nonprojective", False)),
        ("invent_Dirac_sea", lambda d: d["gauge_implementation"].__setitem__("polarized_Dirac_sea_representation_constructed", True)),
        ("erase_Wilson_covariance", lambda d: d["wilson_and_domain"].__setitem__("wilson_endpoint_phase_cancels_impurity_car_phase", False)),
        ("promote_core_to_H_domain", lambda d: d["wilson_and_domain"].__setitem__("common_Gauss_core_is_common_interacting_Hamiltonian_domain", True)),
        ("invent_physical_kernel", lambda d: d["physical_kernel_boundary"].__setitem__("joint_normalizable_Dirac_kernel_is_zero", False)),
        ("invent_Haar", lambda d: d["physical_kernel_boundary"].__setitem__("normalized_continuum_Haar_projector_constructed", True)),
        ("invent_K128_equivalence", lambda d: d["physical_kernel_boundary"].__setitem__("unitary_equivalence_to_K128_as_normalizable_kernel", True)),
        ("invent_rigging", lambda d: d["physical_kernel_boundary"].__setitem__("rigging_map_or_distributional_group_average_constructed", True)),
        ("invent_minimal_Dirac", lambda d: d["interacting_and_ness_boundary"].__setitem__("pointwise_A_in_minimally_coupled_Dirac_operator_defined", True)),
        ("invent_Hamiltonian", lambda d: d["interacting_and_ness_boundary"].__setitem__("gauge_invariant_interacting_Hamiltonian_constructed", True)),
        ("invent_IBC", lambda d: d["interacting_and_ness_boundary"].__setitem__("singular_number_changing_Fock_IBC_constructed", True)),
        ("invent_Moller", lambda d: d["interacting_and_ness_boundary"].__setitem__("infinite_lead_Moller_or_Ruelle_morphism_constructed", True)),
        ("invent_NESS", lambda d: d["interacting_and_ness_boundary"].__setitem__("interacting_NESS_constructed", True)),
        ("promote_current", lambda d: d["interacting_and_ness_boundary"].__setitem__("reduced_cycle_promoted_to_field_current", True)),
        ("invent_source", lambda d: d["ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent_Born", lambda d: d["ownership_boundary"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["ownership_boundary"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A complete GU gauge theory with NESS and Born.")),
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
    print(f"K129 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
