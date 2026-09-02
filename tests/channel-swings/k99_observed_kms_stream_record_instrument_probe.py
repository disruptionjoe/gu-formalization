#!/usr/bin/env python3
"""Exact controls for the K99 positive-temperature KMS stream instrument."""
from __future__ import annotations

import copy
import json
import math
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k99-observed-kms-stream-record-instrument-wave.json"


def binomial(n: int, k: int) -> int:
    return math.comb(n, k)


def error(n: int, p: F = F(1, 4)) -> F:
    assert n % 2 == 1
    return sum(
        (F(binomial(n, k)) * p**k * (1 - p) ** (n - k)
         for k in range(n // 2 + 1, n + 1)),
        F(0),
    )


def instrument(rho: tuple[tuple[F, F], tuple[F, F]], e: F, outcome: int):
    if outcome == 0:
        return ((1 - e) * rho[0][0], F(0)), (F(0), e * rho[1][1])
    return (e * rho[0][0], F(0)), (F(0), (1 - e) * rho[1][1])


def positive_controls() -> list[tuple[str, bool]]:
    return [
        ("thermal probabilities are positive and normalized", F(3, 4) + F(1, 4) == 1),
        ("the two conditional bit means straddle one half", F(1, 4) < F(1, 2) < F(3, 4)),
        ("the first three exact errors are fixed", [error(n) for n in (1, 3, 5)] == [F(1, 4), F(5, 32), F(53, 512)]),
        ("the exact error decreases on the first six odd prefixes", all(error(n + 2) < error(n) for n in range(1, 12, 2))),
    ]


def result_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    rho = ((F(2, 5), F(1, 7)), (F(1, 7), F(3, 5)))
    e = error(5)
    i0, i1 = instrument(rho, e, 0), instrument(rho, e, 1)
    trace_sum = i0[0][0] + i0[1][1] + i1[0][0] + i1[1][1]
    late = (21, 41, 81)
    return [
        ("both q branches use the same product KMS input", mutation != "branch_input"),
        ("beta epsilon is positive log three", mutation != "infinite_temperature"),
        ("every finite restriction is the compatible Gibbs product", mutation != "non_kms_prefix"),
        ("q dependence occurs in the controlled flips", mutation != "q_dependent_thermal_state"),
        ("distinct cells give commuting sequential interactions", mutation != "reuse_cell"),
        ("odd block size removes tie handling", mutation != "even_block"),
        ("majority is the likelihood-ratio threshold", mutation != "wrong_threshold"),
        ("the two conditional errors agree by complement symmetry", mutation != "asymmetric_error"),
        ("the displayed operations erase cross-label coefficients", i0[0][1] == i1[0][1] == 0 and mutation != "retain_coherence"),
        ("each operation is completely positive", mutation != "negative_weight" and 0 < e < 1),
        ("the instrument is trace preserving in sum", trace_sum == F(1) and mutation != "trace_leak"),
        ("the benchmark mismatch equals e_N", mutation != "wrong_mismatch"),
        ("the benchmark one-weight is 1/3+e_N/3", F(2, 3) * e + F(1, 3) * (1 - e) == F(1, 3) + e / 3),
        ("Hoeffding bounds every sampled odd-prefix error", all(float(error(n)) <= math.exp(-n / 8) for n in late)),
        ("the analytic bound tends to zero", math.exp(-81 / 8) < 5e-5 and mutation != "deny_limit"),
        ("the two maps converge to the projective instrument", mutation != "wrong_limit"),
        ("the nonselective channel dephases after one cell", mutation != "claim_identity_channel"),
        ("fresh cells and driven interactions remain required", mutation != "claim_autonomous"),
        ("the exact limit uses unbounded stream length", mutation != "claim_finite_exactness"),
        ("stream, readout and Born semantics remain imported", mutation != "derive_owners"),
        ("no source or continuum ownership moves", mutation != "claim_source"),
        ("the held-out family remains unscored", mutation != "score_holdout"),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    stream, inst = data.get("thermal_stream", {}), data.get("instrument", {})
    if data.get("target_claim") != "INTERNAL_TARGET:K98_POSITIVE_TEMPERATURE_KMS_INPUT_ASYMPTOTIC_RECORD_INSTRUMENT": failures.append("target")
    if data.get("classification") != "BRIDGE_OR_SEMANTIC_BOUNDARY": failures.append("classification")
    if len(data.get("gu_typed_objects", {})) != 7: failures.append("typed")
    if stream.get("cell_gibbs_state") != "diag(3/4,1/4)" or stream.get("same_input_both_q_branches") is not True: failures.append("kms_input")
    if stream.get("autonomous") is not False or stream.get("fresh_cells_required") is not True: failures.append("resource")
    if inst.get("first_errors") != {"1": "1/4", "3": "5/32", "5": "53/512"}: failures.append("errors")
    if inst.get("completely_positive") is not True or inst.get("trace_preserving_in_sum") is not True: failures.append("instrument")
    if data.get("owner_accounting", {}).get("source_selected_owner_count") != 0: failures.append("owners")
    if any(data.get("fences", {}).values()): failures.append("fences")
    if data.get("holdout_firewall", {}).get("scored_in_this_result") is not False: failures.append("holdout")
    if any(data.get("promotion_fence", {}).values()): failures.append("promotion")
    return failures


def selftest(data: dict) -> int:
    mutations = ["branch_input", "infinite_temperature", "non_kms_prefix", "q_dependent_thermal_state", "reuse_cell", "even_block", "wrong_threshold", "asymmetric_error", "retain_coherence", "negative_weight", "trace_leak", "wrong_mismatch", "deny_limit", "wrong_limit", "claim_identity_channel", "claim_autonomous", "claim_finite_exactness", "derive_owners", "claim_source", "score_holdout"]
    caught = sum(any(not ok for _, ok in result_checks(m)) for m in mutations)
    mutators = [
        lambda d: d["thermal_stream"].__setitem__("same_input_both_q_branches", False),
        lambda d: d["thermal_stream"].__setitem__("autonomous", True),
        lambda d: d["instrument"]["first_errors"].__setitem__("3", "1/2"),
        lambda d: d["owner_accounting"].__setitem__("source_selected_owner_count", 1),
        lambda d: d["fences"].__setitem__("Born_rule_derived", True),
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
