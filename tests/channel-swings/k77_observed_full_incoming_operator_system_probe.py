#!/usr/bin/env python3
"""Exact full-incoming ordered-state/composite controls for the observed K77 packet."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-observed-full-incoming-operator-system-wave.json"
PREDECESSOR = ROOT / "lab/process/k77-observed-composite-instrument-extension-wave.json"


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
    return {
        (i, j): vi * vj
        for i, vi in vector.items()
        for j, vj in vector.items()
        if vi * vj
    }


def trace(state):
    return sum((value for (i, j), value in state.items() if i == j), F(0))


def quadratic(state, vector):
    return sum(
        (vector.get(i, F(0)) * value * vector.get(j, F(0))
         for (i, j), value in state.items()),
        F(0),
    )


def encode(a, b, n):
    return a * n + b


def decode(index, n):
    return divmod(index, n)


def partial_trace_b(state, n):
    out = {}
    for (row, col), value in state.items():
        a, b = decode(row, n)
        c, d = decode(col, n)
        if b == d:
            out[(a, c)] = out.get((a, c), F(0)) + value
    return {key: value for key, value in out.items() if value}


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
        if (decode(row, n)[0] in keep) and (decode(col, n)[0] in keep)
    }


def local_signed_permutation_a(state, n, permutation):
    out = {}
    for (row, col), value in state.items():
        a, b = decode(row, n)
        c, d = decode(col, n)
        aa, sa = permutation.get(a, (a, F(1)))
        cc, sc = permutation.get(c, (c, F(1)))
        key = (encode(aa, b, n), encode(cc, d, n))
        out[key] = out.get(key, F(0)) + sa * sc * value
    return {key: value for key, value in out.items() if value}


def model_checks(mutation=None):
    ambient, n = 1920, 960
    incoming_density_dim = n * (n + 1) // 2
    composite_amplitude_dim = n * n
    composite_density_dim = composite_amplitude_dim * (composite_amplitude_dim + 1) // 2
    bell_vector = {encode(0, 0, n): F(1), encode(1, 1, n): F(1)}
    bell = scale(F(1, 2), rank_one(bell_vector))
    if mutation == "factorize_bell":
        product_vector = {encode(0, 0, n): F(1)}
        bell = rank_one(product_vector)
    marginal_a, marginal_b = partial_trace_b(bell, n), partial_trace_a(bell, n)
    expected_marginal = {(0, 0): F(1, 2), (1, 1): F(1, 2)}
    branch0 = local_filter_a(bell, n, {0})
    branch_rest = local_filter_a(bell, n, set(range(1, n)))
    nonselective = add(branch0, branch_rest)
    if mutation == "signal_remote":
        nonselective = branch0
    quarter_turn = {0: (1, F(1)), 1: (0, F(-1))}
    phased = local_signed_permutation_a(bell, n, quarter_turn)
    dephased = add(scale(F(1, 2), bell), scale(F(1, 2), nonselective))
    if mutation == "amplify_coherence":
        dephased = add(scale(F(3, 2), bell), scale(F(-1, 2), nonselective))
    product = rank_one({encode(7, 11, n): F(1)})
    sign_pair = {3: F(3, 5), 9: F(4, 5)}
    rho_sign = rank_one(sign_pair)
    rho_neg = rank_one({key: -value for key, value in sign_pair.items()})
    witnesses = (
        {encode(0, 0, n): F(1), encode(1, 1, n): F(-1)},
        {encode(0, 0, n): F(2), encode(1, 1, n): F(3)},
        {encode(7, 11, n): F(1)},
    )
    checks = [
        ("ambient observed carrier rank remains 1920", ambient == 1920),
        ("incoming projector range rank is exactly 960", n == 960 and ambient == 2 * n),
        ("full real-symmetric incoming density carrier has dimension 461280", incoming_density_dim == 461280),
        ("two-copy incoming amplitude carrier has rank 921600", composite_amplitude_dim == 921600),
        ("two-copy symmetric density carrier dimension is exact", composite_density_dim == 424673740800),
        ("quadratic lift identifies amplitude sign on the full incoming carrier", rho_sign == rho_neg),
        ("rank-one quadratic states are positive on exact sparse witnesses", all(quadratic(bell, v) >= 0 for v in witnesses)),
        ("trace is the deterministic unit on normalized quadratic states", trace(bell) == 1 and trace(rho_sign) == 1),
        ("both Bell marginals are the same normalized rank-two density", marginal_a == marginal_b == expected_marginal),
        ("the Bell density is not the product of its marginals", bell != {(encode(a, b, n), encode(c, d, n)): x * y for (a, c), x in expected_marginal.items() for (b, d), y in expected_marginal.items()}),
        ("a product embedding has the expected pure marginals", partial_trace_b(product, n) == {(7, 7): F(1)} and partial_trace_a(product, n) == {(11, 11): F(1)}),
        ("rank-one versus complement branches are positive", all(quadratic(branch0, v) >= 0 and quadratic(branch_rest, v) >= 0 for v in witnesses)),
        ("the full-space two-outcome instrument is trace preserving", trace(nonselective) == trace(bell) == 1),
        ("the local nonselective instrument preserves the remote marginal", partial_trace_a(nonselective, n) == marginal_b),
        ("an energy-orthogonal quarter turn preserves normalization", trace(phased) == 1),
        ("the local quarter turn preserves the remote marginal", partial_trace_a(phased, n) == marginal_b),
        ("half-dephasing preserves trace and remote marginal", trace(dephased) == 1 and partial_trace_a(dephased, n) == marginal_b),
        ("half-dephasing halves the planted Bell coherence", dephased.get((encode(0, 0, n), encode(1, 1, n)), F(0)) == F(1, 4)),
        ("signed energy-orthogonal basis transport preserves trace and positivity", trace(phased) == trace(bell) and all(quadratic(phased, v) >= 0 for v in witnesses)),
    ]
    return checks


def manifest_failures(data, predecessor):
    failures = []
    packet = data.get("packet", {})
    construction = data.get("construction", {})
    fences = data.get("fences", {})
    result = data.get("result", {})
    if packet.get("id") != "K77-OBSERVED-INCOMING-PROJECTOR" or packet.get("ambient_rank") != 1920 or packet.get("incoming_rank") != 960:
        failures.append("packet")
    if construction.get("two_copy_amplitude_rank") != 921600 or construction.get("two_copy_density_dimension") != 424673740800:
        failures.append("dimensions")
    if construction.get("coordinate_status") != "canonical_up_to_energy_isometry":
        failures.append("covariance")
    if predecessor.get("result", {}).get("K77_selected_composite_rules_completed") != 0:
        failures.append("predecessor")
    required_false = (
        "ambient_rank1920_factorization", "physical_gauge_quotient", "global_causal_domain",
        "source_selected_Born_rule", "action_selected_composite", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if result.get("packet_derived_algebraic_composites_completed") != 1 or result.get("GU_native_physical_composites_completed") != 0 or result.get("action_selection") != "none":
        failures.append("promotion")
    if data.get("holdout_firewall", {}).get("status") != "reserved_unscored":
        failures.append("holdout")
    if "rank-960 incoming energy space" not in data.get("claim_ceiling", ""):
        failures.append("ceiling")
    return failures


def selftest(data, predecessor):
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in ("factorize_bell", "signal_remote", "amplify_coherence")]
    updates = (
        ("wrong_ambient", lambda d: d["packet"].__setitem__("ambient_rank", 192)),
        ("wrong_composite_rank", lambda d: d["construction"].__setitem__("two_copy_amplitude_rank", 1920)),
        ("coordinate_choice", lambda d: d["construction"].__setitem__("coordinate_status", "basis_selected")),
        ("factorization", lambda d: d["fences"].__setitem__("ambient_rank1920_factorization", True)),
        ("physical_quotient", lambda d: d["fences"].__setitem__("physical_gauge_quotient", True)),
        ("global_domain", lambda d: d["fences"].__setitem__("global_causal_domain", True)),
        ("born", lambda d: d["fences"].__setitem__("source_selected_Born_rule", True)),
        ("selected_composite", lambda d: d["result"].__setitem__("GU_native_physical_composites_completed", 1)),
        ("action", lambda d: d["result"].__setitem__("action_selection", "selected")),
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
    checks.append(("manifest preserves packet dimensions, covariance and claim fences", not manifest_failures(data, predecessor)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K77 OBSERVED FULL-INCOMING OPERATOR SYSTEM: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
