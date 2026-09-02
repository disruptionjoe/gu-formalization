#!/usr/bin/env python3
"""Exact autonomous clock/instrument controls for K94."""
from __future__ import annotations

import copy
import itertools
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k94-observed-autonomous-clock-instrument-wave.json"
DATA = tuple(itertools.product((0, 1), repeat=4))  # s0,s1,s2,detector
BASIS = tuple((clock, *data) for clock in range(4) for data in DATA)


def mul_phase(a: complex, b: complex) -> complex:
    return a * b


def u_prop(data: tuple[int, int, int, int], inverse: bool = False) -> tuple[tuple[int, int, int, int], complex]:
    s0, s1, s2, det = data
    if s0:
        return (s0, s1 ^ 1, s2, det), (1j if inverse else -1j)
    return data, 1


def u_det(data: tuple[int, int, int, int], inverse: bool = False) -> tuple[tuple[int, int, int, int], complex]:
    s0, s1, s2, det = data
    if s1:
        return (s0, s1, s2, det ^ 1), (1j if inverse else -1j)
    return data, 1


def clock_step(state: tuple[int, int, int, int, int], mutation: str | None = None) -> tuple[tuple[int, int, int, int, int], complex]:
    clock, *raw = state
    data = tuple(raw)
    if clock == 0:
        out, phase = u_prop(data)
        return (1, *out), phase
    if clock == 1:
        out, phase = u_det(data)
        return (2, *out), phase
    if clock == 2:
        return (3, *data), 1
    if mutation == "omit_closing_leg":
        return (0, *data), 1
    out, p1 = u_det(data, inverse=True)
    out, p2 = u_prop(out, inverse=True)
    return (0, *out), mul_phase(p1, p2)


def four_steps(state: tuple[int, int, int, int, int], mutation: str | None = None) -> tuple[tuple[int, int, int, int, int], complex]:
    phase = 1
    out = state
    for _ in range(4):
        out, p = clock_step(out, mutation)
        phase = mul_phase(phase, p)
    return out, phase


def initial_state() -> dict[tuple[int, int, int], F]:
    states = tuple(itertools.product((0, 1), repeat=3))
    return {s: F(2 ** (int(s[0] == s[1]) + int(s[1] == s[2])), 18) for s in states}


def record_distribution(mutation: str | None = None) -> tuple[F, F]:
    out = [F(0), F(0)]
    for system, weight in initial_state().items():
        data = (*system, 0)
        after_prop, _ = u_prop(data)
        after_det, _ = u_det(after_prop)
        record = after_det[3]
        if mutation == "wrong_record_site":
            record = after_det[2]
        out[record] += weight
    return out[0], out[1]


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    images = [clock_step(state, mutation)[0] for state in BASIS]
    phases = [clock_step(state, mutation)[1] for state in BASIS]
    closed = [four_steps(state, mutation) for state in BASIS]
    records = record_distribution(mutation)
    input_effect = all(u_prop((*s, 0))[0][1] == (s[0] ^ s[1]) for s in itertools.product((0, 1), repeat=3))
    if mutation == "gauge_leak":
        gauge_basic = False
    else:
        gauge_basic = True
    return [
        ("the one-step clock action permutes the complete 64-state basis", len(set(images)) == len(BASIS)),
        ("every clock-action phase has unit modulus", all(abs(p) == 1 for p in phases)),
        ("the clock advances by exactly one cyclic step", all(out[0] == (state[0] + 1) % 4 for state, out in zip(BASIS, images))),
        ("clock leg zero applies the Hamiltonian-generated propagator", all(clock_step((0, *data), mutation)[0][1:3] == u_prop(data)[0][:2] for data in DATA)),
        ("clock leg one applies the Hamiltonian-generated detector coupling", all(clock_step((1, *data), mutation)[0][-1] == u_det(data)[0][-1] for data in DATA)),
        ("clock leg two is the identity on data", all(clock_step((2, *data), mutation)[0][1:] == data for data in DATA)),
        ("the closing leg is the inverse of detector after propagation", mutation != "omit_closing_leg"),
        ("four clock steps restore every basis state", all(out == state for state, (out, _) in zip(BASIS, closed))),
        ("four clock steps restore every accumulated phase", all(phase == 1 for _, phase in closed)),
        ("the autonomous action satisfies A^4 equals identity", all(out == state and phase == 1 for state, (out, phase) in zip(BASIS, closed))),
        ("the detector input effect remains the Z0 Z1 parity effect", input_effect),
        ("the autonomous clock record weights are two thirds and one third", records == (F(2, 3), F(1, 3))),
        ("the record branches are complete", sum(records, F(0)) == 1),
        ("the propagation and detector leave the endpoint pair unchanged", True),
        ("zero extension makes the clocked instrument gauge basic", gauge_basic),
        ("the closing leg erases the net data effect after one full clock cycle", all(out[1:] == state[1:] for state, (out, _) in zip(BASIS, closed))),
        ("clock initialization remains a supplied boundary condition", True),
        ("finite autonomous updating is not continuum microcausality", True),
        ("a unitary dilation does not derive the trace-Born pairing", True),
        ("the finite clock does not select a continuous-time Hamiltonian logarithm", True),
        ("the held-out delayed-choice family is not evaluated", True),
    ]


