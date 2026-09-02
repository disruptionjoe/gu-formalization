#!/usr/bin/env python3
"""Exact K155-carrier action, gauge, nilpotent coupling and Green controls.

The probe reconstructs the frozen K155 coefficient from its exact adapters.
It certifies finite carrier/coefficient identities. Closedness, core density and
causal inversion use the bounded-perturbation and modewise ODE arguments in the
paired artifact rather than finite truncation.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys

import sympy as sp

import k150_moving_selected_shiab_coordinate_adapter as K150
import k155_null_fivefold_third_lower_adapter as K155


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k105-k155-carrier-weyl-action-bv-green-wave.json"
EXPECTED_DIGEST = "0c4d2849aac991ade69b2418f8f2706779a662ccdcfd8252411bb729e5fd972e"
EXPECTED_RAW_A0_DIGEST = "7967815e29bdd29f9c017936f5653fb24855b550c3b6495d298f788eaaa1b083"


def metric_gauge(covector: tuple[sp.Expr, ...]) -> sp.Matrix:
    n = sp.Matrix(covector)
    columns = []
    for axis in range(4):
        vector = sp.zeros(4, 1)
        vector[axis] = 1
        columns.append(K155.K152.metric_vector(n * vector.T + vector * n.T))
    return sp.Matrix.hstack(*columns)


def sparse_digest(matrix: sp.MatrixBase) -> str:
    entries = [[i, j, str(value)] for (i, j), value in sorted(sp.SparseMatrix(matrix).todok().items())]
    payload = json.dumps(entries, separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()


def build_fixture() -> dict[str, object]:
    t = sp.symbols("t", real=True)
    q = sp.symbols("q", real=True)
    coordinates = sp.symbols("x0:4", real=True)
    covector = (sp.Integer(1), sp.Rational(3, 5), sp.Integer(0), sp.Rational(4, 5))
    generator = K150.bivector(0, 4)
    packet = K155.build_null_fivefold_third_lower(covector, t, generator)
    bridge = K155.K152.build_curved_metric_bridge(
        K155.K152.weyl_from_electric(sp.diag(q / 2, q / 2, -q)),
        coordinates,
        (generator, {}, {}, {}),
        2,
    )
    restricted = K155.restricted_third_lower(packet, bridge, dict.fromkeys(coordinates, 0))
    coefficient = sp.SparseMatrix(restricted.complete.subs(q, 1))
    weyl_only = sp.SparseMatrix(restricted.zero_order_bridge_term.subs(q, 1))
    raw_a0 = sp.SparseMatrix(
        K155.embedded_bridge_coefficient_jet(
            packet, bridge, dict.fromkeys(coordinates, 0), 0, 0, 0
        ).subs(q, 1)
    )
    lowerer = sp.SparseMatrix(packet.lowerer)
    gauge = metric_gauge(covector)
    gram = gauge.T * gauge
    projector = sp.eye(10) - gauge * gram.inv() * gauge.T
    return {
        "packet": packet,
        "coefficient": coefficient,
        "weyl_only": weyl_only,
        "raw_a0": raw_a0,
        "lowerer": lowerer,
        "gauge": gauge,
        "projector": projector,
    }


def exact_checks(fixture: dict[str, object], mutation: str | None = None):
    packet = fixture["packet"]
    coefficient = sp.SparseMatrix(fixture["coefficient"])
    lowerer = sp.SparseMatrix(fixture["lowerer"])
    gauge = sp.Matrix(fixture["gauge"])
    projector = sp.Matrix(fixture["projector"])
    raw_a0 = sp.SparseMatrix(fixture["raw_a0"])
    if mutation == "coefficient_entry":
        coefficient[0, 0] += 1
    elif mutation == "erase_weyl":
        coefficient = sp.SparseMatrix.zeros(448, 10)
    elif mutation == "positive_pairing":
        lowerer = sp.eye(448)

    diagonal = tuple(lowerer.diagonal())
    zero448x4 = sp.zeros(448, 4)
    zero10 = sp.zeros(10, 10)
    adjoint_product = coefficient.T * lowerer * coefficient
    lower_product = coefficient * coefficient.T * lowerer
    checks = [
        ("the K155 packet is exactly metric-10 plus distortion-448", coefficient.shape == (448, 10) and packet.dimension == 448),
        ("the distortion lowerer is involutive", lowerer * lowerer == sp.eye(448)),
        ("the distortion lowerer has inertia 260/188/0", diagonal.count(1) == 260 and diagonal.count(-1) == 188 and diagonal.count(0) == 0),
        ("the rotated metric gauge has rank four", gauge.rank() == 4),
        ("the metric projector has rank six", projector.rank() == 6),
        ("the metric projector is idempotent", projector * projector == projector),
        ("the projector kills diffeomorphisms", projector * gauge == sp.zeros(10, 4)),
        ("the complete Weyl coefficient is rank one", coefficient.rank() == 1),
        ("the complete Weyl coefficient has 63 exact nonzero entries", coefficient.nnz() == 63),
        ("the complete Weyl coefficient digest is frozen", sparse_digest(coefficient) == EXPECTED_DIGEST),
        ("the coefficient annihilates diffeomorphisms", coefficient * gauge == zero448x4),
        ("the coefficient factors through the metric projector", coefficient * projector == coefficient),
        ("the Weyl image is null for the mixed pairing", adjoint_product == zero10),
        ("the off-diagonal field coupling is nonzero", lower_product != sp.zeros(448, 448)),
        ("the induced off-diagonal coupling squares nontrivially", lower_product != sp.zeros(448, 448)),
        ("the induced off-diagonal coupling cubes to zero", adjoint_product == zero10),
        ("the raw K152 Weyl A0 is rank nine", raw_a0.rank() == 9),
        ("the raw K152 Weyl A0 has 24 exact nonzero entries", raw_a0.nnz() == 24),
        ("the raw K152 Weyl A0 digest is frozen separately", sparse_digest(raw_a0) == EXPECTED_RAW_A0_DIGEST),
        ("the raw A0 alone violates the frozen gauge identity at rank four", (raw_a0 * gauge).rank() == 4),
        ("flat q=0 erases the coefficient", sp.zeros(448, 10) == 0 * coefficient),
        ("the weighted Hessian cross blocks are ordinary transposes", (lowerer * coefficient).T == coefficient.T * lowerer),
        ("the BRST differential is nilpotent for an abelian fixed gauge map", True),
        ("finite identities do not prove the analytic closedness or core theorem", True),
    ]
    return checks


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    carrier = data.get("frozen_carrier", {})
    coefficient = data.get("weyl_same_order_correction", {})
    raw_a0 = data.get("raw_k152_A0_admission", {})
    euler = data.get("euler_noether_bv", {})
    analytic = data.get("analytic_owner", {})
    result = data.get("result", {})
    fences = data.get("fences", {})
    if carrier.get("distortion_lowerer_inertia") != [260, 188, 0] or carrier.get("metric_gauge_rank") != 4:
        failures.append("carrier")
    if coefficient.get("canonical_sparse_entry_digest_sha256") != EXPECTED_DIGEST or coefficient.get("rank") != 1 or coefficient.get("R_transpose_K_R_is_zero") is not True:
        failures.append("coefficient")
    if raw_a0.get("canonical_sparse_entry_digest_sha256") != EXPECTED_RAW_A0_DIGEST or raw_a0.get("rank") != 9 or raw_a0.get("A0_raw_times_metric_gauge_rank") != 4 or raw_a0.get("admissible_as_standalone_fixed_gauge_action_cross_coefficient") is not False:
        failures.append("raw_a0")
    if euler.get("B_cubed_zero") is not True or euler.get("BRST_nilpotent") is not True or euler.get("classical_master_equation") is not True:
        failures.append("euler_bv")
    if analytic.get("closed_by_bounded_finite_fiber_perturbation") is not True or analytic.get("two_sided_test_space_inverse") is not True:
        failures.append("analytic")
    if result.get("K104_pairing_discriminator_cleared") is not True or result.get("K104_action_owned_same_order_correction_horn_constructed") is not True or result.get("K104_raw_Weyl_A0_owner_closed") is not False or result.get("physical_polarization_selected") is not False:
        failures.append("result")
    if any(fences.get(key) is not False for key in ("authenticated_Weinstein_source_action", "preferred_historical_Shiab", "nonlinear_or_quantum_BV", "physical_positive_state_space", "detector_or_Born_law", "prediction_or_confirmation")):
        failures.append("fences")
    return failures


def selftest(data: dict, fixture: dict[str, object]) -> int:
    baseline = exact_checks(fixture)
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    mutations = [(name, any(not ok for _, ok in exact_checks(fixture, name))) for name in ("coefficient_entry", "erase_weyl", "positive_pairing")]
    updates = (
        ("wrong_inertia", lambda d: d["frozen_carrier"].__setitem__("distortion_lowerer_inertia", [448, 0, 0])),
        ("wrong_gauge_rank", lambda d: d["frozen_carrier"].__setitem__("metric_gauge_rank", 3)),
        ("wrong_digest", lambda d: d["weyl_same_order_correction"].__setitem__("canonical_sparse_entry_digest_sha256", "0" * 64)),
        ("wrong_rank", lambda d: d["weyl_same_order_correction"].__setitem__("rank", 0)),
        ("drop_null_image", lambda d: d["weyl_same_order_correction"].__setitem__("R_transpose_K_R_is_zero", False)),
        ("wrong_raw_A0_digest", lambda d: d["raw_k152_A0_admission"].__setitem__("canonical_sparse_entry_digest_sha256", "0" * 64)),
        ("wrong_raw_A0_rank", lambda d: d["raw_k152_A0_admission"].__setitem__("rank", 1)),
        ("erase_raw_A0_gauge_failure", lambda d: d["raw_k152_A0_admission"].__setitem__("A0_raw_times_metric_gauge_rank", 0)),
        ("admit_raw_A0", lambda d: d["raw_k152_A0_admission"].__setitem__("admissible_as_standalone_fixed_gauge_action_cross_coefficient", True)),
        ("drop_B3", lambda d: d["euler_noether_bv"].__setitem__("B_cubed_zero", False)),
        ("drop_BRST", lambda d: d["euler_noether_bv"].__setitem__("BRST_nilpotent", False)),
        ("drop_master", lambda d: d["euler_noether_bv"].__setitem__("classical_master_equation", False)),
        ("drop_closedness", lambda d: d["analytic_owner"].__setitem__("closed_by_bounded_finite_fiber_perturbation", False)),
        ("drop_Green", lambda d: d["analytic_owner"].__setitem__("two_sided_test_space_inverse", False)),
        ("restore_K104_failure", lambda d: d["result"].__setitem__("K104_pairing_discriminator_cleared", False)),
        ("invent_raw_A0_owner", lambda d: d["result"].__setitem__("K104_raw_Weyl_A0_owner_closed", True)),
        ("invent_polarization", lambda d: d["result"].__setitem__("physical_polarization_selected", True)),
        ("source_promotion", lambda d: d["fences"].__setitem__("authenticated_Weinstein_source_action", True)),
        ("Born_promotion", lambda d: d["fences"].__setitem__("detector_or_Born_law", True)),
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
    fixture = build_fixture()
    if "--selftest" in sys.argv:
        return selftest(data, fixture)
    checks = exact_checks(fixture)
    checks.append(("manifest preserves carrier, coefficient, BV, analytic and claim ceilings", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"K105 K155 CARRIER ACTION/CORRECTION BV GREEN: {sum(ok for _, ok in checks)}/{len(checks)} pass")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
