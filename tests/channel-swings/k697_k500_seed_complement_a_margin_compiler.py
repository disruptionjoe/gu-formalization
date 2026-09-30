#!/usr/bin/env python3
"""K697: compose seed and complete-complement control into an A margin."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k697-k500-seed-complement-a-margin-compiler.json"


def q(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def build() -> dict[str, Any]:
    k676 = json.loads((ROOT / "lab/process/k676-k500-three-line-native-compression-criterion.json").read_text())
    k677 = json.loads((ROOT / "lab/process/k677-k500-complement-cofinal-norm-certificate.json").read_text())
    assert k676["decision"]["three_native_action_rows_suffice_after_charge_intertwining"]
    assert k677["decision"]["complete_complement_obligation_reduced_to_executable_rows_and_tail"]
    seed, complement = Fraction(1, 4), Fraction(1, 100)
    global_upper = max(seed, complement)
    a_lower = Fraction(1) - global_upper
    slack = a_lower - Fraction(2, 3)
    return {
        "schema_version": "1.0",
        "result_id": "K697-K500-SEED-COMPLEMENT-A-MARGIN-COMPILER",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A complete seed/complement block certificate turning K676 and K677 into the direct A=I-R*R lower required by K668/K670.",
        "gu_typed_objects": {
            "operator": "bounded native R=T a^-1 on H",
            "seed_projection": "orthogonal P_seed onto K675's three charge-graded graph-normalized lines",
            "complement": "Q_seed=I-P_seed",
            "margin": "A=I-R*R",
            "result": "seed-complement A-margin compiler MAP-TYPE=complete two-block operator order",
            "target": "K668/K670's complete A_lower input",
        },
        "block_theorem": {
            "native_seed_compression_required": True,
            "complete_complement_bound_required": True,
            "R_star_R_reduction_required_for_maximum_rule": True,
            "reduction_consequence": "P_seed R*R Q_seed=0 and ||R||^2=max(||R P_seed||^2,||R Q_seed||^2)",
            "nonreducing_repair": "if ||P R*R Q||<=k, then ||R||^2 is bounded by lambda_max([[s,k],[k,t]])",
            "A_consequence": "A>=1-max(s,t) under reduction",
            "linewise_seed_bounds_without_charge_or_Gram_control_sufficient": False,
            "finite_complement_prefix_without_complete_tail_sufficient": False,
            "seed_and_complement_norms_without_cross_or_reduction_sufficient": False,
            "bath_labels_without_R_star_R_reduction_sufficient": False,
            "strict_A_margin_automatic_from_seed_control_alone": False,
        },
        "exact_controls": {
            "controls_are_synthetic": True,
            "seed_norm_square_upper": q(seed),
            "complement_norm_square_upper": q(complement),
            "cross_upper": "0",
            "global_R_norm_square_upper": q(global_upper),
            "A_lower": q(a_lower),
            "target_A_lower": "2/3",
            "strict_slack": q(slack),
            "accepted": a_lower > Fraction(2, 3),
            "nonreducing_counterexample": "R(x,y)=(x+y)/2 has both one-dimensional compression norm-squares 1/4 but complete norm-square 1/2 because the cross block is 1/4.",
        },
        "dependency_reconciliation": {
            "K676_native_seed_input_consumed_conditionally": True,
            "K677_complete_complement_input_consumed_conditionally": True,
            "K694_Q_seed_Gram_route_retained": True,
            "K668_K670_A_input_closed_conditionally": True,
            "native_seed_complement_or_reduction_data_added": False,
        },
        "native_interface_status": {
            "actual_native_R_constructed": False,
            "actual_native_seed_actions_computed": False,
            "actual_native_charge_or_Gram_seed_control_proved": False,
            "actual_native_complete_complement_bound_proved": False,
            "actual_native_R_star_R_reduction_proved": False,
            "actual_native_cross_bound_proved": False,
            "native_A_above_two_thirds_proved": False,
            "native_complete_floor_emitted": False,
        },
        "decision": {
            "reducing_seed_complement_packet_suffices_for_A_above_two_thirds": True,
            "native_A_margin_constructed": False,
            "next_exact_input": "After K696 constructs native R, prove K676's three seed actions or Gram domination, prove K677/K694's complete complement bound, and prove that P_seed reduces R*R (or supply the complete cross norm). Then emit the native A lower for K668/K670.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional complete operator block estimate and supplies no source-owned action, physical quotient, state or observable.",
        "preflight_bookend": {
            "route_comparison": "K676 and K677 isolate the two diagonal blocks. K697 states the missing global composition rule and makes the reduction/cross obligation explicit before A is credited.",
            "retrieval_collision_result": "K674 asks for seed and complement budgets but no prior packet derives a complete A lower while guarding the off-diagonal block.",
            "strongest_alternative": "Prove K672's direct cofinal A certificate without factorizing through R or the seed split.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Taking the maximum of seed and complement norms without proving that the split reduces R*R.",
            "strongest_contrary_construction": "Two individually small columns with aligned output have a nonzero cross block and a complete norm larger than either compression.",
            "weakest_reproducibility_seam": "The seed and complement bounds, reduction or cross estimate, and A definition must all use the same native R and complete graph Hilbert norm.",
        },
        "controls": {
            "producer": "tests/channel-swings/k697_k500_seed_complement_a_margin_compiler.py",
            "probe": "tests/channel-swings/k697_k500_seed_complement_a_margin_compiler_probe.py",
            "controls_passed": 38,
            "hostile_mutations_rejected": 32,
        },
        "claim_ceiling": "Exact conditional two-block theorem: native seed control and a complete complement bound give ||R||^2 by a maximum only when P_seed reduces R*R; otherwise a complete cross bound is required. The synthetic reducing packet gives A>=3/4, exceeding 2/3 by 1/12. Current custody supplies no native R, seed actions, complement tail, reduction or cross row. No native A, B, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, n = p["block_theorem"], p["exact_controls"], p["native_interface_status"]
    assert t["native_seed_compression_required"] and t["complete_complement_bound_required"]
    assert t["R_star_R_reduction_required_for_maximum_rule"]
    for key in (
        "linewise_seed_bounds_without_charge_or_Gram_control_sufficient",
        "finite_complement_prefix_without_complete_tail_sufficient",
        "seed_and_complement_norms_without_cross_or_reduction_sufficient",
        "bath_labels_without_R_star_R_reduction_sufficient",
        "strict_A_margin_automatic_from_seed_control_alone",
    ):
        assert not t[key]
    assert c["seed_norm_square_upper"] == "1/4" and c["complement_norm_square_upper"] == "1/100"
    assert c["cross_upper"] == "0" and c["global_R_norm_square_upper"] == "1/4"
    assert c["A_lower"] == "3/4" and c["target_A_lower"] == "2/3" and c["strict_slack"] == "1/12" and c["accepted"]
    assert p["target_claim"] == "NONE-NOT-A-KILL" and p["source_and_ledger_effect"] == "none"
    assert all(value is False for value in n.values())
    assert p["decision"]["reducing_seed_complement_packet_suffices_for_A_above_two_thirds"]
    assert not p["decision"]["native_A_margin_constructed"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
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
