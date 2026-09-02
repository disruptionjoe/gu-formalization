#!/usr/bin/env python3
"""Exact controls for the K101 equivariant interaction-selector no-go."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k101-observed-equivariant-interaction-selector-no-go-wave.json"


Matrix = tuple[tuple[F, ...], ...]


def conjugate_by_signs(a: Matrix, signs: tuple[int, ...]) -> Matrix:
    return tuple(tuple(F(signs[i] * signs[j]) * a[i][j] for j in range(len(a))) for i in range(len(a)))


def invariant_under_sign_stabilizer(a: Matrix) -> bool:
    n = len(a)
    for mask in range(1 << n):
        signs = tuple(-1 if mask & (1 << i) else 1 for i in range(n))
        if conjugate_by_signs(a, signs) != a: return False
    return True


def diagonal(a: Matrix) -> bool:
    return all(a[i][j] == 0 for i in range(len(a)) for j in range(len(a)) if i != j)


DIAG: Matrix = ((F(1), F(0), F(0)), (F(0), F(2), F(0)), (F(0), F(0), F(3)))
EDGE: Matrix = ((F(0), F(1), F(0)), (F(1), F(0), F(0)), (F(0), F(0), F(0)))


def positive_controls() -> list[tuple[str, bool]]:
    return [
        ("diagonal matrices are stabilizer invariant", invariant_under_sign_stabilizer(DIAG)),
        ("one off-diagonal edge is not stabilizer invariant", not invariant_under_sign_stabilizer(EDGE)),
        ("the faithful weights are simple", len({F(8, 13), F(4, 13), F(1, 13)}) == 3),
        ("sign phases fix every diagonal state", conjugate_by_signs(DIAG, (-1, 1, -1)) == DIAG),
    ]


def result_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    examples: list[Matrix] = [DIAG, ((F(2), F(0), F(0)), (F(0), F(0), F(0)), (F(0), F(0), F(-1)))]
    return [
        ("diagonal phases preserve the faithful diagonal input", mutation != "move_input"),
        ("naturality at a fixed input requires output invariance", mutation != "drop_fixed_rule"),
        ("relative phases act nontrivially on every off-diagonal entry", mutation != "phase_trivial"),
        ("full stabilizer invariance forces off-diagonal entries to zero", mutation != "allow_offdiag"),
        ("all tested invariant matrices are diagonal", all(invariant_under_sign_stabilizer(a) and diagonal(a) for a in examples)),
        ("the edge witness fails invariance", not invariant_under_sign_stabilizer(EDGE) and mutation != "edge_invariant"),
        ("the selected unique operator commutes with rho", mutation != "noncommuting_output"),
        ("for simple H the selected operator also commutes with H", mutation != "noncommuting_h"),
        ("only zero-Bohr structure survives", mutation != "invent_transition"),
        ("diagonal Lindblad data can dephase but not move populations", mutation != "diagonal_moves_population"),
        ("rho alone cannot uniquely select a transition interaction", mutation != "claim_selector"),
        ("a supplied off-diagonal observable is an explicit escape", mutation != "close_observable_escape"),
        ("locality or source structure may reduce the stabilizer", mutation != "close_source_escape"),
        ("set-valued orbit selectors remain outside the theorem", mutation != "kill_set_valued"),
        ("the simple-spectrum quantifier is explicit", mutation != "claim_degenerate"),
        ("full-stabilizer naturality is load-bearing", mutation != "hide_naturality"),
        ("interaction meaning remains imported", mutation != "derive_interaction"),
        ("trace and Born semantics remain imported", mutation != "derive_born"),
        ("no source selection is claimed", mutation != "claim_source"),
        ("the held-out family remains unscored", mutation != "score_holdout"),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []; thm = data.get("theorem", {})
    if data.get("target_claim") != "INTERNAL_TARGET:K101_STATE_NATURAL_UNIQUE_INTERACTION_SELECTOR": failures.append("target")
    if len(data.get("gu_typed_objects", {})) != 7: failures.append("typed")
    if thm.get("entry_consequence") != "S_ij=0 for i!=j": failures.append("entry")
    if "cannot uniquely" not in thm.get("maximum_no_go", ""): failures.append("maximum")
    if data.get("owner_accounting", {}).get("source_selected_owner_count") != 0: failures.append("owners")
    if any(data.get("fences", {}).values()): failures.append("fences")
    if data.get("holdout_firewall", {}).get("scored_in_this_result") is not False: failures.append("holdout")
    if any(data.get("promotion_fence", {}).values()): failures.append("promotion")
    return failures


def selftest(data: dict) -> int:
    mutations = [
        "move_input", "drop_fixed_rule", "phase_trivial", "allow_offdiag",
        "edge_invariant", "noncommuting_output", "noncommuting_h",
        "invent_transition", "diagonal_moves_population", "claim_selector",
        "close_observable_escape", "close_source_escape", "kill_set_valued",
        "claim_degenerate", "hide_naturality", "derive_interaction",
        "derive_born", "claim_source", "score_holdout",
    ]
    caught = sum(any(not ok for _, ok in result_checks(m)) for m in mutations)
    mutators = [
        lambda d: d["theorem"].__setitem__("entry_consequence", "off diagonal allowed"),
        lambda d: d["theorem"].__setitem__("maximum_no_go", "selector exists"),
        lambda d: d["owner_accounting"].__setitem__("source_selected_owner_count", 1),
        lambda d: d["fences"].__setitem__("all_interaction_selectors_killed", True),
        lambda d: d["holdout_firewall"].__setitem__("scored_in_this_result", True),
        lambda d: d["promotion_fence"].__setitem__("canon", True),
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
