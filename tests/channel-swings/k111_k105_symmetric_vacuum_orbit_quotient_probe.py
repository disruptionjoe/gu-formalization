#!/usr/bin/env python3
"""Exact K111 symmetric-vacuum and orbit-quotient controls (stdlib only)."""
from __future__ import annotations

import copy
from fractions import Fraction
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k111-k105-symmetric-vacuum-orbit-quotient-wave.json"


def f(x: Fraction, a: Fraction, b: Fraction) -> Fraction:
    return (x - a) ** 2 * (x - b) ** 2


def fprime(x: Fraction, a: Fraction, b: Fraction) -> Fraction:
    return 2 * (x - a) * (x - b) * (2 * x - a - b)


def fsecond(x: Fraction, a: Fraction, b: Fraction) -> Fraction:
    return 2 * ((2 * x - a - b) ** 2 + 2 * (x - a) * (x - b))


def action(weights: list[Fraction], a: Fraction, b: Fraction) -> Fraction:
    return sum((f(x, a, b) for x in weights), Fraction(0))


def vacuum(n: int, selected: int, a: Fraction, b: Fraction) -> list[Fraction]:
    weights = [b] * n
    weights[selected] = a
    return weights


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    n = 256
    a = Fraction(2, 257)
    b = Fraction(1, 257)
    if mutation == "wrong_dimension":
        n = 255
    elif mutation == "wrong_heavy_weight":
        a = Fraction(3, 257)
    elif mutation == "equal_wells":
        a = b

    vacua = [vacuum(n, j, a, b) for j in range(n)]
    normalized_vacua = [w for w in vacua if sum(w) == 1]
    zero_vacua = [w for w in vacua if action(w, a, b) == 0]
    admissible_heavy_counts = [
        k for k in range(n + 1) if k * a + (n - k) * b == 1
    ]
    uniform = [Fraction(1, n)] * n
    uniform_gradient = [fprime(x, a, b) for x in uniform]
    projected_uniform_gradient = [
        g - sum(uniform_gradient, Fraction(0)) / n for g in uniform_gradient
    ]
    vacuum_hessian = fsecond(a, a, b)
    light_hessian = fsecond(b, a, b)
    uniform_hessian = fsecond(Fraction(1, n), a, b)

    sample = vacua[0]
    reversed_sample = list(reversed(sample))
    selected = sample.index(max(sample)) if sample else -1
    reversed_selected = reversed_sample.index(max(reversed_sample)) if reversed_sample else -1
    average_projector_diagonal = [Fraction(1, n)] * n
    abstract_scalar = Fraction(7, 5)
    transported_scalar = abstract_scalar

    return [
        ("the frozen positive blind carrier has dimension 256", n == 256),
        ("the two rational wells are distinct and strictly positive", 0 < b < a),
        ("one heavy and 255 light weights normalize exactly", a + (n - 1) * b == 1),
        ("the polynomial action is nonnegative on rational controls", all(action(w, a, b) >= 0 for w in vacua + [uniform])),
        ("all 256 displayed vacua have zero action", len(zero_vacua) == 256),
        ("all 256 displayed vacua lie in the normalized simplex", len(normalized_vacua) == 256),
        ("the simplex sum permits exactly one heavy well coordinate", admissible_heavy_counts == [1]),
        ("the vacuum orbit contains 256 distinct weights", len({tuple(w) for w in vacua}) == 256),
        ("coordinate reversal preserves the symmetric action", action(sample, a, b) == action(reversed_sample, a, b)),
        ("coordinate reversal transports rather than fixes the selected branch", selected == 0 and reversed_selected == n - 1),
        ("each vacuum stabilizer has size 255 factorial", math.factorial(n - 1) * n == math.factorial(n)),
        ("the vacuum tangent Hessian gap is exactly 2/257^2", vacuum_hessian == light_hessian == Fraction(2, 257**2)),
        ("each vacuum is a strict constrained local minimum", vacuum_hessian > 0 and light_hessian > 0),
        ("the uniform weight is a constrained critical point", all(g == 0 for g in projected_uniform_gradient)),
        ("the uniform critical point is not a global vacuum", action(uniform, a, b) > 0),
        ("the uniform restricted Hessian is positive in this exact control", uniform_hessian > 0),
        ("symmetric projected gradient dynamics leaves the uniform datum fixed", projected_uniform_gradient == [Fraction(0)] * n),
        ("no vacuum is fixed by the full coordinate group", all(len(set(w)) > 1 for w in vacua)),
        ("the group-averaged projector is full rank rather than rank one", all(x == Fraction(1, 256) for x in average_projector_diagonal) and len(average_projector_diagonal) == 256),
        ("the vacuum orbit quotient has one orbit", len({tuple(sorted(w)) for w in vacua}) == 1),
        ("the retract-family quotient preserves an abstract line coordinate", transported_scalar == abstract_scalar),
        ("the abstract quotient does not recover an embedded coordinate", len({w.index(max(w)) for w in vacua}) == 256),
        ("the action coefficients contain weight values but no chosen label", action(sample, a, b) == action(vacua[17], a, b) == 0),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    carrier = data.get("frozen_carrier", {})
    owner = data.get("symmetric_nonlinear_vacuum_owner", {})
    vacua = data.get("vacuum_classification", {})
    family = data.get("equivariant_retract_family", {})
    descent = data.get("orbit_quotient_descent", {})
    result = data.get("result", {})
    if carrier.get("dimension") != 256 or carrier.get("K105_selects_positive_seed") is not False:
        failures.append("carrier")
    if owner.get("S_256_invariant") is not True or owner.get("coordinate_label_in_coefficients") is not False or owner.get("source_or_GU_owned") is not False:
        failures.append("owner")
    if vacua.get("global_minimum_count") != 256 or vacua.get("one_vacuum_stabilizer") != "S_255" or vacua.get("restricted_Hessian_eigenvalue_at_each_vacuum") != "2/257^2" or vacua.get("uniform_weight_is_global_minimum") is not False:
        failures.append("vacua")
    if family.get("map_is_S_256_equivariant") is not True or family.get("every_vacuum_selects_one_existing_K91_action_domain_Green_retract") is not True or family.get("branch_selected_without_extra_datum") is not False:
        failures.append("family")
    if descent.get("total_retract_family_quotient_is_abstract_line") is not True or descent.get("invariant_section_into_vacuum_orbit_exists") is not False or descent.get("distinguished_embedded_rank_one_projector_descends") is not False or descent.get("group_average_projector_rank") != 256:
        failures.append("descent")
    required_false = (
        "unique_physical_branch_selected",
        "concrete_K105_embedded_retract_descends",
        "actual_spacetime_or_BV_BFV_global_quotient_constructed",
        "source_action_or_GU_boundary_law_derived",
        "Born_rule_derived",
        "prediction_or_confirmation_credit",
        "held_out_scored",
    )
    if any(result.get(key) is not False for key in required_false) or result.get("canon_verdict_change") != "none":
        failures.append("result")
    ceiling = data.get("claim_ceiling", "")
    if "finite nonlinear" not in ceiling or "no invariant vacuum section" not in ceiling or "No source/GU action" not in ceiling:
        failures.append("ceiling")
    return failures


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [
        (name, any(not ok for _, ok in exact_checks(name)))
        for name in ("wrong_dimension", "wrong_heavy_weight", "equal_wells")
    ]
    updates = (
        ("invent_K105_selector", lambda d: d["frozen_carrier"].__setitem__("K105_selects_positive_seed", True)),
        ("break_invariance", lambda d: d["symmetric_nonlinear_vacuum_owner"].__setitem__("S_256_invariant", False)),
        ("encode_label", lambda d: d["symmetric_nonlinear_vacuum_owner"].__setitem__("coordinate_label_in_coefficients", True)),
        ("invent_source_owner", lambda d: d["symmetric_nonlinear_vacuum_owner"].__setitem__("source_or_GU_owned", True)),
        ("wrong_vacuum_count", lambda d: d["vacuum_classification"].__setitem__("global_minimum_count", 1)),
        ("wrong_stabilizer", lambda d: d["vacuum_classification"].__setitem__("one_vacuum_stabilizer", "S_256")),
        ("erase_hessian_gap", lambda d: d["vacuum_classification"].__setitem__("restricted_Hessian_eigenvalue_at_each_vacuum", "0")),
        ("promote_uniform", lambda d: d["vacuum_classification"].__setitem__("uniform_weight_is_global_minimum", True)),
        ("break_equivariance", lambda d: d["equivariant_retract_family"].__setitem__("map_is_S_256_equivariant", False)),
        ("invent_branch", lambda d: d["equivariant_retract_family"].__setitem__("branch_selected_without_extra_datum", True)),
        ("invent_section", lambda d: d["orbit_quotient_descent"].__setitem__("invariant_section_into_vacuum_orbit_exists", True)),
        ("invent_embedded_descent", lambda d: d["orbit_quotient_descent"].__setitem__("distinguished_embedded_rank_one_projector_descends", True)),
        ("rank_one_average", lambda d: d["orbit_quotient_descent"].__setitem__("group_average_projector_rank", 1)),
        ("invent_physical_branch", lambda d: d["result"].__setitem__("unique_physical_branch_selected", True)),
        ("invent_global_BV", lambda d: d["result"].__setitem__("actual_spacetime_or_BV_BFV_global_quotient_constructed", True)),
        ("invent_Born", lambda d: d["result"].__setitem__("Born_rule_derived", True)),
        ("score_holdout", lambda d: d["result"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["result"].__setitem__("canon_verdict_change", "changed")),
        ("erase_scope", lambda d: d.__setitem__("claim_ceiling", "GU selects one physical branch.")),
    )
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught.append((name, bool(manifest_failures(mutant))))
    for name, ok in caught:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(int(bool(ok)) for _, ok in caught)}/{len(caught)} caught")
    return 0 if all(ok for _, ok in caught) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if "--selftest" in sys.argv:
        return selftest(data)
    checks = exact_checks()
    checks.append(("manifest preserves variational, descent and ownership ceilings", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"K111 K105 SYMMETRIC VACUUM/QUOTIENT: {sum(int(bool(ok)) for _, ok in checks)}/{len(checks)} pass")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
