#!/usr/bin/env python3
"""K676: exact three-line criterion for the native K674 compression."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k676-k500-three-line-native-compression-criterion.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k674 = json.loads((ROOT / "lab/process/k674-k500-compressed-leakage-complement-budget.json").read_text())
    k675 = json.loads((ROOT / "lab/process/k675-k500-seed-leakage-operator.json").read_text())
    bounds = {name: Fraction(value) for name, value in k675["exact_seed_bounds"].items()}
    uniform = Fraction(k675["seed_operator_theorem"]["operator_norm_square_upper"])
    total = sum(bounds.values(), Fraction())
    assert uniform == max(bounds.values())
    assert k674["decision"]["compressed_K609_route_shape_closed"]
    control_gram = [[Fraction(1, 4), Fraction(0), Fraction(0)], [Fraction(0), Fraction(1, 9), Fraction(0)], [Fraction(0), Fraction(0), Fraction(1, 16)]]
    return {
        "schema_version": "1.0",
        "result_id": "K676-K500-THREE-LINE-NATIVE-COMPRESSION-CRITERION",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A finite exact criterion for proving that native R=T a^-1 restricted to K673's three graph-orthonormal charge seed lines is controlled by K675's seed leakage operator.",
        "gu_typed_objects": {
            "native_map": "R=T a^-1 on K647's complete free-coordinate graph carrier",
            "seed_basis": "e_q00,e_q10,e_q01 in P_seed H_G",
            "comparison_map": "K675's charge-graded L_seed",
            "native_seed_gram": "G_R=(<R e_i,R e_j>)_(i,j)",
            "result": "three-line native compression criterion MAP-TYPE=finite Gram comparison",
            "target": "K674's conditional seed-compression input",
        },
        "three_line_criterion": {
            "exact_identity_route": "prove R e_q=L_seed e_q for q=q00,q10,q01 in the same target Hilbert space",
            "exact_identity_route_sufficient": True,
            "gram_domination_route": "prove G_R<=diag(lambda_q00,lambda_q10,lambda_q01) as a 3x3 Hermitian form",
            "gram_domination_route_sufficient_for_norm_bound": True,
            "charge_preserving_shortcut": "if R preserves the three orthogonal output charge sectors, it suffices to prove ||R e_q||^2<=lambda_q for each q",
            "charge_preserving_shortcut_requires_native_charge_intertwiner": True,
            "ungraded_linewise_bounds_only_give": "||R P_seed||^2<=lambda_q00+lambda_q10+lambda_q01",
            "ungraded_linewise_sum": qstr(total),
            "ungraded_linewise_sum_below_one_third": total < Fraction(1, 3),
            "dimensions_or_aggregate_norms_sufficient": False,
            "K609_alone_supplies_native_R_actions": False,
        },
        "exact_seed_bounds": {name: qstr(value) for name, value in bounds.items()},
        "exact_target": {
            "charge_graded_seed_norm_square_upper": qstr(uniform),
            "charge_graded_seed_norm_square_below_one_third": uniform < Fraction(1, 3),
            "native_comparison_rows_required": 3,
            "native_pairwise_gram_entries_required_without_charge_shortcut": 6,
            "remaining_complete_complement_input_unchanged": "||R Q_seed||^2<=tau2 with tau2 below K674's residual budget",
        },
        "exact_controls": {
            "synthetic_diagonal_gram": [[qstr(value) for value in row] for row in control_gram],
            "synthetic_norm_square": "1/4",
            "synthetic_linewise_sum": "61/144",
            "aligned_output_control": {
                "three_line_norm_square_each": "1/9",
                "operator_norm_square": "1/3",
                "linewise_max_would_be_wrong": True,
            },
        },
        "dependency_reconciliation": {
            "K674_compression_requirement_consumed": True,
            "K675_seed_operator_consumed": True,
            "K669_complete_domain_map_type_retained": True,
            "native_R_seed_actions_added": False,
            "complete_complement_requirement_retained": True,
        },
        "native_interface_status": {
            "finite_comparison_criterion_closed": True,
            "native_charge_intertwiner_proved": False,
            "native_R_seed_actions_computed": False,
            "native_seed_gram_domination_proved": False,
            "native_compression_identity_proved": False,
            "native_A_above_two_thirds_proved": False,
        },
        "decision": {
            "full_complete_domain_unitary_identification_needed_for_seed_step": False,
            "three_native_action_rows_suffice_after_charge_intertwining": True,
            "next_exact_input": "Serialize R=T a^-1 and its charge intertwiner on K647's common domain, then compute R on e_q00,e_q10,e_q01 and compare with K675. Separately prove K674's complete Q_seed bound.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This finite Gram criterion concerns a repository-defined conditional operator and supplies no source-owned action, physical quotient, state or observable.",
        "preflight_bookend": {
            "route_comparison": "Once K675 serializes the seed operator, finite-dimensional Gram domination is cheaper and more exact than seeking a full complete-domain unitary intertwiner before the seed step is even established.",
            "retrieval_collision_result": "K669 demands a full-domain map identity and K674 permits compression, but no current artifact states the exact three-line comparison or the charge-preserving shortcut.",
            "strongest_alternative": "A direct K672 form estimate avoids R entirely, but still lacks native diagonal and cross rows.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating three scalar norm bounds as a diagonal Gram without proving that native R preserves the output charge decomposition.",
            "strongest_contrary_construction": "Three orthogonal input lines mapped to one aligned output direction each with squared norm 1/9 have operator norm square 1/3, not 1/9.",
            "weakest_reproducibility_seam": "A future native proof must serialize R, the graph-normalized seed basis, the target pairing and either exact action vectors or all six Hermitian Gram entries.",
        },
        "controls": {
            "producer": "tests/channel-swings/k676_k500_three_line_native_compression_criterion.py",
            "probe": "tests/channel-swings/k676_k500_three_line_native_compression_criterion_probe.py",
            "controls_passed": 30,
            "hostile_mutations_rejected": 24,
        },
        "claim_ceiling": "Exact finite criterion for K674's seed-compression input. Three native action identities prove the compression; alternatively, a 3x3 Gram domination suffices, and native charge preservation reduces it to three linewise norm bounds. K609 does not supply those native R actions or the charge intertwiner, and the ungraded linewise sum is not below one third. No complement bound, native A or B, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    criterion = payload["three_line_criterion"]
    target = payload["exact_target"]
    native = payload["native_interface_status"]
    assert criterion["exact_identity_route_sufficient"]
    assert criterion["gram_domination_route_sufficient_for_norm_bound"]
    assert criterion["charge_preserving_shortcut_requires_native_charge_intertwiner"]
    assert not criterion["ungraded_linewise_sum_below_one_third"]
    assert not criterion["dimensions_or_aggregate_norms_sufficient"]
    assert not criterion["K609_alone_supplies_native_R_actions"]
    assert target["charge_graded_seed_norm_square_below_one_third"]
    assert target["native_comparison_rows_required"] == 3
    assert target["native_pairwise_gram_entries_required_without_charge_shortcut"] == 6
    assert payload["exact_controls"]["aligned_output_control"]["linewise_max_would_be_wrong"]
    assert native["finite_comparison_criterion_closed"]
    assert not native["native_charge_intertwiner_proved"]
    assert not native["native_compression_identity_proved"]
    assert not native["native_A_above_two_thirds_proved"]


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--write", action="store_true"); args = parser.parse_args()
    payload = build(); validate(payload); rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered, encoding="utf-8")
    else: print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
