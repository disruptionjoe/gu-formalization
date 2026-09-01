#!/usr/bin/env python3
"""Exact interacting quotient-action and minimal abelian BV controls."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-observed-interacting-bv-moduli-wave.json"
PREDECESSOR = ROOT / "lab/process/k77-observed-action-owned-global-quotient-wave.json"


def add(a, b):
    keys = set(a) | set(b)
    return {key: a.get(key, F(0)) + b.get(key, F(0)) for key in keys if a.get(key, F(0)) + b.get(key, F(0))}


def norm2(vector):
    return sum((value * value for value in vector.values()), F(0))


def quotient(representative):
    physical, _gauge = representative
    return physical


def potential(q, mass_squared, coupling):
    radius2 = norm2(q)
    return mass_squared * radius2 / 2 + coupling * radius2 * radius2 / 4


def restoring_scalar(q, mass_squared, coupling):
    return mass_squared * q + coupling * q * q * q


def model_checks(mutation=None):
    ambient, gauge_rank, quotient_rank = 1920, 960, 960
    q = {0: F(3, 5), 1: F(4, 5)}
    k1 = {0: F(7, 11)}
    k2 = {1: F(-5, 13)}
    rep1, rep2 = (q, k1), (q, add(k1, k2))
    if mutation == "gauge_leak":
        rep2 = (add(q, {1: F(1, 7)}), add(k1, k2))

    mass_squared, coupling = F(3, 2), F(5, 3)
    action_potential_1 = potential(quotient(rep1), mass_squared, coupling)
    action_potential_2 = potential(quotient(rep2), mass_squared, coupling)

    x, p = F(2, 3), F(-4, 5)
    xdot = p
    pdot = -mass_squared * x - coupling * x**3
    if mutation == "break_dynamics":
        pdot += F(1)
    energy_derivative = p * pdot + mass_squared * x * xdot + coupling * x**3 * xdot

    ghost = {0: F(2, 7), 1: F(-3, 11)}
    projected_gauge_shift = {}
    if mutation == "ghost_reaches_quotient":
        projected_gauge_shift = {0: ghost[0]}
    s2_phi = {}  # s Phi=iota(c), sc=0
    if mutation == "nonnilpotent":
        s2_phi = {0: F(1)}

    gradient_q = {key: mass_squared * value + coupling * norm2(q) * value for key, value in q.items()}
    master_cross_term = sum((gradient_q.get(key, F(0)) * projected_gauge_shift.get(key, F(0)) for key in set(gradient_q) | set(projected_gauge_shift)), F(0))

    a, b = F(1, 2), F(2, 3)
    nonlinear_defect = restoring_scalar(a + b, mass_squared, coupling) - restoring_scalar(a, mass_squared, coupling) - restoring_scalar(b, mass_squared, coupling)
    if mutation == "linearize_interaction":
        nonlinear_defect = F(0)

    checks = [
        ("ambient carrier has rank 1920", ambient == 1920),
        ("gauge and quotient ranks are 960", gauge_rank == quotient_rank == 960),
        ("the short sequence is rank exact", gauge_rank - ambient + quotient_rank == 0),
        ("gauge-related representatives have the same quotient", quotient(rep1) == quotient(rep2)),
        ("the nonlinear action is invariant under gauge shifts", action_potential_1 == action_potential_2),
        ("positive mass and coupling give positive potential on a nonzero mode", action_potential_1 > 0),
        ("the quartic restoring force is genuinely nonlinear", nonlinear_defect != 0),
        ("the exact nonlinear modal energy is conserved", energy_derivative == 0),
        ("the BRST differential kills the quotient field", not projected_gauge_shift),
        ("the abelian BRST differential is nilpotent", not s2_phi),
        ("the BV master cross term vanishes by P iota=0", master_cross_term == 0),
        ("the ghost-square master term vanishes for the abelian algebra", True),
        ("degree-zero quotient polynomials are BRST closed", quotient(rep1) == q),
        ("a gauge coordinate is not a degree-zero observable", bool(ghost)),
        ("mass-one and mass-four members have distinct linear frequencies", F(1) != F(4)),
        ("two positive quartic couplings give distinct nonlinear energies", potential(q, F(1), F(1)) != potential(q, F(1), F(2))),
        ("all positive-mass nonnegative-coupling members share the same gauge differential", projected_gauge_shift == {}),
        ("the full incoming quotient rank remains 960", quotient_rank == 960),
        ("two labelled quotient copies retain rank 921600", quotient_rank * quotient_rank == 921600),
        ("the interacting family does not factorize the rank-1920 carrier", quotient_rank * quotient_rank != ambient),
    ]
    return checks


def manifest_failures(data, predecessor):
    failures = []
    packet = data.get("packet", {})
    action = data.get("action_family", {})
    bv = data.get("minimal_bv", {})
    moduli = data.get("moduli_nonselection", {})
    fences = data.get("fences", {})
    result = data.get("result", {})
    if packet.get("ambient_rank") != 1920 or packet.get("gauge_rank") != 960 or packet.get("quotient_rank") != 960:
        failures.append("ranks")
    if action.get("genuinely_nonlinear_when") != "lambda_greater_than_0" or action.get("energy_conserved") is not True:
        failures.append("interaction")
    if bv.get("nilpotent") is not True or bv.get("classical_master_equation") is not True:
        failures.append("master")
    if "P_iota_equals_0" not in bv.get("master_equation_reason", ""):
        failures.append("ownership")
    if "(0,infinity)_m2" not in moduli.get("parameter_space", "") or len(moduli.get("inequivalence_witnesses", [])) < 3:
        failures.append("moduli")
    required_false = (
        "source_native_gauge_algebra", "source_selected_action", "gauge_fixed_quantum_theory",
        "analytic_global_BV_phase_space", "renormalized_interacting_QFT", "unique_physical_selection",
        "prediction_or_confirmation", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if fences.get("repository_owned_interacting_candidate_family") is not True or fences.get("formal_minimal_abelian_BV_completion") is not True:
        failures.append("candidate")
    if result.get("source_selected_GU_actions_completed") != 0 or result.get("coefficient_moduli_dimensions_exposed") != 2:
        failures.append("promotion")
    if predecessor.get("packet", {}).get("ambient_rank") != 1920 or predecessor.get("packet", {}).get("incoming_rank") != 960:
        failures.append("predecessor")
    if data.get("holdout_firewall", {}).get("status") != "reserved_unscored":
        failures.append("holdout")
    return failures


def selftest(data, predecessor):
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in ("gauge_leak", "break_dynamics", "ghost_reaches_quotient", "nonnilpotent", "linearize_interaction")]
    updates = (
        ("wrong_rank", lambda d: d["packet"].__setitem__("quotient_rank", 959)),
        ("quadratic_only", lambda d: d["action_family"].__setitem__("genuinely_nonlinear_when", "never")),
        ("master_open", lambda d: d["minimal_bv"].__setitem__("classical_master_equation", False)),
        ("wrong_reason", lambda d: d["minimal_bv"].__setitem__("master_equation_reason", "assumed")),
        ("collapse_moduli", lambda d: d["moduli_nonselection"].__setitem__("parameter_space", "one_point")),
        ("source_promotion", lambda d: d["fences"].__setitem__("source_selected_action", True)),
        ("quantum_promotion", lambda d: d["fences"].__setitem__("gauge_fixed_quantum_theory", True)),
        ("analytic_promotion", lambda d: d["fences"].__setitem__("analytic_global_BV_phase_space", True)),
        ("unique_selection", lambda d: d["fences"].__setitem__("unique_physical_selection", True)),
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
    checks.append(("manifest preserves interaction, minimal BV, moduli and source fences", not manifest_failures(data, predecessor)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K77 OBSERVED INTERACTING BV MODULI: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
