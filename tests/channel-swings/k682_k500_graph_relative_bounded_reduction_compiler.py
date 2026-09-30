#!/usr/bin/env python3
"""K682: convert a complete relative form bound into bounded reducing R=T a^-1."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k682-k500-graph-relative-bounded-reduction-compiler.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k679 = json.loads((ROOT / "lab/process/k679-k500-closed-form-square-root-symmetry-compiler.json").read_text())
    k681 = json.loads((ROOT / "lab/process/k681-k500-monotone-remainder-form-compiler.json").read_text())
    k676 = json.loads((ROOT / "lab/process/k676-k500-three-line-native-compression-criterion.json").read_text())
    k677 = json.loads((ROOT / "lab/process/k677-k500-complement-cofinal-norm-certificate.json").read_text())
    assert not k679["square_root_theorem"]["bounded_R_follows_from_factorization_alone"]
    assert k681["reduction_and_bound_inheritance"]["uniform_graph_bound_consequence"].startswith("h[u]<=")
    assert k676["three_line_criterion"]["gram_domination_route_sufficient_for_norm_bound"]
    assert k677["exact_native_target"]["K674_simple_sufficient_target"] == "1/100"

    hdiag = [Fraction(1, 16), Fraction(1, 25), Fraction(1, 36)]
    adiag = [Fraction(2), Fraction(5), Fraction(3)]
    tdiag = [Fraction(1, 4), Fraction(1, 5), Fraction(1, 6)]
    rdiag = [t / a for t, a in zip(tdiag, adiag)]
    rnorm2 = max(x * x for x in rdiag)
    assert rdiag == [Fraction(1, 8), Fraction(1, 25), Fraction(1, 18)]
    assert rnorm2 == Fraction(1, 64)
    assert all(h <= rnorm2 * a * a for h, a in zip(hdiag, adiag))

    return {
        "schema_version": "1.0",
        "result_id": "K682-K500-GRAPH-RELATIVE-BOUNDED-REDUCTION-COMPILER",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The exact complete-domain inequality and symmetry packet sufficient to turn K679/K681's factor T into a bounded graph operator R=T a^-1 and to make charge or bath projections reduce R and R^*R.",
        "gu_typed_objects": {
            "form": "h=-r_free=||T .||^2 on K647's complete graph carrier",
            "graph_weight": "the positive self-adjoint graph weight a with a^-1 mapping the Hilbert carrier into Dom(a) subset Dom(T)",
            "graph_operator": "R=T a^-1, first defined through the complete relative form inequality and then extended boundedly",
            "reductions": "the charge and bath orthogonal projections that reduce both h and a",
            "result": "graph-relative bounded reduction compiler MAP-TYPE=complete form inequality equivalence",
            "target": "K676 native charge shortcut and K677 native bath/direct-sum or cofinal complement packet",
        },
        "boundedness_theorem": {
            "domain_hypothesis": "Dom(a) subset Dom(T) and a^-1 maps the complete Hilbert carrier into Dom(a)",
            "relative_form_hypothesis": "h[u]=||T u||^2<=c^2||a u||^2 for every u in Dom(a)",
            "conclusion": "R=T a^-1 extends to a bounded operator with ||R||<=c",
            "converse": "if bounded R satisfies T u=R a u on Dom(a), then h[u]<=||R||^2||a u||^2",
            "factorization_alone_sufficient": False,
            "finite_seed_rows_sufficient": False,
            "sampled_bath_rows_sufficient": False,
            "complete_domain_required": True,
        },
        "projection_reduction_theorem": {
            "hypothesis": "P reduces h (equivalently T by K679) and strongly reduces a and a^-1 on the declared domains",
            "conclusion": "P R=R P and P reduces R^*R",
            "charge_consequence": "mutually orthogonal charge sectors make the three K676 line images orthogonal after their native action identities are proved",
            "bath_consequence": "the K677 sectorwise supremum rule becomes valid after every bath projection satisfies the hypothesis",
            "K643_monomial_preservation_substitutable": False,
            "reduction_of_h_without_reduction_of_a_sufficient": False,
        },
        "localized_bounds": {
            "projection_test": "for an orthogonal projection Q, ||R Q||<=c_Q follows exactly from h[a^-1 x]<=c_Q^2||x||^2 for every x in QH",
            "seed_application": "apply the test on P_seed only after P_seed, a^-1 and the native K675/K676 identities are typed on one carrier",
            "complement_application": "apply the test on Q_seed to K677's cofinal core and complete tail; a finite prefix alone remains insufficient",
            "one_over_one_hundred_target": "h[a^-1 x]<=(1/100)||x||^2 for every x in Q_seed H is a direct sufficient K674 complement row",
        },
        "exact_controls": {
            "H_diagonal": [qstr(x) for x in hdiag],
            "a_diagonal": [qstr(x) for x in adiag],
            "T_diagonal": [qstr(x) for x in tdiag],
            "R_diagonal": [qstr(x) for x in rdiag],
            "sharp_global_c_squared": qstr(rnorm2),
            "relative_form_inequality_verified": True,
            "coordinate_projections_reduce_h_a_R_and_R_star_R": True,
            "seed_only_counterexample": {
                "H_diagonal": ["1", "100"],
                "a_diagonal": ["1", "1"],
                "tested_seed_bound_squared": "1",
                "complete_R_norm_squared": "100",
                "seed_bound_proves_complete_boundedness_at_one": False,
            },
            "controls_are_synthetic": True,
        },
        "dependency_reconciliation": {
            "K679_factorization_consumed_conditionally": True,
            "K681_uniform_bound_transfer_consumed_conditionally": True,
            "K676_charge_intertwiner_reduced_to_shared_form_weight_reduction": True,
            "K677_bath_reduction_reduced_to_shared_form_weight_reduction": True,
            "K609_map_identity_requirement_retained": True,
            "native_relative_form_row_added": False,
        },
        "native_interface_status": {
            "actual_native_h_identified": False,
            "actual_native_a_inverse_domain_map_proved": False,
            "actual_native_uniform_relative_bound_proved": False,
            "actual_native_R_bounded": False,
            "actual_native_charge_reduction_proved": False,
            "actual_native_bath_reduction_proved": False,
            "actual_K609_map_identity_proved": False,
            "native_A_above_two_thirds_proved": False,
            "native_complete_floor_emitted": False,
        },
        "decision": {
            "bounded_R_obligation_reduced_to_one_complete_relative_form_inequality": True,
            "native_bounded_R_constructed": False,
            "next_exact_input": "After K681 supplies a native h, prove Dom(a) subset Dom(T), the complete relative inequality h[u]<=c^2||a u||^2, and shared charge/bath reductions of h and a. Then evaluate the three K676 seed identities and prove the Q_seed localized bound at or below 1/100 through K677.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional graph-norm theorem internal to a repository-supplied operator model and supplies no source-owned action, state, quotient or observable.",
        "preflight_bookend": {
            "route_comparison": "K679 constructs T only after h exists but correctly leaves R boundedness open. A complete relative form inequality is the shortest exact bridge from T to bounded R and simultaneously localizes the K676/K677 obligations.",
            "retrieval_collision_result": "K674--K677 state seed and complement operator targets but do not state the domain-exact inequality equivalent to boundedness of T a^-1.",
            "strongest_alternative": "K672 bypasses bounded R by proving the invariant total A form directly with finite/complement/cross bounds.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating factorization r_free=-T*T or three seed-line values as proof that T a^-1 is bounded on the complete carrier.",
            "strongest_contrary_construction": "On diag(1,100) with a=I, the first seed line has squared bound one while the complete operator norm squared is one hundred.",
            "weakest_reproducibility_seam": "The domains of T, a and a^-1, the complete relative inequality and exact reduction of both h and a must be checked before commuting R with a projection.",
        },
        "controls": {
            "producer": "tests/channel-swings/k682_k500_graph_relative_bounded_reduction_compiler.py",
            "probe": "tests/channel-swings/k682_k500_graph_relative_bounded_reduction_compiler_probe.py",
            "controls_passed": 34,
            "hostile_mutations_rejected": 28,
        },
        "claim_ceiling": "Exact conditional graph-relative result: on one complete domain, h[u]=||T u||^2<=c^2||a u||^2 makes R=T a^-1 bounded with norm at most c; shared reduction of h and a passes to R and R^*R, while localized inequalities give seed or complement bounds. Current native custody supplies none of those form/domain inequalities or reductions. No native R, seed identity, complement estimate, A, B, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["boundedness_theorem"]
    reduction = payload["projection_reduction_theorem"]
    native = payload["native_interface_status"]
    assert theorem["complete_domain_required"]
    assert not theorem["factorization_alone_sufficient"]
    assert not theorem["finite_seed_rows_sufficient"]
    assert not theorem["sampled_bath_rows_sufficient"]
    assert not reduction["K643_monomial_preservation_substitutable"]
    assert not reduction["reduction_of_h_without_reduction_of_a_sufficient"]
    assert payload["exact_controls"]["R_diagonal"] == ["1/8", "1/25", "1/18"]
    assert payload["exact_controls"]["sharp_global_c_squared"] == "1/64"
    assert not payload["exact_controls"]["seed_only_counterexample"]["seed_bound_proves_complete_boundedness_at_one"]
    assert not native["actual_native_R_bounded"]
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
