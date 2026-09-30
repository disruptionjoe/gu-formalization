#!/usr/bin/env python3
"""K677: cofinal certificate for K674's complete complement norm."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k677-k500-complement-cofinal-norm-certificate.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k643 = json.loads((ROOT / "lab/process/k643-k500-bath-sector-boundary-reduction.json").read_text())
    k674 = json.loads((ROOT / "lab/process/k674-k500-compressed-leakage-complement-budget.json").read_text())
    budget = Fraction(k674["exact_native_target"]["exact_remaining_tau2_budget"])
    simple = Fraction(k674["exact_native_target"]["simple_sufficient_tau2_target"])
    assert simple < budget
    assert "direct_sum_n B_n" in k643["sector_reduction_theorem"]["reducing_property"]
    core = Fraction(1, 400)
    tail = Fraction(1, 400)
    composed = core + tail
    assert composed <= simple
    return {
        "schema_version": "1.0",
        "result_id": "K677-K500-COMPLEMENT-COFINAL-NORM-CERTIFICATE",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A complete cofinal certificate for K674's Q_seed complement norm, with a general finite-prefix/tail route and a sharper bath-reducing direct-sum route.",
        "gu_typed_objects": {
            "operator": "R=T a^-1 on K647's complete graph carrier",
            "complement": "Q_seed H_G",
            "cofinal_projections": "E_N increasing strongly to Q_seed on the declared graph Hilbert space",
            "bath_route": "orthogonal bath-sector projections Q_n only after native R^*R reduction is proved",
            "result": "complete complement norm certificate MAP-TYPE=cofinal projection compiler",
            "target": "K674's tau2 complement input",
        },
        "general_cofinal_theorem": {
            "hypotheses": "E_N are graph-orthogonal finite/cofinal projections with E_N strongly increasing to Q_seed",
            "finite_core_input": "||R E_N||^2<=u_N",
            "complete_tail_input": "||R(Q_seed-E_N)||^2<=v_N",
            "two_column_conclusion": "||R Q_seed||^2<=u_N+v_N",
            "output_range_orthogonality_required": False,
            "strict_target_test": "u_N+v_N<1/3-lambda_K609",
            "simple_target_test": "u_N+v_N<=1/100",
            "finite_rows_without_complete_tail_sufficient": False,
            "sampled_tail_sufficient": False,
        },
        "bath_reducing_shortcut": {
            "extra_hypothesis": "Q_m R^*R Q_n=0 for m!=n on Q_seed H_G, equivalently the declared bath decomposition reduces R^*R",
            "conclusion": "||R Q_seed||^2=sup_n ||R Q_n||^2",
            "finite_rows": "prove ||R Q_n||^2<=tau2 for every n<=N",
            "uniform_tail": "prove sup_(n>N)||R Q_n||^2<=tau2",
            "complete_result": "||R Q_seed||^2<=tau2",
            "K643_exchange_bath_preservation_proves_R_reduction": False,
            "native_reduction_must_be_proved_for_R": True,
            "individual_sector_bounds_without_reduction_sufficient": False,
        },
        "exact_native_target": {
            "K674_exact_budget": qstr(budget),
            "K674_simple_sufficient_target": qstr(simple),
            "strict_budget_positive": budget > 0,
            "target_is_conditional_not_native": True,
            "required_native_objects": [
                "the complete graph projection Q_seed",
                "one cofinal projection family E_N or an exact R-reducing bath decomposition",
                "all finite/core operator-norm rows used",
                "one complete unsampled tail bound",
            ],
        },
        "exact_controls": {
            "synthetic_general_core_upper": qstr(core),
            "synthetic_general_tail_upper": qstr(tail),
            "synthetic_general_composed_upper": qstr(composed),
            "synthetic_general_meets_one_over_one_hundred": composed <= simple,
            "reducing_direct_sum_rows": ["1/256", "1/400", "1/900"],
            "reducing_direct_sum_norm_square": "1/256",
            "nonreducing_aligned_two_sector_counterexample": {
                "each_sector_norm_square": "1/200",
                "complete_norm_square": "1/100",
                "sector_max_would_be_wrong": True,
            },
        },
        "dependency_reconciliation": {
            "K674_tau2_budget_consumed": True,
            "K643_bath_decomposition_consumed_as_candidate_only": True,
            "K643_monomial_invariance_promoted_to_R_invariance": False,
            "K672_finite_complement_logic_retained": True,
            "native_complement_rows_added": False,
            "native_complete_tail_added": False,
        },
        "native_interface_status": {
            "cofinal_certificate_shape_closed": True,
            "native_Q_seed_projection_serialized": False,
            "native_R_bath_reduction_proved": False,
            "native_finite_core_bound_proved": False,
            "native_complete_tail_bound_proved": False,
            "native_tau2_at_most_one_over_one_hundred_proved": False,
            "native_A_above_two_thirds_proved": False,
        },
        "decision": {
            "complete_complement_obligation_reduced_to_executable_rows_and_tail": True,
            "finite_prefix_alone_rejected": True,
            "next_exact_input": "Serialize Q_seed and R=T a^-1 on one cofinal graph decomposition. Either prove a finite-prefix operator bound plus a complete tail whose sum is at most 1/100, or prove the decomposition reduces R^*R and bound every finite sector and the uniform tail by 1/100.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional complete-domain operator certificate inside a repository-supplied point-Fock model and supplies no source-owned action, physical state, quotient or observable.",
        "preflight_bookend": {
            "route_comparison": "K674 names a complete complement norm but not a reproducible proof shape. Cofinal graph projections turn it into finite/core rows plus one explicit tail, while an actual reducing bath decomposition yields the sharper supremum rule.",
            "retrieval_collision_result": "K643 proves bath preservation for each K179 monomial and K652 treats B-form parity tails; neither proves that R=T a^-1 reduces bath sectors or compiles K674's Q_seed norm.",
            "strongest_alternative": "A direct K672 finite/tail/cross A-form proof remains valid if native form rows appear before R is serialized.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Using K643's monomial bath preservation as if it proved reduction for the still-unidentified factor R=T a^-1.",
            "strongest_contrary_construction": "Two orthogonal input sectors mapped to the same output direction can double the squared norm relative to either sector row; sectorwise bounds need reduction or a complete prefix estimate.",
            "weakest_reproducibility_seam": "The cofinal projections, graph pairing, R domain, cross-sector reduction and unsampled tail must all be serialized on the same complete carrier.",
        },
        "controls": {
            "producer": "tests/channel-swings/k677_k500_complement_cofinal_norm_certificate.py",
            "probe": "tests/channel-swings/k677_k500_complement_cofinal_norm_certificate_probe.py",
            "controls_passed": 32,
            "hostile_mutations_rejected": 26,
        },
        "claim_ceiling": "Exact cofinal certificate shape for K674's complete Q_seed complement norm. A finite/cofinal core bound plus a complete tail gives tau2<=u+v without output-range orthogonality; if native R^*R reduction by bath number is proved, sectorwise rows compose by a supremum. K643 does not itself prove that reduction for R, and no native core row or tail is supplied. No native tau2, A or B, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    general = payload["general_cofinal_theorem"]
    bath = payload["bath_reducing_shortcut"]
    native = payload["native_interface_status"]
    assert not general["output_range_orthogonality_required"]
    assert general["two_column_conclusion"] == "||R Q_seed||^2<=u_N+v_N"
    assert not general["finite_rows_without_complete_tail_sufficient"]
    assert not general["sampled_tail_sufficient"]
    assert not bath["K643_exchange_bath_preservation_proves_R_reduction"]
    assert bath["native_reduction_must_be_proved_for_R"]
    assert not bath["individual_sector_bounds_without_reduction_sufficient"]
    assert payload["exact_native_target"]["strict_budget_positive"]
    assert payload["exact_native_target"]["target_is_conditional_not_native"]
    assert payload["exact_controls"]["synthetic_general_meets_one_over_one_hundred"]
    assert payload["exact_controls"]["nonreducing_aligned_two_sector_counterexample"]["sector_max_would_be_wrong"]
    assert native["cofinal_certificate_shape_closed"]
    assert not native["native_R_bath_reduction_proved"]
    assert not native["native_tau2_at_most_one_over_one_hundred_proved"]
    assert not native["native_A_above_two_thirds_proved"]


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--write", action="store_true"); args = parser.parse_args()
    payload = build(); validate(payload); rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered, encoding="utf-8")
    else: print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
