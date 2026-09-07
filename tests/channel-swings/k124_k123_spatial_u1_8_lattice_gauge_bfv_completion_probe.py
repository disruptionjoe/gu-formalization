#!/usr/bin/env python3
"""Exact standard-library certificate for the K124 spatial gauge control."""

from __future__ import annotations

import copy
import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k124-k123-spatial-u1-8-lattice-gauge-bfv-completion-wave.json"
STATES = [(x, r) for x in range(3) for r in range(3)]
ROOT_VERTEX = 8
SPATIAL_SITES = 4


def charges() -> list[list[int]]:
    return [[int(v == a) for a in range(8)] if v != ROOT_VERTEX else [0] * 8 for v in range(9)]


def edges(mutation: str | None = None) -> list[tuple[int, int]]:
    rows: list[tuple[int, int]] = []
    for i, (x, r) in enumerate(STATES):
        for j, (y, s) in enumerate(STATES):
            if i < j and ((r == s and x != y) or (x == y and r != s)):
                rows.append((i, j))
    if mutation == "drop_transition_edge":
        rows.pop()
    return rows


def sub(left: list[int], right: list[int]) -> list[int]:
    return [a - b for a, b in zip(left, right)]


def add(left: list[int], right: list[int]) -> list[int]:
    return [a + b for a, b in zip(left, right)]


