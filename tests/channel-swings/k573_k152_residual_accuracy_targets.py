#!/usr/bin/env python3
"""K573 exact best-gap residual targets for K469/K470."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k573-k152-residual-accuracy-targets.json"
K570 = ROOT / "lab/process/k570-complete-m-dual-residual-enclosure.json"


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def sci(value: Fraction) -> str:
    with localcontext() as ctx:
        ctx.prec = 20
        number = Decimal(value.numerator) / Decimal(value.denominator)
        return f"{number:.12E}"


def residual_upper() -> Fraction:
    data = json.loads(K570.read_text())
    return Fraction(data["complete_M_dual_residual_norm_square"]["interval_exact"][1])


def ground_row(upper: Fraction, gap: Fraction, deficit: Fraction) -> dict:
    budget = deficit * (gap + deficit)
    return {
        "target_ground_deficit": q(deficit),
        "best_gap_residual_square_budget": q(budget),
        "current_upper_passes": upper <= budget,
        "required_upper_improvement_factor_exact": q(upper / budget),
        "required_upper_improvement_factor_scientific": sci(upper / budget),
    }


def projection_row(upper: Fraction, gap: Fraction, sine: Fraction) -> dict:
    budget = sine**2 * gap**2 / (1 - sine**2) ** 2
    return {
        "target_projection_sine": q(sine),
        "best_gap_residual_square_budget": q(budget),
        "current_upper_passes": upper <= budget,
        "required_upper_improvement_factor_exact": q(upper / budget),
        "required_upper_improvement_factor_scientific": sci(upper / budget),
    }


def build() -> dict:
    upper = residual_upper()
    gap = Fraction(5, 2)
    ground = [ground_row(upper, gap, value) for value in (Fraction(1), Fraction(1, 2), Fraction(1, 10))]
    projection = [projection_row(upper, gap, value) for value in (Fraction(1, 2), Fraction(1, 3), Fraction(1, 10))]
    return {
        "schema_version": "1.0",
        "result_id": "K573-K152-RESIDUAL-ACCURACY-TARGETS",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact K469/K470 residual-square target table at K169's most favorable admissible 5/2 relative gap, using K570's complete M-dual upper only as the current certificate baseline.",
        "gu_typed_objects": {
            "result": "complete-residual accuracy target compiler MAP-TYPE=decision-budget",
            "carrier": "one fixed complete K162 charge sector",
            "pairing": "positive physical metric M=S* S",
            "form": "fixed K139/K168 reference form",
            "target": "future cancellation-aware residual or action-flux certificate",
        },
        "inputs": {
            "K169_best_admissible_relative_gap": q(gap),
            "K570_current_complete_M_dual_square_upper_exact": q(upper),
            "K570_current_complete_M_dual_square_upper_scientific": "2.48890514834555913e+2347",
            "upper_is_not_actual_residual_lower": True,
        },
        "ground_deficit_targets": ground,
        "projection_targets": projection,
        "controls": {
            "ground_budgets_exact": [row["best_gap_residual_square_budget"] for row in ground],
            "projection_budgets_exact": [row["best_gap_residual_square_budget"] for row in projection],
            "all_current_targets_fail": all(not row["current_upper_passes"] for row in ground + projection),
            "budgets_tighten_with_accuracy": all(
                Fraction(left["best_gap_residual_square_budget"]) > Fraction(right["best_gap_residual_square_budget"])
                for rows in (ground, projection)
                for left, right in zip(rows, rows[1:])
            ),
        },
        "decision": {
            "quantitative_K466_shift_is_priority_for_residual_accuracy": False,
            "complete_floor_alone_can_rescue_current_K570_upper": False,
            "residual_or_flux_accuracy_must_move_by_over_10_to_2346": True,
            "complete_reference_specific_floor_still_required": True,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Replace the global absolute-value Peano residual ceiling with cancellation-aware coherent evaluation or an action-flux certificate whose complete error is below the target table, while completing K494/K500's reference-specific floor. The exact first milestone is residual square <=25/9 for projection sine <=1/2 at the best possible gap.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact decision budgets only. At the most favorable native gap allowed by K169, the current K570 upper would need to improve by more than 10^2346 even for the loosest named ground/projection targets. The table does not lower-bound the actual residual, prove that a future complete floor exists, emit K152, or change source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusions.",
    }


def validate(payload: dict) -> None:
    controls = payload["controls"]
    decision = payload["decision"]
    if not payload["inputs"]["upper_is_not_actual_residual_lower"]:
        raise AssertionError("K573 lost the upper-bound distinction")
    if not controls["all_current_targets_fail"] or not controls["budgets_tighten_with_accuracy"]:
        raise AssertionError("K573 target table failed")
    if decision["quantitative_K466_shift_is_priority_for_residual_accuracy"]:
        raise AssertionError("K573 reversed K571")
    if decision["complete_floor_alone_can_rescue_current_K570_upper"]:
        raise AssertionError("K573 ignored K572")
    if not decision["residual_or_flux_accuracy_must_move_by_over_10_to_2346"]:
        raise AssertionError("K573 lost the measured target gap")
    if decision["native_K152_interval_emitted"]:
        raise AssertionError("K573 overclaimed native closure")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
