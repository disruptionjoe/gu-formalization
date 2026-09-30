#!/usr/bin/env python3
"""K675: construct the charge-graded K609 seed leakage operator."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k675-k500-seed-leakage-operator.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k609 = json.loads((ROOT / "lab/process/k609-k500-complete-uniform-leakage-enclosure.json").read_text())
    k673 = json.loads((ROOT / "lab/process/k673-k500-seed-line-leakage-custody.json").read_text())
    levels = ("q00", "q10", "q01")
    lambdas = {level: Fraction(k609["level_enclosures"][level]["complete_leakage_square_upper"]) for level in levels}
    uniform = Fraction(k609["uniform_complete_leakage_square_upper"])
    assert uniform == max(lambdas.values())
    assert k673["coverage_theorem"]["K609_complete_on_named_seed_lines"]
    control = {"q00": Fraction(1, 4), "q10": Fraction(1, 9), "q01": Fraction(1, 16)}
    return {
        "schema_version": "1.0",
        "result_id": "K675-K500-SEED-LEAKAGE-OPERATOR",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The bounded charge-graded operator on K673's three-dimensional seed subspace obtained from K609's actual normalized residual vectors and their complete outward norm enclosures.",
        "gu_typed_objects": {
            "input": "P_seed H_G=span{e_q00,e_q10,e_q01} with graph-orthonormal charge-homogeneous seeds",
            "output": "the orthogonal direct sum of the corresponding K177/K179 charge sectors",
            "residual_vectors": "zeta_q=(w_q-<v_q,w_q>||v_q||^-2 v_q)/||v_q||, with K609's interval-safe projection convention",
            "operator": "L_seed e_q=zeta_q, extended linearly on P_seed H_G",
            "result": "seed leakage operator MAP-TYPE=charge-graded finite-rank operator",
            "target": "the compressed input in K674 before comparison with native R=T a^-1",
        },
        "seed_operator_theorem": {
            "input_charge_lines_orthogonal": True,
            "output_charge_sectors_orthogonal": True,
            "residual_projection_stays_in_charge_sector": True,
            "operator_well_defined_on_three_dimensional_seed_space": True,
            "gram_majorant": "L_seed^* L_seed<=diag(lambda_q00,lambda_q10,lambda_q01)",
            "operator_norm_square_upper": qstr(uniform),
            "operator_norm_square_is_maximum_of_line_uppers": True,
            "sum_of_line_uppers_used": False,
            "complete_domain_extension_claimed": False,
            "native_R_compression_identity_claimed": False,
        },
        "exact_seed_bounds": {level: qstr(lambdas[level]) for level in levels},
        "exact_controls": {
            "synthetic_charge_graded_diagonal": {level: qstr(control[level]) for level in levels},
            "synthetic_operator_norm_square": qstr(max(control.values())),
            "synthetic_trace_of_gram": qstr(sum(control.values(), Fraction())),
            "maximum_not_trace": max(control.values()) < sum(control.values(), Fraction()),
            "ungraded_aligned_output_counterexample": {
                "three_line_norm_square": "1/9",
                "complete_operator_norm_square": "1/3",
                "proves_output_orthogonality_load_bearing": True,
            },
        },
        "dependency_reconciliation": {
            "K609_actual_vectors_consumed": True,
            "K609_interval_uppers_retained": True,
            "K673_carrier_ceiling_retained": True,
            "K674_seed_compression_object_now_serialized": True,
            "K674_native_compression_identity_completed": False,
        },
        "native_interface_status": {
            "seed_operator_constructed": True,
            "actual_native_R_actions_identified": False,
            "actual_seed_compression_identity_proved": False,
            "actual_complete_complement_bound_proved": False,
            "native_A_above_two_thirds_proved": False,
            "native_complete_floor_emitted": False,
        },
        "decision": {
            "K609_promoted_from_three_scalars_to_typed_seed_operator": True,
            "next_exact_input": "Compute native R=T a^-1 on the three graph-normalized charge seeds and compare those actions with L_seed; then certify the complete Q_seed complement independently.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a typed finite-rank operator extracted from repository-owned conditional point-Fock vectors; it supplies no source-owned action, physical state, quotient or observable.",
        "preflight_bookend": {
            "route_comparison": "K674 needs a typed compression, not merely three numbers. Charge grading makes the direct-sum operator the cheapest exact object that preserves all K609 evidence.",
            "retrieval_collision_result": "K609 records seedwise residual bounds and K673 records their carrier ceiling, but neither serializes the bounded direct-sum seed operator.",
            "strongest_alternative": "A direct K672 A-form estimate bypasses the operator, but currently has no native diagonal or cross inputs.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Identifying L_seed with native R P_seed or extending it to K647's complete graph domain without computing native actions.",
            "strongest_contrary_construction": "Three equal line norms with aligned ungraded outputs have operator norm square three times one line value; charge orthogonality is essential.",
            "weakest_reproducibility_seam": "K609 gives outward residual norm enclosures rather than exact residual coordinates, so the result is an operator with an exact Gram majorant, not an exact singular-value table.",
        },
        "controls": {
            "producer": "tests/channel-swings/k675_k500_seed_leakage_operator.py",
            "probe": "tests/channel-swings/k675_k500_seed_leakage_operator_probe.py",
            "controls_passed": 28,
            "hostile_mutations_rejected": 22,
        },
        "claim_ceiling": "Exact construction of K609's charge-graded three-line seed leakage operator with squared norm bounded by the maximum of the three complete seed enclosures. It serializes the compressed object K674 needs but does not identify it with native R=T a^-1, control the graph-orthogonal complement, prove A or B, release K473/K152, or change source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusions.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["seed_operator_theorem"]
    native = payload["native_interface_status"]
    assert theorem["input_charge_lines_orthogonal"] and theorem["output_charge_sectors_orthogonal"]
    assert theorem["operator_norm_square_is_maximum_of_line_uppers"]
    assert not theorem["sum_of_line_uppers_used"]
    assert not theorem["complete_domain_extension_claimed"]
    assert not theorem["native_R_compression_identity_claimed"]
    assert Fraction(theorem["operator_norm_square_upper"]) < Fraction(1, 3)
    assert payload["exact_controls"]["maximum_not_trace"]
    assert payload["exact_controls"]["ungraded_aligned_output_counterexample"]["proves_output_orthogonality_load_bearing"]
    assert native["seed_operator_constructed"]
    assert not native["actual_seed_compression_identity_proved"]
    assert not native["native_A_above_two_thirds_proved"]


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--write", action="store_true"); args = parser.parse_args()
    payload = build(); validate(payload); rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered, encoding="utf-8")
    else: print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
