#!/usr/bin/env python3
"""Exact finite controls for the K105 generated-selector closure theorem."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k107-k105-generated-selector-closure-wave.json"


def fixture(mutation: str | None = None):
    # Four positive blind axes, two negative blind axes, one active axis.
    K = sp.diag(1, 1, 1, 1, -1, -1, 1)
    rotation = sp.eye(7)
    rotation[:2, :2] = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)],
                                  [sp.Rational(4, 5), sp.Rational(3, 5)]])
    swap = sp.eye(7)
    swap[0, 0] = swap[1, 1] = 0
    swap[0, 1] = swap[1, 0] = 1

    # Every owned generator is scalar on each blind block. The active axis may
    # carry an independent coefficient without breaking blind symmetry.
    generators = [
        K,
        sp.diag(0, 0, 0, 0, 0, 0, 3),
        sp.diag(2, 2, 2, 2, 5, 5, 7),
        sp.diag(sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 5), sp.Rational(1, 5), sp.Rational(1, 7)),
    ]
    if mutation == "break_generator":
        generators[2] = sp.diag(2, 3, 2, 2, 5, 5, 7)

    words = [sp.eye(7)]
    frontier = [sp.eye(7)]
    for _ in range(5):
        frontier = [word * generator for word in frontier for generator in generators]
        words.extend(frontier)

    polynomial = generators[2] ** 3 - 2 * generators[2] + sp.eye(7)
    inverse = generators[2].inv()
    projector_active = sp.diag(0, 0, 0, 0, 0, 0, 1)
    planted = sp.diag(1, 2, 3, 4, 5, 6, 7)
    return K, rotation, swap, words, polynomial, inverse, projector_active, planted


def commutes(a: sp.MatrixBase, b: sp.MatrixBase) -> bool:
    return a * b == b * a


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    K, rotation, swap, words, polynomial, inverse, projector, planted = fixture(mutation)
    return [
        ("the surrogate lowerer has inertia 5/2/0", tuple(K.diagonal()).count(1) == 5 and tuple(K.diagonal()).count(-1) == 2),
        ("the exact 3/4/5 rotation is orthogonal", rotation.T * rotation == sp.eye(7)),
        ("the rotation is K-orthogonal", rotation.T * K * rotation == K),
        ("the swap is K-orthogonal", swap.T * K * swap == K),
        ("every generated word through degree five commutes with the rotation", all(commutes(word, rotation) for word in words)),
        ("every generated word through degree five commutes with the swap", all(commutes(word, swap) for word in words)),
        ("the polynomial representative commutes", commutes(polynomial, rotation) and commutes(polynomial, swap)),
        ("the inverse representative commutes", commutes(inverse, rotation) and commutes(inverse, swap)),
        ("the isolated active spectral projector commutes", commutes(projector, rotation) and commutes(projector, swap)),
        ("the planted full operator breaks the positive blind rotation", not commutes(planted, rotation)),
        ("the planted lowest line is K-positive and simple", planted[0, 0] == 1 and planted[1, 1] == 2 and K[0, 0] == 1),
    ]


def failures(data: dict) -> list[str]:
    out: list[str] = []
    symmetry = data.get("frozen_symmetry", {})
    generated = data.get("generated_data_class", {})
    theorem = data.get("theorem", {})
    control = data.get("finite_control", {})
    result = data.get("result", {})
    if symmetry.get("group_subgroup") != "O(256)_times_O(183)" or symmetry.get("positive_blind_dimension") != 256:
        out.append("symmetry")
    if generated.get("every_generator_commutes_with_blind_group") is not True or generated.get("closure_preserves_commutation") is not True or generated.get("every_generated_spectral_projector_is_blind_group_invariant") is not True:
        out.append("closure")
    if theorem.get("generated_selector_can_have_natural_rank_one_positive_projector_in_blind_sector") is not False or theorem.get("new_independently_owned_symmetry_breaking_datum_required") is not True:
        out.append("theorem")
    if control.get("generated_word_degree_tested") != 5 or control.get("generated_words_commute") is not True or control.get("planted_full_operator_source_owned") is not False:
        out.append("control")
    if result.get("repackaging_owned_action_domain_Green_data_can_select_K91_line") is not False or result.get("all_possible_actions_or_boundary_operators_obstructed") is not False or result.get("physical_state_or_Born_credit") is not False or result.get("canon_verdict_change") != "none":
        out.append("result")
    ceiling = data.get("claim_ceiling", "")
    if "generated solely" not in ceiling or "No obstruction" not in ceiling:
        out.append("ceiling")
    return out


def selftest(data: dict) -> int:
    if failures(data) or not all(ok for _, ok in exact_checks()):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [("break_generator", any(not ok for _, ok in exact_checks("break_generator")))]
    updates = (
        ("shrink_group", lambda d: d["frozen_symmetry"].__setitem__("group_subgroup", "Z2")),
        ("erase_commutation", lambda d: d["generated_data_class"].__setitem__("every_generator_commutes_with_blind_group", False)),
        ("erase_closure", lambda d: d["generated_data_class"].__setitem__("closure_preserves_commutation", False)),
        ("invent_generated_line", lambda d: d["theorem"].__setitem__("generated_selector_can_have_natural_rank_one_positive_projector_in_blind_sector", True)),
        ("erase_new_datum", lambda d: d["theorem"].__setitem__("new_independently_owned_symmetry_breaking_datum_required", False)),
        ("invent_source_control", lambda d: d["finite_control"].__setitem__("planted_full_operator_source_owned", True)),
        ("invent_repackaging", lambda d: d["result"].__setitem__("repackaging_owned_action_domain_Green_data_can_select_K91_line", True)),
        ("universalize", lambda d: d["result"].__setitem__("all_possible_actions_or_boundary_operators_obstructed", True)),
        ("invent_physics", lambda d: d["result"].__setitem__("physical_state_or_Born_credit", True)),
        ("promote_canon", lambda d: d["result"].__setitem__("canon_verdict_change", "changed")),
        ("erase_scope", lambda d: d.__setitem__("claim_ceiling", "No selector exists.")),
    )
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught.append((name, bool(failures(mutant))))
    for name, ok in caught:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(ok for _, ok in caught)}/{len(caught)} caught")
    return 0 if all(ok for _, ok in caught) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    if "--selftest" in sys.argv:
        return selftest(data)
    checks = exact_checks()
    checks.append(("manifest preserves closure, contrary route and claim ceiling", not failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"K107 K105 GENERATED SELECTOR CLOSURE: {sum(ok for _, ok in checks)}/{len(checks)} pass")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
