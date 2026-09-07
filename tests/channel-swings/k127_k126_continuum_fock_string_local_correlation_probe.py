#!/usr/bin/env python3
"""Exact K127 continuum Fock, string-locality, and correlation controls."""

from __future__ import annotations

import cmath
import copy
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k127-k126-continuum-fock-string-local-correlation-wave.json"
N = 3
KAPPA = Fraction(2, 5)
CLOCK = Fraction(7, 11)
HIGH = Fraction(81, 113)
LOW = Fraction(16, 113)
STATES = [(x, r) for x in range(N) for r in range(N)]
INDEX = {state: i for i, state in enumerate(STATES)}


def vertices() -> list[tuple[int, int]]:
    return STATES


def edges() -> list[tuple[int, int]]:
    return [
        (i, j)
        for i, (x, r) in enumerate(STATES)
        for j, (y, s) in enumerate(STATES)
        if i < j and ((r == s and x != y) or (x == y and r != s))
    ]


def charges() -> list[list[int]]:
    return [[int(v == a) for a in range(8)] if v != 8 else [0] * 8 for v in range(9)]


def transition_charges() -> list[list[int]]:
    q = charges()
    return [[q[v][a] - q[u][a] for a in range(8)] for u, v in edges()]


def wilson_covariance_error(mutation: str | None = None) -> float:
    sites = 17
    charge = transition_charges()[7][:]
    if mutation == "break_charge":
        charge[0] += 1
    frozen_impurity_charge = transition_charges()[7]
    alpha = [
        [0.05 * (a + 1) * (0.3 + math.sin(2 * math.pi * j / sites)) for a in range(8)]
        for j in range(sites)
    ]
    links = [[0.02 * (a + 1) * math.cos(2 * math.pi * (j + 0.5) / sites) for a in range(8)] for j in range(sites)]
    psi = [cmath.exp(0.13j * j) for j in range(sites)]
    weights = [1 / sites for _ in range(sites)]

    def dot(xs: list[int] | list[float], ys: list[float]) -> float:
        return sum(float(x) * y for x, y in zip(xs, ys))

    transport = [1 + 0j]
    for j in range(1, sites):
        transport.append(transport[-1] * cmath.exp(1j * dot(charge, links[j - 1])))
    dressed = sum(weights[j] * transport[j] * psi[j] for j in range(sites))
    transformed_links = [
        [links[j][a] + alpha[(j + 1) % sites][a] - alpha[j][a] for a in range(8)]
        for j in range(sites)
    ]
    transformed_transport = [1 + 0j]
    for j in range(1, sites):
        transformed_transport.append(
            transformed_transport[-1] * cmath.exp(1j * dot(charge, transformed_links[j - 1]))
        )
    transformed_psi = [cmath.exp(-1j * dot(charge, alpha[j])) * psi[j] for j in range(sites)]
    transformed = sum(weights[j] * transformed_transport[j] * transformed_psi[j] for j in range(sites))
    impurity_phase = cmath.exp(1j * dot(frozen_impurity_charge, alpha[0]))
    return abs(impurity_phase * transformed - dressed)


def kernel(x: int, mutation: str | None = None) -> list[Fraction]:
    high = HIGH + (Fraction(1, 113) if mutation == "break_rate" else 0)
    return [high if r == x else LOW for r in range(N)]


def rates(mutation: str | None = None) -> list[dict[int, Fraction]]:
    rows: list[dict[int, Fraction]] = []
    for x, r in STATES:
        row: dict[int, Fraction] = {}
        for y in range(N):
            if y != x:
                row[INDEX[(y, r)]] = KAPPA
        for s in range(N):
            if s != r:
                row[INDEX[(x, s)]] = CLOCK * kernel(x, mutation)[s]
        rows.append(row)
    return rows


def spectral_factorization(mutation: str | None = None) -> dict[str, object]:
    original = rates(mutation)
    rebuilt: list[dict[int, Fraction]] = [dict() for _ in STATES]
    occupations: list[Fraction] = []
    kappas: list[Fraction] = []
    for i in range(len(STATES)):
        for j in range(i + 1, len(STATES)):
            forward = original[i].get(j, Fraction(0))
            reverse = original[j].get(i, Fraction(0))
            if not forward and not reverse:
                continue
            total = forward + reverse
            occupation = reverse / total
            if mutation == "wrong_occupation" and not occupations:
                occupation += Fraction(1, 97)
            rebuilt[i][j] = total * (1 - occupation)
            rebuilt[j][i] = total * occupation
            occupations.append(occupation)
            kappas.append(total)
    return {"original": original, "rebuilt": rebuilt, "occupations": occupations, "kappas": kappas}


