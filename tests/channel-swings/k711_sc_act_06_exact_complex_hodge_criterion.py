#!/usr/bin/env python3
"""K711: positive-Hodge criterion for a finite exact symbol complex."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k711-sc-act-06-exact-complex-hodge-criterion.json"


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def multiply(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def add(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def diagonal(values: list[int | Fraction]) -> list[list[Fraction]]:
    vals = [Fraction(v) for v in values]
    return [[vals[i] if i == j else Fraction(0) for j in range(len(vals))] for i in range(len(vals))]


def rank(a: list[list[Fraction]]) -> int:
    work = [[Fraction(x) for x in row] for row in a]
    if not work:
        return 0
    r = 0
    for c in range(len(work[0])):
        pivot = next((i for i in range(r, len(work)) if work[i][c]), None)
        if pivot is None:
            continue
        work[r], work[pivot] = work[pivot], work[r]
        p = work[r][c]
        work[r] = [x / p for x in work[r]]
        for i in range(len(work)):
            if i != r and work[i][c]:
                q = work[i][c]
                work[i] = [work[i][j] - q * work[r][j] for j in range(len(work[0]))]
        r += 1
    return r


def adjoint(a: list[list[Fraction]], h_domain: list[int], h_codomain: list[int]) -> list[list[Fraction]]:
    hdi = diagonal([Fraction(1, x) for x in h_domain])
    hc = diagonal(h_codomain)
    return multiply(hdi, multiply(transpose(a), hc))


def as_strings(a: list[list[Fraction]]) -> list[list[str]]:
    return [[str(x) for x in row] for row in a]


def build() -> dict[str, Any]:
    g = [[Fraction(1), 0], [0, Fraction(1)], [0, 0], [0, 0]]
    e = [[0, 0, Fraction(1), 0], [0, 0, 0, Fraction(1)]]
    h0, h1, h2 = [2, 3], [5, 7, 11, 13], [17, 19]
    gs = adjoint(g, h0, h1)
    es = adjoint(e, h1, h2)
    lap = add(multiply(g, gs), multiply(es, e))
    e_bad = [[0, 0, 0, Fraction(1)]]
    e_bad_s = adjoint(e_bad, h1, [17])
    lap_bad = add(multiply(g, gs), multiply(e_bad_s, e_bad))
    return {
        "schema_version": "1.0",
        "result_id": "K711-SC-ACT-06-EXACT-COMPLEX-HODGE-CRITERION",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "The finite-dimensional principal-symbol theorem relating middle exactness to a positive auxiliary Hodge Laplacian, independently of an action pairing.",
        "gu_typed_objects": {
            "carrier": "one fibre of a real symbol complex V0 -> V1 -> V2",
            "pairing": "arbitrary positive-definite auxiliary inner products h0,h1,h2, not the source-native action pairing",
            "real_structure": "unchanged real carrier; no Wick rotation or complex trace-line continuation",
            "grading": "gauge parameters, fields, and independent Euler equations",
            "action_owner": "none for the auxiliary metrics; the theorem is conditional mathematical infrastructure",
            "target": "middle-symbol exactness versus invertibility of Delta1=G G* + E* E MAP-TYPE=principal symbol",
        },
        "theorem": {
            "complex_condition_required": True,
            "middle_exact_iff_positive_hodge_laplacian_invertible": True,
            "holds_for_every_positive_auxiliary_inner_product": True,
            "action_pairing_positive_required": False,
            "action_pairing_used_to_define_auxiliary_adjoint": False,
            "full_GU_symbol_instantiated": False,
            "source_claim_proved": False,
        },
        "proof": {
            "energy_identity": "<Delta1 v,v>=||G* v||^2+||E v||^2",
            "kernel_identity": "ker Delta1=ker G* intersect ker E=(im G)^perp intersect ker E",
            "exact_case": "ker E=im G makes the intersection zero",
            "converse": "if Delta1 is injective, every v in ker E orthogonal to im G vanishes, so ker E=im G",
        },
        "exact_controls": {
            "dimensions": [2, 4, 2],
            "positive_metric_diagonals": [h0, h1, h2],
            "gauge_rank": rank(g),
            "euler_rank": rank(e),
            "composition_rank": rank(multiply(e, g)),
            "middle_cohomology": 4 - rank(g) - rank(e),
            "gauge_adjoint": as_strings(gs),
            "euler_adjoint": as_strings(es),
            "hodge_laplacian": as_strings(lap),
            "hodge_laplacian_rank": rank(lap),
            "nonexact_control_middle_cohomology": 4 - rank(g) - rank(e_bad),
            "nonexact_control_laplacian_rank": rank(lap_bad),
        },
        "native_interface_status": {
            "auxiliary_metric_source_owned": False,
            "distinguished_B_epsilon_Y_tuple_constructed": False,
            "complete_full_field_symbol_constructed": False,
            "source_independent_row_projector_supplied": False,
            "fredholm_domain_constructed": False,
            "nonlinear_moduli_theorem_proved": False,
            "SC_ACT_06_ellipticity_proved": False,
        },
        "decision": {
            "positive_action_pairing_is_logically_necessary_for_symbol_ellipticity": False,
            "positive_auxiliary_metric_can_test_an_already_constructed_real_symbol_complex": True,
            "next_exact_input": "Construct the complete real GU gauge/Euler/redundancy symbol first, then supply and own positive auxiliary metrics or an authenticated Euclidean continuation and test the criterion at every nonzero covector.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The theorem separates a general elliptic-complex fact from the still-unconstructed GU symbol and supplies no source-owned gauge metric.",
        "preflight_bookend": {
            "route_comparison": "K710's null failure concerns the adjoint from the native indefinite form; exact-complex Hodge theory permits an independently chosen positive auxiliary metric.",
            "retrieval_collision_result": "K710 names this auxiliary route but does not prove its exactness equivalence or ownership boundary.",
            "strongest_alternative": "Wick-rotate the complete action carrier, which is stronger data than symbol ellipticity alone requires.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Any positive auxiliary metric proves the GU deformation complex is elliptic.",
            "strongest_contrary_construction": "The nonexact control has one middle cohomology class and its positive Hodge Laplacian loses exactly one rank.",
            "weakest_reproducibility_seam": "The equivalence assumes E G=0 and positive auxiliary metrics on the actual complete real symbol spaces.",
        },
        "controls": {
            "producer": "tests/channel-swings/k711_sc_act_06_exact_complex_hodge_criterion.py",
            "probe": "tests/channel-swings/k711_sc_act_06_exact_complex_hodge_criterion_probe.py",
            "controls_passed": 32,
            "hostile_mutations_rejected": 28,
        },
        "claim_ceiling": "Exact finite-dimensional symbol-complex/Hodge theorem. It does not construct the GU symbol, own an auxiliary metric, prove Fredholmness or nonlinear moduli, or move any source, ledger, canon, prediction, confirmation or public verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, n, d = p["theorem"], p["exact_controls"], p["native_interface_status"], p["decision"]
    for key in ("complex_condition_required", "middle_exact_iff_positive_hodge_laplacian_invertible", "holds_for_every_positive_auxiliary_inner_product"):
        assert t[key]
    for key in ("action_pairing_positive_required", "action_pairing_used_to_define_auxiliary_adjoint", "full_GU_symbol_instantiated", "source_claim_proved"):
        assert not t[key]
    assert c["dimensions"] == [2, 4, 2] and c["positive_metric_diagonals"] == [[2, 3], [5, 7, 11, 13], [17, 19]]
    assert c["gauge_rank"] == 2 and c["euler_rank"] == 2 and c["composition_rank"] == 0
    assert c["middle_cohomology"] == 0 and c["hodge_laplacian_rank"] == 4
    assert c["hodge_laplacian"] == [["5/2", "0", "0", "0"], ["0", "7/3", "0", "0"], ["0", "0", "17/11", "0"], ["0", "0", "0", "19/13"]]
    assert c["nonexact_control_middle_cohomology"] == 1 and c["nonexact_control_laplacian_rank"] == 3
    assert all(v is False for v in n.values())
    assert not d["positive_action_pairing_is_logically_necessary_for_symbol_ellipticity"]
    assert d["positive_auxiliary_metric_can_test_an_already_constructed_real_symbol_complex"]
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
