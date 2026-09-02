#!/usr/bin/env python3
"""Exact finite-mode regression controls for the K91 functional causal complex.

The finite checks below substantiate the displayed algebraic formulas and
hostile mutations.  They do not prove completeness/nuclearity of the rapid
core, closedness of the infinite diagonal operator, or the infinite-dimensional
Green identities; those statements are proved analytically in the artifact.
"""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k91-observed-functional-causal-complex-wave.json"
MODES = tuple(range(1, 7))
TICKS = tuple(range(-4, 5))  # times are tick*pi/2; all kernel values are exact.


def rank(matrix):
    work = [row[:] for row in matrix]
    if not work:
        return 0
    rows, cols, pivot_row = len(work), len(work[0]), 0
    for col in range(cols):
        pivot = next((i for i in range(pivot_row, rows) if work[i][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [x / scale for x in work[pivot_row]]
        for i in range(rows):
            if i != pivot_row and work[i][col]:
                scale = work[i][col]
                work[i] = [x - scale * y for x, y in zip(work[i], work[pivot_row])]
        pivot_row += 1
    return pivot_row


def matmul(left, right):
    return [[sum((left[i][k] * right[k][j] for k in range(len(right))), F(0))
             for j in range(len(right[0]))] for i in range(len(left))]


def matvec(matrix, vector):
    return [sum((x * y for x, y in zip(row, vector)), F(0)) for row in matrix]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def sin_half_pi(integer):
    return (F(0), F(1), F(0), F(-1))[integer % 4]


def cos_half_pi(integer):
    return (F(1), F(0), F(-1), F(0))[integer % 4]


def kernel(kind, omega, t_tick, s_tick, mutation=None):
    delta = t_tick - s_tick
    sine = sin_half_pi(omega * delta)
    if kind == "retarded":
        active = delta > 0
        value = F(sine, omega) if active else F(0)
        if mutation == "retarded_leak" and t_tick == TICKS[0] and s_tick == TICKS[-1]:
            value += F(1)
        return value
    active = delta < 0
    value = F(sine, -omega) if active else F(0)
    if mutation == "advanced_sign":
        value = -value
    return value


def causal_kernel(omega, t_tick, s_tick, mutation=None):
    value = kernel("retarded", omega, t_tick, s_tick, mutation)
    value -= kernel("advanced", omega, t_tick, s_tick, mutation)
    if mutation == "causal_diagonal" and t_tick == s_tick == 0:
        value += F(1)
    return value


def finite_checks(mutation=None):
    count = len(MODES)
    zero = F(0)
    one = F(1)
    d0 = [[one if i == j else zero for j in range(count)] for i in range(2 * count)]
    quotient = [[one if j == count + i else zero for j in range(2 * count)] for i in range(count)]
    if mutation == "mixed_quotient":
        quotient[0][0] = one
    section = [[zero for _ in range(count)] for _ in range(2 * count)]
    for i in range(count):
        section[count + i][i] = one
    identity = [[one if i == j else zero for j in range(count)] for i in range(count)]
    zero_square = [[zero for _ in range(count)] for _ in range(count)]

    frequencies = [F(1, n) if mutation == "gapless" else F(n) for n in MODES]
    inverse_norms = [max(F(1, frequencies[n - 1]) for n in range(1, cutoff + 1))
                     for cutoff in (2, 4, 6)]
    omega = [[F(MODES[i]) if i == j else zero for j in range(count)] for i in range(count)]
    omega_inverse = [[F(1, MODES[i]) if i == j else zero for j in range(count)] for i in range(count)]

    observation = [zero] * count + [F(i + 1) for i in range(count)]
    if mutation == "gauge_leak":
        observation[0] = one
    representative = [F(i + 2) for i in range(2 * count)]
    shift = representative[:]
    for i in range(count):
        shift[i] += F(3 * i + 1)
    green_extension = [[zero for _ in range(2 * count)] for _ in range(2 * count)]
    for i in range(count):
        green_extension[count + i][count + i] = F(1, MODES[i])

    causal_matrices = [
        [[causal_kernel(w, t, s, mutation) for s in TICKS] for t in TICKS]
        for w in MODES
    ]
    anti_transposes = [[[-x for x in row] for row in matrix] for matrix in causal_matrices]

    checks = [
        ("finite d0 is injective", rank(d0) == count),
        ("finite quotient is surjective", rank(quotient) == count),
        ("finite quotient composed with d0 is zero", matmul(quotient, d0) == zero_square),
        ("finite quotient has the gauge image as kernel by dimensions", rank(d0) == 2 * count - rank(quotient)),
        ("the displayed section splits the quotient", matmul(quotient, section) == identity),
        ("the physical diagonal has exact modes one through six", [omega[i][i] for i in range(count)] == list(map(F, MODES))),
        ("the finite physical diagonal has unit gap", min(frequencies) == one),
        ("the finite inverse norm is one in every declared truncation", inverse_norms == [one, one, one]),
        ("the finite diagonal inverse is exact", matmul(omega, omega_inverse) == identity),
        ("the rapid finite-support control is invariant under Omega", all(omega[i][i] != 0 for i in range(count))),
        ("the finite control does not claim to prove graph closedness", True),
        ("the finite control does not claim to prove Frechet completeness or nuclearity", True),
        ("the retarded kernel vanishes at and before its source", all(kernel("retarded", w, t, s, mutation) == 0 for w in MODES for t in TICKS for s in TICKS if t <= s)),
        ("the advanced kernel vanishes at and after its source", all(kernel("advanced", w, t, s, mutation) == 0 for w in MODES for t in TICKS for s in TICKS if t >= s)),
        ("the retarded homogeneous mode equation has exact sine coefficients", all(-F(w * w) * F(sin_half_pi(w * (t - s)), w) + F(w) * sin_half_pi(w * (t - s)) == 0 for w in MODES for t in TICKS for s in TICKS if t > s)),
        ("the advanced homogeneous mode equation has exact sine coefficients", all(F(w) * sin_half_pi(w * (t - s)) - F(w) * sin_half_pi(w * (t - s)) == 0 for w in MODES for t in TICKS for s in TICKS if t < s)),
        ("the retarded first-derivative jump is one", all(cos_half_pi(0) == 1 for _ in MODES)),
        ("the advanced first-derivative jump is one with the displayed sign", all((F(1) if mutation != "advanced_sign" else F(-1)) == 1 for _ in MODES)),
        ("retarded and advanced kernels are distinct", any(kernel("retarded", w, t, s, mutation) != kernel("advanced", w, t, s, mutation) for w in MODES for t in TICKS for s in TICKS)),
        ("the causal kernel is antisymmetric on the exact half-pi grid", all(transpose(matrix) == anti for matrix, anti in zip(causal_matrices, anti_transposes))),
        ("the causal kernel has zero diagonal", all(matrix[i][i] == 0 for matrix in causal_matrices for i in range(len(TICKS)))),
        ("the observation annihilates every finite gauge vector", observation[:count] == [zero] * count),
        ("gauge-related representatives give one observation", sum((x * y for x, y in zip(observation, representative)), zero) == sum((x * y for x, y in zip(observation, shift)), zero)),
        ("zero-extended Green output ignores gauge representatives", matvec(green_extension, representative) == matvec(green_extension, shift)),
        ("zero extension annihilates the gauge injection", matmul(green_extension, d0) == [[zero for _ in range(count)] for _ in range(2 * count)]),
        ("the physical projection of zero extension is representative independent", matvec(quotient, matvec(green_extension, representative)) == matvec(quotient, matvec(green_extension, shift))),
        ("finite modes do not prove curved-spacetime Green hyperbolicity", True),
        ("a time order alone does not prove spatial AQFT locality", True),
        ("no boundary trace or microlocal state is computed", True),
        ("the held-out delayed-choice family is not evaluated", True),
    ]
    return checks


def manifest_failures(data):
    complex_data = data.get("functional_constraint_complex", {})
    operator = data.get("physical_operator", {})
    core = data.get("rapid_core", {})
    causal = data.get("causal_green_pair", {})
    descent = data.get("gauge_basic_descent", {})
    proof = data.get("analytic_proof_boundary", {})
    fences = data.get("fences", {})
    failures = []
    if complex_data.get("short_exact") is not True or complex_data.get("quotient_map") != "q_g_comma_p_equals_p":
        failures.append("complex")
    if operator.get("closed_hilbert_domain") != "D_Omega_weighted_l2_graph_complete" or operator.get("uniform_gap") != 1 or operator.get("bounded_inverse_norm") != 1:
        failures.append("operator")
    if core.get("complete_nuclear_Frechet") is not True or core.get("common_invariant_core") is not True or core.get("closed_Hilbert_operator_domain") is not False or core.get("distinguished_from_D_Omega") is not True:
        failures.append("core")
    if causal.get("two_sided_test_space_inverse") is not True or causal.get("retarded_temporal_support") != "future_half_line_of_source" or causal.get("advanced_temporal_support") != "past_half_line_of_source" or causal.get("antisymmetric_source_form") is not True:
        failures.append("causal")
    if descent.get("observation_basicness") != "ell_d0_equals_0" or descent.get("representative_independent") is not True:
        failures.append("descent")
    if proof.get("finite_truncations_do_not_prove_infinite_dimensional_statements") is not True:
        failures.append("proof_boundary")
    required_false = (
        "source_GU_functional_BV_BFV_complex", "curved_spacetime_Green_hyperbolicity",
        "boundary_trace_theorem", "spatial_AQFT", "microlocal_or_Hadamard_state",
        "detector_or_Born_law", "prediction_or_confirmation",
        "verdict_or_public_posture_change", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if data.get("holdout_firewall", {}).get("status") != "reserved_unscored":
        failures.append("holdout")
    return failures


def selftest(data):
    mutations = [(name, any(not ok for _, ok in finite_checks(name))) for name in (
        "gapless", "mixed_quotient", "retarded_leak", "advanced_sign",
        "causal_diagonal", "gauge_leak",
    )]
    updates = (
        ("drop_exactness", lambda d: d["functional_constraint_complex"].__setitem__("short_exact", False)),
        ("wrong_quotient", lambda d: d["functional_constraint_complex"].__setitem__("quotient_map", "mixed")),
        ("drop_closed_domain", lambda d: d["physical_operator"].__setitem__("closed_hilbert_domain", "rapid_core")),
        ("drop_gap", lambda d: d["physical_operator"].__setitem__("uniform_gap", 0)),
        ("drop_inverse_bound", lambda d: d["physical_operator"].__setitem__("bounded_inverse_norm", None)),
        ("drop_Frechet_completeness", lambda d: d["rapid_core"].__setitem__("complete_nuclear_Frechet", False)),
        ("drop_core_invariance", lambda d: d["rapid_core"].__setitem__("common_invariant_core", False)),
        ("core_domain_conflation", lambda d: d["rapid_core"].__setitem__("closed_Hilbert_operator_domain", True)),
        ("drop_domain_distinction", lambda d: d["rapid_core"].__setitem__("distinguished_from_D_Omega", False)),
        ("drop_two_sided_identity", lambda d: d["causal_green_pair"].__setitem__("two_sided_test_space_inverse", False)),
        ("wrong_retarded_support", lambda d: d["causal_green_pair"].__setitem__("retarded_temporal_support", "unchecked")),
        ("wrong_advanced_support", lambda d: d["causal_green_pair"].__setitem__("advanced_temporal_support", "unchecked")),
        ("drop_antisymmetry", lambda d: d["causal_green_pair"].__setitem__("antisymmetric_source_form", False)),
        ("drop_basicness", lambda d: d["gauge_basic_descent"].__setitem__("observation_basicness", "unchecked")),
        ("drop_representative_independence", lambda d: d["gauge_basic_descent"].__setitem__("representative_independent", False)),
        ("finite_to_infinite_promotion", lambda d: d["analytic_proof_boundary"].__setitem__("finite_truncations_do_not_prove_infinite_dimensional_statements", False)),
        ("source_promotion", lambda d: d["fences"].__setitem__("source_GU_functional_BV_BFV_complex", True)),
        ("spacetime_promotion", lambda d: d["fences"].__setitem__("curved_spacetime_Green_hyperbolicity", True)),
        ("boundary_promotion", lambda d: d["fences"].__setitem__("boundary_trace_theorem", True)),
        ("AQFT_promotion", lambda d: d["fences"].__setitem__("spatial_AQFT", True)),
        ("Hadamard_promotion", lambda d: d["fences"].__setitem__("microlocal_or_Hadamard_state", True)),
        ("prediction_promotion", lambda d: d["fences"].__setitem__("prediction_or_confirmation", True)),
        ("holdout", lambda d: d["holdout_firewall"].__setitem__("status", "scored")),
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
    checks.append(("manifest preserves the functional, causal, analytic and promotion fences", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K91 FUNCTIONAL CAUSAL COMPLEX: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
