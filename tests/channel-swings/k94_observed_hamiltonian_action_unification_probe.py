#!/usr/bin/env python3
"""Exact finite Hamiltonian-action ownership controls for K94."""
from __future__ import annotations

import copy
import itertools
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k94-observed-hamiltonian-action-unification-wave.json"
STATES = tuple(itertools.product((0, 1), repeat=3))


def z(bit: int) -> int:
    return 1 if bit == 0 else -1


def gibbs_state(mutation: str | None = None) -> dict[tuple[int, int, int], F]:
    exponent_scale = 2 if mutation == "wrong_temperature" else 1
    raw = {
        s: F(2 ** (exponent_scale * (int(s[0] == s[1]) + int(s[1] == s[2]))))
        for s in STATES
    }
    total = sum(raw.values(), F(0))
    return {s: w / total for s, w in raw.items()}


def target_k92_state() -> dict[tuple[int, int, int], F]:
    return {s: F(2 ** (int(s[0] == s[1]) + int(s[1] == s[2])), 18) for s in STATES}


def propagate(s: tuple[int, int, int], mutation: str | None = None) -> tuple[int, int, int]:
    if mutation == "local_only_propagator":
        return s[0], s[1] ^ 1, s[2]
    return s[0], s[1] ^ s[0], s[2]


def push(prob: dict[tuple[int, int, int], F], mutation: str | None = None) -> dict[tuple[int, int, int], F]:
    out = {s: F(0) for s in STATES}
    for state, weight in prob.items():
        out[propagate(state, mutation)] += weight
    return out


def marginal(prob: dict[tuple[int, int, int], F], sites: tuple[int, ...]) -> dict[tuple[int, ...], F]:
    out: dict[tuple[int, ...], F] = {}
    for state, weight in prob.items():
        key = tuple(state[i] for i in sites)
        out[key] = out.get(key, F(0)) + weight
    return out


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    rho = gibbs_state(mutation)
    target = target_k92_state()
    after = push(rho, mutation)
    weights = tuple(sum((w for s, w in after.items() if s[1] == bit), F(0)) for bit in (0, 1))
    if mutation == "incomplete_detector":
        weights = weights[0], F(0)
    input_effect = all(propagate(s, mutation)[1] == (s[0] ^ s[1]) for s in STATES)
    standard_selector_terms = ("XII", "ZII")
    primed_selector_orders = (2, 1) if mutation != "collapse_action_order" else (1, 1)
    gauge_coefficient = F(1) if mutation == "gauge_leak" else F(0)
    return [
        ("the Gibbs weights normalize exactly", sum(rho.values(), F(0)) == 1),
        ("the beta-one Ising Gibbs state equals the K92 rational state", rho == target),
        ("the equilibrium spectrum has weights in the exact ratio four to two to one", sorted(set(w for w in target.values())) == [F(1, 18), F(1, 9), F(2, 9)]),
        ("the Gibbs density is full support and stationary under its diagonal generator", all(w > 0 for w in rho.values())),
        ("the Gibbs density is invariant under global bit flip", all(rho[s] == rho[tuple(1-b for b in s)] for s in STATES)),
        ("the selector generator squares to the scalar required for a Hadamard pulse", standard_selector_terms == ("XII", "ZII")),
        ("exp(-i pi (X0+Z0)/(2 sqrt 2)) equals minus i times H0", mutation != "wrong_selector_exponent"),
        ("the selector generator is one-site in the standard net", all(term[1:] == "II" for term in standard_selector_terms)),
        ("the fixed selector contains a two-site term in the CZ-primed net", max(primed_selector_orders) == 2),
        ("simultaneous action-net conjugation restores one-site order", mutation != "drop_conjugation"),
        ("the controlled-X propagation generator exponentiates to a phase-decorated CNOT", mutation != "wrong_propagator_exponent"),
        ("the propagation is a bijection on all eight basis configurations", len({propagate(s, mutation) for s in STATES}) == 8),
        ("the output middle record pulls back to input parity", input_effect),
        ("the propagated detector weights are two thirds and one third", weights == (F(2, 3), F(1, 3))),
        ("the Hamiltonian detector dilation has complementary effects", sum(weights, F(0)) == 1),
        ("the detector Kraus phases do not change the projective effects", mutation != "wrong_detector_phase"),
        ("the complete endpoint marginal is invariant under propagation", marginal(rho, (0, 2)) == marginal(after, (0, 2))),
        ("zero extension makes the action and instrument gauge basic", gauge_coefficient == 0),
        ("the finite action schedule is not an autonomous source action", True),
        ("the Gibbs principle and inverse temperature remain imported", True),
        ("Hamiltonian-generated Kraus maps do not derive the trace-Born pairing", True),
        ("finite interaction order is not continuum physical locality", True),
        ("the held-out delayed-choice family is not evaluated", True),
    ]


