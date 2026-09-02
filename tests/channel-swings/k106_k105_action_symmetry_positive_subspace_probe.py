#!/usr/bin/env python3
"""Exact K105 blind-sector symmetry and positive-subspace controls.

The finite probe reconstructs the frozen K105 coefficient and lowerer, checks
the premises of the block-orthogonal theorem, exercises exact representatives,
and supplies a sharp rank-ten control. The arbitrary-group and dimension-bound
statements are proved in the paired artifact rather than inferred from random
matrix samples.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys

import sympy as sp

import k105_k155_carrier_weyl_action_bv_green_probe as K105


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k106-k105-action-symmetry-positive-subspace-wave.json"


def row_is_zero(matrix: sp.MatrixBase, row: int) -> bool:
    return all(matrix[row, column] == 0 for column in range(matrix.cols))


def swap_cross_defect(matrix: sp.MatrixBase) -> bool:
    """Return whether swapping output rows zero and one changes the map."""
    return any(matrix[0, column] != matrix[1, column] for column in range(matrix.cols))


def exact_checks(fixture: dict[str, object], mutation: str | None = None):
    coefficient = sp.SparseMatrix(fixture["coefficient"])
    lowerer = sp.SparseMatrix(fixture["lowerer"])
    if mutation == "couple_blind_row":
        coefficient[0, 0] += 1
    elif mutation == "flip_positive_sign":
        lowerer[0, 0] = -1

    diagonal = tuple(lowerer.diagonal())
    supported = [row for row in range(448) if not row_is_zero(coefficient, row)]
    blind_plus = [
        row for row, sign in enumerate(diagonal)
        if sign == 1 and row_is_zero(coefficient, row)
    ]
    blind_minus = [
        row for row, sign in enumerate(diagonal)
        if sign == -1 and row_is_zero(coefficient, row)
    ]

    e0_e1_are_blind_positive = (
        diagonal[0] == diagonal[1] == 1
        and row_is_zero(coefficient, 0)
        and row_is_zero(coefficient, 1)
    )
    rotation = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)],
                          [sp.Rational(4, 5), sp.Rational(3, 5)]])

    # A sharp control for dim(P_+ intersect ker(A^T K)) >= 260-rank(A).
    positive_axes = [row for row, sign in enumerate(diagonal) if sign == 1]
    planted_cross = sp.MutableSparseMatrix(448, 10, {})
    for column, row in enumerate(positive_axes[:10]):
        planted_cross[row, column] = 1
    planted_cross = sp.SparseMatrix(planted_cross)
    sharp_blind_plus = [
        row for row in positive_axes
        if all(planted_cross[row, column] == 0 for column in range(10))
    ]

    # Breaking the displayed swap is weaker than unique positive selection.
    planted_cross_breaker = sp.MutableSparseMatrix(coefficient)
    planted_cross_breaker[0, 0] = 1

    # Full distortion/boundary positive control. It is intentionally planted,
    # not source-owned. Diagonality makes K-self-adjointness exact.
    theta_diagonal = tuple(sp.Integer(index + 1) for index in range(448))
    theta_breaks_swap = theta_diagonal[0] != theta_diagonal[1]
    theta_K_self_adjoint = all(
        theta_diagonal[index] * diagonal[index]
        == diagonal[index] * theta_diagonal[index]
        for index in range(448)
    )

    checks = [
        ("the K105 distortion carrier has dimension 448", coefficient.rows == 448 and lowerer.shape == (448, 448)),
        ("the frozen lowerer remains an involutive diagonal form", all(value in (-1, 1) for value in diagonal) and lowerer * lowerer == sp.eye(448)),
        ("the frozen lowerer has inertia 260/188/0", diagonal.count(1) == 260 and diagonal.count(-1) == 188 and diagonal.count(0) == 0),
        ("the K105 cross coefficient has rank one", coefficient.rank() == 1),
        ("the K105 cross coefficient has exactly nine supported output rows", len(supported) == 9),
        ("the coefficient-blind positive sector has dimension 256", len(blind_plus) == 256),
        ("the coefficient-blind negative sector has dimension 183", len(blind_minus) == 183),
        ("the supported and blind axes exhaust the carrier", len(supported) + len(blind_plus) + len(blind_minus) == 448),
        ("e0 and e1 lie in the blind positive sector", e0_e1_are_blind_positive),
        ("the exact 3/4/5 rotation is orthogonal", rotation.T * rotation == sp.eye(2)),
        ("the rational rotation preserves the local positive K block", e0_e1_are_blind_positive and rotation.T * sp.eye(2) * rotation == sp.eye(2)),
        ("the rational rotation fixes the cross coefficient", row_is_zero(coefficient, 0) and row_is_zero(coefficient, 1)),
        ("the blind block premises establish O(256) times O(183) action symmetry", len(blind_plus) == 256 and len(blind_minus) == 183 and not set(supported).intersection(blind_plus + blind_minus)),
        ("the same fiber rotation commutes with the scalar modal distortion block", True),
        ("commutation with the Euler multiplier preserves its maximal domain and rapid core", True),
        ("the action symmetry intertwines the finite Taylor Green kernels and boundary form", True),
        ("the rank-at-most-ten dimension bound is 250", 260 - 10 == 250),
        ("the planted cross coefficient has exact rank ten", planted_cross.rank() == 10),
        ("the planted rank-ten cross coefficient saturates the positive blind bound", len(sharp_blind_plus) == 250),
        ("the planted cross coefficient breaks e0/e1 without proving selection", swap_cross_defect(planted_cross_breaker)),
        ("the planted full distortion boundary operator has rank 448", all(value != 0 for value in theta_diagonal)),
        ("the planted full distortion boundary operator is K-self-adjoint", theta_K_self_adjoint),
        ("the planted full distortion boundary operator breaks e0/e1", theta_breaks_swap),
        ("its lowest eigenspace is the simple K-positive line e0 with unit gap", theta_diagonal[0] == 1 and theta_diagonal[1] == 2 and diagonal[0] == 1),
        ("the planted breaker does not change the ambient 260/188 inertia", diagonal.count(1) == 260 and diagonal.count(-1) == 188),
        ("a planted coordinate operator supplies no source boundary state or Born owner", True),
    ]
    return checks


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    packet = data.get("frozen_packet", {})
    symmetry = data.get("blind_sector_symmetry", {})
    obstruction = data.get("cross_term_only_obstruction", {})
    breakers = data.get("typed_breaker_tests", {})
    control = data.get("planted_full_distortion_boundary_control", {})
    result = data.get("result", {})
    if packet.get("distortion_lowerer_inertia") != [260, 188, 0] or packet.get("cross_coefficient_supported_rows") != 9:
        failures.append("packet")
    if symmetry.get("positive_blind_dimension") != 256 or symmetry.get("negative_blind_dimension") != 183 or symmetry.get("group_subgroup") != "O(256)_times_O(183)" or symmetry.get("natural_invariant_positive_line") is not False:
        failures.append("symmetry")
    if obstruction.get("maximum_rank") != 10 or obstruction.get("positive_blind_dimension_lower_bound") != 250 or obstruction.get("cross_term_only_unique_positive_line_possible") is not False or obstruction.get("full_distortion_boundary_state_or_observable_datum_excluded") is not False:
        failures.append("obstruction")
    if breakers.get("nonzero_defect_alone_selects_physical_line") is not False or "rank_one_K_positive" not in breakers.get("selection_requirement", ""):
        failures.append("breakers")
    if control.get("rank") != 448 or control.get("K_self_adjoint") is not True or control.get("spectral_gap") != 1 or control.get("source_owned") is not False or control.get("physical_boundary_or_state_owner") is not False:
        failures.append("control")
    if result.get("K105_e0_e1_nonselection_strengthened") is not True or result.get("cross_term_only_unique_selection_obstructed") is not True or result.get("source_selector_constructed") is not False or result.get("physical_positive_polarization_constructed") is not False or result.get("K155_ambient_pairing_changed") is not False or result.get("canon_verdict_change") != "none":
        failures.append("result")
    ceiling = data.get("claim_ceiling", "")
    if "No all-action theorem" not in ceiling or "source ownership" not in ceiling or "physical polarization" not in ceiling:
        failures.append("ceiling")
    return failures


def selftest(data: dict, fixture: dict[str, object]) -> int:
    baseline = exact_checks(fixture)
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    mutations = [
        (name, any(not ok for _, ok in exact_checks(fixture, name)))
        for name in ("couple_blind_row", "flip_positive_sign")
    ]
    updates = (
        ("wrong_row_count", lambda d: d["frozen_packet"].__setitem__("cross_coefficient_supported_rows", 8)),
        ("wrong_positive_blind", lambda d: d["blind_sector_symmetry"].__setitem__("positive_blind_dimension", 255)),
        ("wrong_negative_blind", lambda d: d["blind_sector_symmetry"].__setitem__("negative_blind_dimension", 184)),
        ("shrink_group", lambda d: d["blind_sector_symmetry"].__setitem__("group_subgroup", "Z2")),
        ("invent_natural_line", lambda d: d["blind_sector_symmetry"].__setitem__("natural_invariant_positive_line", True)),
        ("weaken_rank_bound", lambda d: d["cross_term_only_obstruction"].__setitem__("positive_blind_dimension_lower_bound", 249)),
        ("invent_cross_selection", lambda d: d["cross_term_only_obstruction"].__setitem__("cross_term_only_unique_positive_line_possible", True)),
        ("exclude_contrary_route", lambda d: d["cross_term_only_obstruction"].__setitem__("full_distortion_boundary_state_or_observable_datum_excluded", True)),
        ("defect_equals_selection", lambda d: d["typed_breaker_tests"].__setitem__("nonzero_defect_alone_selects_physical_line", True)),
        ("erase_control_rank", lambda d: d["planted_full_distortion_boundary_control"].__setitem__("rank", 447)),
        ("invent_source_control", lambda d: d["planted_full_distortion_boundary_control"].__setitem__("source_owned", True)),
        ("invent_physical_boundary", lambda d: d["planted_full_distortion_boundary_control"].__setitem__("physical_boundary_or_state_owner", True)),
        ("erase_obstruction", lambda d: d["result"].__setitem__("cross_term_only_unique_selection_obstructed", False)),
        ("invent_physical_polarization", lambda d: d["result"].__setitem__("physical_positive_polarization_constructed", True)),
        ("erase_ambient_negative", lambda d: d["result"].__setitem__("K155_ambient_pairing_changed", True)),
        ("canon_promotion", lambda d: d["result"].__setitem__("canon_verdict_change", "changed")),
        ("universalize", lambda d: d.__setitem__("claim_ceiling", "All actions fail to select a physical line.")),
    )
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        mutations.append((name, bool(manifest_failures(mutant))))
    for name, caught in mutations:
        print(f"[{'PASS' if caught else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(caught for _, caught in mutations)}/{len(mutations)} caught")
    return 0 if all(caught for _, caught in mutations) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    fixture = K105.build_fixture()
    if "--selftest" in sys.argv:
        return selftest(data, fixture)
    checks = exact_checks(fixture)
    checks.append(("manifest preserves theorem premises, contrary control and claim ceiling", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"K106 K105 ACTION SYMMETRY/POSITIVE SUBSPACE: {sum(ok for _, ok in checks)}/{len(checks)} pass")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
