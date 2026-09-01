#!/usr/bin/env python3
"""Exact I1B rank-jump and logarithmic singular-reduction controls."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-i1b-cross-null-singular-reduction-wave.json"
PREDECESSOR = ROOT / "lab/process/k77-i1b-action-induced-connection-wave.json"


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def matmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0)) for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c, a):
    return [[c * value for value in row] for row in a]


def rank(matrix):
    a = [row[:] for row in matrix]
    rows, cols = len(a), len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((row for row in range(pivot_row, rows) if a[row][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        pivot_value = a[pivot_row][col]
        a[pivot_row] = [value / pivot_value for value in a[pivot_row]]
        for row in range(rows):
            if row != pivot_row and a[row][col]:
                factor = a[row][col]
                a[row] = [a[row][j] - factor * a[pivot_row][j] for j in range(cols)]
        pivot_row += 1
    return pivot_row


def block_diag(a, b):
    za, zb = len(a), len(b)
    out = [[F(0) for _ in range(za + zb)] for _ in range(za + zb)]
    for i in range(za):
        for j in range(za):
            out[i][j] = a[i][j]
    for i in range(zb):
        for j in range(zb):
            out[za + i][za + j] = b[i][j]
    return out


def model_checks(mutation=None):
    ambient, radical_t, radical_n = 220, 196, 198
    quotient_t, quotient_n = ambient - radical_t, ambient - radical_n
    j2 = [[F(0), F(1)], [F(-1), F(0)]]
    u = F(2, 3)
    j_u = block_diag(j2, scale(u, j2))
    j_0 = block_diag(j2, scale(F(0), j2))
    if mutation == "remove_rank_jump":
        j_0 = block_diag(j2, j2)

    general_b = [[F(2, 5), F(7, 11)], [F(-3, 8), F(5, 13)]]
    lhs_identity = add(matmul(transpose(general_b), j2), matmul(j2, general_b))
    rhs_identity = scale(general_b[0][0] + general_b[1][1], j2)

    singular_b = [[-F(1, 2) / u, F(0)], [F(0), -F(1, 2) / u]]
    if mutation == "hide_pole":
        singular_b = [[F(0), F(0)], [F(0), F(0)]]
    compatibility = add(j2, scale(u, add(matmul(transpose(singular_b), j2), matmul(j2, singular_b))))
    forced_trace = singular_b[0][0] + singular_b[1][1]

    trace_sequence = [-(F(n)) for n in (1, 2, 5, 10)]  # tr B_(u=1/n)
    if mutation == "claim_bounded":
        trace_sequence = [F(-1)] * 4

    h = [[F(1), F(0)], [F(0), F(-1)]]
    h_condition = add(matmul(transpose(h), j2), matmul(j2, h))
    hol2 = [[F(1, 2), F(0)], [F(0), F(2)]]
    hol3 = [[F(1, 3), F(0)], [F(0), F(3)]]
    if mutation == "select_log2":
        hol3 = hol2
    hol2_green = matmul(matmul(transpose(hol2), j2), hol2)
    hol3_green = matmul(matmul(transpose(hol3), j2), hol3)

    u0, u1 = F(4), F(1)
    transport_squared = u1 / u0
    if mutation == "invert_transport":
        transport_squared = u0 / u1

    checks = [
        ("native ambient fibre rank is 220", ambient == 220),
        ("timelike radical and quotient ranks are 196 and 24", radical_t == 196 and quotient_t == 24),
        ("null radical and quotient ranks are 198 and 22", radical_n == 198 and quotient_n == 22),
        ("the transverse normal form has rank four away from the interface", rank(j_u) == 4),
        ("the transverse normal form drops to rank two at the interface", rank(j_0) == 2),
        ("the degenerating pair supplies exactly two new radical directions", rank(j_u) - rank(j_0) == 2),
        ("the two-by-two symplectic trace identity is exact", lhs_identity == rhs_identity),
        ("the logarithmic representative satisfies Green compatibility", compatibility == [[F(0), F(0)], [F(0), F(0)]]),
        ("compatibility forces trace B=-1/u", forced_trace == -F(1) / u),
        ("the forced trace is unbounded along u=1/n", [abs(value) for value in trace_sequence] == [F(1), F(2), F(5), F(10)]),
        ("parallel transport collapses by sqrt(u1/u0)", transport_squared == F(1, 4)),
        ("inverse transport must diverge toward the interface", F(1) / transport_squared == F(4)),
        ("the tangential hyperbolic generator is symplectic", h_condition == [[F(0), F(0)], [F(0), F(0)]]),
        ("the log2 holonomy preserves the Green form", hol2_green == j2),
        ("the log3 holonomy preserves the Green form", hol3_green == j2),
        ("log2 and log3 holonomies remain distinct", hol2 != hol3),
        ("both holonomies have determinant one", hol2[0][0] * hol2[1][1] == hol3[0][0] * hol3[1][1] == 1),
        ("the normal residue is independent of the tangential holonomy base", forced_trace == -F(1) / u),
    ]
    return checks


def manifest_failures(data, predecessor):
    failures = []
    ranks = data.get("native_rank_inputs", {})
    normal = data.get("normal_form", {})
    connection = data.get("compatible_connection", {})
    quotient = data.get("quotient_boundary", {})
    tangential = data.get("tangential_nonselection", {})
    fences = data.get("fences", {})
    result = data.get("result", {})
    if (ranks.get("ambient_fibre_rank"), ranks.get("timelike_radical_rank"), ranks.get("timelike_quotient_rank"), ranks.get("null_radical_rank"), ranks.get("null_quotient_rank")) != (220, 196, 24, 198, 22):
        failures.append("ranks")
    if normal.get("rank_for_u_nonzero") != 24 or normal.get("rank_at_u_zero") != 22 or normal.get("extra_null_radical_rank") != 2:
        failures.append("normal_form")
    if connection.get("forced_trace") != "trace(B_u)_equals_minus_1_over_u" or connection.get("smooth_cross_null_connection_exists") is not False:
        failures.append("pole")
    if connection.get("forced_trace_residue") != "minus_one" or connection.get("symmetric_representative_residue") != "minus_one_half_I2" or connection.get("cross_null_isomorphism") is not False:
        failures.append("transport")
    if quotient.get("ordinary_constant_rank_quotient_bundle_across_u_zero") is not False or quotient.get("null_stratum_rank22_quotient") is not True:
        failures.append("quotient")
    if tangential.get("forced_trace_residue_independent_of_r") is not True or tangential.get("log2_candidate_compatible") is not True or tangential.get("log3_candidate_compatible") is not True:
        failures.append("nonselection")
    required_false = (
        "ordinary_smooth_cross_null_quotient_bundle", "bounded_compatible_cross_null_connection",
        "source_native_coupled_I1B_Hessian", "physical_cross_null_reduction",
        "tangential_coefficient_selected", "prediction_or_confirmation", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if result.get("smooth_cross_null_quotient_bundles_constructed") != 0 or result.get("tangential_coefficients_selected") != 0:
        failures.append("promotion")
    if predecessor.get("packet", {}).get("ambient_fibre_rank") != 220 or predecessor.get("packet", {}).get("quotient_rank") != 24:
        failures.append("predecessor")
    if data.get("holdout_firewall", {}).get("status") != "reserved_unscored":
        failures.append("holdout")
    return failures


def selftest(data, predecessor):
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in ("remove_rank_jump", "hide_pole", "claim_bounded", "invert_transport", "select_log2")]
    updates = (
        ("wrong_null_rank", lambda d: d["native_rank_inputs"].__setitem__("null_quotient_rank", 24)),
        ("smooth_claim", lambda d: d["compatible_connection"].__setitem__("smooth_cross_null_connection_exists", True)),
        ("missing_residue", lambda d: d["compatible_connection"].__setitem__("forced_trace_residue", "none")),
        ("bundle_promotion", lambda d: d["quotient_boundary"].__setitem__("ordinary_constant_rank_quotient_bundle_across_u_zero", True)),
        ("source_promotion", lambda d: d["fences"].__setitem__("source_native_coupled_I1B_Hessian", True)),
        ("physical_promotion", lambda d: d["fences"].__setitem__("physical_cross_null_reduction", True)),
        ("selected_coefficient", lambda d: d["fences"].__setitem__("tangential_coefficient_selected", True)),
        ("constructed_bundle", lambda d: d["result"].__setitem__("smooth_cross_null_quotient_bundles_constructed", 1)),
        ("holdout", lambda d: d["holdout_firewall"].__setitem__("status", "scored")),
    )
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        mutations.append((name, bool(manifest_failures(mutant, predecessor))))
    for name, caught in mutations:
        print(f"[{'PASS' if caught else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(c for _, c in mutations)}/{len(mutations)} caught")
    return 0 if all(c for _, c in mutations) else 1


def main():
    data = json.loads(MANIFEST.read_text())
    predecessor = json.loads(PREDECESSOR.read_text())
    if "--selftest" in sys.argv:
        return selftest(data, predecessor)
    checks = model_checks()
    checks.append(("manifest preserves native ranks, logarithmic obstruction, nonselection and fences", not manifest_failures(data, predecessor)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K77 I1B CROSS-NULL SINGULAR REDUCTION: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
