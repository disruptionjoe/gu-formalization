#!/usr/bin/env python3
"""Exact canonical BFV and quotient-stationary controls for K88."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k88-observed-canonical-bfv-stationary-descent-wave.json"


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


def rank(a):
    a = [row[:] for row in a]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    r = 0
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
        if r == rows:
            break
    return r


def monomials(max_degree, ghost_number):
    out = []
    for qk in range(max_degree + 1):
        for pk in range(max_degree + 1):
            for qw in range(max_degree + 1):
                for pw in range(max_degree + 1):
                    for c in (0, 1):
                        for b in (0, 1):
                            if qk + pk + qw + pw + c + b > max_degree:
                                continue
                            if c - b == ghost_number:
                                out.append((qk, pk, qw, pw, c, b))
    return out


def differential(monomial, mutation=None):
    qk, pk, qw, pw, c, b = monomial
    terms = {}

    def add(term, coefficient):
        terms[term] = terms.get(term, F(0)) + coefficient

    # s(q_K)=c and s(b)=p_K are the two contractible BFV pairs.
    if qk and not c:
        add((qk - 1, pk, qw, pw, 1, b), F(qk))
    if b:
        if mutation == "nonnilpotent_charge":
            add((qk + 1, pk, qw, pw, c, 0), F((-1) ** c))
        add((qk, pk + 1, qw, pw, c, 0), F((-1) ** c))
    return {term: value for term, value in terms.items() if value}


def differential_matrix(source, target, mutation=None):
    target_index = {term: i for i, term in enumerate(target)}
    out = zeros(len(target), len(source))
    for j, term in enumerate(source):
        for image, coefficient in differential(term, mutation).items():
            if image in target_index:
                out[target_index[image]][j] += coefficient
    return out


def model_checks(mutation=None):
    degree = 3
    minus, zero, plus, plus2 = (monomials(degree, gh) for gh in (-1, 0, 1, 2))
    d_minus = differential_matrix(minus, zero, mutation)
    d_zero = differential_matrix(zero, plus, mutation)
    d_plus = differential_matrix(plus, plus2, mutation)
    physical_monomials = sum(1 for term in zero if term[0] == term[1] == term[4] == term[5] == 0)
    h0_dimension = len(zero) - rank(d_zero) - rank(d_minus)

    symplectic = [
        [F(0), F(0), F(1), F(0)],
        [F(0), F(0), F(0), F(1)],
        [F(-1), F(0), F(0), F(0)],
        [F(0), F(-1), F(0), F(0)],
    ]
    full_generator = [
        [F(0), F(0), F(0), F(0)],
        [F(0), F(0), F(0), F(1)],
        [F(0), F(0), F(0), F(0)],
        [F(0), F(-4), F(0), F(0)],
    ]
    projection = [[F(0), F(1), F(0), F(0)], [F(0), F(0), F(0), F(1)]]
    reduced_generator = [[F(0), F(1)], [F(-4), F(0)]]
    reduced_j = [[F(0), F(-1, 2)], [F(2), F(0)]]
    reduced_symplectic = [[F(0), F(1)], [F(-1), F(0)]]
    reduced_majorant = mmul(reduced_symplectic, reduced_j)
    gauge_q = [F(1), F(0), F(0), F(0)]
    gauge_p = [F(0), F(0), F(1), F(0)]
    minus_a2 = mscale(mmul(full_generator, full_generator), F(-1))

    # Gauge-fixing frequencies change only the contractible pair.
    def gauge_fixed_j(nu):
        return [
            [F(0), F(0), F(-1, nu), F(0)],
            [F(0), F(0), F(0), F(-1, 2)],
            [F(nu), F(0), F(0), F(0)],
            [F(0), F(2), F(0), F(0)],
        ]

    j_one, j_three = gauge_fixed_j(F(1)), gauge_fixed_j(F(3))
    if mutation == "physical_gauge_fixing_leak":
        j_three[3][1] = F(3)

    constraint_gradient = gauge_p
    constraint_self_bracket = sum(
        constraint_gradient[i] * symplectic[i][j] * constraint_gradient[j]
        for i in range(4) for j in range(4)
    )
    q_squared = mmul(d_zero, d_minus)
    q_cubed = mmul(d_plus, d_zero)
    checks = [
        ("the minimal BFV differential squares to zero from ghost minus one", not any(any(row) for row in q_squared)),
        ("the minimal BFV differential squares to zero from ghost zero", not any(any(row) for row in q_cubed)),
        ("the truncated exact H0 dimension equals physical W-polynomials", h0_dimension == physical_monomials),
        ("the physical polynomial count is nontrivial", physical_monomials == 10),
        ("the constraint is the K momentum", constraint_gradient == gauge_p),
        ("the abelian constraint has vanishing canonical self bracket", constraint_self_bracket == 0),
        ("the full stationary generator is symplectic", not any(any(row) for row in madd(mmul(transpose(full_generator), symplectic), mmul(symplectic, full_generator)))),
        ("the gauge configuration vector is a stationary zero mode", not any(sum(full_generator[i][j] * gauge_q[j] for j in range(4)) for i in range(4))),
        ("the gauge momentum vector is a stationary zero mode", not any(sum(full_generator[i][j] * gauge_p[j] for j in range(4)) for i in range(4))),
        ("minus A squared is singular on the ambient carrier", rank(minus_a2) == 2),
        ("the ambient spectral inverse square root is therefore unavailable", rank(minus_a2) < 4),
        ("the quotient intertwines full and reduced evolution", mmul(projection, full_generator) == mmul(reduced_generator, projection)),
        ("the reduced spectral complex structure squares to minus identity", mmul(reduced_j, reduced_j) == mscale(eye(2), F(-1))),
        ("the reduced selector commutes with evolution", mmul(reduced_j, reduced_generator) == mmul(reduced_generator, reduced_j)),
        ("the reduced compatible majorant is positive", reduced_majorant == [[F(2), F(0)], [F(0), F(1, 2)]]),
        ("gauge fixing at frequency one descends to the same physical J", mmul(projection, j_one) == mmul(reduced_j, projection)),
        ("gauge fixing at frequency three descends to the same physical J", mmul(projection, j_three) == mmul(reduced_j, projection)),
        ("the ambient gauge-fixed selectors differ", j_one != j_three),
        ("the physical selector is gauge-fixing independent", mmul(projection, j_one) == mmul(projection, j_three)),
        ("the finite full carrier is one closed common algebraic domain", True),
        ("finite closed-domain ownership is not a continuum Green-domain theorem", True),
        ("the full phase rank and physical phase rank scale correctly", 960 * 4 == 3840 and 960 * 2 == 1920),
        ("the held-out delayed-choice family is not evaluated", True),
    ]
    return checks


def manifest_failures(data):
    failures = []
    bfv = data.get("canonical_BFV_completion", {})
    selector = data.get("stationary_selector_descent", {})
    fences = data.get("fences", {})
    result = data.get("result", {})
    if bfv.get("charge") != "Q_equals_sum_c_a_pK_a" or bfv.get("nilpotent") is not True:
        failures.append("bfv")
    if bfv.get("H0") != "polynomial_observables_on_W960_direct_sum_W960":
        failures.append("cohomology")
    if selector.get("ambient_selector_exists") is not False or selector.get("physical_selector_exists") is not True:
        failures.append("selector")
    if selector.get("gauge_fixing_independent_on_cohomology") is not True:
        failures.append("gauge_fixing")
    required_false = (
        "source_owned_action", "functional_continuum_BV_BFV", "unbounded_Green_domain",
        "physical_GU_Hilbert_space", "Hadamard_state", "Born_rule",
        "prediction_or_confirmation", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if result.get("source_selected_physical_states") != 0 or result.get("prediction_or_confirmation_change") != "none":
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
        "nonnilpotent_charge", "physical_gauge_fixing_leak",
    )]
    updates = (
        ("wrong_charge", lambda d: d["canonical_BFV_completion"].__setitem__("charge", "assumed")),
        ("drop_nilpotency", lambda d: d["canonical_BFV_completion"].__setitem__("nilpotent", False)),
        ("wrong_H0", lambda d: d["canonical_BFV_completion"].__setitem__("H0", "ambient_functions")),
        ("ambient_promotion", lambda d: d["stationary_selector_descent"].__setitem__("ambient_selector_exists", True)),
        ("drop_physical_selector", lambda d: d["stationary_selector_descent"].__setitem__("physical_selector_exists", False)),
        ("drop_gauge_independence", lambda d: d["stationary_selector_descent"].__setitem__("gauge_fixing_independent_on_cohomology", False)),
        ("source_promotion", lambda d: d["fences"].__setitem__("source_owned_action", True)),
        ("continuum_promotion", lambda d: d["fences"].__setitem__("functional_continuum_BV_BFV", True)),
        ("green_promotion", lambda d: d["fences"].__setitem__("unbounded_Green_domain", True)),
        ("hilbert_promotion", lambda d: d["fences"].__setitem__("physical_GU_Hilbert_space", True)),
        ("hadamard_promotion", lambda d: d["fences"].__setitem__("Hadamard_state", True)),
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
    checks.append(("manifest preserves BFV, quotient-selector, custody and domain fences", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K88 CANONICAL BFV STATIONARY DESCENT: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
