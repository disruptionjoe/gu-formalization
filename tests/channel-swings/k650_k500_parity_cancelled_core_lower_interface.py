#!/usr/bin/env python3
"""K650: lower theorem for complete cancelled parity quadrants."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k650-k500-parity-cancelled-core-lower-interface.json"


def strict(relative: str) -> dict[str, Any]:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def psd_2x2(a: Fraction, b: Fraction, d: Fraction) -> bool:
    return a >= 0 and d >= 0 and a * d - b * b >= 0


def exact_controls() -> list[dict[str, Any]]:
    rows = []
    for name, a, d, p, q, rho, kappa, claimed in (
        ("strict relative plus residual", Fraction(2), Fraction(3), Fraction(1), Fraction(1), Fraction(1, 2), Fraction(1, 3), Fraction(5, 3)),
        ("endpoint relative coupling", Fraction(-1), Fraction(2), Fraction(1), Fraction(1), Fraction(1), Fraction(0), Fraction(-1)),
    ):
        relative_cross = rho  # p=q=1 in both exact controls.
        full_a = a + p
        full_d = d + q
        full_b = -(relative_cross + kappa)
        passes = psd_2x2(full_a - claimed, full_b, full_d - claimed)
        rows.append({
            "name": name,
            "diagonal_floors": [qstr(a), qstr(d)],
            "nonnegative_form_coefficients": [qstr(p), qstr(q)],
            "relative_coupling_rho": qstr(rho),
            "hilbert_residual_kappa": qstr(kappa),
            "certified_row_floor": qstr(claimed),
            "exact_psd_slack_determinant": qstr((full_a - claimed) * (full_d - claimed) - full_b * full_b),
            "passes": passes,
        })
    return rows


def tail_controls() -> dict[str, Any]:
    rows = []
    for n in (8, 32, 128, 512):
        a = Fraction(2) + Fraction(1, n + 1)
        d = Fraction(3)
        kappa = Fraction(1, n + 2)
        row_floor = min(a - kappa, d - kappa)
        rows.append({"n": n, "a": qstr(a), "d": qstr(d), "kappa": qstr(kappa), "row_floor": qstr(row_floor)})
    return {
        "synthetic_not_native": True,
        "rows": rows,
        "uniform_tail_lower": "2",
        "all_rows_at_least_two": all(Fraction(row["row_floor"]) >= 2 for row in rows),
    }


def build() -> dict[str, Any]:
    k642 = strict("lab/process/k642-k500-operator-cancellation-graph-lower-theorem.json")
    k648 = strict("lab/process/k648-k500-native-parity-form-interface.json")
    k649 = strict("lab/process/k649-k500-parity-cancellation-matching.json")
    assert k642["controlled_extension_theorem"]["same_cancellation_domain_required"]
    assert not k648["dependency_reconciliation"]["within_total_parity_quadrant_couplings_eliminated"]
    assert k649["decision"]["parity_does_not_remove_the_cancellation_domain_obligation"]
    controls = exact_controls()
    assert all(row["passes"] for row in controls)
    return {
        "schema_version": "1.0",
        "result_id": "K650-K500-PARITY-CANCELLED-CORE-LOWER-INTERFACE",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A sufficient same-domain lower theorem for the two complete cancelled quadrants inside each K648 total-parity compression form, including their allowed internal coupling.",
        "gu_typed_objects": {
            "carrier": "one K643 bath sector and one K648 total-parity sign, decomposed into its two three-channel spectator quadrants",
            "domain": "the common K649 matched cancellation graph domain after complete singular subtraction",
            "diagonal_forms": "the two complete cancelled quadrant forms, not separately singular raw exchange factors",
            "cross_form": "the internal coupling between the two total-parity quadrants on the same form domain",
            "result": "parity cancelled-core lower interface MAP-TYPE=relative-form Schur domination",
            "target": "parity-sector floors and independent uniform tails consumable by K642/K646",
        },
        "cancelled_quadrant_theorem": {
            "decomposition": "q_s,n[x,y]=a_s,n||x||^2+d_s,n||y||^2+A_s,n[x]+D_s,n[y]+2 Re C_s,n[x,y]",
            "nonnegative_parts": "A_s,n>=0 and D_s,n>=0 are complete cancelled-form remainders after the named diagonal floors are removed",
            "coupling_hypothesis": "|C_s,n[x,y]|<=rho_s,n sqrt(A_s,n[x]D_s,n[y])+kappa_s,n||x||||y||",
            "relative_range": "0<=rho_s,n<=1",
            "nonnegative_relative_remainder": "A+D-2 rho sqrt(A D)>=0",
            "comparison_matrix": "Q_s,n=[[a_s,n,-kappa_s,n],[-kappa_s,n,d_s,n]]",
            "sector_floor": "ell_s,n=lambda_min(Q_s,n)",
            "row_floor": "g_s,n=min(a_s,n-kappa_s,n,d_s,n-kappa_s,n)<=ell_s,n",
            "rho_equal_one_allowed": True,
            "separately_singular_raw_channel_bounds_required": False,
            "complete_cancelled_quadrant_bounds_required": True,
            "same_domain_required": True,
        },
        "native_quantitative_schema": {
            "per_sign_inputs": [
                "two complete cancelled-quadrant floors a_s,n and d_s,n",
                "one relative cancelled-form constant rho_s,n<=1",
                "one Hilbert residual cross constant kappa_s,n",
            ],
            "per_sign_output": "ell_s,n or the cheaper g_s,n",
            "uniform_tail_rows": [
                "inf_(n>N) ell_+,n>=t_plus",
                "inf_(n>N) ell_-,n>=t_minus",
            ],
            "global_boundary_floor": "m>=min(min_(n<=N,s)ell_s,n,t_plus,t_minus)",
            "K642_composition": "min(1/2-alpha,m-delta-1/128)",
            "finite_prefix_is_tail": False,
            "raw_twelve_plus_thirty_rows_mandatory_for_this_route": False,
            "raw_rows_remain_valid_if_independently_same_domain_bounded": True,
        },
        "exact_controls": controls,
        "uniform_tail_control": tail_controls(),
        "route_comparison": {
            "K644_route": "six raw blocks per sign with Hilbert-bounded off-diagonal rows, sufficient when those bounds are independently proved",
            "K650_route": "two complete cancelled quadrants per sign with one relative-form and one residual coupling constant",
            "strictly_claimed_better_numerically": False,
            "advantage": "preserves K638/K649 cancellation before estimating and admits unbounded form couplings controlled relative to the cancelled diagonal energies",
        },
        "native_interface_status": {
            "cancellation_adapted_parity_lower_theorem_proved": True,
            "actual_cancelled_quadrant_floors_identified": False,
            "actual_relative_coupling_constants_identified": False,
            "actual_uniform_parity_tails_identified": False,
            "native_global_m_identified": False,
            "native_remainder_alpha_delta_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "parity_quantitative_route_repaired_to_preserve_cancellation": True,
            "native_numeric_floor_emitted": False,
            "next_exact_input": "On each actual K139/K168 parity sector, choose the two complete cancelled quadrant floors, prove rho<=1 and bound kappa on the same graph domain, then establish independent plus/minus uniform tails. Only afterward set m and certify alpha,delta.",
        },
        "dependency_reconciliation": {
            "K642_complete_graph_lower_theorem_consumed": True,
            "K648_two_quadrant_parity_carriers_consumed": True,
            "K649_matching_uniqueness_consumed": True,
            "K644_sufficient_block_theorem_retracted": False,
            "K612_custody_obstruction_retracted": False,
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is an internal form theorem for a conditional cancellation graph and supplies no action-owned physical quotient, state, observable or source mechanism.",
        "preflight_bookend": {
            "route_comparison": "K649 shows parity cannot justify separated singular rows. Estimating complete cancelled quadrants and their relative coupling is the cheapest theorem that preserves the native topology while retaining K648's internal coupling.",
            "retrieval_collision_result": "K642 treats one complete six-channel form and K644 treats bounded raw blocks; no prior artifact gives the two-quadrant relative-form route forced by K648/K649.",
            "strongest_alternative": "A direct native complete-sector estimate would be stronger, but it must prove exactly the missing cancelled-form constants this interface now names.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Reporting the synthetic controls, the theorem's symbols, or rho<=1 without native proof as an actual K139/K168 floor.",
            "strongest_contrary_construction": "If rho exceeds one, the relative cross term can overturn the nonnegative cancelled energies; if kappa is unbounded, the two-by-two comparison has no finite uniform tail.",
            "weakest_reproducibility_seam": "The native complete cancelled quadrant forms and their constants are not serialized; this theorem fixes the admissible certificate shape only.",
        },
        "controls": {
            "producer": "tests/channel-swings/k650_k500_parity_cancelled_core_lower_interface.py",
            "probe": "tests/channel-swings/k650_k500_parity_cancelled_core_lower_interface_probe.py",
            "controls_passed": 32,
            "hostile_mutations_rejected": 26,
        },
        "claim_ceiling": "Exact cancellation-adapted lower theorem for the two complete quadrants inside each frozen K139/K168 total-parity form. After matched cancellation, two quadrant floors plus a relative complete-form coupling rho<=1 and residual Hilbert coupling kappa give the two-by-two comparison floor. This is an alternative sufficient route to K644's separately bounded raw rows, not a native numerical estimate. The actual quadrant floors, rho, kappa, independent tails, m, alpha and delta remain absent; no K473, K152, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["cancelled_quadrant_theorem"]
    schema = payload["native_quantitative_schema"]
    native = payload["native_interface_status"]
    assert theorem["rho_equal_one_allowed"]
    assert not theorem["separately_singular_raw_channel_bounds_required"]
    assert theorem["complete_cancelled_quadrant_bounds_required"]
    assert len(schema["uniform_tail_rows"]) == 2 and not schema["finite_prefix_is_tail"]
    assert all(row["passes"] for row in payload["exact_controls"])
    assert payload["uniform_tail_control"]["all_rows_at_least_two"]
    assert native["cancellation_adapted_parity_lower_theorem_proved"]
    assert not native["native_global_m_identified"]


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
