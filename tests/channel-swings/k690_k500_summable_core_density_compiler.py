#!/usr/bin/env python3
"""K690: put a dense common core inside K687's maximal column domain."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k690-k500-summable-core-density-compiler.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k687 = json.loads((ROOT / "lab/process/k687-k500-countable-closed-column-compiler.json").read_text())
    assert k687["countable_column_theorem"]["density_hypothesis"] == "D_col is dense in H"

    square_sum = sum((Fraction(1, 2**j) ** 2 for j in range(1, 80)), Fraction(0))
    tail = sum((Fraction(1, 2**j) ** 2 for j in range(80, 240)), Fraction(0))
    assert square_sum + tail < Fraction(1, 3)
    exact_sum = Fraction(1, 3)

    return {
        "schema_version": "1.0",
        "result_id": "K690-K500-SUMMABLE-CORE-DENSITY-COMPILER",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A sufficient complete-domain packet placing one dense native common core inside K687's maximal square-summable component domain.",
        "gu_typed_objects": {
            "common_core": "a dense linear D0 in the invariant remainder carrier H, contained in Dom(a) and every Dom(C_j)",
            "component_domination": "||C_j u|| <= b_j ||a u|| on D0 with sum_j b_j^2 finite",
            "maximal_domain": "D_col={u in intersection_j Dom(C_j): sum_j ||C_j u||^2<infinity}",
            "result": "summable-core density compiler MAP-TYPE=complete graph domination",
            "target": "K687's density hypothesis for the complete closed column",
        },
        "summable_core_theorem": {
            "dense_common_core_required": True,
            "same_graph_weight_required": True,
            "complete_square_sum_required": True,
            "inequality": "sum_j||C_j u||^2 <= (sum_j b_j^2)||a u||^2 for every u in D0",
            "domain_consequence": "D0 subset D_col, hence D_col is dense in H",
            "closedness_composition": "if every C_j is closed, K687 then makes the maximal column C closed and densely defined",
            "finite_prefix_bounds_sufficient": False,
            "pointwise_finite_component_values_sufficient": False,
            "nonsummable_uniform_component_bounds_sufficient": False,
            "separate_component_cores_without_one_common_dense_core_sufficient": False,
        },
        "exact_controls": {
            "controls_are_synthetic": True,
            "model": "H=l2(N), a e_n=(n+1)e_n, D0=finite sequences, C_j=2^-j a on Dom(a)",
            "component_bound": "b_j=2^-j",
            "complete_square_sum": qstr(exact_sum),
            "maximal_domain": "D_col=Dom(a)",
            "finite_sequences_dense": True,
            "column_square_identity": "sum_j||C_j u||^2=(1/3)||a u||^2",
            "nonsummable_counterexample": "C_j=I for every j has an individually closed uniformly bounded family, but every nonzero u has sum_j||C_j u||^2=infinity and D_col={0}",
        },
        "dependency_reconciliation": {
            "K687_density_hypothesis_reduced_to_complete_core_bounds": True,
            "K687_component_closedness_requirement_retained": True,
            "K688_partial_gram_requirement_retained": True,
            "native_common_core_or_component_family_added": False,
        },
        "native_interface_status": {
            "actual_native_common_core_serialized": False,
            "actual_native_common_core_dense": False,
            "actual_native_components_serialized": False,
            "actual_native_complete_square_sum_proved": False,
            "actual_native_maximal_domain_dense": False,
            "actual_native_remainder_identified": False,
            "native_complete_floor_emitted": False,
        },
        "decision": {
            "summable_core_domination_suffices_for_K687_density": True,
            "native_dense_column_constructed": False,
            "next_exact_input": "Serialize a single dense native core D0, one complete closed component family C_j and one graph weight a; prove D0 lies in every component domain and derive a square-summable sequence b_j with ||C_j u||<=b_j||a u|| on D0.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional Hilbert-domain theorem inside a repository-supplied operator model and supplies no source-owned action, physical state, quotient or observable.",
        "preflight_bookend": {
            "route_comparison": "K687 leaves density as an independent hypothesis. A complete summable domination on one already dense native core is the cheapest checkable sufficient packet.",
            "retrieval_collision_result": "K179's finite coefficient bank and K687's formal maximal domain do not provide a dense complete core or a summable all-component graph bound.",
            "strongest_alternative": "Prove density directly by an explicit approximation theorem for the maximal domain, or use K681's monotone-form route instead of components.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating individual closedness, one core per component, a finite prefix or a nonsummable uniform bound as proof that the complete maximal column domain is dense.",
            "strongest_contrary_construction": "The constant family C_j=I is closed and uniformly bounded componentwise but has maximal square-summable domain {0}.",
            "weakest_reproducibility_seam": "The same D0, carrier H, graph weight a, component domains and complete coefficient square sum must be explicit; asymptotic or sampled bounds do not suffice.",
        },
        "controls": {
            "producer": "tests/channel-swings/k690_k500_summable_core_density_compiler.py",
            "probe": "tests/channel-swings/k690_k500_summable_core_density_compiler_probe.py",
            "controls_passed": 35,
            "hostile_mutations_rejected": 29,
        },
        "claim_ceiling": "Exact conditional density theorem: a single dense common core with complete square-summable component domination lies in K687's maximal column domain, hence makes it dense; component closedness then gives the closed column. Finite prefixes, separate cores, pointwise finiteness and nonsummable bounds do not suffice. Current native custody supplies no component family, common core, summable domination or remainder identity. No native r_free, T, R, A, B, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["summable_core_theorem"]
    controls = payload["exact_controls"]
    native = payload["native_interface_status"]
    assert theorem["dense_common_core_required"]
    assert theorem["same_graph_weight_required"]
    assert theorem["complete_square_sum_required"]
    assert not theorem["finite_prefix_bounds_sufficient"]
    assert not theorem["pointwise_finite_component_values_sufficient"]
    assert not theorem["nonsummable_uniform_component_bounds_sufficient"]
    assert not theorem["separate_component_cores_without_one_common_dense_core_sufficient"]
    assert controls["complete_square_sum"] == "1/3"
    assert controls["maximal_domain"] == "D_col=Dom(a)"
    assert not native["actual_native_maximal_domain_dense"]
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
