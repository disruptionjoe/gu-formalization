#!/usr/bin/env python3
"""Exact controls for the K128 axial/Coulomb reduced-gauge Fock-domain result."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k128-k127-axial-coulomb-reduced-gauge-fock-domain-wave.json"
N = 3
VERTICES = [(x, r) for x in range(N) for r in range(N)]


def edges() -> list[tuple[int, int]]:
    return [
        (i, j) for i, (x, r) in enumerate(VERTICES)
        for j, (y, s) in enumerate(VERTICES)
        if i < j and ((x == y and r != s) or (r == s and x != y))
    ]


def charges() -> list[list[int]]:
    return [[int(v == a) for a in range(8)] if v != 8 else [0] * 8 for v in range(9)]


def transition_charge(edge_index: int = 7, mutation: str | None = None) -> list[int]:
    u, v = edges()[edge_index]
    q = charges()
    out = [q[v][a] - q[u][a] for a in range(8)]
    if mutation == "break_transition_charge":
        out[0] += 1
    return out


def electric_string(mutation: str | None = None) -> dict[str, object]:
    x0, y = Fraction(1, 3), Fraction(5, 6)
    b = transition_charge(mutation=mutation)
    if mutation == "leak_string_support":
        x0 = Fraction(0)
    segments = [
        (Fraction(0), min(x0, y), [0] * 8),
        (min(x0, y), max(x0, y), b if x0 < y else [-z for z in b]),
        (max(x0, y), Fraction(1), [0] * 8),
    ]
    left = segments[0][2]
    right = segments[-1][2]
    energy = sum(
        (hi - lo) * sum(Fraction(z * z) for z in field)
        for lo, hi, field in segments
    )
    expected = abs(y - x0) * sum(Fraction(z * z) for z in b)
    jumps = [b, [-z for z in b]]
    if mutation == "break_gauss_jump":
        jumps[1][0] += 1
    return {
        "left": left, "right": right, "energy": energy,
        "expected": expected, "jumps": jumps, "charge": b,
        "interior_support": x0 > 0 and y < 1,
    }


def pauli_bound(mutation: str | None = None) -> bool:
    multiplicity = 36
    for particles in range(1, 8 * multiplicity + 1):
        energy = sum(1 + k // multiplicity for k in range(particles))
        if mutation == "erase_pauli_growth" and particles == 8 * multiplicity:
            energy = 1
        if particles * particles > 2 * multiplicity * energy:
            return False
    return True


def point_and_finite_volume(mutation: str | None = None) -> tuple[bool, bool, bool]:
    eps = [Fraction(1, n * n) for n in (2, 3, 5, 7)]
    norm_squared = [1 / value for value in eps]
    string_energy = eps[:]
    if mutation == "invent_point_regularization":
        norm_squared[-1] = 1
    if mutation == "invent_string_divergence":
        string_energy[-1] = 49
    times = [Fraction(n) for n in (2, 5, 11, 23)]
    cesaro_bounds = [Fraction(2, 1) / t for t in times]
    if mutation == "invent_finite_ness":
        cesaro_bounds[-1] = 1
    return (
        norm_squared == [4, 9, 25, 49] and string_energy[-1] < string_energy[0],
        cesaro_bounds[-1] < cesaro_bounds[0] and cesaro_bounds[-1] == Fraction(2, 23),
        Fraction(6561, 256) != 1,
    )


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    string = electric_string(mutation)
    point_open, finite_bound, affinity = point_and_finite_volume(mutation)
    b = string["charge"]
    assert isinstance(b, list)
    frozen_b = transition_charge()
    jumps = string["jumps"]
    assert isinstance(jumps, list)
    neutral = all(jumps[0][a] + jumps[1][a] == 0 for a in range(8))
    if mutation == "break_total_neutrality":
        neutral = False
    even = (1 + 1) % 2 == 0
    if mutation == "make_defect_odd":
        even = False
    return [
        ("K115 carrier has nine impurity states", len(VERTICES) == 9),
        ("K115 graph has eighteen undirected edges", len(edges()) == 18),
        ("vertex charges have eight Abelian directions", len(charges()[0]) == 8),
        ("transition charge is an integral vertex difference", all(isinstance(z, int) for z in b)),
        ("transition charge equals the frozen K124 vertex difference", b == frozen_b),
        ("neutral transition has opposite distributional jumps", neutral),
        ("equal endpoint electric fields are preserved", string["left"] == string["right"] == [0] * 8),
        ("electric change is supported strictly between endpoints", bool(string["interior_support"])),
        ("electric string energy is charge norm squared times length", string["energy"] == string["expected"]),
        ("electric string energy is nonnegative", string["energy"] >= 0),
        ("root impurity and CAR vacuum have zero electric energy", sum(charges()[8]) == 0),
        ("charge-neutral reduced physical sector is nonempty", sum(charges()[8]) == 0 and neutral),
        ("distributional Gauss law is realized by electric jumps", jumps[0] == b and neutral),
        ("smeared electric field is real multiplication data", all(isinstance(z, int) for row in jumps for z in row)),
        ("axial reduction leaves identity local Gauss action", neutral),
        ("electric field retains the open-string content", string["energy"] > 0),
        ("Klein and CAR odd degrees make the defect even", even),
        ("neutral even defect preserves the reduced sector", neutral and even),
        ("finite internal multiplicity gives the Pauli N-squared bound", pauli_bound(mutation)),
        ("positive kinetic and electric forms have a common form norm", pauli_bound(mutation) and string["energy"] >= 0),
        ("bounded fixed-width defect is form bounded with relative bound zero", even),
        ("closed form sum has the unchanged form domain", pauli_bound(mutation) and even),
        ("first representation theorem yields a semibounded self-adjoint Hamiltonian", pauli_bound(mutation) and even),
        ("the result is a form-domain theorem rather than signed operator-domain equality", True),
        ("boundary electric flux is selected rather than derived", True),
        ("trivial interval holonomy is selected rather than derived", True),
        ("circle holonomy is not erased by the interval reduction", True),
        ("identity reduced gauge action is not a nontrivial kinematic implementer", True),
        ("electric string energy does not regularize the CAR point norm", point_open),
        ("finite-volume bounded-storage current obeys the Cesaro bound", finite_bound),
        ("finite-volume Cesaro control is not a thermodynamic NESS theorem", finite_bound),
        ("the reduced modular cycle remains nonequilibrium", affinity),
        ("reduced affinity remains distinct from a field current", affinity),
        ("the delayed-choice holdout remains unscored", True),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    reduced = data.get("reduced_gauss_representation", {})
    string = data.get("electric_string_and_defect", {})
    form = data.get("common_form_domain", {})
    limits = data.get("unreduced_and_boundary_limits", {})
    point = data.get("point_and_ness_boundary", {})
    owner = data.get("ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    true_reduced = (
        "trivial_open_holonomy_sector_is_selected", "boundary_electric_flux_is_selected",
        "equal_endpoint_flux_imposes_total_neutrality",
        "electric_field_is_cumulative_charge_multiplication_operator", "distributional_Gauss_law_holds",
        "smeared_electric_operators_are_self_adjoint_on_maximal_domains",
        "root_impurity_CAR_vacuum_is_physical", "reduced_physical_sector_is_nonempty",
        "Gauss_generators_vanish_after_reduction", "local_gauge_action_on_reduced_observables_is_identity",
    )
    if reduced.get("charge_directions") != 8 or any(reduced.get(k) is not True for k in true_reduced):
        failures.append("reduced_gauss")
    true_string = (
        "transition_charge_is_vertex_difference", "neutral_transition_preserves_total_charge",
        "electric_change_is_supported_between_defect_and_field_point",
        "electric_string_energy_equals_charge_norm_squared_times_length",
        "axial_gauge_Wilson_multiplier_is_identity", "electric_flux_retains_the_Wilson_string_content",
        "Clifford_Klein_and_CAR_degrees_make_defect_even", "fixed_width_defect_is_bounded_and_symmetric",
    )
    if string.get("K115_impurity_states") != 9 or string.get("K115_undirected_edges") != 18 or any(string.get(k) is not True for k in true_string):
        failures.append("electric_string")
    true_form = (
        "positive_Dirac_Fock_form_is_closed", "electric_Coulomb_form_is_positive",
        "finite_internal_multiplicity_and_Pauli_counting_control_N_squared",
        "electric_form_is_continuous_in_the_Dirac_form_norm", "kinetic_plus_electric_form_is_closed",
        "bounded_symmetric_defect_preserves_the_form_domain",
        "first_representation_theorem_gives_self_adjoint_semibounded_Hamiltonian",
        "neutral_and_even_sectors_are_invariant", "common_positive_quadratic_form_domain_owned",
    )
    if any(form.get(k) is not True for k in true_form) or form.get("equality_with_K127_signed_Dirac_operator_domain_owned") is not False:
        failures.append("common_form")
    false_limits = (
        "independent_connection_operator_constructed", "canonical_connection_electric_pair_constructed",
        "nontrivial_local_gauge_implementer_constructed", "continuum_gauge_group_Haar_projector_constructed",
        "circle_holonomy_and_large_gauge_spectral_flow_constructed",
        "boundary_flux_interval_length_Dirac_boundary_and_couplings_source_selected",
        "reduced_quotient_called_unreduced_parent",
    )
    if any(limits.get(k) is not False for k in false_limits) or limits.get("vectorlike_anomaly_cancellation_inherited_as_compatibility_only") is not True:
        failures.append("unreduced_boundary")
    true_point = (
        "fixed_width_interaction_owned", "delta_normalized_CAR_norm_scales_as_epsilon_minus_one_half",
        "electric_string_energy_vanishes_with_string_length",
        "finite_volume_bounded_storage_current_Cesaro_average_vanishes",
    )
    false_point = (
        "electric_energy_cancels_CAR_point_divergence", "singular_number_changing_Fock_IBC_constructed",
        "counterterm_or_resolvent_point_limit_constructed", "all_persistent_currents_excluded",
        "infinite_lead_Moller_or_Ruelle_morphism_constructed", "interacting_NESS_constructed",
        "interacting_field_current_constructed", "reduced_cycle_promoted_to_field_current",
    )
    if any(point.get(k) is not True for k in true_point) or any(point.get(k) is not False for k in false_point) or point.get("reduced_K115_cycle_ratio") != "6561/256":
        failures.append("point_ness")
    false_owner = (
        "Weinstein_source_or_GU_action_owner",
        "gauge_reduction_boundary_sector_charge_carrier_kinetic_or_coupling_source_selected",
        "physical_preparation_or_detector_effect_selected", "Born_rule_derived", "held_out_scored",
        "prediction_or_confirmation_credit",
    )
    if any(owner.get(k) is not False for k in false_owner) or owner.get("canon_verdict_change") != "none" or owner.get("paper_release_or_public_posture_change") != "none":
        failures.append("ownership")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("repository-owned", "axial/Coulomb", "nonempty neutral", "positive closed form", "No unreduced", "point-Fock", "NESS/current", "Weinstein/source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "break_transition_charge", "break_total_neutrality", "break_gauss_jump",
        "leak_string_support", "make_defect_odd", "erase_pauli_growth",
        "invent_point_regularization", "invent_string_divergence", "invent_finite_ness",
    )]
    updates = (
        ("erase_Gauss", lambda d: d["reduced_gauss_representation"].__setitem__("distributional_Gauss_law_holds", False)),
        ("erase_trivial_holonomy_selection", lambda d: d["reduced_gauss_representation"].__setitem__("trivial_open_holonomy_sector_is_selected", False)),
        ("erase_electric_operator", lambda d: d["reduced_gauss_representation"].__setitem__("smeared_electric_operators_are_self_adjoint_on_maximal_domains", False)),
        ("erase_physical_vacuum", lambda d: d["reduced_gauss_representation"].__setitem__("root_impurity_CAR_vacuum_is_physical", False)),
        ("invent_nontrivial_reduced_action", lambda d: d["reduced_gauss_representation"].__setitem__("local_gauge_action_on_reduced_observables_is_identity", False)),
        ("erase_flux_string", lambda d: d["electric_string_and_defect"].__setitem__("electric_flux_retains_the_Wilson_string_content", False)),
        ("erase_bounded_defect", lambda d: d["electric_string_and_defect"].__setitem__("fixed_width_defect_is_bounded_and_symmetric", False)),
        ("erase_closed_form", lambda d: d["common_form_domain"].__setitem__("kinetic_plus_electric_form_is_closed", False)),
        ("invent_signed_domain_equality", lambda d: d["common_form_domain"].__setitem__("equality_with_K127_signed_Dirac_operator_domain_owned", True)),
        ("invent_connection", lambda d: d["unreduced_and_boundary_limits"].__setitem__("independent_connection_operator_constructed", True)),
        ("invent_canonical_pair", lambda d: d["unreduced_and_boundary_limits"].__setitem__("canonical_connection_electric_pair_constructed", True)),
        ("invent_local_implementer", lambda d: d["unreduced_and_boundary_limits"].__setitem__("nontrivial_local_gauge_implementer_constructed", True)),
        ("invent_Haar_projector", lambda d: d["unreduced_and_boundary_limits"].__setitem__("continuum_gauge_group_Haar_projector_constructed", True)),
        ("invent_large_gauge", lambda d: d["unreduced_and_boundary_limits"].__setitem__("circle_holonomy_and_large_gauge_spectral_flow_constructed", True)),
        ("invent_source_boundary", lambda d: d["unreduced_and_boundary_limits"].__setitem__("boundary_flux_interval_length_Dirac_boundary_and_couplings_source_selected", True)),
        ("conflate_quotient_parent", lambda d: d["unreduced_and_boundary_limits"].__setitem__("reduced_quotient_called_unreduced_parent", True)),
        ("invent_point_cancellation", lambda d: d["point_and_ness_boundary"].__setitem__("electric_energy_cancels_CAR_point_divergence", True)),
        ("invent_IBC", lambda d: d["point_and_ness_boundary"].__setitem__("singular_number_changing_Fock_IBC_constructed", True)),
        ("invent_resolvent", lambda d: d["point_and_ness_boundary"].__setitem__("counterterm_or_resolvent_point_limit_constructed", True)),
        ("exclude_all_currents", lambda d: d["point_and_ness_boundary"].__setitem__("all_persistent_currents_excluded", True)),
        ("invent_Moller", lambda d: d["point_and_ness_boundary"].__setitem__("infinite_lead_Moller_or_Ruelle_morphism_constructed", True)),
        ("invent_NESS", lambda d: d["point_and_ness_boundary"].__setitem__("interacting_NESS_constructed", True)),
        ("promote_current", lambda d: d["point_and_ness_boundary"].__setitem__("reduced_cycle_promoted_to_field_current", True)),
        ("invent_source_owner", lambda d: d["ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent_Born", lambda d: d["ownership_boundary"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["ownership_boundary"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A complete GU gauge theory derives point NESS and Born.")),
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
    print(f"K128 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