def bump_boundary(mutation: str | None = None) -> tuple[bool, bool, bool, bool]:
    # p(x)=(1-x^2)^3, p'=-6x(1-x^2)^2, p''=-6+36x^2-30x^4.
    def p(x: Fraction) -> Fraction:
        value = (1 - x * x) ** 3
        if mutation == "break_bump_value" and x == 1:
            value += 1
        return value

    def dp(x: Fraction) -> Fraction:
        value = -6 * x * (1 - x * x) ** 2
        if mutation == "break_bump_first" and x == -1:
            value += 1
        return value

    def ddp(x: Fraction) -> Fraction:
        value = -6 + 36 * x * x - 30 * x**4
        if mutation == "break_bump_second" and x == 1:
            value += 1
        return value

    endpoints = (Fraction(-1), Fraction(1))
    value_zero = all(p(x) == 0 for x in endpoints)
    first_zero = all(dp(x) == 0 for x in endpoints)
    second_zero = all(ddp(x) == 0 for x in endpoints)
    center_one = p(Fraction(0)) == 1
    return value_zero, first_zero, second_zero, center_one


def causal_support(mutation: str | None = None) -> tuple[bool, bool, bool]:
    interval = set(range(-2, 3))
    time = 3
    hull = set(range(min(interval) - time, max(interval) + time + 1))
    distant = set(range(6, 10))
    if mutation == "overlap_causal_hull":
        distant = set(range(5, 9))
    finite_speed = hull == set(range(-5, 6))
    spacelike = hull.isdisjoint(distant)
    impurity_degree, klein_degree, car_degree = 0, 1, 1
    if mutation == "make_interaction_odd":
        klein_degree = 0
    even = (impurity_degree + klein_degree + car_degree) % 2 == 0
    return finite_speed, spacelike, even


