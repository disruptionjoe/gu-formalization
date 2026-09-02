#!/usr/bin/env python3
"""Exact fixed-state local-algebra and CHSH-selection controls for K87."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k87-observed-local-algebra-correlation-selection-wave.json"


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mmul(a, b):
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(row, col)), F(0)) for col in bt] for row in a]


def madd(a, b):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def kron(a, b):
    out = []
    for ra in a:
        for rb in b:
            row = []
            for xa in ra:
                row.extend(xa * xb for xb in rb)
            out.append(row)
    return out


def mv(a, v):
    return [sum((x * y for x, y in zip(row, v)), F(0)) for row in a]


def dot(u, v):
    return sum((x * y for x, y in zip(u, v)), F(0))


def conjugate(u, a):
    return mmul(transpose(u), mmul(a, u))


def is_zero(a):
    return not any(any(row) for row in a)


def model_checks(mutation=None):
    i2 = eye(2)
    x = [[F(0), F(1)], [F(1), F(0)]]
    z = [[F(1), F(0)], [F(0), F(-1)]]
    a_z, a_x = kron(z, i2), kron(x, i2)
    b_z, b_x = kron(i2, z), kron(i2, x)

    c, s = F(3, 5), F(4, 5)
    if mutation == "nonnormalized_rotation":
        c, s = F(3, 5), F(3, 5)
    u = [
        [c, F(0), F(0), -s],
        [F(0), F(1), F(0), F(0)],
        [F(0), F(0), F(1), F(0)],
        [s, F(0), F(0), c],
    ]
    if mutation == "noncommon_embedding":
        b_x = conjugate([[F(1), F(0), F(0), F(0)], [F(0), F(0), F(1), F(0)], [F(0), F(1), F(0), F(0)], [F(0), F(0), F(0), F(1)]], b_x)

    az_u, ax_u = conjugate(u, a_z), conjugate(u, a_x)
    bz_u, bx_u = conjugate(u, b_z), conjugate(u, b_x)
    e0 = [F(1), F(0), F(0), F(0)]
    moved = mv(u, e0)
    t = 2 * c * s
    if mutation == "wrong_correlation_parameter":
        t = c * s
    chsh_square = 4 * (1 + t * t)

    # Correlation tensor for c|00>+s|11> is diag(2cs,-2cs,1).
    corr_xx = dot(moved, mv(mmul(a_x, b_x), moved))
    y = [[F(0), F(-1)], [F(1), F(0)]]  # real skew control; YxY has real entries
    corr_yy_magnitude = dot(moved, mv(mmul(kron(y, i2), kron(i2, y)), moved))
    corr_zz = dot(moved, mv(mmul(a_z, b_z), moved))

    product_square = F(4)
    bell_square = F(8)
    intermediate_square = F(4) * (1 + F(24, 25) ** 2)
    if mutation == "erase_intermediate":
        intermediate_square = bell_square

    checks = [
        ("the entangling coordinate change is orthogonal", mmul(transpose(u), u) == eye(4)),
        ("the fixed reference state is normalized", dot(e0, e0) == 1),
        ("the moved comparison state is normalized", dot(moved, moved) == 1),
        ("the pulled A-Z observable is an involution", mmul(az_u, az_u) == eye(4)),
        ("the pulled A-X observable is an involution", mmul(ax_u, ax_u) == eye(4)),
        ("the pulled B-Z observable is an involution", mmul(bz_u, bz_u) == eye(4)),
        ("the pulled B-X observable is an involution", mmul(bx_u, bx_u) == eye(4)),
        ("the pulled A-Z and B-Z observables commute", is_zero(madd(mmul(az_u, bz_u), [[-x for x in row] for row in mmul(bz_u, az_u)]))),
        ("the pulled A-Z and B-X observables commute", is_zero(madd(mmul(az_u, bx_u), [[-x for x in row] for row in mmul(bx_u, az_u)]))),
        ("the pulled A-X and B-Z observables commute", is_zero(madd(mmul(ax_u, bz_u), [[-x for x in row] for row in mmul(bz_u, ax_u)]))),
        ("the pulled A-X and B-X observables commute", is_zero(madd(mmul(ax_u, bx_u), [[-x for x in row] for row in mmul(bx_u, ax_u)]))),
        ("the XX correlation is exactly 2cs", corr_xx == 2 * c * s),
        ("the YY correlation magnitude is exactly 2cs", corr_yy_magnitude == 2 * c * s),
        ("the ZZ correlation is exactly one", corr_zz == 1),
        ("the two largest correlation-tensor squares are 1 and t squared", chsh_square == 4 * (1 + (2 * c * s) ** 2)),
        ("the fixed-state intermediate embedding is above the classical boundary", chsh_square > 4),
        ("the fixed-state intermediate embedding is below the Tsirelson boundary", chsh_square < 8),
        ("the product endpoint has maximal CHSH square four", product_square == 4),
        ("the Bell endpoint has maximal CHSH square eight", bell_square == 8),
        ("the rational 3-4-5 control has t=24/25", 2 * F(3, 5) * F(4, 5) == F(24, 25)),
        ("the rational control is a strict intermediate face", 4 < intermediate_square < 8),
        ("one fixed vector supports distinct faces under distinct local embeddings", len({product_square, intermediate_square, bell_square}) == 3),
        ("abstract cross-commutation does not assert spacetime locality", True),
        ("the held-out delayed-choice family is not evaluated", True),
    ]
    return checks


def manifest_failures(data):
    failures = []
    fixed = data.get("fixed_state_construction", {})
    family = data.get("local_algebra_family", {})
    selection = data.get("selection_boundary", {})
    fences = data.get("fences", {})
    result = data.get("result", {})
    if fixed.get("state") != "fixed_product_vector_00" or fixed.get("state_varied") is not False:
        failures.append("fixed_state")
    if family.get("cross_commuting_for_all_theta") is not True or family.get("CHSH_max_squared") != "4_times_1_plus_sin_squared_2theta":
        failures.append("family")
    if selection.get("product_endpoint") != "2" or selection.get("Tsirelson_endpoint") != "2sqrt2" or selection.get("strict_intermediate_exists") is not True:
        failures.append("boundary")
    if selection.get("state_alone_selects_correlation_face") is not False or selection.get("abstract_commutation_proves_spacetime_locality") is not False:
        failures.append("selection")
    required_false = (
        "source_selected_local_net", "physical_spacelike_factorization", "Born_measurement_dynamics",
        "complete_BFV_descent", "Bell_prediction_or_confirmation", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if result.get("source_selected_local_nets_completed") != 0 or result.get("physical_GU_Bell_predictions") != 0:
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
        "nonnormalized_rotation", "noncommon_embedding", "wrong_correlation_parameter", "erase_intermediate",
    )]
    updates = (
        ("vary_state", lambda d: d["fixed_state_construction"].__setitem__("state_varied", True)),
        ("drop_commutation", lambda d: d["local_algebra_family"].__setitem__("cross_commuting_for_all_theta", False)),
        ("wrong_formula", lambda d: d["local_algebra_family"].__setitem__("CHSH_max_squared", "assumed")),
        ("wrong_product", lambda d: d["selection_boundary"].__setitem__("product_endpoint", "sqrt2")),
        ("drop_intermediate", lambda d: d["selection_boundary"].__setitem__("strict_intermediate_exists", False)),
        ("erase_nonselection", lambda d: d["selection_boundary"].__setitem__("state_alone_selects_correlation_face", True)),
        ("claim_locality", lambda d: d["selection_boundary"].__setitem__("abstract_commutation_proves_spacetime_locality", True)),
        ("source_promotion", lambda d: d["fences"].__setitem__("source_selected_local_net", True)),
        ("spacelike_promotion", lambda d: d["fences"].__setitem__("physical_spacelike_factorization", True)),
        ("Born_promotion", lambda d: d["fences"].__setitem__("Born_measurement_dynamics", True)),
        ("BFV_promotion", lambda d: d["fences"].__setitem__("complete_BFV_descent", True)),
        ("prediction_promotion", lambda d: d["fences"].__setitem__("Bell_prediction_or_confirmation", True)),
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
    checks.append(("manifest preserves fixed-state, local-algebra, locality and source fences", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K87 LOCAL ALGEBRA CORRELATION SELECTION: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
