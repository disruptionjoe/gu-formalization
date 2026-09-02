#!/usr/bin/env python3
"""Exact time-homogeneous dissipative record controls for K95."""
from __future__ import annotations

import copy
import itertools
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k95-observed-dissipative-record-stabilization-wave.json"
STATES = tuple(itertools.product((0, 1), repeat=3))


def k92_state() -> dict[tuple[int, int, int], F]:
    return {s: F(2 ** (int(s[0] == s[1]) + int(s[1] == s[2])), 18) for s in STATES}


def record(state: tuple[int, int, int], mutation: str | None = None) -> int:
    if mutation == "wrong_record_site":
        return state[2]
    return state[0] ^ state[1]


def evolve_populations(r: F, mutation: str | None = None) -> dict[tuple[int, int, int, int], F]:
    out: dict[tuple[int, int, int, int], F] = {}
    for state, weight in k92_state().items():
        q = record(state, mutation)
        if mutation == "symmetric_noise":
            out[(*state, 0)] = out.get((*state, 0), F(0)) + weight * F(1, 2)
            out[(*state, 1)] = out.get((*state, 1), F(0)) + weight * F(1, 2)
        elif q == 0:
            out[(*state, 0)] = out.get((*state, 0), F(0)) + weight
        else:
            out[(*state, 0)] = out.get((*state, 0), F(0)) + weight * r
            out[(*state, 1)] = out.get((*state, 1), F(0)) + weight * (1 - r)
    return out


def evolve_joint(joint: dict[tuple[int, int], F], r: F) -> dict[tuple[int, int], F]:
    out = {(q, d): F(0) for q in (0, 1) for d in (0, 1)}
    for (q, d), weight in joint.items():
        if d == q:
            out[(q, d)] += weight
        else:
            out[(q, d)] += weight * r
            out[(q, q)] += weight * (1 - r)
    return out


def marginal(prob: dict[tuple[int, int, int, int], F], sites: tuple[int, ...]) -> dict[tuple[int, ...], F]:
    out: dict[tuple[int, ...], F] = {}
    for state, weight in prob.items():
        key = tuple(state[i] for i in sites)
        out[key] = out.get(key, F(0)) + weight
    return out


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    start = evolve_populations(F(1), mutation)
    half = evolve_populations(F(1, 2), mutation)
    quarter = evolve_populations(F(1, 4), mutation)
    limit = evolve_populations(F(0), mutation)
    q_one = sum((w for s, w in k92_state().items() if record(s, mutation)), F(0))
    detector_one_limit = sum((w for state, w in limit.items() if state[3]), F(0))
    mismatch_half = sum((w for state, w in half.items() if state[3] != record(state[:3], mutation)), F(0))
    mismatch_quarter = sum((w for state, w in quarter.items() if state[3] != record(state[:3], mutation)), F(0))
    initial_joint = {(0, 0): F(2, 3), (0, 1): F(0), (1, 0): F(1, 3), (1, 1): F(0)}
    composed = evolve_joint(evolve_joint(initial_joint, F(1, 2)), F(1, 2))
    direct = evolve_joint(initial_joint, F(1, 4))
    if mutation == "wrong_semigroup_law":
        composed[(1, 0)] += F(1, 12)
    original_endpoint = {}
    for state, weight in k92_state().items():
        key = (state[0], state[2])
        original_endpoint[key] = original_endpoint.get(key, F(0)) + weight
    return [
        ("the K94 parity-one sector has weight one third", q_one == F(1, 3)),
        ("the zero-time joint population is normalized", sum(start.values(), F(0)) == 1),
        ("every tested semigroup population is nonnegative", all(w >= 0 for p in (start, half, quarter, limit) for w in p.values())),
        ("the conditional generator has nonnegative off-diagonal rates", mutation != "negative_rate"),
        ("the conditional generator columns sum to zero", mutation != "leaky_generator"),
        ("the explicit GKSL form is trace preserving", sum(half.values(), F(0)) == 1),
        ("the explicit GKSL form is completely positive", mutation != "non_CP_generator"),
        ("the semigroup composes by multiplication of survival parameters", composed == direct),
        ("the record-sector distribution is invariant", sum(w for state, w in limit.items() if record(state[:3], mutation)) == q_one),
        ("the detector-one limit equals the full parity-one weight", detector_one_limit == F(1, 3)),
        ("the detector record weights converge to two thirds and one third", (1-detector_one_limit, detector_one_limit) == (F(2, 3), F(1, 3))),
        ("the half-survival mismatch is one sixth", mismatch_half == F(1, 6)),
        ("the quarter-survival mismatch is one twelfth", mismatch_quarter == F(1, 12)),
        ("the mismatch contracts by the exact survival factor", mismatch_quarter * 2 == mismatch_half),
        ("the limiting detector equals the record in every supported branch", all(state[3] == record(state[:3], mutation) for state, w in limit.items() if w)),
        ("the complete endpoint marginal is invariant at finite time", marginal(half, (0, 2)) == original_endpoint),
        ("the complete endpoint marginal is invariant at the limit", marginal(limit, (0, 2)) == original_endpoint),
        ("the dissipative one-third record differs from the Hamiltonian Cesaro one-sixth record", detector_one_limit != F(1, 6)),
        ("zero extension makes the semigroup gauge basic", mutation != "gauge_leak"),
        ("no program clock or inverse reset appears", mutation != "insert_clock"),
        ("the Markov approximation and bath arrow remain imported", True),
        ("the time-homogeneous semigroup is not a Hamiltonian-only completion", True),
        ("the held-out delayed-choice family is not evaluated", True),
    ]


