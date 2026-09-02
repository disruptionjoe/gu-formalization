#!/usr/bin/env python3
"""Exact K152 A2+A0 curved-gauge Noether completion.

The finite certificate evaluates the complete K152 differential bridge on the
Lie derivative of its own Ricci-flat normal-coordinate metric germ.  Vector
field monomials through degree three exhaust the jet of this order-three
composition.  The separately frozen A0-times-principal-gauge failure is kept
as a required nonvacuity control.
"""
from __future__ import annotations

import copy
import hashlib
import json
import math
from itertools import product
from pathlib import Path
import sys

import sympy as sp

import k150_moving_selected_shiab_coordinate_adapter as K150
import k152_curved_metric_bridge_adapter as K152
import k105_k155_carrier_weyl_action_bv_green_probe as K105


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k106-k152-gauge-completed-a2-a0-owner-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k106-k152-gauge-completed-a2-a0-owner-wave-2026-09-02.md"
EXPECTED_RAW_A0_DIGEST = "7967815e29bdd29f9c017936f5653fb24855b550c3b6495d298f788eaaa1b083"


def normal_metric_germ(
    curvature: dict[tuple[int, int, int, int], sp.Expr],
    coordinates: tuple[sp.Symbol, ...],
) -> sp.ImmutableMatrix:
    """Quadratic normal-coordinate germ with zero third metric jet."""
    metric = sp.Matrix(K152.ETA4)
    for mu, nu, a, b in product(range(4), repeat=4):
        metric[mu, nu] += (
            sp.Rational(1, 2)
            * K152.normal_metric_twojet(curvature, mu, nu, a, b)
            * coordinates[a]
            * coordinates[b]
        )
    return sp.ImmutableMatrix(metric.applyfunc(sp.expand))


def normalized_monomial(
    coordinates: tuple[sp.Symbol, ...], alpha: tuple[int, ...]
) -> sp.Expr:
    value = sp.Integer(1)
    for coordinate, power in zip(coordinates, alpha):
        value *= coordinate**power / math.factorial(power)
    return value


def multiindices(maximum_degree: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        alpha
        for alpha in product(range(maximum_degree + 1), repeat=4)
        if sum(alpha) <= maximum_degree
    )


def lie_metric(
    metric: sp.MatrixBase,
    vector: tuple[sp.Expr, ...],
    coordinates: tuple[sp.Symbol, ...],
    *,
    include_transport: bool = True,
) -> sp.ImmutableMatrix:
    output = sp.zeros(4)
    for mu in range(4):
        for nu in range(4):
            transported = sum(
                vector[rho] * sp.diff(metric[mu, nu], coordinates[rho])
                for rho in range(4)
            ) if include_transport else 0
            output[mu, nu] = sp.expand(
                transported
                + sum(
                    metric[rho, nu] * sp.diff(vector[rho], coordinates[mu])
                    + metric[mu, rho] * sp.diff(vector[rho], coordinates[nu])
                    for rho in range(4)
                )
            )
    return sp.ImmutableMatrix(output)


def derivative_at_origin(
    expression: sp.Expr,
    alpha: tuple[int, ...],
    coordinates: tuple[sp.Symbol, ...],
    origin: dict[sp.Symbol, int],
) -> sp.Expr:
    value = expression
    for coordinate, power in zip(coordinates, alpha):
        if power:
            value = sp.diff(value, coordinate, power)
    return sp.expand(value.subs(origin))


def apply_bridge_at_origin(
    bridge: K152.CurvedMetricBridge,
    metric_variation: sp.MatrixBase,
    origin: dict[sp.Symbol, int],
    *,
    coefficient_orders: tuple[int, ...] = (0, 2),
) -> sp.SparseMatrix:
    variation = tuple(
        metric_variation[mu, nu] for mu, nu in K152.METRIC_SLOTS
    )
    output = sp.SparseMatrix.zeros(bridge.density_dual.output_dimension, 1)
    for alpha, coefficient in bridge.density_dual.coefficients.items():
        if sum(alpha) not in coefficient_orders:
            continue
        jet = sp.Matrix(
            [
                derivative_at_origin(value, alpha, bridge.coordinates, origin)
                for value in variation
            ]
        )
        output += sp.SparseMatrix(sp.Matrix(coefficient).subs(origin)) * jet
    return sp.SparseMatrix(output)


