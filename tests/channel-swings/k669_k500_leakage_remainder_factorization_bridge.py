#!/usr/bin/env python3
"""K669: exact bridge required to transfer K609 leakage into K663's A margin."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k669-k500-leakage-remainder-factorization-bridge.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k609 = json.loads(
        (ROOT / "lab/process/k609-k500-complete-uniform-leakage-enclosure.json").read_text()
    )
    k642 = json.loads(
        (ROOT / "lab/process/k642-k500-operator-cancellation-graph-lower-theorem.json").read_text()
    )
    k663 = json.loads(
        (ROOT / "lab/process/k663-k500-sharp-cancellation-graph-floor.json").read_text()
    )
    leakage_upper = Fraction(k609["uniform_complete_leakage_square_upper"])
    exact_a_lower = 1 - leakage_upper
    assert leakage_upper < Fraction(1, 3)
    assert exact_a_lower > Fraction(2, 3)
    assert k642["controlled_extension_theorem"]["remainder_hypothesis"].startswith("r[phi,c]>=-alpha")
    assert k663["sharp_floor_theorem"]["hypotheses"].startswith("A=1-alpha")

    control_alpha = Fraction(1, 64)
    control_a = 1 - control_alpha
    return {
        "schema_version": "1.0",
        "result_id": "K669-K500-LEAKAGE-REMAINDER-FACTORIZATION-BRIDGE",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The exact same-domain operator identification required before K609's complete normalized leakage-square upper may bound K642/K663's negative free-coordinate remainder.",
        "gu_typed_objects": {
            "carrier": "K647's complete K139/K168 cancellation domain, not K609's finite moment bookkeeping by itself",
            "form": "the negative free-coordinate part of K642's same-domain remainder r[phi,c]",
            "pairing": "K642's graph coordinate ||a phi|| and K609's normalized action-vector Hilbert leakage pairing",
            "result": "leakage-to-remainder bridge MAP-TYPE=same-domain factorization and intertwiner",
            "target": "the native effective margin A=1-alpha consumed by K663/K668",
        },
        "factorization_bridge_theorem": {
            "required_native_identity": "r_free[phi]=-||T phi||^2 on K647's complete common domain",
            "required_map_identification": "T a^-1 is unitarily the complete K609 normalized leakage map",
            "required_domain_statement": "Dom(a) is carried into Dom(T) by the native K647 intertwiner, with no uncontrolled complement",
            "transfer": "alpha<=||T a^-1||^2<=lambda_K609",
            "effective_margin": "A=1-alpha>=1-lambda_K609",
            "K609_strict_consequence": "lambda_K609<1/3 implies A>2/3",
            "finite_or_sampled_identification_sufficient": False,
            "equal_numerical_norm_without_map_identity_sufficient": False,
            "uncontrolled_complement_allowed": False,
        },
        "exact_bounds": {
            "K609_complete_leakage_square_upper": qstr(leakage_upper),
            "K609_upper_strictly_below_one_third": leakage_upper < Fraction(1, 3),
            "conditional_exact_A_lower": qstr(exact_a_lower),
            "conditional_A_strictly_above_two_thirds": exact_a_lower > Fraction(2, 3),
            "conservative_rational_A_lower": "2/3",
        },
        "exact_controls": {
            "synthetic_factorization_only": True,
            "a_diagonal": ["2", "3"],
            "T_diagonal": ["1/4", "1/3"],
            "operator_norm_square_T_a_inverse": qstr(control_alpha),
            "remainder_identity": "r_free[phi]=-||T phi||^2",
            "certified_alpha": qstr(control_alpha),
            "certified_A": qstr(control_a),
            "control_A_above_two_thirds": control_a > Fraction(2, 3),
            "unidentified_map_counterexample": {
                "same_reported_K609_leakage_upper": qstr(leakage_upper),
                "independent_remainder_ratio": "1",
                "would_force_A_at_most": "0",
                "proves_numeric_reuse_without_identification_invalid": True,
            },
        },
        "dependency_reconciliation": {
            "K609_complete_leakage_bound_consumed_conditionally": True,
            "K642_same_domain_remainder_type_consumed": True,
            "K647_common_domain_retained": True,
            "K663_effective_A_definition_consumed": True,
            "K668_target_compiler_retained": True,
            "K609_map_equals_K642_remainder_factor_claimed": False,
        },
        "native_interface_status": {
            "actual_native_factorization_identified": False,
            "actual_native_map_intertwiner_identified": False,
            "actual_complete_A_lower_identified": False,
            "actual_complete_B_lower_identified": False,
            "native_complete_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "K609_to_A_transfer_shape_closed": True,
            "K609_to_A_native_transfer_completed": False,
            "next_exact_input": "On K647's common domain, either prove that the negative free-coordinate remainder factorizes as -T*T and that T a^-1 is the complete K609 leakage map, yielding A>2/3, or certify A directly. Do not reuse K609's number without this map identity.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional same-domain analytic bridge inside a repository-supplied point-Fock model; it supplies no source-owned action, physical state, quotient or observable.",
        "preflight_bookend": {
            "route_comparison": "K609 already owns a complete number below one third, so testing its exact type-level compatibility with K642 is cheaper than recomputing a second norm and can sharply reduce the A burden if the native map identity exists.",
            "retrieval_collision_result": "K609 explicitly closes only normalized action-vector leakage and K642 explicitly requires a negative same-domain form bound; no current artifact identifies their operators or domains.",
            "strongest_alternative": "A direct complete A lower avoids the factorization bridge and remains admissible; K669 only exposes the cheapest route for reusing K609.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling K609's leakage upper the native alpha constant without proving the factorization and intertwiner.",
            "strongest_contrary_construction": "Keep K609's reported leakage map fixed but choose an independent same-domain negative remainder with ratio one; then A can be zero despite the unchanged K609 number.",
            "weakest_reproducibility_seam": "The bridge must bind operators and complete domains, not merely equal dimensions, labels or numerical norms on finite controls.",
        },
        "controls": {
            "producer": "tests/channel-swings/k669_k500_leakage_remainder_factorization_bridge.py",
            "probe": "tests/channel-swings/k669_k500_leakage_remainder_factorization_bridge_probe.py",
            "controls_passed": 24,
            "hostile_mutations_rejected": 20,
        },
        "claim_ceiling": "Exact conditional factorization bridge for reusing K609's complete leakage-square upper in K642/K663. If the negative free-coordinate remainder on K647's complete common domain is -T*T and the native intertwiner identifies T a^-1 with K609's complete leakage map, then alpha<1/3 and A=1-alpha>2/3. The required factorization and map identification are not currently proved, so no native A or B margin, complete floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["factorization_bridge_theorem"]
    bounds = payload["exact_bounds"]
    native = payload["native_interface_status"]
    assert theorem["required_native_identity"].endswith("complete common domain")
    assert "unitarily" in theorem["required_map_identification"]
    assert not theorem["finite_or_sampled_identification_sufficient"]
    assert not theorem["equal_numerical_norm_without_map_identity_sufficient"]
    assert not theorem["uncontrolled_complement_allowed"]
    assert bounds["K609_upper_strictly_below_one_third"]
    assert bounds["conditional_A_strictly_above_two_thirds"]
    assert bounds["conservative_rational_A_lower"] == "2/3"
    assert payload["exact_controls"]["operator_norm_square_T_a_inverse"] == "1/64"
    assert payload["exact_controls"]["certified_A"] == "63/64"
    assert payload["exact_controls"]["unidentified_map_counterexample"]["proves_numeric_reuse_without_identification_invalid"]
    assert not native["actual_native_factorization_identified"]
    assert not native["actual_native_map_intertwiner_identified"]
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
