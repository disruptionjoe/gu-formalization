#!/usr/bin/env python3
"""Exact controls for the K105 quadratic-ray normalization boundary."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k108-k105-quadratic-ray-cone-normalization-boundary-wave.json"


def q(v: sp.Matrix) -> sp.Matrix:
    return v * v.T


def symvec(a: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([a[0, 0], a[1, 1], a[2, 2], a[0, 1], a[0, 2], a[1, 2]])


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    K = sp.diag(1, 1, -1)
    e1, e2, f = (sp.eye(3).col(i) for i in range(3))
    positive_vectors = [e1, e2, e1 + e2, 2 * e1 + f, 2 * e1 - f, 2 * e2 + f]
    if mutation == "timelike_generator":
        positive_vectors[-1] = f
    rays = [q(v) for v in positive_vectors]
    k_trace = lambda a: sp.trace(K * a)

    b11, b22, b33, b12, b13, b23 = sp.symbols("b11 b22 b33 b12 b13 b23")
    B = sp.Matrix([[b11, b12, b13], [b12, b22, b23], [b13, b23, b33]])
    signs = [sp.diag(-1, 1, 1), sp.diag(1, -1, 1), sp.diag(1, 1, -1)]
    swap = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    group_generators = signs + [swap]
    equations = []
    for g in group_generators:
        equations.extend(list(g.T * B * g - B))
    coeff = sp.linear_eq_to_matrix(equations, [b11, b22, b33, b12, b13, b23])[0]

    H1 = sp.eye(3)
    H2 = sp.diag(1, 1, 2)
    n = sp.symbols("n", positive=True, integer=True)
    vn = sp.Matrix([(n + 1) / n, 0, 1])
    null = e1 + f

    return [
        ("surrogate has inertia 2/1/0", tuple(K.diagonal()).count(1) == 2 and tuple(K.diagonal()).count(-1) == 1),
        ("every declared quadratic generator is K-positive", all(k_trace(a) > 0 for a in rays)),
        ("every quadratic generator is positive semidefinite", all(a.is_positive_semidefinite for a in rays)),
        ("positive quadratic generators span all Sym2(R3)", sp.Matrix.hstack(*(symvec(a) for a in rays)).rank() == 6),
        ("product-group invariant linear normalizations form two dimensions", 6 - coeff.rank() == 2),
        ("identity is an invariant positive-definite majorant", H1.is_positive_definite is True and all(g.T * H1 * g == H1 for g in group_generators)),
        ("a second nonproportional invariant positive majorant exists", H2.is_positive_definite is True and H2 != H1 and all(g.T * H2 * g == H2 for g in group_generators)),
        ("positive rays converge to a nonzero null-boundary ray", q(null) != sp.zeros(3) and k_trace(q(null)) == 0 and sp.simplify(k_trace(q(vn))) > 0 and all(sp.limit(q(vn)[i, j], n, sp.oo) == q(null)[i, j] for i in range(3) for j in range(3))),
        ("identity normalization is faithful on nonzero PSD matrices", sp.trace(q(null)) > 0 and all(sp.trace(a) > 0 for a in rays)),
        ("identity-normalized pure rays are Euclidean bounded", all(sp.simplify(sp.trace(q(v / sp.sqrt((v.T * v)[0])))) == 1 for v in positive_vectors)),
        ("the two majorants assign different relative negative-block weight", sp.trace(H1 * q(f)) == sp.trace(H1 * q(e1)) and sp.trace(H2 * q(f)) == 2 * sp.trace(H2 * q(e1))),
    ]


def failures(data: dict) -> list[str]:
    out: list[str] = []
    carrier = data.get("actual_carrier", {})
    lift = data.get("quadratic_lift", {})
    norm = data.get("invariant_normalization", {})
    result = data.get("result", {})
    if carrier.get("lowerer_inertia") != [256, 183, 0] or carrier.get("proved_symmetry_subgroup") != "O(256)_times_O(183)":
        out.append("carrier")
    if lift.get("identifies_sign") is not True or lift.get("pointed") is not True or lift.get("linear_span_is_all_Sym2") is not True:
        out.append("lift")
    if lift.get("closed") is not False or lift.get("nonzero_null_rank_one_rays_in_closure") is not True:
        out.append("closure")
    if norm.get("invariant_space_dimension") != 2 or norm.get("invariant_positive_definite_majorants_exist") is not True or norm.get("closed_cone_trace_one_base_compact") is not True or norm.get("relative_block_weight_uniquely_selected_by_group") is not False:
        out.append("normalization")
    if result.get("raw_sign_obstruction_evaded_by_quadratic_lift") is not True or result.get("closed_faithfully_normalized_compact_repository_control_constructed") is not True or result.get("normalization_family_unique") is not False or result.get("new_rank_one_selector_constructed") is not False:
        out.append("result")
    if result.get("source_or_action_owner_added") is not False or result.get("physical_state_or_Born_credit") is not False or result.get("canon_verdict_change") != "none":
        out.append("promotion")
    ceiling = data.get("claim_ceiling", "")
    if "compact product subgroup" not in ceiling or "No source-owned physical state" not in ceiling:
        out.append("ceiling")
    return out


def selftest(data: dict) -> int:
    if failures(data) or not all(ok for _, ok in exact_checks()):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [("timelike_generator", any(not ok for _, ok in exact_checks("timelike_generator")))]
    updates = (
        ("wrong_inertia", lambda d: d["actual_carrier"].__setitem__("lowerer_inertia", [439, 0, 0])),
        ("erase_sign_escape", lambda d: d["quadratic_lift"].__setitem__("identifies_sign", False)),
        ("deny_span", lambda d: d["quadratic_lift"].__setitem__("linear_span_is_all_Sym2", False)),
        ("invent_closed_open_cone", lambda d: d["quadratic_lift"].__setitem__("closed", True)),
        ("erase_null_boundary", lambda d: d["quadratic_lift"].__setitem__("nonzero_null_rank_one_rays_in_closure", False)),
        ("collapse_invariant_family", lambda d: d["invariant_normalization"].__setitem__("invariant_space_dimension", 1)),
        ("deny_invariant_majorant", lambda d: d["invariant_normalization"].__setitem__("invariant_positive_definite_majorants_exist", False)),
        ("deny_compact_control", lambda d: d["invariant_normalization"].__setitem__("closed_cone_trace_one_base_compact", False)),
        ("invent_unique_weight", lambda d: d["invariant_normalization"].__setitem__("relative_block_weight_uniquely_selected_by_group", True)),
        ("erase_constructed_control", lambda d: d["result"].__setitem__("closed_faithfully_normalized_compact_repository_control_constructed", False)),
        ("invent_source", lambda d: d["result"].__setitem__("source_or_action_owner_added", True)),
        ("invent_physics", lambda d: d["result"].__setitem__("physical_state_or_Born_credit", True)),
        ("promote_canon", lambda d: d["result"].__setitem__("canon_verdict_change", "changed")),
        ("erase_scope", lambda d: d.__setitem__("claim_ceiling", "A physical state space is selected.")),
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
    checks.append(("manifest preserves the compactification, ambiguity and ceiling", not failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"K108 K105 QUADRATIC RAY NORMALIZATION: {sum(ok for _, ok in checks)}/{len(checks)} pass")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
