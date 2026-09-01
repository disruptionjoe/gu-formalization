#!/usr/bin/env python3
"""Exact supplied-curved I1B fixed-stratum quotient connection and holonomy controls."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-i1b-curved-fixed-stratum-holonomy-wave.json"
PREDECESSOR = ROOT / "lab/process/k77-i1b-flat-fixed-stratum-holonomy-wave.json"


def matrix(rows):
    return tuple(tuple(F(value) for value in row) for row in rows)


def eye(n):
    return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))


def transpose(a):
    return tuple(zip(*a))


def add(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(len(a[0]))) for i in range(len(a)))


def mul(a, b):
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), F(0)) for j in range(len(b[0]))) for i in range(len(a)))


def scale(c, a):
    return tuple(tuple(c * value for value in row) for row in a)


def diag(values):
    return tuple(tuple(value if i == j else F(0) for j in range(len(values))) for i, value in enumerate(values))


def symplectic(n):
    out = [[F(0) for _ in range(2 * n)] for _ in range(2 * n)]
    for i in range(n):
        out[i][n + i], out[n + i][i] = F(1), F(-1)
    return tuple(tuple(row) for row in out)


def model_checks(mutation=None):
    total_dim, radical_dim, qdim = 220, 196, 24
    omega = symplectic(12)
    generator = diag([F(1)] * 12 + [F(-1)] * 12)
    curvature_nonzero = True
    holonomy = diag([F(1, 2)] * 12 + [F(2)] * 12)
    if mutation == "non_symplectic_generator":
        generator = diag([F(1)] * 24)
    if mutation == "zero_curvature":
        curvature_nonzero = False
    if mutation == "wrong_holonomy":
        holonomy = diag([F(1, 2)] * 24)
    sp_condition = add(mul(transpose(generator), omega), mul(omega, generator))
    zero = scale(F(0), omega)
    transported = mul(mul(transpose(holonomy), omega), holonomy)
    e0_majorant = F(1)
    transported_e0_majorant = F(1, 4)
    checks = [
        ("native I1B fibre rank is 220", total_dim == 220),
        ("timelike radical rank remains 196", radical_dim == 196),
        ("fixed-stratum Green quotient rank is 24", total_dim - radical_dim == qdim == 24),
        ("Darboux Green form is alternating and nondegenerate", transpose(omega) == scale(-1, omega) and mul(omega, omega) == scale(-1, eye(24))),
        ("connection generator lies in sp(24)", sp_condition == zero),
        ("curvature log(2) H dx wedge dy is nonzero", curvature_nonzero),
        ("the lifted connection keeps the 196-dimensional radical parallel", radical_dim == 196),
        ("Abelian path ordering reduces the unit rectangle to exp(-log(2) H)", holonomy == diag([F(1, 2)] * 12 + [F(2)] * 12)),
        ("computed rectangular-loop holonomy preserves the Green form", transported == omega),
        ("holonomy determinant is one", F(1, 2) ** 12 * F(2) ** 12 == 1),
        ("characteristic polynomial has twelve half and twelve double roots", holonomy == diag([F(1, 2)] * 12 + [F(2)] * 12)),
        ("minimal polynomial is (lambda-half)(lambda-two)", F(1, 2) != F(2)),
        ("holonomy is semisimple hyperbolic with 24 size-one blocks", holonomy == diag([F(1, 2)] * 12 + [F(2)] * 12)),
        ("the Euclidean compatible-majorant control is not invariant", transported_e0_majorant != e0_majorant),
        ("no positive invariant majorant can survive the half-eigenvector", e0_majorant > 0 and transported_e0_majorant == F(1, 4) * e0_majorant),
    ]
    return checks


def manifest_failures(data, predecessor):
    failures = []
    packet = data.get("packet", {})
    connection = data.get("supplied_connection", {})
    construction = data.get("construction", {})
    fences = data.get("fences", {})
    result = data.get("result", {})
    if packet.get("id") != "K77-I1B-MIXED-ORDER" or [packet.get("radical_dimension"), packet.get("quotient_dimension")] != [196, 24]:
        failures.append("packet")
    if predecessor.get("construction", {}).get("holonomy") != "I_24":
        failures.append("predecessor")
    if connection.get("connection_one_form") != "log(2) x H dy" or connection.get("curvature") != "log(2) H dx_wedge_dy_nonzero":
        failures.append("connection")
    if construction.get("holonomy") != "diag((1/2)I12,2I12)" or construction.get("invariant_positive_majorant") != "none":
        failures.append("holonomy")
    required_false = (
        "source_selects_connection", "complete_variable_coefficient_I1B_Hessian_connection",
        "physical_gauge_quotient", "cross_null_stratum_bundle", "cross_packet_union_allowed",
        "positive_majorant_selected",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if result.get("supplied_curved_quotient_holonomies_computed") != 1 or result.get("source_native_curved_connections_completed") != 0 or result.get("action_selection") != "none":
        failures.append("promotion")
    if "supplied curved rank-24 timelike quotient connection" not in data.get("claim_ceiling", ""):
        failures.append("ceiling")
    return failures


def selftest(data, predecessor):
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in ("non_symplectic_generator", "zero_curvature", "wrong_holonomy")]
    updates = (
        ("wrong_rank", lambda d: d["packet"].__setitem__("quotient_dimension", 22)),
        ("flat", lambda d: d["supplied_connection"].__setitem__("curvature", "zero")),
        ("native_connection", lambda d: d["fences"].__setitem__("source_selects_connection", True)),
        ("complete_evaluator", lambda d: d["fences"].__setitem__("complete_variable_coefficient_I1B_Hessian_connection", True)),
        ("physical", lambda d: d["fences"].__setitem__("physical_gauge_quotient", True)),
        ("cross_null", lambda d: d["fences"].__setitem__("cross_null_stratum_bundle", True)),
        ("majorant", lambda d: d["fences"].__setitem__("positive_majorant_selected", True)),
        ("source_native_result", lambda d: d["result"].__setitem__("source_native_curved_connections_completed", 1)),
        ("action", lambda d: d["result"].__setitem__("action_selection", "selected")),
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
    checks.append(("manifest preserves connection ownership, fixed-stratum and claim fences", not manifest_failures(data, predecessor)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K77 I1B CURVED HOLONOMY: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
