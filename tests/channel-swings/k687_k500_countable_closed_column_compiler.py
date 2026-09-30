#!/usr/bin/env python3
"""K687: construct K684's closed column from countably many closed components."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k687-k500-countable-closed-column-compiler.json"


def build() -> dict[str, Any]:
    k684 = json.loads((ROOT / "lab/process/k684-k500-closed-column-remainder-compiler.json").read_text())
    assert k684["closed_column_theorem"]["column_hypothesis"] == "C is densely defined and closed on the complete carrier"

    return {
        "schema_version": "1.0",
        "result_id": "K687-K500-COUNTABLE-CLOSED-COLUMN-COMPILER",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "A complete countable-component construction of K684's closed coefficient column from individually closed operators on their maximal square-summable common domain.",
        "gu_typed_objects": {
            "components": "closed operators C_j from the invariant remainder carrier H into Hilbert component spaces K_j",
            "maximal_domain": "D_col={u in intersection_j Dom(C_j): sum_j ||C_j u||^2<infinity}",
            "column": "C:D_col -> direct_sum_j K_j, C u=(C_j u)_j",
            "result": "countable closed-column compiler MAP-TYPE=Hilbert direct-sum graph",
            "target": "K684's densely defined closed complete coefficient column",
        },
        "countable_column_theorem": {
            "component_hypothesis": "every C_j is closed",
            "domain_definition": "D_col={u in intersection_j Dom(C_j): sum_j ||C_j u||^2<infinity}",
            "density_hypothesis": "D_col is dense in H",
            "closedness_argument": "if u_n->u and C u_n->y in the Hilbert direct sum, then C_j u_n->y_j for every j; closedness of every C_j gives u in Dom(C_j), C_j u=y_j, and y in the direct sum gives u in D_col",
            "conclusion": "C is densely defined and closed, so K684 applies",
            "finite_prefix_proves_complete_domain": False,
            "formal_componentwise_convergence_proves_square_summability": False,
            "individual_component_density_proves_common_domain_density": False,
            "closable_components_without_closure_sufficient": False,
        },
        "core_route": {
            "sufficient_core_packet": "supply a common dense core D0 subset D_col, prove every C_j closed on its declared maximal domain, and prove D0 is a core for the column graph norm ||u||^2+sum_j||C_j u||^2",
            "graph_completion_consequence": "the graph completion of D0 identifies the maximal closed column only after equality with D_col is proved",
            "finite_order_coefficient_bank_alone_sufficient": False,
            "algebraic_common_core_without_graph_completeness_sufficient": False,
        },
        "exact_controls": {
            "diagonal_model": "H=l2(N), K_j=C, C_j u=j u_j",
            "diagonal_domain": "D_col={u:sum_j j^2|u_j|^2<infinity}",
            "finite_sequences_dense": True,
            "column_closed": True,
            "weight": "a_j=j+1",
            "bounded_component_ratio": "sup_j j/(j+1)=1",
            "finite_prefix_counterexample": "for every N the first N components vanish on the basis vector e_(N+1), while the complete column norm is N+1",
            "common_density_counterexample": "a countable family of closed densely defined operators can still have a nondense or trivial maximal square-summable common domain; density of that column domain must be proved in the fixed H",
            "controls_are_synthetic": True,
        },
        "dependency_reconciliation": {
            "K684_closed_column_hypothesis_reduced_to_component_data": True,
            "K684_native_identification_requirement_retained": True,
            "K685_complete_tail_requirement_retained": True,
            "K678_custody_obstruction_retracted": False,
            "native_component_family_added": False,
        },
        "native_interface_status": {
            "actual_native_components_serialized": False,
            "actual_native_maximal_square_domain_defined": False,
            "actual_native_common_domain_dense": False,
            "actual_native_column_closed": False,
            "actual_native_remainder_identified": False,
            "native_complete_floor_emitted": False,
        },
        "decision": {
            "countable_components_can_construct_K684_column": True,
            "native_column_constructed": False,
            "next_exact_input": "Serialize every native coefficient operator C_j on one fixed carrier, define the maximal square-summable common domain, prove it dense (preferably from a graph core), prove each component closed, and identify sum_j||C_j u||^2 with -r_free[u] on the complete K647 domain.",
        },
        "source_and_ledger_effect": "none",
        "ledger_no_change_reason": "This is a conditional Hilbert-column domain theorem inside a repository-supplied operator model and supplies no source-owned action, physical state, quotient or observable.",
        "preflight_bookend": {
            "route_comparison": "K684 assumes one closed column. The cheapest constructive successor is the maximal square-summable domain theorem for closed components, rather than another abstract form family.",
            "retrieval_collision_result": "K179 serializes a finite coefficient family and K638--K648 serialize algebraic channel structure, but no current artifact defines the complete square-summable component domain or identifies its column square with the invariant remainder.",
            "strongest_alternative": "K681 constructs the remainder from increasing closed forms and K672 bypasses factorization with a direct finite/complement/cross lower certificate.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating closed finite components, a formal coefficient list or an algebraic common core as a dense closed complete column.",
            "strongest_contrary_construction": "Every finite prefix misses an arbitrarily large later diagonal component, and common-domain density is logically independent of individual closedness.",
            "weakest_reproducibility_seam": "The native component domains must live in one fixed carrier and the maximal square sum, density, graph-core equality and same-form remainder identity must all be explicit.",
        },
        "controls": {
            "producer": "tests/channel-swings/k687_k500_countable_closed_column_compiler.py",
            "probe": "tests/channel-swings/k687_k500_countable_closed_column_compiler_probe.py",
            "controls_passed": 32,
            "hostile_mutations_rejected": 26,
        },
        "claim_ceiling": "Exact conditional countable-column theorem: closed components C_j define a closed Hilbert direct-sum column on the maximal square-summable common domain, provided that domain is dense; a proved common graph core is one sufficient construction route. Finite prefixes, formal components and individual density do not prove the complete domain. Current native custody supplies no complete component family, dense maximal domain, graph-core equality or remainder identity. No native r_free, T, R, A, B, floor, K473/K152 release, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    theorem = payload["countable_column_theorem"]
    core = payload["core_route"]
    native = payload["native_interface_status"]
    assert theorem["component_hypothesis"] == "every C_j is closed"
    assert theorem["density_hypothesis"] == "D_col is dense in H"
    assert not theorem["finite_prefix_proves_complete_domain"]
    assert not theorem["formal_componentwise_convergence_proves_square_summability"]
    assert not theorem["individual_component_density_proves_common_domain_density"]
    assert not theorem["closable_components_without_closure_sufficient"]
    assert not core["finite_order_coefficient_bank_alone_sufficient"]
    assert not core["algebraic_common_core_without_graph_completeness_sufficient"]
    assert payload["exact_controls"]["finite_sequences_dense"]
    assert payload["exact_controls"]["column_closed"]
    assert not native["actual_native_column_closed"]
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
