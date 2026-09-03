#!/usr/bin/env python3
"""Exact K105 conditional boundary-selector and finite-interface controls."""
from __future__ import annotations

import copy
from functools import lru_cache
import json
from pathlib import Path
import sys

import sympy as sp

import k105_k155_carrier_weyl_action_bv_green_probe as K105


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k110-k105-boundary-state-selector-interface-wave.json"


def partial_trace_second(a: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(2, 2, lambda i, j: sum(a[2 * i + k, 2 * j + k] for k in range(2)))


def row_is_zero(matrix: sp.MatrixBase, row: int) -> bool:
    return all(matrix[row, column] == 0 for column in range(matrix.cols))


@lru_cache(maxsize=1)
def frozen_fixture() -> dict[str, object]:
    return K105.build_fixture()


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    fixture = frozen_fixture()
    coefficient = sp.SparseMatrix(fixture["coefficient"])
    lowerer = sp.SparseMatrix(fixture["lowerer"])
    positive_blind = [
        i for i, sign in enumerate(lowerer.diagonal())
        if sign == 1 and row_is_zero(coefficient, i)
    ]
    weights = [sp.Rational(1, 257)] * 256
    weights[0] = sp.Rational(2, 257)
    if mutation == "equalize_weights":
        weights[0] = sp.Rational(1, 257)
    elif mutation == "denormalize_weights":
        weights[-1] = sp.Rational(2, 257)

    density = sp.zeros(448)
    for seed, weight in zip(positive_blind, weights):
        density[seed, seed] = weight
    selected = max(range(256), key=weights.__getitem__)
    maximum_multiplicity = weights.count(max(weights))
    equal_weights = [sp.Rational(1, 256)] * 256
    projector = sp.zeros(448)
    projector[positive_blind[selected], positive_blind[selected]] = 1
    swapped_weights = list(weights)
    swapped_weights[0], swapped_weights[1] = swapped_weights[1], swapped_weights[0]

    I = sp.eye(2)
    X = sp.Matrix([[0, 1], [1, 0]])
    Z = sp.diag(1, -1)
    J = sp.Matrix([[0, -1], [1, 0]])
    plus = sp.Matrix([1, 1]) / sp.sqrt(2)
    minus = sp.Matrix([1, -1]) / sp.sqrt(2)
    Pplus = plus * plus.T
    mixture = I / 2
    interference = (
        sp.simplify(sp.trace((plus * plus.T) * Pplus)),
        sp.simplify(sp.trace((minus * minus.T) * Pplus)),
        sp.simplify(sp.trace(mixture * Pplus)),
    )
    bell = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
    rho_bell = bell * bell.T
    B0 = (Z + X) / sp.sqrt(2)
    B1 = (Z - X) / sp.sqrt(2)
    chsh = (
        sp.kronecker_product(Z, B0)
        + sp.kronecker_product(Z, B1)
        + sp.kronecker_product(X, B0)
        - sp.kronecker_product(X, B1)
    )
    bell_value = sp.simplify(sp.trace(rho_bell * chsh))
    hidden = sp.kronecker_product(J, J)
    local = [I, X, Z]
    products = [sp.kronecker_product(a, b) for a in local for b in local]
    product_rank = sp.Matrix.hstack(*(a.reshape(16, 1) for a in products)).rank()
    augmented_rank = sp.Matrix.hstack(
        *(a.reshape(16, 1) for a in products), hidden.reshape(16, 1)
    ).rank()
    quarter_turn = J

    return [
        ("the frozen K105 positive coefficient-blind seed count is 256", len(positive_blind) == 256),
        ("the conditional boundary weights are strictly positive", all(weight > 0 for weight in weights)),
        ("the conditional boundary weights are normalized", sum(weights) == 1),
        ("the boundary density has rank 256 on the positive blind block", density.rank() == 256),
        ("the rational boundary weight has one strict maximum", maximum_multiplicity == 1 and selected == 0),
        ("the unique-maximum selection gap is 1/257", max(weights) - sorted(weights)[-2] == sp.Rational(1, 257)),
        ("the e0/e1 seed swap has nonzero boundary-state defect", weights[0] != weights[1]),
        ("the boundary stabilizer is S255 by one-plus-255 weight multiplicities", weights.count(sp.Rational(2, 257)) == 1 and weights.count(sp.Rational(1, 257)) == 255),
        ("the equal-weight negative control retains S256 and selects no seed", len(set(equal_weights)) == 1),
        ("moving the heavy weight moves the selected seed with K105 fixed", max(range(256), key=swapped_weights.__getitem__) == 1),
        ("the selected spectral projector is idempotent", projector * projector == projector),
        ("the selected projector is K self-adjoint", projector.T * lowerer == lowerer * projector),
        ("the selected line is K positive", (projector.T * lowerer * projector)[positive_blind[0], positive_blind[0]] == 1),
        ("the K105 cross coefficient annihilates the selected line", coefficient.T * lowerer * projector == sp.zeros(10, 448)),
        ("the boundary quotient has one-dimensional range and 447-dimensional kernel", projector.rank() == 1 and 448 - projector.rank() == 447),
        ("the finite dynamics generator is skew and its quarter-turn is orthogonal", J.T == -J and quarter_turn.T * quarter_turn == I),
        ("orthogonal conjugation preserves trace and positivity", sp.trace(quarter_turn * Pplus * quarter_turn.T) == 1 and quarter_turn * Pplus * quarter_turn.T == minus * minus.T),
        ("the packet-owned state/effect pairing gives probabilities 1,0,1/2", interference == (1, 0, sp.Rational(1, 2))),
        ("the packet-owned real tensor interface saturates Tsirelson", bell_value == 2 * sp.sqrt(2)),
        ("the Bell local marginal is maximally mixed", partial_trace_second(rho_bell) == I / 2),
        ("the displayed Bell state is normalized and positive", sp.trace(rho_bell) == 1 and rho_bell.is_positive_semidefinite),
        ("the real composite retains one hidden nonlocal direction", hidden.T == hidden and product_rank == 9 and augmented_rank == 10),
        ("the selected seed is exactly recoverable from the boundary weights", selected == weights.index(max(weights))),
        ("the selection owner changes while the frozen K105 fixture does not", swapped_weights != weights and len(positive_blind) == 256),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    frozen = data.get("frozen_k105_data", {})
    boundary = data.get("conditional_boundary_owner", {})
    theorem = data.get("stabilizer_and_information_theorem", {})
    quotient = data.get("boundary_owned_quotient_and_retract", {})
    interface = data.get("packet_owned_finite_operational_interface", {})
    result = data.get("result", {})
    if frozen.get("positive_coefficient_blind_seed_count") != 256 or frozen.get("K105_selects_positive_seed") is not False:
        failures.append("frozen")
    if boundary.get("unique_maximum_seed") != 0 or boundary.get("selection_gap") != "1/257" or boundary.get("coordinate_permutation_stabilizer") != "S_255" or boundary.get("source_owned") is not False or boundary.get("physically_derived") is not False:
        failures.append("boundary")
    if theorem.get("coordinate_seed_is_uniquely_selected_iff_weight_is_unique_strict_maximum") is not True or theorem.get("selection_information_is_relocated_not_derived") is not True:
        failures.append("theorem")
    if quotient.get("projector_K_self_adjoint") is not True or quotient.get("K91_action_retract_selected") is not True or quotient.get("ambient_K105_inertia_changed") is not False or quotient.get("quotient_owner") != "conditional_boundary_packet":
        failures.append("quotient")
    if interface.get("interface_owner") != "same_conditional_boundary_packet" or interface.get("Bell_CHSH") != "2_sqrt_2" or interface.get("operational_no_signalling") is not True or interface.get("Born_pairing_derived_from_K105") is not False:
        failures.append("interface")
    if result.get("nonzero_positive_blind_symmetry_defect_constructed") is not True or result.get("one_positive_K91_retract_conditionally_selected") is not True or result.get("selection_derived_from_frozen_K105_data") is not False or result.get("source_or_GU_physical_state_selected") is not False or result.get("Born_rule_derived") is not False or result.get("prediction_or_confirmation_credit") is not False or result.get("held_out_scored") is not False or result.get("canon_verdict_change") != "none":
        failures.append("result")
    ceiling = data.get("claim_ceiling", "")
    if "selection is relocated rather than derived" not in ceiling or "No source/GU boundary law" not in ceiling or "held-out score" not in ceiling:
        failures.append("ceiling")
    return failures


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [
        (name, any(not ok for _, ok in exact_checks(name)))
        for name in ("equalize_weights", "denormalize_weights")
    ]
    updates = (
        ("wrong_seed_count", lambda d: d["frozen_k105_data"].__setitem__("positive_coefficient_blind_seed_count", 255)),
        ("invent_K105_selection", lambda d: d["frozen_k105_data"].__setitem__("K105_selects_positive_seed", True)),
        ("wrong_selected_seed", lambda d: d["conditional_boundary_owner"].__setitem__("unique_maximum_seed", 1)),
        ("erase_gap", lambda d: d["conditional_boundary_owner"].__setitem__("selection_gap", "0")),
        ("wrong_stabilizer", lambda d: d["conditional_boundary_owner"].__setitem__("coordinate_permutation_stabilizer", "S_256")),
        ("invent_source_owner", lambda d: d["conditional_boundary_owner"].__setitem__("source_owned", True)),
        ("invent_physical_derivation", lambda d: d["conditional_boundary_owner"].__setitem__("physically_derived", True)),
        ("erase_iff", lambda d: d["stabilizer_and_information_theorem"].__setitem__("coordinate_seed_is_uniquely_selected_iff_weight_is_unique_strict_maximum", False)),
        ("invent_derivation", lambda d: d["stabilizer_and_information_theorem"].__setitem__("selection_information_is_relocated_not_derived", False)),
        ("drop_K_self_adjointness", lambda d: d["boundary_owned_quotient_and_retract"].__setitem__("projector_K_self_adjoint", False)),
        ("alter_ambient_inertia", lambda d: d["boundary_owned_quotient_and_retract"].__setitem__("ambient_K105_inertia_changed", True)),
        ("misassign_quotient_owner", lambda d: d["boundary_owned_quotient_and_retract"].__setitem__("quotient_owner", "K105")),
        ("misassign_interface_owner", lambda d: d["packet_owned_finite_operational_interface"].__setitem__("interface_owner", "GU_source")),
        ("inflate_Bell", lambda d: d["packet_owned_finite_operational_interface"].__setitem__("Bell_CHSH", "4")),
        ("invent_Born_derivation", lambda d: d["packet_owned_finite_operational_interface"].__setitem__("Born_pairing_derived_from_K105", True)),
        ("invent_GU_state", lambda d: d["result"].__setitem__("source_or_GU_physical_state_selected", True)),
        ("invent_prediction", lambda d: d["result"].__setitem__("prediction_or_confirmation_credit", True)),
        ("score_holdout", lambda d: d["result"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["result"].__setitem__("canon_verdict_change", "changed")),
        ("erase_scope", lambda d: d.__setitem__("claim_ceiling", "K105 derives the physical state and Born rule.")),
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
    data = json.loads(MANIFEST.read_text())
    if "--selftest" in sys.argv:
        return selftest(data)
    checks = exact_checks()
    checks.append(("manifest preserves selector, interface and ownership ceilings", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"K110 K105 BOUNDARY SELECTOR/INTERFACE: {sum(int(bool(ok)) for _, ok in checks)}/{len(checks)} pass")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
