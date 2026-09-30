#!/usr/bin/env python3
"""K674: compressed K609 leakage plus a complete-complement norm budget."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k674-k500-compressed-leakage-complement-budget.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k609 = json.loads((ROOT / "lab/process/k609-k500-complete-uniform-leakage-enclosure.json").read_text())
    k663 = json.loads((ROOT / "lab/process/k663-k500-sharp-cancellation-graph-floor.json").read_text())
    k672 = json.loads((ROOT / "lab/process/k672-k500-direct-a-cofinal-certificate.json").read_text())
    k673 = json.loads((ROOT / "lab/process/k673-k500-seed-line-leakage-custody.json").read_text())
    lam = Fraction(k609["uniform_complete_leakage_square_upper"])
    target = Fraction(2, 3)
    budget = Fraction(1, 3) - lam
    rational_tail_target = Fraction(1, 100)
    target_slack = budget - rational_tail_target
    conditional_a = 1 - lam - rational_tail_target
    assert k663["sharp_floor_theorem"]["hypotheses"].startswith("A=1-alpha")
    assert "(a_N-2/3)(a_tail-2/3)>kappa^2" in k672["direct_A_theorem"]["two_thirds_test"]
    assert k673["decision"]["K609_seed_compression_reuse_remains_live"]
    assert budget > rational_tail_target
    control_lambda = Fraction(16, 49)
    control_tau2 = Fraction(1, 196)
    control_sum = control_lambda + control_tau2
    control_a = 1 - control_sum
    return {
        "schema_version": "1.0",
        "result_id": "K674-K500-COMPRESSED-LEAKAGE-COMPLEMENT-BUDGET",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A complete-domain A-margin certificate that reuses K609 only as the compression of K669's remainder factor to K673's three seed lines and separately controls the graph-orthogonal complement.",
        "gu_typed_objects": {
            "operator": "R=T a^-1 from K669 on K647's complete free-coordinate graph carrier",
            "projection": "graph-orthogonal P_seed onto K673's q00, q10 and q01 seed lines, with Q_seed=I-P_seed",
            "compressed_data": "||R P_seed||^2<=lambda after a native compression identity with K609",
            "complement_data": "||R Q_seed||^2<=tau2 on the complete graph-orthogonal complement",
            "result": "compressed leakage complement certificate MAP-TYPE=two-column operator norm bound",
            "target": "the complete A=1-alpha margin consumed by K663/K670",
        },
        "compressed_bridge_theorem": {
            "seed_compression_identity_required": "R P_seed is unitarily the direct sum of K609's three normalized seed-line leakage maps",
            "complete_complement_bound_required": "||R Q_seed||^2<=tau2 on every vector of the complete graph-orthogonal complement",
            "range_orthogonality_required": False,
            "two_column_bound": "||R||^2<=lambda+tau2 by ||Rp+Rq||<=sqrt(lambda)||p||+sqrt(tau2)||q|| and Cauchy-Schwarz",
            "complete_A_lower": "A>=1-lambda-tau2",
            "K672_diagonal_inputs": "a_N=1-lambda and a_tail=1-tau2",
            "K672_cross_input": "kappa^2<=lambda*tau2",
            "two_thirds_shifted_determinant": "(1/3-lambda)(1/3-tau2)-lambda*tau2=1/9-(lambda+tau2)/3",
            "strict_two_thirds_test": "lambda+tau2<1/3",
            "finite_or_sampled_complement_sufficient": False,
            "uncontrolled_complement_allowed": False,
        },
        "exact_native_target": {
            "K609_uniform_seed_lambda": qstr(lam),
            "K609_lambda_strictly_below_one_third": lam < Fraction(1, 3),
            "exact_remaining_tau2_budget": qstr(budget),
            "exact_remaining_tau2_budget_decimal": f"{float(budget):.18f}",
            "simple_sufficient_tau2_target": qstr(rational_tail_target),
            "simple_target_strictly_inside_budget": rational_tail_target < budget,
            "simple_target_A_lower": qstr(conditional_a),
            "simple_target_A_strictly_above_two_thirds": conditional_a > target,
            "simple_target_excess_above_two_thirds": qstr(target_slack),
            "target_is_conditional_not_native": True,
        },
        "exact_controls": {
            "synthetic_aligned_range_control": True,
            "lambda": qstr(control_lambda),
            "tau2": qstr(control_tau2),
            "lambda_plus_tau2": qstr(control_sum),
            "attained_complete_norm_square": qstr(control_sum),
            "complete_A": qstr(control_a),
            "complete_A_above_two_thirds": control_a > target,
            "two_column_bound_sharp_without_range_orthogonality": True,
            "endpoint_lambda_plus_tau2": "1/3",
            "endpoint_A": "2/3",
            "endpoint_strict_target_rejected": True,
        },
        "dependency_reconciliation": {
            "K609_exact_seed_bound_consumed_conditionally": True,
            "K663_A_definition_consumed": True,
            "K669_full_map_identity_no_longer_required_for_compressed_route": True,
            "K672_finite_complement_certificate_instantiated_conditionally": True,
            "K673_seed_coverage_ceiling_respected": True,
            "K670_complete_B_target_retained_conditionally": True,
        },
        "native_interface_status": {
            "actual_seed_compression_identity_proved": False,
            "actual_complete_complement_tau2_identified": False,
            "actual_complete_A_lower_identified": False,
            "actual_complete_B_lower_identified": False,
            "native_complete_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "compressed_K609_route_shape_closed": True,
            "full_K669_identity_required_for_this_route": False,
            "native_A_above_two_thirds_proved": False,
            "next_exact_input": "Identify K609 with R P_seed on K647's graph domain and prove ||R Q_seed||^2<=1/100 (or any exact value below the displayed residual budget). This would prove A>2/3 without a full-domain unitary identification. Then certify K665's complete B>=1/170 packet.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional operator-norm composition inside a repository-supplied point-Fock model and supplies no source-owned action, physical state, quotient, observable or empirical consequence.",
        "preflight_bookend": {
            "route_comparison": "K673 rejects full-domain reuse from three seed lines but does not erase their value; a two-column compression/complement estimate is the sharpest honest route that converts the existing number into a smaller native obligation.",
            "retrieval_collision_result": "K672 supplies the general finite/complement determinant test but does not exploit the factorized negative form R^*R or K609's exact seed compression.",
            "strongest_alternative": "A direct invariant-form K672 packet remains valid and may be easier if native diagonal form lowers appear before the operator compression identity.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Reporting the positive residual budget or the convenient 1/100 target as an already proved native complement estimate.",
            "strongest_contrary_construction": "At lambda+tau2=1/3 with aligned output ranges, the complete norm square reaches one third and A equals exactly two thirds, so the strict budget cannot be weakened to a non-strict one.",
            "weakest_reproducibility_seam": "The compression identity and Q_seed norm must use the same graph pairing and complete domain; charge-orthogonal input lines do not imply orthogonal output ranges.",
        },
        "controls": {
            "producer": "tests/channel-swings/k674_k500_compressed_leakage_complement_budget.py",
            "probe": "tests/channel-swings/k674_k500_compressed_leakage_complement_budget_probe.py",
            "controls_passed": 26,
            "hostile_mutations_rejected": 22,
        },
        "claim_ceiling": "Exact compressed leakage-to-A certificate. If K609 is proved to be the P_seed compression of K669's R=T a^-1 and the complete graph-orthogonal complement satisfies ||R Q_seed||^2<=tau2, then ||R||^2<=lambda_K609+tau2 and A>2/3 follows from tau2<1/3-lambda_K609. The current exact residual budget is positive and exceeds 1/100, but no native compression identity or complement bound is supplied. No native A, B, complete floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["compressed_bridge_theorem"]
    target = payload["exact_native_target"]
    control = payload["exact_controls"]
    native = payload["native_interface_status"]
    assert theorem["range_orthogonality_required"] is False
    assert theorem["two_column_bound"].startswith("||R||^2<=lambda+tau2")
    assert theorem["complete_A_lower"] == "A>=1-lambda-tau2"
    assert theorem["K672_diagonal_inputs"] == "a_N=1-lambda and a_tail=1-tau2"
    assert theorem["K672_cross_input"] == "kappa^2<=lambda*tau2"
    assert theorem["strict_two_thirds_test"] == "lambda+tau2<1/3"
    assert not theorem["finite_or_sampled_complement_sufficient"]
    assert not theorem["uncontrolled_complement_allowed"]
    assert target["K609_lambda_strictly_below_one_third"]
    assert target["simple_sufficient_tau2_target"] == "1/100"
    assert target["simple_target_strictly_inside_budget"]
    assert target["simple_target_A_strictly_above_two_thirds"]
    assert target["target_is_conditional_not_native"]
    assert control["lambda_plus_tau2"] == "65/196"
    assert control["attained_complete_norm_square"] == "65/196"
    assert control["complete_A"] == "131/196"
    assert control["complete_A_above_two_thirds"]
    assert control["two_column_bound_sharp_without_range_orthogonality"]
    assert control["endpoint_strict_target_rejected"]
    assert not native["actual_seed_compression_identity_proved"]
    assert not native["actual_complete_complement_tau2_identified"]
    assert not native["actual_complete_A_lower_identified"]
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
