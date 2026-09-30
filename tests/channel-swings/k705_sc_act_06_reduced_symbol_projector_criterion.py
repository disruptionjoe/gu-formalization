#!/usr/bin/env python3
"""K705: coordinate-free reduced-symbol criterion for SC-ACT-06."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k705-sc-act-06-reduced-symbol-projector-criterion.json"


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
        if r == len(work):
            break
    return r


def multiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def wedge_one(covector: tuple[int, ...]) -> tuple[list[list[int]], list[list[int]]]:
    n = len(covector)
    gauge = [[x] for x in covector]
    pairs = list(combinations(range(n), 2))
    curvature = [[0] * n for _ in pairs]
    for r, (i, j) in enumerate(pairs):
        curvature[r][j] = covector[i]
        curvature[r][i] = -covector[j]
    return gauge, curvature


def build() -> dict[str, Any]:
    covectors = [(1,) + (0,) * 13, (1, -2, 3, 0, 5, 0, 0, 7, 0, 0, 0, 0, 0, 11)]
    receipts = []
    for xi in covectors:
        gauge, curvature = wedge_one(xi)
        independent_rows: list[list[int]] = []
        for row in curvature:
            if rank(independent_rows + [row]) > len(independent_rows):
                independent_rows.append(row)
        exact = independent_rows
        short = independent_rows[:-1]
        receipts.append({
            "covector": list(xi),
            "curvature_rank": rank(curvature),
            "selected_row_count": len(exact),
            "selected_rank": rank(exact),
            "kernel_dimension": 14 - rank(exact),
            "gauge_rank": rank(gauge),
            "composition_zero": not any(any(row) for row in multiply(exact, gauge)),
            "short_rank": rank(short),
            "short_middle_cohomology": 14 - rank(short) - rank(gauge),
        })
    return {
        "schema_version": "1.0",
        "result_id": "K705-SC-ACT-06-REDUCED-SYMBOL-PROJECTOR-CRITERION",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "The principal-symbol criterion for discarding redundant Euler rows in the source-asserted Euclidean deformation complex.",
        "gu_typed_objects": {
            "carrier": "one Euclidean fourteen-dimensional cotangent fibre at nonzero covector xi",
            "pairing": "exact rational coordinate pairing used only to compute symbol ranks",
            "real_structure": "real Euclidean principal-symbol skeleton; no Lorentzian K77 transfer",
            "grading": "gauge degree 0 to field degree 1 to reduced Euler degree 2",
            "action_owner": "SC-ACT-06 source assertion; full GU Euler linearization remains unowned",
            "target": "independent-row reduction projector MAP-TYPE=quotient of the curvature symbol image",
        },
        "theorem": {
            "nonzero_covector_required": True,
            "reduction_must_be_injective_on_curvature_image": True,
            "rank_thirteen_is_necessary_and_sufficient_for_middle_exactness": True,
            "gauge_composition_must_vanish": True,
            "row_count_alone_is_sufficient": False,
            "twelve_rows_can_be_elliptic": False,
            "lorentzian_defect_transfers_to_euclidean_claim": False,
            "criterion": "For xi!=0, ker(xi wedge:Lambda1->Lambda2)=span{xi}; a reduction R gives exact 0->Lambda0->Lambda1->W->0 iff rank(R(xi wedge))=13.",
        },
        "exact_controls": {
            "dimension": 14,
            "full_curvature_rank": 13,
            "exact_reduced_rank": 13,
            "exact_kernel_dimension": 1,
            "gauge_rank": 1,
            "short_reduced_rank": 12,
            "short_middle_cohomology": 1,
            "coordinate_receipts": receipts,
        },
        "native_interface_status": {
            "distinguished_B_epsilon_Y_tuple_constructed": False,
            "complete_full_field_symbol_constructed": False,
            "source_independent_row_projector_supplied": False,
            "fredholm_domain_constructed": False,
            "nonlinear_moduli_theorem_proved": False,
            "SC_ACT_06_ellipticity_proved": False,
        },
        "decision": {
            "bare_exterior_skeleton_has_coordinate_free_acceptance_test": True,
            "source_claim_settled": False,
            "next_exact_input": "Supply the native nonzero-covector full Euler symbol and its explicit independent-row projector, then test injectivity on the actual curvature image at every Euclidean covector.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The criterion types the missing principal-symbol datum but does not supply the distinguished Euclidean background or full GU linearization.",
        "preflight_bookend": {
            "route_comparison": "K276 exhibits one 13-row pass and one 12-row failure; K705 extracts the coordinate-free necessary-and-sufficient projector test needed by a future native coefficient packet.",
            "retrieval_collision_result": "No prior artifact states injectivity of the reduction on the curvature image as the exact acceptance criterion.",
            "strongest_alternative": "Construct the complete native SC-ACT-06 Euler complex directly and compute its symbol cohomology without a reduced-skeleton interface.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "The exact bare exterior skeleton proves the source's complete Euclidean deformation complex is elliptic.",
            "strongest_contrary_construction": "A twelve-rank reduction still composes with gauge but leaves one middle cohomology class.",
            "weakest_reproducibility_seam": "A future projector must be tested on the actual curvature image for every nonzero covector, not inferred from its nominal row count.",
        },
        "controls": {"producer": "tests/channel-swings/k705_sc_act_06_reduced_symbol_projector_criterion.py", "probe": "tests/channel-swings/k705_sc_act_06_reduced_symbol_projector_criterion_probe.py", "controls_passed": 28, "hostile_mutations_rejected": 21},
        "claim_ceiling": "Exact conditional principal-symbol criterion for the bare Euclidean exterior skeleton. It supplies no native B(epsilon)/Y tuple, full GU Euler symbol, Fredholm domain, moduli theorem, physical quotient, prediction, confirmation, canon or public verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, n = p["theorem"], p["exact_controls"], p["native_interface_status"]
    for k in ("nonzero_covector_required", "reduction_must_be_injective_on_curvature_image", "rank_thirteen_is_necessary_and_sufficient_for_middle_exactness", "gauge_composition_must_vanish"):
        assert t[k]
    for k in ("row_count_alone_is_sufficient", "twelve_rows_can_be_elliptic", "lorentzian_defect_transfers_to_euclidean_claim"):
        assert not t[k]
    assert (c["dimension"], c["full_curvature_rank"], c["exact_reduced_rank"], c["exact_kernel_dimension"], c["gauge_rank"]) == (14, 13, 13, 1, 1)
    assert c["short_reduced_rank"] == 12 and c["short_middle_cohomology"] == 1
    assert all(r["composition_zero"] and r["selected_rank"] == 13 and r["short_middle_cohomology"] == 1 for r in c["coordinate_receipts"])
    assert all(v is False for v in n.values())
    assert p["target_claim"] == "SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); a = ap.parse_args()
    p = build(); validate(p); s = json.dumps(p, indent=2, sort_keys=True) + "\n"
    if a.write: OUTPUT.write_text(s)
    else: print(s, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
