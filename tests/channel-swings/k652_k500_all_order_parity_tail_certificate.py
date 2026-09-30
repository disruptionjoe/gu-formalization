#!/usr/bin/env python3
"""K652: all-order cancellation-preserving parity-tail certificate."""

from __future__ import annotations

import argparse
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k652-k500-all-order-parity-tail-certificate.json"


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


K651 = load("k651_for_k652", "k651_k500_parity_tail_prefix_nonidentifiability.py")


def row_floor(a: Fraction, d: Fraction, kappa: Fraction) -> Fraction:
    return min(a - kappa, d - kappa)


def exact_rows(
    name: str,
    a: Callable[[int], Fraction],
    d: Callable[[int], Fraction],
    kappa: Callable[[int], Fraction],
    tail: Fraction,
) -> dict[str, Any]:
    rows = []
    for n in (1, 2, 4, 8, 32, 128):
        value = row_floor(a(n), d(n), kappa(n))
        rows.append({
            "n": n,
            "a_lower": str(a(n)),
            "d_lower": str(d(n)),
            "kappa_upper": str(kappa(n)),
            "row_floor": str(value),
            "at_least_declared_tail": value >= tail,
        })
    return {"sign": name, "declared_tail": str(tail), "rows": rows}


def build() -> dict[str, Any]:
    k651 = K651.build()
    plus = exact_rows(
        "+",
        lambda n: Fraction(2) + Fraction(1, n),
        lambda n: Fraction(3) + Fraction(1, n),
        lambda n: Fraction(1, n + 1),
        Fraction(2),
    )
    minus = exact_rows(
        "-",
        lambda n: Fraction(5, 2) + Fraction(1, n + 2),
        lambda n: Fraction(7, 4) + Fraction(1, n),
        lambda n: Fraction(1, 2 * (n + 1)),
        Fraction(7, 4),
    )
    return {
        "schema_version": "1.0",
        "result_id": "K652-K500-ALL-ORDER-PARITY-TAIL-CERTIFICATE",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A sufficient all-order same-domain certificate for the independent K650 plus/minus tails after K651 rules out finite-prefix extrapolation.",
        "gu_typed_objects": {
            "carrier": "each K643 bath sector and K648 total-parity sign, split into K650's two complete cancelled quadrants",
            "diagonal_forms": "complete cancelled-quadrant forms with lower functions A_s(n),D_s(n)",
            "cross_form": "relative complete-form coupling rho_s(n)<=1 plus residual Hilbert coupling kappa_s(n)",
            "domain": "one common K647/K650 graph form domain in every certified sector",
            "result": "all-order parity-tail certificate MAP-TYPE=asymptotic form comparison",
            "target": "t_plus,t_minus and the finite-prefix composition required by K646/K650",
        },
        "all_order_tail_theorem": {
            "hypotheses": [
                "a_s,n>=A_s(n) and d_s,n>=D_s(n) on the complete cancelled quadrants",
                "0<=rho_s,n<=1 on the same form domain",
                "0<=kappa_s,n<=K_s(n) for the residual Hilbert coupling",
            ],
            "sector_row_floor": "g_s,n>=min(A_s(n)-K_s(n),D_s(n)-K_s(n))",
            "sector_sharp_floor": "ell_s,n>=lambda_min([[A_s(n),-K_s(n)],[-K_s(n),D_s(n)]])",
            "tail_definition": "t_s=min(inf_(n>N)(A_s(n)-K_s(n)),inf_(n>N)(D_s(n)-K_s(n)))",
            "tail_conclusion": "inf_(n>N) ell_s,n>=t_s",
            "finite_prefix_composition": "m>=min(min_(n<=N,s)ell_s,n,t_plus,t_minus)",
            "rho_endpoint_allowed": True,
            "separately_singular_raw_rows_required": False,
            "all_order_hypotheses_required": True,
            "finite_prefix_alone_sufficient": False,
        },
        "asymptotic_corollaries": {
            "liminf_rule": "if liminf A_s>=A_s*, liminf D_s>=D_s*, and limsup K_s<=K_s*, then every epsilon>0 has an eventual tail at least min(A_s*-K_s*,D_s*-K_s*)-epsilon",
            "coercive_growth_rule": "if min(A_s(n),D_s(n))-K_s(n) tends to +infinity, the parity tail is eventually arbitrarily positive",
            "bounded_tail_rule": "uniform lower bounds A_s,D_s and a uniform residual upper K_s give t_s>=min(A_s-K_s,D_s-K_s)",
            "relative_energy_not_charged_twice": True,
        },
        "exact_controls": {
            "synthetic_not_native": True,
            "plus": plus,
            "minus": minus,
            "global_declared_tail": "7/4",
            "all_rows_pass": all(
                row["at_least_declared_tail"]
                for block in (plus, minus)
                for row in block["rows"]
            ),
        },
        "decision": {
            "K651_prefix_obstruction_consumed": k651["decision"]["orders_two_through_twelve_are_not_a_tail_certificate"],
            "constructive_all_order_route_closed_abstractly": True,
            "native_numeric_tail_emitted": False,
            "next_exact_input": "Derive native all-order A_s(n),D_s(n),K_s(n) on the K647 common domain for both parity signs, with explicit eventual infimum/liminf control; then combine their tails with certified finite sectors and separately prove alpha,delta.",
        },
        "native_interface_status": {
            "all_order_certificate_shape_complete": True,
            "actual_all_order_diagonal_lower_functions_identified": False,
            "actual_all_order_residual_upper_functions_identified": False,
            "actual_uniform_parity_tails_identified": False,
            "native_global_m_identified": False,
            "native_remainder_alpha_delta_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "dependency_reconciliation": {
            "K646_parity_tail_composition_consumed": True,
            "K650_cancelled_quadrant_theorem_consumed": True,
            "K651_finite_prefix_obstruction_consumed": True,
            "K644_raw_route_retracted": False,
            "K612_custody_obstruction_retracted": False,
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is an abstract sufficient theorem for a conditional internal operator form; its controls are synthetic and supply no action-owned physical quotient, state, observable or source mechanism.",
        "preflight_bookend": {
            "route_comparison": "After K651, another finite prefix cannot close the tail. The shortest constructive repair is an all-order form inequality stated directly on K650's cancellation-preserving quadrants.",
            "retrieval_collision_result": "K643 names a uniform tail and K650 names sector constants, but neither turns all-order diagonal/residual envelopes into explicit independent parity tails.",
            "strongest_alternative": "A direct spectral theorem for the full fixed operator would be stronger, but it must still establish at least these same-domain all-order lower controls or an equivalent argument.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Reporting the synthetic 7/4 control as the K139/K168 tail or treating asymptotic hypotheses as already proved.",
            "strongest_contrary_construction": "If K_s overtakes either diagonal lower function along a subsequence, the row tail can fail even though every inspected finite prefix is positive.",
            "weakest_reproducibility_seam": "The theorem is exact but native all-order kernel envelopes remain unserialized; its scientific value is the closed proof obligation, not a numerical result.",
        },
        "claim_ceiling": "Exact all-order cancellation-preserving tail theorem for K650. Native lower functions for the two complete cancelled quadrants and an all-order residual Hilbert-coupling upper give explicit independent total-parity tails through min(A-K,D-K), while rho<=1 is absorbed by the nonnegative complete-form energy. This closes the abstract constructive route after K651's finite-prefix obstruction, but no native A,D,K, t_plus, t_minus, m, alpha or delta is supplied. No K473, K152, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["all_order_tail_theorem"]
    native = payload["native_interface_status"]
    assert theorem["rho_endpoint_allowed"]
    assert not theorem["separately_singular_raw_rows_required"]
    assert theorem["all_order_hypotheses_required"]
    assert not theorem["finite_prefix_alone_sufficient"]
    assert payload["exact_controls"]["all_rows_pass"]
    assert payload["exact_controls"]["global_declared_tail"] == "7/4"
    assert native["all_order_certificate_shape_complete"]
    assert not native["actual_uniform_parity_tails_identified"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
