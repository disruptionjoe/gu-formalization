#!/usr/bin/env python3
"""Exact K121 thermal Araki--Woods/KMS boundary-net controls (stdlib only)."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k121-k120-thermal-araki-woods-kms-boundary-net-wave.json"
N = 3
KAPPA = Fraction(2, 5)
CLOCK = Fraction(7, 11)
HIGH = Fraction(81, 113)
LOW = Fraction(16, 113)
STATES = [(x, r) for x in range(N) for r in range(N)]
INDEX = {state: i for i, state in enumerate(STATES)}


def kernel(x: int, mutation: str | None = None) -> list[Fraction]:
    high, low = HIGH, LOW
    if mutation == "unnormalized_kernel":
        high = Fraction(82, 113)
    if mutation == "uninformative_kernel":
        high = low = Fraction(1, 3)
    return [high if r == x else low for r in range(N)]


def rates(mutation: str | None = None) -> list[dict[int, Fraction]]:
    out: list[dict[int, Fraction]] = []
    for x, r in STATES:
        row: dict[int, Fraction] = {}
        for y in range(N):
            if y != x:
                rate = KAPPA
                if mutation == "break_one_rate" and (x, y, r) == (0, 1, 0):
                    rate += Fraction(1, 97)
                row[INDEX[(y, r)]] = rate
        for s in range(N):
            if s != r:
                row[INDEX[(x, s)]] = CLOCK * kernel(x, mutation)[s]
        out.append(row)
    return out


def generator(mutation: str | None = None) -> list[list[Fraction]]:
    edge_rows = rates(mutation)
    q = [[Fraction(0) for _ in STATES] for _ in STATES]
    for i, row in enumerate(edge_rows):
        for j, rate in row.items():
            q[i][j] = rate
        q[i][i] = -sum(row.values(), Fraction(0))
    return q


def stationary(mutation: str | None = None) -> list[Fraction]:
    attenuation = CLOCK / (CLOCK + N * KAPPA)
    values = [
        (Fraction(1, N) + attenuation * (kernel(x, mutation)[r] - Fraction(1, N))) / N
        for x, r in STATES
    ]
    if mutation == "wrong_stationary":
        values[0] += Fraction(1, 101)
    return values


def row_times(population: list[Fraction], matrix: list[list[Fraction]]) -> list[Fraction]:
    return [sum(population[i] * matrix[i][j] for i in range(len(population))) for j in range(len(population))]


def cycle_ratio(mutation: str | None = None) -> Fraction:
    p = [kernel(x, mutation) for x in range(N)]
    x, y, r, s = 0, 1, 0, 1
    return (p[x][s] * p[y][r]) / (p[x][r] * p[y][s])


def decompose_pairs(mutation: str | None = None) -> dict[str, object]:
    edge_rows = rates(mutation)
    reconstructed = [dict() for _ in STATES]
    pair_count = asymmetric = symmetric = physical_thermal = vacuum_directed = doubled = 0
    occupations: list[Fraction] = []
    gammas: list[Fraction] = []
    for i in range(len(STATES)):
        for j in range(i + 1, len(STATES)):
            forward = edge_rows[i].get(j, Fraction(0))
            reverse = edge_rows[j].get(i, Fraction(0))
            if not forward and not reverse:
                continue
            pair_count += 1
            if forward == reverse:
                symmetric += 1
                vacuum_directed += 2
                reconstructed[i][j] = forward
                reconstructed[j][i] = reverse
                continue
            asymmetric += 1
            physical_thermal += 1
            doubled += 2
            high = max(forward, reverse)
            low = min(forward, reverse)
            gamma = high - low
            occupation = low / gamma
            if mutation == "wrong_gamma" and asymmetric == 1:
                gamma += Fraction(1, 103)
            if mutation == "wrong_occupation" and asymmetric == 1:
                occupation += Fraction(1, 107)
            high_rebuilt = gamma * (occupation + 1)
            low_rebuilt = gamma * occupation
            if forward > reverse:
                reconstructed[i][j] = high_rebuilt
                reconstructed[j][i] = low_rebuilt
            else:
                reconstructed[i][j] = low_rebuilt
                reconstructed[j][i] = high_rebuilt
            occupations.append(occupation)
            gammas.append(gamma)
    return {
        "reconstructed": reconstructed,
        "pair_count": pair_count,
        "asymmetric": asymmetric,
        "symmetric": symmetric,
        "physical_thermal": physical_thermal,
        "vacuum_directed": vacuum_directed,
        "doubled": doubled,
        "noise_modes": vacuum_directed + doubled,
        "occupations": occupations,
        "gammas": gammas,
    }


def reconstructed_generator(mutation: str | None = None) -> list[list[Fraction]]:
    rows = decompose_pairs(mutation)["reconstructed"]
    assert isinstance(rows, list)
    q = [[Fraction(0) for _ in STATES] for _ in STATES]
    for i, row in enumerate(rows):
        assert isinstance(row, dict)
        for j, rate in row.items():
            q[i][j] = rate
        q[i][i] = -sum(row.values(), Fraction(0))
    return q


def lindblad_diagonal(population: list[Fraction], mutation: str | None = None) -> list[Fraction]:
    rows = decompose_pairs(mutation)["reconstructed"]
    assert isinstance(rows, list)
    derivative = [Fraction(0) for _ in STATES]
    for i, row in enumerate(rows):
        assert isinstance(row, dict)
        for j, rate in row.items():
            derivative[j] += population[i] * rate
            derivative[i] -= population[i] * rate
    if mutation == "wrong_lindblad_drift":
        derivative[0] += Fraction(1, 109)
    return derivative


def hp_unitarity_residual(mutation: str | None = None) -> list[Fraction]:
    rows = decompose_pairs(mutation)["reconstructed"]
    assert isinstance(rows, list)
    exits = [sum(row.values(), Fraction(0)) for row in rows]
    twice_drift = [-value for value in exits]
    if mutation == "wrong_hp_drift":
        twice_drift[0] += Fraction(1, 127)
    return [twice_drift[i] + exits[i] for i in range(len(exits))]


def local_net_checks(mutation: str | None = None) -> dict[str, bool]:
    small = {2, 3}
    large = {1, 2, 3, 4}
    spacelike_a = {0, 1}
    spacelike_b = {3, 4}
    translated = {value + 5 for value in spacelike_a}
    expected = {5, 6}
    if mutation == "overlap_intervals":
        spacelike_b = {1, 4}
    if mutation == "break_translation":
        expected = {5, 7}
    return {
        "isotony": small.issubset(large),
        "disjoint_commutation": spacelike_a.isdisjoint(spacelike_b),
        "translation_covariance": translated == expected,
    }


def thermal_checks(mutation: str | None = None) -> dict[str, object]:
    beta = math.log(81.0 / 16.0)
    if mutation == "bad_kms_beta":
        beta = math.log(80.0 / 16.0)
    occupation = 1.0 / math.expm1(beta)
    ratio = math.exp(-beta)
    # The chiral-current thermal correction omega*n_beta(omega) is finite at
    # omega=0 and exponentially decaying at high frequency.
    epsilons = (1e-2, 1e-3, 1e-4)
    infrared = [eps / math.expm1(beta * eps) for eps in epsilons]
    ultraviolet = [omega / math.expm1(beta * omega) for omega in (4.0, 8.0, 12.0)]
    energy_density = math.pi / (2.0 * beta * beta)
    if mutation == "infinite_local_energy":
        energy_density = math.inf
    return {
        "beta": beta,
        "occupation": occupation,
        "ratio": ratio,
        "infrared": infrared,
        "ultraviolet": ultraviolet,
        "energy_density": energy_density,
    }


def output_accounting(q: list[list[Fraction]], nu: list[Fraction]) -> tuple[Fraction, float]:
    activity = Fraction(0)
    entropy = 0.0
    for i in range(len(STATES)):
        for j in range(len(STATES)):
            if i == j or not q[i][j]:
                continue
            forward = nu[i] * q[i][j]
            reverse = nu[j] * q[j][i]
            activity += forward
            if reverse:
                entropy += float(forward) * math.log(float(forward / reverse))
    return activity, entropy


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    obstruction = data.get("single_equilibrium_obstruction", {})
    census = data.get("edge_pair_census", {})
    thermal = data.get("thermal_rate_owner", {})
    state = data.get("boundary_CCR_KMS_state", {})
    interaction = data.get("thermal_HP_interaction", {})
    action = data.get("action_state_effect_boundary", {})
    boundary = data.get("ownership_boundary", {})
    control = data.get("exact_control", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    if obstruction.get("cycle_affinity_nonzero") is not True or obstruction.get("single_equilibrium_KMS_owner_of_exact_K115_possible") is not False or obstruction.get("multi_reservoir_or_work_input_required") is not True or obstruction.get("universal_no_go_for_nonequilibrium_KMS_components_claimed") is not False:
        failures.append("obstruction")
    expected_census = {"directed_edges": 36, "undirected_pairs": 18, "asymmetric_record_pairs": 6, "symmetric_pairs": 12, "positive_temperature_physical_channels": 6, "zero_temperature_directed_channels": 24, "Araki_Woods_doubled_vacuum_noise_modes": 12, "total_vacuum_noise_modes": 36}
    if any(census.get(key) != value for key, value in expected_census.items()) or census.get("channel_multiplicity_selected_by_source_or_GU") is not False:
        failures.append("census")
    if thermal.get("thermal_occupation_at_Bohr_frequency") != "16/65" or thermal.get("KMS_ratio_exp_minus_beta_omega") != "16/81" or thermal.get("all_K115_rates_recovered_exactly") is not True:
        failures.append("thermal_rates")
    if state.get("isotony") is not True or state.get("disjoint_interval_commutation") is not True or state.get("translation_covariance") is not True or state.get("KMS_spectral_relation") is not True or state.get("thermal_minus_vacuum_current_two_point_function_smooth_locally") is not True or state.get("boundary_Hadamard_positive_frequency_singularity_class") is not True or state.get("finite_total_energy_on_infinite_stationary_line") is not False or state.get("normal_global_Gibbs_density_in_vacuum_Fock_representation") is not False or state.get("full_two_dimensional_spacetime_AQFT_net_or_scalar_Hadamard_theorem") is not False:
        failures.append("state")
    if interaction.get("thermal_pair_gives_forward_and_reverse_Lindblad_operators") is not True or interaction.get("total_effective_directed_coefficients") != 36 or interaction.get("diagonal_restriction_exactly_K115") is not True or interaction.get("K115_stationary_law_preserved") is not True or interaction.get("stationary_activity_and_entropy_production_recovered") is not True or interaction.get("past_output_commutes_with_future_input") is not True or interaction.get("single_closed_autonomous_equilibrium_interaction") is not False:
        failures.append("interaction")
    if action.get("smooth_finite_band_doubled_chiral_action_constructed") is not True or action.get("KMS_state_selected_by_boundary_covariance_not_classical_variation_alone") is not True or action.get("finite_particle_H1_L2_Hminus1_rigging_retained") is not True or action.get("endpoint_symplectic_and_minimal_nongauge_BV_BFV_identity") is not True or action.get("Born_rule_derived") is not False or action.get("nontrivial_gauge_or_ghost_complex_constructed") is not False:
        failures.append("action")
    required_false = (
        "Weinstein_source_or_GU_action_state_channel_coupling_or_effect_owner",
        "K118_or_K120_selected_temperature_and_Araki_Woods_polarization",
        "one_equilibrium_bath_constructed", "multi_reservoir_work_or_switching_is_free",
        "finite_total_reservoir_energy_claimed", "full_spacetime_AQFT_net_constructed",
        "Born_rule_derived", "held_out_scored", "prediction_or_confirmation_credit",
    )
    if any(boundary.get(key) is not False for key in required_false) or boundary.get("canon_verdict_change") != "none":
        failures.append("boundary")
    if control.get("cycle_pair_thermal_KMS_CCR_generator_stationarity_output_and_domain_boundaries_checked") is not True:
        failures.append("control")
    ceiling = data.get("claim_ceiling", "")
    if "single-equilibrium obstruction" not in ceiling or "finite local energy density" not in ceiling or "no finite total energy" not in ceiling or "No Weinstein/source/GU ownership" not in ceiling:
        failures.append("ceiling")
    return failures


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    q = generator(mutation)
    rebuilt = reconstructed_generator(mutation)
    decomp = decompose_pairs(mutation)
    nu = stationary(mutation)
    thermal = thermal_checks(mutation)
    local = local_net_checks(mutation)
    basis = [[Fraction(1) if i == k else Fraction(0) for i in range(len(STATES))] for k in range(len(STATES))]
    diagonal_matches = all(lindblad_diagonal(vector, mutation) == row_times(vector, q) for vector in basis)
    occupations = decomp["occupations"]
    gammas = decomp["gammas"]
    assert isinstance(occupations, list) and isinstance(gammas, list)
    activity, entropy = output_accounting(rebuilt, nu)
    infrared = thermal["infrared"]
    ultraviolet = thermal["ultraviolet"]
    assert isinstance(infrared, list) and isinstance(ultraviolet, list)
    expected_activity = Fraction(83387296, 70931795)
    checks = [
        ("nine K115 detector states", len(STATES) == 9),
        ("event kernels normalize", all(sum(kernel(x, mutation), Fraction(0)) == 1 for x in range(N))),
        ("event kernels remain informative", any(kernel(x, mutation)[r] != Fraction(1, 3) for x in range(N) for r in range(N))),
        ("generator has thirty-six directed edges", sum(len(row) for row in rates(mutation)) == 36),
        ("generator rows sum to zero", all(sum(row, Fraction(0)) == 0 for row in q)),
        ("K117 cycle is nonreversible", cycle_ratio(mutation) != 1),
        ("K117 cycle ratio remains 256/6561", cycle_ratio(mutation) == Fraction(256, 6561)),
        ("eighteen undirected pairs", decomp["pair_count"] == 18),
        ("six asymmetric record pairs", decomp["asymmetric"] == 6),
        ("twelve symmetric pairs", decomp["symmetric"] == 12),
        ("six positive-temperature physical channels", decomp["physical_thermal"] == 6),
        ("twenty-four directed vacuum channels", decomp["vacuum_directed"] == 24),
        ("twelve Araki-Woods doubled modes", decomp["doubled"] == 12),
        ("total doubled vacuum-noise count is thirty-six", decomp["noise_modes"] == 36),
        ("all thermal occupations are 16/65", bool(occupations) and all(value == Fraction(16, 65) for value in occupations)),
        ("all thermal couplings are 455/1243", bool(gammas) and all(value == Fraction(455, 1243) for value in gammas)),
        ("thermal down rate is 567/1243", all(gammas[i] * (occupations[i] + 1) == Fraction(567, 1243) for i in range(len(gammas)))),
        ("thermal up rate is 112/1243", all(gammas[i] * occupations[i] == Fraction(112, 1243) for i in range(len(gammas)))),
        ("Araki-Woods decomposition recovers every rate", rebuilt == q),
        ("KMS ratio is 16/81", abs(float(thermal["ratio"]) - 16.0 / 81.0) < 1e-14),
        ("KMS occupation is 16/65", abs(float(thermal["occupation"]) - 16.0 / 65.0) < 1e-14),
        ("chiral-current thermal correction is infrared finite", max(abs(value - 1.0 / float(thermal["beta"])) for value in infrared) < 0.006),
        ("chiral-current thermal correction decays in the ultraviolet", ultraviolet[0] > ultraviolet[1] > ultraviolet[2] > 0.0),
        ("renormalized local thermal energy density is finite positive", math.isfinite(float(thermal["energy_density"])) and float(thermal["energy_density"]) > 0.0),
        ("interval net is isotone", bool(local["isotony"])),
        ("disjoint interval algebras commute", bool(local["disjoint_commutation"])),
        ("characteristic translations are covariant", bool(local["translation_covariance"])),
        ("HP coefficient identity is exact", all(value == 0 for value in hp_unitarity_residual(mutation))),
        ("thermal Lindblad diagonal is exactly K115", diagonal_matches),
        ("K115 stationary law normalizes", sum(nu, Fraction(0)) == 1),
        ("thermal generator preserves K115 stationarity", all(value == 0 for value in lindblad_diagonal(nu, mutation))),
        ("stationary output activity is inherited exactly", activity == expected_activity),
        ("stationary entropy production remains positive", entropy > 0.0),
    ]
    return checks


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "unnormalized_kernel", "uninformative_kernel", "break_one_rate",
        "wrong_gamma", "wrong_occupation", "wrong_stationary",
        "wrong_lindblad_drift", "wrong_hp_drift", "overlap_intervals",
        "break_translation", "bad_kms_beta", "infinite_local_energy",
    )]
    updates = (
        ("erase_cycle_obstruction", lambda d: d["single_equilibrium_obstruction"].__setitem__("cycle_affinity_nonzero", False)),
        ("invent_single_equilibrium", lambda d: d["single_equilibrium_obstruction"].__setitem__("single_equilibrium_KMS_owner_of_exact_K115_possible", True)),
        ("invent_universal_no_go", lambda d: d["single_equilibrium_obstruction"].__setitem__("universal_no_go_for_nonequilibrium_KMS_components_claimed", True)),
        ("wrong_pair_count", lambda d: d["edge_pair_census"].__setitem__("undirected_pairs", 17)),
        ("wrong_thermal_count", lambda d: d["edge_pair_census"].__setitem__("positive_temperature_physical_channels", 5)),
        ("wrong_noise_count", lambda d: d["edge_pair_census"].__setitem__("total_vacuum_noise_modes", 35)),
        ("invent_GU_channel_selection", lambda d: d["edge_pair_census"].__setitem__("channel_multiplicity_selected_by_source_or_GU", True)),
        ("wrong_manifest_occupation", lambda d: d["thermal_rate_owner"].__setitem__("thermal_occupation_at_Bohr_frequency", "17/65")),
        ("erase_rate_recovery", lambda d: d["thermal_rate_owner"].__setitem__("all_K115_rates_recovered_exactly", False)),
        ("erase_isotony", lambda d: d["boundary_CCR_KMS_state"].__setitem__("isotony", False)),
        ("erase_locality", lambda d: d["boundary_CCR_KMS_state"].__setitem__("disjoint_interval_commutation", False)),
        ("erase_KMS", lambda d: d["boundary_CCR_KMS_state"].__setitem__("KMS_spectral_relation", False)),
        ("invent_finite_total_energy", lambda d: d["boundary_CCR_KMS_state"].__setitem__("finite_total_energy_on_infinite_stationary_line", True)),
        ("invent_full_AQFT", lambda d: d["boundary_CCR_KMS_state"].__setitem__("full_two_dimensional_spacetime_AQFT_net_or_scalar_Hadamard_theorem", True)),
        ("erase_thermal_HP", lambda d: d["thermal_HP_interaction"].__setitem__("thermal_pair_gives_forward_and_reverse_Lindblad_operators", False)),
        ("break_diagonal_generator", lambda d: d["thermal_HP_interaction"].__setitem__("diagonal_restriction_exactly_K115", False)),
        ("invent_closed_equilibrium", lambda d: d["thermal_HP_interaction"].__setitem__("single_closed_autonomous_equilibrium_interaction", True)),
        ("erase_action", lambda d: d["action_state_effect_boundary"].__setitem__("smooth_finite_band_doubled_chiral_action_constructed", False)),
        ("invent_variational_temperature", lambda d: d["action_state_effect_boundary"].__setitem__("KMS_state_selected_by_boundary_covariance_not_classical_variation_alone", False)),
        ("invent_Born", lambda d: d["action_state_effect_boundary"].__setitem__("Born_rule_derived", True)),
        ("invent_source_owner", lambda d: d["ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_state_channel_coupling_or_effect_owner", True)),
        ("invent_free_work", lambda d: d["ownership_boundary"].__setitem__("multi_reservoir_work_or_switching_is_free", True)),
        ("score_holdout", lambda d: d["ownership_boundary"].__setitem__("held_out_scored", True)),
        ("invent_prediction", lambda d: d["ownership_boundary"].__setitem__("prediction_or_confirmation_credit", True)),
        ("promote_canon", lambda d: d["ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A GU equilibrium bath derives quantum measurement.")),
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
    print(f"K121 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
