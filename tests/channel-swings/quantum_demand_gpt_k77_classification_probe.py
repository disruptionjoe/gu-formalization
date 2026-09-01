#!/usr/bin/env python3
"""Exact hostile probe for GPT demand classification and K77 coverage."""
from __future__ import annotations

import copy
import importlib.util
import itertools
import json
import pathlib
import sys
from fractions import Fraction


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/quantum-demand-gpt-k77-classification-wave.json"
QUANTUM_PROBE = ROOT / "tests/channel-swings/quantum_anchor_reverse_scaffold_interface_probe.py"


def load_quantum_probe():
    spec = importlib.util.spec_from_file_location("quantum_anchor_probe", QUANTUM_PROBE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load quantum anchor probe")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def classical_event(state: tuple[Fraction, Fraction], effect: tuple[Fraction, Fraction]) -> Fraction:
    return sum((p * e for p, e in zip(state, effect)), Fraction(0))


def apply_map(matrix: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
              state: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return tuple(sum((row[j] * state[j] for j in range(2)), Fraction(0)) for row in matrix)  # type: ignore[return-value]


def deterministic_local_chsh_bound() -> int:
    values = []
    for a0, a1, b0, b1 in itertools.product((-1, 1), repeat=4):
        values.append(a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1)
    return max(abs(value) for value in values)


def pr_probability(a: int, b: int, x: int, y: int, mutation: str | None = None) -> Fraction:
    if mutation == "signal" and x == 1:
        return Fraction(1, 2) if (a == 0 and b in (0, 1)) else Fraction(0)
    relation = (a ^ b) == (x & y)
    if mutation == "localize":
        relation = (a ^ b) == 0
    value = Fraction(1, 2) if relation else Fraction(0)
    if mutation == "negative" and (a, b, x, y) == (0, 0, 0, 0):
        return Fraction(-1, 2)
    return value


def pr_context_total(x: int, y: int, mutation: str | None = None) -> Fraction:
    return sum((pr_probability(a, b, x, y, mutation) for a, b in itertools.product((0, 1), repeat=2)), Fraction(0))


def pr_marginal_alice(a: int, x: int, y: int, mutation: str | None = None) -> Fraction:
    return sum((pr_probability(a, b, x, y, mutation) for b in (0, 1)), Fraction(0))


def pr_marginal_bob(b: int, x: int, y: int, mutation: str | None = None) -> Fraction:
    return sum((pr_probability(a, b, x, y, mutation) for a in (0, 1)), Fraction(0))


def pr_correlator(x: int, y: int, mutation: str | None = None) -> Fraction:
    return sum((Fraction((-1) ** (a ^ b)) * pr_probability(a, b, x, y, mutation)
                for a, b in itertools.product((0, 1), repeat=2)), Fraction(0))


def pr_chsh(mutation: str | None = None) -> Fraction:
    return pr_correlator(0, 0, mutation) + pr_correlator(0, 1, mutation) + pr_correlator(1, 0, mutation) - pr_correlator(1, 1, mutation)


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    quantum = load_quantum_probe()
    state = (Fraction(1, 3), Fraction(2, 3))
    unit = (Fraction(1), Fraction(1))
    outcome0 = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(0)))
    outcome1 = ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(1)))
    after0 = apply_map(outcome0, state)
    after1 = apply_map(outcome1, state)

    checks: list[tuple[str, bool]] = []
    checks.append(("classical simplex state is normalized", sum(state) == 1))
    checks.append(("classical order unit is deterministic", classical_event(state, unit) == 1))
    checks.append(("classical effect interval is nonnegative", classical_event(state, (Fraction(1), Fraction(0))) == Fraction(1, 3)))
    checks.append(("classical instrument outcomes sum to normalization", sum(after0) + sum(after1) == 1))
    checks.append(("deterministic local CHSH ceiling is exact", deterministic_local_chsh_bound() == 2))

    probs = [pr_probability(a, b, x, y, mutation) for a, b, x, y in itertools.product((0, 1), repeat=4)]
    checks.append(("PR probabilities are nonnegative", all(value >= 0 for value in probs)))
    checks.append(("PR contexts are normalized", all(pr_context_total(x, y, mutation) == 1 for x, y in itertools.product((0, 1), repeat=2))))
    checks.append(("PR Alice marginals are independent of Bob context",
                   all(pr_marginal_alice(a, x, 0, mutation) == pr_marginal_alice(a, x, 1, mutation)
                       for a, x in itertools.product((0, 1), repeat=2))))
    checks.append(("PR Bob marginals are independent of Alice context",
                   all(pr_marginal_bob(b, 0, y, mutation) == pr_marginal_bob(b, 1, y, mutation)
                       for b, y in itertools.product((0, 1), repeat=2))))
    checks.append(("PR CHSH is exact four", pr_chsh(mutation) == 4))

    quantum_checks = quantum.model_checks()
    checks.append(("prior exact quantum witness remains green", all(passed for _, passed in quantum_checks)))
    quantum_chsh = quantum.quantum_chsh(quantum.BELL)
    checks.append(("quantum CHSH square is exact eight", quantum.q2_square(quantum_chsh) == quantum.Q2(Fraction(8))))
    checks.append(("no-signalling GPT set is strictly broader than quantum witness", pr_chsh(mutation) ** 2 > 8))
    return checks


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    if data.get("direction") != "observed_to_native":
        failures.append("direction")
    core_ids = {row.get("id") for row in data.get("carrier_neutral_gpt_core", [])}
    if core_ids != {f"GPT-C{i}" for i in range(1, 7)}:
        failures.append("gpt_core")
    r1 = data.get("qd_r1_classification", [])
    if {row.get("id") for row in r1} != {f"QD-R1-{i}" for i in range(1, 6)}:
        failures.append("r1_denominator")
    discriminators = {row.get("id") for row in data.get("exact_model_discriminators", [])}
    if discriminators != {"GPT-D1-CLASSICAL-SIMPLEX", "GPT-D2-QUANTUM-WITNESS", "GPT-D3-PR-BOX"}:
        failures.append("discriminator_triangle")
    candidates = data.get("candidate_local_k77_coverage", [])
    if {row.get("id") for row in candidates} != {"K77-I1B-MIXED-ORDER", "K77-OBSERVED-INCOMING-PROJECTOR"}:
        failures.append("k77_population")
    for candidate in candidates:
        coverage = candidate.get("coverage", [])
        if {row.get("requirement") for row in coverage} != {f"QD-R1-{i}" for i in range(1, 6)}:
            failures.append(f"coverage_denominator:{candidate.get('id')}")
        if any(row.get("state") not in {"partial", "absent", "wrong_object"} for row in coverage):
            failures.append(f"coverage_promotion:{candidate.get('id')}")
        if not all(row.get("owned") and row.get("missing") for row in coverage):
            failures.append(f"coverage_reason:{candidate.get('id')}")
    excluded = {row.get("id") for row in data.get("excluded_packets", [])}
    if "K95-B5-STRICT-RS" not in excluded or "W154-W229-CONDITIONAL-COMPOSITE" not in excluded:
        failures.append("excluded_population")
    composition = data.get("composability", {})
    if composition.get("cross_packet_union_allowed") is not False or composition.get("candidate_selected") is not False:
        failures.append("composition_or_selection")
    if composition.get("current_root_candidate_set") != []:
        failures.append("root_candidate_set")
    result = data.get("result", {})
    if result.get("complete_k77_requirement_rows") != 0 or result.get("quantum_selection") != "not_derived":
        failures.append("result_ceiling")
    holdout = data.get("holdout_firewall", {})
    if holdout.get("status") != "reserved_unscored" or holdout.get("scored_in_this_result") is not False:
        failures.append("holdout")
    if "No GU-native" not in data.get("claim_ceiling", ""):
        failures.append("claim_ceiling")
    for candidate in candidates:
        ref = candidate.get("source_ref", "").split("#", 1)[0]
        if not ref or not (ROOT / ref).is_file():
            failures.append(f"evidence:{candidate.get('id')}")
    return failures