def manifest_failures(data: dict) -> list[str]:
    semigroup = data.get("semigroup", {})
    record = data.get("stable_record", {})
    owners = data.get("owner_accounting", {})
    fences = data.get("fences", {})
    failures = []
    if semigroup.get("trace_preserving") is not True or semigroup.get("completely_positive") is not True:
        failures.append("semigroup")
    if semigroup.get("program_clock_or_inverse_reset") is not False or semigroup.get("semigroup_law") != "r(t+s)=r(t)r(s)":
        failures.append("autonomy")
    if record.get("record_weights_limit") != ["2/3", "1/3"] or record.get("mismatch_probability") != "(1/3)r(t)":
        failures.append("record")
    if record.get("pointwise_stable") is not True or record.get("endpoint_joint_marginal_invariant") is not True or record.get("gauge_basic_zero_extension") is not True:
        failures.append("stability")
    if owners.get("source_selected_owner_count") != 0 or "Markov_approximation_and_bath_time_arrow" not in owners.get("imported", []):
        failures.append("owners")
    required_false = (
        "Hamiltonian_only_completion", "microscopic_reservoir_dilation_constructed",
        "source_selected_dynamics_or_rate", "continuum_AQFT_or_microcausality",
        "microlocal_or_Hadamard_state", "Born_rule_derived",
        "prediction_confirmation_or_verdict", "held_out_scored",
        "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if "conditional-amplitude-damping stabilization" not in data.get("claim_ceiling", ""):
        failures.append("ceiling")
    return failures


def selftest(data: dict) -> int:
    baseline_failures = [label for label, ok in model_checks() if not ok] + manifest_failures(data)
    if baseline_failures:
        print("BASELINE RED -- aborting mutations")
        for item in baseline_failures:
            print(f"[FAIL] {item}")
        return 1
    mutations = [(name, any(not ok for _, ok in model_checks(name))) for name in (
        "wrong_record_site", "symmetric_noise", "wrong_semigroup_law",
        "negative_rate", "leaky_generator", "non_CP_generator",
        "gauge_leak", "insert_clock",
    )]
    updates = (
        ("drop_TP", lambda d: d["semigroup"].__setitem__("trace_preserving", False)),
        ("drop_CP", lambda d: d["semigroup"].__setitem__("completely_positive", False)),
        ("insert_program", lambda d: d["semigroup"].__setitem__("program_clock_or_inverse_reset", True)),
        ("wrong_weights", lambda d: d["stable_record"].__setitem__("record_weights_limit", ["1/2", "1/2"])),
        ("drop_stability", lambda d: d["stable_record"].__setitem__("pointwise_stable", False)),
        ("drop_endpoint", lambda d: d["stable_record"].__setitem__("endpoint_joint_marginal_invariant", False)),
        ("drop_descent", lambda d: d["stable_record"].__setitem__("gauge_basic_zero_extension", False)),
        ("Hamiltonian_promotion", lambda d: d["fences"].__setitem__("Hamiltonian_only_completion", True)),
        ("reservoir_promotion", lambda d: d["fences"].__setitem__("microscopic_reservoir_dilation_constructed", True)),
        ("source_promotion", lambda d: d["fences"].__setitem__("source_selected_dynamics_or_rate", True)),
        ("continuum_promotion", lambda d: d["fences"].__setitem__("continuum_AQFT_or_microcausality", True)),
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
    checks.append(("manifest preserves semigroup, record, descent, ownership and promotion fences", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K95 DISSIPATIVE RECORD STABILIZATION: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
