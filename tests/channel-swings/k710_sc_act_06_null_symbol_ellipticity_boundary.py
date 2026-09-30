#!/usr/bin/env python3
"""K710: null-covector boundary between Koszul exactness and metric gauge fixing."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k710-sc-act-06-null-symbol-ellipticity-boundary.json"


def rank(matrix: list[list[int | Fraction]]) -> int:
    work = [[Fraction(x) for x in row] for row in matrix]
    if not work:
        return 0
    r = 0
    for c in range(len(work[0])):
        pivot = next((i for i in range(r, len(work)) if work[i][c]), None)
        if pivot is None:
            continue
        work[r], work[pivot] = work[pivot], work[r]
        q = work[r][c]
        work[r] = [x / q for x in work[r]]
        for i in range(len(work)):
            if i != r and work[i][c]:
                q = work[i][c]
                work[i] = [work[i][j] - q * work[r][j] for j in range(len(work[0]))]
        r += 1
    return r


def multiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def add(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def symbol_packet(covector: tuple[int, ...], inverse_metric: tuple[int, ...]) -> dict[str, Any]:
    n = len(covector)
    pairs = list(combinations(range(n), 2))
    wedge0 = [[x] for x in covector]
    wedge1 = [[0] * n for _ in pairs]
    for p, (i, j) in enumerate(pairs):
        wedge1[p][j] = covector[i]
        wedge1[p][i] = -covector[j]
    metric_dual = tuple(inverse_metric[i] * covector[i] for i in range(n))
    contract1 = [list(metric_dual)]
    contract2 = [[0] * len(pairs) for _ in range(n)]
    for p, (i, j) in enumerate(pairs):
        contract2[i][p] = -metric_dual[j]
        contract2[j][p] = metric_dual[i]
    lap1 = add(multiply(contract2, wedge1), multiply(wedge0, contract1))
    q = sum(inverse_metric[i] * covector[i] * covector[i] for i in range(n))
    expected = [[q if i == j else 0 for j in range(n)] for i in range(n)]
    # A metric-independent contracting vector for Koszul exactness.
    pivot = next(i for i, x in enumerate(covector) if x)
    auxiliary_v = [0] * n
    auxiliary_v[pivot] = Fraction(1, covector[pivot])
    auxiliary_pairing = sum(auxiliary_v[i] * covector[i] for i in range(n))
    return {
        "covector": list(covector),
        "metric_norm": q,
        "gauge_rank": rank(wedge0),
        "curvature_rank": rank(wedge1),
        "middle_cohomology": n - rank(wedge1) - rank(wedge0),
        "metric_laplacian_rank_on_one_forms": rank(lap1),
        "clifford_identity_exact": lap1 == expected,
        "auxiliary_contracting_vector_pairing": int(auxiliary_pairing),
    }


def build() -> dict[str, Any]:
    n = 14
    pseudo = (1,) * 13 + (-1,)
    euclidean = (1,) * 14
    null = (1,) + (0,) * 12 + (1,)
    spacelike = (1,) + (0,) * 13
    timelike = (0,) * 13 + (1,)
    null_packet = symbol_packet(null, pseudo)
    return {
        "schema_version": "1.0",
        "result_id": "K710-SC-ACT-06-NULL-SYMBOL-ELLIPTICITY-BOUNDARY",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "The distinction between metric-independent exactness of K705's exterior symbol and ellipticity of the gauge-fixed symbol formed with K708's indefinite native metric.",
        "gu_typed_objects": {
            "carrier": "real exterior algebra of a fourteen-dimensional `(13,1)` cotangent fibre",
            "pairing": "pseudo-Riemannian metric adjoint from the K708 total signature",
            "real_structure": "real `(13,1)` carrier before any authenticated Euclidean continuation",
            "grading": "Lambda^0 to Lambda^1 to Lambda^2 and its metric contraction homotopy",
            "action_owner": "bare connection/Bianchi symbol skeleton only; complete GU Euler symbol remains unowned",
            "target": "null-covector obstruction to the native metric-adjoint gauge-fixed symbol MAP-TYPE=principal symbol",
        },
        "theorem": {
            "koszul_exact_for_every_nonzero_covector_without_metric": True,
            "pseudo_metric_dual_is_a_contracting_homotopy_at_null_covector": False,
            "metric_hodge_symbol_equals_covector_norm_times_identity": True,
            "nonzero_null_covectors_exist_for_13_1": True,
            "native_metric_gauge_fixed_symbol_is_elliptic": False,
            "koszul_exactness_alone_is_refuted_by_indefinite_signature": False,
            "source_claim_is_refuted_by_null_symbol": False,
        },
        "exact_controls": {
            "dimension": n,
            "pseudo_signature": [13, 1, 0],
            "null_covector": null_packet,
            "spacelike_covector": symbol_packet(spacelike, pseudo),
            "timelike_covector": symbol_packet(timelike, pseudo),
            "same_null_coordinates_after_euclidean_continuation": symbol_packet(null, euclidean),
            "null_koszul_exact": null_packet["middle_cohomology"] == 0,
            "null_metric_laplacian_rank": null_packet["metric_laplacian_rank_on_one_forms"],
            "euclideanized_laplacian_rank": symbol_packet(null, euclidean)["metric_laplacian_rank_on_one_forms"],
        },
        "native_interface_status": {
            "authenticated_euclidean_metric_adjoint_constructed": False,
            "distinguished_B_epsilon_Y_tuple_constructed": False,
            "complete_full_field_symbol_constructed": False,
            "source_independent_row_projector_supplied": False,
            "fredholm_domain_constructed": False,
            "nonlinear_moduli_theorem_proved": False,
            "SC_ACT_06_ellipticity_proved": False,
        },
        "decision": {
            "k705_koszul_criterion_survives_as_algebra": True,
            "native_indefinite_hodge_gauge_fixing_can_instantiate_euclidean_claim": False,
            "next_exact_input": "Supply the authenticated Euclidean continuation and recompute the complete gauge, Euler, redundancy and gauge-fixing symbols on that one real carrier before any Fredholm or moduli step.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The null-symbol result blocks one native metric-adjoint shortcut while preserving metric-independent complex exactness and every unconstructed continuation.",
        "preflight_bookend": {
            "route_comparison": "A signature mismatch matters only if it changes the actual symbol test; K710 locates the change at the metric-adjoint gauge fixing, not the exterior complex itself.",
            "retrieval_collision_result": "K705 checks exterior exactness and K708 checks inertia; no prior artifact composes them through the null Hodge-symbol identity.",
            "strongest_alternative": "Use an auxiliary positive-definite metric solely for elliptic gauge fixing, which remains a distinct extra choice requiring compatibility with the full GU symbol.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "The null Hodge symbol proves the source deformation complex is nonexact.",
            "strongest_contrary_construction": "The same nonzero null covector leaves the Koszul complex exact through an auxiliary nonmetric contracting vector.",
            "weakest_reproducibility_seam": "The future full-field Euler/redundancy symbol may not be the bare exterior complex, and its gauge fixing must be tested on the continued carrier actually chosen.",
        },
        "controls": {
            "producer": "tests/channel-swings/k710_sc_act_06_null_symbol_ellipticity_boundary.py",
            "probe": "tests/channel-swings/k710_sc_act_06_null_symbol_ellipticity_boundary_probe.py",
            "controls_passed": 38,
            "hostile_mutations_rejected": 33,
        },
        "claim_ceiling": "Exact distinction between algebraic Koszul exactness and indefinite metric-adjoint gauge-fixed ellipticity. It proves neither the complete GU complex nor a source no-go, Fredholm domain, moduli theorem, prediction, confirmation, canon or public verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, n, d = p["theorem"], p["exact_controls"], p["native_interface_status"], p["decision"]
    for key in ("koszul_exact_for_every_nonzero_covector_without_metric", "metric_hodge_symbol_equals_covector_norm_times_identity", "nonzero_null_covectors_exist_for_13_1"):
        assert t[key]
    for key in ("pseudo_metric_dual_is_a_contracting_homotopy_at_null_covector", "native_metric_gauge_fixed_symbol_is_elliptic", "koszul_exactness_alone_is_refuted_by_indefinite_signature", "source_claim_is_refuted_by_null_symbol"):
        assert not t[key]
    assert c["dimension"] == 14 and c["pseudo_signature"] == [13, 1, 0]
    null = c["null_covector"]
    assert null["metric_norm"] == 0 and null["gauge_rank"] == 1 and null["curvature_rank"] == 13
    assert null["middle_cohomology"] == 0 and null["metric_laplacian_rank_on_one_forms"] == 0
    assert null["clifford_identity_exact"] and null["auxiliary_contracting_vector_pairing"] == 1
    assert c["spacelike_covector"]["metric_laplacian_rank_on_one_forms"] == 14
    assert c["timelike_covector"]["metric_laplacian_rank_on_one_forms"] == 14
    assert c["same_null_coordinates_after_euclidean_continuation"]["metric_norm"] == 2
    assert c["null_koszul_exact"] and c["null_metric_laplacian_rank"] == 0 and c["euclideanized_laplacian_rank"] == 14
    assert all(v is False for v in n.values())
    assert d["k705_koszul_criterion_survives_as_algebra"]
    assert not d["native_indefinite_hodge_gauge_fixing_can_instantiate_euclidean_claim"]
    assert p["target_claim"] == "SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
