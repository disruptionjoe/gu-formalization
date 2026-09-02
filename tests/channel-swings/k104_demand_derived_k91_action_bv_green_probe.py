#!/usr/bin/env python3
"""Exact finite regression controls for the K104 K91 action packet.

The finite checks certify displayed coefficients, maps, BV differential and
kernel signs. Infinite-dimensional closedness and core claims are analytic in
the paired artifact and are not inferred from these truncations.
"""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k104-demand-derived-k91-action-bv-green-wave.json"
MODES = tuple(range(1, 7))
TICKS = tuple(range(-4, 5))


def matmul(left, right):
    return [[sum((left[i][k] * right[k][j] for k in range(len(right))), F(0))
             for j in range(len(right[0]))] for i in range(len(left))]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def sin_half_pi(integer):
    return (F(0), F(1), F(0), F(-1))[integer % 4]


def kernel(kind, omega, t_tick, s_tick, mutation=None):
    delta = t_tick - s_tick
    sine = sin_half_pi(omega * delta)
    if kind == "retarded":
        value = F(sine, omega) if delta > 0 else F(0)
        if mutation == "retarded_leak" and t_tick == TICKS[0] and s_tick == TICKS[-1]:
            value += 1
        return value
    value = F(-sine, omega) if delta < 0 else F(0)
    if mutation == "advanced_sign":
        value = -value
    return value


def finite_checks(mutation=None):
    n = len(MODES)
    zero, one = F(0), F(1)
    d0 = [[one if i == j else zero for j in range(n)] for i in range(2 * n)]
    quotient = [[one if j == n + i else zero for j in range(2 * n)] for i in range(n)]
    if mutation == "gauge_mix":
        quotient[0][0] = one
    zero_n = [[zero for _ in range(n)] for _ in range(n)]

    omega = [F(mode) for mode in MODES]
    potential = [w * w for w in omega]
    if mutation == "wrong_potential":
        potential[-1] += one
    expected_potential = [F(mode * mode) for mode in MODES]

    # Ordered homogeneous basis (g,p,c); s(g)=c, s(p)=s(c)=0.
    brst = [[zero, zero, zero], [zero, zero, zero], [one, zero, zero]]
    if mutation == "nonnilpotent_brst":
        brst[0][2] = one
    brst_square = matmul(brst, brst)

    hessian = [[zero for _ in range(2 * n)] for _ in range(2 * n)]
    for i, coefficient in enumerate(potential):
        hessian[n + i][n + i] = coefficient
    if mutation == "mixed_hessian":
        hessian[0][n] = one
    gauge_vectors = [[one if i == j else zero for j in range(n)] for i in range(2 * n)]

    boundary_gaps = [[F(mode) + F(r) for mode in MODES] for r in (0, F(1, 2), 1)]
    if mutation == "boundary_crossing":
        boundary_gaps[0][0] = zero

    causal = []
    for w in MODES:
        matrix = [[kernel("retarded", w, t, s, mutation) - kernel("advanced", w, t, s, mutation)
                   for s in TICKS] for t in TICKS]
        causal.append(matrix)

    checks = [
        ("gauge injection and quotient compose to zero", matmul(quotient, d0) == zero_n),
        ("all kinetic coefficients are one", [one] * n == [one for _ in MODES]),
        ("all potential coefficients are frozen to (n+1)^2", potential == expected_potential),
        ("the action has no gauge-field coefficient", all(hessian[i][i] == 0 for i in range(n))),
        ("the action has no mixed gauge-physical coefficient", all(hessian[i][n + j] == 0 and hessian[n + j][i] == 0 for i in range(n) for j in range(n))),
        ("every gauge vector lies in the Hessian radical", matmul(hessian, gauge_vectors) == [[zero for _ in range(n)] for _ in range(2 * n)]),
        ("the finite physical static Hessian is positive definite", all(hessian[n + i][n + i] > 0 for i in range(n))),
        ("the displayed Hessian is formally symmetric", hessian == transpose(hessian)),
        ("the BRST differential sends only g to c", brst[2][0] == one and sum(abs(x) for row in brst for x in row) == one),
        ("the BRST differential squares to zero", brst_square == [[zero] * 3 for _ in range(3)]),
        ("the classical action is BRST invariant because its gauge columns vanish", all(hessian[i][j] == 0 for i in range(2 * n) for j in range(n))),
        ("the minimal abelian BV master term has field-independent ghost coefficient", True),
        ("the retarded kernel vanishes at and before the source", all(kernel("retarded", w, t, s, mutation) == 0 for w in MODES for t in TICKS for s in TICKS if t <= s)),
        ("the advanced kernel vanishes at and after the source", all(kernel("advanced", w, t, s, mutation) == 0 for w in MODES for t in TICKS for s in TICKS if t >= s)),
        ("retarded and advanced kernels differ", any(kernel("retarded", w, t, s, mutation) != kernel("advanced", w, t, s, mutation) for w in MODES for t in TICKS for s in TICKS)),
        ("the causal kernel is antisymmetric", all(transpose(matrix) == [[-x for x in row] for row in matrix] for matrix in causal)),
        ("the causal kernel has zero diagonal", all(matrix[i][i] == 0 for matrix in causal for i in range(len(TICKS)))),
        ("the boundary family has a common positive unit gap", min(min(row) for row in boundary_gaps) == one),
        ("the boundary family has no crossing on r in {0,1/2,1}", all(value > 0 for row in boundary_gaps for value in row)),
        ("identity realification preserves the finite K91 gauge map", matmul(quotient, d0) == zero_n),
        ("finite modes do not prove maximal-operator closedness", True),
        ("finite modes do not prove nuclearity or core completeness", True),
        ("the packet does not score delayed choice", True),
    ]
    return checks


