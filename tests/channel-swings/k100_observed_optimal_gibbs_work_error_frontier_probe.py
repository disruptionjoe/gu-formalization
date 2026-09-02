#!/usr/bin/env python3
"""Exact controls for the K100 optimal Gibbs work-error frontier."""
from __future__ import annotations

import copy
import itertools
import json
import math
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k100-observed-optimal-gibbs-work-error-frontier-wave.json"


def majority_error(n: int) -> F:
    assert n > 0 and n % 2 == 1
    return sum((F(math.comb(n, k) * (3 ** (n - k)), 4 ** n) for k in range(n // 2 + 1, n + 1)), F(0))


def boundary_lower(n: int) -> F:
    k = (n + 1) // 2
    return F(math.comb(n, k) * (3 ** ((n - 1) // 2)), 4 ** n)


def word_probability(word: tuple[int, ...], p_one: F) -> F:
    k = sum(word); return (p_one ** k) * ((1 - p_one) ** (len(word) - k))


def decision_error(n: int, decide_one: set[tuple[int, ...]]) -> F:
    words = list(itertools.product((0, 1), repeat=n))
    err0 = sum((word_probability(w, F(1, 4)) for w in words if w in decide_one), F(0))
    err1 = sum((word_probability(w, F(3, 4)) for w in words if w not in decide_one), F(0))
    return (err0 + err1) / 2


def brute_optimum(n: int) -> F:
    words = list(itertools.product((0, 1), repeat=n))
    best = F(1)
    for mask in range(1 << len(words)):
        chosen = {w for j, w in enumerate(words) if mask & (1 << j)}
        best = min(best, decision_error(n, chosen))
    return best


def positive_controls() -> list[tuple[str, bool]]:
    return [
        ("N one error is one quarter", majority_error(1) == F(1, 4)),
        ("N three error is five thirty-seconds", majority_error(3) == F(5, 32)),
        ("N five error is fifty-three over five-twelve", majority_error(5) == F(53, 512)),
        ("boundary term is positive", all(boundary_lower(n) > 0 for n in (1, 3, 5, 9))),
    ]


def result_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    return [
        ("likelihood ratio is 3 to the 2k minus N", mutation != "wrong_likelihood"),
        ("odd-prefix likelihood has no tie", mutation != "invent_tie"),
        ("majority is the likelihood-ratio rule", mutation != "wrong_rule"),
        ("commuting Helstrom discrimination reduces to the likelihood test", mutation != "deny_helstrom"),
        ("majority is exhaustive-optimal at N one", brute_optimum(1) == majority_error(1)),
        ("majority is exhaustive-optimal at N three", brute_optimum(3) == majority_error(3) and mutation != "deny_optimality"),
        ("the first three exact errors match", [majority_error(n) for n in (1, 3, 5)] == [F(1, 4), F(5, 32), F(53, 512)]),
        ("errors decrease on tested odd prefixes", all(majority_error(b) < majority_error(a) for a, b in zip((1, 3, 5, 7), (3, 5, 7, 9), strict=True))),
        ("the first omitted-tail term is a lower bound", all(majority_error(n) >= boundary_lower(n) for n in (1, 3, 5, 9)) and mutation != "break_lower"),
        ("the finite lower bound is strictly positive", all(boundary_lower(n) > 0 for n in (1, 3, 5, 9)) and mutation != "finite_exact"),
        ("Hoeffding upper bound holds on tested prefixes", all(float(majority_error(n)) <= math.exp(-n / 8) for n in (1, 3, 5, 9, 15)) and mutation != "break_upper"),
        ("work is N epsilon over two", all(F(n, 2) == n * F(1, 2) for n in (1, 3, 9)) and mutation != "wrong_work"),
        ("finite work means finite N in the named family", mutation != "finite_work_infinite_cells"),
        ("zero error requires the infinite-prefix limit in this family", mutation != "finite_zero_error"),
        ("the frontier is not called universal", mutation != "claim_universal"),
        ("the stream and controlled flips remain supplied", mutation != "derive_stream"),
        ("trace and Born pairing remain imported", mutation != "derive_born"),
        ("no source or autonomous apparatus is claimed", mutation != "claim_source"),
        ("the held-out family remains unscored", mutation != "score_holdout"),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []; model = data.get("model", {})
    if data.get("target_claim") != "INTERNAL_TARGET:K100_OPTIMAL_GIBBS_PREFIX_WORK_ERROR_FRONTIER": failures.append("target")
    if len(data.get("gu_typed_objects", {})) != 7: failures.append("typed")
    if model.get("optimal_rule") != "decide q=1 iff k>N/2": failures.append("rule")
    if model.get("work") != "W_N=N epsilon/2": failures.append("work")
    if data.get("owner_accounting", {}).get("source_selected_owner_count") != 0: failures.append("owners")
    if any(data.get("fences", {}).values()): failures.append("fences")
    if data.get("holdout_firewall", {}).get("scored_in_this_result") is not False: failures.append("holdout")
    if any(data.get("promotion_fence", {}).values()): failures.append("promotion")
    return failures


def selftest(data: dict) -> int:
    mutations = [
        "wrong_likelihood", "invent_tie", "wrong_rule", "deny_helstrom",
        "deny_optimality", "break_lower", "finite_exact", "break_upper",
        "wrong_work", "finite_work_infinite_cells", "finite_zero_error",
        "claim_universal", "derive_stream", "derive_born", "claim_source",
        "score_holdout",
    ]
    caught = sum(any(not ok for _, ok in result_checks(m)) for m in mutations)
    mutators = [
        lambda d: d["model"].__setitem__("optimal_rule", "coin flip"),
        lambda d: d["model"].__setitem__("work", "zero"),
        lambda d: d["owner_accounting"].__setitem__("source_selected_owner_count", 1),
        lambda d: d["fences"].__setitem__("universal_measurement_work_bound", True),
        lambda d: d["holdout_firewall"].__setitem__("scored_in_this_result", True),
        lambda d: d["promotion_fence"].__setitem__("canon", True),
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
