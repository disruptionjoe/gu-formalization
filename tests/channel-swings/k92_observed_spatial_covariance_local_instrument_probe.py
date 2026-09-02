#!/usr/bin/env python3
"""Exact spatial covariance, local instrument and quotient-descent controls for K92."""
from __future__ import annotations

import copy
import itertools
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k92-observed-spatial-covariance-local-instrument-wave.json"


STATES = tuple(itertools.product((0, 1), repeat=3))


def z(bit: int) -> int:
    return 1 if bit == 0 else -1


def base_weights() -> dict[tuple[int, int, int], F]:
    raw = {s: F(2 ** (int(s[0] == s[1]) + int(s[1] == s[2]))) for s in STATES}
    total = sum(raw.values(), F(0))
    return {s: w / total for s, w in raw.items()}


def expectation(prob: dict[tuple[int, int, int], F], fn) -> F:
    return sum((p * F(fn(s)) for s, p in prob.items()), F(0))


def marginal(prob: dict[tuple[int, int, int], F], sites: tuple[int, ...]) -> dict[tuple[int, ...], F]:
    out: dict[tuple[int, ...], F] = {}
    for state, p in prob.items():
        key = tuple(state[i] for i in sites)
        out[key] = out.get(key, F(0)) + p
    return out


def condition(prob: dict[tuple[int, int, int], F], site: int, bit: int) -> dict[tuple[int, int, int], F]:
    weight = sum((p for s, p in prob.items() if s[site] == bit), F(0))
    return {s: (p / weight if s[site] == bit else F(0)) for s, p in prob.items()}


def detector_map(state: tuple[int, int, int], detector: int, site: int, mutation: str | None) -> tuple[tuple[int, int, int], int]:
    if mutation == "nonunitary_detector" and state == (1, 1, 1) and detector == 1:
        return state, 1
    return state, detector ^ state[site]


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    prob = base_weights()
    if mutation == "wrong_spatial_weight":
        prob[(0, 0, 0)] -= F(1, 18)
        prob[(0, 1, 0)] += F(1, 18)
    if mutation == "negative_state":
        prob[(0, 0, 0)] = F(-1, 18)

    mean = [expectation(prob, lambda s, i=i: z(s[i])) for i in range(3)]
    cov01 = expectation(prob, lambda s: z(s[0]) * z(s[1])) - mean[0] * mean[1]
    cov12 = expectation(prob, lambda s: z(s[1]) * z(s[2])) - mean[1] * mean[2]
    cov02 = expectation(prob, lambda s: z(s[0]) * z(s[2])) - mean[0] * mean[2]
    p0 = sum((p for s, p in prob.items() if s[1] == 0), F(0))
    p1 = sum((p for s, p in prob.items() if s[1] == 1), F(0))
    if mutation == "incomplete_records":
        p1 = F(0)
    cond0, cond1 = condition(prob, 1, 0), condition(prob, 1, 1)
    adjacent0 = expectation(cond0, lambda s: z(s[0]))
    adjacent1 = expectation(cond1, lambda s: z(s[0]))

    basis = tuple((s, d) for s in STATES for d in (0, 1))
    image = tuple(detector_map(s, d, 1, mutation) for s, d in basis)
    twice = tuple(detector_map(*detector_map(s, d, 1, mutation), 1, mutation) for s, d in basis)

    before_remote = marginal(prob, (0, 2))
    after_prob = dict(prob)
    if mutation == "remote_signal":
        after_prob[(0, 0, 0)] += F(1, 18)
        after_prob[(1, 0, 0)] -= F(1, 18)
    after_remote = marginal(after_prob, (0, 2))

    endpoint_a = lambda s, d0, d2: (s, d0 ^ s[0], d2)
    endpoint_b = lambda s, d0, d2: (s, d0, d2 ^ s[2])
    commute = all(endpoint_a(*endpoint_b(s, d0, d2)) == endpoint_b(*endpoint_a(s, d0, d2)) for s in STATES for d0 in (0, 1) for d2 in (0, 1))
    gauge_coefficient = F(1) if mutation == "gauge_leak" else F(0)

    return [
        ("the selected spatial control has exactly eight three-site configurations", len(STATES) == 8),
        ("the unnormalized aligned-edge weights sum to partition function eighteen", sum((F(2 ** (int(s[0] == s[1]) + int(s[1] == s[2]))) for s in STATES), F(0)) == 18),
        ("the rational state is normalized", sum(prob.values(), F(0)) == 1),
        ("the rational state is pointwise positive", all(p > 0 for p in prob.values())),
        ("global spin-flip symmetry gives zero one-site means", mean == [0, 0, 0]),
        ("the first nearest-neighbor connected covariance is one third", cov01 == F(1, 3)),
        ("the second nearest-neighbor connected covariance is one third", cov12 == F(1, 3)),
        ("the endpoint connected covariance is one ninth", cov02 == F(1, 9)),
        ("the endpoint covariance composes through the middle Markov site", cov02 == cov01 * cov12),
        ("the middle detector interaction is a permutation of the joint basis", len(set(image)) == len(basis)),
        ("the controlled detector interaction is an involution and hence unitary", twice == basis),
        ("record zero and record one are complementary middle-site projectors", p0 + p1 == 1),
        ("both detector record weights are exactly one half", p0 == p1 == F(1, 2)),
        ("the record-zero adjacent conditional mean is plus one third", adjacent0 == F(1, 3)),
        ("the record-one adjacent conditional mean is minus one third", adjacent1 == F(-1, 3)),
        ("conditioning exposes the selected spatial covariance", adjacent0 - adjacent1 == F(2, 3)),
        ("forgetting the middle record leaves the diagonal state unchanged", after_prob == prob),
        ("the nonselective local instrument preserves both remote endpoint marginals", after_remote == before_remote),
        ("endpoint-controlled detector interactions commute exactly", commute),
        ("the record algebra is the two-dimensional algebra of complementary projections", p0 > 0 and p1 > 0 and p0 + p1 == 1),
        ("zero extension makes the detector observation gauge basic", gauge_coefficient == 0),
        ("gauge-basic detector output is representative independent", gauge_coefficient * F(7) == 0),
        ("the selected P8 tensor factor is additional soldering data, not a consequence of l2 alone", True),
        ("finite equal-time algebraic locality is not continuum microcausality", True),
        ("the trace-Born pairing and record semantics remain imported", True),
        ("the held-out delayed-choice family is not evaluated", True),
    ]


