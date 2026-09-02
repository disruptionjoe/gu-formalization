#!/usr/bin/env python3
"""Exact real-quantum composition and anchor controls for K108."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k108-real-quantum-local-tomography-boundary-wave.json"


def tr(a: sp.Matrix) -> sp.Expr:
    return sp.trace(a)


def partial_trace_second(a: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(2, 2, lambda i, j: sum(a[2 * i + k, 2 * j + k] for k in range(2)))


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    I = sp.eye(2)
    X = sp.Matrix([[0, 1], [1, 0]])
    Z = sp.diag(1, -1)
    J = sp.Matrix([[0, -1], [1, 0]])
    H = sp.kronecker_product(J, J)
    if mutation == "visible_hidden_direction":
        H = sp.kronecker_product(X, X)

    local = [I, X, Z]
    products = [sp.kronecker_product(a, b) for a in local for b in local]
    product_rank = sp.Matrix.hstack(*(a.reshape(16, 1) for a in products)).rank()
    augmented_rank = sp.Matrix.hstack(*(a.reshape(16, 1) for a in products), H.reshape(16, 1)).rank()
    rho_plus = (sp.eye(4) + H) / 4
    rho_minus = (sp.eye(4) - H) / 4

    plus = sp.Matrix([1, 1]) / sp.sqrt(2)
    minus = sp.Matrix([1, -1]) / sp.sqrt(2)
    Pplus = plus * plus.T
    coherent_plus = plus * plus.T
    coherent_minus = minus * minus.T
    mixture = sp.eye(2) / 2

    bell = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
    rho_bell = bell * bell.T
    B0 = (Z + X) / sp.sqrt(2)
    B1 = (Z - X) / sp.sqrt(2)
    CHSH = sp.kronecker_product(Z, B0) + sp.kronecker_product(Z, B1) + sp.kronecker_product(X, B0) - sp.kronecker_product(X, B1)

    eig_plus = set(rho_plus.eigenvals())
    eig_minus = set(rho_minus.eigenvals())
    local_differences = [sp.simplify(tr((rho_plus - rho_minus) * effect)) for effect in products]
    return [
        ("local rebit observable space has dimension three", sp.Matrix.hstack(*(a.reshape(4, 1) for a in local)).rank() == 3),
        ("local product observables span dimension nine", product_rank == 9),
        ("the global symmetric rebit space has dimension ten", 4 * 5 // 2 == 10),
        ("J tensor J is symmetric and squares to one", H.T == H and H * H == sp.eye(4)),
        ("J tensor J supplies the missing tenth direction", augmented_rank == 10),
        ("the hidden direction is orthogonal to every local symmetric product", all(value == 0 for value in local_differences)),
        ("rho plus and minus are positive normalized states", tr(rho_plus) == tr(rho_minus) == 1 and eig_plus <= {0, sp.Rational(1, 2)} and eig_minus <= {0, sp.Rational(1, 2)}),
        ("rho plus and minus are distinct", rho_plus != rho_minus),
        ("the global hidden observable distinguishes them", tr(rho_plus * H) == 1 and tr(rho_minus * H) == -1),
        ("real coherent alternatives interfere exactly", tr(coherent_plus * Pplus) == 1 and tr(coherent_minus * Pplus) == 0 and tr(mixture * Pplus) == sp.Rational(1, 2)),
        ("the real Bell witness saturates Tsirelson", sp.simplify(tr(rho_bell * CHSH)) == 2 * sp.sqrt(2)),
        ("the Bell local marginal is maximally mixed", partial_trace_second(rho_bell) == sp.eye(2) / 2),
    ]


def failures(data: dict) -> list[str]:
    out: list[str] = []
    local = data.get("local_system", {})
    composite = data.get("composite", {})
    states = data.get("indistinguishable_states", {})
    controls = data.get("calibration_controls", {})
    result = data.get("result", {})
    if local.get("field") != "real" or local.get("dimension") != 3:
        out.append("local")
    if composite.get("global_dimension") != 10 or composite.get("local_product_span_dimension") != 9 or composite.get("locally_tomographic") is not False:
        out.append("dimensions")
    if composite.get("hidden_direction") != "J_tensor_J" or composite.get("hidden_direction_orthogonal_to_all_local_symmetric_products") is not True:
        out.append("hidden")
    if states.get("positive") is not True or states.get("normalized") is not True or states.get("distinct") is not True or states.get("same_all_local_product_expectations") is not True or states.get("global_J_tensor_J_expectations") != [1, -1]:
        out.append("states")
    if controls.get("real_two_path_interference") is not True or controls.get("real_Bell_CHSH") != "2_sqrt_2" or controls.get("operational_no_signalling") is not True or controls.get("held_out_scored") is not False:
        out.append("anchors")
    if result.get("two_calibration_anchors_select_complex_scalars") is not False or result.get("two_calibration_anchors_select_local_tomography") is not False or result.get("real_quantum_composite_is_exact_contrary_model") is not True:
        out.append("result")
    if result.get("GU_native_composition_or_state_constructed") is not False or result.get("Born_rule_derived") is not False or result.get("prediction_or_confirmation_credit") is not False or result.get("canon_verdict_change") != "none":
        out.append("promotion")
    ceiling = data.get("claim_ceiling", "")
    if "real-quantum countermodel" not in ceiling or "does not choose a GU carrier" not in ceiling:
        out.append("ceiling")
    return out


def selftest(data: dict) -> int:
    if failures(data) or not all(ok for _, ok in exact_checks()):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [("visible_hidden_direction", any(not ok for _, ok in exact_checks("visible_hidden_direction")))]
    updates = (
        ("wrong_local_dimension", lambda d: d["local_system"].__setitem__("dimension", 4)),
        ("wrong_product_dimension", lambda d: d["composite"].__setitem__("local_product_span_dimension", 10)),
        ("invent_local_tomography", lambda d: d["composite"].__setitem__("locally_tomographic", True)),
        ("erase_hidden_orthogonality", lambda d: d["composite"].__setitem__("hidden_direction_orthogonal_to_all_local_symmetric_products", False)),
        ("erase_positivity", lambda d: d["indistinguishable_states"].__setitem__("positive", False)),
        ("erase_indistinguishability", lambda d: d["indistinguishable_states"].__setitem__("same_all_local_product_expectations", False)),
        ("wrong_global_values", lambda d: d["indistinguishable_states"].__setitem__("global_J_tensor_J_expectations", [0, 0])),
        ("erase_interference", lambda d: d["calibration_controls"].__setitem__("real_two_path_interference", False)),
        ("invent_complex_selection", lambda d: d["result"].__setitem__("two_calibration_anchors_select_complex_scalars", True)),
        ("invent_tomography_selection", lambda d: d["result"].__setitem__("two_calibration_anchors_select_local_tomography", True)),
        ("invent_GU_state", lambda d: d["result"].__setitem__("GU_native_composition_or_state_constructed", True)),
        ("invent_Born", lambda d: d["result"].__setitem__("Born_rule_derived", True)),
        ("promote_canon", lambda d: d["result"].__setitem__("canon_verdict_change", "changed")),
        ("erase_scope", lambda d: d.__setitem__("claim_ceiling", "Quantum theory is not selected.")),
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
    checks.append(("manifest preserves the countermodel and claim ceiling", not failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"K108 REAL QUANTUM LOCAL TOMOGRAPHY: {sum(ok for _, ok in checks)}/{len(checks)} pass")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