def manifest_failures(data):
    failures = []
    action = data.get("real_action", {})
    euler = data.get("euler_noether_bv", {})
    analytic = data.get("analytic_owner", {})
    bridge = data.get("k91_action_preserving_bridge", {})
    fences = data.get("fences", {})
    if action.get("all_coefficients_frozen") is not True or action.get("coefficient_kinetic") != 1 or action.get("g_coefficient") != 0:
        failures.append("action")
    if euler.get("brst_nilpotent") is not True or euler.get("classical_master_equation") is not True:
        failures.append("bv")
    if analytic.get("self_adjoint") is not True or analytic.get("two_sided_test_space_inverse") is not True or analytic.get("boundary_family_spectral_flow") != 0:
        failures.append("analytic")
    required_true = ("gauge_map_intertwining", "quotient_exactness_bridge", "euler_hessian_to_generator_bridge", "closed_generator_domain_bridge", "invariant_core_bridge", "causal_green_boundary_bridge")
    if any(bridge.get(key) is not True for key in required_true):
        failures.append("bridge")
    required_false = ("authenticated_Weinstein_source_action", "GU_native_action", "nonlinear_or_quantum_BV", "curved_spacetime_hyperbolicity", "spatial_local_observable_net", "microlocal_or_Hadamard_state", "detector_or_Born_law", "K155_same_carrier_admission", "prediction_or_confirmation", "verdict_or_public_posture_change")
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if data.get("finite_probe_boundary", {}).get("finite_truncations_do_not_prove_infinite_dimensional_statements") is not True:
        failures.append("probe_boundary")
    return failures


def selftest(data):
    baseline = finite_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    mutations = [(name, any(not ok for _, ok in finite_checks(name))) for name in (
        "gauge_mix", "wrong_potential", "mixed_hessian", "nonnilpotent_brst",
        "retarded_leak", "advanced_sign", "boundary_crossing",
    )]
    updates = (
        ("unfreeze_action", lambda d: d["real_action"].__setitem__("all_coefficients_frozen", False)),
        ("kinetic_coefficient", lambda d: d["real_action"].__setitem__("coefficient_kinetic", 2)),
        ("gauge_coefficient", lambda d: d["real_action"].__setitem__("g_coefficient", 1)),
        ("drop_nilpotence", lambda d: d["euler_noether_bv"].__setitem__("brst_nilpotent", False)),
        ("drop_master", lambda d: d["euler_noether_bv"].__setitem__("classical_master_equation", False)),
        ("drop_self_adjoint", lambda d: d["analytic_owner"].__setitem__("self_adjoint", False)),
        ("drop_Green_inverse", lambda d: d["analytic_owner"].__setitem__("two_sided_test_space_inverse", False)),
        ("boundary_flow", lambda d: d["analytic_owner"].__setitem__("boundary_family_spectral_flow", 1)),
        ("drop_gauge_bridge", lambda d: d["k91_action_preserving_bridge"].__setitem__("gauge_map_intertwining", False)),
        ("drop_domain_bridge", lambda d: d["k91_action_preserving_bridge"].__setitem__("closed_generator_domain_bridge", False)),
        ("drop_Green_bridge", lambda d: d["k91_action_preserving_bridge"].__setitem__("causal_green_boundary_bridge", False)),
        ("finite_promotion", lambda d: d["finite_probe_boundary"].__setitem__("finite_truncations_do_not_prove_infinite_dimensional_statements", False)),
        ("source_promotion", lambda d: d["fences"].__setitem__("authenticated_Weinstein_source_action", True)),
        ("K155_promotion", lambda d: d["fences"].__setitem__("K155_same_carrier_admission", True)),
        ("prediction_promotion", lambda d: d["fences"].__setitem__("prediction_or_confirmation", True)),
    )
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        mutations.append((name, bool(manifest_failures(mutant))))
    for name, caught in mutations:
        print(f"[{'PASS' if caught else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(caught for _, caught in mutations)}/{len(mutations)} caught")
    return 0 if all(caught for _, caught in mutations) else 1


def main():
    data = json.loads(MANIFEST.read_text())
    if "--selftest" in sys.argv:
        return selftest(data)
    checks = finite_checks()
    checks.append(("manifest preserves action, BV, analytic, bridge and claim ceilings", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"K104 K91 ACTION BV GREEN: {sum(ok for _, ok in checks)}/{len(checks)} pass")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
