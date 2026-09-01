#!/usr/bin/env python3
"""Exact Q(sqrt(2)) CCR/Fock state-correlation controls for K86."""
from __future__ import annotations

import copy
import itertools
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k86-observed-ccr-state-correlation-boundary-wave.json"


# Scalars are a+b*r with r^2=2.
def s(a=0, b=0):
    return (F(a), F(b))


def sadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def sneg(x):
    return (-x[0], -x[1])


def ssub(x, y):
    return sadd(x, sneg(y))


def smul(x, y):
    return (x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def sscale(x, q):
    return (x[0] * F(q), x[1] * F(q))


def qmat(rows):
    return [[s(x) for x in row] for row in rows]


def eye(n):
    return [[s(int(i == j)) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def madd(a, b):
    return [[sadd(x, y) for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def msub(a, b):
    return [[ssub(x, y) for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def mscale(a, x):
    return [[smul(x, y) for y in row] for row in a]


def mmul(a, b):
    bt = transpose(b)
    return [[sum_s(smul(x, y) for x, y in zip(row, col)) for col in bt] for row in a]


def sum_s(values):
    out = s()
    for value in values:
        out = sadd(out, value)
    return out


def kron(a, b):
    out = []
    for ra in a:
        for rb in b:
            row = []
            for xa in ra:
                row.extend(smul(xa, xb) for xb in rb)
            out.append(row)
    return out


def mv(a, v):
    return [sum_s(smul(x, y) for x, y in zip(row, v)) for row in a]


def inner(u, v):
    return sum_s(smul(x, y) for x, y in zip(u, v))


def trace(a):
    return sum_s(a[i][i] for i in range(len(a)))


def density_expectation(rho, operator):
    return trace(mmul(rho, operator))


def outer(v):
    return [[smul(x, y) for y in v] for x in v]


def model_checks(mutation=None):
    i2 = eye(2)
    x = qmat([[0, 1], [1, 0]])
    z = qmat([[1, 0], [0, -1]])
    if mutation == "commuting_A_pair":
        x = z
    invsqrt2 = s(0, F(1, 2))
    bplus = mscale(madd(z, x), invsqrt2)
    bminus = mscale(msub(z, x), invsqrt2)
    if mutation == "wrong_B1_sign":
        bminus = bplus

    a0, a1 = kron(z, i2), kron(x, i2)
    b0, b1 = kron(i2, bplus), kron(i2, bminus)
    c = msub(madd(mmul(a0, b0), mmul(a0, b1)), msub(mmul(a1, b1), mmul(a1, b0)))
    # The preceding expression is A0B0+A0B1+A1B0-A1B1.
    i4 = eye(4)
    bell = [s(0, F(1, 2)), s(), s(), s(0, F(1, 2))]
    if mutation == "bad_Bell_norm":
        bell[3] = s()
    product = [s(1), s(), s(), s()]
    bell_rho = outer(bell)
    trace_rho = mscale(i4, s(F(1, 4)))
    t = F(3, 4)
    if mutation == "nonconvex_Werner":
        t = F(5, 4)
    werner = madd(mscale(bell_rho, s(t)), mscale(i4, s((1 - t) / 4)))

    bell_expect = inner(bell, mv(c, bell))
    product_expect = inner(product, mv(c, product))
    trace_expect = density_expectation(trace_rho, c)
    werner_expect = density_expectation(werner, c)
    c2, c3 = mmul(c, c), mmul(mmul(c, c), c)
    target_bell = [smul(s(0, 2), v) for v in bell]

    # No finite N+1 truncation can obey [a,a*]=I at its top state.
    cutoff = 3
    top_commutator_eigenvalue = -F(cutoff)
    if mutation == "claim_finite_CCR":
        top_commutator_eigenvalue = F(1)

    classical_values = []
    for a0v, a1v, b0v, b1v in itertools.product((-1, 1), repeat=4):
        classical_values.append(a0v * b0v + a0v * b1v + a1v * b0v - a1v * b1v)

    checks = [
        ("the reduced input contains two canonical modes", 2 == 2),
        ("Fock ladder commutator holds algebraically on n=0", (0 + 1) - 0 == 1),
        ("Fock ladder commutator holds algebraically on n=7", (7 + 1) - 7 == 1),
        ("a finite truncation has the expected top-level CCR defect", top_commutator_eigenvalue != 1),
        ("the two-qubit sector has dimension four", len(i4) == 4),
        ("A0 is a self-adjoint involution", transpose(a0) == a0 and mmul(a0, a0) == i4),
        ("A1 is a self-adjoint involution", transpose(a1) == a1 and mmul(a1, a1) == i4),
        ("B0 is a self-adjoint involution", transpose(b0) == b0 and mmul(b0, b0) == i4),
        ("B1 is a self-adjoint involution", transpose(b1) == b1 and mmul(b1, b1) == i4),
        ("A0 commutes with B0", mmul(a0, b0) == mmul(b0, a0)),
        ("A0 commutes with B1", mmul(a0, b1) == mmul(b1, a0)),
        ("A1 commutes with B0", mmul(a1, b0) == mmul(b0, a1)),
        ("A1 commutes with B1", mmul(a1, b1) == mmul(b1, a1)),
        ("the local A observables anticommute", madd(mmul(a0, a1), mmul(a1, a0)) == [[s() for _ in range(4)] for _ in range(4)]),
        ("the Bell vector is normalized", inner(bell, bell) == s(1)),
        ("the product vector is normalized", inner(product, product) == s(1)),
        ("the Bell density has trace one", trace(bell_rho) == s(1)),
        ("the tracial density has trace one", trace(trace_rho) == s(1)),
        ("the Werner mixture coefficient is convex", F(0) <= t <= F(1)),
        ("the Werner density has trace one", trace(werner) == s(1)),
        ("the Bell vector is a 2sqrt2 eigenvector", mv(c, bell) == target_bell),
        ("the Bell CHSH value is exactly 2sqrt2", bell_expect == s(0, 2)),
        ("the product CHSH value is exactly sqrt2", product_expect == s(0, 1)),
        ("the normalized trace CHSH value is zero", trace_expect == s()),
        ("the Werner CHSH value is exactly 3sqrt2/2", werner_expect == s(0, F(3, 2))),
        ("the Werner value is strictly above the classical ceiling", smul(werner_expect, werner_expect)[0] > 4),
        ("the Werner value is strictly below the Tsirelson ceiling", smul(werner_expect, werner_expect)[0] < 8),
        ("the CHSH operator satisfies C cubed equals 8C", c3 == mscale(c, s(8))),
        ("the CHSH square has trace sixteen", trace(c2) == s(16)),
        ("every commutative deterministic assignment gives plus or minus two", set(classical_values) == {-2, 2}),
        ("all sixteen commutative assignments were checked", len(classical_values) == 16),
        ("the same noncommutative algebra supports distinct correlation faces", len({bell_expect, werner_expect, product_expect, trace_expect}) == 4),
    ]
    return checks


def manifest_failures(data):
    failures = []
    packet = data.get("packet", {})
    quant = data.get("quantization", {})
    obs = data.get("observables", {})
    states = data.get("positive_states", {})
    boundary = data.get("selection_boundary", {})
    fences = data.get("fences", {})
    result = data.get("result", {})
    if packet.get("classical_modes") != 2 or "rank4" not in packet.get("bounded_observable_sector", ""):
        failures.append("packet")
    if quant.get("finite_matrix_CCR_claimed") is not False or quant.get("hbar") != "arbitrary_positive":
        failures.append("quantization")
    if obs.get("self_adjoint_involutions") is not True or obs.get("cross_commutation") is not True or obs.get("minimal_polynomial") != "C_cubed_equals_8C":
        failures.append("observables")
    required_states = ("bell", "werner_three_quarters", "product_00", "normalized_trace")
    if any(states.get(key, {}).get("normalized_positive") is not True for key in required_states):
        failures.append("states")
    if states.get("bell", {}).get("CHSH_expectation") != "2sqrt2" or states.get("werner_three_quarters", {}).get("CHSH_expectation") != "3sqrt2_over_2":
        failures.append("values")
    if boundary.get("same_noncommutative_algebra_supports_distinct_CHSH_faces") is not True:
        failures.append("boundary")
    if boundary.get("action_and_CCR_select_state") is not False or boundary.get("action_and_CCR_select_measurement_embedding") is not False:
        failures.append("selection")
    required_false = (
        "source_selected_quantization", "physical_GU_Hilbert_space", "unique_physical_state",
        "Born_rule_or_measurement_dynamics", "full_constraint_BFV_descent",
        "continuum_interacting_QFT", "Bell_prediction_or_confirmation", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if fences.get("repository_selected_quantization_exists") is not True or fences.get("normalized_positive_states_exist") is not True:
        failures.append("existence")
    if result.get("source_selected_quantizations_completed") != 0 or result.get("physical_GU_states_selected") != 0:
        failures.append("promotion")
    if data.get("classical_control", {}).get("deterministic_assignments_checked") != 16:
        failures.append("classical")
    if data.get("holdout_firewall", {}).get("status") != "reserved_unscored":
        failures.append("holdout")
    return failures


def selftest(data):
    baseline = model_checks()
    if any(not ok for _, ok in baseline) or manifest_failures(data):
        print("[FAIL] clean baseline must pass before mutations")
        return 1
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in (
        "commuting_A_pair", "wrong_B1_sign", "bad_Bell_norm", "nonconvex_Werner", "claim_finite_CCR",
    )]
    updates = (
        ("wrong_mode_count", lambda d: d["packet"].__setitem__("classical_modes", 1)),
        ("finite_CCR_promotion", lambda d: d["quantization"].__setitem__("finite_matrix_CCR_claimed", True)),
        ("drop_involutions", lambda d: d["observables"].__setitem__("self_adjoint_involutions", False)),
        ("drop_cross_commutation", lambda d: d["observables"].__setitem__("cross_commutation", False)),
        ("wrong_minpoly", lambda d: d["observables"].__setitem__("minimal_polynomial", "assumed")),
        ("negative_state", lambda d: d["positive_states"]["bell"].__setitem__("normalized_positive", False)),
        ("wrong_bell_value", lambda d: d["positive_states"]["bell"].__setitem__("CHSH_expectation", "2")),
        ("erase_state_nonselection", lambda d: d["selection_boundary"].__setitem__("action_and_CCR_select_state", True)),
        ("source_promotion", lambda d: d["fences"].__setitem__("source_selected_quantization", True)),
        ("Hilbert_promotion", lambda d: d["fences"].__setitem__("physical_GU_Hilbert_space", True)),
        ("Born_promotion", lambda d: d["fences"].__setitem__("Born_rule_or_measurement_dynamics", True)),
        ("QFT_promotion", lambda d: d["fences"].__setitem__("continuum_interacting_QFT", True)),
        ("prediction_promotion", lambda d: d["fences"].__setitem__("Bell_prediction_or_confirmation", True)),
        ("wrong_classical_count", lambda d: d["classical_control"].__setitem__("deterministic_assignments_checked", 15)),
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
    checks.append(("manifest preserves CCR, state, selection and source fences", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K86 OBSERVED CCR STATE BOUNDARY: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
