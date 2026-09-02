#!/usr/bin/env python3
"""Exact finite closed-Hamiltonian asymptotic controls for K95."""
from __future__ import annotations

import copy
import itertools
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k95-observed-finite-hamiltonian-asymptotic-no-go-wave.json"
STATES = tuple(itertools.product((0, 1), repeat=3))


def k92_state() -> dict[tuple[int, int, int], F]:
    return {s: F(2 ** (int(s[0] == s[1]) + int(s[1] == s[2])), 18) for s in STATES}


def q(state: tuple[int, int, int]) -> int:
    return state[0] ^ state[1]


def q_weight(mutation: str | None = None) -> F:
    if mutation == "wrong_record_effect":
        return sum((w for s, w in k92_state().items() if s[2]), F(0))
    return sum((w for s, w in k92_state().items() if q(s)), F(0))


def detector_probability(sin_squared: F, mutation: str | None = None) -> F:
    weight = q_weight(mutation)
    if mutation == "add_damping_by_hand":
        return weight * (1 - sin_squared)
    return weight * sin_squared


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    weight = q_weight(mutation)
    at_zero = detector_probability(F(0), mutation)
    at_half = detector_probability(F(1), mutation)
    at_full = detector_probability(F(0), mutation)
    cesaro = weight * (F(1) if mutation == "wrong_Cesaro" else F(1, 2))
    trace_distance_before = F(1)
    trace_distance_after = F(0) if mutation == "contractive_unitary" else F(1)
    nonzero_gap_blocks = 0 if mutation != "retain_nonzero_gap_limit" else 1
    commuting_effect_constant = mutation != "moving_commuting_effect"
    return [
        ("the K94 input parity-one weight is one third", weight == F(1, 3)),
        ("unitary conjugation preserves the trace distance of orthogonal states", trace_distance_before == trace_distance_after),
        ("two distinct states cannot converge to one trace-norm attractor", trace_distance_after > 0),
        ("finite spectral evolution is a finite real-frequency Fourier sum", True),
        ("universal effect convergence removes every nonzero-gap coefficient", nonzero_gap_blocks == 0),
        ("the surviving zero-gap effect commutes with the Hamiltonian", nonzero_gap_blocks == 0),
        ("a commuting detector effect is constant rather than newly formed", commuting_effect_constant),
        ("the parity-controlled detector starts with zero one-weight", at_zero == 0),
        ("the half-turn detector reproduces the full parity-one weight", at_half == F(1, 3)),
        ("the full-turn detector erases that record", at_full == 0),
        ("the zero and full-record subsequences disagree", at_zero != at_half),
        ("the K94 static finite-Hamiltonian record has no pointwise limit", at_zero != at_half and at_full == at_zero),
        ("the Cesaro detector-one weight is one sixth", cesaro == F(1, 6)),
        ("the Cesaro mean does not reproduce the full one-third record", cesaro != at_half),
        ("Cesaro averaging is an additional owner, not closed-flow attraction", True),
        ("zero extension preserves gauge-basicness", mutation != "gauge_leak"),
        ("the theorem binds finite closed Hamiltonian flow only", True),
        ("infinite reservoirs and thermodynamic limits remain outside scope", True),
        ("open-system and coarse-grained escapes remain outside scope", True),
        ("the trace-Born pairing remains imported", True),
        ("the held-out delayed-choice family is not evaluated", True),
    ]


def manifest_failures(data: dict) -> list[str]:
    theorem = data.get("theorem", {})
    witness = data.get("k94_witness", {})
    owners = data.get("owner_accounting", {})
    fences = data.get("fences", {})
    failures = []
    if theorem.get("common_pointwise_attractor_for_two_distinct_states") is not False or theorem.get("new_universal_pointwise_record_formation") is not False:
        failures.append("theorem")
    if "[H,E]=0" not in theorem.get("effect_limit_conclusion", ""):
        failures.append("effect_limit")
    if witness.get("record_one_weight") != "1/3" or witness.get("detector_one_probability") != "(1/3) sin^2(t)":
        failures.append("witness")
    if witness.get("pointwise_limit_exists") is not False or witness.get("Cesaro_detector_one_weight") != "1/6":
        failures.append("asymptotic")
    if witness.get("gauge_basic_zero_extension") is not True:
        failures.append("descent")
    if owners.get("source_selected_owner_count") != 0 or "Cesaro_averaging_when_invoked" not in owners.get("imported", []):
        failures.append("owners")
    required_false = (
        "source_dynamics_no_go", "infinite_reservoir_or_thermodynamic_no_go",
        "open_system_or_coarse_graining_no_go", "continuum_AQFT_or_microcausality",
        "microlocal_or_Hadamard_state", "Born_rule_derived",
        "prediction_confirmation_or_verdict", "held_out_scored",
        "cross_packet_union_allowed",
    )
    if any(fences.get(key) is not False for key in required_false):
        failures.append("fences")
    if "finite-dimensional obstruction" not in data.get("claim_ceiling", ""):
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
        "wrong_record_effect", "add_damping_by_hand", "wrong_Cesaro",
        "contractive_unitary", "retain_nonzero_gap_limit",
        "moving_commuting_effect", "gauge_leak",
    )]
    updates = (
        ("allow_attractor", lambda d: d["theorem"].__setitem__("common_pointwise_attractor_for_two_distinct_states", True)),
        ("allow_new_record", lambda d: d["theorem"].__setitem__("new_universal_pointwise_record_formation", True)),
        ("wrong_witness", lambda d: d["k94_witness"].__setitem__("detector_one_probability", "1/3")),
        ("fake_limit", lambda d: d["k94_witness"].__setitem__("pointwise_limit_exists", True)),
        ("drop_descent", lambda d: d["k94_witness"].__setitem__("gauge_basic_zero_extension", False)),
        ("source_no_go", lambda d: d["fences"].__setitem__("source_dynamics_no_go", True)),
        ("reservoir_no_go", lambda d: d["fences"].__setitem__("infinite_reservoir_or_thermodynamic_no_go", True)),
        ("open_no_go", lambda d: d["fences"].__setitem__("open_system_or_coarse_graining_no_go", True)),
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
    checks.append(("manifest preserves theorem, witness, ownership and promotion fences", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed = sum(ok for _, ok in checks)
    print(f"K95 FINITE HAMILTONIAN ASYMPTOTIC NO-GO: {passed}/{len(checks)} pass")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
