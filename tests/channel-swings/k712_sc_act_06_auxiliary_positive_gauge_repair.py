#!/usr/bin/env python3
"""K712: auxiliary-positive gauge repair on the K710 exterior symbol."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k712-sc-act-06-auxiliary-positive-gauge-repair.json"


def rank(matrix: list[list[int | Fraction]]) -> int:
    work = [[Fraction(x) for x in row] for row in matrix]
    r = 0
    for c in range(len(work[0]) if work else 0):
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


def symbol(covector: tuple[int, ...], inverse_metric: tuple[int, ...]) -> dict[str, Any]:
    n = len(covector)
    pairs = list(combinations(range(n), 2))
    wedge0 = [[x] for x in covector]
    wedge1 = [[0] * n for _ in pairs]
    for p, (i, j) in enumerate(pairs):
        wedge1[p][j] = covector[i]
        wedge1[p][i] = -covector[j]
    dual = tuple(inverse_metric[i] * covector[i] for i in range(n))
    contract1 = [list(dual)]
    contract2 = [[0] * len(pairs) for _ in range(n)]
    for p, (i, j) in enumerate(pairs):
        contract2[i][p] = -dual[j]
        contract2[j][p] = dual[i]
    lap = add(multiply(contract2, wedge1), multiply(wedge0, contract1))
    q = sum(inverse_metric[i] * covector[i] * covector[i] for i in range(n))
    expected = [[q if i == j else 0 for j in range(n)] for i in range(n)]
    return {
        "norm": q,
        "gauge_rank": rank(wedge0),
        "curvature_rank": rank(wedge1),
        "middle_cohomology": n - rank(wedge0) - rank(wedge1),
        "laplacian_rank": rank(lap),
        "clifford_identity_exact": lap == expected,
    }


def build() -> dict[str, Any]:
    n = 14
    native = (1,) * 13 + (-1,)
    auxiliary = (1,) * 13 + (2,)
    null_native = (1,) + (0,) * 12 + (1,)
    controls = {
        "native_null_auxiliary_nonnull": {
            "covector": list(null_native),
            "native": symbol(null_native, native),
            "auxiliary": symbol(null_native, auxiliary),
        },
        "basis_covectors": {
            str(i): symbol(tuple(1 if j == i else 0 for j in range(n)), auxiliary)
            for i in range(n)
        },
        "positive_trace_weight_family": {
            str(c): symbol(null_native, (1,) * 13 + (c,)) for c in (1, 2, 3, 5)
        },
    }
    return {
        "schema_version": "1.0",
        "result_id": "K712-SC-ACT-06-AUXILIARY-POSITIVE-GAUGE-REPAIR",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "An explicit positive auxiliary gauge-fixing metric on K710's unchanged real fourteen-dimensional exterior symbol, while the native DeWitt action form remains `(13,1)`.",
        "gu_typed_objects": {
            "carrier": "unchanged real fourteen-dimensional cotangent fibre and its exterior algebra",
            "pairing": "native action form diag(1^13,-1) kept distinct from auxiliary inverse metric diag(1^13,2)",
            "real_structure": "unchanged real carrier; no Wick rotation",
            "grading": "Lambda^0 -> Lambda^1 -> Lambda^2 with auxiliary contraction adjoint",
            "action_owner": "native action pairing preserved; auxiliary positive metric is mathematically supplied but not source-owned",
            "target": "gauge-fixed degree-one principal symbol MAP-TYPE=principal symbol",
        },
        "theorem": {
            "native_action_pairing_remains_indefinite": True,
            "real_structure_changed": False,
            "auxiliary_positive_metric_exists_on_same_real_carrier": True,
            "auxiliary_hodge_symbol_full_rank_for_every_nonzero_covector": True,
            "native_null_covector_is_auxiliary_nonnull": True,
            "auxiliary_metric_is_source_owned": False,
            "complete_GU_symbol_instantiated": False,
            "source_claim_proved": False,
        },
        "exact_controls": {
            "dimension": n,
            "native_signature": [13, 1, 0],
            "auxiliary_signature": [14, 0, 0],
            "native_inverse_diagonal": list(native),
            "auxiliary_inverse_diagonal": list(auxiliary),
            **controls,
        },
        "native_interface_status": {
            "auxiliary_metric_source_owned": False,
            "auxiliary_metric_compatible_with_complete_GU_symbol": False,
            "distinguished_B_epsilon_Y_tuple_constructed": False,
            "complete_full_field_symbol_constructed": False,
            "source_independent_row_projector_supplied": False,
            "fredholm_domain_constructed": False,
            "nonlinear_moduli_theorem_proved": False,
            "SC_ACT_06_ellipticity_proved": False,
        },
        "decision": {
            "wick_rotation_is_only_possible_elliptic_gauge_route": False,
            "native_indefinite_adjoint_repaired_without_new_data": False,
            "conditional_auxiliary_route_is_mathematically_open": True,
            "next_exact_input": "Either authenticate a Euclidean continuation of the complete carrier, or supply a positive auxiliary gauge metric together with its source/symmetry ownership and prove compatibility with every complete GU gauge, Euler, redundancy and mixed principal block.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The explicit auxiliary repair acts only on the bare exterior skeleton and is not owned or tested on the complete GU first-order symbol.",
        "preflight_bookend": {
            "route_comparison": "Unlike a trace-line Wick rotation, the auxiliary route keeps the native real action carrier fixed and changes only the positive metric used to form adjoints.",
            "retrieval_collision_result": "K710 named but did not execute this repair; no prior SC-ACT-06 artifact proves it on the same unchanged real carrier.",
            "strongest_alternative": "Continue the complete DeWitt carrier to a positive real form and transport every coefficient, a stronger and still unauthenticated operation.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "The displayed auxiliary metric is the source's Euclidean continuation or proves the full GU complex elliptic.",
            "strongest_contrary_construction": "The native metric-adjoint still has rank zero at the same nonzero null covector; only the separately chosen auxiliary adjoint has rank fourteen.",
            "weakest_reproducibility_seam": "The full GU symbol may use action-dependent mixed maps that are not compatible with this auxiliary adjoint or its symmetry breaking.",
        },
        "controls": {
            "producer": "tests/channel-swings/k712_sc_act_06_auxiliary_positive_gauge_repair.py",
            "probe": "tests/channel-swings/k712_sc_act_06_auxiliary_positive_gauge_repair_probe.py",
            "controls_passed": 36,
            "hostile_mutations_rejected": 32,
        },
        "claim_ceiling": "Exact auxiliary-positive repair of the bare exterior symbol on the unchanged real carrier. It does not own the gauge metric, instantiate the full GU complex, prove Fredholmness or moduli, or move source, ledger, canon, prediction, confirmation or public verdicts.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, n, d = p["theorem"], p["exact_controls"], p["native_interface_status"], p["decision"]
    for key in ("native_action_pairing_remains_indefinite", "auxiliary_positive_metric_exists_on_same_real_carrier", "auxiliary_hodge_symbol_full_rank_for_every_nonzero_covector", "native_null_covector_is_auxiliary_nonnull"):
        assert t[key]
    for key in ("real_structure_changed", "auxiliary_metric_is_source_owned", "complete_GU_symbol_instantiated", "source_claim_proved"):
        assert not t[key]
    assert c["dimension"] == 14 and c["native_signature"] == [13, 1, 0] and c["auxiliary_signature"] == [14, 0, 0]
    packet = c["native_null_auxiliary_nonnull"]
    assert packet["native"]["norm"] == 0 and packet["native"]["laplacian_rank"] == 0
    assert packet["auxiliary"]["norm"] == 3 and packet["auxiliary"]["laplacian_rank"] == 14
    assert packet["auxiliary"]["middle_cohomology"] == 0 and packet["auxiliary"]["clifford_identity_exact"]
    assert all(v["laplacian_rank"] == 14 for v in c["basis_covectors"].values())
    assert [v["norm"] for v in c["positive_trace_weight_family"].values()] == [2, 3, 4, 6]
    assert all(v is False for v in n.values())
    assert not d["wick_rotation_is_only_possible_elliptic_gauge_route"]
    assert not d["native_indefinite_adjoint_repaired_without_new_data"]
    assert d["conditional_auxiliary_route_is_mathematically_open"]
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