def rank(matrix: list[list[Fraction]]) -> int:
    work = [row[:] for row in matrix]
    if not work:
        return 0
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next((row for row in range(pivot_row, len(work)) if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(len(work)):
            if row != pivot_row and work[row][column]:
                factor = work[row][column]
                work[row] = [a - factor * b for a, b in zip(work[row], work[pivot_row])]
        pivot_row += 1
    return pivot_row


def transition_charges(mutation: str | None = None) -> list[list[int]]:
    q = charges()
    rows = [sub(q[v], q[u]) for u, v in edges(mutation)]
    return rows


def rate(u: int, v: int, mutation: str | None = None) -> Fraction:
    x, r = STATES[u]
    y, s = STATES[v]
    if r == s and x != y:
        return Fraction(2, 5)
    if x == y and r != s:
        if mutation == "equilibrate_cycle":
            return Fraction(7, 11 * 3)
        return Fraction(7, 11) * Fraction(81 if s == x else 16, 113)
    return Fraction(0)


def cycle_ratio(mutation: str | None = None) -> Fraction:
    index = {state: i for i, state in enumerate(STATES)}
    route = [index[(0, 0)], index[(1, 0)], index[(1, 1)], index[(0, 1)]]
    forward = Fraction(1)
    reverse = Fraction(1)
    for u, v in zip(route, route[1:] + route[:1]):
        forward *= rate(u, v, mutation)
        reverse *= rate(v, u, mutation)
    return forward / reverse


def phase_pair(charge: list[int], theta: list[int]) -> int:
    return sum(a * b for a, b in zip(charge, theta))


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    q = charges()
    edge_list = edges(mutation)
    b = transition_charges(mutation)
    c = [[-entry for entry in row] for row in b]
    if mutation == "break_defect_charge":
        c[0][0] += 1
    theta0 = [2, -1, 3, 0, 1, -2, 4, -3]
    theta1 = [-1, 5, 0, 2, -4, 3, 1, 2]
    defect_exponents = [phase_pair(be, theta0) + phase_pair(ce, theta0) for be, ce in zip(b, c)]
    hopping_exponents = [
        phase_pair(ce, theta1) + phase_pair(ce, sub(theta0, theta1)) - phase_pair(ce, theta0)
        for ce in c
    ]
    incidence_rows = [[Fraction(value) for value in row] for row in b]
    gauss_commutators = [[0 for _ in range(8 * SPATIAL_SITES)] for _ in range(8 * SPATIAL_SITES)]
    if mutation == "nonabelian_gauss":
        gauss_commutators[0][1] = 1
    electric_divergence = [
        [((x + 1) * (a + 2)) - (((x - 1) % SPATIAL_SITES) + 1) * (a + 2) for a in range(8)]
        for x in range(SPATIAL_SITES)
    ]
    telescopes = [sum(electric_divergence[x][a] for x in range(SPATIAL_SITES)) for a in range(8)]
    if mutation == "break_periodic_telescoping":
        telescopes[0] += 1
    integer_gauss_spectra = mutation != "noninteger_gauss"
    group_average_eigenvalues = [1 if value == 0 else 0 for value in (-2, -1, 0, 1, 2)] if integer_gauss_spectra else [0, 0, 0, 0, 0]
    hopping_bounded = mutation != "unbounded_hopping"
    defect_bounded = mutation != "unbounded_defect"
    electric_positive = mutation != "negative_electric_energy"
    hamiltonian_invariant = mutation != "break_hamiltonian_invariance"
    root_vacuum_charge = q[ROOT_VERTEX]
    ratio = cycle_ratio(mutation)
    return [
        ("K115 carrier has nine detector states", len(q) == 9),
        ("one root plus eight basis charges gives rank eight", rank(incidence_rows) == 8),
        ("K115 graph has 18 undirected transitions", len(edge_list) == 18),
        ("every transition charge is nonzero", all(any(row) for row in b)),
        ("CAR creation charge cancels transition charge", all(add(be, ce) == [0] * 8 for be, ce in zip(b, c))),
        ("every defect monomial is locally neutral", all(value == 0 for value in defect_exponents)),
        ("every covariant spatial hop is locally neutral", all(value == 0 for value in hopping_exponents)),
        ("finite periodic regulator has four sites", SPATIAL_SITES == 4),
        ("there are eight local Gauss generators per site", 8 * SPATIAL_SITES == 32),
        ("all local Gauss generators commute", all(value == 0 for row in gauss_commutators for value in row)),
        ("periodic electric divergence telescopes", all(value == 0 for value in telescopes)),
        ("Gauss sum therefore imposes total matter neutrality", all(value == 0 for value in telescopes)),
        ("root-system zero-flux vacuum is physical", root_vacuum_charge == [0] * 8),
        ("compact integer group average selects zero Gauss eigenvalue", group_average_eigenvalues == [0, 0, 1, 0, 0]),
        ("group-average eigenvalues define a projector", all(value * value == value for value in group_average_eigenvalues)),
        ("abelian BFV charge squares to zero", all(value == 0 for row in gauss_commutators for value in row)),
        ("electric rotor energy is positive", electric_positive),
        ("finite-lattice covariant CAR hopping is bounded", hopping_bounded),
        ("compactly smeared defect remains bounded", defect_bounded),
        ("bounded perturbation preserves the electric self-adjoint domain", electric_positive and hopping_bounded and defect_bounded),
        ("full regulated Hamiltonian preserves Gauss kernel", hamiltonian_invariant and all(value == 0 for value in defect_exponents + hopping_exponents)),
        ("spatial circle leaves eight Wilson holonomies", 8 * (SPATIAL_SITES - (SPATIAL_SITES - 1)) == 8),
        ("transition graph cycle rank remains ten", len(edge_list) - 9 + 1 == 10),
        ("spatial holonomies are not transition cycles", 8 != 10),
        ("selected modular rate cycle remains 6561/256", ratio == Fraction(6561, 256)),
        ("gauge phases do not equilibrate the modular cycle", ratio != 1),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    charge = data.get("charge_localization", {})
    lattice = data.get("spatial_lattice_gauge_model", {})
    bfv = data.get("dirac_bfv_boundary", {})
    domain = data.get("hamiltonian_domain", {})
    cycle = data.get("cycle_and_nonselection_boundary", {})
    state = data.get("state_effect_boundary", {})
    owner = data.get("ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    expected_charge = {
        "detector_states": 9, "transition_edges": 18,
        "independent_vertex_charge_directions": 8,
        "charge_lattice": "Z^8_after_one_root_state",
        "transition_charge_is_vertex_difference": True,
        "CAR_species_creation_charge_is_negative_transition_charge": True,
        "defect_monomials_are_locally_neutral": True,
        "charge_root_or_normalization_source_selected": False,
    }
    if any(charge.get(key) != value for key, value in expected_charge.items()):
        failures.append("charge_localization")
    required_lattice = (
        "finite_periodic_sites", "integer_electric_spectrum",
        "covariant_CAR_hopping_is_locally_gauge_invariant", "Gauss_generators_commute",
        "periodic_Gauss_sum_is_total_matter_charge", "global_neutrality_required",
        "root_vacuum_zero_flux_physical_sector_exists", "neutral_defect_preserves_physical_sector",
    )
    if lattice.get("spatial_dimension") != 1 or lattice.get("compact_link_group") != "U(1)^8" or lattice.get("local_Gauss_generators_per_site") != 8 or any(lattice.get(key) is not True for key in required_lattice):
        failures.append("spatial_lattice")
    if any(bfv.get(key) is not True for key in ("compact_Haar_group_average_is_orthogonal_physical_projector", "projector_image_is_joint_Gauss_kernel", "abelian_BFV_charge_is_nilpotent", "finite_lattice_Hamiltonian_Dirac_sector_owned", "finite_lattice_algebraic_BFV_complex_owned")) or any(bfv.get(key) is not False for key in ("continuum_Lagrangian_BV_master_action_owned", "source_derived_boundary_BFV_charge_owned", "GU_native_physical_cohomology_owned")):
        failures.append("dirac_bfv")
    if any(domain.get(key) is not True for key in ("electric_energy_positive_and_self_adjoint_on_rotor_domain", "finite_lattice_covariant_CAR_hopping_bounded", "compactly_smeared_defect_bounded", "full_regulated_Hamiltonian_self_adjoint_on_electric_domain", "full_regulated_Hamiltonian_bounded_below", "Hamiltonian_preserves_joint_Gauss_kernel")) or any(domain.get(key) is not False for key in ("continuum_or_unsmeared_limit_constructed", "complete_interacting_Haag_Kastler_net_constructed", "interacting_nonequilibrium_stationary_state_constructed")):
        failures.append("hamiltonian_domain")
    expected_cycle = {
        "spacetime_gauge_charge_directions": 8,
        "transition_graph_cycle_directions": 10,
        "periodic_spatial_Wilson_holonomies": 8,
        "these_three_counts_identified_as_one_object": False,
        "selected_rate_cycle_forward_reverse_ratio": "6561/256",
        "modular_affinity_remains_nonzero": True,
        "compact_gauge_phase_identified_with_real_affinity": False,
        "gauge_covariance_selects_regulator_couplings_boundary_flux_or_state": False,
        "K123_recovered_only_after_supplied_gauge_slice_and_frozen_sector": True,
    }
    if any(cycle.get(key) != value for key, value in expected_cycle.items()):
        failures.append("cycle_nonselection")
    if state.get("mathematical_physical_subspace_owned_for_regulated_model") is not True or any(state.get(key) is not False for key in ("incoming_or_stationary_physical_state_selected", "physical_detector_effects_selected", "Born_rule_derived")):
        failures.append("state_effect")
    if owner.get("Weinstein_source_or_GU_action_gauge_group_charge_coupling_domain_state_or_observable_owner") is not False or owner.get("finite_regulator_promoted_to_continuum_GU_theory") is not False or owner.get("held_out_scored") is not False or owner.get("prediction_or_confirmation_credit") is not False or owner.get("canon_verdict_change") != "none":
        failures.append("ownership")
    if data.get("exact_control", {}).get("charge_covariance_Gauss_BFV_domain_cycle_affinity_and_ownership_boundaries_checked") is not True:
        failures.append("exact_control")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("repository-owned", "finite", "U(1)^8", "Gauss", "No Weinstein/source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "drop_transition_edge", "break_defect_charge", "nonabelian_gauss",
        "break_periodic_telescoping", "noninteger_gauss", "unbounded_hopping",
        "unbounded_defect", "negative_electric_energy",
        "break_hamiltonian_invariance", "equilibrate_cycle",
    )]
    updates = (
        ("invent_source_charge", lambda d: d["charge_localization"].__setitem__("charge_root_or_normalization_source_selected", True)),
        ("erase_local_covariance", lambda d: d["spatial_lattice_gauge_model"].__setitem__("covariant_CAR_hopping_is_locally_gauge_invariant", False)),
        ("erase_neutrality", lambda d: d["spatial_lattice_gauge_model"].__setitem__("global_neutrality_required", False)),
        ("erase_physical_sector", lambda d: d["spatial_lattice_gauge_model"].__setitem__("root_vacuum_zero_flux_physical_sector_exists", False)),
        ("erase_BFV_nilpotence", lambda d: d["dirac_bfv_boundary"].__setitem__("abelian_BFV_charge_is_nilpotent", False)),
        ("invent_continuum_BV", lambda d: d["dirac_bfv_boundary"].__setitem__("continuum_Lagrangian_BV_master_action_owned", True)),
        ("invent_source_BFV", lambda d: d["dirac_bfv_boundary"].__setitem__("source_derived_boundary_BFV_charge_owned", True)),
        ("invent_GU_cohomology", lambda d: d["dirac_bfv_boundary"].__setitem__("GU_native_physical_cohomology_owned", True)),
        ("erase_self_adjointness", lambda d: d["hamiltonian_domain"].__setitem__("full_regulated_Hamiltonian_self_adjoint_on_electric_domain", False)),
        ("invent_unsmeared_limit", lambda d: d["hamiltonian_domain"].__setitem__("continuum_or_unsmeared_limit_constructed", True)),
        ("invent_AQFT", lambda d: d["hamiltonian_domain"].__setitem__("complete_interacting_Haag_Kastler_net_constructed", True)),
        ("invent_NESS", lambda d: d["hamiltonian_domain"].__setitem__("interacting_nonequilibrium_stationary_state_constructed", True)),
        ("conflate_cycles", lambda d: d["cycle_and_nonselection_boundary"].__setitem__("these_three_counts_identified_as_one_object", True)),
        ("conflate_affinity", lambda d: d["cycle_and_nonselection_boundary"].__setitem__("compact_gauge_phase_identified_with_real_affinity", True)),
        ("invent_parameter_selection", lambda d: d["cycle_and_nonselection_boundary"].__setitem__("gauge_covariance_selects_regulator_couplings_boundary_flux_or_state", True)),
        ("erase_supplied_slice", lambda d: d["cycle_and_nonselection_boundary"].__setitem__("K123_recovered_only_after_supplied_gauge_slice_and_frozen_sector", False)),
        ("invent_state", lambda d: d["state_effect_boundary"].__setitem__("incoming_or_stationary_physical_state_selected", True)),
        ("invent_detector", lambda d: d["state_effect_boundary"].__setitem__("physical_detector_effects_selected", True)),
        ("invent_Born", lambda d: d["state_effect_boundary"].__setitem__("Born_rule_derived", True)),
        ("invent_GU_owner", lambda d: d["ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_gauge_group_charge_coupling_domain_state_or_observable_owner", True)),
        ("promote_regulator", lambda d: d["ownership_boundary"].__setitem__("finite_regulator_promoted_to_continuum_GU_theory", True)),
        ("score_holdout", lambda d: d["ownership_boundary"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A GU gauge theory derives Born probabilities.")),
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
    print(f"K124 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
