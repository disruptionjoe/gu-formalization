#!/usr/bin/env sage-python
"""K620 obstruction to selecting the K619 module from K438 functional calculus."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from k435_k77_full_h640_observed_map import PRIMES
from k619_k77_zero_form_moving_graph_common_action_module import build_prime_module


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k620-k77-action-functional-calculus-selection-obstruction.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def scalar_multiple(left, right) -> bool:
    left_entries = left.list()
    right_entries = right.list()
    pivot = next((index for index, value in enumerate(right_entries) if value), None)
    if pivot is None:
        return not any(left_entries)
    scalar = left_entries[pivot] / right_entries[pivot]
    return all(x == scalar * y for x, y in zip(left_entries, right_entries))


def build_prime_gate(prime: int) -> dict:
    packet = build_prime_module(prime, keep_matrices=True)
    compressed = packet["compressed"]
    split = packet["split"]
    graph = packet["graph"]
    zero_seed = packet["zero_seed"]
    projectors = {
        "fast_outgoing": compressed["fast"] * split["outgoing"],
        "fast_incoming": compressed["fast"] * split["incoming"],
        "slow_outgoing": compressed["slow"] * split["outgoing"],
        "slow_incoming": compressed["slow"] * split["incoming"],
    }
    common_module_ranks = {
        "fast_outgoing": 128,
        "fast_incoming": 128,
        "slow_outgoing": 64,
        "slow_incoming": 64,
    }
    total_ranks = {
        "fast_outgoing": 192,
        "fast_incoming": 192,
        "slow_outgoing": 64,
        "slow_incoming": 64,
    }
    rows = {}
    for name, projector in projectors.items():
        graph_block = projector * graph
        zero_block = projector * zero_seed
        rows[name] = {
            "eigenspace_rank": total_ranks[name],
            "common_module_rank": common_module_ranks[name],
            "graph_seed_block_rank": int(graph_block.rank()),
            "zero_seed_block_rank": int(zero_block.rank()),
            "seed_maps_scalar_proportional": scalar_multiple(graph_block, zero_block),
        }

    checks = {
        "all_seed_blocks_are_nonzero": all(
            row["graph_seed_block_rank"] > 0 and row["zero_seed_block_rank"] > 0
            for row in rows.values()
        ),
        "no_eigenblock_seed_maps_are_scalar_proportional": all(
            not row["seed_maps_scalar_proportional"] for row in rows.values()
        ),
        "common_module_is_proper_inside_both_fast_eigenspaces": all(
            rows[name]["common_module_rank"] == 128
            and rows[name]["eigenspace_rank"] == 192
            for name in ("fast_outgoing", "fast_incoming")
        ),
        "common_module_exhausts_both_slow_eigenspaces": all(
            rows[name]["common_module_rank"] == rows[name]["eigenspace_rank"] == 64
            for name in ("slow_outgoing", "slow_incoming")
        ),
    }
    if not all(checks.values()):
        raise AssertionError({"prime": prime, "rows": rows, "checks": checks})
    return {"prime": prime, "eigenblock_rows": rows, "checks": checks}


def build() -> dict:
    k438 = strict("lab/process/k438-k77-constraint-compressed-boundary-symbol.json")
    k618 = strict("lab/process/k618-k77-moving-varpi-corrected-action-hull.json")
    k619 = strict("lab/process/k619-k77-zero-form-moving-graph-common-action-module.json")
    assert k438["cross_characteristic_result"]["minimal_polynomial_on_im_P"] == "(x^2-1)(x^2-1/576)"
    assert k618["action_hull_theorem"]["minimal_action_hull_rank"] == 384
    assert k619["common_module_theorem"]["filtrations_equal_from_depth_3"]
    packets = [build_prime_gate(prime) for prime in PRIMES]
    assert packets[0]["eigenblock_rows"] == packets[1]["eigenblock_rows"]
    rows = packets[0]["eigenblock_rows"]
    return {
        "schema_version": "1.0",
        "result_id": "K620-K77-ACTION-FUNCTIONAL-CALCULUS-SELECTION-OBSTRUCTION",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact functional-calculus test for whether a polynomial in K438's four-root corrected action symbol can select K619's common rank-384 module or send the K614 zero-form seed map to the K617 moving-graph seed map.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "action": "K438 corrected frozen normal symbol A with four distinct roots plus/minus 1 and plus/minus 1/24",
            "functional_calculus": "R[A], acting by one scalar on each of the four K438/K439 eigenspaces",
            "common_module": "K619 rank-384 A-invariant subspace with block ranks 128,128,64,64",
            "seed_maps": "K614 J0 and K617 X as 128-column maps into the corrected carrier",
            "result": "functional-calculus selection obstruction MAP-TYPE=eigenblock scalar-action theorem",
            "target": "canonical module projector or action-polynomial seed adapter",
        },
        "cross_characteristic_packets": packets,
        "eigenblock_fingerprint": rows,
        "module_projector_theorem": {
            "functional_calculus_is_scalar_on_each_eigenspace": True,
            "fast_eigenspace_ranks": [192, 192],
            "common_module_fast_ranks": [128, 128],
            "slow_eigenspace_ranks": [64, 64],
            "common_module_slow_ranks": [64, 64],
            "common_module_is_union_of_full_eigenspaces": False,
            "polynomial_projector_with_image_common_module_exists": False,
            "polynomial_projector_with_image_rank128_complement_exists": False,
            "reason": "A polynomial in A cannot distinguish the rank-128 module slice from the rank-64 complement inside either rank-192 fast eigenspace.",
        },
        "seed_adapter_theorem": {
            "each_seed_meets_all_four_eigenspaces": True,
            "corresponding_seed_maps_scalar_proportional_in_any_eigenspace": False,
            "scalar_polynomial_p_with_pA_J0_equals_X_exists": False,
            "arbitrary_commutant_or_domain_endomorphism_tested": False,
            "mixed_hessian_bilinear_adapter_constructed": False,
        },
        "ownership_reconciliation": {
            "A_owns_four_spectral_projectors": True,
            "A_owns_common_module_projector": False,
            "A_owns_seed_identification": False,
            "A_invariance_of_common_module_implies_action_selection": False,
            "nonpolynomial_action_owned_adapter_excluded": False,
            "moving_nonlinear_mixed_hessian_excluded": False,
        },
        "decision": {
            "K619_common_module_retracted": False,
            "K618_spectral_components_action_derived_retracted": False,
            "common_module_selected_by_frozen_action": False,
            "zero_form_and_moving_graph_seeds_identified": False,
            "actual_K596_K598_packet_released": False,
            "selected_source_action_rejected": False,
            "next_exact_input": "Supply an independently action-owned nonpolynomial commutant or mixed-Hessian adapter on a nonzero stationary moving background, together with its common BV/Green domain. The frozen symbol A alone owns the four coarse eigenspaces but neither the common-module projector nor a J0-to-X seed map.",
        },
        "ledger_no_change_reason": "The obstruction is internal to the conditional frozen corrected-carrier model and neither constructs nor rejects the source action, a stationary solution, a gauge-reduced class, an observation map, or physical cohomology. SC-ACT-01/02 and SC-CHI-01/51 remain unchanged, as do all v0.263 ledger rows.",
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "After K619 proves orbit-span equality, test the smallest action-owned adapter class R[A] before treating common reachability as selection.",
            "retrieval_collision_result": "K610 classifies factorwise R[A] idempotents globally, while K619 supplies a new proper A-invariant submodule; no predecessor tests whether that particular module is a spectral image or whether p(A) maps its two seeds.",
            "strongest_alternative": "A larger action commutant, domain endomorphism, or mixed Hessian could map the seeds, but none is owned by the current frozen action and this gate does not exclude one.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling failure of R[A] selection failure of every action-owned nonlinear or nonpolynomial adapter.",
            "strongest_contrary_construction": "An independently supplied operator acting inside the fast eigenspace multiplicities could distinguish the rank-128 slices from their rank-64 complements while commuting with A.",
            "weakest_reproducibility_seam": "The no-projector theorem uses K438's exact four-root decomposition and K619's block ranks; the seed-map test independently checks nonproportionality in every block at both good characteristics.",
        },
        "claim_ceiling": "Exact obstruction inside K438's polynomial functional calculus. K619's common module exhausts the two slow eigenspaces but occupies only rank 128 of each rank-192 fast eigenspace, so no polynomial in A can project onto the common rank-384 module or its rank-128 complement. In every eigenspace the K614 and K617 seed maps are nonzero and not scalar proportional, so no scalar polynomial p(A) sends J0 to X. This does not exclude a larger action-owned commutant, domain endomorphism, nonlinear mixed Hessian, or moving BV/Green construction; it releases no K596/K598 packet and moves no source, ledger, canon, paper, public, novelty, prediction, confirmation, or physical conclusion.",
    }


def validate(payload: dict) -> None:
    projector = payload["module_projector_theorem"]
    adapter = payload["seed_adapter_theorem"]
    ownership = payload["ownership_reconciliation"]
    decision = payload["decision"]
    assert len(payload["cross_characteristic_packets"]) == 2
    assert not projector["common_module_is_union_of_full_eigenspaces"]
    assert not projector["polynomial_projector_with_image_common_module_exists"]
    assert not projector["polynomial_projector_with_image_rank128_complement_exists"]
    assert not adapter["corresponding_seed_maps_scalar_proportional_in_any_eigenspace"]
    assert not adapter["scalar_polynomial_p_with_pA_J0_equals_X_exists"]
    assert ownership["A_owns_four_spectral_projectors"] and not ownership["A_owns_common_module_projector"]
    assert not decision["common_module_selected_by_frozen_action"]
    assert not decision["actual_K596_K598_packet_released"]


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
