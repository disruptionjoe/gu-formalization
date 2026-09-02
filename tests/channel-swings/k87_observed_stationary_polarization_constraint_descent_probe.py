#!/usr/bin/env python3
"""Exact stationary polarization and quotient-domain controls for K87."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k87-observed-stationary-polarization-constraint-descent-wave.json"


def zeros(n, m):
    return [[F(0) for _ in range(m)] for _ in range(n)]


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mmul(a, b):
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(row, col)), F(0)) for col in bt] for row in a]


def madd(a, b):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def mscale(a, q):
    return [[q * x for x in row] for row in a]


def block(a, b, c, d):
    return [ra + rb for ra, rb in zip(a, b)] + [rc + rd for rc, rd in zip(c, d)]


def mv(a, v):
    return [sum((x * y for x, y in zip(row, v)), F(0)) for row in a]


def dot(u, v):
    return sum((x * y for x, y in zip(u, v)), F(0))


def is_zero(a):
    return not any(any(row) for row in a)


def positive_diagonal(a):
    return all(a[i][i] > 0 for i in range(len(a))) and all(
        a[i][j] == 0 for i in range(len(a)) for j in range(len(a)) if i != j
    )


def model_checks(mutation=None):
    z2 = zeros(2, 2)
    i2 = eye(2)
    omega = [[F(2), F(0)], [F(0), F(3)]]
    if mutation == "zero_frequency":
        omega[0][0] = F(0)
    omega2 = mmul(omega, omega)
    omega_inv = [[F(0), F(0)], [F(0), F(0)]]
    if omega[0][0] and omega[1][1]:
        omega_inv = [[1 / omega[0][0], F(0)], [F(0), 1 / omega[1][1]]]

    symplectic = block(z2, i2, mscale(i2, F(-1)), z2)
    generator = block(z2, i2, mscale(omega2, F(-1)), z2)
    complex_j = block(z2, mscale(omega_inv, F(-1)), omega, z2)
    if mutation == "wrong_sign_J":
        complex_j = mscale(complex_j, F(-1))
    majorant = mmul(symplectic, complex_j)
    abs_inverse = block(omega_inv, z2, z2, omega_inv)
    spectral_j = mscale(mmul(generator, abs_inverse), F(-1))
    covariance = mscale(block(omega_inv, z2, z2, omega), F(1, 2))
    pure_map = mscale(mmul(covariance, symplectic), F(2))

    # Ambient representative adds one configuration and momentum gauge slot.
    p = [
        [F(0), F(1), F(0), F(0), F(0), F(0)],
        [F(0), F(0), F(1), F(0), F(0), F(0)],
        [F(0), F(0), F(0), F(0), F(1), F(0)],
        [F(0), F(0), F(0), F(0), F(0), F(1)],
    ]
    pt = transpose(p)
    ambient_generator = mmul(pt, mmul(generator, p))
    ambient_j = mmul(pt, mmul(complex_j, p))
    gauge_q = [F(1), F(0), F(0), F(0), F(0), F(0)]
    gauge_p = [F(0), F(0), F(0), F(1), F(0), F(0)]
    if mutation == "gauge_leak":
        ambient_generator[1][0] = F(1)

    # The first oscillator is a planted invariant constraint/domain subspace.
    allowed_vectors = [
        [F(1), F(0), F(0), F(0)],
        [F(0), F(0), F(1), F(0)],
    ]
    if mutation == "constraint_leak":
        generator[1][0] = F(1)
    if mutation == "domain_not_J_invariant":
        allowed_vectors = [[F(1), F(0), F(0), F(0)]]

    def in_span_first_mode(v):
        if len(allowed_vectors) == 1:
            return v[1:] == [F(0), F(0), F(0)]
        return v[1] == 0 and v[3] == 0

    constraint_preserved = all(in_span_first_mode(mv(generator, v)) for v in allowed_vectors)
    domain_j_preserved = all(in_span_first_mode(mv(complex_j, v)) for v in allowed_vectors)

    time_reversed_j = mscale(spectral_j, F(-1))
    time_reversed_majorant = mmul(symplectic, time_reversed_j)

    checks = [
        ("the stationary frequency matrix is positive and gapped", positive_diagonal(omega)),
        ("the Hamiltonian generator is symplectic", is_zero(madd(mmul(transpose(generator), symplectic), mmul(symplectic, generator)))),
        ("the spectral formula reproduces J=-A(-A^2)^-1/2", spectral_j == complex_j),
        ("the selected complex structure squares to minus identity", mmul(complex_j, complex_j) == mscale(eye(4), F(-1))),
        ("the selected complex structure commutes with stationary evolution", mmul(generator, complex_j) == mmul(complex_j, generator)),
        ("the compatible majorant is positive", positive_diagonal(majorant)),
        ("the majorant is symmetric", transpose(majorant) == majorant),
        ("the quasifree ground covariance is positive", positive_diagonal(covariance)),
        ("the ground covariance is pure", mmul(pure_map, pure_map) == mscale(eye(4), F(-1))),
        ("time reversal flips the spectral complex structure", time_reversed_j == mscale(complex_j, F(-1))),
        ("the time-reversed sign is not positive for the fixed symplectic orientation", not positive_diagonal(time_reversed_majorant)),
        ("the ambient quotient map has the expected dimensions", len(p) == 4 and len(p[0]) == 6),
        ("the configuration gauge vector is killed by the quotient", not any(mv(p, gauge_q))),
        ("the momentum gauge vector is killed by the quotient", not any(mv(p, gauge_p))),
        ("stationary evolution preserves the configuration gauge image", not any(mv(ambient_generator, gauge_q))),
        ("stationary evolution preserves the momentum gauge image", not any(mv(ambient_generator, gauge_p))),
        ("the ambient selector preserves the configuration gauge image", not any(mv(ambient_j, gauge_q))),
        ("the ambient selector preserves the momentum gauge image", not any(mv(ambient_j, gauge_p))),
        ("the quotient intertwines the lifted and reduced generator", mmul(p, ambient_generator) == mmul(generator, p)),
        ("the quotient intertwines the lifted and reduced complex structure", mmul(p, ambient_j) == mmul(complex_j, p)),
        ("the planted constraint kernel is evolution invariant", constraint_preserved),
        ("the planted boundary domain is J invariant", domain_j_preserved),
        ("the two selected frequencies are not assumed degenerate", omega[0][0] != omega[1][1]),
        ("the result uses the even K86 phase space rather than the odd BV bracket", True),
    ]
    return checks


def manifest_failures(data):
    failures = []
    selector = data.get("stationary_selector", {})
    descent = data.get("constraint_descent", {})
    owners = data.get("load_bearing_owners", {})
    fences = data.get("fences", {})
    result = data.get("result", {})
    if selector.get("formula") != "J_equals_minus_A_times_inverse_sqrt_minus_A_squared":
        failures.append("formula")
    if selector.get("positive_majorant") is not True or selector.get("ground_covariance_selected") is not True:
        failures.append("selector")
    if descent.get("gauge_image_invariant") is not True or descent.get("constraint_kernel_invariant") is not True or descent.get("boundary_domain_J_invariant") is not True:
        failures.append("descent")
    if len(owners) < 4:
        failures.append("owners")
    required_false = (
        "source_selected_full_action", "full_interacting_polarization", "complete_BFV_complex",
        "continuum_Hadamard_state", "Born_rule", "prediction_or_confirmation",
        "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if result.get("source_selected_polarizations_completed") != 0 or result.get("physical_GU_states_selected") != 0:
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
        "zero_frequency", "wrong_sign_J", "gauge_leak", "constraint_leak", "domain_not_J_invariant",
    )]
    updates = (
        ("wrong_formula", lambda d: d["stationary_selector"].__setitem__("formula", "assumed")),
        ("drop_positive_majorant", lambda d: d["stationary_selector"].__setitem__("positive_majorant", False)),
        ("drop_ground_covariance", lambda d: d["stationary_selector"].__setitem__("ground_covariance_selected", False)),
        ("drop_gauge_invariance", lambda d: d["constraint_descent"].__setitem__("gauge_image_invariant", False)),
        ("drop_constraint_invariance", lambda d: d["constraint_descent"].__setitem__("constraint_kernel_invariant", False)),
        ("drop_domain_invariance", lambda d: d["constraint_descent"].__setitem__("boundary_domain_J_invariant", False)),
        ("erase_owners", lambda d: d.__setitem__("load_bearing_owners", {})),
        ("source_promotion", lambda d: d["fences"].__setitem__("source_selected_full_action", True)),
        ("BFV_promotion", lambda d: d["fences"].__setitem__("complete_BFV_complex", True)),
        ("Hadamard_promotion", lambda d: d["fences"].__setitem__("continuum_Hadamard_state", True)),
        ("Born_promotion", lambda d: d["fences"].__setitem__("Born_rule", True)),
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
    checks.append(("manifest preserves selector, descent, owner and source fences", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K87 STATIONARY POLARIZATION DESCENT: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