def embed_bridge(
    packet: object, bridge: K152.CurvedMetricBridge
) -> sp.SparseMatrix:
    packet_index = {entry: index for index, entry in enumerate(packet.basis)}
    embedding = sp.MutableSparseMatrix(packet.dimension, len(bridge.basis), {})
    for column, entry in enumerate(bridge.basis):
        embedding[packet_index[entry], column] = 1
    return sp.SparseMatrix(embedding)


def build_certificate() -> dict[str, object]:
    coordinates = sp.symbols("x0:4", real=True)
    origin = dict.fromkeys(coordinates, 0)
    curvature = K152.weyl_from_electric(sp.diag(sp.Rational(1, 2), sp.Rational(1, 2), -1))
    metric = normal_metric_germ(curvature, coordinates)
    generator = K150.bivector(0, 4)
    bridge = K152.build_curved_metric_bridge(
        curvature, coordinates, (generator, {}, {}, {}), 2
    )
    frozen = K105.build_fixture()
    embedding = embed_bridge(frozen["packet"], bridge)

    jet_results: dict[int, list[sp.SparseMatrix]] = {degree: [] for degree in range(4)}
    for alpha in multiindices(3):
        monomial = normalized_monomial(coordinates, alpha)
        for component in range(4):
            vector = tuple(monomial if rho == component else sp.Integer(0) for rho in range(4))
            variation = lie_metric(metric, vector, coordinates)
            jet_results[sum(alpha)].append(
                apply_bridge_at_origin(bridge, variation, origin)
            )

    n = (sp.Integer(1), sp.Rational(3, 5), sp.Integer(0), sp.Rational(4, 5))
    phase = sum(value * coordinate for value, coordinate in zip(n, coordinates))
    truncated_exponential = sum(phase**degree / math.factorial(degree) for degree in range(4))
    raw_columns = []
    prolonged_columns = []
    incomplete_columns = []
    for lower_component in range(4):
        contravariant = tuple(
            K152.ETA4[rho, lower_component] * truncated_exponential
            for rho in range(4)
        )
        variation = lie_metric(metric, contravariant, coordinates)
        raw = apply_bridge_at_origin(
            bridge, variation, origin, coefficient_orders=(0,)
        )
        prolonged = apply_bridge_at_origin(
            bridge, variation, origin, coefficient_orders=(2,)
        )
        raw_columns.append(raw)
        prolonged_columns.append(prolonged)
        incomplete = lie_metric(
            metric, contravariant, coordinates, include_transport=False
        )
        incomplete_columns.append(
            apply_bridge_at_origin(bridge, incomplete, origin)
        )

    raw_matrix = sp.SparseMatrix.hstack(*raw_columns)
    prolonged_matrix = sp.SparseMatrix.hstack(*prolonged_columns)
    incomplete_matrix = sp.SparseMatrix.hstack(*incomplete_columns)
    embedded_zero = embedding * sp.SparseMatrix(bridge.zero_order(origin))
    return {
        "bridge": bridge,
        "metric": metric,
        "curvature": curvature,
        "frozen": frozen,
        "embedding": embedding,
        "jet_results": jet_results,
        "raw_matrix": raw_matrix,
        "prolonged_matrix": prolonged_matrix,
        "incomplete_matrix": incomplete_matrix,
        "embedded_zero": embedded_zero,
    }