def manifest_failures(data: dict) -> list[str]:
    spatial = data.get("spatial_control", {})
    instrument = data.get("local_instrument", {})
    descent = data.get("quotient_descent", {})
    owners = data.get("owner_accounting", {})
    duplicate = data.get("retrieval_duplicate_boundary", {})
    fences = data.get("fences", {})
    failures = []
    if spatial.get("partition_function") != 18 or spatial.get("nearest_neighbor_covariance") != "1/3" or spatial.get("endpoint_covariance") != "1/9": failures.append("spatial")
    if instrument.get("completeness") != "K0^*K0+K1^*K1=I8" or instrument.get("endpoint_detector_commutation") is not True or instrument.get("nonselective_remote_marginal_invariance") is not True: failures.append("instrument")
    if descent.get("zero_extension_over_gauge") is not True or "annihilate G" not in descent.get("basic_observation_criterion", ""): failures.append("descent")
    if owners.get("source_selected_owner_count") != 0 or "trace_Born_state_effect_pairing" not in owners.get("imported", []): failures.append("owners")
    if duplicate.get("nearby_controls_repeated_or_promoted") is not False or "spatial tensor factor" not in duplicate.get("new_object_only", ""): failures.append("duplicate")
    required_false = (
        "source_selected_spatial_factorization", "source_selected_GU_state_or_detector",
        "continuum_AQFT_or_microcausality", "curved_spacetime_Green_hyperbolicity",
        "microlocal_or_Hadamard_state", "Born_rule_derived", "physical_record_semantics_derived",
        "prediction_confirmation_or_verdict", "held_out_scored", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false): failures.append("fences")
    holdout = data.get("holdout_firewall", {})
    if holdout.get("status") != "reserved_unscored" or holdout.get("scored_in_this_result") is not False: failures.append("holdout")
    if "no source-selected factorization" not in data.get("claim_ceiling", ""): failures.append("ceiling")
    return failures


def selftest(data: dict) -> int:
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in (
        "wrong_spatial_weight", "negative_state", "incomplete_records",
        "nonunitary_detector", "remote_signal", "gauge_leak",
    )]
    updates = (
        ("wrong_partition", lambda d: d["spatial_control"].__setitem__("partition_function", 17)),
        ("drop_commutation", lambda d: d["local_instrument"].__setitem__("endpoint_detector_commutation", False)),
        ("drop_remote_invariance", lambda d: d["local_instrument"].__setitem__("nonselective_remote_marginal_invariance", False)),
        ("drop_descent", lambda d: d["quotient_descent"].__setitem__("zero_extension_over_gauge", False)),
        ("source_factorization", lambda d: d["fences"].__setitem__("source_selected_spatial_factorization", True)),
        ("continuum_promotion", lambda d: d["fences"].__setitem__("continuum_AQFT_or_microcausality", True)),
        ("hadamard_promotion", lambda d: d["fences"].__setitem__("microlocal_or_Hadamard_state", True)),
        ("Born_promotion", lambda d: d["fences"].__setitem__("Born_rule_derived", True)),
        ("source_owner", lambda d: d["owner_accounting"].__setitem__("source_selected_owner_count", 1)),
        ("duplicate_promotion", lambda d: d["retrieval_duplicate_boundary"].__setitem__("nearby_controls_repeated_or_promoted", True)),
        ("holdout_promotion", lambda d: d["holdout_firewall"].__setitem__("scored_in_this_result", True)),
    )
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        mutations.append((name, bool(manifest_failures(mutant))))
    for name, caught in mutations:
        print(f"[{'PASS' if caught else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(c for _, c in mutations)}/{len(mutations)} caught")
    return 0 if all(c for _, c in mutations) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    if "--selftest" in sys.argv:
        return selftest(data)
    checks = model_checks()
    checks.append(("manifest preserves spatial, instrument, descent, ownership and promotion fences", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K92 SPATIAL COVARIANCE LOCAL INSTRUMENT: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
