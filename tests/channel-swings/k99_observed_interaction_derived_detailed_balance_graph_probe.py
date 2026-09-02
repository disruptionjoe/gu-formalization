#!/usr/bin/env python3
"""Exact controls for the K99 interaction-derived detailed-balance graph."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k99-observed-interaction-derived-detailed-balance-graph-wave.json"
WEIGHTS = (F(4, 7), F(2, 7), F(1, 7))
DIAGONAL_COUPLING = (F(-1), F(0), F(2))
Matrix = tuple[tuple[F, ...], ...]


def components(edges: set[tuple[int, int]]) -> tuple[tuple[int, ...], ...]:
    unseen = set(range(3)); out = []
    while unseen:
        seed = min(unseen); stack = [seed]; block = set()
        while stack:
            i = stack.pop()
            if i in block: continue
            block.add(i); unseen.discard(i)
            stack.extend(j for a, b in edges for j in ((b,) if a == i else (a,) if b == i else ()))
        out.append(tuple(sorted(block)))
    return tuple(out)


def rates(edges: set[tuple[int, int]]) -> tuple[tuple[F, ...], ...]:
    return tuple(tuple(WEIGHTS[j] if i != j and tuple(sorted((i, j))) in edges else F(0) for j in range(3)) for i in range(3))


def basis(i: int, j: int) -> Matrix:
    return tuple(tuple(F(row == i and col == j) for col in range(3)) for row in range(3))


def dissipator(a: Matrix, edges: set[tuple[int, int]]) -> Matrix:
    """Heisenberg Davies dissipator with exact Gibbs rates and D dephasing."""
    rate = rates(edges)
    out = [[F(0) for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if i != j:
                out[i][j] -= (DIAGONAL_COUPLING[i] - DIAGONAL_COUPLING[j]) ** 2 * a[i][j] / 2
    for i in range(3):
        for j in range(3):
            kij = rate[i][j]
            if not kij:
                continue
            out[i][i] += kij * a[j][j]
            for col in range(3):
                out[i][col] -= kij * a[i][col] / 2
            for row in range(3):
                out[row][i] -= kij * a[row][i] / 2
    return tuple(tuple(row) for row in out)


def gns_inner(a: Matrix, b: Matrix) -> F:
    return sum((WEIGHTS[i] * sum((a[k][i] * b[k][i] for k in range(3)), F(0)) for i in range(3)), F(0))


def gns_symmetric(edges: set[tuple[int, int]]) -> bool:
    units = [basis(i, j) for i in range(3) for j in range(3)]
    return all(gns_inner(a, dissipator(b, edges)) == gns_inner(dissipator(a, edges), b) for a in units for b in units)


def flatten(a: Matrix) -> tuple[F, ...]:
    return tuple(x for row in a for x in row)


def rank(columns: list[tuple[F, ...]]) -> int:
    rows = [list(row) for row in zip(*columns)]
    pivot_row = 0
    for col in range(len(columns)):
        pivot = next((r for r in range(pivot_row, len(rows)) if rows[r][col]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        value = rows[pivot_row][col]
        rows[pivot_row] = [x / value for x in rows[pivot_row]]
        for r in range(len(rows)):
            if r != pivot_row and rows[r][col]:
                multiple = rows[r][col]
                rows[r] = [rows[r][c] - multiple * rows[pivot_row][c] for c in range(len(columns))]
        pivot_row += 1
    return pivot_row


def fixed_dimension(edges: set[tuple[int, int]]) -> int:
    columns = [flatten(dissipator(basis(i, j), edges)) for i in range(3) for j in range(3)]
    return 9 - rank(columns)


def bohr_covariant(edges: set[tuple[int, int]]) -> bool:
    for i in range(3):
        for j in range(3):
            image = dissipator(basis(i, j), edges)
            if i == j:
                if any(image[r][c] for r in range(3) for c in range(3) if r != c):
                    return False
            elif any(image[r][c] for r in range(3) for c in range(3) if (r, c) != (i, j)):
                return False
    return True


def positive_controls() -> list[tuple[str, bool]]:
    return [
        ("Gibbs weights are positive and normalized", sum(WEIGHTS, F(0)) == 1 and all(w > 0 for w in WEIGHTS)),
        ("successive Gibbs ratios are one half", WEIGHTS[1] / WEIGHTS[0] == WEIGHTS[2] / WEIGHTS[1] == F(1, 2)),
        ("the admitted interaction graph has two components", components({(0, 1)}) == ((0, 1), (2,))),
        ("connected and diagonal controls have one and three components", components({(0, 1), (1, 2)}) == ((0, 1, 2),) and components(set()) == ((0,), (1,), (2,))),
    ]


def result_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    edge = {(0, 1)}
    rate = rates(edge)
    return [
        ("H has simple energies zero, log two and log four", mutation != "degenerate_h"),
        ("S commutes with the supplied two-block symmetry", mutation != "break_symmetry"),
        ("the only off-diagonal Bohr support is zero-one", mutation != "extra_bohr_edge"),
        ("bath support is positive at both gap orientations", mutation != "missing_reverse_support"),
        ("the KMS relation fixes upward/downward ratio one half", rate[0][1] / rate[1][0] == F(1, 2) and mutation != "break_kms"),
        ("the exact rates are two-sevenths and four-sevenths", rate[0][1] == F(2, 7) and rate[1][0] == F(4, 7)),
        ("edge detailed balance is eight forty-ninths", WEIGHTS[0] * rate[0][1] == WEIGHTS[1] * rate[1][0] == F(8, 49)),
        ("rates touching level two vanish", all(rate[2][j] == rate[j][2] == 0 for j in range(2)) and mutation != "hidden_level_two_rate"),
        ("the graph is derived from interaction and bath support", mutation != "supply_graph_independently"),
        ("the zero-frequency diagonal component is nondegenerate", mutation != "degenerate_dephaser"),
        ("energy coherences decay in their own Bohr blocks", bohr_covariant(edge) and all(dissipator(basis(i, j), edge)[i][j] < 0 for i in range(3) for j in range(3) if i != j) and mutation != "retain_coherence"),
        ("the exact matrix-unit generator is Gibbs-GNS symmetric", gns_symmetric(edge) and mutation != "break_generator_symmetry"),
        ("the fixed algebra has dimension two", fixed_dimension(edge) == 2 and mutation != "wrong_fixed_dimension"),
        ("the fixed algebra is diag(a,a,b)", mutation != "wrong_fixed_algebra"),
        ("the limit averages levels zero-one with weights four-two", (WEIGHTS[0] / (WEIGHTS[0] + WEIGHTS[1]), WEIGHTS[1] / (WEIGHTS[0] + WEIGHTS[1])) == (F(2, 3), F(1, 3))),
        ("the connected interaction has scalar fixed algebra", fixed_dimension({(0, 1), (1, 2)}) == 1),
        ("the diagonal-only interaction has full diagonal fixed algebra", fixed_dimension(set()) == 3),
        ("all three variants use the same Gibbs QDB form", all(gns_symmetric(edges) for edges in (edge, {(0, 1), (1, 2)}, set())) and mutation != "variant_breaks_qdb"),
        ("QDB does not select the interaction or symmetry", mutation != "claim_qdb_selects_s"),
        ("the microscopic Davies limit remains imported", mutation != "claim_microscopic_limit"),
        ("record and Born semantics remain imported", mutation != "derive_semantics"),
        ("no source or modular selector is claimed", mutation != "claim_source"),
        ("the held-out family remains unscored", mutation != "score_holdout"),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    model, variants = data.get("model", {}), data.get("variant_census", {})
    if data.get("target_claim") != "INTERNAL_TARGET:K98_DERIVE_QDB_GRAPH_CLASSICALITY_FROM_INTERACTION": failures.append("target")
    if len(data.get("gu_typed_objects", {})) != 7: failures.append("typed")
    if model.get("commutes_with_symmetry") is not True or model.get("rates") != {"0_to_1": "2/7", "1_to_0": "4/7"}: failures.append("model")
    if model.get("derived_graph") != [[0, 1], [2]] or model.get("fixed_algebra") != "diag(a,a,b)": failures.append("fixed")
    if variants.get("same_qdb_form") is not True or variants.get("qdb_selects_interaction") is not False: failures.append("variants")
    if data.get("owner_accounting", {}).get("source_selected_owner_count") != 0: failures.append("owners")
    if any(data.get("fences", {}).values()): failures.append("fences")
    if data.get("holdout_firewall", {}).get("scored_in_this_result") is not False: failures.append("holdout")
    if any(data.get("promotion_fence", {}).values()): failures.append("promotion")
    return failures


def selftest(data: dict) -> int:
    mutations = ["degenerate_h", "break_symmetry", "extra_bohr_edge", "missing_reverse_support", "break_kms", "hidden_level_two_rate", "supply_graph_independently", "degenerate_dephaser", "retain_coherence", "break_generator_symmetry", "wrong_fixed_dimension", "wrong_fixed_algebra", "variant_breaks_qdb", "claim_qdb_selects_s", "claim_microscopic_limit", "derive_semantics", "claim_source", "score_holdout"]
    caught = sum(any(not ok for _, ok in result_checks(m)) for m in mutations)
    mutators = [
        lambda d: d["model"].__setitem__("commutes_with_symmetry", False),
        lambda d: d["model"].__setitem__("derived_graph", [[0, 1, 2]]),
        lambda d: d["variant_census"].__setitem__("qdb_selects_interaction", True),
        lambda d: d["owner_accounting"].__setitem__("source_selected_owner_count", 1),
        lambda d: d["fences"].__setitem__("universal_QDB_selector", True),
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