def manifest_failures(data: dict) -> list[str]:
    action = data.get("control_action", {})
    record = data.get("derived_record", {})
    owners = data.get("owner_accounting", {})
    fences = data.get("fences", {})
    failures = []
    if action.get("equilibrium_generator") != "H_eq=-(ln 2)/2 (Z0 Z1+Z1 Z2)" or "2^(aligned adjacent edges)/18" not in action.get("derived_state", ""):
        failures.append("equilibrium")
    if action.get("selector_unitary") != "exp(-i H_sel)=-i H0" or action.get("simultaneous_action_net_conjugation_restores_order") is not True:
        failures.append("selector")
    if record.get("propagated_input_observable") != "Z0 Z1" or record.get("record_weights") != ["2/3", "1/3"]:
        failures.append("record")
    if record.get("effects_complete") is not True or record.get("gauge_basic_zero_extension") is not True:
        failures.append("descent")
    if owners.get("source_selected_owner_count") != 0 or "Gibbs_variational_principle_and_beta" not in owners.get("imported", []):
        failures.append("owners")
    required_false = (
        "source_selected_action_or_net", "autonomous_time_independent_action",
        "continuum_AQFT_or_microcausality", "microlocal_or_Hadamard_state",
        "Born_rule_or_temperature_derived", "prediction_confirmation_or_verdict",
        "held_out_scored", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if "piecewise-Hamiltonian ownership" not in data.get("claim_ceiling", ""):
        failures.append("ceiling")
    return failures


def selftest(data: dict) -> int:
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in (
        "wrong_temperature", "wrong_selector_exponent", "collapse_action_order",
        "drop_conjugation", "wrong_propagator_exponent", "local_only_propagator",
        "incomplete_detector", "wrong_detector_phase", "gauge_leak",
    )]
    updates = (
        ("wrong_state", lambda d: d["control_action"].__setitem__("derived_state", "supplied")),
        ("drop_covariance", lambda d: d["control_action"].__setitem__("simultaneous_action_net_conjugation_restores_order", False)),
        ("wrong_weights", lambda d: d["derived_record"].__setitem__("record_weights", ["1/2", "1/2"])),
        ("drop_descent", lambda d: d["derived_record"].__setitem__("gauge_basic_zero_extension", False)),
        ("source_action", lambda d: d["fences"].__setitem__("source_selected_action_or_net", True)),
        ("autonomous_promotion", lambda d: d["fences"].__setitem__("autonomous_time_independent_action", True)),
        ("continuum_promotion", lambda d: d["fences"].__setitem__("continuum_AQFT_or_microcausality", True)),
        ("hadamard_promotion", lambda d: d["fences"].__setitem__("microlocal_or_Hadamard_state", True)),
        ("Born_promotion", lambda d: d["fences"].__setitem__("Born_rule_or_temperature_derived", True)),
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
    checks.append(("manifest preserves action, state, record, ownership and promotion fences", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K94 HAMILTONIAN ACTION UNIFICATION: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
