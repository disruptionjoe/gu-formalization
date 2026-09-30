#!/usr/bin/env python3
"""K684: compile one closed coefficient column into h, T and bounded R."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k684-k500-closed-column-remainder-compiler.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k681 = json.loads((ROOT / "lab/process/k681-k500-monotone-remainder-form-compiler.json").read_text())
    k682 = json.loads((ROOT / "lab/process/k682-k500-graph-relative-bounded-reduction-compiler.json").read_text())
    assert k681["monotone_form_theorem"]["limit_density_required"]
    assert k682["boundedness_theorem"]["complete_domain_required"]

    c_diag = [Fraction(1, 4), Fraction(1, 5), Fraction(1, 6)]
    a_diag = [Fraction(2), Fraction(5), Fraction(3)]
    h_diag = [x * x for x in c_diag]
    r_diag = [c / a for c, a in zip(c_diag, a_diag)]
    r_norm = max(r_diag)
    assert h_diag == [Fraction(1, 16), Fraction(1, 25), Fraction(1, 36)]
    assert r_diag == [Fraction(1, 8), Fraction(1, 25), Fraction(1, 18)]

    return {
        "schema_version": "1.0",
        "result_id": "K684-K500-CLOSED-COLUMN-REMAINDER-COMPILER",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A coefficient-level construction that turns one explicitly supplied densely defined closed complete column operator into K679's closed remainder form and K682's bounded graph realization.",
        "gu_typed_objects": {
            "coefficient_column": "C:Dom(C) subset H -> direct_sum_j K_j, a densely defined closed operator containing every native remainder component",
            "form": "h[u]=||C u||^2 on Dom(C), identified with -r_free only after a separate native same-form proof",
            "factor": "T=|C|=(C* C)^(1/2), with Dom(T)=Dom(C) and ||T u||=||C u||",
            "graph_operator": "R=T a^-1, norm-equivalent to the bounded column C a^-1",
            "result": "closed-column remainder compiler MAP-TYPE=operator-polar-decomposition",
            "target": "K681/K682's complete form, bounded realization and charge/bath reduction packet",
        },
        "closed_column_theorem": {
            "column_hypothesis": "C is densely defined and closed on the complete carrier",
            "form_conclusion": "h[u]=||C u||^2 with Dom(h)=Dom(C) is a densely defined closed nonnegative quadratic form",
            "associated_operator": "H=C* C is nonnegative self-adjoint and T=H^(1/2)=|C|",
            "domain_identity": "Dom(T)=Dom(C)",
            "norm_identity": "||T u||=||C u|| for every u in Dom(C)",
            "native_identification_required": True,
            "finite_or_formal_component_list_sufficient": False,
            "unclosed_column_sufficient": False,
        },
        "bounded_realization": {
            "weight_hypothesis": "a is the declared positive graph weight and a^-1 maps the complete Hilbert carrier into Dom(a)=Dom(C)",
            "column_hypothesis": "B=C a^-1 extends boundedly to the complete Hilbert carrier",
            "conclusion": "R=T a^-1 extends boundedly",
            "norm_identity": "||R||=||C a^-1||=||B||",
            "relative_form_identity": "h[u]=||C u||^2<=||B||^2||a u||^2 on Dom(a)",
            "factorization_without_bounded_column_sufficient": False,
            "seed_only_column_sufficient": False,
        },
        "reduction_theorem": {
            "hypothesis": "for orthogonal P on H and Q on the column codomain, C P=Q C on Dom(C), C(I-P)=(I-Q)C, and P strongly reduces a and a^-1",
            "form_consequence": "P reduces h and C* C",
            "factor_consequence": "P reduces T=|C|",
            "graph_consequence": "P reduces R and R*R",
            "component_labels_without_intertwining_sufficient": False,
        },
        "exact_controls": {
            "C_diagonal": [qstr(x) for x in c_diag],
            "h_diagonal": [qstr(x) for x in h_diag],
            "a_diagonal": [qstr(x) for x in a_diag],
            "R_diagonal": [qstr(x) for x in r_diag],
            "R_norm": qstr(r_norm),
            "R_norm_square": qstr(r_norm * r_norm),
            "coordinate_projections_intertwine_column_and_reduce_weight": True,
            "nonclosed_counterexample": {
                "operator": "the derivative on L2(0,1) restricted to smooth compactly supported functions",
                "densely_defined": True,
                "closed": False,
                "square_form_closed_on_that_uncompleted_domain": False,
            },
            "controls_are_synthetic": True,
        },
        "dependency_reconciliation": {
            "K679_closed_form_factorization_consumed": True,
            "K681_monotone_family_is_one_route_not_required_by_closed_column_route": True,
            "K682_relative_bound_consumed": True,
            "K676_charge_reduction_reduced_to_column_intertwining_plus_weight_reduction": True,
            "K677_bath_reduction_reduced_to_column_intertwining_plus_weight_reduction": True,
            "native_closed_column_added": False,
        },
        "native_interface_status": {
            "actual_native_complete_column_serialized": False,
            "actual_native_column_closed": False,
            "actual_native_r_free_identified": False,
            "actual_native_C_a_inverse_bounded": False,
            "actual_native_charge_reduction_proved": False,
            "actual_native_bath_reduction_proved": False,
            "native_A_above_two_thirds_proved": False,
            "native_complete_floor_emitted": False,
        },
        "decision": {
            "closed_column_bypasses_separate_monotone_approximant_construction": True,
            "native_column_constructed": False,
            "next_exact_input": "Serialize the complete native coefficient column C for the invariant remainder, prove it is closed and Dom(C)=Dom(a), prove C a^-1 bounded, and prove its charge/bath intertwiners. Then use K685 to certify the seed complement and K676 to compare the three seed actions.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional polar-decomposition compiler for an internal repository model and supplies no source-owned action, state, quotient or observable.",
        "preflight_bookend": {
            "route_comparison": "K681 constructs h from monotone forms, but a native coefficient expansion may arrive more naturally as one closed column. Polar decomposition then constructs h and T without separately proving every finite partial form closed.",
            "retrieval_collision_result": "K159 owns an operator-valued gamma/Weyl interface and K456 owns an action column, but neither identifies a closed column whose square is K642's invariant remainder.",
            "strongest_alternative": "K672 bypasses remainder factorization and proves the invariant total A form directly.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating a formal or finite coefficient list as a densely defined closed complete column, or identifying its square with r_free without a same-form proof.",
            "strongest_contrary_construction": "A densely defined but nonclosed derivative restriction has a nonclosed square form on its uncompleted domain, so density and component formulas alone do not construct h.",
            "weakest_reproducibility_seam": "The complete column domain, closedness, native same-form identity, bounded C a^-1 and exact projection intertwiners must be serialized on one carrier.",
        },
        "controls": {
            "producer": "tests/channel-swings/k684_k500_closed_column_remainder_compiler.py",
            "probe": "tests/channel-swings/k684_k500_closed_column_remainder_compiler_probe.py",
            "controls_passed": 35,
            "hostile_mutations_rejected": 29,
        },
        "claim_ceiling": "Exact conditional closed-column result: one supplied densely defined closed complete coefficient column C constructs h=C* C as a closed form, T=|C| and, when C a^-1 is bounded, R=T a^-1 with the same norm; exact column intertwiners shared with a pass charge/bath reductions to R and R*R. Current native custody supplies no such column, identification, boundedness or intertwiner. No native r_free, T, R, A, B, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["closed_column_theorem"]
    bounded = payload["bounded_realization"]
    reduction = payload["reduction_theorem"]
    native = payload["native_interface_status"]
    assert theorem["native_identification_required"]
    assert not theorem["finite_or_formal_component_list_sufficient"]
    assert not theorem["unclosed_column_sufficient"]
    assert bounded["norm_identity"] == "||R||=||C a^-1||=||B||"
    assert not bounded["factorization_without_bounded_column_sufficient"]
    assert not bounded["seed_only_column_sufficient"]
    assert not reduction["component_labels_without_intertwining_sufficient"]
    assert payload["exact_controls"]["R_norm_square"] == "1/64"
    assert not payload["exact_controls"]["nonclosed_counterexample"]["square_form_closed_on_that_uncompleted_domain"]
    assert not native["actual_native_complete_column_serialized"]
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
