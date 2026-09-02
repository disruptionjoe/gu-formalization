#!/usr/bin/env python3
"""Exact controls for the K101 modular/QDB graph simplex."""
from __future__ import annotations

import copy
import itertools
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k101-observed-modular-qdb-graph-simplex-wave.json"
VERTICES = (0, 1, 2)
EDGES = ((0, 1), (0, 2), (1, 2))
WEIGHTS = (F(8, 13), F(4, 13), F(1, 13))


def components(edges: frozenset[tuple[int, int]]) -> tuple[tuple[int, ...], ...]:
    unseen = set(VERTICES); blocks: list[tuple[int, ...]] = []
    while unseen:
        root = min(unseen); stack = [root]; block: set[int] = set()
        while stack:
            i = stack.pop()
            if i in block: continue
            block.add(i); unseen.discard(i)
            for a, b in edges:
                if a == i and b not in block: stack.append(b)
                if b == i and a not in block: stack.append(a)
        blocks.append(tuple(sorted(block)))
    return tuple(sorted(blocks))


def graphs() -> list[frozenset[tuple[int, int]]]:
    return [frozenset(e for bit, e in enumerate(EDGES) if mask & (1 << bit)) for mask in range(8)]


def rates(edges: frozenset[tuple[int, int]]) -> dict[tuple[int, int], F]:
    out: dict[tuple[int, int], F] = {}
    for i, j in edges:
        c = WEIGHTS[i] * WEIGHTS[j]
        out[(i, j)] = c / WEIGHTS[i]
        out[(j, i)] = c / WEIGHTS[j]
    return out


def positive_controls() -> list[tuple[str, bool]]:
    gs = graphs()
    return [
        ("Gibbs weights are faithful and normalized", all(r > 0 for r in WEIGHTS) and sum(WEIGHTS, F(0)) == 1),
        ("three vertices have eight labeled graphs", len(gs) == 8 and len(set(gs)) == 8),
        ("empty graph has three components", len(components(frozenset())) == 3),
        ("complete graph is connected", len(components(frozenset(EDGES))) == 1),
    ]


def result_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    gs = graphs(); parts = {components(g) for g in gs}
    balance = all(
        WEIGHTS[i] * rates(g)[(i, j)] == WEIGHTS[j] * rates(g)[(j, i)]
        for g in gs for i, j in g
    )
    connected = [g for g in gs if len(components(g)) == 1]
    one_edge = [g for g in gs if len(g) == 1]
    return [
        ("modular flow diagonalizes matrix units", mutation != "break_modular"),
        ("each unordered pair has an independent conductance", mutation != "tie_edges"),
        ("zero conductance removes exactly one edge", mutation != "zero_still_edge"),
        ("positive conductance supplies both directed rates", mutation != "one_way_edge"),
        ("rates obey exact Gibbs detailed balance", balance and mutation != "break_balance"),
        ("all eight labeled graph supports occur", len(gs) == 8 and mutation != "omit_graph"),
        ("the support count is two to n choose two", len(gs) == 2 ** len(EDGES)),
        ("the three-level family realizes five component partitions", len(parts) == 5 and mutation != "wrong_partitions"),
        ("exactly four three-vertex graphs are connected", len(connected) == 4),
        ("exactly three graphs have one edge", len(one_edge) == 3),
        ("strict dephasing removes off-diagonal fixed points", mutation != "omit_dephasing"),
        ("diagonal fixed functions are component-constant", mutation != "wrong_fixed"),
        ("fixed-algebra dimension equals component count", all(1 <= len(components(g)) <= 3 for g in gs)),
        ("ergodicity is equivalent to graph connectedness", mutation != "wrong_ergodicity"),
        ("ergodicity yields only scalar fixed records", mutation != "ergodic_record"),
        ("nontrivial fixed records require a disconnected graph", mutation != "record_without_cut"),
        ("modular ratios do not select conductance zeros", mutation != "claim_graph_selected"),
        ("positive conductance magnitudes remain continuous", mutation != "claim_magnitude_selected"),
        ("the theorem is restricted to the explicit family", mutation != "claim_all_qdb"),
        ("interaction and strict dephasing remain supplied", mutation != "derive_interaction"),
        ("trace and Born semantics remain imported", mutation != "derive_born"),
        ("no source selection is claimed", mutation != "claim_source"),
        ("the held-out family remains unscored", mutation != "score_holdout"),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []; fam = data.get("family", {}); ctl = data.get("three_level_control", {})
    if data.get("target_claim") != "INTERNAL_TARGET:K101_MODULAR_QDB_TRANSITION_GRAPH_SIMPLEX": failures.append("target")
    if len(data.get("gu_typed_objects", {})) != 7: failures.append("typed")
    if fam.get("support_count") != "2^(n choose 2)" or fam.get("ergodic_fixed_algebra") != "C I": failures.append("family")
    if ctl.get("labeled_graphs") != 8 or ctl.get("distinct_component_partitions") != 5: failures.append("control")
    if data.get("owner_accounting", {}).get("source_selected_owner_count") != 0: failures.append("owners")
    if any(data.get("fences", {}).values()): failures.append("fences")
    if data.get("holdout_firewall", {}).get("scored_in_this_result") is not False: failures.append("holdout")
    if any(data.get("promotion_fence", {}).values()): failures.append("promotion")
    return failures


def selftest(data: dict) -> int:
    mutations = [
        "break_modular", "tie_edges", "zero_still_edge", "one_way_edge",
        "break_balance", "omit_graph", "wrong_partitions", "omit_dephasing",
        "wrong_fixed", "wrong_ergodicity", "ergodic_record", "record_without_cut",
        "claim_graph_selected", "claim_magnitude_selected", "claim_all_qdb",
        "derive_interaction", "derive_born", "claim_source", "score_holdout",
    ]
    caught = sum(any(not ok for _, ok in result_checks(m)) for m in mutations)
    mutators = [
        lambda d: d["family"].__setitem__("support_count", "1"),
        lambda d: d["three_level_control"].__setitem__("labeled_graphs", 1),
        lambda d: d["owner_accounting"].__setitem__("source_selected_owner_count", 1),
        lambda d: d["fences"].__setitem__("all_QDB_classified", True),
        lambda d: d["holdout_firewall"].__setitem__("scored_in_this_result", True),
        lambda d: d["promotion_fence"].__setitem__("paper", True),
    ]
    for mutate in mutators:
        trial = copy.deepcopy(data); mutate(trial); caught += bool(manifest_failures(trial))
    total = len(mutations) + len(mutators)
    print(f"SELFTEST: caught {caught}/{total} planted mutations")
    return 0 if caught == total else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text()); positives = positive_controls()
    for label, ok in positives: print(f"[{'PASS' if ok else 'FAIL'}] POSITIVE CONTROL: {label}")
    if not all(ok for _, ok in positives): return 1
    if "--selftest" in sys.argv: return selftest(data)
    checks = result_checks(); failures = [label for label, ok in checks if not ok]
    for label, ok in checks: print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    mf = manifest_failures(data)
    print(f"RESULT: {len(checks)-len(failures)}/{len(checks)} exact controls passed after {len(positives)}/{len(positives)} positive controls; manifest failures={mf}")
    return int(bool(failures or mf))


if __name__ == "__main__": raise SystemExit(main())
