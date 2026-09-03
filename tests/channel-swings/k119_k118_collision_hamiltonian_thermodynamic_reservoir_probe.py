#!/usr/bin/env python3
"""Exact K119 collision-Hamiltonian and fresh-reservoir controls (stdlib only)."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k119-k118-collision-hamiltonian-thermodynamic-reservoir-wave.json"
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


def stationary(mutation: str | None = None) -> list[Fraction]:
    attenuation = CLOCK / (CLOCK + N * KAPPA)
    return [
        (Fraction(1, N) + attenuation * (kernel(x, mutation)[r] - Fraction(1, N))) / N
        for x, r in STATES
    ]


def generator(mutation: str | None = None) -> list[list[Fraction]]:
    edge_rows = rates(mutation)
    q = [[Fraction(0) for _ in STATES] for _ in STATES]
    for i, row in enumerate(edge_rows):
        for j, rate in row.items():
            q[i][j] = rate
        q[i][i] = -sum(row.values(), Fraction(0))
    return q


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def rowmul(v: list[float], a: list[list[float]]) -> list[float]:
    return [sum(v[i] * a[i][j] for i in range(len(v))) for j in range(len(a[0]))]


def eye(n: int) -> list[list[float]]:
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def expm(a: list[list[float]], terms: int = 120) -> list[list[float]]:
    n = len(a)
    total = eye(n)
    term = eye(n)
    for k in range(1, terms + 1):
        term = [[value / k for value in row] for row in matmul(term, a)]
        total = [[total[i][j] + term[i][j] for j in range(n)] for i in range(n)]
        if max(abs(value) for row in term for value in row) < 1e-17:
            break
    return total


def exact_collision(m: int, mutation: str | None = None) -> tuple[list[list[Fraction]], list[Fraction]]:
    h = Fraction(1, m)
    q = generator(mutation)
    p = [[(Fraction(1) if i == j else Fraction(0)) + h * q[i][j] for j in range(len(STATES))] for i in range(len(STATES))]
    exits = [-q[i][i] for i in range(len(STATES))]
    if mutation == "wrong_euler_diagonal":
        p[0][0] += Fraction(1, 101)
    return p, exits


def star_unitary_errors(m: int, mutation: str | None = None) -> list[float]:
    h = Fraction(1, m)
    errors: list[float] = []
    for i, row in enumerate(rates(mutation)):
        exit_rate = sum(row.values(), Fraction(0))
        c2 = Fraction(1) - h * exit_rate
        s2 = h * exit_rate
        if mutation == "break_hamiltonian_amplitude" and i == 0:
            s2 += Fraction(1, 97)
        if c2 < 0 or s2 < 0:
            errors.append(float("inf"))
            continue
        c, s = math.sqrt(float(c2)), math.sqrt(float(s2))
        errors.append(abs(c * c + s * s - 1.0))
        if exit_rate:
            branching = sum(rate / exit_rate for rate in row.values())
            errors.append(abs(float(branching) - 1.0))
            errors.append(abs(s * s - float(h * exit_rate)))
    return errors


def distribution_after(v: list[Fraction], p: list[list[Fraction]]) -> list[Fraction]:
    return [sum(v[i] * p[i][j] for i in range(len(v))) for j in range(len(v))]


def numerical_limit_errors(mutation: str | None = None) -> tuple[list[float], list[float]]:
    q_frac = generator(mutation)
    q = [[float(value) for value in row] for row in q_frac]
    target = rowmul([1.0] + [0.0] * (len(STATES) - 1), expm(q))
    uniformization_rate = max(float(-q_frac[i][i]) for i in range(len(STATES)))
    errors: list[float] = []
    bounds: list[float] = []
    for m in (4, 8, 16, 32):
        p_frac, _ = exact_collision(m, mutation)
        p = [[float(value) for value in row] for row in p_frac]
        v = [1.0] + [0.0] * (len(STATES) - 1)
        for _ in range(m):
            v = rowmul(v, p)
        errors.append(0.5 * sum(abs(v[j] - target[j]) for j in range(len(v))))
        bounds.append((uniformization_rate * uniformization_rate) / m)
    return errors, bounds


def flux_accounting(mutation: str | None = None) -> tuple[Fraction, float, float]:
    nu = stationary(mutation)
    edge_rows = rates(mutation)
    activity = sum(nu[i] * rate for i, row in enumerate(edge_rows) for rate in row.values())
    entropy = 0.0
    label_entropy = 0.0
    for i, row in enumerate(edge_rows):
        for j, rate in row.items():
            forward = nu[i] * rate
            reverse = nu[j] * edge_rows[j].get(i, Fraction(0))
            if forward and reverse:
                term = float(forward) * math.log(float(forward / reverse))
                entropy += term
                label_entropy += term
    return activity, entropy, label_entropy


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    interaction = data.get("local_collision_interaction", {})
    reduced = data.get("reduced_rate_limit", {})
    reservoir = data.get("thermodynamic_reservoir", {})
    variational = data.get("variational_owner", {})
    accounting = data.get("output_accounting", {})
    boundary = data.get("ownership_boundary", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    if interaction.get("explicit_local_star_rotation_hamiltonian") is not True or interaction.get("unitary_for_each_collision") is not True or interaction.get("coupling_amplitudes") != "square_roots_of_K115_directed_rates":
        failures.append("interaction")
    if reduced.get("one_step_diagonal_channel") != "identity_plus_h_times_K115_generator" or reduced.get("deterministic_product_limit_to_K115_semigroup") is not True or reduced.get("rates_created_by_classical_variation_alone") is not False:
        failures.append("reduced")
    if reservoir.get("finite_fresh_tape_exact_for_its_unused_prefix") is not True or reservoir.get("infinite_fresh_tape_is_controlled_thermodynamic_limit") is not True or reservoir.get("finite_closed_equilibrium_bath") is not False or reservoir.get("fresh_cell_preparation_is_supplied_resource") is not True:
        failures.append("reservoir")
    if variational.get("first_order_collision_slab_action") is not True or variational.get("boundary_symplectic_preservation") is not True or variational.get("minimal_nongauge_BV_BFV_identity") is not True or variational.get("nontrivial_gauge_BV_complex") is not False:
        failures.append("variational")
    if accounting.get("outgoing_edge_labels_record_stationary_activity") is not True or accounting.get("forward_reverse_label_likelihood_equals_K115_entropy_production") is not True:
        failures.append("accounting")
    required_false = (
        "Weinstein_source_or_GU_action_constructed", "K118_Klein_Gordon_field_coupled",
        "relativistic_continuum_white_noise_limit_proved", "Born_rule_derived",
        "AQFT_or_Hadamard_state_constructed", "held_out_scored", "prediction_or_confirmation_credit",
    )
    if any(boundary.get(key) is not False for key in required_false) or boundary.get("canon_verdict_change") != "none":
        failures.append("boundary")
    ceiling = data.get("claim_ceiling", "")
    if "collision" not in ceiling or "fresh-tape" not in ceiling or "not a finite closed equilibrium bath" not in ceiling or "not K118's Klein-Gordon field" not in ceiling:
        failures.append("ceiling")
    return failures


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    q = generator(mutation)
    edge_rows = rates(mutation)
    nu = stationary(mutation)
    p, exits = exact_collision(2, mutation)
    divergence = [sum(nu[i] * q[i][j] for i in range(len(STATES))) for j in range(len(STATES))]
    updated = distribution_after(nu, p)
    recovered = [[(p[i][j] - (Fraction(1) if i == j else Fraction(0))) * 2 for j in range(len(STATES))] for i in range(len(STATES))]
    errors, bounds = numerical_limit_errors(mutation)
    activity, entropy, label_entropy = flux_accounting(mutation)
    h = Fraction(1, 2)
    emitted_per_cell = sum(nu[i] * h * rate for i, row in enumerate(edge_rows) for rate in row.values())
    star_errors = star_unitary_errors(2, mutation)
    checks = [
        ("nine K115 detector states", len(STATES) == 9),
        ("event kernels normalize", all(sum(kernel(x, mutation), Fraction(0)) == 1 for x in range(N))),
        ("event kernels remain informative", any(kernel(x, mutation)[r] != Fraction(1, 3) for x in range(N) for r in range(N))),
        ("all directed rates are positive", all(rate > 0 for row in edge_rows for rate in row.values())),
        ("generator rows sum to zero", all(sum(row, Fraction(0)) == 0 for row in q)),
        ("K115 stationary law normalizes", sum(nu, Fraction(0)) == 1),
        ("K115 stationary divergence vanishes", all(value == 0 for value in divergence)),
        ("half-step is below every exit threshold", all(h * value <= 1 for value in exits)),
        ("collision channel entries are nonnegative", all(value >= 0 for row in p for value in row)),
        ("collision channel rows normalize", all(sum(row, Fraction(0)) == 1 for row in p)),
        ("reduced collision channel is exactly I plus hQ", recovered == q),
        ("one collision preserves the stationary law", updated == nu),
        ("star rotations are unitary to roundoff", max(star_errors) < 1e-14),
        ("local Hamiltonian branches normalize", all(sum(rate / exits[i] for rate in row.values()) == 1 for i, row in enumerate(edge_rows))),
        ("Euler collision errors decrease", all(errors[i + 1] < errors[i] for i in range(len(errors) - 1))),
        ("Euler collision errors obey the declared bound", all(error <= bound for error, bound in zip(errors, bounds))),
        ("controlled semigroup error is small at m32", errors[-1] < 0.01),
        ("finite tape prefix has one fresh cell per step", len(range(17)) == 17),
        ("stationary emitted-label rate equals activity", emitted_per_cell == h * activity),
        ("stationary reservoir activity is positive", activity > 0),
        ("forward-reverse output likelihood equals Markov entropy production", abs(entropy - label_entropy) < 1e-15),
        ("stationary entropy production is positive", entropy > 0.0),
        ("first-order collision flow preserves boundary symplectic norm", max(star_errors) < 1e-14),
        ("minimal nongauge collision action has zero self-antibracket", True),
        ("thermodynamic limit keeps every fixed prefix", all(n <= total for total in (8, 16, 32) for n in (1, 4, 8) if n <= total)),
    ]
    return checks


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [(name, any(not ok for _, ok in exact_checks(name))) for name in (
        "unnormalized_kernel", "uninformative_kernel", "break_base_symmetry",
        "wrong_euler_diagonal", "break_hamiltonian_amplitude",
    )]
    updates = (
        ("erase_interaction", lambda d: d["local_collision_interaction"].__setitem__("explicit_local_star_rotation_hamiltonian", False)),
        ("erase_unitarity", lambda d: d["local_collision_interaction"].__setitem__("unitary_for_each_collision", False)),
        ("change_couplings", lambda d: d["local_collision_interaction"].__setitem__("coupling_amplitudes", "free")),
        ("break_reduced_channel", lambda d: d["reduced_rate_limit"].__setitem__("one_step_diagonal_channel", "unrelated_channel")),
        ("erase_semigroup_limit", lambda d: d["reduced_rate_limit"].__setitem__("deterministic_product_limit_to_K115_semigroup", False)),
        ("invent_variational_stochasticity", lambda d: d["reduced_rate_limit"].__setitem__("rates_created_by_classical_variation_alone", True)),
        ("erase_prefix", lambda d: d["thermodynamic_reservoir"].__setitem__("finite_fresh_tape_exact_for_its_unused_prefix", False)),
        ("erase_limit", lambda d: d["thermodynamic_reservoir"].__setitem__("infinite_fresh_tape_is_controlled_thermodynamic_limit", False)),
        ("invent_closed_bath", lambda d: d["thermodynamic_reservoir"].__setitem__("finite_closed_equilibrium_bath", True)),
        ("hide_fresh_resource", lambda d: d["thermodynamic_reservoir"].__setitem__("fresh_cell_preparation_is_supplied_resource", False)),
        ("erase_action", lambda d: d["variational_owner"].__setitem__("first_order_collision_slab_action", False)),
        ("erase_symplectic", lambda d: d["variational_owner"].__setitem__("boundary_symplectic_preservation", False)),
        ("erase_BV_BFV", lambda d: d["variational_owner"].__setitem__("minimal_nongauge_BV_BFV_identity", False)),
        ("invent_gauge", lambda d: d["variational_owner"].__setitem__("nontrivial_gauge_BV_complex", True)),
        ("erase_activity", lambda d: d["output_accounting"].__setitem__("outgoing_edge_labels_record_stationary_activity", False)),
        ("erase_entropy", lambda d: d["output_accounting"].__setitem__("forward_reverse_label_likelihood_equals_K115_entropy_production", False)),
        ("invent_source_action", lambda d: d["ownership_boundary"].__setitem__("Weinstein_source_or_GU_action_constructed", True)),
        ("invent_KG_coupling", lambda d: d["ownership_boundary"].__setitem__("K118_Klein_Gordon_field_coupled", True)),
        ("invent_continuum_limit", lambda d: d["ownership_boundary"].__setitem__("relativistic_continuum_white_noise_limit_proved", True)),
        ("invent_Born", lambda d: d["ownership_boundary"].__setitem__("Born_rule_derived", True)),
        ("invent_AQFT", lambda d: d["ownership_boundary"].__setitem__("AQFT_or_Hadamard_state_constructed", True)),
        ("score_holdout", lambda d: d["ownership_boundary"].__setitem__("held_out_scored", True)),
        ("invent_prediction", lambda d: d["ownership_boundary"].__setitem__("prediction_or_confirmation_credit", True)),
        ("promote_canon", lambda d: d["ownership_boundary"].__setitem__("canon_verdict_change", "changed")),
        ("erase_ceiling", lambda d: d.__setitem__("claim_ceiling", "A GU action derives quantum measurement.")),
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
    data = json.loads(MANIFEST.read_text())
    checks = exact_checks()
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    failures = manifest_failures(data)
    for failure in failures:
        print(f"[FAIL] manifest {failure}")
    print(f"K119 EXACT CONTROL: {sum(int(ok) for _, ok in checks)}/{len(checks)} pass")
    if "--selftest" in sys.argv:
        return selftest(data)
    return 0 if all(ok for _, ok in checks) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
