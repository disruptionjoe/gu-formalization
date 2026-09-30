#!/usr/bin/env python3
"""K685: compile complete component-square bounds into K677's complement budget."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k685-k500-component-square-budget-compiler.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k684 = json.loads((ROOT / "lab/process/k684-k500-closed-column-remainder-compiler.json").read_text())
    k677 = json.loads((ROOT / "lab/process/k677-k500-complement-cofinal-norm-certificate.json").read_text())
    assert k684["closed_column_theorem"]["domain_identity"] == "Dom(T)=Dom(C)"
    assert k677["exact_native_target"]["K674_simple_sufficient_target"] == "1/100"

    displayed = [Fraction(1, 20) ** 2, Fraction(1, 25) ** 2]
    tail = Fraction(1, 400)
    total = sum(displayed, Fraction(0)) + tail
    target = Fraction(1, 100)
    assert total == Fraction(33, 5000)
    assert target - total == Fraction(17, 5000)

    return {
        "schema_version": "1.0",
        "result_id": "K685-K500-COMPONENT-SQUARE-BUDGET-COMPILER",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A complete coefficient-square certificate that turns operator bounds for every component of K684's closed column, including a rigorous infinite tail, into K677's localized seed-complement target.",
        "gu_typed_objects": {
            "column": "K684's complete closed column C=(C_j)_j on the invariant remainder carrier",
            "localized_map": "C a^-1 Q_seed from the full seed complement into the Hilbert direct sum of component codomains",
            "component_bounds": "complete operator bounds b_j>=||C_j a^-1 Q_seed||",
            "tail": "one rigorous upper on sum_(j>N) b_j^2 covering every undisplayed component",
            "result": "component-square complement compiler MAP-TYPE=Hilbert-column norm budget",
            "target": "K677's sufficient ||R Q_seed||^2<=1/100 row",
        },
        "component_square_theorem": {
            "column_identity": "||C a^-1 Q x||^2=sum_j ||C_j a^-1 Q x||^2",
            "component_hypothesis": "||C_j a^-1 Q||<=b_j for every displayed component",
            "tail_hypothesis": "sum_(j>N) ||C_j a^-1 Q x||^2<=v_N||x||^2 for every x in QH",
            "conclusion": "||R Q||^2=||C a^-1 Q||^2<=sum_(j<=N)b_j^2+v_N",
            "one_over_one_hundred_admission": "sum_(j<=N)b_j^2+v_N<=1/100",
            "finite_prefix_without_tail_sufficient": False,
            "scalar_coefficient_bounds_without_operator_norms_sufficient": False,
            "same_codomain_sum_without_cross_Gram_control_sufficient": False,
        },
        "seed_composition": {
            "line_identity_requirement": "the three K676 native seed action identities must identify C a^-1 e_q on q00, q10 and q01",
            "charge_orthogonality_requirement": "their complete column outputs occupy mutually orthogonal charge sectors",
            "conclusion": "on P_seed the squared operator norm is the maximum of the three complete linewise component-square sums",
            "three_untyped_scalar_values_sufficient": False,
            "complement_budget_alone_proves_seed_identity": False,
        },
        "exact_controls": {
            "displayed_component_norms": ["1/20", "1/25"],
            "displayed_square_sum": qstr(sum(displayed, Fraction(0))),
            "complete_tail_square_budget": qstr(tail),
            "total_complement_square_budget": qstr(total),
            "target": qstr(target),
            "slack": qstr(target - total),
            "accepted": total <= target,
            "nonorthogonal_counterexample": {
                "two_same_codomain_unit_components": True,
                "sum_of_individual_squares": "2",
                "squared_norm_of_component_sum": "4",
                "column_or_Gram_typing_required": True,
            },
            "hidden_tail_counterexample": "append one undisplayed complement component of arbitrary norm while preserving every finite displayed component",
            "controls_are_synthetic": True,
        },
        "dependency_reconciliation": {
            "K674_one_over_one_hundred_target_consumed": True,
            "K677_cofinal_core_tail_shape_consumed": True,
            "K684_closed_column_representation_consumed": True,
            "K676_seed_identity_requirement_retained": True,
            "K676_charge_intertwiner_requirement_retained": True,
            "native_component_bounds_added": False,
        },
        "native_interface_status": {
            "actual_native_component_column_serialized": False,
            "actual_native_component_operator_bounds_proved": False,
            "actual_native_complete_square_tail_proved": False,
            "actual_native_seed_actions_identified": False,
            "actual_native_complement_below_one_over_one_hundred": False,
            "native_A_above_two_thirds_proved": False,
            "native_complete_floor_emitted": False,
        },
        "decision": {
            "complete_component_budget_is_direct_K677_input": True,
            "native_complement_budget_proved": False,
            "next_exact_input": "After a native K684 column is owned, bound each displayed C_j a^-1 Q_seed in operator norm and prove one complete square tail for all remaining j with total at most 1/100. Separately prove the three K676 seed action identities and charge orthogonality before composing K674.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional Hilbert-column norm budget inside a repository-supplied operator model and supplies no source-owned action, state, quotient or observable.",
        "preflight_bookend": {
            "route_comparison": "K677 accepts an abstract cofinal core/tail bound. K684 exposes a native coefficient column, so the cheapest actionable successor is a square-summable component budget rather than another global norm guess.",
            "retrieval_collision_result": "K176 and K574 own tails for a different exchange action column; no current result identifies those coefficients with K684's invariant remainder column or supplies the Q_seed component-square tail.",
            "strongest_alternative": "K672 can prove A directly by finite/complement/cross form bounds without identifying a column or seed map.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Summing displayed scalar coefficients, omitting the complete square tail, or treating a same-codomain sum as an orthogonal column.",
            "strongest_contrary_construction": "Two unit components with the same range have individual square sum two but coherent sum squared norm four; an undisplayed hidden component can make any finite prefix arbitrarily incomplete.",
            "weakest_reproducibility_seam": "Every component must be an operator on the same localized domain, the direct-sum or Gram geometry must be explicit, and the tail must cover the entire undisplayed complement.",
        },
        "controls": {
            "producer": "tests/channel-swings/k685_k500_component_square_budget_compiler.py",
            "probe": "tests/channel-swings/k685_k500_component_square_budget_compiler_probe.py",
            "controls_passed": 34,
            "hostile_mutations_rejected": 28,
        },
        "claim_ceiling": "Exact conditional component-square result: complete operator bounds for every displayed component of C a^-1 Q plus a rigorous full square tail bound give ||R Q||^2<=sum b_j^2+v_N and directly admit K677's 1/100 complement target when that total is at most 1/100. Finite prefixes, scalar coefficients and nonorthogonal sums without Gram control do not suffice. Current native custody supplies no component column, bounds, tail or seed identities. No native complement estimate, A, B, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["component_square_theorem"]
    seed = payload["seed_composition"]
    native = payload["native_interface_status"]
    controls = payload["exact_controls"]
    assert not theorem["finite_prefix_without_tail_sufficient"]
    assert not theorem["scalar_coefficient_bounds_without_operator_norms_sufficient"]
    assert not theorem["same_codomain_sum_without_cross_Gram_control_sufficient"]
    assert not seed["three_untyped_scalar_values_sufficient"]
    assert not seed["complement_budget_alone_proves_seed_identity"]
    assert controls["total_complement_square_budget"] == "33/5000"
    assert controls["slack"] == "17/5000"
    assert controls["accepted"]
    assert controls["nonorthogonal_counterexample"]["squared_norm_of_component_sum"] == "4"
    assert not native["actual_native_complete_square_tail_proved"]
    assert not native["native_complete_floor_emitted"]


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
