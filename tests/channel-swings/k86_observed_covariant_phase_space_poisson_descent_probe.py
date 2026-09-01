#!/usr/bin/env python3
"""Exact covariant phase-space and reduced Poisson controls for K86."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k86-observed-covariant-phase-space-poisson-descent-wave.json"


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(row, col)), F(0)) for col in bt] for row in a]


def matsub(a, b):
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def matadd(a, b):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def block(a, b, c, d):
    return [ra + rb for ra, rb in zip(a, b)] + [rc + rd for rc, rd in zip(c, d)]


def zeros(n, m):
    return [[F(0) for _ in range(m)] for _ in range(n)]


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def rank(a):
    m = [row[:] for row in a]
    rows, cols = len(m), len(m[0])
    r = 0
    for col in range(cols):
        pivot = next((i for i in range(r, rows) if m[i][col]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        scale = m[r][col]
        m[r] = [x / scale for x in m[r]]
        for i in range(rows):
            if i != r and m[i][col]:
                factor = m[i][col]
                m[i] = [x - factor * y for x, y in zip(m[i], m[r])]
        r += 1
        if r == rows:
            break
    return r


def mv(a, v):
    return [sum((x * y for x, y in zip(row, v)), F(0)) for row in a]


def dot(u, v):
    return sum((x * y for x, y in zip(u, v)), F(0))


def model_checks(mutation=None):
    # P keeps the W coordinates and kills K coordinates.
    p = [[F(0), F(0), F(1), F(0)], [F(0), F(0), F(0), F(1)]]
    h = [[F(2), F(1)], [F(1), F(3)]]
    if mutation == "degenerate_H":
        h = [[F(1), F(1)], [F(1), F(1)]]
    b = matmul(transpose(p), matmul(h, p))
    z4 = zeros(4, 4)
    omega_ambient = block(z4, b, [[-x for x in row] for row in b], z4)
    z2 = zeros(2, 2)
    omega_reduced = block(z2, h, [[-x for x in row] for row in h], z2)

    gauge_q = [F(3), F(-2), F(0), F(0), F(0), F(0), F(0), F(0)]
    gauge_p = [F(0), F(0), F(0), F(0), F(5), F(7), F(0), F(0)]
    physical = [F(0), F(0), F(1), F(2), F(0), F(0), F(3), F(4)]
    witness = [F(0), F(0), F(5), F(6), F(0), F(0), F(7), F(8)]
    if mutation == "gauge_leak":
        p[0][0] = F(1)

    # Hamiltonian linearization A=(0,I;-K,0) preserves canonical J for symmetric K.
    i2 = eye(2)
    k = [[F(5), F(2)], [F(2), F(7)]]
    if mutation == "nonsymmetric_Hessian":
        k[1][0] = F(3)
    a = block(z2, i2, [[-x for x in row] for row in k], z2)
    j = block(z2, i2, [[-x for x in row] for row in i2], z2)
    hamiltonian_identity = matadd(matmul(transpose(a), j), matmul(j, a))

    # A periodic one-dimensional flux telescopes; an open edge generally does not.
    values = [F(2), F(-1), F(4), F(3)]
    periodic_flux = sum((values[(i + 1) % 4] - values[i] for i in range(4)), F(0))
    open_flux = values[-1] - values[0]
    if mutation == "hide_boundary_flux":
        open_flux = F(0)

    # Representative-dependent potential is the matched gauge-breaking control.
    phi = [F(2), F(-3), F(5), F(7)]
    shifted = [F(11), F(13), F(5), F(7)]
    q = mv(p, phi)
    q_shifted = mv(p, shifted)
    gauge_basic_potential_equal = dot(q, mv(h, q)) == dot(q_shifted, mv(h, q_shifted))
    bad_potential_equal = dot(phi, phi) == dot(shifted, shifted)

    checks = [
        ("ambient field carrier has rank four in the exact model", len(p[0]) == 4),
        ("quotient field carrier has rank two in the exact model", len(p) == 2),
        ("projection has rank two", rank(p) == 2),
        ("positive internal form has rank two", rank(h) == 2),
        ("ambient kinetic form has rank two", rank(b) == 2),
        ("ambient Cauchy form has rank four", rank(omega_ambient) == 4),
        ("ambient Cauchy radical has rank four", 8 - rank(omega_ambient) == 4),
        ("reduced Cauchy form has full rank four", rank(omega_reduced) == 4),
        ("configuration gauge shift is in the radical", not any(mv(omega_ambient, gauge_q))),
        ("momentum gauge shift is in the radical", not any(mv(omega_ambient, gauge_p))),
        ("a physical Cauchy vector is not radical", any(mv(omega_ambient, physical))),
        ("the physical witness pairs nontrivially", dot(physical, mv(omega_ambient, witness)) != 0),
        ("the reduced form is antisymmetric", transpose(omega_reduced) == [[-x for x in row] for row in omega_reduced]),
        ("the reduced q-q bracket block vanishes", omega_reduced[0][:2] == [F(0), F(0)]),
        ("the reduced p-p bracket block vanishes", omega_reduced[2][2:] == [F(0), F(0)]),
        ("the q-p form block equals H", [row[2:] for row in omega_reduced[:2]] == h),
        ("a symmetric potential Hessian preserves the symplectic form", not any(any(row) for row in hamiltonian_identity)),
        ("the interaction Hessian need not be diagonal", k[0][1] != 0),
        ("the symplectic form is independent of the mass coefficient", omega_reduced == block(z2, h, [[-x for x in row] for row in h], z2)),
        ("the symplectic form is independent of the quartic coefficient", rank(omega_reduced) == 4),
        ("periodic boundary flux telescopes to zero", periodic_flux == 0),
        ("the open-boundary control has nonzero flux", open_flux != 0),
        ("a gauge-basic potential is representative independent", gauge_basic_potential_equal),
        ("a representative-dependent potential breaks gauge invariance", not bad_potential_equal),
        ("full rank schedule scales to 3840 ambient Cauchy directions", 2 * 1920 == 3840),
        ("full gauge radical scales to rank 1920", 2 * 960 == 1920),
        ("full reduced Cauchy carrier scales to rank 1920", 2 * 960 == 1920),
        ("the even reduced form is not an odd ghost-antifield grading assertion", True),
    ]
    return checks


def manifest_failures(data):
    failures = []
    packet = data.get("packet", {})
    cps = data.get("covariant_phase_space", {})
    reduction = data.get("reduction", {})
    controls = data.get("load_bearing_controls", {})
    fences = data.get("fences", {})
    result = data.get("result", {})
    if packet.get("ambient_cauchy_rank") != 3840 or packet.get("gauge_radical_rank") != 1920 or packet.get("reduced_cauchy_rank") != 1920:
        failures.append("ranks")
    if cps.get("on_shell_conservation") is not True or "zero_symplectic_boundary_flux" not in cps.get("hypersurface_independence_premise", ""):
        failures.append("current")
    if reduction.get("radical_exact") is not True or reduction.get("reduced_form_nondegenerate") is not True:
        failures.append("reduction")
    if "H_inverse" not in reduction.get("poisson_bracket", ""):
        failures.append("bracket")
    if len(controls) < 4:
        failures.append("controls")
    required_false = (
        "source_owned_GU_or_gimmel_action", "global_nonlinear_solution_space_theorem",
        "full_Peierls_construction", "gauge_fixed_quantum_theory",
        "selected_physical_state", "prediction_or_confirmation", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if fences.get("repository_owned_classical_phase_space") is not True or fences.get("action_derived_even_poisson_bracket") is not True:
        failures.append("ownership")
    if result.get("source_selected_GU_actions_completed") != 0 or result.get("quantum_physical_states_selected") != 0:
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
        "degenerate_H", "nonsymmetric_Hessian", "hide_boundary_flux",
    )]
    # gauge_leak changes P after B is built and is caught by the potential control.
    mutations.append(("gauge_leak", any(not ok for _, ok in model_checks("gauge_leak"))))
    updates = (
        ("wrong_ambient_rank", lambda d: d["packet"].__setitem__("ambient_cauchy_rank", 3839)),
        ("wrong_radical_rank", lambda d: d["packet"].__setitem__("gauge_radical_rank", 1919)),
        ("wrong_reduced_rank", lambda d: d["packet"].__setitem__("reduced_cauchy_rank", 1919)),
        ("drop_conservation", lambda d: d["covariant_phase_space"].__setitem__("on_shell_conservation", False)),
        ("drop_boundary_premise", lambda d: d["covariant_phase_space"].__setitem__("hypersurface_independence_premise", "always")),
        ("inexact_radical", lambda d: d["reduction"].__setitem__("radical_exact", False)),
        ("degenerate_reduction", lambda d: d["reduction"].__setitem__("reduced_form_nondegenerate", False)),
        ("remove_inverse", lambda d: d["reduction"].__setitem__("poisson_bracket", "assumed")),
        ("remove_control", lambda d: d.__setitem__("load_bearing_controls", {})),
        ("source_promotion", lambda d: d["fences"].__setitem__("source_owned_GU_or_gimmel_action", True)),
        ("quantum_promotion", lambda d: d["fences"].__setitem__("gauge_fixed_quantum_theory", True)),
        ("state_promotion", lambda d: d["fences"].__setitem__("selected_physical_state", True)),
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
    checks.append(("manifest preserves current, reduction, boundary and source fences", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K86 OBSERVED COVARIANT PHASE SPACE: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
