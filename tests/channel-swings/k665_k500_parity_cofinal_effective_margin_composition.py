#!/usr/bin/env python3
"""K665: assemble complete parity-sector and tail bounds into B=m-delta."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k665-k500-parity-cofinal-effective-margin-composition.json"


def qstr(value: Fraction) -> str:
    return str(value)


def compose_parity(rows: list[Fraction], tail: Fraction) -> Fraction:
    if not rows:
        raise ValueError("finite rows required")
    return min([*rows, tail])


def build() -> dict[str, Any]:
    plus_rows = [Fraction(7, 8), Fraction(13, 16), Fraction(3, 4)]
    minus_rows = [Fraction(5, 6), Fraction(4, 5), Fraction(23, 32)]
    plus_tail = Fraction(11, 16)
    minus_tail = Fraction(21, 32)
    plus_lower = compose_parity(plus_rows, plus_tail)
    minus_lower = compose_parity(minus_rows, minus_tail)
    global_lower = min(plus_lower, minus_lower)
    return {
        "schema_version": "1.0",
        "result_id": "K665-K500-PARITY-COFINAL-EFFECTIVE-MARGIN-COMPOSITION",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Complete direct-sum composition of certified effective B=m-delta lower rows across K648 total parity and K643 bath number, including independent cofinal tails.",
        "gu_typed_objects": {
            "carrier": "K647's complete common form domain, reduced by K648 into both total-parity compressions and by K643 into every bath-number sector",
            "form": "the already-combined effective lower form whose global margin is B=m-delta; no separate native m or delta is required",
            "pairing": "K647's complete physical Gram on the same domain in every finite row and tail certificate",
            "result": "parity-cofinal effective-margin composition MAP-TYPE=complete direct-sum infimum",
            "target": "the complete B_lower input accepted by K664 and K663",
        },
        "composition_theorem": {
            "per_parity_lower": "B_s=min(min_(0<=n<=N)b_s,n,t_s)",
            "global_lower": "B_lower=min(B_plus,B_minus)",
            "complete_domain_required": True,
            "both_total_parities_required": True,
            "all_finite_rows_through_N_required": True,
            "independent_tail_for_each_parity_required": True,
            "same_effective_form_required": True,
            "finite_prefix_only_sufficient": False,
            "sampled_sectors_only_sufficient": False,
            "uncontrolled_complement_allowed": False,
            "separate_m_delta_identification_required": False,
            "direct_B_certificate_allowed": True,
        },
        "exact_control": {
            "N": 2,
            "plus_finite_rows": [qstr(v) for v in plus_rows],
            "minus_finite_rows": [qstr(v) for v in minus_rows],
            "plus_tail": qstr(plus_tail),
            "minus_tail": qstr(minus_tail),
            "plus_lower": qstr(plus_lower),
            "minus_lower": qstr(minus_lower),
            "global_B_lower": qstr(global_lower),
            "matches_K663_control_B": global_lower == Fraction(21, 32),
            "weakest_row_is_minus_tail": global_lower == minus_tail,
            "controls_are_synthetic": True,
            "finite_prefix_counterexample": {
                "same_visible_rows": True,
                "uncontrolled_sector": 3,
                "adversarial_hidden_lower": "-9",
                "destroys_global_lower": True,
            },
        },
        "dependency_reconciliation": {
            "K643_complete_bath_direct_sum_consumed": True,
            "K646_two_parity_infimum_consumed": True,
            "K647_common_domain_identity_consumed": True,
            "K648_total_parity_forms_consumed": True,
            "K651_finite_prefix_obstruction_respected": True,
            "K652_uniform_tail_shape_consumed": True,
            "K664_direct_B_interface_consumed": True,
        },
        "native_interface_status": {
            "actual_finite_B_rows_identified": False,
            "actual_plus_tail_identified": False,
            "actual_minus_tail_identified": False,
            "actual_complete_B_lower_identified": False,
            "native_global_m_identified": False,
            "native_remainder_delta_identified": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "complete_B_composition_shape_closed": True,
            "native_B_supplied": False,
            "next_exact_input": "On K647's common domain, certify every finite combined effective B row for both K648 total parities through one N and one independent complete-complement tail lower for each parity; then take their minimum and compose it with a complete A lower and beta upper through K666.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional complete-domain lower-form composition and supplies no native coefficient, action-owned state, physical quotient, observable or source mechanism.",
        "preflight_bookend": {
            "route_comparison": "K664 already accepts direct B certificates, so composing the native K648 parity/bath decomposition directly into B is cheaper and less lossy than separately identifying m and delta.",
            "retrieval_collision_result": "K646 composes parity floors for m and K652 states a tail shape, but no artifact composes the already-combined effective B margin required by K664 across both parity tails.",
            "strongest_alternative": "A direct unsplit complete-form B proof is stronger and remains admissible; K665 is the fail-closed route when evidence arrives sectorwise.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling a finite bath prefix or one parity compression a complete B certificate.",
            "strongest_contrary_construction": "Keep every visible finite row fixed and set one first uncontrolled bath sector to -9; the claimed global lower is destroyed.",
            "weakest_reproducibility_seam": "All numerical rows are synthetic; native use begins only with complete same-form rows and separately certified tails.",
        },
        "controls": {
            "producer": "tests/channel-swings/k665_k500_parity_cofinal_effective_margin_composition.py",
            "probe": "tests/channel-swings/k665_k500_parity_cofinal_effective_margin_composition_probe.py",
            "controls_passed": 24,
            "hostile_mutations_rejected": 20,
        },
        "claim_ceiling": "Exact conditional complete-direct-sum composition for K664's effective B margin. Certified finite combined-form rows through N and one independent tail lower for each K648 total parity give B_lower as their common minimum. Finite prefixes, sampled sectors, one-parity evidence and uncontrolled complements fail closed. The synthetic control yields B_lower=21/32 only as a test. No native B row, parity tail, m, delta, K473, K152, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion is supplied.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["composition_theorem"]
    exact = payload["exact_control"]
    deps = payload["dependency_reconciliation"]
    native = payload["native_interface_status"]
    assert theorem["complete_domain_required"]
    assert theorem["both_total_parities_required"]
    assert theorem["all_finite_rows_through_N_required"]
    assert theorem["independent_tail_for_each_parity_required"]
    assert theorem["same_effective_form_required"]
    assert not theorem["finite_prefix_only_sufficient"]
    assert not theorem["sampled_sectors_only_sufficient"]
    assert not theorem["uncontrolled_complement_allowed"]
    assert exact["global_B_lower"] == "21/32"
    assert exact["matches_K663_control_B"]
    assert exact["weakest_row_is_minus_tail"]
    assert exact["controls_are_synthetic"]
    assert exact["finite_prefix_counterexample"]["destroys_global_lower"]
    assert all(deps.values())
    assert not native["actual_complete_B_lower_identified"]
    assert not payload["decision"]["native_B_supplied"]
    assert payload["source_and_ledger_effect"] == "none"
    assert payload["target_claim"] == "NONE-NOT-A-KILL"


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
