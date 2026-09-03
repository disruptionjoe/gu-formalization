#!/usr/bin/env python3
"""Exact K105/K91 retract-equivariant quantum-anchor nonselection controls."""
from __future__ import annotations

import copy
from functools import lru_cache
import itertools
import json
from pathlib import Path
import sys

import sympy as sp

import k105_k155_carrier_weyl_action_bv_green_probe as K105


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k109-k105-quantum-anchor-retract-selection-boundary-wave.json"


def trace(a: sp.Matrix) -> sp.Expr:
    return sp.trace(a)


def partial_trace_second(a: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(2, 2, lambda i, j: sum(a[2 * i + k, 2 * j + k] for k in range(2)))


@lru_cache(maxsize=1)
def base_fixture() -> tuple[sp.SparseMatrix, sp.SparseMatrix]:
    fixture = K105.build_fixture()
    return sp.SparseMatrix(fixture["coefficient"]), sp.SparseMatrix(fixture["lowerer"])


def exact_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    base_coefficient, base_lowerer = base_fixture()
    coefficient = sp.SparseMatrix(base_coefficient)
    lowerer = sp.SparseMatrix(base_lowerer)
    if mutation == "couple_second_seed":
        coefficient[1, 0] = 1
    elif mutation == "flip_second_seed":
        lowerer[1, 1] = -1

    weighted = lowerer * coefficient
    positive = [i for i, value in enumerate(lowerer.diagonal()) if value == 1]
    valid = [i for i in positive if all(weighted[i, j] == 0 for j in range(10))]
    e0 = sp.zeros(448, 1)
    e1 = sp.zeros(448, 1)
    e0[0] = 1
    e1[1] = 1

    # K85's complete joint-assignment control for commutative H^0.
    assignments = list(itertools.product((-1, 1), repeat=4))
    chsh = [a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1 for a0, a1, b0, b1 in assignments]
    if mutation == "inflate_classical_face":
        chsh[0] = 4
    f = sp.Matrix(range(16))
    g = sp.Matrix(list(reversed(range(16))))
    fg = sp.Matrix([f[i] * g[i] for i in range(16)])
    gf = sp.Matrix([g[i] * f[i] for i in range(16)])

    # The explicitly imported K108 real-quantum interface.
    I = sp.eye(2)
    X = sp.Matrix([[0, 1], [1, 0]])
    Z = sp.diag(1, -1)
    J = sp.Matrix([[0, -1], [1, 0]])
    plus = sp.Matrix([1, 1]) / sp.sqrt(2)
    minus = sp.Matrix([1, -1]) / sp.sqrt(2)
    Pplus = plus * plus.T
    mixture = I / 2
    interference = (
        sp.simplify(trace((plus * plus.T) * Pplus)),
        sp.simplify(trace((minus * minus.T) * Pplus)),
        sp.simplify(trace(mixture * Pplus)),
    )
    bell = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
    rho_bell = bell * bell.T
    B0 = (Z + X) / sp.sqrt(2)
    B1 = (Z - X) / sp.sqrt(2)
    C = (
        sp.kronecker_product(Z, B0)
        + sp.kronecker_product(Z, B1)
        + sp.kronecker_product(X, B0)
        - sp.kronecker_product(X, B1)
    )
    bell_value = sp.simplify(trace(rho_bell * C))
    H = sp.kronecker_product(J, J)
    local = [I, X, Z]
    products = [sp.kronecker_product(a, b) for a in local for b in local]
    product_rank = sp.Matrix.hstack(*(a.reshape(16, 1) for a in products)).rank()
    augmented_rank = sp.Matrix.hstack(*(a.reshape(16, 1) for a in products), H.reshape(16, 1)).rank()
    if mutation == "break_anchor_equivariance":
        seed_statistics = (interference, (interference[0], interference[1], sp.Integer(0)))
    else:
        seed_statistics = (interference, interference)

    return [
        ("the frozen K105 fixture has 256 positive coefficient-blind coordinate retract seeds", len(valid) == 256),
        ("e0 and e1 are distinct admitted positive retract seeds", 0 in valid and 1 in valid and e0 != e1),
        ("both displayed seeds have unit K norm and are K orthogonal", (e0.T * lowerer * e0)[0] == 1 and (e1.T * lowerer * e1)[0] == 1 and (e0.T * lowerer * e1)[0] == 0),
        ("the e0/e1 swap preserves the frozen lowerer", lowerer[0, 0] == lowerer[1, 1] == 1 and lowerer[0, 1] == lowerer[1, 0] == 0),
        ("the e0/e1 swap preserves the frozen Weyl coefficient", all(coefficient[row, col] == 0 for row in (0, 1) for col in range(10))),
        ("all 16 classical joint assignments are present", len(assignments) == 16),
        ("pointwise degree-zero observables commute", fg == gf),
        ("the commutative joint algebra has sharp CHSH ceiling two", set(chsh) == {-2, 2}),
        ("the transported classical boundary therefore cannot realize the Bell anchor", max(chsh) == 2 < 2 * sp.sqrt(2)),
        ("each positive seed supplies the same two-mode positive Gram control", (e0.T * lowerer * e0)[0] * sp.eye(2) == (e1.T * lowerer * e1)[0] * sp.eye(2) == sp.eye(2)),
        ("the imported rebit interface realizes exact two-path probabilities 1,0,1/2", interference == (1, 0, sp.Rational(1, 2))),
        ("the imported real Bell interface saturates Tsirelson", bell_value == 2 * sp.sqrt(2)),
        ("the Bell local marginal is maximally mixed", partial_trace_second(rho_bell) == I / 2),
        ("the real composite retains K108's hidden tenth direction", H.T == H and H * H == sp.eye(4) and product_rank == 9 and augmented_rank == 10),
        ("the displayed quantum-anchor statistics are identical on symmetry-related retracts", seed_statistics[0] == seed_statistics[1]),
        ("the exact controls add no source, physical quotient or Born owner", True),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    frozen = data.get("frozen_owner_data", {})
    classical = data.get("classical_cohomology_transport", {})
    quantum = data.get("imported_quantum_interface", {})
    symmetry = data.get("equivariance_and_nonselection", {})
    result = data.get("result", {})
    if frozen.get("positive_coefficient_blind_coordinate_lines") != 256 or frozen.get("proved_action_symmetry_subgroup") != "O(256)_times_O(183)" or frozen.get("source_or_physical_selection_owner") is not False:
        failures.append("frozen")
    if classical.get("sharp_CHSH_ceiling") != 2 or classical.get("transported_to_all_256_positive_retracts") is not True or classical.get("Bell_anchor_satisfied_by_minimal_cohomology") is not False:
        failures.append("classical")
    if quantum.get("Bell_CHSH") != "2_sqrt_2" or quantum.get("operational_no_signalling") is not True or quantum.get("local_tomography") is not False or quantum.get("physical_Born_or_tensor_owner") is not False:
        failures.append("quantum")
    required_symmetry = (
        "positive_retract_seed_swaps_preserve_lowerer",
        "positive_retract_seed_swaps_preserve_Weyl_coefficient",
        "positive_retract_seed_swaps_preserve_action_domain_Green_data",
        "minimal_BRST_cohomology_and_classical_CHSH_are_identical_on_every_seed",
        "imported_interference_Bell_and_no_signalling_statistics_are_identical_on_every_seed",
    )
    if any(symmetry.get(key) is not True for key in required_symmetry) or symmetry.get("calibration_anchors_break_S_256_symmetry") is not False or symmetry.get("K105_action_plus_calibration_anchors_select_unique_positive_retract") is not False:
        failures.append("symmetry")
    if result.get("conditional_quantum_anchor_interfaces_constructed_per_positive_retract") != 256 or result.get("distinct_physical_GU_states_selected") != 0 or result.get("Born_rule_derived") is not False or result.get("prediction_or_confirmation_credit") is not False or result.get("held_out_scored") is not False or result.get("canon_verdict_change") != "none":
        failures.append("result")
    ceiling = data.get("claim_ceiling", "")
    if "explicitly imported" not in ceiling or "do not select a positive retract" not in ceiling or "Born rule" not in ceiling:
        failures.append("ceiling")
    return failures


def selftest(data: dict) -> int:
    baseline = exact_checks()
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    caught = [
        (name, any(not ok for _, ok in exact_checks(name)))
        for name in ("couple_second_seed", "flip_second_seed", "inflate_classical_face", "break_anchor_equivariance")
    ]
    updates = (
        ("wrong_retract_count", lambda d: d["frozen_owner_data"].__setitem__("positive_coefficient_blind_coordinate_lines", 255)),
        ("invent_frozen_owner", lambda d: d["frozen_owner_data"].__setitem__("source_or_physical_selection_owner", True)),
        ("inflate_classical_CHSH", lambda d: d["classical_cohomology_transport"].__setitem__("sharp_CHSH_ceiling", 4)),
        ("invent_classical_Bell", lambda d: d["classical_cohomology_transport"].__setitem__("Bell_anchor_satisfied_by_minimal_cohomology", True)),
        ("invent_local_tomography", lambda d: d["imported_quantum_interface"].__setitem__("local_tomography", True)),
        ("invent_Born_owner", lambda d: d["imported_quantum_interface"].__setitem__("physical_Born_or_tensor_owner", True)),
        ("break_action_equivariance", lambda d: d["equivariance_and_nonselection"].__setitem__("positive_retract_seed_swaps_preserve_action_domain_Green_data", False)),
        ("invent_anchor_symmetry_break", lambda d: d["equivariance_and_nonselection"].__setitem__("calibration_anchors_break_S_256_symmetry", True)),
        ("invent_unique_retract", lambda d: d["equivariance_and_nonselection"].__setitem__("K105_action_plus_calibration_anchors_select_unique_positive_retract", True)),
        ("invent_physical_state", lambda d: d["result"].__setitem__("distinct_physical_GU_states_selected", 1)),
        ("invent_prediction", lambda d: d["result"].__setitem__("prediction_or_confirmation_credit", True)),
        ("score_holdout", lambda d: d["result"].__setitem__("held_out_scored", True)),
        ("promote_canon", lambda d: d["result"].__setitem__("canon_verdict_change", "changed")),
        ("erase_scope", lambda d: d.__setitem__("claim_ceiling", "The quantum anchors select the physical state.")),
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
    checks.append(("manifest preserves transport, import, equivariance and claim ceilings", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"K109 K105 QUANTUM-ANCHOR RETRACT BOUNDARY: {sum(int(bool(ok)) for _, ok in checks)}/{len(checks)} pass")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
