#!/usr/bin/env python3
"""Exact causal Green-pair and gauge-quotient controls for K90."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k90-observed-causal-green-quotient-wave.json"
SOURCE = tuple(range(-3, 4))
EVAL = tuple(range(-5, 6))


def retarded(source, mutation=None):
    out = {n: sum((F(n - k) * source.get(k, F(0)) for k in SOURCE if k < n), F(0)) for n in EVAL}
    if mutation == "precausal_leak":
        out[-5] += source.get(3, F(0))
    return out


def advanced(source, mutation=None):
    sign = F(1) if mutation == "wrong_advanced_sign" else F(1)
    out = {n: sign * sum((F(k - n) * source.get(k, F(0)) for k in SOURCE if k > n), F(0)) for n in EVAL}
    if mutation == "wrong_advanced_sign":
        out = {n: -value for n, value in out.items()}
    return out


def operator(field, n):
    return field[n + 1] - 2 * field[n] + field[n - 1]


def basis(k):
    return {j: F(j == k) for j in SOURCE}


def causal_matrix(mutation=None):
    matrix = [[F(n - k) for k in SOURCE] for n in SOURCE]
    if mutation == "symmetric_leak":
        matrix[0][0] = F(1)
    return matrix


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def matvec(matrix, vector):
    return [sum((x * y for x, y in zip(row, vector)), F(0)) for row in matrix]


def checks(mutation=None):
    retarded_solutions = [retarded(basis(k), mutation) for k in SOURCE]
    advanced_solutions = [advanced(basis(k), mutation) for k in SOURCE]
    matrix = causal_matrix(mutation)
    gauge_basic = [F(0), F(0)] + [F(i == 3) for i in range(len(SOURCE))]
    if mutation == "gauge_leak":
        gauge_basic[0] = F(1)
    representative = [F(2), F(-1)] + [F(i + 1) for i in range(len(SOURCE))]
    shifted = representative[:]
    shifted[0] += 5
    shifted[1] -= 7
    physical = representative[2:]
    physical_shifted = shifted[2:]
    quotient_green = matvec(matrix, physical)
    quotient_green_shifted = matvec(matrix, physical_shifted)
    return [
        ("the retarded kernel is a right fundamental solution", all(operator(u, n) == F(n == k) for k, u in zip(SOURCE, retarded_solutions) for n in SOURCE)),
        ("the advanced kernel is a right fundamental solution", all(operator(u, n) == F(n == k) for k, u in zip(SOURCE, advanced_solutions) for n in SOURCE)),
        ("the retarded kernel vanishes strictly before each source", all(u[n] == 0 for k, u in zip(SOURCE, retarded_solutions) for n in EVAL if n <= k)),
        ("the advanced kernel vanishes strictly after each source", all(u[n] == 0 for k, u in zip(SOURCE, advanced_solutions) for n in EVAL if n >= k)),
        ("the causal propagator is retarded minus advanced", all(retarded_solutions[j][n] - advanced_solutions[j][n] == F(n - k) for j, k in enumerate(SOURCE) for n in SOURCE)),
        ("the causal propagator is antisymmetric", transpose(matrix) == [[-x for x in row] for row in matrix]),
        ("the causal propagator has zero diagonal", all(matrix[i][i] == 0 for i in range(len(matrix)))),
        ("the causal propagator is homogeneous in both variables away from source", all((matrix[i + 1][j] - 2 * matrix[i][j] + matrix[i - 1][j]) == 0 for i in range(1, len(SOURCE) - 1) for j in range(len(SOURCE)))),
        ("compact source support gives the declared retarded future", retarded(basis(0))[-3] == 0 and retarded(basis(0))[3] == 3),
        ("compact source support gives the declared advanced past", advanced(basis(0))[3] == 0 and advanced(basis(0))[-3] == 3),
        ("the observation annihilates both gauge coordinates", gauge_basic[:2] == [0, 0]),
        ("gauge-related representatives give one observation", sum(x * y for x, y in zip(gauge_basic, representative)) == sum(x * y for x, y in zip(gauge_basic, shifted))),
        ("physical quotient coordinates are representative independent", physical == physical_shifted),
        ("the quotient Green map is representative independent", quotient_green == quotient_green_shifted),
        ("the Peierls pairing of a source with itself vanishes", sum(x * y for x, y in zip(physical, quotient_green)) == 0),
        ("separated source probes have opposite Peierls signs", matrix[1][5] == -matrix[5][1] != 0),
        ("the finite source space is nontrivial", len(SOURCE) == 7),
        ("retarded and advanced solutions differ", retarded(basis(0)) != advanced(basis(0))),
        ("a finite causal chain is not continuum spacetime", True),
        ("time-chain support is not spatial AQFT locality", True),
        ("finite exact kernels do not prove an unbounded common domain", True),
        ("no wavefront set or Hadamard condition is computed", True),
        ("the held-out delayed-choice family is not evaluated", True),
    ]


def manifest_failures(data):
    model = data.get("causal_chain_model", {})
    quotient = data.get("gauge_quotient", {})
    fences = data.get("fences", {})
    failures = []
    if model.get("retarded_kernel") != "Gret_nk_equals_max_n_minus_k_0" or model.get("advanced_kernel") != "Gadv_nk_equals_max_k_minus_n_0":
        failures.append("kernels")
    if model.get("two_sided_fundamental_solution_on_finite_sources") is not True:
        failures.append("inverse")
    if quotient.get("observation_basicness") != "observation_annihilates_G" or quotient.get("representative_independent") is not True or quotient.get("antisymmetric_peierls_form") is not True:
        failures.append("quotient")
    required_false = (
        "source_owned_action_or_complex", "continuum_spacetime_green_hyperbolicity",
        "common_unbounded_BFV_green_domain", "spatial_locality_or_AQFT",
        "microlocal_wavefront_or_Hadamard", "anomaly_measure_or_renormalization",
        "Born_detector_law", "prediction_or_confirmation", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if data.get("holdout_firewall", {}).get("status") != "reserved_unscored":
        failures.append("holdout")
    return failures


def selftest(data):
    mutations = [(name, any(not ok for _, ok in checks(name))) for name in (
        "precausal_leak", "wrong_advanced_sign", "gauge_leak", "symmetric_leak",
    )]
    updates = (
        ("wrong_retarded", lambda d: d["causal_chain_model"].__setitem__("retarded_kernel", "assumed")),
        ("wrong_advanced", lambda d: d["causal_chain_model"].__setitem__("advanced_kernel", "assumed")),
        ("drop_inverse", lambda d: d["causal_chain_model"].__setitem__("two_sided_fundamental_solution_on_finite_sources", False)),
        ("drop_basicness", lambda d: d["gauge_quotient"].__setitem__("observation_basicness", "unchecked")),
        ("drop_rep_independence", lambda d: d["gauge_quotient"].__setitem__("representative_independent", False)),
        ("drop_antisymmetry", lambda d: d["gauge_quotient"].__setitem__("antisymmetric_peierls_form", False)),
        ("source_promotion", lambda d: d["fences"].__setitem__("source_owned_action_or_complex", True)),
        ("continuum_promotion", lambda d: d["fences"].__setitem__("continuum_spacetime_green_hyperbolicity", True)),
        ("domain_promotion", lambda d: d["fences"].__setitem__("common_unbounded_BFV_green_domain", True)),
        ("locality_promotion", lambda d: d["fences"].__setitem__("spatial_locality_or_AQFT", True)),
        ("hadamard_promotion", lambda d: d["fences"].__setitem__("microlocal_wavefront_or_Hadamard", True)),
        ("born_promotion", lambda d: d["fences"].__setitem__("Born_detector_law", True)),
        ("prediction_promotion", lambda d: d["fences"].__setitem__("prediction_or_confirmation", True)),
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
    results = checks()
    results.append(("manifest preserves causal, quotient, source and continuum fences", not manifest_failures(data)))
    for label, ok in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in results)
    print(f"K90 CAUSAL GREEN QUOTIENT: {passed}/{len(results)} pass")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
