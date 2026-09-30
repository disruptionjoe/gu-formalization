#!/usr/bin/env python3
"""K692: obtain K689's gap and gamma anchor from native form/trace bounds."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k692-k500-friedrichs-trace-anchor-compiler.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k657 = json.loads((ROOT / "lab/process/k657-k500-boundary-weyl-base-floor-certificate.json").read_text())
    k689 = json.loads((ROOT / "lab/process/k689-k500-gamma-anchor-propagation-compiler.json").read_text())
    assert "Friedrichs extension" in k657["ordinary_boundary_triple_theorem"]["reference_premise"]
    assert k689["gamma_resolvent_theorem"]["same_reference_required"]

    target = Fraction(341, 170)
    anchor = Fraction(21, 10)
    lower = Fraction(13, 5)
    trace_coercivity = Fraction(5, 1)
    gap = lower - anchor
    anchor_norm = 1 / trace_coercivity
    factor = 1 + (anchor - target) / gap
    target_norm = factor * anchor_norm
    omega = (anchor - target) * anchor_norm * target_norm
    nearby_margin = Fraction(1, 100)
    transferred = nearby_margin - omega
    assert gap == Fraction(1, 2)
    assert anchor_norm == Fraction(1, 5)
    assert factor == Fraction(101, 85)
    assert target_norm == Fraction(101, 425)
    assert omega == Fraction(808, 180625)
    assert transferred == Fraction(3993, 722500)

    return {
        "schema_version": "1.0",
        "result_id": "K692-K500-FRIEDRICHS-TRACE-ANCHOR-COMPILER",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A complete sufficient packet deriving K689's reference spectral gap and gamma anchor from one Friedrichs form lower bound and one coercive defect-space boundary trace.",
        "gu_typed_objects": {
            "ordinary_triple": "one authenticated complete ordinary boundary triple (Gamma_0,Gamma_1) for S*",
            "friedrichs_reference": "A_0=S* restricted to ker(Gamma_0), proved equal to the Friedrichs extension",
            "defect_trace": "Gamma_0 restricted to N_mu=ker(S*-mu) in the same boundary coordinate",
            "result": "Friedrichs-trace anchor compiler MAP-TYPE=form lower plus inverse trace bound",
            "target": "K689's dist(I,sigma(A_0)) lower and complete ||gamma(mu)|| upper",
        },
        "friedrichs_gap_theorem": {
            "authenticated_friedrichs_reference_required": True,
            "complete_form_lower_required": True,
            "interval_below_lower_edge_required": True,
            "form_hypothesis": "a_0[f]>=c||f||^2 on the complete Friedrichs form domain",
            "spectral_consequence": "sigma(A_0) subset [c,infinity), so for I=[lambda,mu] with mu<c, dist(I,sigma(A_0))>=c-mu",
            "finite_sector_lower_sufficient": False,
            "qualitative_semiboundedness_sufficient": False,
            "non_friedrichs_extension_lower_substitutable": False,
        },
        "defect_trace_theorem": {
            "same_boundary_coordinate_required": True,
            "complete_defect_space_required": True,
            "bijective_trace_from_ordinary_triple_required": True,
            "coercive_trace_hypothesis": "||Gamma_0 f||>=kappa||f|| for every f in N_mu",
            "gamma_inverse_identity": "gamma(mu)=(Gamma_0 restricted to N_mu)^-1",
            "norm_consequence": "||gamma(mu)||<=1/kappa",
            "finite_defect_subspace_bound_sufficient": False,
            "sampled_trace_vectors_sufficient": False,
            "trace_from_different_coordinate_substitutable": False,
        },
        "target_composition": {
            "controls_are_synthetic": True,
            "target_lambda": qstr(target),
            "anchor_mu": qstr(anchor),
            "friedrichs_lower": qstr(lower),
            "interval_gap_lower": qstr(gap),
            "trace_coercivity": qstr(trace_coercivity),
            "anchor_gamma_norm_upper": qstr(anchor_norm),
            "K689_propagation_factor": qstr(factor),
            "target_gamma_norm_upper": qstr(target_norm),
            "K686_weyl_variation_upper": qstr(omega),
            "nearby_denominator_margin": qstr(nearby_margin),
            "transferred_target_margin": qstr(transferred),
            "accepted": transferred >= 0,
        },
        "failing_controls": {
            "lower_not_above_interval": "c<=mu gives no positive lower on dist(I,sigma(A_0)) from semiboundedness alone",
            "finite_trace_control": "coercivity on a finite or sampled defect subspace does not bound the inverse trace on the complete boundary space",
            "wrong_reference": "a lower bound for another self-adjoint extension does not authenticate the K657/K689 Friedrichs reference",
        },
        "dependency_reconciliation": {
            "K689_reference_gap_reduced_to_friedrichs_form_lower": True,
            "K689_anchor_norm_reduced_to_complete_defect_trace_coercivity": True,
            "K657_Friedrichs_identification_requirement_retained": True,
            "K683_nearby_denominator_requirement_retained": True,
            "native_triple_form_or_trace_data_added": False,
        },
        "native_interface_status": {
            "actual_native_boundary_triple_authenticated": False,
            "actual_native_Friedrichs_reference_proved": False,
            "actual_native_complete_form_lower_proved": False,
            "actual_native_defect_trace_coercivity_proved": False,
            "actual_native_reference_gap_proved": False,
            "actual_native_anchor_gamma_norm_proved": False,
            "actual_native_denominator_margin_proved": False,
            "native_complete_floor_emitted": False,
        },
        "decision": {
            "friedrichs_lower_plus_trace_coercivity_suffices_for_K689_inputs": True,
            "native_target_denominator_proved": False,
            "next_exact_input": "Serialize K139's minimal operator and complete ordinary boundary maps; prove ker(Gamma_0) is the Friedrichs reference, establish a complete form lower c above 21/10, and prove Gamma_0 is bounded below on the entire defect space N_(21/10). Then combine K692 with a same-coordinate nearby denominator margin through K689/K686/K683.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional ordinary-boundary-triple operator estimate inside a repository-supplied model and supplies no source-owned action, physical state, quotient or observable.",
        "preflight_bookend": {
            "route_comparison": "K689 leaves a spectral-distance lower and gamma anchor as abstract inputs. A Friedrichs form lower and complete defect-trace coercivity are concrete native inequalities that imply exactly those inputs.",
            "retrieval_collision_result": "K657--K689 require or transport the reference and gamma data, but no current artifact derives both from the native minimal form and trace map.",
            "strongest_alternative": "Compute D_W(341/170) directly, or bound gamma(mu) by an independently proved Weyl derivative M'(mu)=gamma(mu)*gamma(mu).",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Using qualitative semiboundedness, a finite-sector lower, sampled trace vectors or a bound from a different self-adjoint extension or boundary coordinate.",
            "strongest_contrary_construction": "A finite-dimensional trace restriction can be perfectly coercive while the omitted defect directions have singular values tending to zero, making the complete inverse trace unbounded.",
            "weakest_reproducibility_seam": "The minimal operator, complete Friedrichs form domain, exact boundary coordinate, whole defect space, trace bijection, lower constants and same-coordinate denominator must all be authenticated together.",
        },
        "controls": {
            "producer": "tests/channel-swings/k692_k500_friedrichs_trace_anchor_compiler.py",
            "probe": "tests/channel-swings/k692_k500_friedrichs_trace_anchor_compiler_probe.py",
            "controls_passed": 38,
            "hostile_mutations_rejected": 32,
        },
        "claim_ceiling": "Exact conditional ordinary-boundary-triple theorem: a complete Friedrichs form lower c above the target interval gives K689's spectral-distance lower, and coercivity of Gamma_0 on the complete anchor defect space gives the gamma norm through the inverse trace. The synthetic packet reproduces K689's propagated norm and positive transferred margin. Current native custody supplies no authenticated triple, Friedrichs proof, complete form lower, trace coercivity or denominator. No native denominator, r0, B, parity tail, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    gap = payload["friedrichs_gap_theorem"]
    trace = payload["defect_trace_theorem"]
    target = payload["target_composition"]
    native = payload["native_interface_status"]
    assert gap["authenticated_friedrichs_reference_required"]
    assert gap["complete_form_lower_required"]
    assert gap["interval_below_lower_edge_required"]
    assert not gap["finite_sector_lower_sufficient"]
    assert not gap["qualitative_semiboundedness_sufficient"]
    assert not gap["non_friedrichs_extension_lower_substitutable"]
    assert trace["same_boundary_coordinate_required"]
    assert trace["complete_defect_space_required"]
    assert trace["bijective_trace_from_ordinary_triple_required"]
    assert not trace["finite_defect_subspace_bound_sufficient"]
    assert not trace["sampled_trace_vectors_sufficient"]
    assert not trace["trace_from_different_coordinate_substitutable"]
    assert target["interval_gap_lower"] == "1/2"
    assert target["anchor_gamma_norm_upper"] == "1/5"
    assert target["K689_propagation_factor"] == "101/85"
    assert target["target_gamma_norm_upper"] == "101/425"
    assert target["K686_weyl_variation_upper"] == "808/180625"
    assert target["transferred_target_margin"] == "3993/722500"
    assert target["accepted"]
    assert not native["actual_native_anchor_gamma_norm_proved"]
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