def selftest(data: dict) -> int:
    mutations = []
    edits = (
        ("direction", lambda d: d.__setitem__("direction", "native_to_observed")),
        ("remove_r1", lambda d: d.__setitem__("qd_r1_classification", d["qd_r1_classification"][:-1])),
        ("select_action", lambda d: d["composability"].__setitem__("candidate_selected", True)),
        ("cross_union", lambda d: d["composability"].__setitem__("cross_packet_union_allowed", True)),
        ("promote_row", lambda d: d["candidate_local_k77_coverage"][0]["coverage"][0].__setitem__("state", "complete")),
        ("include_k95", lambda d: d["candidate_local_k77_coverage"].append({"id": "K95-B5-STRICT-RS", "coverage": []})),
        ("score_holdout", lambda d: d["holdout_firewall"].__setitem__("scored_in_this_result", True)),
        ("derive_quantum", lambda d: d["result"].__setitem__("quantum_selection", "derived")),
        ("inflate_ceiling", lambda d: d.__setitem__("claim_ceiling", "GU quantum state derived")),
    )
    for name, edit in edits:
        mutated = copy.deepcopy(data)
        edit(mutated)
        mutations.append((name, bool(manifest_failures(mutated))))
    for name in ("signal", "localize", "negative"):
        mutations.append((name, any(not passed for _, passed in model_checks(name))))
    for name, caught in mutations:
        print(f"[{'PASS' if caught else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(caught for _, caught in mutations)}/{len(mutations)} caught")
    return 0 if all(caught for _, caught in mutations) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if "--selftest" in sys.argv:
        return selftest(data)
    checks = model_checks()
    failures = manifest_failures(data)
    checks.append(("manifest core, discriminator, coverage, exclusion and ceiling custody", not failures))
    failed = 0
    for label, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failed += int(not passed)
    print(f"GPT K77 CLASSIFICATION: {len(checks) - failed}/{len(checks)} pass")
    if failures:
        print("manifest failures:", ", ".join(failures))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
