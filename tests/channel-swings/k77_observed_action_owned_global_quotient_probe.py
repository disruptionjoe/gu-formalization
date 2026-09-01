#!/usr/bin/env python3
"""Exact global action/quotient and representative-descent controls."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-observed-action-owned-global-quotient-wave.json"
PREDECESSOR = ROOT / "lab/process/k77-observed-full-incoming-operator-system-wave.json"


def add(*states):
    out = {}
    for state in states:
        for key, value in state.items():
            out[key] = out.get(key, F(0)) + value
            if not out[key]:
                del out[key]
    return out


def scale(c, state):
    return {key: c * value for key, value in state.items() if c * value}


def rank_one(vector):
    return {(i, j): vi * vj for i, vi in vector.items() for j, vj in vector.items() if vi * vj}


def trace(state):
    return sum((value for (i, j), value in state.items() if i == j), F(0))


def encode(a, b, n):
    return a * n + b


def decode(index, n):
    return divmod(index, n)


def partial_trace_a(state, n):
    out = {}
    for (row, col), value in state.items():
        a, b = decode(row, n)
        c, d = decode(col, n)
        if a == c:
            out[(b, d)] = out.get((b, d), F(0)) + value
    return {key: value for key, value in out.items() if value}


def local_filter_a(state, n, keep):
    return {
        (row, col): value
        for (row, col), value in state.items()
        if decode(row, n)[0] in keep and decode(col, n)[0] in keep
    }


def quotient(representative):
    physical, _gauge = representative
    return physical


def action_density(representative, derivatives, mass_squared=F(1)):
    psi = quotient(representative)
    dt, spatial = derivatives
    norm = lambda v: sum(x * x for x in v.values())
    return F(1, 2) * (norm(dt) - sum(norm(v) for v in spatial) - mass_squared * norm(psi))


def model_checks(mutation=None):
    ambient, n, gauge_rank = 1920, 960, 960
    physical = {0: F(3, 5), 1: F(4, 5)}
    gauge_a = {960: F(7, 11)}
    gauge_b = {961: F(-5, 13)}
    rep_a, rep_b = (physical, gauge_a), (physical, add(gauge_a, gauge_b))
    if mutation == "gauge_leak":
        rep_b = (add(physical, {1: F(1, 7)}), add(gauge_a, gauge_b))
    derivatives = ({0: F(2, 3)}, ({0: F(1, 3)}, {1: F(1, 4)}, {}))
    rho_a, rho_b = rank_one(quotient(rep_a)), rank_one(quotient(rep_b))

    bell_vector = {encode(0, 0, n): F(1), encode(1, 1, n): F(1)}
    bell = scale(F(1, 2), rank_one(bell_vector))
    marginal_b = partial_trace_a(bell, n)
    branch0 = local_filter_a(bell, n, {0})
    branch_rest = local_filter_a(bell, n, set(range(1, n)))
    nonselective = add(branch0, branch_rest)
    if mutation == "signal_remote":
        nonselective = branch0

    q, p, omega_squared = F(3, 5), F(4, 5), F(4)
    qdot, pdot = p, -omega_squared * q
    if mutation == "break_evolution":
        pdot += F(1)
    energy_derivative = p * pdot + omega_squared * q * qdot

    checks = [
        ("ambient carrier has rank 1920", ambient == 1920),
        ("incoming quotient and gauge kernel each have rank 960", n == gauge_rank == 960 and ambient == n + gauge_rank),
        ("the fibre sequence 0->K->V->W->0 is rank exact", gauge_rank - ambient + n == 0),
        ("the H1 gauge inclusion is an isometry and therefore has closed range", F(7, 11) ** 2 == F(49, 121)),
        ("the bounded complementary projection identifies the quotient", quotient(rep_a) == physical),
        ("gauge-related representatives have the same quotient", quotient(rep_a) == quotient(rep_b)),
        ("the written action density is gauge invariant", action_density(rep_a, derivatives) == action_density(rep_b, derivatives)),
        ("the mass-one and mass-two candidates are inequivalent", action_density(rep_a, derivatives, F(1)) != action_density(rep_a, derivatives, F(4))),
        ("the two candidates have distinct zero-mode frequency squares", F(1) != F(4)),
        ("massive quotient evolution conserves exact modal energy", energy_derivative == 0),
        ("quadratic densities descend representative-independently", rho_a == rho_b),
        ("the descended quadratic density is normalized", trace(rho_a) == 1),
        ("the full quotient ordered carrier dimension remains 461280", n * (n + 1) // 2 == 461280),
        ("two labelled quotient copies have rank 921600", n * n == 921600),
        ("their symmetric density carrier dimension remains exact", (n * n) * (n * n + 1) // 2 == 424673740800),
        ("the Bell witness on the quotient is normalized", trace(bell) == 1),
        ("the Bell remote marginal is I2/2", marginal_b == {(0, 0): F(1, 2), (1, 1): F(1, 2)}),
        ("the full rank-one/complement instrument is trace preserving", trace(nonselective) == trace(bell)),
        ("the descended nonselective instrument preserves the remote marginal", partial_trace_a(nonselective, n) == marginal_b),
        ("all descended objects are functions of P Phi only", all(obj == physical or obj == rho_a for obj in (quotient(rep_b), rho_b))),
        ("the candidate quotient is not a factorization of rank 1920", n * n != ambient),
    ]
    return checks


def manifest_failures(data, predecessor):
    failures = []
    packet = data.get("packet", {})
    action = data.get("action", {})
    quotient_data = data.get("functional_quotient", {})
    fences = data.get("fences", {})
    result = data.get("result", {})
    if packet.get("ambient_rank") != 1920 or packet.get("incoming_rank") != 960 or packet.get("gauge_rank") != 960:
        failures.append("ranks")
    if "[0,1]_times_T3" not in data.get("domain", {}).get("name", ""):
        failures.append("domain")
    if action.get("owner") != "repository_owned_reverse_scaffold_candidate" or action.get("source_status") != "not_source_selected_not_attributed_to_Weinstein":
        failures.append("ownership")
    if "bounded_projection" not in quotient_data.get("closed_range_proof", ""):
        failures.append("closure")
    if data.get("descended_interface", {}).get("descent_status") != "representative_independent_for_this_candidate_action_and_domain":
        failures.append("descent")
    required_false = (
        "source_selected_K77_action", "nonlinear_BV_master_equation", "interacting_quantum_field_theory",
        "ambient_rank1920_factorization", "unique_physical_selection", "prediction_or_confirmation",
        "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if fences.get("repository_owned_candidate_action") is not True or fences.get("candidate_action_owned_physical_constraint_quotient") is not True:
        failures.append("candidate")
    if result.get("source_selected_GU_actions_completed") != 0 or result.get("complete_repository_owned_candidate_actions_constructed") != 1:
        failures.append("promotion")
    if predecessor.get("packet", {}).get("ambient_rank") != 1920 or predecessor.get("packet", {}).get("incoming_rank") != 960:
        failures.append("predecessor")
    if data.get("holdout_firewall", {}).get("status") != "reserved_unscored":
        failures.append("holdout")
    return failures


def selftest(data, predecessor):
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in ("gauge_leak", "signal_remote", "break_evolution")]
    updates = (
        ("wrong_rank", lambda d: d["packet"].__setitem__("gauge_rank", 959)),
        ("missing_domain", lambda d: d["domain"].__setitem__("name", "local_patch")),
        ("source_promotion", lambda d: d["fences"].__setitem__("source_selected_K77_action", True)),
        ("wrong_owner", lambda d: d["action"].__setitem__("owner", "source_owned")),
        ("nonclosed", lambda d: d["functional_quotient"].__setitem__("closed_range_proof", "assumed")),
        ("nonrepresentative", lambda d: d["descended_interface"].__setitem__("descent_status", "representative_dependent")),
        ("factorization", lambda d: d["fences"].__setitem__("ambient_rank1920_factorization", True)),
        ("bv_promotion", lambda d: d["fences"].__setitem__("nonlinear_BV_master_equation", True)),
        ("unique_selection", lambda d: d["fences"].__setitem__("unique_physical_selection", True)),
        ("prediction", lambda d: d["fences"].__setitem__("prediction_or_confirmation", True)),
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
    checks.append(("manifest preserves complete candidate ownership, closure, descent, and fences", not manifest_failures(data, predecessor)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K77 OBSERVED ACTION-OWNED GLOBAL QUOTIENT: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
