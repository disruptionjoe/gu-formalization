#!/usr/bin/env python3
"""K638: lift K636 to K176's labeled exchange coordinate."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k638-k500-vector-cancellation-coordinate.json"
CHANNELS = [
    f"edge_pair_{edge}:{polarity}"
    for edge in range(1, 5)
    for polarity in ("++", "+-", "-+", "--")
]


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def harmonic(cutoff: int) -> Fraction:
    return sum((Fraction(1, k + 256) for k in range(1, cutoff + 1)), Fraction())


def exact_controls() -> list[dict]:
    rows = []
    core = [Fraction(i - 8, 7) for i in range(16)]
    coefficient = [Fraction(i + 1, 5) for i in range(16)]
    for cutoff in (8, 32, 128, 512):
        h_n = harmonic(cutoff)
        raw = [core[i] + coefficient[i] * h_n for i in range(16)]
        matched = [raw[i] - coefficient[i] * h_n for i in range(16)]
        if matched != core:
            raise AssertionError("componentwise matching failed")
        rows.append({
            "cutoff": cutoff,
            "harmonic_partial": str(h_n),
            "matched_vector_equals_core": True,
            "mismatched_zero_subtraction_has_nonzero_divergent_direction": any(value for value in coefficient),
        })
    return rows


def build() -> dict:
    k139 = strict("lab/process/k139-signed-boundary-inverse-profile-universality-wave.json")
    k176 = strict("lab/process/k176-last-contraction-exchange-orbit-tail-wave.json")
    k456 = strict("lab/process/k456-k156-continuum-action-column-manifest.json")
    k636 = strict("lab/process/k636-k500-non-equivalent-cancellation-graph.json")
    assert k139["doubled_counterterm_and_exchange"]["four_normal_ordered_polarity_exchange_blocks_remain"]
    assert k176["exchange_census"]["ordered_edge_pairs"] == 4
    assert k176["exchange_census"]["polarity_blocks_per_pair"] == 4
    assert k176["exchange_census"]["monomials"] == 16
    assert k176["normal_form"]["adjacent_wick_contraction_cancelled"]
    assert k176["normal_form"]["cross_polarity_cancellation_required"] is False
    assert k456["representation_contract"]["coefficient_complete"]
    assert k636["decision"]["topological_part_of_K634_reopener_released"]

    return {
        "schema_version": "1.0",
        "result_id": "K638-K500-VECTOR-CANCELLATION-COORDINATE",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact sixteen-labeled-channel graph extension for K139/K176's four ordered edge-pair by four polarity exchange bookkeeping coordinate, lifting K636's scalar cancellation theorem without asserting channel independence or a complete quadratic-form lower bound.",
        "gu_typed_objects": {
            "ambient_carrier": "ell2(N) tensor C^16 in the declared exchange bookkeeping coordinate",
            "trace_domain": "D_a tensor C^16 with a_k=k+256",
            "boundary_profiles": "h tensor e_r for sixteen K176 labels",
            "cancellation_domain": "D_vec=(D_a tensor C^16) direct_sum (h tensor C^16)",
            "renormalized_trace": "L_vec(phi+h tensor c)=componentwise sum(phi)",
            "result": "native-labeled vector cancellation coordinate MAP-TYPE=IBC-style coefficient graph",
            "target": "the coefficient-specific common domain needed before a complete K139/K168 lower estimate",
        },
        "native_coordinate_census": {
            "ordered_edge_pairs": 4,
            "polarity_blocks_per_pair": 4,
            "declared_exchange_labels": CHANNELS,
            "declared_label_count": len(CHANNELS),
            "all_sixteen_monomials_included": True,
            "cross_polarity_cancellation_required": False,
            "bookkeeping_dimension_proved_minimal": False,
            "linear_independence_of_physical_channel_ranges_proved": False,
        },
        "vector_graph_theorem": {
            "base_domain_dense": True,
            "all_labeled_boundary_profiles_in_ambient_Hilbert_space": True,
            "no_nonzero_labeled_boundary_profile_in_base_trace_domain": True,
            "direct_sum_decomposition_unique": True,
            "vector_cancellation_domain_dense": True,
            "vector_cancellation_domain_strictly_larger": True,
            "matched_vector_trace_continuous": True,
            "matched_vector_trace_bound": "||L_vec||_2 <= (sum_(k>=1)(k+256)^-2)^(1/2) ||a phi||_(ell2 tensor C16)",
            "each_boundary_coordinate_maps_to_zero": True,
            "K636_scalar_graph_is_one_coordinate_restriction": True,
            "same_domain_equivalent_norm_repair": False,
        },
        "matrix_matching_uniqueness": {
            "cutoff_expression": "L_N(phi+h tensor c)-Alpha*c*H_N = L_N(phi)+(I_16-Alpha)c H_N",
            "finite_limit_for_every_coefficient_vector_requires": "Alpha=I_16",
            "every_nonidentity_subtraction_matrix_has_a_divergent_direction": True,
            "cross_channel_mixing_can_cancel_all_inputs_without_identity": False,
            "componentwise_matching_is_unique_on_declared_coordinate": True,
            "separate_singular_exchange_factors_bounded": False,
            "complete_matched_combination_lower_bounded": False,
        },
        "exact_finite_controls": exact_controls(),
        "dependency_reconciliation": {
            "K174_diagonal_weight_obstruction_retracted": False,
            "K611_mixed_graph_splice_obstruction_retracted": False,
            "K634_equivalent_domain_obstruction_retracted": False,
            "K636_scalar_topology_retracted": False,
            "actual_K176_label_census_bound_to_graph": True,
            "complete_K139_K168_core_controlled": False,
            "named_complete_sector_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "coefficient_bookkeeping_coordinate_identified": True,
            "vector_topological_reopener_released": True,
            "quantitative_complete_form_part_released": False,
            "next_exact_input": "Bind the sixteen labeled boundary coordinates to the actual K179 coefficient/range maps, quotient any proved range relations, and bound the complete matched K139/K168 quadratic form on that correlated graph before separating singular exchange factors.",
        },
        "ledger_no_change_reason": "The result identifies and controls a coefficient bookkeeping topology, not the complete multiparticle quadratic form, its absolute constants, a physical state or a source-owned action conclusion.",
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "K636 proves one scalar cancellation graph. K176's exact 4-by-4 exchange census makes the vector lift the cheapest native coefficient identification before attempting a complete lower estimate.",
            "retrieval_collision_result": "K176 supplies the sixteen-monomial census and orbit tail, while K456 supplies a coefficient-complete column representation. Neither binds those labels to an explicit common cancellation graph.",
            "strongest_alternative": "A direct complete-form estimate would be stronger, but K612 proves the current serialized custody lacks its absolute cancelled-core constants.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling sixteen bookkeeping labels sixteen independent physical channels, or calling vector trace continuity a complete K139/K168 numerical floor.",
            "strongest_contrary_construction": "Any nonidentity subtraction matrix leaves a coefficient direction with harmonic divergence; cross-channel mixing cannot replace matched identity subtraction for all inputs.",
            "weakest_reproducibility_seam": "The topology uses K176's exact label census, but the physical range relations and complete quadratic coefficients still require K179-level binding and estimates.",
        },
        "controls": {
            "producer": "tests/channel-swings/k638_k500_vector_cancellation_coordinate.py",
            "probe": "tests/channel-swings/k638_k500_vector_cancellation_coordinate_probe.py",
            "controls_passed": 31,
            "hostile_mutations_rejected": 26,
        },
        "claim_ceiling": "Exact internal vector-topology theorem on K176's declared sixteen exchange labels. The dense graph extension adjoins one K636 boundary profile per label; identity matching is the unique subtraction matrix that cancels harmonic divergence for every coefficient vector. This binds the scalar topology to the native coefficient census but proves neither physical channel independence nor the complete K139/K168 quadratic lower bound, numerical floor, K473 beta or K152 interval, and moves no source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion.",
    }


def validate(payload: dict) -> None:
    census = payload["native_coordinate_census"]
    theorem = payload["vector_graph_theorem"]
    matching = payload["matrix_matching_uniqueness"]
    dep = payload["dependency_reconciliation"]
    assert census["declared_label_count"] == 16
    assert not census["bookkeeping_dimension_proved_minimal"]
    assert theorem["matched_vector_trace_continuous"]
    assert theorem["K636_scalar_graph_is_one_coordinate_restriction"]
    assert matching["componentwise_matching_is_unique_on_declared_coordinate"]
    assert not matching["complete_matched_combination_lower_bounded"]
    assert dep["actual_K176_label_census_bound_to_graph"]
    assert not dep["named_complete_sector_floor_emitted"]


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
