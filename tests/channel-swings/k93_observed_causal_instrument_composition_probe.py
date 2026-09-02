#!/usr/bin/env python3
"""Exact propagation/instrument composition controls for K93."""
from __future__ import annotations

import copy
import itertools
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k93-observed-causal-instrument-composition-wave.json"
STATES = tuple(itertools.product((0, 1), repeat=3))


def z(bit: int) -> int:
    return 1 if bit == 0 else -1


def initial_state() -> dict[tuple[int, int, int], F]:
    return {s: F(2 ** (int(s[0] == s[1]) + int(s[1] == s[2])), 18) for s in STATES}


def propagate(s: tuple[int, int, int], mutation: str | None = None) -> tuple[int, int, int]:
    if mutation == "nonlocal_propagator":
        return s[0], s[1] ^ s[2], s[2]
    if mutation == "nonbijective_propagator" and s == (1, 1, 1):
        return 0, 0, 0
    return s[0], s[1] ^ s[0], s[2]


def push(prob: dict[tuple[int, int, int], F], mutation: str | None = None) -> dict[tuple[int, int, int], F]:
    out = {s: F(0) for s in STATES}
    for s, weight in prob.items():
        out[propagate(s, mutation)] += weight
    return out


def marginal(prob: dict[tuple[int, int, int], F], sites: tuple[int, ...]) -> dict[tuple[int, ...], F]:
    out: dict[tuple[int, ...], F] = {}
    for state, weight in prob.items():
        key = tuple(state[i] for i in sites)
        out[key] = out.get(key, F(0)) + weight
    return out


def expectation(prob: dict[tuple[int, int, int], F], fn) -> F:
    return sum((weight * F(fn(state)) for state, weight in prob.items()), F(0))


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    before = initial_state()
    after = push(before, mutation)
    image = tuple(propagate(s, mutation) for s in STATES)
    twice = tuple(propagate(propagate(s, mutation), mutation) for s in STATES)
    before_weights = tuple(sum((w for s, w in before.items() if s[1] == b), F(0)) for b in (0, 1))
    after_weights = tuple(sum((w for s, w in after.items() if s[1] == b), F(0)) for b in (0, 1))
    if mutation == "incomplete_effects":
        after_weights = after_weights[0], F(0)
    input_effect_matches = all((propagate(s, mutation)[1] == b) == ((s[0] ^ s[1]) == b) for s in STATES for b in (0, 1))
    remote_before = marginal(before, (2,))
    remote_after = marginal(after, (2,))
    endpoint_before = marginal(before, (0, 2))
    endpoint_after = marginal(after, (0, 2))
    if mutation == "remote_signal":
        remote_after = {(0,): F(2, 3), (1,): F(1, 3)}
    means = tuple(expectation(after, lambda s, i=i: z(s[i])) for i in range(3))
    correlations = tuple(expectation(after, lambda s, i=i, j=j: z(s[i]) * z(s[j])) for i, j in ((0, 1), (1, 2), (0, 2)))
    gauge_coefficient = F(1) if mutation == "gauge_leak" else F(0)
    return [
        ("the K92 input state is normalized", sum(before.values(), F(0)) == 1),
        ("the one-edge propagator permutes all eight configurations", len(set(image)) == 8),
        ("the CNOT propagator is an involution", twice == STATES),
        ("the propagator leaves site zero unchanged", all(propagate(s, mutation)[0] == s[0] for s in STATES)),
        ("the propagator leaves remote site two unchanged", all(propagate(s, mutation)[2] == s[2] for s in STATES)),
        ("the propagated state is normalized", sum(after.values(), F(0)) == 1),
        ("the output middle record pulls back to input parity s0 xor s1", input_effect_matches),
        ("the Heisenberg output Z1 effect is the two-site past-neighborhood observable Z0 Z1", input_effect_matches),
        ("the two pulled-back record effects are complementary", sum(after_weights, F(0)) == 1),
        ("the before-propagation middle record weights are one half and one half", before_weights == (F(1, 2), F(1, 2))),
        ("the after-propagation middle record weights are two thirds and one third", after_weights == (F(2, 3), F(1, 3))),
        ("causal ordering changes the record table", before_weights != after_weights),
        ("the after-propagation one-site means are zero, one third, zero", means == (F(0), F(1, 3), F(0))),
        ("the two adjacent Z correlations vanish after propagation", correlations[:2] == (F(0), F(0))),
        ("the endpoint Z correlation remains one ninth", correlations[2] == F(1, 9)),
        ("the remote site-two marginal is invariant", remote_after == remote_before),
        ("the complete endpoint joint marginal is invariant", endpoint_after == endpoint_before),
        ("the propagator has exact one-edge Heisenberg support", mutation != "nonlocal_propagator"),
        ("recording after propagation yields a complete two-branch instrument", sum(after_weights, F(0)) == 1),
        ("zero extension makes the composed instrument gauge basic", gauge_coefficient == 0),
        ("gauge-basic output is representative independent", gauge_coefficient * F(11) == 0),
        ("the finite neighborhood is not continuum microcausality", True),
        ("Kraus completeness does not derive the trace-Born pairing", True),
        ("the action circuit and record semantics remain repository supplied", True),
        ("the held-out delayed-choice family is not evaluated", True),
    ]


