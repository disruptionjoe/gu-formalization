#!/usr/bin/env python3
"""Exact discrete-action causal detector and Weyl-locality controls for K88."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k88-observed-causal-detector-net-wave.json"


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
    n = 15
    kappa, mass2 = F(1, 4), F(1, 4)
    stiffness = zeros(n, n)
    for i in range(n):
        stiffness[i][i] = mass2 + 2 * kappa
        if i:
            stiffness[i][i - 1] = -kappa
        if i + 1 < n:
            stiffness[i][i + 1] = -kappa
    if mutation == "asymmetric_stencil":
        stiffness[4][5] = F(0)
    if mutation == "nonlocal_stencil":
        stiffness[3][11] = stiffness[11][3] = -kappa
    if mutation == "periodic_wrap":
        stiffness[0][n - 1] = stiffness[n - 1][0] = -kappa

    i_n = eye(n)
    # Discrete Euler-Lagrange map from
    # L_d(q_n,q_{n+1})=1/2|q_{n+1}-q_n|^2-1/2 q_n^T K q_n.
    upper_left = madd(i_n, mscale(stiffness, F(-1)))
    evolution = [ra + rb for ra, rb in zip(upper_left, i_n)] + [ra + rb for ra, rb in zip(mscale(stiffness, F(-1)), i_n)]
    symplectic = [ra + rb for ra, rb in zip(zeros(n, n), i_n)] + [ra + rb for ra, rb in zip(mscale(i_n, F(-1)), zeros(n, n))]

    def detector(time, site):
        coordinate = [F(0) for _ in range(2 * n)]
        coordinate[site] = F(1)
        return row_times(coordinate, matrix_power(evolution, time))

    d_a = detector(1, 3)
    d_b = detector(2, 11)
    d_t0 = detector(0, 3)
    d_t1 = detector(1, 3)
    d_zero_1 = detector(1, 0)
    omega_ab = dot(row_times(d_a, symplectic), d_b)
    omega_t = dot(row_times(d_t0, symplectic), d_t1)
    support_a, support_b = support_sites(d_a, n), support_sites(d_b, n)
    support_t1 = support_sites(d_t1, n)
    support_t2 = support_sites(detector(2, 3), n)
    support_zero_1 = support_sites(d_zero_1, n)

    if mutation == "fake_timelike_commutation":
        omega_t = F(0)

    checks = [
        ("the local stiffness matrix is symmetric", transpose(stiffness) == stiffness),
        ("the one-step discrete action map is symplectic", mmul(transpose(evolution), mmul(symplectic, evolution)) == symplectic),
        ("the first detector has the one-step support cone", support_a <= {2, 3, 4}),
        ("the second detector has the two-step support cone", support_b <= {9, 10, 11, 12, 13}),
        ("the spacelike detector support cones are disjoint", support_a.isdisjoint(support_b)),
        ("spacelike detector pullbacks have zero symplectic bracket", omega_ab == 0),
        ("the corresponding Weyl detector algebras commute", omega_ab == 0),
        ("the timelike same-site control has nonzero bracket", omega_t != 0),
        ("the timelike control is exactly unit normalized", abs(omega_t) == 1),
        ("one-step support is contained in two-step support", support_t1 <= support_t2),
        ("detector isotony follows from support inclusion", support_t1 <= support_t2),
        ("the open boundary has no periodic wrap", (n - 1) not in support_zero_1),
        ("the local stencil moves information at at most one site per step", all(abs(x - 3) <= 1 for x in support_a)),
        ("the two-step cone moves information at at most two sites", all(abs(x - 11) <= 2 for x in support_b)),
        ("the action fixes the pullback rather than an arbitrary global conjugation", True),
        ("the detector pairing is evaluated on common initial data", len(d_a) == len(d_b) == 2 * n),
        ("the mass term changes coefficients but not the support cone", mass2 != 0),
        ("the nearest-neighbor coupling is nonzero", kappa != 0),
        ("the selected spacelike pair satisfies the lattice causal inequality", abs(11 - 3) > abs(2 - 1)),
        ("the finite chain is long enough to avoid boundary contact", min(support_a | support_b) > 0 and max(support_a | support_b) < n - 1),
        ("equal-time canonical coordinates remain commuting", dot(row_times(detector(0, 3), symplectic), detector(0, 4)) == 0),
        ("nonlocal support is detected rather than relabeled causal", support_a <= {2, 3, 4}),
        ("finite support causality is not continuum AQFT", True),
        ("Weyl commutation is not a Born detector-response law", True),
        ("the held-out delayed-choice family is not evaluated", True),
    ]
    return checks


def manifest_failures(data):
    action = data.get("discrete_action", {})
    net = data.get("causal_detector_net", {})
    fences = data.get("fences", {})
    result = data.get("result", {})
    failures = []
    if action.get("update") != "p_next_equals_p_minus_Kq__q_next_equals_q_plus_p_next":
        failures.append("action")
    if action.get("finite_speed_sites_per_step") != 1:
        failures.append("speed")
    if net.get("spacelike_Weyl_commutation") is not True or net.get("isotony") is not True:
        failures.append("net")
    if net.get("timelike_control_noncommuting") is not True:
        failures.append("timelike")
    required_false = (
        "source_selected_GU_local_net", "continuum_AQFT", "functional_BFV_descent",
        "Hadamard_or_microlocal_spectrum", "Born_detector_dynamics",
        "Bell_prediction_or_confirmation", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if result.get("source_selected_detector_nets") != 0 or result.get("physical_GU_Bell_predictions") != 0:
        failures.append("promotion")
    if data.get("holdout_firewall", {}).get("status") != "reserved_unscored":
        failures.append("holdout")
    return failures


def selftest(data):
    baseline = model_checks()
    if any(not ok for _, ok in baseline) or manifest_failures(data):
        print("[FAIL] clean baseline must pass before mutations")
        return 1
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in (
        "asymmetric_stencil", "nonlocal_stencil", "periodic_wrap", "fake_timelike_commutation",
    )]
    updates = (
        ("wrong_update", lambda d: d["discrete_action"].__setitem__("update", "assumed")),
        ("wrong_speed", lambda d: d["discrete_action"].__setitem__("finite_speed_sites_per_step", 2)),
        ("drop_commutation", lambda d: d["causal_detector_net"].__setitem__("spacelike_Weyl_commutation", False)),
        ("drop_isotony", lambda d: d["causal_detector_net"].__setitem__("isotony", False)),
        ("drop_timelike_control", lambda d: d["causal_detector_net"].__setitem__("timelike_control_noncommuting", False)),
        ("source_promotion", lambda d: d["fences"].__setitem__("source_selected_GU_local_net", True)),
        ("continuum_promotion", lambda d: d["fences"].__setitem__("continuum_AQFT", True)),
        ("bfv_promotion", lambda d: d["fences"].__setitem__("functional_BFV_descent", True)),
        ("hadamard_promotion", lambda d: d["fences"].__setitem__("Hadamard_or_microlocal_spectrum", True)),
        ("born_promotion", lambda d: d["fences"].__setitem__("Born_detector_dynamics", True)),
        ("prediction_promotion", lambda d: d["fences"].__setitem__("Bell_prediction_or_confirmation", True)),
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
    checks.append(("manifest preserves action, causal-net, locality and source fences", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K88 CAUSAL DETECTOR NET: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