def exact_checks(certificate: dict[str, object]) -> list[tuple[str, bool]]:
    bridge = certificate["bridge"]
    metric = certificate["metric"]
    curvature = certificate["curvature"]
    frozen = certificate["frozen"]
    jet_results = certificate["jet_results"]
    raw_matrix = certificate["raw_matrix"]
    prolonged_matrix = certificate["prolonged_matrix"]
    incomplete_matrix = certificate["incomplete_matrix"]
    embedded_zero = certificate["embedded_zero"]
    zero112x4 = sp.zeros(112, 4)
    metric_twojet_replays = all(
        sp.diff(metric[mu, nu], bridge.coordinates[a], bridge.coordinates[b]).subs(
            dict.fromkeys(bridge.coordinates, 0)
        )
        == K152.normal_metric_twojet(curvature, mu, nu, a, b)
        for mu, nu, a, b in product(range(4), repeat=4)
    )
    ricci_zero = all(
        sp.simplify(
            sum(
                K152.ETA4[a, r] * curvature.get((a, mu, r, nu), 0)
                for a, r in product(range(4), repeat=2)
            )
        ) == 0
        for mu, nu in product(range(4), repeat=2)
    )
    all_jets_zero = {
        degree: all(value == sp.zeros(112, 1) for value in values)
        for degree, values in jet_results.items()
    }
    raw_a0 = sp.SparseMatrix(frozen["raw_a0"])
    gauge = sp.Matrix(frozen["gauge"])
    return [
        ("the aligned background curvature is Ricci flat", ricci_zero),
        ("the metric germ is normal through first order", metric.subs(dict.fromkeys(bridge.coordinates, 0)) == K152.ETA4 and all(sp.diff(metric, coordinate).subs(dict.fromkeys(bridge.coordinates, 0)) == sp.zeros(4) for coordinate in bridge.coordinates)),
        ("the metric two-jet exactly replays the K152 curvature germ", metric_twojet_replays),
        ("the chosen formal background third metric jet is zero", all(sp.diff(metric, *axes).subs(dict.fromkeys(bridge.coordinates, 0)) == sp.zeros(4) for axes in product(bridge.coordinates, repeat=3))),
        ("the K152 bridge has only differential orders two and zero", {sum(alpha) for alpha in bridge.density_dual.coefficients} == {0, 2}),
        ("the bridge output embeds injectively from 112 into 448 directions", certificate["embedding"].shape == (448, 112) and certificate["embedding"].rank() == 112),
        ("the embedded zero-order coefficient equals the separately frozen raw A0", embedded_zero == raw_a0),
        ("the raw K152 A0 digest remains frozen", K105.sparse_digest(raw_a0) == EXPECTED_RAW_A0_DIGEST),
        ("the raw K152 A0 retains rank nine and 24 entries", raw_a0.rank() == 9 and raw_a0.nnz() == 24),
        ("the frozen principal gauge retains rank four", gauge.rank() == 4),
        ("standalone raw A0 times the frozen gauge retains rank four", (raw_a0 * gauge).rank() == 4),
        ("constant vector-field jets give zero complete Noether composition", all_jets_zero[0]),
        ("linear vector-field jets give zero complete Noether composition", all_jets_zero[1]),
        ("quadratic vector-field jets give zero complete Noether composition", all_jets_zero[2]),
        ("cubic vector-field jets give zero complete Noether composition", all_jets_zero[3]),
        ("all 140 vector-field jets through degree three are exhausted", sum(len(values) for values in jet_results.values()) == 140),
        ("the raw A0 gauge contribution is nonvacuous rank four", raw_matrix.rank() == 4),
        ("the A2 curvature/prolongation contribution is nonvacuous rank four", prolonged_matrix.rank() == 4),
        ("the A2 prolongation cancels raw A0 exactly", raw_matrix + prolonged_matrix == zero112x4),
        ("omitting Lie transport leaves a nonzero planted defect", incomplete_matrix != zero112x4),
        ("the full differential completion does not alter the K155 rank-one correction", frozen["coefficient"].rank() == 1),
    ]


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    exact = data.get("exact_result", {})
    action = data.get("action_owner", {})
    controls = data.get("controls", {})
    result = data.get("result", {})
    fences = data.get("fences", {})
    if exact.get("vector_field_jet_dimension") != 140 or exact.get("complete_Noether_composition_rank") != 0:
        failures.append("jet_certificate")
    if exact.get("raw_A0_rank") != 9 or exact.get("raw_A0_times_frozen_gauge_rank") != 4:
        failures.append("raw_A0")
    if exact.get("A2_prolongation_rank") != 4 or exact.get("A2_plus_A0_gauge_composition_rank") != 0:
        failures.append("cancellation")
    if action.get("H_times_R_zero") is not True or action.get("free_classical_BV_CME") is not True:
        failures.append("action")
    if controls.get("omit_Lie_transport_is_nonzero") is not True or controls.get("K155_verdict_changed") is not False:
        failures.append("controls")
    if result.get("raw_A0_differential_owner_constructed") is not True or result.get("standalone_raw_A0_admitted") is not False:
        failures.append("result")
    if any(value is not False for value in fences.values()):
        failures.append("fences")
    return failures


