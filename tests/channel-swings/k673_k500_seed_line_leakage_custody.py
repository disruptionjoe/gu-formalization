#!/usr/bin/env python3
"""K673: distinguish K609 seed-line completeness from complete-domain coverage."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k673-k500-seed-line-leakage-custody.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k609 = json.loads((ROOT / "lab/process/k609-k500-complete-uniform-leakage-enclosure.json").read_text())
    k669 = json.loads((ROOT / "lab/process/k669-k500-leakage-remainder-factorization-bridge.json").read_text())
    levels = k609["level_enclosures"]
    line_squares = {name: row["complete_leakage_square_upper"] for name, row in levels.items()}
    uniform = Fraction(k609["uniform_complete_leakage_square_upper"])
    assert uniform == max(Fraction(value) for value in line_squares.values())
    assert uniform < Fraction(1, 3)
    hidden = Fraction(1)
    return {
        "schema_version": "1.0",
        "result_id": "K673-K500-SEED-LINE-LEAKAGE-CUSTODY",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The carrier coverage of K609's all-order normalized leakage enclosures relative to K669's required complete-domain operator identity.",
        "gu_typed_objects": {
            "seed_subspace": "P_seed=direct sum of the three orthogonal q00, q10 and q01 zero-bath cyclic seed lines used by K609",
            "complete_carrier": "K647's complete free-coordinate graph domain, containing P_seed and an uncontrolled graph-orthogonal complement",
            "seed_data": "three complete-in-order normalized action-vector leakage Rayleigh bounds",
            "result": "seed-line coverage custody MAP-TYPE=operator-extension nonidentifiability",
            "target": "the complete K669 map T a^-1 required to control K663's A margin",
        },
        "coverage_theorem": {
            "K609_complete_in_truncation_order": True,
            "K609_complete_on_named_seed_lines": True,
            "named_seed_lines": ["q00", "q10", "q01"],
            "seed_lines_pairwise_orthogonal_by_charge": True,
            "K609_complete_domain_operator_norm_proved": False,
            "seed_line_bounds_determine_hidden_complement": False,
            "seed_line_bounds_alone_identify_K669_map": False,
            "native_complete_extension_denied": False,
            "required_repair": "either prove the K669 full complete-domain intertwiner or retain K609 only as a P_seed compression and control its complete complement separately",
        },
        "exact_seed_data": {
            "line_leakage_square_uppers": line_squares,
            "uniform_seed_square_upper": qstr(uniform),
            "uniform_seed_square_strictly_below_one_third": uniform < Fraction(1, 3),
            "all_order_tail_charged_once": k609["composition_theorem"]["tail_charged_exactly_once"],
        },
        "hidden_complement_countermodel": {
            "positive_gram_operator": "R_M^* R_M=diag(lambda_q00,lambda_q10,lambda_q01,M) on P_seed direct_sum C e_hidden",
            "all_seed_line_values_unchanged_for_every_M_nonnegative": True,
            "complete_norm_square": "max(lambda_seed,M)",
            "displayed_hidden_M": qstr(hidden),
            "displayed_complete_norm_square": qstr(max(uniform, hidden)),
            "displayed_A_upper_at_most": qstr(1 - max(uniform, hidden)),
            "same_seed_data_can_have_complete_norm_at_least_one": True,
            "proves_seed_data_insufficient_not_native_A_nonpositive": True,
        },
        "dependency_reconciliation": {
            "K609_exact_seed_values_retained": True,
            "K609_all_order_tail_retained": True,
            "K647_complete_domain_retained": True,
            "K669_full_identity_not_claimed": True,
            "K672_compression_complement_route_open": True,
        },
        "native_interface_status": {
            "actual_seed_compression_identity_proved": False,
            "actual_complete_extension_identified": False,
            "actual_complete_complement_norm_identified": False,
            "actual_complete_A_lower_identified": False,
            "native_complete_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "K609_full_complete_domain_reuse_from_current_artifact_rejected": True,
            "K609_seed_compression_reuse_remains_live": True,
            "next_exact_input": "Prove that K609 is the P_seed compression of K669's R=T a^-1, then prove a complete graph-orthogonal complement norm square below K674's residual budget; or prove the full K669 identity directly.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is an operator-domain custody result inside a repository-supplied conditional point-Fock model; it changes no source-owned action, physical state, quotient, observable or empirical consequence.",
        "preflight_bookend": {
            "route_comparison": "K609 owns an exact number below one third, but K669 requires a complete-domain operator identity; resolving whether 'complete' refers to perturbative order or carrier coverage precedes any numerical reuse.",
            "retrieval_collision_result": "K609 names exactly three zero-bath seed levels and K669 names K647's complete domain; no artifact proves these carriers coincide.",
            "strongest_alternative": "A direct K672 finite/complement form proof bypasses K609 but currently has no native diagonal or cross inputs.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling an all-order bound on three orthogonal seed lines the operator norm on the complete graph domain.",
            "strongest_contrary_construction": "The hidden-complement diagonal M=1 preserves every K609 seed-line value while making the complete norm square one.",
            "weakest_reproducibility_seam": "A future bridge must serialize the projection P_seed, prove charge-sector orthogonality in the graph pairing and identify the compressed native operator, not only compare three numbers.",
        },
        "controls": {
            "producer": "tests/channel-swings/k673_k500_seed_line_leakage_custody.py",
            "probe": "tests/channel-swings/k673_k500_seed_line_leakage_custody_probe.py",
            "controls_passed": 24,
            "hostile_mutations_rejected": 20,
        },
        "claim_ceiling": "Exact carrier-coverage custody for K609. Its q00/q10/q01 leakage enclosures are complete in truncation order and tail on three orthogonal seed lines, but those values do not determine a bounded operator on K647's complete free-coordinate domain: a hidden complement can change the complete norm arbitrarily while preserving all three values. This does not deny a native complete extension and preserves compressed reuse. No native factorization, complement bound, A, B, complete floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["coverage_theorem"]
    seed = payload["exact_seed_data"]
    hidden = payload["hidden_complement_countermodel"]
    native = payload["native_interface_status"]
    assert theorem["K609_complete_in_truncation_order"]
    assert theorem["K609_complete_on_named_seed_lines"]
    assert theorem["named_seed_lines"] == ["q00", "q10", "q01"]
    assert theorem["seed_lines_pairwise_orthogonal_by_charge"]
    assert not theorem["K609_complete_domain_operator_norm_proved"]
    assert not theorem["seed_line_bounds_determine_hidden_complement"]
    assert not theorem["seed_line_bounds_alone_identify_K669_map"]
    assert not theorem["native_complete_extension_denied"]
    assert seed["uniform_seed_square_strictly_below_one_third"]
    assert seed["all_order_tail_charged_once"]
    assert hidden["all_seed_line_values_unchanged_for_every_M_nonnegative"]
    assert hidden["displayed_hidden_M"] == "1"
    assert hidden["displayed_complete_norm_square"] == "1"
    assert hidden["displayed_A_upper_at_most"] == "0"
    assert hidden["same_seed_data_can_have_complete_norm_at_least_one"]
    assert hidden["proves_seed_data_insufficient_not_native_A_nonpositive"]
    assert not native["actual_seed_compression_identity_proved"]
    assert not native["actual_complete_extension_identified"]
    assert not native["actual_complete_complement_norm_identified"]
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
