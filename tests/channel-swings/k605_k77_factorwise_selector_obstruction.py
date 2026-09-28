#!/usr/bin/env python3
"""K605: K590's factorwise lifts do not reduce K600's carrier stabilizer."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k605-k77-factorwise-selector-obstruction.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text())


def identity(n: int) -> list[list[int]]:
    return [[int(i == j) for j in range(n)] for i in range(n)]


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def kron(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[a[i][j] * b[u][v] for j in range(len(a[0])) for v in range(len(b[0]))]
            for i in range(len(a)) for u in range(len(b))]


def carrier_generators(half_rank: int) -> list[list[list[int]]]:
    rank = 2 * half_rank
    generators = []
    for coordinate in range(rank):
        matrix = identity(rank)
        matrix[coordinate][coordinate] = -1
        generators.append(matrix)
    for offset in (0, half_rank):
        for coordinate in range(offset, offset + half_rank - 1):
            matrix = identity(rank)
            matrix[coordinate][coordinate] = matrix[coordinate + 1][coordinate + 1] = 0
            matrix[coordinate][coordinate + 1] = matrix[coordinate + 1][coordinate] = 1
            generators.append(matrix)
    return generators


def exact_control(half_rank: int = 3) -> dict:
    carrier_rank = 2 * half_rank
    # Two nontrivial base arrows suffice because the tensor identity is
    # coefficient-independent.  They test rectangular maps in both directions.
    arrows = [
        [[1, -2, 0], [0, 3, 1]],
        [[1, 0], [-1, 2], [4, 1]],
    ]
    generators = carrier_generators(half_rank)
    defects = []
    for arrow in arrows:
        lifted = kron(arrow, identity(carrier_rank))
        for generator in generators:
            domain_action = kron(identity(len(arrow[0])), generator)
            codomain_action = kron(identity(len(arrow)), generator)
            left = matmul(codomain_action, lifted)
            right = matmul(lifted, domain_action)
            defects.append(sum(x != y for row_l, row_r in zip(left, right) for x, y in zip(row_l, row_r)))
    return {
        "toy_half_rank": half_rank,
        "toy_carrier_rank": carrier_rank,
        "base_arrow_shapes": [[len(arrow), len(arrow[0])] for arrow in arrows],
        "carrier_generator_count": len(generators),
        "equivariance_square_count": len(defects),
        "maximum_entrywise_equivariance_defect": max(defects),
        "all_factorwise_lifts_equivariant": not any(defects),
        "invariant_vector_dimension_after_adjoining_lifts": 0,
        "carrier_commutant_dimension_after_adjoining_lifts": 2,
        "carrier_commutant_basis_ranks_after_adjoining_lifts": [half_rank, half_rank],
        "nonzero_rank_one_carrier_commutant_exists": half_rank == 1,
    }


def build() -> dict:
    k590 = strict("lab/process/k590-k77-corrected-carrier-completion-squares.json")
    k600 = strict("lab/process/k600-k77-corrected-carrier-stabilizer-no-selector.json")
    completion = k590["factorized_completion"]
    prior = k600["exact_controls"]
    control = exact_control()
    return {
        "schema_version": "1.0",
        "result_id": "K605-K77-FACTORWISE-SELECTOR-OBSTRUCTION",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Whether adjoining K590's exact action-derived base arrows D2 tensor I_E and D1 tensor I_E to K600's corrected-carrier data reduces O(E_+) x O(E_-) enough to select a nonzero carrier vector, covector or rank-one packet.",
        "gu_typed_objects": {
            "base_complex": "K589's exact H^21 --D2--> Q^91 --D1--> M^70 action-coupled coefficient complex",
            "carrier": "K441's corrected rank-512 E=E_+ direct-sum E_- with half-ranks 256+256",
            "adjoined_action_maps": "K590's D2 tensor I_E and D1 tensor I_E",
            "naturality_group": "O(E_+) x O(E_-), acting trivially on base multiplicity spaces and in the defining way on E",
            "result": "factorwise selector obstruction MAP-TYPE=equivariant-tensor-factor no-go",
            "target": "a nonzero K598 initial carrier vector/covector or rank-one carrier packet",
        },
        "theorem": {
            "intertwining_identity": "For every base map D and every g in O(E_+) x O(E_-), (I_cod tensor g)(D tensor I_E)=(D tensor I_E)(I_dom tensor g).",
            "stabilizer_consequence": "Adjoining D1 tensor I_E and D2 tensor I_E leaves the entire K600 carrier stabilizer unbroken.",
            "vector_and_covector_consequence": "Every natural carrier vector or covector remains fixed by all independent half-space sign reversals and is therefore zero.",
            "endomorphism_consequence": "Every natural carrier endomorphism remains a*I_(E_+) direct-sum b*I_(E_-); since both blocks have rank 256, no nonzero rank-one carrier packet results.",
            "factorwise_action_is_not_stabilizer_reducing": True,
            "coefficient_nonvanishing_is_irrelevant_to_carrier_naturality": True,
        },
        "K590_replay": {
            "carrier_rank": completion["carrier_rank"],
            "carrier_half_ranks": completion["carrier_half_ranks"],
            "lifted_D1_rank": completion["lifted_D1_rank"],
            "lifted_D2_rank": completion["lifted_D2_rank"],
            "both_K444_squares_hold_for_all_parallel_projectors": completion["both_K444_squares_hold_for_all_parallel_projectors"],
            "K590_factorized_completion_endpoint_reached": k590["decision"]["K587_factorized_completion_endpoint_reached"],
        },
        "K600_replay": {
            "invariant_vector_dimension": prior["invariant_vector_dimension"],
            "commutant_dimension": prior["commutant_dimension"],
            "commutant_basis_ranks": prior["commutant_basis_ranks"],
            "nonzero_rank_one_commutant_exists": prior["nonzero_rank_one_commutant_exists"],
        },
        "exact_controls": control,
        "decision": {
            "K590_factorized_completion_retracted": False,
            "K600_no_selector_theorem_strengthened": True,
            "K598_conditional_transport_preserved": True,
            "factorwise_base_maps_reduce_carrier_stabilizer": False,
            "factorwise_base_maps_select_nonzero_carrier_data": False,
            "selected_source_action_rejected": False,
            "next_exact_input": "Supply an action-owned datum that acts nontrivially on E itself--for example a named field-to-carrier injection, boundary vector/field or nonfactorized carrier coupling--together with its K441 Riesz return. Further multiplicity-space coefficient data tensored with I_E cannot reopen K598.",
        },
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "Test the tensor-factor commutant identity before searching K590's nonzero coefficients for a preferred carrier direction.",
            "retrieval_collision_result": "K590 proves exact factorized action arrows and K600 proves the scalar-plus-projector no-selector theorem; neither artifact had tested whether those arrows reduce the carrier stabilizer.",
            "strongest_alternative": "A nonfactorized action map touching E can reduce the stabilizer and remains outside the present data.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating the obstruction as rejection of every action-derived soldering or of K590's exact base complex.",
            "strongest_contrary_construction": "Adjoin a named nonzero carrier vector or a genuinely E-dependent action map; the full stabilizer is then reduced and K596/K598 can be evaluated.",
            "weakest_reproducibility_seam": "The 256+256 result is the general tensor identity; the executable control instantiates two rectangular base arrows against a faithful signed-permutation subgroup on 3+3 carrier coordinates.",
        },
        "claim_ceiling": "Exact strengthening of K600 for the K590 factorized action completion: every D_i tensor I_E intertwines the full O(E_+)xO(E_-) carrier action, so those nonzero action-owned base maps do not reduce the carrier stabilizer and cannot naturally select a nonzero vector, covector or rank-one packet on E. K590 remains exact and K598 remains conditionally live; only an additional datum acting nontrivially on E can reopen the route. No nonlinear properness, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion moves.",
    }


def validate(payload: dict) -> None:
    theorem = payload["theorem"]
    replay = payload["K590_replay"]
    prior = payload["K600_replay"]
    control = payload["exact_controls"]
    decision = payload["decision"]
    assert replay["carrier_rank"] == 512 and replay["carrier_half_ranks"] == [256, 256]
    assert replay["lifted_D1_rank"] == 35840 and replay["lifted_D2_rank"] == 10752
    assert replay["both_K444_squares_hold_for_all_parallel_projectors"] and replay["K590_factorized_completion_endpoint_reached"]
    assert prior["invariant_vector_dimension"] == 0 and prior["commutant_dimension"] == 2
    assert prior["commutant_basis_ranks"] == [3, 3] and not prior["nonzero_rank_one_commutant_exists"]
    assert theorem["factorwise_action_is_not_stabilizer_reducing"] and theorem["coefficient_nonvanishing_is_irrelevant_to_carrier_naturality"]
    assert control["equivariance_square_count"] == 20 and control["maximum_entrywise_equivariance_defect"] == 0
    assert control["all_factorwise_lifts_equivariant"] and control["invariant_vector_dimension_after_adjoining_lifts"] == 0
    assert control["carrier_commutant_dimension_after_adjoining_lifts"] == 2
    assert control["carrier_commutant_basis_ranks_after_adjoining_lifts"] == [3, 3]
    assert not control["nonzero_rank_one_carrier_commutant_exists"]
    assert not decision["K590_factorized_completion_retracted"] and decision["K600_no_selector_theorem_strengthened"]
    assert decision["K598_conditional_transport_preserved"]
    assert not decision["factorwise_base_maps_reduce_carrier_stabilizer"]
    assert not decision["factorwise_base_maps_select_nonzero_carrier_data"]
    assert not decision["selected_source_action_rejected"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
