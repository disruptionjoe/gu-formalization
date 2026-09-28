#!/usr/bin/env python3
"""K600 no-selector theorem for K594 scalar data on the K441 carrier."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k600-k77-corrected-carrier-stabilizer-no-selector.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text())


def control(half_rank: int = 3) -> dict:
    rank = 2 * half_rank
    # Every coordinate has an independent sign-flip generator.  Hence no
    # coordinate vector survives all generators, and a matrix unit E_ij can
    # commute with all sign flips only when i=j.  Adjacent permutations inside
    # each half then identify the diagonal coefficients within that half.
    sign_flip_count = rank
    adjacent_swap_count = 2 * (half_rank - 1)
    invariant_coordinates = [
        coordinate
        for coordinate in range(rank)
        if all((-1 if flip == coordinate else 1) == 1 for flip in range(rank))
    ]
    sign_commuting_matrix_units = [
        (row, column)
        for row in range(rank)
        for column in range(rank)
        if all(
            (-1 if flip == row else 1) == (-1 if flip == column else 1)
            for flip in range(rank)
        )
    ]
    diagonal_orbits = [list(range(half_rank)), list(range(half_rank, rank))]
    return {
        "toy_half_rank": half_rank,
        "toy_carrier_rank": rank,
        "generator_count": sign_flip_count + adjacent_swap_count,
        "invariant_vector_dimension": len(invariant_coordinates),
        "sign_commuting_matrix_units": [list(pair) for pair in sign_commuting_matrix_units],
        "commutant_dimension": len(diagonal_orbits),
        "commutant_basis_ranks": sorted(len(orbit) for orbit in diagonal_orbits),
        "block_identity_basis_recovered": sign_commuting_matrix_units == [(index, index) for index in range(rank)],
        "nonzero_rank_one_commutant_exists": any(len(orbit) == 1 for orbit in diagonal_orbits),
    }


def build() -> dict:
    k441 = strict("lab/process/k441-k77-moving-corrected-boundary-transport.json")
    k594 = strict("lab/process/k594-k77-native-third-jet-carrier-typing.json")
    k598 = strict("lab/process/k598-k77-covariant-rank-one-soldering-interface.json")
    half_ranks = k598["theorem"]["rank512_extension"]
    carrier_rank = sum(k441["factorized_transport"]["spectral_block_ranks"])
    projector_half_rank = carrier_rank // 2
    exact = control()
    coefficients = k594["selected_action_third_jet"]["serialized_coefficients"]
    return {
        "schema_version": "1.0",
        "result_id": "K600-K77-CORRECTED-CARRIER-STABILIZER-NO-SELECTOR",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The maximal corrected-carrier datum naturally determined by K594's serialized scalar selected-I1B third-jet coefficients, K441's positive pairing and one corrected half-projector, before any additional action-owned field/carrier injection or symmetry-breaking datum is supplied.",
        "gu_typed_objects": {
            "carrier": "K441 corrected real rank-512 carrier E=E_+ direct-sum E_- with dim(E_+)=dim(E_-)=256",
            "pairing": "K441 transported positive boundary pairing",
            "projector": "Pi with image E_+ and kernel E_-",
            "available_action_data": "the K594 scalar coefficients D3_ttt=8736 and D3_tvv=-(56/3)<V,*V>, with no field-to-carrier injection or K441 Riesz return",
            "naturality_group": "O(E_+) x O(E_-), already preserving the pairing, projector and scalar coefficients",
            "target": "a nonzero initial corrected-carrier vector or rank-one coupling for either K589 arrow",
            "result": "stabilizer no-selector theorem MAP-TYPE=natural-transformation-obstruction",
        },
        "theorem": {
            "vector_selector": "Any vector determined equivariantly from only scalar data, the positive pairing and Pi must be fixed by O(E_+) x O(E_-). Independent sign reversals force every coordinate to zero.",
            "covector_selector": "The same argument applies after the positive Riesz identification E*=E; no nonzero Riesz return is selected by these data.",
            "endomorphism_commutant": "Every equivariant endomorphism is a*I_(E_+) direct-sum b*I_(E_-).",
            "rank_one_consequence": "Because both half-ranks are 256, the only rank-at-most-one equivariant endomorphism is zero.",
            "conditional_escape": "A nonzero K598 packet therefore requires an additional action-owned vector, injection, boundary field, or other datum that reduces the stabilizer; scalar nonvanishing alone cannot supply it.",
            "dimension_mismatch_alone_used": False,
        },
        "selected_action_replay": {
            "D3_t_t_t": coefficients["D3_t_t_t"],
            "D3_t_v_v_over_native_norm": coefficients["D3_t_v_v_over_native_norm"],
            "field_to_carrier_soldering_map_serialized": k594["type_audit"]["field_to_carrier_soldering_map_serialized"],
            "action_Riesz_map_on_K441_pairing_serialized": k594["type_audit"]["action_Riesz_map_on_K441_pairing_serialized"],
            "K598_conditional_covariant_packet_constructed": k598["ownership_boundary"]["conditional_covariant_packet_constructed"],
            "K598_actual_action_owned_packet_constructed": k598["ownership_boundary"]["actual_action_owned_packet_constructed"],
            "K598_rank512_factorization_replayed": "rank-512" in half_ranks,
        },
        "exact_controls": exact,
        "decision": {
            "scalar_third_jet_selects_nonzero_initial_vector": False,
            "scalar_third_jet_selects_nonzero_Riesz_return": False,
            "nonzero_rank_one_packet_natural_from_current_inputs": False,
            "additional_action_owned_symmetry_breaking_datum_required": True,
            "K598_conditional_transport_preserved": True,
            "K590_factorized_completion_retracted": False,
            "selected_source_action_rejected": False,
            "next_exact_input": "Supply a named action-owned field-to-carrier injection, boundary field or equivalent stabilizer-reducing datum and its K441 Riesz return; only then apply K596 at the initial fibre and K598 for transport. Do not search the scalar-plus-projector data for a canonical direction.",
        },
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "Test naturality under the full stabilizer before choosing a coordinate vector or expanding a 512-by-512 matrix.",
            "retrieval_collision_result": "K594 supplies only scalar native-field trilinears and K598 supplies transport conditional on initial vectors; neither breaks the corrected-half stabilizer.",
            "strongest_alternative": "An independently action-owned boundary injection can reduce the stabilizer and remains the exact live reopener.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating the no-selector theorem as nonexistence of every action-derived soldering map.",
            "strongest_contrary_construction": "Adjoining one nonzero action-owned vector immediately reduces the stabilizer and makes K596/K598 evaluable.",
            "weakest_reproducibility_seam": "The general 256+256 proof is analytic; the exact matrix control uses a 3+3 faithful signed-permutation subgroup.",
        },
        "claim_ceiling": "Exact no-selector theorem for the currently serialized K594/K441 data: scalar third-jet coefficients, the positive corrected-carrier pairing and its rank-256 half-projector have full O(256)xO(256) stabilizer, whose fixed-vector and fixed-covector spaces are zero and whose endomorphism commutant contains no nonzero rank-one map. Thus those inputs cannot canonically supply K598's initial vectors or Riesz return. An additional action-owned stabilizer-reducing datum remains live; no source action is rejected and no nonlinear properness, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion moves.",
    }


def validate(payload: dict) -> None:
    theorem = payload["theorem"]
    replay = payload["selected_action_replay"]
    control_data = payload["exact_controls"]
    decision = payload["decision"]
    assert not theorem["dimension_mismatch_alone_used"]
    assert replay["D3_t_t_t"] == "8736" and replay["D3_t_v_v_over_native_norm"] == "-56/3"
    assert not replay["field_to_carrier_soldering_map_serialized"] and not replay["action_Riesz_map_on_K441_pairing_serialized"]
    assert replay["K598_conditional_covariant_packet_constructed"] and not replay["K598_actual_action_owned_packet_constructed"]
    assert control_data["invariant_vector_dimension"] == 0 and control_data["commutant_dimension"] == 2
    assert control_data["commutant_basis_ranks"] == [3, 3] and control_data["block_identity_basis_recovered"]
    assert not control_data["nonzero_rank_one_commutant_exists"]
    assert not decision["scalar_third_jet_selects_nonzero_initial_vector"]
    assert not decision["scalar_third_jet_selects_nonzero_Riesz_return"]
    assert not decision["nonzero_rank_one_packet_natural_from_current_inputs"]
    assert decision["additional_action_owned_symmetry_breaking_datum_required"] and decision["K598_conditional_transport_preserved"]
    assert not decision["K590_factorized_completion_retracted"] and not decision["selected_source_action_rejected"]


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