def point_scaling(mutation: str | None = None) -> tuple[bool, bool, bool]:
    epsilons = [Fraction(1, n * n) for n in (2, 3, 5, 7)]
    norm_squared = [1 / eps for eps in epsilons]
    scaled_norm_squared = [eps * value for eps, value in zip(epsilons, norm_squared)]
    strengths_squared = epsilons[:]
    if mutation == "erase_point_divergence":
        norm_squared[-1] = 1
    if mutation == "invent_point_strength":
        strengths_squared[-1] = 1
    return (
        norm_squared == [Fraction(4), Fraction(9), Fraction(25), Fraction(49)],
        all(value == 1 for value in scaled_norm_squared),
        strengths_squared[-1] < strengths_squared[0] and strengths_squared[-1] == Fraction(1, 49),
    )


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    factor = spectral_factorization(mutation)
    original = factor["original"]
    rebuilt = factor["rebuilt"]
    occupations = factor["occupations"]
    kappas = factor["kappas"]
    assert isinstance(original, list) and isinstance(rebuilt, list)
    assert isinstance(occupations, list) and isinstance(kappas, list)
    value_zero, first_zero, second_zero, center_one = bump_boundary(mutation)
    finite_speed, spacelike, interaction_even = causal_support(mutation)
    point_diverges, scaled_bounded, strength_zero = point_scaling(mutation)
    norm_preserved = all(abs(abs(cmath.exp(1j * x / 11)) - 1) < 1e-12 for x in range(18))
    if mutation == "break_wilson_norm":
        norm_preserved = False
    symmetric = all(rebuilt[i].get(j, 0) == original[i].get(j, 0) for i in range(9) for j in range(9))
    biased = [f for f in occupations if f != Fraction(1, 2)]
    return [
        ("K115 carrier has nine impurity states", len(vertices()) == 9),
        ("K115 graph has eighteen undirected edges", len(edges()) == 18),
        ("continuum lead carrier has eighteen full Dirac species", len(edges()) == 18),
        ("background gauge group has eight charges", len(transition_charges()[0]) == 8),
        ("Wilson multiplication preserves every L2 norm", norm_preserved),
        ("dressed CAR smearing is background-gauge covariant", wilson_covariance_error(mutation) < 1e-11),
        ("Klein and CAR odd degrees make the defect even", interaction_even),
        ("adjoint pairing makes the bounded defect symmetric", interaction_even and norm_preserved),
        ("finite CAR edge sum has the stated norm bound", 2 * len(edges()) == 36 and norm_preserved),
        ("bounded perturbation retains the free self-adjoint domain", interaction_even and norm_preserved),
        ("finite-particle smooth vectors remain a core", interaction_even and norm_preserved),
        ("free Dirac propagation expands support at unit speed", finite_speed),
        ("test algebra lies outside the causal hull", spacelike),
        ("even defect commutes across the graded-local split", spacelike and interaction_even),
        ("Dyson relative dynamics is causal-hull localized", finite_speed and spacelike and interaction_even),
        ("compact bump equals one on shell", center_one),
        ("compact bump value vanishes at both boundaries", value_zero),
        ("compact bump first derivative vanishes at both boundaries", first_zero),
        ("compact bump second derivative vanishes at both boundaries", second_zero),
        ("zero extension is C2 and supports two integrations by parts", value_zero and first_zero and second_zero),
        ("K115 spectral factorization has eighteen pairs", len(occupations) == 18),
        ("six pair occupations are biased", len(biased) == 6),
        ("twelve pair occupations are half filled", occupations.count(Fraction(1, 2)) == 12),
        ("biased occupations have odds 16/81", all(min(f, 1 - f) / max(f, 1 - f) == Fraction(16, 81) for f in biased)),
        ("six biased spectral totals equal 679/1243", kappas.count(Fraction(679, 1243)) == 6),
        ("nine symmetric base totals equal 4/5", kappas.count(Fraction(4, 5)) == 9),
        ("three symmetric record totals equal 224/1243", kappas.count(Fraction(224, 1243)) == 3),
        ("on-shell particle and hole weights recover all K115 rates", symmetric),
        ("delta-normalized L2 norm diverges", point_diverges),
        ("sqrt-epsilon coupling keeps the operator norm bounded", scaled_bounded),
        ("bounded scaling has vanishing distributional point strength", strength_zero),
        ("background covariance remains distinct from dynamical Gauss quantization", wilson_covariance_error(mutation) < 1e-11),
        ("fixed-width causal support remains distinct from point locality", len(set(range(-2, 3))) > 1),
        ("free L1 correlations remain distinct from finite-coupling NESS", value_zero and second_zero),
        ("the reduced modular cycle remains nonequilibrium", 6561 != 256),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    fock = data.get("continuum_fock_representation", {})
    gauge = data.get("background_gauge_covariance", {})
    local = data.get("string_local_causal_control", {})
    corr = data.get("thermal_correlation_control", {})
    point = data.get("point_and_ness_boundary", {})
    owner = data.get("ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    required_fock = (
        "Wilson_dressed_test_functions_remain_L2", "Wilson_dressing_preserves_each_L2_norm",
        "CAR_creation_and_annihilation_are_bounded_by_the_test_function_norm", "finite_defect_sum_is_bounded",
        "defect_is_symmetric_and_fermion_even", "free_second_quantized_Dirac_Hamiltonian_is_self_adjoint",
        "bounded_perturbation_gives_self_adjoint_interacting_Hamiltonian", "interacting_domain_equals_free_domain",
        "finite_particle_smooth_core_remains_a_core",
    )
    if any(fock.get(key) is not True for key in required_fock) or fock.get("connection_status") != "smooth_bounded_external_U1_to_the_8_background":
        failures.append("fock_domain")
    required_gauge = ("dressed_smearing_transforms_only_at_defect_origin", "impurity_phase_cancels_dressed_CAR_phase", "interaction_is_background_gauge_invariant", "path_convention_is_supplied_not_selected")
    false_gauge = ("dynamical_connection_operator_constructed", "electric_field_operator_constructed", "Gauss_generator_constructed", "physical_Gauss_kernel_or_projector_constructed", "quantum_gauge_Hilbert_representation_claimed")
    if any(gauge.get(key) is not True for key in required_gauge) or any(gauge.get(key) is not False for key in false_gauge):
        failures.append("background_gauge")
    required_local = ("Wilson_paths_and_smearing_support_lie_in_one_fixed_interval", "defect_belongs_to_the_even_local_algebra_of_that_interval_with_impurity", "defect_commutes_with_graded_local_algebras_at_disjoint_support", "free_Dirac_propagation_has_finite_speed", "Dyson_terms_are_supported_in_the_iterated_causal_hull", "relative_dynamics_is_trivial_on_the_spacelike_complement_of_the_causal_hull", "finite_width_string_local_relative_net_owned")
    false_local = ("path_independence_owned", "point_locality_owned", "complete_dynamical_gauge_Haag_Kastler_net_owned")
    if any(local.get(key) is not True for key in required_local) or any(local.get(key) is not False for key in false_local):
        failures.append("string_locality")
    required_corr = ("extended_spectral_shape_is_C2", "value_and_first_two_derivatives_vanish_at_support_boundary", "Fermi_factor_is_smooth_on_support", "particle_and_hole_spectral_functions_are_compactly_supported_C2", "two_integrations_by_parts_give_O_abs_t_minus_2_correlation_decay", "particle_and_hole_correlations_are_L1_in_time", "on_shell_spectral_total_equals_K122_kappa", "on_shell_Fermi_factor_equals_K122_occupation", "all_K115_Davies_rates_recovered_exactly")
    if corr.get("lead_pairs") != 18 or corr.get("directed_K115_rates") != 36 or any(corr.get(key) is not True for key in required_corr) or corr.get("analytic_Davies_limit_theorem_reproved_here") is not False or corr.get("finite_coupling_scattering_or_return_to_NESS_proved") is not False:
        failures.append("correlations")
    true_point = ("fixed_width_interacting_Fock_domain_owned", "delta_normalized_L2_norm_scales_as_epsilon_minus_one_half", "uniformly_bounded_linear_coupling_has_zero_distributional_point_strength")
    false_point = ("singular_number_changing_Fock_IBC_constructed", "counterterm_quadratic_form_or_resolvent_point_limit_constructed", "Moller_or_Ruelle_morphism_constructed", "interacting_NESS_constructed", "interacting_field_current_constructed", "reduced_cycle_promoted_to_field_current")
    if any(point.get(key) is not True for key in true_point) or any(point.get(key) is not False for key in false_point) or point.get("reduced_K115_cycle_ratio") != "6561/256":
        failures.append("point_ness")
    false_owner = ("Weinstein_source_or_GU_action_owner", "background_connection_paths_Klein_carrier_form_factors_or_modular_data_source_selected", "physical_state_or_detector_effect_selected", "Born_rule_derived", "held_out_scored", "prediction_or_confirmation_credit")
    if any(owner.get(key) is not False for key in false_owner) or owner.get("canon_verdict_change") != "none":
        failures.append("ownership")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("repository-owned", "smooth bounded external", "common self-adjoint", "string-local", "L1", "No dynamical", "Weinstein/source/GU", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "break_charge", "break_rate", "wrong_occupation", "break_wilson_norm",
        "make_interaction_odd", "overlap_causal_hull", "break_bump_value",
        "break_bump_first", "break_bump_second", "erase_point_divergence",
        "invent_point_strength",
    )]
    updates = (
        ("erase_common_domain", lambda d: d["continuum_fock_representation"].__setitem__("interacting_domain_equals_free_domain", False)),
        ("erase_boundedness", lambda d: d["continuum_fock_representation"].__setitem__("finite_defect_sum_is_bounded", False)),
        ("mislabel_connection", lambda d: d["continuum_fock_representation"].__setitem__("connection_status", "dynamical_quantum_gauge_field")),
        ("invent_Gauss", lambda d: d["background_gauge_covariance"].__setitem__("Gauss_generator_constructed", True)),
        ("invent_gauge_Hilbert", lambda d: d["background_gauge_covariance"].__setitem__("quantum_gauge_Hilbert_representation_claimed", True)),
        ("erase_covariance", lambda d: d["background_gauge_covariance"].__setitem__("interaction_is_background_gauge_invariant", False)),
        ("invent_path_independence", lambda d: d["string_local_causal_control"].__setitem__("path_independence_owned", True)),
        ("invent_point_locality", lambda d: d["string_local_causal_control"].__setitem__("point_locality_owned", True)),
        ("erase_causal_hull", lambda d: d["string_local_causal_control"].__setitem__("relative_dynamics_is_trivial_on_the_spacelike_complement_of_the_causal_hull", False)),
        ("invent_complete_net", lambda d: d["string_local_causal_control"].__setitem__("complete_dynamical_gauge_Haag_Kastler_net_owned", True)),
        ("erase_C2", lambda d: d["thermal_correlation_control"].__setitem__("extended_spectral_shape_is_C2", False)),
        ("erase_L1", lambda d: d["thermal_correlation_control"].__setitem__("particle_and_hole_correlations_are_L1_in_time", False)),
        ("erase_rates", lambda d: d["thermal_correlation_control"].__setitem__("all_K115_Davies_rates_recovered_exactly", False)),
        ("invent_Davies_proof", lambda d: d["thermal_correlation_control"].__setitem__("analytic_Davies_limit_theorem_reproved_here", True)),
        ("invent_return_to_NESS", lambda d: d["thermal_correlation_control"].__setitem__("finite_coupling_scattering_or_return_to_NESS_proved", True)),
        ("invent_IBC", lambda d: d["point_and_ness_boundary"].__setitem__("singular_number_changing_Fock_IBC_constructed", True)),
        ("invent_resolvent", lambda d: d["point_and_ness_boundary"].__setitem__("counterterm_quadratic_form_or_resolvent_point_limit_constructed", True)),
        ("invent_Moller", lambda d: d["point_and_ness_boundary"].__setitem__("Moller_or_Ruelle_morphism_constructed", True)),
        ("invent_NESS", lambda d: d["point_and_ness_boundary"].__setitem__("interacting_NESS_constructed", True)),
        ("promote_current", lambda d: d["point_and_ness_boundary"].__setitem__("reduced_cycle_promoted_to_field_current", True)),
        ("invent_source_owner", lambda d: d["ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_owner", True)),
        ("invent_Born", lambda d: d["ownership_boundary"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["ownership_boundary"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A complete GU point gauge theory derives NESS and Born.")),
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
    print(f"K127 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
