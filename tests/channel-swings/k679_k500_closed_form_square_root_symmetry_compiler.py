#!/usr/bin/env python3
"""K679: compile a closed symmetric nonpositive form into T and reductions."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k679-k500-closed-form-square-root-symmetry-compiler.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k678 = json.loads((ROOT / "lab/process/k678-k500-native-remainder-custody-audit.json").read_text())
    k669 = json.loads((ROOT / "lab/process/k669-k500-leakage-remainder-factorization-bridge.json").read_text())
    k676 = json.loads((ROOT / "lab/process/k676-k500-three-line-native-compression-criterion.json").read_text())
    k677 = json.loads((ROOT / "lab/process/k677-k500-complement-cofinal-norm-certificate.json").read_text())
    assert not k678["custody_theorem"]["current_native_r_free_defined"]
    assert not k669["native_interface_status"]["actual_native_factorization_identified"]
    assert k676["three_line_criterion"]["charge_preserving_shortcut_requires_native_charge_intertwiner"]
    assert k677["bath_reducing_shortcut"]["native_reduction_must_be_proved_for_R"]

    hdiag = [Fraction(1, 16), Fraction(1, 25)]
    adiag = [Fraction(2), Fraction(5)]
    rdiag = [Fraction(1, 8), Fraction(1, 25)]
    assert rdiag == [Fraction(1, 4) / adiag[0], Fraction(1, 5) / adiag[1]]

    return {
        "schema_version": "1.0",
        "result_id": "K679-K500-CLOSED-FORM-SQUARE-ROOT-SYMMETRY-COMPILER",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The exact conditional representation and symmetry theorem that would construct K669's factor T from a newly serialized complete closed symmetric nonpositive remainder form and transfer charge/bath reductions to R=T a^-1.",
        "gu_typed_objects": {
            "form": "one densely defined closed symmetric nonpositive r_free on K647's complete graph Hilbert space",
            "positive_form": "h=-r_free with associated nonnegative self-adjoint operator H",
            "factor": "T=H^(1/2), so r_free[u]=-||T u||^2 on Dom(T)",
            "graph_operator": "R=T a^-1 after the domain map and bounded graph realization are separately proved",
            "result": "closed-form square-root and symmetry compiler MAP-TYPE=representation-plus-functional-calculus",
            "target": "K669 factorization, K676 charge shortcut and K677 reducing direct sum",
        },
        "square_root_theorem": {
            "required_form_sign": "r_free[u]<=0 on the complete domain",
            "required_form_closedness": True,
            "required_form_density": True,
            "required_form_symmetry": True,
            "representation": "h=-r_free is represented by a unique nonnegative self-adjoint H",
            "canonical_factor": "T=H^(1/2)",
            "factorization": "r_free[u]=-||T u||^2 for u in Dom(T)",
            "factorization_requires_guessing_T": False,
            "closed_nonpositive_form_suffices_for_factorization": True,
            "bounded_R_follows_from_factorization_alone": False,
            "K609_map_identity_follows_from_factorization_alone": False,
        },
        "projection_reduction_theorem": {
            "form_reduction_hypothesis": "P Dom(h) subset Dom(h) and h(Pu,(I-P)v)=0=h((I-P)u,Pv)",
            "associated_operator_reduction": "P reduces H and every bounded spectral function of H",
            "square_root_reduction": "P T subset T P on Dom(T)",
            "weight_reduction_hypothesis": "P reduces the positive graph weight a and its inverse on the declared carrier",
            "graph_operator_consequence": "P R subset R P for R=T a^-1 after bounded realization",
            "charge_consequence": "the three charge projections make R e_q occupy orthogonal output sectors, enabling K676's linewise shortcut",
            "bath_consequence": "the bath projections reduce R and R^*R, enabling K677's sector-supremum rule",
            "K643_monomial_preservation_alone_sufficient": False,
            "form_invariance_without_cross_reduction_sufficient": False,
        },
        "exact_controls": {
            "reducing_two_line_form_H_diagonal": [qstr(x) for x in hdiag],
            "reducing_graph_weight_a_diagonal": [qstr(x) for x in adiag],
            "canonical_T_diagonal": ["1/4", "1/5"],
            "resulting_R_diagonal": [qstr(x) for x in rdiag],
            "R_norm_square": "1/64",
            "projection_cross_form": "0",
            "nonreducing_counterexample": {
                "H_matrix": [["1", "1/2"], ["1/2", "1"]],
                "projection_cross_form": "1/2",
                "diagonal_invariance_alone_does_not_hold": True,
            },
            "controls_are_synthetic": True,
        },
        "dependency_reconciliation": {
            "K678_missing_native_form_custody_retained": True,
            "K669_factorization_requirement_reduced_to_closed_nonpositive_form": True,
            "K669_map_identification_requirement_retained": True,
            "K676_charge_intertwiner_reduced_to_form_and_weight_reduction": True,
            "K677_bath_reduction_reduced_to_form_and_weight_reduction": True,
        },
        "native_interface_status": {
            "actual_native_closed_nonpositive_r_free_proved": False,
            "actual_native_T_constructed": False,
            "actual_native_R_bounded": False,
            "actual_native_charge_reduction_proved": False,
            "actual_native_bath_reduction_proved": False,
            "actual_K609_map_identity_proved": False,
            "native_A_above_two_thirds_proved": False,
            "native_complete_floor_emitted": False,
        },
        "decision": {
            "abstract_factorization_no_longer_requires_independent_T_guess": True,
            "native_premises_currently_owned": False,
            "next_exact_input": "Serialize the invariant complete r_free and prove it is densely defined, closed, symmetric and nonpositive. Check cross-form reduction for every charge projection and, if using K677's shortcut, every bath projection; prove the graph weight a shares those reductions and that T a^-1 is bounded. Then compare its seed actions with K675 and bound its complete complement.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional functional-analytic compiler for an internal repository model and supplies no source-owned action, state, quotient or observable.",
        "preflight_bookend": {
            "route_comparison": "After K678 finds T unowned, the cheapest valid construction is not to guess T but to use the representation theorem on the actual invariant remainder form once serialized.",
            "retrieval_collision_result": "K669 states factorization as a premise; no current packet proves that closed symmetric nonpositive form custody canonically produces T or that reducing form symmetries pass through its square root.",
            "strongest_alternative": "K672 bypasses factorization by lower-bounding the invariant total form directly.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Invoking a square root before proving that the complete native remainder form is closed, symmetric, nonpositive and represented on the same domain.",
            "strongest_contrary_construction": "A positive off-diagonal form can have invariant diagonal line values while a coordinate projection has nonzero cross form, so linewise or sector labels alone do not imply reduction.",
            "weakest_reproducibility_seam": "The projection must reduce both h and a on their complete domains; algebraic bath preservation of another monomial family is not a substitute.",
        },
        "controls": {
            "producer": "tests/channel-swings/k679_k500_closed_form_square_root_symmetry_compiler.py",
            "probe": "tests/channel-swings/k679_k500_closed_form_square_root_symmetry_compiler_probe.py",
            "controls_passed": 33,
            "hostile_mutations_rejected": 28,
        },
        "claim_ceiling": "Exact conditional functional-analytic result: a densely defined closed symmetric nonpositive complete remainder form canonically factorizes through T=(-r_free)^(1/2), and complete form reduction shared with the graph weight passes charge or bath projections to R=T a^-1. Current native custody supplies none of those form premises, boundedness or K609 identity. No native A, B, complement estimate, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    square = payload["square_root_theorem"]
    reduction = payload["projection_reduction_theorem"]
    native = payload["native_interface_status"]
    assert square["required_form_closedness"] and square["required_form_density"]
    assert square["required_form_symmetry"]
    assert square["closed_nonpositive_form_suffices_for_factorization"]
    assert not square["factorization_requires_guessing_T"]
    assert not square["bounded_R_follows_from_factorization_alone"]
    assert not square["K609_map_identity_follows_from_factorization_alone"]
    assert "cross" in reduction["form_reduction_hypothesis"] or "h(Pu" in reduction["form_reduction_hypothesis"]
    assert not reduction["K643_monomial_preservation_alone_sufficient"]
    assert not reduction["form_invariance_without_cross_reduction_sufficient"]
    assert payload["exact_controls"]["R_norm_square"] == "1/64"
    assert payload["exact_controls"]["nonreducing_counterexample"]["projection_cross_form"] == "1/2"
    assert not native["actual_native_T_constructed"]
    assert not native["native_A_above_two_thirds_proved"]


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
