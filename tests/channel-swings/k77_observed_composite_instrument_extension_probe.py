#!/usr/bin/env python3
"""Exact packet-local composite/instrument controls for the observed K77 interface."""
from __future__ import annotations

import copy
import itertools
import json
import pathlib
import sys
from fractions import Fraction as F

ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-observed-composite-instrument-extension-wave.json"
PREDECESSOR = ROOT / "lab/process/k77-quotient-majorant-descent-wave.json"


def matrix(rows): return tuple(tuple(F(x) for x in row) for row in rows)
def eye(n): return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))
def transpose(a): return tuple(zip(*a))
def add(a, b): return tuple(tuple(a[i][j]+b[i][j] for j in range(len(a[0]))) for i in range(len(a)))
def scale(c, a): return tuple(tuple(c*x for x in row) for row in a)
def mul(a, b): return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))), F(0)) for j in range(len(b[0]))) for i in range(len(a)))
def trace(a): return sum((a[i][i] for i in range(len(a))), F(0))
def kron(a, b): return tuple(tuple(a[i][j]*b[k][l] for j in range(len(a[0])) for l in range(len(b[0]))) for i in range(len(a)) for k in range(len(b)))
def outer(v): return tuple(tuple(x*y for y in v) for x in v)


def ptrace_a(rho):
    return tuple(tuple(sum((rho[2*a+b][2*a+d] for a in range(2)), F(0)) for d in range(2)) for b in range(2))


def ptrace_b(rho):
    return tuple(tuple(sum((rho[2*a+b][2*c+b] for b in range(2)), F(0)) for c in range(2)) for a in range(2))


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    I, X, Z = eye(2), matrix(((0, 1), (1, 0))), matrix(((1, 0), (0, -1)))
    zero_density, one_density = matrix(((1, 0), (0, 0))), matrix(((0, 0), (0, 1)))
    rho = matrix(((F(1,2),0,0,F(1,2)),(0,0,0,0),(0,0,0,0),(F(1,2),0,0,F(1,2))))
    if mutation == "factorize_bell":
        rho = scale(F(1,4), tuple(tuple(F(1) for _ in range(4)) for _ in range(4)))
    rho_a, rho_b = ptrace_b(rho), ptrace_a(rho)
    p0, p1 = zero_density, one_density
    k0, k1 = kron(p0, I), kron(p1, I)
    branch0, branch1 = mul(mul(k0, rho), transpose(k0)), mul(mul(k1, rho), transpose(k1))
    nonselective = add(branch0, branch1)
    if mutation == "signal_remote":
        nonselective = matrix(((1,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0)))
    phase = kron(X, I)
    phased = mul(mul(phase, rho), transpose(phase))
    eta = F(1, 2)
    dephased = add(scale(eta, rho), scale(1-eta, nonselective))
    if mutation == "amplify_decoherence":
        eta = F(3, 2)
        dephased = add(scale(eta, rho), scale(1-eta, nonselective))
    # Work with sqrt(2)-scaled Bob observables. A value 4 here is 2 sqrt(2).
    B0_scaled, B1_scaled = add(Z, X), add(Z, scale(-1, X))
    expect = lambda a, b: trace(mul(rho, kron(a, b)))
    chsh_scaled = expect(Z, B0_scaled) + expect(Z, B1_scaled) + expect(X, B0_scaled) - expect(X, B1_scaled)
    classical = max(abs(a0*b0+a0*b1+a1*b0-a1*b1)
                    for a0, a1, b0, b1 in itertools.product((-1, 1), repeat=4))
    product = kron(p0, p1)
    witnesses = ((F(1),F(2),F(3),F(4)), (F(-3),F(1),F(2),F(5)))
    quadratic = lambda v, a: sum((v[i]*a[i][j]*v[j] for i in range(len(v)) for j in range(len(v))), F(0))
    checks = [
        ("Bell density is symmetric, rank-one by exact row proportionality and normalized", rho == transpose(rho) and rho[0] == rho[3] and rho[1] == rho[2] == (F(0),)*4 and trace(rho) == 1),
        ("Bell density is positive on exact hostile witnesses", all(quadratic(v,rho) == (v[0]+v[3])**2/F(2) for v in witnesses)),
        ("both Bell marginals are exactly I2/2", rho_a == scale(F(1,2), I) and rho_b == scale(F(1,2), I)),
        ("Bell density is not the product of its marginals", rho != kron(rho_a, rho_b)),
        ("product-state embedding has the expected marginals", ptrace_b(product) == p0 and ptrace_a(product) == p1),
        ("local projectors resolve the identity", add(k0, k1) == eye(4)),
        ("both local branches are positive on exact hostile witnesses", all(quadratic(v,branch0) >= 0 and quadratic(v,branch1) >= 0 for v in witnesses)),
        ("branch weights are nonnegative and sum to one", trace(branch0) >= 0 and trace(branch1) >= 0 and trace(nonselective) == 1),
        ("nonselective local measurement preserves the remote marginal", ptrace_a(nonselective) == rho_b),
        ("local phase is reversible and preserves trace", mul(transpose(phase),phase) == eye(4) and trace(phased) == 1),
        ("local phase preserves the remote marginal", ptrace_a(phased) == rho_b),
        ("eta-half dephasing preserves trace", trace(dephased) == 1),
        ("eta-half dephasing preserves the remote marginal", ptrace_a(dephased) == rho_b),
        ("eta-half dephasing halves Bell coherence", dephased[0][3] == F(1, 4)),
        ("scaled Bell CHSH numerator is four, hence CHSH is exactly 2 sqrt 2", chsh_scaled == 4),
        ("exhaustive deterministic local ceiling is two", classical == 2),
    ]
    return checks


