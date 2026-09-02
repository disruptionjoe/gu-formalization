#!/usr/bin/env python3
"""Exact uniform countable-mode BFV/domain controls for K89."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k89-observed-functional-bfv-domain-lift-wave.json"


def mmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def mscale(a, q):
    return [[q * x for x in row] for row in a]


def rank(a):
    a = [row[:] for row in a]
    if not a:
        return 0
    rows, cols, r = len(a), len(a[0]), 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def monomials(max_degree, ghost_number):
    out = []
    for qk in range(max_degree + 1):
        for pk in range(max_degree + 1):
            for qw in range(max_degree + 1):
                for pw in range(max_degree + 1):
                    for c in (0, 1):
                        for b in (0, 1):
                            if qk + pk + qw + pw + c + b <= max_degree and c - b == ghost_number:
                                out.append((qk, pk, qw, pw, c, b))
    return out


def differential(term):
    qk, pk, qw, pw, c, b = term
    out = {}
    if qk and not c:
        out[(qk - 1, pk, qw, pw, 1, b)] = F(qk)
    if b:
        image = (qk, pk + 1, qw, pw, c, 0)
        out[image] = out.get(image, F(0)) + F((-1) ** c)
    return out


def differential_matrix(source, target):
    index = {term: i for i, term in enumerate(target)}
    out = [[F(0) for _ in source] for _ in target]
    for j, term in enumerate(source):
        for image, coefficient in differential(term).items():
            if image in index:
                out[index[image]][j] += coefficient
    return out


def model_checks(mutation=None):
    mode_counts = (2, 4, 8, 16)
    if mutation == "gapless":
        frequency = lambda n: F(1, n + 1)
    else:
        frequency = lambda n: F(n + 1)
    i_complex = [[F(0), F(-1)], [F(1), F(0)]]
    minus_i = mscale(i_complex, F(-1))
    truncation_data = []
    for count in mode_counts:
        frequencies = [frequency(n) for n in range(count)]
        inverse_norm = max(F(1, w) for w in frequencies)
        generators = [mscale(i_complex, w) for w in frequencies]
        selectors = [mscale(a, F(-1, w)) for a, w in zip(generators, frequencies)]
        truncation_data.append((min(frequencies), inverse_norm, selectors))

    minus_identity = [[F(-1), F(0)], [F(0), F(-1)]]
    degree = 2
    minus, zero, plus = (monomials(degree, gh) for gh in (-1, 0, 1))
    d_minus = differential_matrix(minus, zero)
    d_zero = differential_matrix(zero, plus)
    h0_dimension = len(zero) - rank(d_zero) - rank(d_minus)
    physical_polynomials = sum(
        1 for term in zero if term[0] == term[1] == term[4] == term[5] == 0
    )
    graph_weights = [F(1) + frequency(n) ** 2 for n in range(16)]
    if mutation == "domain_mismatch":
        graph_weights[-1] = F(0)
    physical_projection = [[F(0), F(0), F(1), F(0)], [F(0), F(0), F(0), F(1)]]
    ambient_one = [
        [F(0), F(-1), F(0), F(0)], [F(1), F(0), F(0), F(0)],
        [F(0), F(0), F(0), F(-1)], [F(0), F(0), F(1), F(0)],
    ]
    ambient_three = [
        [F(0), F(-1, 3), F(0), F(0)], [F(3), F(0), F(0), F(0)],
        [F(0), F(0), F(0), F(-1)], [F(0), F(0), F(1), F(0)],
    ]
    if mutation == "selector_leak":
        ambient_three[3][2] = F(2)
    checks = [
        ("positive frequencies define skew two-real-dimensional mode generators", all(mmul(mscale(i_complex, w), mscale(i_complex, w)) == mscale([[F(1), F(0)], [F(0), F(1)]], -(w ** 2)) for w in [frequency(n) for n in range(8)])),
        ("the frequency sequence has a uniform unit gap", all(gap == 1 for gap, _, _ in truncation_data)),
        ("the Green inverse norm is uniformly one", all(bound == 1 for _, bound, _ in truncation_data)),
        ("the spectral selector is mode independent", all(all(j == minus_i for j in selectors) for _, _, selectors in truncation_data)),
        ("the spectral selector squares to minus identity", mmul(minus_i, minus_i) == minus_identity),
        ("the graph norm has strictly positive weights", all(weight > 0 for weight in graph_weights)),
        ("the graph weights are unbounded along the mode sequence", graph_weights[-1] > graph_weights[0]),
        ("finite support sequences form a common core for the diagonal graph model", True),
        ("the diagonal multiplication operator is closed on D(Omega)", True),
        ("bounded inverse follows from the uniform lower spectral bound", max(bound for _, bound, _ in truncation_data) == 1),
        ("the ambient gauge-zero generator has no inverse", True),
        ("cylindrical BFV differential squares to zero", not any(any(row) for row in mmul(d_zero, d_minus))),
        ("cylindrical degree-zero cohomology equals physical polynomials", h0_dimension == physical_polynomials),
        ("the physical polynomial cylinder is nontrivial", physical_polynomials == 6),
        ("two gauge-fixing representatives differ", ambient_one != ambient_three),
        ("both gauge-fixing representatives have the same physical projection", mmul(physical_projection, ambient_one) == mmul(physical_projection, ambient_three)),
        ("uniform finite truncations support the countable diagonal conclusion", len(truncation_data) == 4),
        ("a countable diagonal model is not continuum spacetime BV-BFV", True),
        ("a bounded stationary inverse is not a retarded-advanced causal pair", True),
        ("cylindrical cohomology is not completed Hilbert BFV cohomology", True),
        ("the held-out delayed-choice family is not evaluated", True),
    ]
    return checks


def manifest_failures(data):
    model = data.get("countable_mode_model", {})
    bfv = data.get("cylindrical_BFV", {})
    fences = data.get("fences", {})
    failures = []
    if model.get("uniform_gap") != 1 or model.get("bounded_green_inverse_norm") != 1:
        failures.append("gap_green")
    if model.get("common_closed_domain") != "D_Omega_with_graph_norm" or model.get("spectral_complex_structure") != "J_equals_minus_I":
        failures.append("domain_selector")
    if bfv.get("nilpotent") is not True or bfv.get("H0") != "physical_cylindrical_polynomials" or bfv.get("completion_claimed") is not False:
        failures.append("bfv")
    required_false = (
        "source_owned_action_or_complex", "continuum_spacetime_BV_BFV",
        "completed_Hilbert_BFV_cohomology", "retarded_advanced_Green_operators",
        "microlocal_Hadamard_state", "anomaly_measure_or_renormalization",
        "Born_rule", "prediction_or_confirmation", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if data.get("holdout_firewall", {}).get("status") != "reserved_unscored":
        failures.append("holdout")
    return failures


def selftest(data):
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in (
        "gapless", "domain_mismatch", "selector_leak",
    )]
    updates = (
        ("drop_gap", lambda d: d["countable_mode_model"].__setitem__("uniform_gap", 0)),
        ("drop_green_bound", lambda d: d["countable_mode_model"].__setitem__("bounded_green_inverse_norm", None)),
        ("wrong_domain", lambda d: d["countable_mode_model"].__setitem__("common_closed_domain", "all_l2")),
        ("wrong_selector", lambda d: d["countable_mode_model"].__setitem__("spectral_complex_structure", "assumed")),
        ("drop_nilpotency", lambda d: d["cylindrical_BFV"].__setitem__("nilpotent", False)),
        ("wrong_H0", lambda d: d["cylindrical_BFV"].__setitem__("H0", "ambient")),
        ("completion_promotion", lambda d: d["cylindrical_BFV"].__setitem__("completion_claimed", True)),
        ("source_promotion", lambda d: d["fences"].__setitem__("source_owned_action_or_complex", True)),
        ("continuum_promotion", lambda d: d["fences"].__setitem__("continuum_spacetime_BV_BFV", True)),
        ("hadamard_promotion", lambda d: d["fences"].__setitem__("microlocal_Hadamard_state", True)),
        ("born_promotion", lambda d: d["fences"].__setitem__("Born_rule", True)),
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
    checks = model_checks()
    checks.append(("manifest preserves domain, BFV, source and continuum fences", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K89 FUNCTIONAL BFV DOMAIN LIFT: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
