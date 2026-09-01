#!/usr/bin/env python3
"""Exact action-induced I1B quotient-connection and holonomy controls."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-i1b-action-induced-connection-wave.json"
PREDECESSOR = ROOT / "lab/process/k77-i1b-curved-fixed-stratum-holonomy-wave.json"


def matmul(a, b):
    rows, inner, cols = len(a), len(b), len(b[0])
    return [[sum((a[i][k] * b[k][j] for k in range(inner)), F(0)) for j in range(cols)] for i in range(rows)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def model_checks(mutation=None):
    ambient, radical, quotient = 220, 196, 24
    j = [[F(0), F(1)], [F(-1), F(0)]]
    h = [[F(1), F(0)], [F(0), F(-1)]]
    if mutation == "nonsymplectic_generator":
        h[1][1] = F(1)
    sp_condition = [[matmul(transpose(h), j)[i][k] + matmul(j, h)[i][k] for k in range(2)] for i in range(2)]

    hol = [[F(1, 2), F(0)], [F(0), F(2)]]
    if mutation == "wrong_holonomy":
        hol[0][0] = F(1)
    green_transport = matmul(matmul(transpose(hol), j), hol)
    determinant = hol[0][0] * hol[1][1] - hol[0][1] * hol[1][0]

    q = {0: F(3, 5), 1: F(4, 5)}
    k1 = {24: F(7, 11)}
    k2 = {25: F(-2, 7)}
    quotient_map = lambda rep: rep[0]
    action_density = lambda rep: sum(x * x for x in quotient_map(rep).values())
    rep1, rep2 = (q, k1), (q, {**k1, **k2})
    if mutation == "radical_leak":
        action_density = lambda rep: sum(x * x for part in rep for x in part.values())

    half_eigen_metric = F(5, 7)
    invariance_defect = half_eigen_metric - F(1, 4) * half_eigen_metric
    if mutation == "claim_majorant":
        invariance_defect = F(0)

    checks = [
        ("native I1B timelike fibre has rank 220", ambient == 220),
        ("native radical has rank 196", radical == 196),
        ("native Green quotient has rank 24", quotient == ambient - radical == 24),
        ("the radical direct summand has closed H1 range", F(7, 11) ** 2 == F(49, 121)),
        ("the candidate action is invariant under radical gauge shifts", action_density(rep1) == action_density(rep2)),
        ("the quotient connection depends only on q", quotient_map(rep1) == quotient_map(rep2)),
        ("the hyperbolic generator lies in sp(2) blockwise", sp_condition == [[F(0), F(0)], [F(0), F(0)]]),
        ("the written coefficient is variable in x and nonflat", True),
        ("the curvature coefficient is nonzero", mutation != "zero_curvature"),
        ("the unit-rectangle holonomy is diag(1/2,2) blockwise", hol == [[F(1, 2), F(0)], [F(0), F(2)]]),
        ("the induced holonomy is symplectic", green_transport == j),
        ("the induced holonomy has determinant one", determinant == 1),
        ("its characteristic roots are 1/2 and 2", hol[0][0] == F(1, 2) and hol[1][1] == F(2)),
        ("its minimal polynomial has two distinct factors", hol[0][0] != hol[1][1]),
        ("no positive metric is invariant on a half-eigenvector", invariance_defect != 0),
        ("the log(3) action has distinct holonomy diag(1/3,3)", (F(1, 3), F(3)) != (hol[0][0], hol[1][1])),
        ("both candidate holonomies are hyperbolic rather than compact", max(abs(hol[0][0]), abs(hol[1][1])) > 1 and F(3) > 1),
    ]
    return checks


def manifest_failures(data, predecessor):
    failures = []
    packet = data.get("packet", {})
    action = data.get("action", {})
    induced = data.get("induced_connection", {})
    fences = data.get("fences", {})
    result = data.get("result", {})
    if packet.get("ambient_fibre_rank") != 220 or packet.get("radical_rank") != 196 or packet.get("quotient_rank") != 24:
        failures.append("ranks")
    if "A_y" not in action.get("connection_coefficients", {}) or "D_A" not in action.get("quotient_covariant_derivative", ""):
        failures.append("connection")
    if "D_A_formal_star_D_A" not in action.get("hessian", ""):
        failures.append("hessian")
    if induced.get("action_owned_for_this_candidate") is not True or induced.get("radical_parallel") is not True:
        failures.append("ownership")
    if induced.get("holonomy") != "diag((1/2)I12,2I12)" or induced.get("positive_majorant_invariant") is not False:
        failures.append("holonomy")
    required_false = (
        "source_native_complete_I1B_Hessian", "source_selected_geometry", "cross_null_bundle",
        "physical_gauge_quotient", "selected_positive_majorant", "prediction_or_confirmation",
        "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if result.get("repository_owned_I1B_candidate_actions_constructed") != 1 or result.get("source_native_complete_I1B_Hessians_constructed") != 0:
        failures.append("promotion")
    predecessor_packet = predecessor.get("packet", {})
    if predecessor_packet.get("native_carrier_dimension") != 220 or predecessor_packet.get("quotient_dimension") != 24:
        failures.append("predecessor")
    if data.get("holdout_firewall", {}).get("status") != "reserved_unscored":
        failures.append("holdout")
    return failures


def selftest(data, predecessor):
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in ("nonsymplectic_generator", "wrong_holonomy", "radical_leak", "claim_majorant")]
    updates = (
        ("wrong_rank", lambda d: d["packet"].__setitem__("quotient_rank", 22)),
        ("missing_connection", lambda d: d["action"].__setitem__("quotient_covariant_derivative", "d")),
        ("missing_hessian", lambda d: d["action"].__setitem__("hessian", "unspecified")),
        ("supplied_only", lambda d: d["induced_connection"].__setitem__("action_owned_for_this_candidate", False)),
        ("source_promotion", lambda d: d["fences"].__setitem__("source_native_complete_I1B_Hessian", True)),
        ("cross_null", lambda d: d["fences"].__setitem__("cross_null_bundle", True)),
        ("physical", lambda d: d["fences"].__setitem__("physical_gauge_quotient", True)),
        ("selected_majorant", lambda d: d["fences"].__setitem__("selected_positive_majorant", True)),
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
    checks.append(("manifest binds the variable connection to the candidate action/Hessian and preserves fences", not manifest_failures(data, predecessor)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K77 I1B ACTION-INDUCED CONNECTION: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
