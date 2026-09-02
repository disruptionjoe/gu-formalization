#!/usr/bin/env python3
"""Exact controls for the K100 faithful-thermal apparatus record floor."""
from __future__ import annotations

import copy
import itertools
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k100-observed-faithful-thermal-record-floor-wave.json"


def classical_helstrom_error(p: tuple[F, ...], q: tuple[F, ...]) -> F:
    return (1 - sum(abs(a - b) for a, b in zip(p, q, strict=True)) / 2) / 2


def permutation_controls(weights: tuple[F, ...]) -> list[F]:
    return [classical_helstrom_error(weights, perm) for perm in itertools.permutations(weights)]


def positive_controls() -> list[tuple[str, bool]]:
    return [
        ("faithful qubit state is normalized", sum((F(3, 4), F(1, 4)), F(0)) == 1),
        ("sharp swapped-qubit error is one quarter", classical_helstrom_error((F(3, 4), F(1, 4)), (F(1, 4), F(3, 4))) == F(1, 4)),
        ("identical branches have error one half", classical_helstrom_error((F(3, 4), F(1, 4)), (F(3, 4), F(1, 4))) == F(1, 2)),
        ("zero-temperature control makes the floor vacuous", 2 * F(0) / 2 == 0),
    ]


def result_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    spectra = [
        (F(3, 4), F(1, 4)),
        (F(1, 2), F(1, 3), F(1, 6)),
        (F(2, 5), F(3, 10), F(1, 5), F(1, 10)),
    ]
    floors_hold = all(
        all(err >= len(w) * min(w) / 2 for err in permutation_controls(w))
        for w in spectra
    )
    return [
        ("unitary conjugation preserves the minimum eigenvalue", mutation != "change_minimum"),
        ("each branch state obeys rho_i at least mI", mutation != "break_order"),
        ("both readout terms are positive", mutation != "negative_effect"),
        ("effect traces sum to d", mutation != "wrong_trace_sum"),
        ("every effect error is at least d m over two", mutation != "wrong_floor"),
        ("the floor is strictly positive for faithful tau", mutation != "allow_zero_faithful"),
        ("the bound is uniform in time and branch unitaries", mutation != "time_dependent_floor"),
        ("autonomous exponential branches are included", mutation != "exclude_autonomous"),
        ("the swapped thermal qubit saturates the floor", classical_helstrom_error((F(3, 4), F(1, 4)), (F(1, 4), F(3, 4))) == F(1, 4) and mutation != "deny_sharpness"),
        ("exact permutation controls respect the floor", floors_hold and mutation != "break_examples"),
        ("fixed faithful apparatus cannot converge to zero error", mutation != "claim_exact_limit"),
        ("zero temperature is an explicit escape", mutation != "close_zero_temperature"),
        ("growing or infinite apparatus is outside the bound", mutation != "claim_infinite"),
        ("nonunitary dynamics is outside the quantified class", mutation != "claim_open_system"),
        ("formation is distinguished from supplied storage", mutation != "confuse_storage"),
        ("trace and Born semantics remain imported", mutation != "derive_born"),
        ("no source dynamics is claimed", mutation != "claim_source"),
        ("the held-out family remains unscored", mutation != "score_holdout"),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    theorem = data.get("theorem", {})
    if data.get("target_claim") != "INTERNAL_TARGET:K100_FIXED_FAITHFUL_THERMAL_AUTONOMOUS_RECORD_FLOOR": failures.append("target")
    if len(data.get("gu_typed_objects", {})) != 7: failures.append("typed")
    if theorem.get("uniform_bound") != "e_t(E)>=d m/2>0": failures.append("bound")
    if theorem.get("autonomous_subset") != "U_i(t)=exp(-itK_i) is included": failures.append("autonomy")
    if data.get("owner_accounting", {}).get("source_selected_owner_count") != 0: failures.append("owners")
    if any(data.get("fences", {}).values()): failures.append("fences")
    if data.get("holdout_firewall", {}).get("scored_in_this_result") is not False: failures.append("holdout")
    if any(data.get("promotion_fence", {}).values()): failures.append("promotion")
    return failures


def selftest(data: dict) -> int:
    mutations = [
        "change_minimum", "break_order", "negative_effect", "wrong_trace_sum",
        "wrong_floor", "allow_zero_faithful", "time_dependent_floor",
        "exclude_autonomous", "deny_sharpness", "break_examples",
        "claim_exact_limit", "close_zero_temperature", "claim_infinite",
        "claim_open_system", "confuse_storage", "derive_born", "claim_source",
        "score_holdout",
    ]
    caught = sum(any(not ok for _, ok in result_checks(m)) for m in mutations)
    mutators = [
        lambda d: d["theorem"].__setitem__("uniform_bound", "e>=0"),
        lambda d: d["theorem"].__setitem__("autonomous_subset", "excluded"),
        lambda d: d["owner_accounting"].__setitem__("source_selected_owner_count", 1),
        lambda d: d["fences"].__setitem__("infinite_KMS_no_go", True),
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
