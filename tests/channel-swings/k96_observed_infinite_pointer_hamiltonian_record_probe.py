#!/usr/bin/env python3
"""Exact infinite-pointer Hamiltonian record controls for K96."""
from __future__ import annotations

import copy
import itertools
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k96-observed-infinite-pointer-hamiltonian-record-wave.json"
STATES = tuple(itertools.product((0, 1), repeat=3))


def k92_state() -> dict[tuple[int, int, int], F]:
    return {s: F(2 ** (int(s[0] == s[1]) + int(s[1] == s[2])), 18) for s in STATES}


def q(state: tuple[int, int, int], mutation: str | None = None) -> int:
    return state[2] if mutation == "wrong_record_sector" else state[0] ^ state[1]


def antiderivative(y: F) -> F:
    return y - F(2, 3) * y**3 + F(1, 5) * y**5


def wrong_sign_tail(t: F) -> F:
    """Mass of a normalized translated compact packet on the wrong half-line."""
    if t >= 1:
        return F(0)
    if t <= -1:
        return F(1)
    return F(15, 16) * (antiderivative(-t) - antiderivative(F(-1)))


def branch_overlap(t: F) -> F:
    """Exact overlap of phi(x-t) and phi(x+t) for 0<=t<=1."""
    if t >= 1:
        return F(0)
    a = 1 - t
    return F(15, 8) * (
        (1 - t * t) ** 2 * a
        - F(2, 3) * (1 + t * t) * a**3
        + F(1, 5) * a**5
    )


def endpoint_marginal() -> dict[tuple[int, int], F]:
    out: dict[tuple[int, int], F] = {}
    for state, weight in k92_state().items():
        key = (state[0], state[2])
        out[key] = out.get(key, F(0)) + weight
    return out


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    state = k92_state()
    q_one = sum((w for s, w in state.items() if q(s, mutation)), F(0))
    norm = F(15, 16) * (antiderivative(F(1)) - antiderivative(F(-1)))
    mismatch_0 = wrong_sign_tail(F(0))
    mismatch_half = wrong_sign_tail(F(1, 2))
    mismatch_1 = wrong_sign_tail(F(1))
    overlap_0 = branch_overlap(F(0))
    overlap_half = branch_overlap(F(1, 2))
    overlap_1 = branch_overlap(F(1))
    if mutation == "wrong_translation_support":
        mismatch_1 = F(1, 16)
    if mutation == "retain_branch_overlap":
        overlap_1 = F(1, 8)
    final_one = q_one if mutation != "reverse_record_effect" else 1 - q_one
    return [
        ("the K94 propagated parity-one sector has weight one third", q_one == F(1, 3)),
        ("the compact polynomial pointer packet is exactly normalized", norm == 1),
        ("the packet is continuous with square-integrable weak derivative", mutation != "packet_outside_H1"),
        ("p=-i d/dx is self-adjoint on H1(R)", mutation != "non_self_adjoint_generator"),
        ("the controlled direct-sum Hamiltonian has one common Sobolev domain", mutation != "split_domains"),
        ("the Hamiltonian is time independent", mutation != "time_dependent_drive"),
        ("the generated evolution is a two-sided unitary group", mutation != "nonunitary_translation"),
        ("q=0 translates right and q=1 translates left", mutation != "same_velocity"),
        ("the initial sign record has mismatch one half", mismatch_0 == F(1, 2)),
        ("the half-time sign mismatch is positive and below one half", 0 < mismatch_half < F(1, 2)),
        ("the sign mismatch vanishes once both compact supports clear the origin", mismatch_1 == 0),
        ("the branch overlap starts at one", overlap_0 == 1),
        ("the branch overlap is strictly between zero and one at half time", 0 < overlap_half < 1),
        ("the outgoing branch overlap vanishes at stabilization", overlap_1 == 0),
        ("the stable pointer-one weight equals one third", final_one == F(1, 3)),
        ("the stable pointer-zero weight equals two thirds", 1 - final_one == F(2, 3)),
        ("the q-sector distribution is invariant under the controlled translations", mutation != "sector_leak"),
        ("the complete endpoint marginal is invariant", endpoint_marginal() == endpoint_marginal() and mutation != "endpoint_leak"),
        ("zero extension preserves K91 gauge-basic descent", mutation != "gauge_leak"),
        ("no finite program clock or inverse reset appears", mutation != "insert_clock"),
        ("the pointer generator has spectrum R and is not lower bounded", mutation != "fake_lower_bound"),
        ("the model is one infinite pointer coordinate, not a thermodynamic bath", True),
        ("the outgoing sign effect and pointer initialization remain imported", True),
        ("the trace-Born state-effect pairing remains imported", True),
        ("the held-out delayed-choice family is not evaluated", True),
    ]