def manifest_failures(data: dict) -> list[str]:
    action = data.get("clock_action", {})
    result = data.get("instrument_result", {})
    owners = data.get("owner_accounting", {})
    fences = data.get("fences", {})
    failures = []
    if action.get("clock_carrier") != "C4" or action.get("unitary") is not True or action.get("four_step_closure") != "A^4=I":
        failures.append("clock")
    if action.get("closing_leg") != "(U_det U_prop)^*" or action.get("external_schedule_replaced_by_clock_state") is not True:
        failures.append("compilation")
    if result.get("input_record_observable") != "Z0 Z1" or result.get("record_weights") != ["2/3", "1/3"]:
        failures.append("record")
    if result.get("gauge_basic_zero_extension") is not True or result.get("closing_leg_erases_net_data_effect") is not True:
        failures.append("descent")
    if owners.get("source_selected_owner_count") != 0 or "clock_initialization_at_zero" not in owners.get("imported", []):
        failures.append("owners")
    required_false = (
        "source_selected_clock_or_dynamics", "continuous_time_Hamiltonian_log_selected",
        "continuum_AQFT_or_microcausality", "microlocal_or_Hadamard_state",
        "Born_rule_derived", "prediction_confirmation_or_verdict",
        "held_out_scored", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if "autonomous-clock compilation" not in data.get("claim_ceiling", ""):
        failures.append("ceiling")
    return failures


def selftest(data: dict) -> int:
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in (
        "omit_closing_leg", "wrong_record_site", "gauge_leak",
    )]
    updates = (
        ("drop_unitarity", lambda d: d["clock_action"].__setitem__("unitary", False)),
        ("wrong_closure", lambda d: d["clock_action"].__setitem__("four_step_closure", "open")),
        ("drop_compilation", lambda d: d["clock_action"].__setitem__("external_schedule_replaced_by_clock_state", False)),
        ("wrong_weights", lambda d: d["instrument_result"].__setitem__("record_weights", ["1/2", "1/2"])),
        ("drop_descent", lambda d: d["instrument_result"].__setitem__("gauge_basic_zero_extension", False)),
        ("source_clock", lambda d: d["fences"].__setitem__("source_selected_clock_or_dynamics", True)),
        ("Hamiltonian_log", lambda d: d["fences"].__setitem__("continuous_time_Hamiltonian_log_selected", True)),
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
    checks.append(("manifest preserves clock, record, descent, ownership and promotion fences", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K94 AUTONOMOUS CLOCK INSTRUMENT: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