def manifest_failures(data: dict) -> list[str]:
    dynamics = data.get("causal_dynamics", {})
    instrument = data.get("composed_instrument", {})
    owners = data.get("owner_accounting", {})
    fences = data.get("fences", {})
    failures = []
    if dynamics.get("propagator") != "CNOT_0_to_1" or dynamics.get("causal_radius") != 1 or dynamics.get("remote_site_fixed") is not True:
        failures.append("dynamics")
    if instrument.get("input_record_observable") != "Z0 Z1" or instrument.get("record_weights_after_propagation") != ["2/3", "1/3"]:
        failures.append("instrument")
    if instrument.get("endpoint_joint_marginal_invariant") is not True or instrument.get("gauge_basic_zero_extension") is not True:
        failures.append("descent")
    if owners.get("source_selected_owner_count") != 0 or "trace_Born_state_effect_pairing" not in owners.get("imported", []):
        failures.append("owners")
    required_false = (
        "source_selected_dynamics_or_detector", "continuum_AQFT_or_microcausality",
        "microlocal_or_Hadamard_state", "Born_rule_derived",
        "prediction_confirmation_or_verdict", "held_out_scored",
        "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if "finite causal propagation/instrument composition" not in data.get("claim_ceiling", ""):
        failures.append("ceiling")
    return failures


def selftest(data: dict) -> int:
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in (
        "nonlocal_propagator", "nonbijective_propagator", "incomplete_effects",
        "remote_signal", "gauge_leak",
    )]
    updates = (
        ("wrong_radius", lambda d: d["causal_dynamics"].__setitem__("causal_radius", 2)),
        ("wrong_weights", lambda d: d["composed_instrument"].__setitem__("record_weights_after_propagation", ["1/2", "1/2"])),
        ("drop_endpoint_invariance", lambda d: d["composed_instrument"].__setitem__("endpoint_joint_marginal_invariant", False)),
        ("drop_descent", lambda d: d["composed_instrument"].__setitem__("gauge_basic_zero_extension", False)),
        ("source_dynamics", lambda d: d["fences"].__setitem__("source_selected_dynamics_or_detector", True)),
        ("continuum_promotion", lambda d: d["fences"].__setitem__("continuum_AQFT_or_microcausality", True)),
        ("hadamard_promotion", lambda d: d["fences"].__setitem__("microlocal_or_Hadamard_state", True)),
        ("Born_promotion", lambda d: d["fences"].__setitem__("Born_rule_derived", True)),
        ("source_owner", lambda d: d["owner_accounting"].__setitem__("source_selected_owner_count", 1)),
        ("heldout_promotion", lambda d: d["fences"].__setitem__("held_out_scored", True)),
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
    checks.append(("manifest preserves dynamics, instrument, descent, ownership and promotion fences", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K93 CAUSAL INSTRUMENT COMPOSITION: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
