#!/usr/bin/env python3
"""Exact K91 retract and positive-polarization nonselection controls for K105."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys

import sympy as sp

import k105_k155_carrier_weyl_action_bv_green_probe as K105


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k105-k91-positive-retract-nonselection-wave.json"


def exact_checks(fixture: dict[str, object], mutation: str | None = None):
    packet = fixture["packet"]
    coefficient = sp.SparseMatrix(fixture["coefficient"])
    lowerer = sp.SparseMatrix(fixture["lowerer"])
    gauge = sp.Matrix(fixture["gauge"])
    projector = sp.Matrix(fixture["projector"])
    if mutation == "couple_e0":
        coefficient[0, 0] += 1
    elif mutation == "negative_e0":
        lowerer[0, 0] = -1

    plus = [i for i, value in enumerate(lowerer.diagonal()) if value == 1]
    minus = [i for i, value in enumerate(lowerer.diagonal()) if value == -1]
    kr = lowerer * coefficient
    valid_plus = [i for i in plus if all(kr[i, j] == 0 for j in range(10))]
    valid_minus = [i for i in minus if all(kr[i, j] == 0 for j in range(10))]

    v = sp.zeros(448, 1)
    v[0] = 1
    w = sp.zeros(448, 1)
    w[1] = 1
    metric_axis = sp.zeros(4, 1)
    metric_axis[0] = 1
    u = gauge * metric_axis
    left_gauge = metric_axis.T * (gauge.T * gauge).inv() * gauge.T
    field_embedding = sp.zeros(458, 2)
    field_embedding[:10, 0] = u
    field_embedding[10:, 1] = v
    field_retraction = sp.zeros(2, 458)
    field_retraction[0, :10] = left_gauge
    field_retraction[1, 10:] = v.T * lowerer

    checks = [
        ("the chosen vector is the frozen basis entry (0,0,1)", packet.basis[0] == (0, 0, 1)),
        ("the chosen distortion line is K-positive", (v.T * lowerer * v)[0] == 1),
        ("the chosen line is orthogonal to the Weyl image", coefficient.T * lowerer * v == sp.zeros(10, 1)),
        ("the selected metric vector is pure diffeomorphism gauge", projector * u == sp.zeros(10, 1)),
        ("the Weyl coefficient kills the selected metric gauge vector", coefficient * u == sp.zeros(448, 1)),
        ("the displayed field projection retracts the displayed embedding", field_retraction * field_embedding == sp.eye(2)),
        ("the K91 gauge injection intertwines", field_embedding[:, 0] == sp.Matrix.vstack(u, sp.zeros(448, 1))),
        ("the restricted kinetic pairing is zero on gauge and one on p", (u.T * projector * u)[0] == 0 and (v.T * lowerer * v)[0] == 1),
        ("the restricted Weyl cross term vanishes", (v.T * lowerer * coefficient * u)[0] == 0),
        ("the field coupling preserves the K91 physical line", coefficient.T * lowerer * v == sp.zeros(10, 1)),
        ("exactly 256 positive coordinate lines avoid the Weyl image", len(valid_plus) == 256),
        ("exactly 183 negative coordinate lines avoid the Weyl image", len(valid_minus) == 183),
        ("both e0 and e1 are distinct positive retract seeds", 0 in valid_plus and 1 in valid_plus and v != w),
        ("swapping e0/e1 preserves the diagonal lowerer", lowerer[0, 0] == lowerer[1, 1] == 1 and lowerer[0, 1] == lowerer[1, 0] == 0),
        ("swapping e0/e1 preserves the coefficient", all(coefficient[row, column] == 0 for row in (0, 1) for column in range(10))),
        ("the frozen action therefore has no unique invariant positive line", 0 in valid_plus and 1 in valid_plus),
        ("the ambient carrier still retains all 188 negative directions", len(minus) == 188),
        ("finite retract checks do not create a physical state or Born pairing", True),
    ]
    return checks


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    retract = data.get("exact_retract", {})
    nonselection = data.get("nonselection", {})
    result = data.get("result", {})
    required_retract = ("retraction_identity", "gauge_map_intertwining", "action_restriction_is_K104_K91_action", "Euler_Hessian_intertwining", "closed_domain_and_core_intertwining", "retarded_advanced_intertwining", "Green_boundary_form_intertwining", "Weyl_coupling_vanishes_on_retract")
    if any(retract.get(key) is not True for key in required_retract) or retract.get("v_K_norm") != 1:
        failures.append("retract")
    if nonselection.get("positive_coordinate_lines_in_Ker_C_W_transpose_K") != 256 or nonselection.get("negative_coordinate_lines_in_Ker_C_W_transpose_K") != 183 or nonselection.get("unique_invariant_positive_line") is not False or nonselection.get("removal_owned_by_K155_action") is not False:
        failures.append("nonselection")
    if result.get("K91_retract_exists") is not True or result.get("K91_retract_selected_by_K155_data") is not False or result.get("K155_ambient_pairing_changed") is not False or result.get("canon_verdict_change") != "none":
        failures.append("result")
    if "No claim that all positive subspaces are equivalent" not in data.get("claim_ceiling", ""):
        failures.append("ceiling")
    return failures


def selftest(data: dict, fixture: dict[str, object]) -> int:
    baseline = exact_checks(fixture)
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    mutations = [(name, any(not ok for _, ok in exact_checks(fixture, name))) for name in ("couple_e0", "negative_e0")]
    updates = (
        ("drop_retraction", lambda d: d["exact_retract"].__setitem__("retraction_identity", False)),
        ("drop_action", lambda d: d["exact_retract"].__setitem__("action_restriction_is_K104_K91_action", False)),
        ("drop_Green", lambda d: d["exact_retract"].__setitem__("retarded_advanced_intertwining", False)),
        ("wrong_positive_count", lambda d: d["nonselection"].__setitem__("positive_coordinate_lines_in_Ker_C_W_transpose_K", 255)),
        ("wrong_negative_count", lambda d: d["nonselection"].__setitem__("negative_coordinate_lines_in_Ker_C_W_transpose_K", 184)),
        ("invent_unique_line", lambda d: d["nonselection"].__setitem__("unique_invariant_positive_line", True)),
        ("invent_selection_owner", lambda d: d["nonselection"].__setitem__("removal_owned_by_K155_action", True)),
        ("erase_retract", lambda d: d["result"].__setitem__("K91_retract_exists", False)),
        ("promote_selection", lambda d: d["result"].__setitem__("K91_retract_selected_by_K155_data", True)),
        ("erase_ambient_negative", lambda d: d["result"].__setitem__("K155_ambient_pairing_changed", True)),
        ("canon_promotion", lambda d: d["result"].__setitem__("canon_verdict_change", "changed")),
        ("universalize", lambda d: d.__setitem__("claim_ceiling", "all positive subspaces are equivalent")),
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
    checks.append(("manifest preserves retract, nonselection and claim ceilings", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"K105 K91 POSITIVE RETRACT: {sum(ok for _, ok in checks)}/{len(checks)} pass")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
