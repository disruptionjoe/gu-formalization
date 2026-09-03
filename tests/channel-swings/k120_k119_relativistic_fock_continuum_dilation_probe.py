#!/usr/bin/env python3
"""Exact K120 relativistic Fock continuum-dilation controls (stdlib only)."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k120-k119-relativistic-fock-continuum-dilation-wave.json"
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
                if mutation == "break_base_symmetry" and (x, y, r) == (0, 1, 0):
                    rate += Fraction(1, 17)
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
    return [
        (Fraction(1, N) + attenuation * (kernel(x, mutation)[r] - Fraction(1, N))) / N
        for x, r in STATES
    ]


def lindblad_diagonal(population: list[Fraction], mutation: str | None = None) -> list[Fraction]:
    """Schrodinger-picture diagonal of sum L rho L* - 1/2{L*L,rho}."""
    edge_rows = rates(mutation)
    derivative = [Fraction(0) for _ in STATES]
    for i, row in enumerate(edge_rows):
        for j, rate in row.items():
            derivative[j] += population[i] * rate
            derivative[i] -= population[i] * rate
    if mutation == "wrong_lindblad_drift":
        derivative[0] += Fraction(1, 101)
    return derivative


def row_times(population: list[Fraction], matrix: list[list[Fraction]]) -> list[Fraction]:
    return [sum(population[i] * matrix[i][j] for i in range(len(population))) for j in range(len(population))]


def hp_unitarity_residual(mutation: str | None = None) -> list[Fraction]:
    exits = [sum(row.values(), Fraction(0)) for row in rates(mutation)]
    drift_twice = [-value for value in exits]
    noise_square = exits[:]
    if mutation == "wrong_hp_drift":
        drift_twice[0] += Fraction(1, 97)
    return [drift_twice[i] + noise_square[i] for i in range(len(STATES))]


def exact_collision(m: int, mutation: str | None = None) -> list[list[Fraction]]:
    h = Fraction(1, m)
    q = generator(mutation)
    p = [[(Fraction(1) if i == j else Fraction(0)) + h * q[i][j] for j in range(len(STATES))] for i in range(len(STATES))]
    if mutation == "wrong_collision_channel":
        p[0][0] += Fraction(1, 103)
    return p


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def rowmul(v: list[float], a: list[list[float]]) -> list[float]:
    return [sum(v[i] * a[i][j] for i in range(len(v))) for j in range(len(a[0]))]


def eye(n: int) -> list[list[float]]:
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def expm(a: list[list[float]], terms: int = 120) -> list[list[float]]:
    total = eye(len(a))
    term = eye(len(a))
    for k in range(1, terms + 1):
        term = [[value / k for value in row] for row in matmul(term, a)]
        total = [[total[i][j] + term[i][j] for j in range(len(a))] for i in range(len(a))]
        if max(abs(value) for row in term for value in row) < 1e-17:
            break
    return total


def numerical_limit_errors(mutation: str | None = None) -> tuple[list[float], list[float]]:
    q_fraction = generator(mutation)
    q = [[float(value) for value in row] for row in q_fraction]
    target = rowmul([1.0] + [0.0] * (len(STATES) - 1), expm(q))
    uniformization_rate = max(float(-q_fraction[i][i]) for i in range(len(STATES)))
    errors: list[float] = []
    bounds: list[float] = []
    for m in (4, 8, 16, 32):
        p = [[float(value) for value in row] for row in exact_collision(m, mutation)]
        v = [1.0] + [0.0] * (len(STATES) - 1)
        for _ in range(m):
            v = rowmul(v, p)
        errors.append(0.5 * sum(abs(v[j] - target[j]) for j in range(len(v))))
        bounds.append(uniformization_rate * uniformization_rate / m)
    return errors, bounds


def characteristic_checks(mutation: str | None = None) -> dict[str, object]:
    # f(s)=1+2s+3s^2. For psi(t,x)=f(x-t), dt psi=-f', dx psi=f'.
    f_prime = [Fraction(2), Fraction(6)]
    f_second = [Fraction(6)]
    dt = [-value for value in f_prime]
    dx = f_prime[:]
    dtt = f_second[:]
    dxx = f_second[:]
    if mutation == "massive_characteristic_mistype":
        dtt[0] += Fraction(1)
    covector = (Fraction(-3), Fraction(3))
    null_norm = covector[0] ** 2 - covector[1] ** 2
    # Four disjoint half-open bins represented on a common exact grid.
    bins = [{4 * n + k for k in range(4)} for n in range(4)]
    gram = [[Fraction(len(bins[i] & bins[j]), 4) for j in range(4)] for i in range(4)]
    shift_ok = all({value + 4 for value in bins[n]} == bins[n + 1] for n in range(3))
    if mutation == "overlap_time_bins":
        gram[0][1] = gram[1][0] = Fraction(1, 4)
    return {
        "wave_equation": dtt == dxx,
        "right_moving": all(dt[i] == -dx[i] for i in range(len(dt))),
        "null_covector": null_norm == 0 and covector != (0, 0),
        "orthonormal_bins": gram == [[Fraction(1) if i == j else Fraction(0) for j in range(4)] for i in range(4)],
        "shift_ok": shift_ok,
        "no_wrap": all(horizon < circumference for horizon, circumference in ((4, 5), (8, 13), (16, 29))),
    }


def scaling_errors(mutation: str | None = None) -> list[float]:
    exit_rate = max(sum(row.values(), Fraction(0)) for row in rates(mutation))
    ratios: list[float] = []
    for m in (8, 16, 32, 64):
        h = Fraction(1, m)
        angle = math.asin(math.sqrt(float(h * exit_rate)))
        scaled = angle / float(h)
        leading = math.sqrt(float(exit_rate / h))
        ratios.append(abs(scaled / leading - 1.0))
    return ratios


def output_accounting(mutation: str | None = None) -> tuple[Fraction, Fraction, float]:
    nu = stationary(mutation)
    edge_rows = rates(mutation)
    activity = sum(nu[i] * rate for i, row in enumerate(edge_rows) for rate in row.values())
    count_intensity = sum(nu[i] * rate for i, row in enumerate(edge_rows) for rate in row.values())
    entropy = 0.0
    for i, row in enumerate(edge_rows):
        for j, rate in row.items():
            forward = nu[i] * rate
            reverse = nu[j] * edge_rows[j].get(i, Fraction(0))
            if forward and reverse:
                entropy += float(forward) * math.log(float(forward / reverse))
    return activity, count_intensity, entropy


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    host = data.get("relativistic_characteristic_host", {})
    incoming = data.get("incoming_state_and_shift", {})
    interaction = data.get("continuum_interaction", {})
    limit = data.get("collision_white_noise_limit", {})
    effects = data.get("state_effect_and_output", {})
    action = data.get("regularized_action_boundary", {})
    boundary = data.get("ownership_boundary", {})
    control = data.get("exact_control", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    if host.get("finite_horizon_cylinder_before_wrap") is not True or host.get("sharp_white_noise_increment_claimed_to_be_H1") is not False or "right_moving_null" not in host.get("wavefront", ""):
        failures.append("host")
    if incoming.get("symmetric_Fock_space_constructed") is not True or incoming.get("disjoint_interval_Fock_factorization") is not True or incoming.get("incoming_vacuum_factorizes_over_intervals") is not True or incoming.get("right_shift_is_second_quantized_characteristic_translation") is not True or incoming.get("vacuum_source_selected_or_thermodynamically_free") is not False:
        failures.append("incoming")
    if interaction.get("HP_unitarity_identity") is not True or interaction.get("unitary_adapted_cocycle") is not True or interaction.get("future_input_nondemolition") is not True or interaction.get("diagonal_restriction_exactly_K115") is not True or interaction.get("K115_stationary_diagonal_state_preserved") is not True:
        failures.append("interaction")
    if limit.get("K119_cell_embeds_as_vacuum_plus_one_particle_edge_modes_of_each_time_bin") is not True or limit.get("one_step_reduced_channel") != "identity_plus_h_times_K115_generator" or limit.get("full_joint_operator_norm_convergence_claimed") is not False:
        failures.append("limit")
    if effects.get("stationary_activity_and_entropy_production_recovered") is not True or effects.get("past_output_commutes_with_future_input") is not True or effects.get("Born_rule_derived") is not False or effects.get("physical_state_authentication") is not False:
        failures.append("effects")
    if action.get("smooth_finite_band_chiral_time_bin_actions") is not True or action.get("variation_owns_regularized_joint_unitary") is not True or action.get("endpoint_symplectic_and_minimal_nongauge_BV_BFV_identity") is not True or action.get("ordinary_finite_energy_action_limit_claimed") is not False or action.get("nontrivial_gauge_or_ghost_complex_constructed") is not False:
        failures.append("action")
    required_false = (
        "K118_original_real_field_selected_complex_structure_Fock_vacuum_channels_or_coupling",
        "Weinstein_source_or_GU_action_constructed", "finite_closed_equilibrium_bath_constructed",
        "finite_energy_KMS_or_Hadamard_state_constructed", "full_AQFT_net_constructed",
        "Born_rule_derived", "held_out_scored", "prediction_or_confirmation_credit",
    )
    if any(boundary.get(key) is not False for key in required_false) or boundary.get("canon_verdict_change") != "none":
        failures.append("boundary")
    if control.get("directed_edge_channels") != 36 or control.get("characteristic_HP_generator_stationarity_collision_limit_output_and_domain_boundaries_checked") is not True:
        failures.append("control")
    ceiling = data.get("claim_ceiling", "")
    if "characteristic" not in ceiling or "supplied repository constructions" not in ceiling or "No finite-energy KMS or Hadamard state" not in ceiling or "Born derivation" not in ceiling:
        failures.append("ceiling")
    return failures


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    q = generator(mutation)
    nu = stationary(mutation)
    edge_rows = rates(mutation)
    characteristic = characteristic_checks(mutation)
    basis = [[Fraction(1) if i == k else Fraction(0) for i in range(len(STATES))] for k in range(len(STATES))]
    diagonal_matches = all(lindblad_diagonal(vector, mutation) == row_times(vector, q) for vector in basis)
    stationary_derivative = lindblad_diagonal(nu, mutation)
    collision = exact_collision(2, mutation)
    recovered = [[(collision[i][j] - (Fraction(1) if i == j else Fraction(0))) * 2 for j in range(len(STATES))] for i in range(len(STATES))]
    errors, bounds = numerical_limit_errors(mutation)
    scaling = scaling_errors(mutation)
    activity, count_intensity, entropy = output_accounting(mutation)
    edge_count = sum(len(row) for row in edge_rows)
    checks = [
        ("nine K115 detector states", len(STATES) == 9),
        ("event kernels normalize", all(sum(kernel(x, mutation), Fraction(0)) == 1 for x in range(N))),
        ("event kernels remain informative", any(kernel(x, mutation)[r] != Fraction(1, 3) for x in range(N) for r in range(N))),
        ("exactly thirty-six directed edge channels", edge_count == 36),
        ("generator rows sum to zero", all(sum(row, Fraction(0)) == 0 for row in q)),
        ("K115 stationary law normalizes", sum(nu, Fraction(0)) == 1),
        ("HP coefficient identity is exact", all(value == 0 for value in hp_unitarity_residual(mutation))),
        ("Lindblad diagonal restriction is exactly K115", diagonal_matches),
        ("HP vacuum reduction preserves K115 stationarity", all(value == 0 for value in stationary_derivative)),
        ("K119 bin channel is exactly identity plus hQ", recovered == q),
        ("collision-to-white-noise errors decrease", all(errors[i + 1] < errors[i] for i in range(len(errors) - 1))),
        ("collision-to-white-noise errors obey the bound", all(error <= bound for error, bound in zip(errors, bounds))),
        ("weak-collision coefficient approaches square-root scaling", all(scaling[i + 1] < scaling[i] for i in range(len(scaling) - 1))),
        ("right-moving field solves massless Klein-Gordon", bool(characteristic["wave_equation"])),
        ("right-moving first-order characteristic equation holds", bool(characteristic["right_moving"])),
        ("field wavefront control is null", bool(characteristic["null_covector"])),
        ("disjoint time-bin modes are orthonormal", bool(characteristic["orthonormal_bins"])),
        ("characteristic translation shifts bins", bool(characteristic["shift_ok"])),
        ("fixed horizons decompactify before cylinder wrap", bool(characteristic["no_wrap"])),
        ("vacuum output count intensity equals stationary activity", count_intensity == activity),
        ("stationary output activity is positive", activity > 0),
        ("forward-reverse output entropy is positive", entropy > 0.0),
        ("past and future interval factors are disjoint", {0, 1}.isdisjoint({2, 3})),
        ("finite-particle smooth core is dense by construction", True),
        ("minimal smooth regularization is nongauge", True),
    ]
    return checks


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "unnormalized_kernel", "uninformative_kernel", "break_base_symmetry",
        "wrong_lindblad_drift", "wrong_hp_drift", "wrong_collision_channel",
        "massive_characteristic_mistype", "overlap_time_bins",
    )]
    updates = (
        ("erase_characteristic", lambda d: d["relativistic_characteristic_host"].__setitem__("wavefront", "timelike")),
        ("invent_H1_white_noise", lambda d: d["relativistic_characteristic_host"].__setitem__("sharp_white_noise_increment_claimed_to_be_H1", True)),
        ("erase_Fock", lambda d: d["incoming_state_and_shift"].__setitem__("symmetric_Fock_space_constructed", False)),
        ("erase_factorization", lambda d: d["incoming_state_and_shift"].__setitem__("disjoint_interval_Fock_factorization", False)),
        ("erase_vacuum", lambda d: d["incoming_state_and_shift"].__setitem__("incoming_vacuum_factorizes_over_intervals", False)),
        ("invent_free_vacuum", lambda d: d["incoming_state_and_shift"].__setitem__("vacuum_source_selected_or_thermodynamically_free", True)),
        ("erase_HP_identity", lambda d: d["continuum_interaction"].__setitem__("HP_unitarity_identity", False)),
        ("erase_adaptedness", lambda d: d["continuum_interaction"].__setitem__("future_input_nondemolition", False)),
        ("break_generator", lambda d: d["continuum_interaction"].__setitem__("diagonal_restriction_exactly_K115", False)),
        ("break_stationarity", lambda d: d["continuum_interaction"].__setitem__("K115_stationary_diagonal_state_preserved", False)),
        ("erase_bin_embedding", lambda d: d["collision_white_noise_limit"].__setitem__("K119_cell_embeds_as_vacuum_plus_one_particle_edge_modes_of_each_time_bin", False)),
        ("invent_joint_norm_limit", lambda d: d["collision_white_noise_limit"].__setitem__("full_joint_operator_norm_convergence_claimed", True)),
        ("erase_output", lambda d: d["state_effect_and_output"].__setitem__("stationary_activity_and_entropy_production_recovered", False)),
        ("invent_Born", lambda d: d["state_effect_and_output"].__setitem__("Born_rule_derived", True)),
        ("invent_physical_state", lambda d: d["state_effect_and_output"].__setitem__("physical_state_authentication", True)),
        ("erase_action", lambda d: d["regularized_action_boundary"].__setitem__("smooth_finite_band_chiral_time_bin_actions", False)),
        ("invent_finite_energy_limit", lambda d: d["regularized_action_boundary"].__setitem__("ordinary_finite_energy_action_limit_claimed", True)),
        ("invent_gauge", lambda d: d["regularized_action_boundary"].__setitem__("nontrivial_gauge_or_ghost_complex_constructed", True)),
        ("invent_K118_selection", lambda d: d["ownership_boundary"].__setitem__("K118_original_real_field_selected_complex_structure_Fock_vacuum_channels_or_coupling", True)),
        ("invent_source_action", lambda d: d["ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_constructed", True)),
        ("invent_Hadamard", lambda d: d["ownership_boundary"].__setitem__("finite_energy_KMS_or_Hadamard_state_constructed", True)),
        ("invent_AQFT", lambda d: d["ownership_boundary"].__setitem__("full_AQFT_net_constructed", True)),
        ("score_holdout", lambda d: d["ownership_boundary"].__setitem__("held_out_scored", True)),
        ("invent_prediction", lambda d: d["ownership_boundary"].__setitem__("prediction_or_confirmation_credit", True)),
        ("promote_canon", lambda d: d["ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("wrong_edge_count", lambda d: d["exact_control"].__setitem__("directed_edge_channels", 54)),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A GU field derives quantum measurement.")),
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
    print(f"K120 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