def manifest_failures(data: dict, predecessor: dict) -> list[str]:
    failures = []
    packet = data.get("packet", {})
    if packet.get("id") != "K77-OBSERVED-INCOMING-PROJECTOR" or packet.get("ambient_carrier") != "real_rank_1920_observed_fermionic_K77_carrier": failures.append("packet_typing")
    if packet.get("not_a_native_factorization") is not True or packet.get("not_a_dimension_reduction") is not True: failures.append("adapter_ceiling")
    prior = {row.get("id"): row for row in predecessor.get("packet_local_results", [])}.get(packet.get("id"), {})
    if prior.get("state_unit_effect_status") != "chart_local_conditional_interface_constructed": failures.append("predecessor")
    if len(data.get("import_accounting", [])) != 7 or any("imported" not in row.get("classification", "") and "assumed" not in row.get("classification", "") for row in data.get("import_accounting", [])): failures.append("imports")
    iso = data.get("packet_isolation", {})
    if iso.get("cross_packet_union_allowed") is not False or iso.get("i1b_data_used") is not False or iso.get("k95_data_used") is not False: failures.append("packet_isolation")
    result = data.get("result", {})
    if result.get("K77_selected_composite_rules_completed") != 0 or result.get("GU_native_physical_states_completed") != 0 or result.get("action_selection") != "none": failures.append("promotion")
    holdout = data.get("holdout_firewall", {})
    if holdout.get("status") != "reserved_unscored" or holdout.get("scored_in_this_result") is not False: failures.append("holdout")
    if "no K77-selected tensor product" not in data.get("claim_ceiling", ""): failures.append("ceiling")
    return failures


def selftest(data: dict, predecessor: dict) -> int:
    mutations = []
    for name in ("factorize_bell", "signal_remote", "amplify_decoherence"):
        mutations.append((name, any(not ok for _, ok in model_checks(name))))
    updates = (
        ("native_factor", lambda d: d["packet"].__setitem__("not_a_native_factorization", False)),
        ("dimension_reduction", lambda d: d["packet"].__setitem__("not_a_dimension_reduction", False)),
        ("cross_packet", lambda d: d["packet_isolation"].__setitem__("cross_packet_union_allowed", True)),
        ("i1b_union", lambda d: d["packet_isolation"].__setitem__("i1b_data_used", True)),
        ("gu_import", lambda d: d["import_accounting"][0].__setitem__("classification", "GU_native")),
        ("selected_composite", lambda d: d["result"].__setitem__("K77_selected_composite_rules_completed", 1)),
        ("physical_state", lambda d: d["result"].__setitem__("GU_native_physical_states_completed", 1)),
        ("action", lambda d: d["result"].__setitem__("action_selection", "selected")),
        ("holdout", lambda d: d["holdout_firewall"].__setitem__("scored_in_this_result", True)),
        ("rank192", lambda d: d["packet"].__setitem__("ambient_carrier", "real_rank_192")),
    )
    for name, update in updates:
        mutant = copy.deepcopy(data); update(mutant)
        mutations.append((name, bool(manifest_failures(mutant, predecessor))))
    for name, caught in mutations: print(f"[{'PASS' if caught else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(c for _, c in mutations)}/{len(mutations)} caught")
    return 0 if all(c for _, c in mutations) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text()); predecessor = json.loads(PREDECESSOR.read_text())
    if "--selftest" in sys.argv: return selftest(data, predecessor)
    checks = model_checks(); checks.append(("manifest preserves packet typing, imports, isolation, holdout and ceiling", not manifest_failures(data, predecessor)))
    for label, ok in checks: print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks); print(f"K77 OBSERVED COMPOSITE INSTRUMENT: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__": raise SystemExit(main())
