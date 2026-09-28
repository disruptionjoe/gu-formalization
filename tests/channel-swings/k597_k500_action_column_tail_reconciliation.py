#!/usr/bin/env python3
"""K597 reconciliation of K456/K574 with K595's K583 moment interface."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k597-k500-action-column-tail-reconciliation.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text())


def build() -> dict:
    k456 = strict("lab/process/k456-k156-continuum-action-column-manifest.json")
    k574 = strict("lab/process/k574-k176-sharp-post-adjoint-tail-reconciliation.json")
    k575 = strict("lab/process/k575-complete-m-dual-residual-sharp-tail-enclosure.json")
    k583 = strict("lab/process/k583-k500-all-level-tensor-pair-leakage.json")
    k595 = strict("lab/process/k595-k500-action-vector-coefficient-sufficiency.json")
    rep = k456["representation_contract"]
    exchange = k456["column_decomposition"]["exchange_component"]
    sharp = k574["sharp_tail"]
    residual = k575["complete_M_dual_residual_norm_square"]
    old_tail, new_tail = Fraction(exchange["post_order_12_tail_norm_upper"]), Fraction(sharp["sharp_tail_norm_upper"])
    assert old_tail / new_tail == Fraction(40, 3)
    return {
        "schema_version": "1.0",
        "result_id": "K597-K500-ACTION-COLUMN-TAIL-RECONCILIATION",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The exact overlap and non-overlap among K456's coefficient-complete continuum action column, K574's sharp post-order-12 exchange tail, K575's M-dual residual enclosure and K595's three-moment K583 leakage interface.",
        "gu_typed_objects": {
            "carrier": "K162 zero-bath q00/q10 seed exchange orbits and their K500 supported bath levels",
            "action_column": "coefficient-complete convergent W_n v_n representation inherited from K456",
            "pairing": "regular Hilbert pairing transported from M=S* S",
            "result": "action-column/tail reconciliation MAP-TYPE=certificate-composition-boundary",
            "target": "the three normalized K583 moments ||v_n||^2, <v_n,W_n v_n>, ||W_n v_n||^2",
        },
        "K456_representation_replay": {
            "complete_continuum_action_column_serialized": rep["complete_continuum_action_column_serialized"],
            "coefficient_complete": rep["coefficient_complete"],
            "all_order_tail_complete": rep["all_order_tail_complete"],
            "complete_continuum_action_column_numerically_evaluated": rep["complete_continuum_action_column_numerically_evaluated"],
            "resolved_orders": exchange["resolved_orders"],
            "resolved_term_count": exchange["resolved_term_count"],
            "unresolved_required_field_instances": exchange["unresolved_required_field_instances"],
            "old_post_order_12_tail_norm_upper": exchange["post_order_12_tail_norm_upper"],
        },
        "K574_tail_replay": {
            "same_post_left_adjoint_location": k574["compatibility_replay"]["same_post_left_adjoint_location"],
            "same_geometric_tail_shape": k574["compatibility_replay"]["same_geometric_tail_shape"],
            "resolved_through_order": sharp["resolved_through_order"],
            "sharp_post_order_12_tail_norm_upper": sharp["sharp_tail_norm_upper"],
            "exact_improvement_factor": sharp["exact_improvement_factor"],
            "sharp_tail_strictly_smaller": new_tail < old_tail,
        },
        "composition_theorem": {
            "coefficient_serialization_already_complete": True,
            "all_level_exchange_tail_already_serialized": True,
            "K574_sharpens_but_does_not_create_representation_completeness": True,
            "finite_vector_integrals_still_numerically_unevaluated": True,
            "K595_support_only_diagnosis_preserved_for_K177": True,
            "K595_global_next_input_corrected_by_K456_retrieval": True,
            "minimum_remaining_numeric_payload": ["||v_n||^2", "<v_n,W_n v_n>", "||W_n v_n||^2"],
            "full_operator_matrix_not_required": k595["theorem"]["full_operator_matrix_not_required"],
            "full_spectrum_not_required": k595["theorem"]["spectral_diameter_not_required"],
        },
        "non_substitutability": {
            "K575_metric_type": residual["metric_type"],
            "K575_object": "complete M-dual residual norm square for a fixed trial vector",
            "K583_object": "orthogonal leakage of W_n v_n from the cyclic line, uniformly over supported n",
            "K575_is_a_K583_three_moment_evaluation": False,
            "K575_interval_can_replace_K583_moments": False,
            "reason": "The M-dual residual norm uses a different typed target and fixed trial-vector residual; it neither supplies <v_n,W_n v_n> nor separates the cyclic projection uniformly across K500 levels.",
        },
        "decision": {
            "K583_direct_vector_route_preserved": k595["decision"]["K583_direct_vector_route_preserved"],
            "coefficient_reserialization_required": False,
            "new_all_level_tail_derivation_required_before_numerics": False,
            "numerical_three_moment_evaluation_required": True,
            "complete_K500_uniform_leakage_emitted": False,
            "native_noncyclic_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Numerically enclose the 2958 finite K456 vector integrals in the three K583 moment contractions, compose K574's sharp tail exactly once, and prove a uniform normalized bound over the supported q00/q10 levels; do not reserialize the action column or substitute K575's M-dual residual.",
        },
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "Retrieve coefficient-complete action-column and tail artifacts before commissioning new serialization or operator-wide work.",
            "retrieval_collision_result": "K456 already serializes every finite coefficient through order 12 and a complete later-order tail; K574 sharpens that same tail by 40/3.",
            "strongest_alternative": "K575 numerically encloses a nearby M-dual residual, but its typed object cannot substitute for K583's cyclic-projection moments.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling coefficient completeness a numerical evaluation, or importing K575's residual interval as a K583 leakage bound.",
            "strongest_contrary_construction": "Two action vectors can share a residual-norm enclosure while having different cyclic inner products and hence different leakage.",
            "weakest_reproducibility_seam": "The 2958 finite vector integrals remain unevaluated in the required moment contractions and uniformity over all supported levels remains open.",
        },
        "claim_ceiling": "Exact retrieval reconciliation: K456 already supplies a coefficient-complete convergent action-column representation with 2,958 resolved exchange terms and an all-order tail, and K574 sharpens that tail from 3011499/838860800 to 9034497/33554432000. The remaining K583 burden is numerical evaluation of three normalized moments and a uniform level bound. K575's fixed M-dual residual is not substitutable. No leakage bound, floor, K473 beta, source, ledger, canon, paper, public, novelty or physical conclusion is emitted.",
    }


def validate(p: dict) -> None:
    a, t, c, n, d = p["K456_representation_replay"], p["K574_tail_replay"], p["composition_theorem"], p["non_substitutability"], p["decision"]
    assert a["complete_continuum_action_column_serialized"] and a["coefficient_complete"] and a["all_order_tail_complete"]
    assert not a["complete_continuum_action_column_numerically_evaluated"] and a["resolved_term_count"] == 2958
    assert t["same_post_left_adjoint_location"] and t["same_geometric_tail_shape"] and t["exact_improvement_factor"] == "40/3" and t["sharp_tail_strictly_smaller"]
    assert c["coefficient_serialization_already_complete"] and c["all_level_exchange_tail_already_serialized"] and c["finite_vector_integrals_still_numerically_unevaluated"]
    assert c["minimum_remaining_numeric_payload"] == ["||v_n||^2", "<v_n,W_n v_n>", "||W_n v_n||^2"]
    assert not n["K575_is_a_K583_three_moment_evaluation"] and not n["K575_interval_can_replace_K583_moments"]
    assert d["K583_direct_vector_route_preserved"] and d["numerical_three_moment_evaluation_required"]
    assert not any(d[k] for k in ("coefficient_reserialization_required", "new_all_level_tail_derivation_required_before_numerics", "complete_K500_uniform_leakage_emitted", "native_noncyclic_floor_emitted", "K473_released", "native_K152_interval_emitted"))


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--write", action="store_true"); args = parser.parse_args()
    payload = build(); validate(payload); rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered)
    else: print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
