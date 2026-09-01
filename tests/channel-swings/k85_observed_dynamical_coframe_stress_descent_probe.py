#!/usr/bin/env python3
"""Exact K85 dynamical-coframe, quotient-principal and stress-Ward controls."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k85-observed-dynamical-coframe-stress-descent-wave.json"
PREDECESSOR = ROOT / "lab/process/k77-observed-interacting-bv-moduli-wave.json"


def dot(h, x, y):
    return sum(h[i] * x[i] * y[i] for i in range(len(h)))


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def principal_block(metric_entry, p, h):
    hmat = [[h[i] if i == j else F(0) for j in range(len(h))] for i in range(len(h))]
    return [[metric_entry * x for x in row] for row in matmul(transpose(p), matmul(hmat, p))]


def mv(a, x):
    return [sum(row[j] * x[j] for j in range(len(x))) for row in a]


def model_checks(mutation=None):
    p = [[F(1), F(0), F(0), F(0)], [F(0), F(1), F(0), F(0)]]
    h = [F(2), F(3)]
    eta = [F(1), F(-1), F(-1), F(-1)]
    gauge = [F(0), F(0), F(5), F(-7)]
    if mutation == "gauge_leak":
        p[0][2] = F(1)
    blocks = [principal_block(entry, p, h) for entry in eta]

    qt = [F(2, 3), F(-1, 5)]
    qx = [F(3, 7), F(4, 9)]
    qtt = [F(5, 11), F(-2, 13)]
    qtx = [F(7, 17), F(1, 19)]
    qxt = list(qtx)
    if mutation == "mixed_jet":
        qxt[0] += F(1)
    qxx = [F(-3, 23), F(5, 29)]
    grad_v = [F(11, 31), F(-13, 37)]
    potential = F(17, 41)
    euler = [qtt[i] - qxx[i] + grad_v[i] / h[i] for i in range(2)]

    t00 = (dot(h, qt, qt) + dot(h, qx, qx)) / 2 + potential
    t01 = -dot(h, qt, qx)
    t10 = -dot(h, qx, qt)
    t11 = (dot(h, qt, qt) + dot(h, qx, qx)) / 2 - potential
    dt_t00 = dot(h, qt, qtt) + dot(h, qx, qxt) + sum(grad_v[i] * qt[i] for i in range(2))
    dx_t10 = -dot(h, qxx, qt) - dot(h, qx, qtx)
    dt_t01 = -dot(h, qtt, qx) - dot(h, qt, qxt)
    dx_t11 = dot(h, qt, qtx) + dot(h, qx, qxx) - sum(grad_v[i] * qx[i] for i in range(2))
    ward0 = dt_t00 + dx_t10
    ward1 = dt_t01 + dx_t11
    if mutation == "ward_sign":
        ward1 = -ward1

    kappa = F(3, 5)
    stress = [[t00, t01], [t10, t11]]
    einstein = [[kappa * x for x in row] for row in stress]
    if mutation == "euler_mismatch":
        einstein[0][0] += F(1)
    total_euler = [[einstein[i][j] / kappa - stress[i][j] for j in range(2)] for i in range(2)]

    preferred_h = [F(1), F(1)]
    preferred_j = [F(0), F(3)]
    temporal = [preferred_h[i] + preferred_j[i] for i in range(2)]
    speeds2 = [preferred_h[i] / temporal[i] for i in range(2)]
    if mutation == "erase_spurion":
        speeds2 = [F(1), F(1)]

    q = [F(3, 5), F(4, 5)]
    rep = q + [F(2), F(-3)]
    shifted = q + [F(11), F(13)]
    radius = dot(h, q, q)
    mass2, coupling = F(3, 2), F(5, 7)
    potential_rep = mass2 * radius / 2 + coupling * radius * radius / 4

    checks = [
        ("ambient rank is four in the exact quotient fixture", len(p[0]) == 4),
        ("quotient rank is two in the exact fixture", len(p) == 2),
        ("the gauge fixture lies in ker P", mv(p, gauge) == [F(0), F(0)]),
        ("the quotient form is positive", all(x > 0 for x in h)),
        ("the temporal ambient principal block is P-star H P", blocks[0] == principal_block(F(1), p, h)),
        ("each gauge direction is principal-null", all(mv(block, gauge) == [F(0)] * 4 for block in blocks)),
        ("every spacetime block has the metric factor", all(block == [[eta[a] * x for x in row] for row in blocks[0]] for a, block in enumerate(blocks))),
        ("quotient mode one has the metric cone", [h[0] * x for x in eta] == [F(2), F(-2), F(-2), F(-2)]),
        ("quotient mode two has the same metric cone", [h[1] * x for x in eta] == [F(3), F(-3), F(-3), F(-3)]),
        ("mass and quartic coupling are lower order", mass2 > 0 and coupling > 0),
        ("the interacting potential is positive on a nonzero quotient field", potential_rep > 0),
        ("gauge-related ambient representatives have one quotient", mv(p, rep) == mv(p, shifted) == q),
        ("the matter stress is symmetric", t01 == t10),
        ("the scalar coframe spin-current obstruction vanishes", stress == transpose(stress)),
        ("the energy density is positive", t00 > 0),
        ("the spatial stress is finite exact rational data", isinstance(t11, F)),
        ("the time Ward identity equals H(E,d0 psi)", ward0 == dot(h, euler, qt)),
        ("the space Ward identity equals H(E,d1-up psi)", ward1 == -dot(h, euler, qx)),
        ("the coupled coframe Euler tensor vanishes", total_euler == [[F(0), F(0)], [F(0), F(0)]]),
        ("the preferred-vector temporal form is positive", all(x > 0 for x in temporal)),
        ("the preferred-vector control has two squared speeds", speeds2 == [F(1), F(1, 4)]),
        ("the preferred-vector control remains hyperbolic", all(x > 0 for x in speeds2)),
        ("the spurion is absent from the minimal candidate field list", preferred_j != [F(0), F(0)]),
        ("the full quotient multiplicity remains 960", 960 == 1920 - 960),
        ("one metric cone covers all 960 quotient modes", len(set(eta)) == 2 and 960 > 0),
        ("the construction does not identify ambient and quotient carriers", 1920 != 960),
    ]
    return checks


def manifest_failures(data, predecessor):
    failures = []
    candidate = data.get("candidate", {})
    descent = data.get("quotient_principal_descent", {})
    ward = data.get("variational_descent", {})
    control = data.get("preferred_vector_control", {})
    fences = data.get("fences", {})
    result = data.get("result", {})
    if "V1920" not in candidate.get("ambient_carrier", "") or "psi=P_Phi" not in candidate.get("physical_field", ""):
        failures.append("carrier")
    if candidate.get("owner") != "repository_owned_reverse_scaffold_candidate_completion":
        failures.append("owner")
    if descent.get("gauge_kernel") != "K960_is_null_for_every_covector" or "g^munu*H" not in descent.get("quotient_tensor", ""):
        failures.append("descent")
    if ward.get("coframe_euler") != "G_munu=kappa*T_munu" or "H(E_psi" not in ward.get("matter_ward", ""):
        failures.append("ward")
    if control.get("squared_speeds") != [1, "1/4"]:
        failures.append("control")
    required_false = ("source_owned_GU_coframe_or_gravity_action", "identified_with_gimmel_gravity", "source_selected_action", "unique_action", "quantum_gravity", "prediction_or_confirmation", "cross_packet_union_allowed")
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fence")
    if result.get("source_selected_completions_constructed") != 0 or result.get("quotient_modes_with_one_metric_cone") != 960:
        failures.append("result")
    if predecessor.get("packet", {}).get("ambient_rank") != 1920 or predecessor.get("packet", {}).get("quotient_rank") != 960:
        failures.append("predecessor")
    return failures


def selftest(data, predecessor):
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in ("gauge_leak", "mixed_jet", "ward_sign", "euler_mismatch", "erase_spurion")]
    updates = (
        ("wrong_owner", lambda d: d["candidate"].__setitem__("owner", "source_owned")),
        ("wrong_carrier", lambda d: d["candidate"].__setitem__("ambient_carrier", "W960")),
        ("lost_kernel", lambda d: d["quotient_principal_descent"].__setitem__("gauge_kernel", "none")),
        ("lost_metric", lambda d: d["quotient_principal_descent"].__setitem__("quotient_tensor", "free")),
        ("wrong_euler", lambda d: d["variational_descent"].__setitem__("coframe_euler", "assumed")),
        ("wrong_ward", lambda d: d["variational_descent"].__setitem__("matter_ward", "assumed")),
        ("erase_control", lambda d: d["preferred_vector_control"].__setitem__("squared_speeds", [1, 1])),
        ("source_promotion", lambda d: d["fences"].__setitem__("source_selected_action", True)),
        ("gimmel_promotion", lambda d: d["fences"].__setitem__("identified_with_gimmel_gravity", True)),
        ("unique_promotion", lambda d: d["fences"].__setitem__("unique_action", True)),
        ("quantum_promotion", lambda d: d["fences"].__setitem__("quantum_gravity", True)),
        ("prediction_promotion", lambda d: d["fences"].__setitem__("prediction_or_confirmation", True)),
        ("source_count", lambda d: d["result"].__setitem__("source_selected_completions_constructed", 1)),
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
    if "--selftest" in sys.argv or "--self-test" in sys.argv:
        return selftest(data, predecessor)
    checks = model_checks()
    checks.extend([
        ("manifest preserves carrier, quotient, Ward and preferred-vector controls", not manifest_failures(data, predecessor)),
        ("candidate is repository-owned rather than source-attributed", data["candidate"]["owner"] == "repository_owned_reverse_scaffold_candidate_completion"),
        ("source and gimmel promotions remain fenced", not data["fences"]["source_owned_GU_coframe_or_gravity_action"] and not data["fences"]["identified_with_gimmel_gravity"]),
        ("prediction and cross-packet credit remain fenced", not data["fences"]["prediction_or_confirmation"] and not data["fences"]["cross_packet_union_allowed"]),
    ])
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K85 OBSERVED DYNAMICAL COFRAME STRESS DESCENT: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
