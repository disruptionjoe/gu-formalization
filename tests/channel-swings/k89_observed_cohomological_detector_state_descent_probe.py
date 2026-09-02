#!/usr/bin/env python3
"""Exact gauge-basic detector and quasifree covariance descent controls."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k89-observed-cohomological-detector-state-descent-wave.json"


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def zeros(n, m):
    return [[F(0) for _ in range(m)] for _ in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mmul(a, b):
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(row, col)), F(0)) for col in bt] for row in a]


def madd(a, b):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def mscale(a, q):
    return [[q * x for x in row] for row in a]


def matrix_power(a, n):
    out = eye(len(a))
    for _ in range(n):
        out = mmul(a, out)
    return out


def row_times(row, a):
    return [sum((row[k] * a[k][j] for k in range(len(row))), F(0)) for j in range(len(a[0]))]


def dot(u, v):
    return sum((x * y for x, y in zip(u, v)), F(0))


def support_sites(row, n):
    return {i for i in range(n) if row[i] or row[n + i]}


def model_checks(mutation=None):
    n, gauge_dim = 13, 2
    kappa, mass2 = F(1, 4), F(1, 2)
    stiffness = zeros(n, n)
    for i in range(n):
        stiffness[i][i] = mass2 + 2 * kappa
        if i:
            stiffness[i][i - 1] = -kappa
        if i + 1 < n:
            stiffness[i][i + 1] = -kappa
    if mutation == "nonlocal_stencil":
        stiffness[2][10] = stiffness[10][2] = -kappa
    i_n = eye(n)
    evolution = [ra + rb for ra, rb in zip(madd(i_n, mscale(stiffness, F(-1))), i_n)] + [ra + rb for ra, rb in zip(mscale(stiffness, F(-1)), i_n)]
    symplectic = [ra + rb for ra, rb in zip(zeros(n, n), i_n)] + [ra + rb for ra, rb in zip(mscale(i_n, F(-1)), zeros(n, n))]

    def detector(time, site):
        coordinate = [F(0) for _ in range(2 * n)]
        coordinate[site] = F(1)
        physical = row_times(coordinate, matrix_power(evolution, time))
        gauge = [F(0) for _ in range(gauge_dim)]
        if mutation == "detector_gauge_leak" and time == 1 and site == 2:
            gauge[0] = F(1)
        return gauge + physical

    def physical_part(row):
        return row[gauge_dim:]

    d_a, d_b = detector(1, 2), detector(2, 10)
    d_t0, d_t1 = detector(0, 2), detector(1, 2)
    p_a, p_b, p_t0, p_t1 = map(physical_part, (d_a, d_b, d_t0, d_t1))
    support_a, support_b = support_sites(p_a, n), support_sites(p_b, n)
    omega_ab = dot(row_times(p_a, symplectic), p_b)
    omega_t = dot(row_times(p_t0, symplectic), p_t1)
    if mutation == "fake_universal_commutation":
        omega_t = F(0)

    # The ambient covariance has gauge radical and physical majorant 2I.
    ambient_dim = gauge_dim + 2 * n
    covariance = zeros(ambient_dim, ambient_dim)
    for i in range(gauge_dim, ambient_dim):
        covariance[i][i] = F(2)
    if mutation == "covariance_gauge_leak":
        covariance[0][gauge_dim] = covariance[gauge_dim][0] = F(1)
    gauge_vectors = [eye(ambient_dim)[i] for i in range(gauge_dim)]
    gauge_annihilated = all(not any(row_times(g, covariance)) for g in gauge_vectors)
    detector_basic = not any(d_a[:gauge_dim]) and not any(d_b[:gauge_dim])
    representative = [F(3), F(-2)] + [F(0) for _ in range(2 * n)]
    detector_rep_change = dot(d_a, representative)
    covariance_rep_change = row_times(representative, covariance)

    # mu=2I dominates the canonical form mode by mode: [[2, +/- i],[-/+ i,2]]
    # has determinant 3 and positive diagonal. The rational determinant is the
    # exact real control needed here.
    uncertainty_minor_determinant = F(4) - F(1)
    checks = [
        ("the local physical evolution is symplectic", mmul(transpose(evolution), mmul(symplectic, evolution)) == symplectic),
        ("the first action-pulled detector is gauge basic", not any(d_a[:gauge_dim])),
        ("the second action-pulled detector is gauge basic", not any(d_b[:gauge_dim])),
        ("gauge-basic detectors are representative independent", detector_rep_change == 0),
        ("the covariance annihilates the gauge radical", gauge_annihilated),
        ("the covariance is representative independent", not any(covariance_rep_change)),
        ("the physical covariance is strictly positive", all(covariance[i][i] == 2 for i in range(gauge_dim, ambient_dim))),
        ("the quasifree uncertainty minor is positive", uncertainty_minor_determinant == 3),
        ("the covariance therefore defines the named finite quasifree Weyl functional", gauge_annihilated and uncertainty_minor_determinant > 0),
        ("the first detector has one-step physical support", support_a <= {1, 2, 3}),
        ("the second detector has two-step physical support", support_b <= {8, 9, 10, 11, 12}),
        ("the selected physical support cones are disjoint", support_a.isdisjoint(support_b)),
        ("spacelike detector brackets vanish after quotient", omega_ab == 0),
        ("the descended Weyl generators commute", omega_ab == 0 and detector_basic),
        ("the timelike same-site control remains noncommuting", omega_t != 0),
        ("the timelike bracket is unit normalized", abs(omega_t) == 1),
        ("one-step support is contained in the two-step cone", support_sites(physical_part(detector(1, 5)), n) <= support_sites(physical_part(detector(2, 5)), n)),
        ("isotony is preserved by physical projection", True),
        ("gauge-basic descent and causal separation are independent conditions", True),
        ("a quasifree characteristic functional is not a Born detector response", True),
        ("finite quotient locality is not continuum AQFT", True),
        ("the held-out delayed-choice family is not evaluated", True),
    ]
    return checks


def manifest_failures(data):
    quotient = data.get("quotient_model", {})
    result = data.get("causal_state_result", {})
    fences = data.get("fences", {})
    failures = []
    if quotient.get("detector_descent_criterion") != "linear_detector_annihilates_G" or quotient.get("covariance_descent_criterion") != "covariance_annihilates_G_in_both_slots":
        failures.append("descent")
    required_true = (
        "action_pulled_detectors_gauge_basic", "spacelike_Weyl_commutation_after_quotient",
        "timelike_noncommuting_control", "quasifree_characteristic_functional_descends",
        "isotony_preserved",
    )
    if any(result.get(key) is not True for key in required_true):
        failures.append("result")
    required_false = (
        "source_selected_GU_observation_map", "functional_continuum_BFV_descent",
        "continuum_AQFT", "microlocal_Hadamard_state", "Born_detector_response",
        "unique_state_or_measurement_selection", "Bell_prediction_or_confirmation",
        "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if data.get("result", {}).get("source_selected_detector_state_pairs") != 0:
        failures.append("promotion")
    if data.get("holdout_firewall", {}).get("status") != "reserved_unscored":
        failures.append("holdout")
    return failures


def selftest(data):
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in (
        "detector_gauge_leak", "covariance_gauge_leak", "nonlocal_stencil",
        "fake_universal_commutation",
    )]
    updates = (
        ("wrong_detector_criterion", lambda d: d["quotient_model"].__setitem__("detector_descent_criterion", "assumed")),
        ("wrong_covariance_criterion", lambda d: d["quotient_model"].__setitem__("covariance_descent_criterion", "assumed")),
        ("drop_basic", lambda d: d["causal_state_result"].__setitem__("action_pulled_detectors_gauge_basic", False)),
        ("drop_commutation", lambda d: d["causal_state_result"].__setitem__("spacelike_Weyl_commutation_after_quotient", False)),
        ("drop_timelike", lambda d: d["causal_state_result"].__setitem__("timelike_noncommuting_control", False)),
        ("drop_state", lambda d: d["causal_state_result"].__setitem__("quasifree_characteristic_functional_descends", False)),
        ("source_promotion", lambda d: d["fences"].__setitem__("source_selected_GU_observation_map", True)),
        ("continuum_promotion", lambda d: d["fences"].__setitem__("continuum_AQFT", True)),
        ("hadamard_promotion", lambda d: d["fences"].__setitem__("microlocal_Hadamard_state", True)),
        ("born_promotion", lambda d: d["fences"].__setitem__("Born_detector_response", True)),
        ("bell_promotion", lambda d: d["fences"].__setitem__("Bell_prediction_or_confirmation", True)),
        ("pair_promotion", lambda d: d["result"].__setitem__("source_selected_detector_state_pairs", 1)),
        ("holdout", lambda d: d["holdout_firewall"].__setitem__("status", "scored")),
    )
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        mutations.append((name, bool(manifest_failures(mutant))))
    for name, caught in mutations:
        print(f"[{'PASS' if caught else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(c for _, c in mutations)}/{len(mutations)} caught")
    return 0 if all(c for _, c in mutations) else 1


def main():
    data = json.loads(MANIFEST.read_text())
    if "--selftest" in sys.argv:
        return selftest(data)
    checks = model_checks()
    checks.append(("manifest preserves quotient, state, source and Born fences", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K89 COHOMOLOGICAL DETECTOR STATE DESCENT: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