def artifact_failures(text: str) -> list[str]:
    required = (
        "GU-COMPARATOR-ROUTING — scope before inference.",
        "Classification: `SOURCE_NATIVE_ROUTE`.",
        "```gu-typed-objects",
        "## Inline preflight bookend",
        "## Inline postflight bookend",
        "claim_ceiling:",
        "target_claim:",
        "canon_verdict_change: none",
    )
    return [marker for marker in required if marker not in text]


def selftest(data: dict, certificate: dict[str, object]) -> int:
    artifact = ARTIFACT.read_text()
    baseline = exact_checks(certificate)
    if not all(ok for _, ok in baseline) or manifest_failures(data) or artifact_failures(artifact):
        print("BASELINE RED: hostile selftest refused")
        return 1
    mutations: list[tuple[str, bool]] = [
        ("freeze_gauge", (certificate["frozen"]["raw_a0"] * certificate["frozen"]["gauge"]).rank() == 4),
        ("omit_Lie_transport", certificate["incomplete_matrix"] != sp.zeros(112, 4)),
    ]
    updates = (
        ("wrong_jet_dimension", lambda d: d["exact_result"].__setitem__("vector_field_jet_dimension", 139)),
        ("invent_Noether_rank", lambda d: d["exact_result"].__setitem__("complete_Noether_composition_rank", 1)),
        ("wrong_A0_rank", lambda d: d["exact_result"].__setitem__("raw_A0_rank", 1)),
        ("erase_frozen_failure", lambda d: d["exact_result"].__setitem__("raw_A0_times_frozen_gauge_rank", 0)),
        ("erase_A2_rank", lambda d: d["exact_result"].__setitem__("A2_prolongation_rank", 0)),
        ("break_cancellation", lambda d: d["exact_result"].__setitem__("A2_plus_A0_gauge_composition_rank", 4)),
        ("drop_action_Noether", lambda d: d["action_owner"].__setitem__("H_times_R_zero", False)),
        ("drop_CME", lambda d: d["action_owner"].__setitem__("free_classical_BV_CME", False)),
        ("erase_transport_plant", lambda d: d["controls"].__setitem__("omit_Lie_transport_is_nonzero", False)),
        ("move_K155", lambda d: d["controls"].__setitem__("K155_verdict_changed", True)),
        ("drop_owner", lambda d: d["result"].__setitem__("raw_A0_differential_owner_constructed", False)),
        ("admit_standalone_A0", lambda d: d["result"].__setitem__("standalone_raw_A0_admitted", True)),
        ("promote_source", lambda d: d["fences"].__setitem__("authenticated_Weinstein_source_action", True)),
        ("promote_global", lambda d: d["fences"].__setitem__("global_curved_action", True)),
        ("promote_physics", lambda d: d["fences"].__setitem__("physical_state_or_Born_owner", True)),
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
    certificate = build_certificate()
    if "--selftest" in sys.argv:
        return selftest(data, certificate)
    checks = exact_checks(certificate)
    checks.append(("manifest preserves the exact owner and claim ceiling", not manifest_failures(data)))
    checks.append(("artifact preserves governance fields and both bookends", not artifact_failures(ARTIFACT.read_text())))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"K106 K152 GAUGE-COMPLETED A2+A0 OWNER: {sum(ok for _, ok in checks)}/{len(checks)} pass")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
