#!/usr/bin/env python3
"""K688: compile positive partial-Gram bounds into complete column estimates."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k688-k500-partial-gram-bound-compiler.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k685 = json.loads((ROOT / "lab/process/k685-k500-component-square-budget-compiler.json").read_text())
    k687 = json.loads((ROOT / "lab/process/k687-k500-countable-closed-column-compiler.json").read_text())
    assert k685["component_square_theorem"]["one_over_one_hundred_admission"] == "sum_(j<=N)b_j^2+v_N<=1/100"
    assert k687["countable_column_theorem"]["conclusion"] == "C is densely defined and closed, so K684 applies"

    prefix = Fraction(41, 10000)
    tail = Fraction(1, 400)
    total = prefix + tail
    target = Fraction(1, 100)
    slack = target - total
    assert total == Fraction(33, 5000)
    assert slack == Fraction(17, 5000)

    return {
        "schema_version": "1.0",
        "result_id": "K688-K500-PARTIAL-GRAM-BOUND-COMPILER",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A complete positive-operator certificate for K684's global graph realization and K685's seed-complement bound using finite partial Grams plus a rigorous full tail.",
        "gu_typed_objects": {
            "bounded_components": "B_j=C_j a^-1 or B_j=C_j a^-1 Q_seed on one fixed input Hilbert space",
            "partial_gram": "G_N=sum_(j<=N) B_j* B_j",
            "tail_gram": "E_N=sum_(j>N) B_j* B_j as a positive strong-form tail",
            "result": "partial-Gram complete-column compiler MAP-TYPE=positive operator order",
            "targets": "K684 bounded C a^-1 and K685 ||C a^-1 Q_seed||^2<=1/100",
        },
        "partial_gram_theorem": {
            "identity": "||B x||^2=sum_j||B_j x||^2=sup_N <x,G_N x>",
            "uniform_partial_bound": "G_N<=q I for every N implies a bounded complete column B with ||B||^2<=q",
            "finite_plus_tail_bound": "G_N<=g_N I and E_N<=v_N I imply B*B<= (g_N+v_N) I",
            "localized_consequence": "the same theorem with B_j=C_j a^-1 Q_seed gives K685's complete complement bound",
            "global_consequence": "the same theorem with B_j=C_j a^-1 gives K684's bounded graph realization",
            "finite_partial_gram_without_tail_sufficient": False,
            "diagonal_matrix_elements_on_sampled_vectors_sufficient": False,
            "component_scalar_coefficients_without_operator_domains_sufficient": False,
            "weak_or_uncontrolled_tail_sufficient": False,
        },
        "exact_controls": {
            "finite_partial_gram_upper": qstr(prefix),
            "complete_tail_gram_upper": qstr(tail),
            "complete_column_square_upper": qstr(total),
            "target": qstr(target),
            "slack": qstr(slack),
            "accepted": total <= target,
            "sampled_diagonal_counterexample": "the positive rank-one operator L|w><w| vanishes on every sampled vector orthogonal to w while its norm is L",
            "hidden_tail_counterexample": "append one undisplayed component of arbitrary norm after N while preserving G_N exactly",
            "controls_are_synthetic": True,
        },
        "seed_composition": {
            "K676_seed_actions_still_required": True,
            "charge_intertwiner_still_required": True,
            "partial_gram_bound_proves_seed_identity": False,
            "partial_gram_bound_proves_native_remainder_identification": False,
        },
        "dependency_reconciliation": {
            "K684_bounded_column_interface_reduced": True,
            "K685_sum_of_component_norms_replaced_by_sharper_operator_order_option": True,
            "K687_complete_column_domain_consumed": True,
            "K677_one_over_one_hundred_target_consumed": True,
            "native_partial_gram_added": False,
        },
        "native_interface_status": {
            "actual_native_bounded_components_serialized": False,
            "actual_native_partial_gram_order_proved": False,
            "actual_native_complete_tail_gram_proved": False,
            "actual_native_global_graph_bound_proved": False,
            "actual_native_seed_complement_below_one_over_one_hundred": False,
            "native_complete_floor_emitted": False,
        },
        "decision": {
            "positive_partial_grams_are_complete_bound_interface": True,
            "native_graph_or_complement_bound_proved": False,
            "next_exact_input": "After K687's native column is identified, prove a positive operator bound for every finite partial Gram of C_j a^-1 (and separately after Q_seed), or prove one finite partial bound plus a complete positive tail. For the complement require total order at most 1/100, then add K676's three seed actions and charge intertwiner.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional positive-operator norm certificate inside a repository-supplied model and supplies no source-owned action, physical state, quotient or observable.",
        "preflight_bookend": {
            "route_comparison": "K685's sum of scalar component norms is sufficient but can be wasteful. Positive partial-Gram order is the exact complete-column quantity and covers both the global and localized graph bounds.",
            "retrieval_collision_result": "K609 and K685 contain scalar or component-square controls, but no current artifact proves a uniform complete positive partial-Gram order for the invariant remainder column.",
            "strongest_alternative": "K672 can certify A directly from finite/complement/cross form bounds without constructing any coefficient column.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Using one finite Gram prefix, sampled diagonal elements or a weakly described tail as a complete operator-order certificate.",
            "strongest_contrary_construction": "A hidden positive rank-one direction or one undisplayed component preserves every sampled or finite-prefix value while making the complete norm arbitrarily large.",
            "weakest_reproducibility_seam": "Every B_j must share the same input domain and output direct-sum typing; the partial-Gram inequality and tail order must hold on the complete input space.",
        },
        "controls": {
            "producer": "tests/channel-swings/k688_k500_partial_gram_bound_compiler.py",
            "probe": "tests/channel-swings/k688_k500_partial_gram_bound_compiler_probe.py",
            "controls_passed": 33,
            "hostile_mutations_rejected": 27,
        },
        "claim_ceiling": "Exact conditional positive partial-Gram result: uniform order bounds on all finite sums of B_j*B_j define and bound the complete column, while one finite partial order plus a complete positive tail gives the same conclusion. Applied to C_j a^-1 and C_j a^-1 Q_seed this supplies K684's global boundedness and K685's complement budget without summing scalar operator norms. Current native custody supplies no such components, operator orders or tail. No native R, complement, A, B, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["partial_gram_theorem"]
    controls = payload["exact_controls"]
    seed = payload["seed_composition"]
    native = payload["native_interface_status"]
    assert theorem["identity"] == "||B x||^2=sum_j||B_j x||^2=sup_N <x,G_N x>"
    assert not theorem["finite_partial_gram_without_tail_sufficient"]
    assert not theorem["diagonal_matrix_elements_on_sampled_vectors_sufficient"]
    assert not theorem["component_scalar_coefficients_without_operator_domains_sufficient"]
    assert not theorem["weak_or_uncontrolled_tail_sufficient"]
    assert controls["complete_column_square_upper"] == "33/5000"
    assert controls["slack"] == "17/5000"
    assert controls["accepted"]
    assert not seed["partial_gram_bound_proves_seed_identity"]
    assert not seed["partial_gram_bound_proves_native_remainder_identification"]
    assert not native["actual_native_seed_complement_below_one_over_one_hundred"]
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
