#!/usr/bin/env python3
"""K672: complete finite-plus-complement certificate for K663's invariant A margin."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k672-k500-direct-a-cofinal-certificate.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def shifted_test(a_finite: Fraction, a_tail: Fraction, kappa: Fraction, target: Fraction) -> dict[str, Any]:
    finite_shift = a_finite - target
    tail_shift = a_tail - target
    determinant = finite_shift * tail_shift - kappa * kappa
    trace = finite_shift + tail_shift
    return {
        "a_finite": qstr(a_finite),
        "a_tail": qstr(a_tail),
        "kappa": qstr(kappa),
        "target": qstr(target),
        "finite_shift": qstr(finite_shift),
        "tail_shift": qstr(tail_shift),
        "shifted_determinant": qstr(determinant),
        "shifted_trace": qstr(trace),
        "target_certified_strictly": finite_shift > 0 and tail_shift > 0 and determinant > 0,
    }


def build() -> dict[str, Any]:
    target = Fraction(2, 3)
    passing = shifted_test(Fraction(3, 4), Fraction(1), Fraction(1, 12), target)
    endpoint = shifted_test(Fraction(3, 4), Fraction(1), Fraction(1, 6), target)
    assert passing["shifted_determinant"] == "1/48"
    assert passing["shifted_trace"] == "5/12"
    assert Fraction(passing["shifted_determinant"]) / Fraction(passing["shifted_trace"]) == Fraction(1, 20)
    assert endpoint["shifted_determinant"] == "0"
    return {
        "schema_version": "1.0",
        "result_id": "K672-K500-DIRECT-A-COFINAL-CERTIFICATE",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A chart-invariant complete finite-plus-complement lower certificate for K663's total free-coordinate form margin A on K647's common domain.",
        "gu_typed_objects": {
            "carrier": "K647's complete common domain split orthogonally in the graph norm into one controlled finite subspace P_N and its full complement Q_N",
            "form": "the invariant total free-coordinate form F[phi]=||a phi||^2+r_free[phi]",
            "pairing": "the graph-norm orthogonal finite/complement decomposition with a same-domain cross-form bound",
            "result": "direct-A cofinal certificate MAP-TYPE=two-by-two complete form comparison",
            "target": "a native complete A>2/3 input for K663/K670",
        },
        "direct_A_theorem": {
            "finite_hypothesis": "F[phi_N]>=a_N ||a phi_N||^2 for every phi_N in P_N",
            "complement_hypothesis": "F[phi_tail]>=a_tail ||a phi_tail||^2 for every phi_tail in Q_N, not only sampled tail vectors",
            "cross_hypothesis": "|F(phi_N,phi_tail)|<=kappa ||a phi_N|| ||a phi_tail|| on the same complete domain",
            "comparison_matrix": "[[a_N,-kappa],[-kappa,a_tail]]",
            "complete_A_lower": "lambda_min=(a_N+a_tail-sqrt((a_N-a_tail)^2+4 kappa^2))/2",
            "target_test": "A>mu if a_N>mu, a_tail>mu and (a_N-mu)(a_tail-mu)>kappa^2",
            "two_thirds_test": "A>2/3 if a_N>2/3, a_tail>2/3 and (a_N-2/3)(a_tail-2/3)>kappa^2",
            "finite_prefix_only_sufficient": False,
            "sampled_complement_sufficient": False,
            "uncontrolled_cross_allowed": False,
            "auxiliary_chart_contraction_substitutable_for_total_form_bound": False,
            "complete_common_domain_required": True,
        },
        "exact_controls": {
            "passing_control": passing,
            "passing_shifted_det_over_trace": "1/20",
            "passing_complete_A_strict_lower": "43/60",
            "passing_A_strictly_above_two_thirds": True,
            "endpoint_control": endpoint,
            "endpoint_exact_complete_A": "2/3",
            "endpoint_strict_target_rejected": True,
            "synthetic_controls_only": True,
        },
        "dependency_reconciliation": {
            "K647_complete_common_domain_retained": True,
            "K663_invariant_total_A_definition_consumed": True,
            "K669_direct_A_alternative_instantiated": True,
            "K671_chart_only_inference_rejected": True,
            "K670_complete_B_target_retained_conditionally": True,
            "K667_matched_trace_bound_retained": True,
        },
        "native_interface_status": {
            "actual_native_finite_A_lower_identified": False,
            "actual_native_complement_A_lower_identified": False,
            "actual_native_cross_bound_identified": False,
            "actual_complete_A_lower_identified": False,
            "actual_complete_B_lower_identified": False,
            "native_complete_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "direct_complete_A_certificate_closed": True,
            "native_A_above_two_thirds_proved": False,
            "next_exact_input": "For one graph-orthogonal P_N plus complete Q_N split of K647's invariant total free-coordinate form, prove native a_N>2/3, a_tail>2/3 and kappa^2<(a_N-2/3)(a_tail-2/3), or prove K669's operator factorization/intertwiner instead. After A>2/3, K670 still requires complete B>=1/170 rows and both parity tails.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a complete-domain analytic lower-bound interface for an internal conditional model and supplies no source-owned action, physical state, quotient, observable or empirical consequence.",
        "preflight_bookend": {
            "route_comparison": "K671 rules out chart-only A inference, while K669 explicitly permits a direct complete A proof; a cofinal finite/complement form comparison is the smallest reusable invariant certificate.",
            "retrieval_collision_result": "K664 permits direct A inputs but does not yet state the concrete finite/complement and cross conditions needed to manufacture one on K647's domain.",
            "strongest_alternative": "A proved K669 factorization/intertwiner would reuse K609 and bypass this finite/complement packet.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Promoting a finite-block eigenvalue or sampled tail check to complete A without a complement lower and cross bound.",
            "strongest_contrary_construction": "At a_N=3/4, a_tail=1 and kappa=1/6, both diagonal margins exceed 2/3 but the exact least eigenvalue equals 2/3, so the strict determinant condition cannot be dropped.",
            "weakest_reproducibility_seam": "The finite projection, complement, graph norm and polarization of the invariant total form must be serialized on one common domain.",
        },
        "controls": {
            "producer": "tests/channel-swings/k672_k500_direct_a_cofinal_certificate.py",
            "probe": "tests/channel-swings/k672_k500_direct_a_cofinal_certificate_probe.py",
            "controls_passed": 24,
            "hostile_mutations_rejected": 20,
        },
        "claim_ceiling": "Exact chart-invariant complete finite-plus-complement certificate for K663's A margin. Complete same-domain finite and complement lowers a_N,a_tail with cross bound kappa give the exact two-by-two least-eigenvalue lower, and A>2/3 follows precisely from positive shifted diagonals and shifted determinant. The displayed 3/4, 1 and 1/12 row is synthetic; native finite, complement and cross inputs remain absent. No native A, B, complete floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["direct_A_theorem"]
    controls = payload["exact_controls"]
    native = payload["native_interface_status"]
    assert theorem["comparison_matrix"] == "[[a_N,-kappa],[-kappa,a_tail]]"
    assert "(a_N-2/3)(a_tail-2/3)>kappa^2" in theorem["two_thirds_test"]
    assert not theorem["finite_prefix_only_sufficient"]
    assert not theorem["sampled_complement_sufficient"]
    assert not theorem["uncontrolled_cross_allowed"]
    assert not theorem["auxiliary_chart_contraction_substitutable_for_total_form_bound"]
    assert theorem["complete_common_domain_required"]
    assert controls["passing_control"]["shifted_determinant"] == "1/48"
    assert controls["passing_control"]["shifted_trace"] == "5/12"
    assert controls["passing_shifted_det_over_trace"] == "1/20"
    assert controls["passing_complete_A_strict_lower"] == "43/60"
    assert controls["passing_A_strictly_above_two_thirds"]
    assert controls["endpoint_control"]["shifted_determinant"] == "0"
    assert controls["endpoint_exact_complete_A"] == "2/3"
    assert controls["endpoint_strict_target_rejected"]
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