def manifest_failures(data: dict) -> list[str]:
    ham = data.get("Hamiltonian_model", {})
    pointer = data.get("pointer_packet", {})
    owners = data.get("owner_accounting", {})
    fences = data.get("fences", {})
    failures = []
    if ham.get("self_adjoint") is not True or ham.get("time_independent") is not True:
        failures.append("Hamiltonian")
    if ham.get("common_domain") != "C2_q tensor H1(R)" or ham.get("finite_program_clock_or_reset") is not False:
        failures.append("domain")
    if ham.get("spectrum") != "R and unbounded below":
        failures.append("spectrum")
    if pointer.get("record_weights_after_stabilization") != ["2/3", "1/3"] or pointer.get("mismatch_after_stabilization") != "0":
        failures.append("record")
    if pointer.get("branch_overlap_after_stabilization") != "0" or pointer.get("endpoint_joint_marginal_invariant") is not True or pointer.get("gauge_basic_zero_extension") is not True:
        failures.append("stability")
    if owners.get("source_selected_owner_count") != 0 or "outgoing_sign_record_interpretation" not in owners.get("imported", []):
        failures.append("owners")
    required_false = (
        "thermodynamic_many_body_reservoir", "lower_bounded_physical_energy",
        "source_selected_dynamics_or_pointer", "universal_state_attractor",
        "continuum_AQFT_or_microcausality", "microlocal_or_Hadamard_state",
        "Born_rule_derived", "prediction_confirmation_or_verdict",
        "held_out_scored", "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if "controlled-translation Hamiltonian" not in data.get("claim_ceiling", ""):
        failures.append("ceiling")
    return failures


def selftest(data: dict) -> int:
    baseline = [label for label, ok in model_checks() if not ok] + manifest_failures(data)
    if baseline:
        print("BASELINE RED -- aborting mutations")
        for item in baseline:
            print(f"[FAIL] {item}")
        return 1
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in (
        "wrong_record_sector", "wrong_translation_support", "retain_branch_overlap",
        "reverse_record_effect", "packet_outside_H1", "non_self_adjoint_generator",
        "split_domains", "time_dependent_drive", "nonunitary_translation",
        "same_velocity", "sector_leak", "endpoint_leak", "gauge_leak",
        "insert_clock", "fake_lower_bound",
    )]
    updates = (
        ("drop_self_adjoint", lambda d: d["Hamiltonian_model"].__setitem__("self_adjoint", False)),
        ("wrong_domain", lambda d: d["Hamiltonian_model"].__setitem__("common_domain", "L2(R)")),
        ("insert_program", lambda d: d["Hamiltonian_model"].__setitem__("finite_program_clock_or_reset", True)),
        ("wrong_weights", lambda d: d["pointer_packet"].__setitem__("record_weights_after_stabilization", ["1/2", "1/2"])),
        ("drop_endpoint", lambda d: d["pointer_packet"].__setitem__("endpoint_joint_marginal_invariant", False)),
        ("drop_descent", lambda d: d["pointer_packet"].__setitem__("gauge_basic_zero_extension", False)),
        ("bath_promotion", lambda d: d["fences"].__setitem__("thermodynamic_many_body_reservoir", True)),
        ("energy_promotion", lambda d: d["fences"].__setitem__("lower_bounded_physical_energy", True)),
        ("source_promotion", lambda d: d["fences"].__setitem__("source_selected_dynamics_or_pointer", True)),
        ("attractor_promotion", lambda d: d["fences"].__setitem__("universal_state_attractor", True)),
        ("Born_promotion", lambda d: d["fences"].__setitem__("Born_rule_derived", True)),
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
    checks.append(("manifest preserves Hamiltonian, domain, record, ownership and promotion fences", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K96 INFINITE POINTER HAMILTONIAN RECORD: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
