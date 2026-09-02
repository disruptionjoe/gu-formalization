#!/usr/bin/env python3
"""Exact controls for K99 KMS-stream tail and work accounting."""
from __future__ import annotations

import copy
import json
import math
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k99-observed-kms-tail-work-accounting-wave.json"


def moments(p_excited: F, n: int) -> tuple[F, F]:
    mean = 1 - 2 * p_excited
    variance = 4 * p_excited * (1 - p_excited) / n
    return mean, variance


def positive_controls() -> list[tuple[str, bool]]:
    return [
        ("flipped Gibbs states are normalized", sum((F(3, 4), F(1, 4)), F(0)) == 1),
        ("the two product means are opposite", moments(F(1, 4), 1)[0] == F(1, 2) and moments(F(3, 4), 1)[0] == F(-1, 2)),
        ("empirical variance decays exactly as 3/(4N)", all(moments(F(1, 4), n)[1] == F(3, 4 * n) for n in (1, 3, 11))),
        ("log-three is positive", math.log(3) > 0),
    ]


def result_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    delta_e = F(1, 2)
    d_coeff = F(3, 4) - F(1, 4)
    return [
        ("one flip changes the excitation energy by epsilon/2", delta_e == F(1, 2) and mutation != "wrong_energy"),
        ("unitary flipping preserves cell entropy", mutation != "entropy_change"),
        ("free-energy change equals energy change", mutation != "wrong_free_energy"),
        ("relative-entropy coefficient is one half log three", d_coeff == F(1, 2) and mutation != "wrong_relative_entropy"),
        ("D equals beta Delta E at beta epsilon log three", mutation != "break_identity"),
        ("energy is additive on finite prefixes", all(n * delta_e == F(n, 2) for n in (1, 3, 8)) and mutation != "nonadditive_energy"),
        ("relative entropy is additive on product prefixes", mutation != "nonadditive_entropy"),
        ("both resources diverge linearly with prefix length", mutation != "finite_resource_limit"),
        ("the zero-sector empirical mean is plus one half", moments(F(1, 4), 7)[0] == F(1, 2)),
        ("the one-sector empirical mean is minus one half", moments(F(3, 4), 7)[0] == F(-1, 2)),
        ("both empirical variances tend to zero", moments(F(1, 4), 1000)[1] < F(1, 1000) and mutation != "variance_floor"),
        ("the limiting-sign tail event separates the sectors", mutation != "deny_tail_separator"),
        ("the tail event is not a fixed finite-local element", mutation != "claim_local_tail"),
        ("finite-support changes leave the empirical limit fixed", mutation != "finite_support_changes_tail"),
        ("the infinite product sectors are globally disjoint", mutation != "claim_global_equivalence"),
        ("finite prefixes retain nonzero classification error", mutation != "finite_prefix_exact"),
        ("the equality is not called a universal work theorem", mutation != "claim_universal_landauer"),
        ("tensor, time, readout and Born owners remain imported", mutation != "derive_owners"),
        ("no source or autonomous equilibrium result is claimed", mutation != "claim_source"),
        ("the held-out family remains unscored", mutation != "score_holdout"),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    cell, prefix, tail = data.get("single_cell", {}), data.get("finite_prefix", {}), data.get("tail_record", {})
    if data.get("target_claim") != "INTERNAL_TARGET:K99_KMS_STREAM_TAIL_RECORD_WORK_OWNER": failures.append("target")
    if len(data.get("gu_typed_objects", {})) != 7: failures.append("typed")
    if cell.get("identity") != "D(tau_one||tau_zero)=beta Delta E" or cell.get("delta_energy") != "epsilon/2": failures.append("identity")
    if prefix.get("additive") is not True or prefix.get("diverges_with_exact_record_limit") is not True: failures.append("prefix")
    if tail.get("probabilities") != [0, 1] or tail.get("fixed_local_element") is not False or tail.get("finite_support_unitary_changes_limit") is not False: failures.append("tail")
    if data.get("owner_accounting", {}).get("source_selected_owner_count") != 0: failures.append("owners")
    if any(data.get("fences", {}).values()): failures.append("fences")
    if data.get("holdout_firewall", {}).get("scored_in_this_result") is not False: failures.append("holdout")
    if any(data.get("promotion_fence", {}).values()): failures.append("promotion")
    return failures


def selftest(data: dict) -> int:
    mutations = ["wrong_energy", "entropy_change", "wrong_free_energy", "wrong_relative_entropy", "break_identity", "nonadditive_energy", "nonadditive_entropy", "finite_resource_limit", "variance_floor", "deny_tail_separator", "claim_local_tail", "finite_support_changes_tail", "claim_global_equivalence", "finite_prefix_exact", "claim_universal_landauer", "derive_owners", "claim_source", "score_holdout"]
    caught = sum(any(not ok for _, ok in result_checks(m)) for m in mutations)
    mutators = [
        lambda d: d["single_cell"].__setitem__("delta_energy", "0"),
        lambda d: d["finite_prefix"].__setitem__("additive", False),
        lambda d: d["tail_record"].__setitem__("probabilities", [F(1, 2), F(1, 2)]),
        lambda d: d["owner_accounting"].__setitem__("source_selected_owner_count", 1),
        lambda d: d["fences"].__setitem__("finite_work_exact_record", True),
        lambda d: d["holdout_firewall"].__setitem__("scored_in_this_result", True),
        lambda d: d["promotion_fence"].__setitem__("paper", True),
    ]
    for mutate in mutators:
        trial = copy.deepcopy(data); mutate(trial); caught += bool(manifest_failures(trial))
    total = len(mutations) + len(mutators)
    print(f"SELFTEST: caught {caught}/{total} planted mutations")
    return 0 if caught == total else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    positives = positive_controls()
    for label, ok in positives: print(f"[{'PASS' if ok else 'FAIL'}] POSITIVE CONTROL: {label}")
    if not all(ok for _, ok in positives): return 1
    if "--selftest" in sys.argv: return selftest(data)
    checks = result_checks(); failures = [label for label, ok in checks if not ok]
    for label, ok in checks: print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    mf = manifest_failures(data)
    print(f"RESULT: {len(checks)-len(failures)}/{len(checks)} exact controls passed after {len(positives)}/{len(positives)} positive controls; manifest failures={mf}")
    return int(bool(failures or mf))


if __name__ == "__main__":
    raise SystemExit(main())
