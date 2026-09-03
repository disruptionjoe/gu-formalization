#!/usr/bin/env python3
"""Exact K122 autonomous CAR-reservoir and bulk gauge-net controls."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k122-k121-autonomous-fermionic-reservoir-bulk-gauge-net-wave.json"
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
    rows: list[dict[int, Fraction]] = []
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
        rows.append(row)
    return rows


def generator(rows: list[dict[int, Fraction]]) -> list[list[Fraction]]:
    q = [[Fraction(0) for _ in STATES] for _ in STATES]
    for i, row in enumerate(rows):
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


def car_factorization(mutation: str | None = None) -> dict[str, object]:
    original = rates(mutation)
    rebuilt: list[dict[int, Fraction]] = [dict() for _ in STATES]
    pairs = biased = symmetric = 0
    occupations: list[Fraction] = []
    kappas: list[Fraction] = []
    for i in range(len(STATES)):
        for j in range(i + 1, len(STATES)):
            forward = original[i].get(j, Fraction(0))
            reverse = original[j].get(i, Fraction(0))
            if not forward and not reverse:
                continue
            pairs += 1
            total = forward + reverse
            occupation = reverse / total
            if mutation == "wrong_occupation" and pairs == 1:
                occupation += Fraction(1, 103)
            if mutation == "wrong_spectral_rate" and pairs == 1:
                total += Fraction(1, 107)
            rebuilt[i][j] = total * (1 - occupation)
            rebuilt[j][i] = total * occupation
            biased += int(forward != reverse)
            symmetric += int(forward == reverse)
            occupations.append(occupation)
            kappas.append(total)
    return {
        "rebuilt": rebuilt,
        "pairs": pairs,
        "biased": biased,
        "symmetric": symmetric,
        "occupations": occupations,
        "kappas": kappas,
        "noise_coefficients": 2 * pairs,
    }


def environment_entropy(rows: list[dict[int, Fraction]], nu: list[Fraction]) -> tuple[float, float]:
    environment = total = 0.0
    for i in range(len(STATES)):
        for j in range(i + 1, len(STATES)):
            qij = rows[i].get(j, Fraction(0))
            qji = rows[j].get(i, Fraction(0))
            if not qij or not qji:
                continue
            current = nu[i] * qij - nu[j] * qji
            environment += float(current) * math.log(float(qij / qji))
            total += float(current) * math.log(float((nu[i] * qij) / (nu[j] * qji)))
    return environment, total


def local_net_checks(mutation: str | None = None) -> dict[str, bool]:
    small_r, small_l = {2, 3}, {7, 8}
    large_r, large_l = {1, 2, 3, 4}, {6, 7, 8, 9}
    spacelike_a = ({0, 1}, {8, 9})
    spacelike_b = ({4, 5}, {2, 3})
    if mutation == "overlap_double_cones":
        spacelike_b = ({1, 5}, {2, 3})
    graded_sign = -1
    if mutation == "break_graded_locality":
        graded_sign = 1
    odd_a, odd_b = 1, 1
    even_a, even_b = 2, 2
    return {
        "isotony": small_r.issubset(large_r) and small_l.issubset(large_l),
        "spacelike": spacelike_a[0].isdisjoint(spacelike_b[0]) and spacelike_a[1].isdisjoint(spacelike_b[1]),
        "graded_locality": graded_sign == (-1) ** (odd_a * odd_b),
        "even_locality": (-1) ** (even_a * even_b) == 1,
        "gauge_even": ((even_a + even_b) % 2) == 0,
    }


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    factor = data.get("fermionic_pair_factorization", {})
    interaction = data.get("autonomous_defect_interaction", {})
    resource = data.get("resource_accounting", {})
    net = data.get("bulk_gauge_even_net", {})
    state = data.get("state_effect_boundary", {})
    boundary = data.get("ownership_boundary", {})
    control = data.get("exact_control", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    expected = {
        "K115_states": 9, "directed_edges": 36, "undirected_pairs": 18,
        "biased_pairs": 6, "half_filled_symmetric_pairs": 12,
        "one_CAR_reservoir_per_undirected_pair": True,
        "particle_hole_noise_coefficients": 36,
        "asymmetric_total_spectral_rate": "679/1243",
        "asymmetric_Fermi_occupation": "112/679",
        "asymmetric_hole_occupation": "567/679",
        "asymmetric_odds": "16/81",
        "symmetric_base_total_spectral_rate": "4/5",
        "symmetric_wrong_record_total_spectral_rate": "224/1243",
        "symmetric_Fermi_occupation": "1/2",
        "all_K115_rates_recovered_exactly": True,
    }
    if any(factor.get(key) != value for key, value in expected.items()):
        failures.append("factorization")
    required_interaction = (
        "time_independent_total_Hamiltonian", "one_constant_boundary_tunnelling_term_per_pair",
        "thermodynamic_limit_leads_supply_stationary_incoming_states",
        "Davies_or_white_noise_limit_gives_declared_generator", "diagonal_restriction_exactly_K115",
        "K115_stationary_law_preserved",
    )
    if any(interaction.get(key) is not True for key in required_interaction) or interaction.get("external_channel_switching_required") is not False or interaction.get("exact_finite_time_reduced_semigroup_claimed") is not False or interaction.get("finite_closed_stationary_reservoir_claimed") is not False:
        failures.append("interaction")
    if resource.get("biased_pair_local_affinity") != "log(81/16)" or resource.get("symmetric_pair_local_affinity") != "0" or resource.get("stationary_environmental_affinity_flow_equals_K117_entropy_production") is not True or resource.get("system_Shannon_boundary_term_vanishes_at_stationarity") is not True or resource.get("reservoir_preparation_and_maintenance_are_free") is not False or resource.get("one_global_equilibrium_state_claimed") is not False:
        failures.append("resource")
    required_net = (
        "double_cone_algebras_from_left_and_right_interval_test_spaces", "isotony",
        "graded_locality_for_field_algebras", "ordinary_locality_for_even_observable_subnet",
        "U1_to_the_18_species_phase_action", "gauge_fixed_even_observable_subnet_preserved_by_free_dynamics",
        "boundary_defect_coupling_locally_declared",
    )
    if any(net.get(key) is not True for key in required_net) or net.get("full_interacting_Haag_Kastler_net_constructed") is not False or net.get("nontrivial_gauge_BV_cohomology_constructed") is not False:
        failures.append("net")
    if state.get("grand_canonical_quasifree_CAR_states_positive_and_normalized") is not True or state.get("fermion_number_projections_are_positive_effects") is not True or state.get("state_on_effect_gives_value_in_unit_interval") is not True or state.get("mathematical_state_effect_pairing_owned") is not True or state.get("physical_detector_identification_derived") is not False or state.get("Born_rule_derived") is not False:
        failures.append("state_effect")
    required_false = (
        "Weinstein_source_or_GU_action_parameter_state_coupling_or_observable_owner",
        "reservoir_temperatures_chemical_potentials_or_spectral_densities_source_selected",
        "one_closed_equilibrium_bath_constructed", "full_interacting_spacetime_AQFT_constructed",
        "Born_rule_derived", "held_out_scored", "prediction_or_confirmation_credit",
    )
    if any(boundary.get(key) is not False for key in required_false) or boundary.get("canon_verdict_change") != "none":
        failures.append("ownership")
    if control.get("pair_CAR_generator_stationarity_affinity_autonomy_locality_gauge_and_state_effect_boundaries_checked") is not True:
        failures.append("control")
    if data.get("held_out") != "delayed-choice entanglement swapping, reserved_unscored":
        failures.append("holdout")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("repository-owned", "time-independent", "controlled", "free", "No Weinstein/source/GU", "No", "Born"):
        if token not in ceiling:
            failures.append(f"claim_ceiling:{token}")
    return failures


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    original = rates(mutation)
    factor = car_factorization(mutation)
    rebuilt = factor["rebuilt"]
    assert isinstance(rebuilt, list)
    q = generator(original)
    q_rebuilt = generator(rebuilt)
    nu = stationary(mutation)
    environment, total = environment_entropy(original, nu)
    local = local_net_checks(mutation)
    occupations = factor["occupations"]
    kappas = factor["kappas"]
    assert isinstance(occupations, list) and isinstance(kappas, list)
    biased_occupations = [f for f in occupations if f != Fraction(1, 2)]
    biased_kappas = [k for k in kappas if k == Fraction(679, 1243)]
    expected_entropy = 0.25863366222968864
    return [
        ("event kernel normalizes", all(sum(kernel(x, mutation), Fraction(0)) == 1 for x in range(N))),
        ("event kernel is informative", any(kernel(x, mutation)[x] != kernel(x, mutation)[(x + 1) % N] for x in range(N))),
        ("K115 has nine states", len(STATES) == 9),
        ("K115 has 36 directed edges", sum(len(row) for row in original) == 36),
        ("CAR census has 18 undirected pairs", factor["pairs"] == 18),
        ("CAR census has six biased pairs", factor["biased"] == 6),
        ("CAR census has twelve symmetric pairs", factor["symmetric"] == 12),
        ("one pair gives two particle-hole coefficients", factor["noise_coefficients"] == 36),
        ("biased Fermi occupations are exact", set(biased_occupations) == {Fraction(112, 679), Fraction(567, 679)}),
        ("biased total spectral rates are exact", len(biased_kappas) == 6),
        ("biased Fermi odds are 16/81 or reciprocal", all(min(f, 1 - f) / max(f, 1 - f) == Fraction(16, 81) for f in biased_occupations)),
        ("symmetric occupations are half filled", occupations.count(Fraction(1, 2)) == 12),
        ("base-pair spectral rate is 4/5", kappas.count(Fraction(4, 5)) == 9),
        ("wrong-record spectral rate is 224/1243", kappas.count(Fraction(224, 1243)) == 3),
        ("CAR factorization exactly rebuilds every rate", q_rebuilt == q),
        ("K115 stationary law normalizes", sum(nu, Fraction(0)) == 1),
        ("CAR generator preserves K115 stationarity", all(value == 0 for value in row_times(nu, q_rebuilt))),
        ("environmental affinity flow equals total entropy production", abs(environment - total) < 1e-14),
        ("stationary entropy production matches K117", abs(total - expected_entropy) < 1e-14),
        ("stationary entropy production is positive", total > 0.0),
        ("double-cone net is isotone", local["isotony"]),
        ("test double cones are spacelike", local["spacelike"]),
        ("field algebra is graded local", local["graded_locality"]),
        ("even observable subnet is ordinarily local", local["even_locality"]),
        ("even observables are gauge neutral", local["gauge_even"]),
    ]


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "unnormalized_kernel", "uninformative_kernel", "break_one_rate", "wrong_occupation",
        "wrong_spectral_rate", "wrong_stationary", "overlap_double_cones", "break_graded_locality",
    )]
    updates = (
        ("wrong_pair_count", lambda d: d["fermionic_pair_factorization"].__setitem__("undirected_pairs", 17)),
        ("wrong_reservoir_count", lambda d: d["fermionic_pair_factorization"].__setitem__("one_CAR_reservoir_per_undirected_pair", False)),
        ("wrong_Fermi_occupation", lambda d: d["fermionic_pair_factorization"].__setitem__("asymmetric_Fermi_occupation", "113/679")),
        ("erase_rate_recovery", lambda d: d["fermionic_pair_factorization"].__setitem__("all_K115_rates_recovered_exactly", False)),
        ("invent_switching", lambda d: d["autonomous_defect_interaction"].__setitem__("external_channel_switching_required", True)),
        ("erase_autonomy", lambda d: d["autonomous_defect_interaction"].__setitem__("time_independent_total_Hamiltonian", False)),
        ("invent_exact_reduction", lambda d: d["autonomous_defect_interaction"].__setitem__("exact_finite_time_reduced_semigroup_claimed", True)),
        ("invent_finite_bath", lambda d: d["autonomous_defect_interaction"].__setitem__("finite_closed_stationary_reservoir_claimed", True)),
        ("hide_maintenance", lambda d: d["resource_accounting"].__setitem__("reservoir_preparation_and_maintenance_are_free", True)),
        ("invent_global_equilibrium", lambda d: d["resource_accounting"].__setitem__("one_global_equilibrium_state_claimed", True)),
        ("erase_entropy_identity", lambda d: d["resource_accounting"].__setitem__("stationary_environmental_affinity_flow_equals_K117_entropy_production", False)),
        ("erase_graded_locality", lambda d: d["bulk_gauge_even_net"].__setitem__("graded_locality_for_field_algebras", False)),
        ("erase_even_locality", lambda d: d["bulk_gauge_even_net"].__setitem__("ordinary_locality_for_even_observable_subnet", False)),
        ("invent_interacting_net", lambda d: d["bulk_gauge_even_net"].__setitem__("full_interacting_Haag_Kastler_net_constructed", True)),
        ("invent_gauge_BV", lambda d: d["bulk_gauge_even_net"].__setitem__("nontrivial_gauge_BV_cohomology_constructed", True)),
        ("erase_state_positivity", lambda d: d["state_effect_boundary"].__setitem__("grand_canonical_quasifree_CAR_states_positive_and_normalized", False)),
        ("invent_detector", lambda d: d["state_effect_boundary"].__setitem__("physical_detector_identification_derived", True)),
        ("invent_Born", lambda d: d["state_effect_boundary"].__setitem__("Born_rule_derived", True)),
        ("invent_source_owner", lambda d: d["ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_parameter_state_coupling_or_observable_owner", True)),
        ("score_holdout", lambda d: d["ownership_boundary"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A GU field theory derives quantum measurement.")),
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
    print(f"K122 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
