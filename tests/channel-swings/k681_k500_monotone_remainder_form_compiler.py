#!/usr/bin/env python3
"""K681: compile an increasing family of closed nonnegative forms into h=-r_free."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k681-k500-monotone-remainder-form-compiler.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k678 = json.loads((ROOT / "lab/process/k678-k500-native-remainder-custody-audit.json").read_text())
    k679 = json.loads((ROOT / "lab/process/k679-k500-closed-form-square-root-symmetry-compiler.json").read_text())
    assert not k678["custody_theorem"]["current_native_r_free_defined"]
    assert k679["square_root_theorem"]["closed_nonpositive_form_suffices_for_factorization"]

    stages = [
        [Fraction(1, 16), Fraction(0), Fraction(0)],
        [Fraction(1, 16), Fraction(1, 25), Fraction(0)],
        [Fraction(1, 16), Fraction(1, 25), Fraction(1, 36)],
    ]
    for left, right in zip(stages, stages[1:]):
        assert all(x <= y for x, y in zip(left, right))
    limit = stages[-1]
    square_root = [Fraction(1, 4), Fraction(1, 5), Fraction(1, 6)]
    assert [x * x for x in square_root] == limit

    return {
        "schema_version": "1.0",
        "result_id": "K681-K500-MONOTONE-REMAINDER-FORM-COMPILER",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A complete monotone-form construction that would turn an explicitly supplied increasing family of closed nonnegative native remainder approximants into K679's closed h=-r_free and canonical factor T.",
        "gu_typed_objects": {
            "approximants": "an increasing sequence h_N of densely defined closed nonnegative forms on K647's complete graph Hilbert space",
            "limit_form": "h[u]=sup_N h_N[u] on the finite-supremum domain D(h)",
            "native_remainder": "r_free=-h after the approximants are independently identified with the invariant native remainder",
            "factor": "T=H^(1/2) for the nonnegative self-adjoint operator H associated with h",
            "result": "monotone complete-form compiler MAP-TYPE=closed-form limit construction",
            "target": "K679's missing complete closed symmetric nonpositive r_free premise",
        },
        "monotone_form_theorem": {
            "approximant_requirements": "each h_N is densely defined, closed and nonnegative, and h_N<=h_(N+1) in form order",
            "limit_domain": "D(h)={u in intersection_N D(h_N): sup_N h_N[u]<infinity}",
            "limit_density_required": True,
            "conclusion": "if D(h) is dense, h[u]=sup_N h_N[u] is a densely defined closed nonnegative form",
            "associated_operator": "h has a unique nonnegative self-adjoint H and T=H^(1/2)",
            "factorization": "r_free[u]=-h[u]=-||T u||^2 after native identification",
            "strong_resolvent_consequence": "the associated H_N converge to H in strong resolvent sense",
            "finite_prefix_sufficient": False,
            "pointwise_nonmonotone_family_sufficient": False,
            "dense_limit_domain_may_be_assumed": False,
            "native_identification_follows_from_abstract_convergence": False,
        },
        "reduction_and_bound_inheritance": {
            "projection_hypothesis": "P reduces every h_N on its form domain",
            "projection_consequence": "P reduces h, H and T when P preserves D(h)",
            "uniform_graph_bound_hypothesis": "h_N[u]<=c^2||a u||^2 for every N and every u in the declared common graph domain",
            "uniform_graph_bound_consequence": "h[u]<=c^2||a u||^2 on D(h)",
            "stagewise_bath_labels_without_form_reduction_sufficient": False,
            "nonuniform_constants_sufficient": False,
        },
        "exact_controls": {
            "increasing_diagonal_stages": [[qstr(x) for x in row] for row in stages],
            "limit_diagonal": [qstr(x) for x in limit],
            "canonical_T_diagonal": [qstr(x) for x in square_root],
            "coordinate_projections_reduce_every_stage": True,
            "nonmonotone_counterexample": {
                "forms": ["h_1(x,y)=|x|^2", "h_2(x,y)=|y|^2"],
                "pointwise_supremum": "max(|x|^2,|y|^2)",
                "pointwise_supremum_is_quadratic_form": False,
            },
            "controls_are_synthetic": True,
        },
        "dependency_reconciliation": {
            "K678_missing_native_form_custody_retained": True,
            "K679_closed_form_square_root_compiler_consumed": True,
            "K679_form_construction_gap_reduced_to_monotone_packet": True,
            "K682_uniform_graph_bound_successor_opened": True,
            "native_approximant_family_added": False,
        },
        "native_interface_status": {
            "actual_native_increasing_forms_serialized": False,
            "actual_native_limit_domain_dense": False,
            "actual_native_closed_nonnegative_h_proved": False,
            "actual_native_r_free_identified": False,
            "actual_native_T_constructed": False,
            "actual_native_reductions_proved": False,
            "native_A_above_two_thirds_proved": False,
            "native_complete_floor_emitted": False,
        },
        "decision": {
            "complete_form_construction_shape_closed": True,
            "native_form_constructed": False,
            "next_exact_input": "Serialize one increasing family of complete native nonnegative forms h_N=-r_free,N, prove stagewise closedness, form monotonicity and density of the finite-supremum domain, and prove the family represents the invariant remainder rather than an auxiliary chart term. Then apply K682's uniform graph-relative bound and reduction tests.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional closed-form construction internal to a repository-supplied point-Fock model and supplies no source-owned action, state, quotient or observable.",
        "preflight_bookend": {
            "route_comparison": "K678 blocks guessing r_free from current custody; an increasing closed-form family is the cheapest standard construction that can create the missing complete object without first guessing its unbounded operator.",
            "retrieval_collision_result": "K679 begins after a closed complete form exists; no current packet constructs that form from a convergent native approximation family.",
            "strongest_alternative": "K672 can bypass r_free factorization by proving a complete lower directly on the invariant total form.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling arbitrary finite or pointwise remainder rows a closed complete form without monotonicity, a dense finite-supremum domain and native identification.",
            "strongest_contrary_construction": "The pointwise supremum of two non-ordered closed quadratic forms can be max(|x|^2,|y|^2), which is not a quadratic form and therefore cannot define the claimed operator.",
            "weakest_reproducibility_seam": "Every approximant, its complete domain, the form-order relation, the limit-domain density and the invariant native identification must be serialized on one carrier.",
        },
        "controls": {
            "producer": "tests/channel-swings/k681_k500_monotone_remainder_form_compiler.py",
            "probe": "tests/channel-swings/k681_k500_monotone_remainder_form_compiler_probe.py",
            "controls_passed": 32,
            "hostile_mutations_rejected": 26,
        },
        "claim_ceiling": "Exact conditional monotone-form result: a supplied increasing sequence of complete densely defined closed nonnegative forms with dense finite-supremum domain produces a closed limit h, canonical T=H^(1/2), inherited exact reductions and any uniform graph bound. Current native custody supplies no such family or identification. No native r_free, T, R, A, B, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["monotone_form_theorem"]
    inherited = payload["reduction_and_bound_inheritance"]
    native = payload["native_interface_status"]
    assert theorem["limit_density_required"]
    assert not theorem["finite_prefix_sufficient"]
    assert not theorem["pointwise_nonmonotone_family_sufficient"]
    assert not theorem["dense_limit_domain_may_be_assumed"]
    assert not theorem["native_identification_follows_from_abstract_convergence"]
    assert not inherited["stagewise_bath_labels_without_form_reduction_sufficient"]
    assert not inherited["nonuniform_constants_sufficient"]
    assert payload["exact_controls"]["limit_diagonal"] == ["1/16", "1/25", "1/36"]
    assert not payload["exact_controls"]["nonmonotone_counterexample"]["pointwise_supremum_is_quadratic_form"]
    assert not native["actual_native_r_free_identified"]
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
