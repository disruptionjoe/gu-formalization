#!/usr/bin/env sage-python
"""K614 source-owned zero-form injection into the corrected K77 carrier."""

from __future__ import annotations

import argparse
import json

from sage.all import block_matrix, identity_matrix, zero_matrix

from k435_k77_full_h640_observed_map import PRIMES
from k438_k77_constraint_compressed_boundary_symbol import build_compressed_packet
from k439_k77_compatible_corrected_boundary_split import build_split_packet


def strict(relative: str) -> dict:
    from pathlib import Path

    root = Path(__file__).resolve().parents[2]
    return json.loads((root / relative).read_text(encoding="utf-8"))


def build_prime_packet(prime: int) -> dict:
    compressed = build_compressed_packet(prime, keep_matrices=True)
    split = build_split_packet(prime, keep_matrices=True)
    field = compressed["field"]
    zero_seed = block_matrix(
        field,
        2,
        1,
        [[zero_matrix(field, 512, 128, sparse=True)],
         [identity_matrix(field, 128, sparse=True)]],
        sparse=True,
    )

    corrected_image = compressed["corrected"] * zero_seed
    fast_image = compressed["fast"] * zero_seed
    slow_image = compressed["slow"] * zero_seed
    incoming_image = split["incoming"] * zero_seed
    outgoing_image = split["outgoing"] * zero_seed
    fast_incoming = compressed["fast"] * split["incoming"] * zero_seed
    fast_outgoing = compressed["fast"] * split["outgoing"] * zero_seed
    slow_incoming = compressed["slow"] * split["incoming"] * zero_seed
    slow_outgoing = compressed["slow"] * split["outgoing"] * zero_seed

    ranks = {
        "source_zero_form": int(zero_seed.rank()),
        "corrected_image": int(corrected_image.rank()),
        "fast_projection": int(fast_image.rank()),
        "slow_projection": int(slow_image.rank()),
        "incoming_projection": int(incoming_image.rank()),
        "outgoing_projection": int(outgoing_image.rank()),
        "fast_incoming_projection": int(fast_incoming.rank()),
        "fast_outgoing_projection": int(fast_outgoing.rank()),
        "slow_incoming_projection": int(slow_incoming.rank()),
        "slow_outgoing_projection": int(slow_outgoing.rank()),
        "action_symbol_image": int((compressed["compressed"] * zero_seed).rank()),
        "sign_image": int((split["sign"] * zero_seed).rank()),
    }
    checks = {
        "zero_form_lies_in_corrected_carrier": corrected_image == zero_seed,
        "zero_form_inclusion_is_injective": ranks["corrected_image"] == 128,
        "fast_projection_is_injective": ranks["fast_projection"] == 128,
        "slow_projection_is_injective": ranks["slow_projection"] == 128,
        "incoming_projection_is_injective": ranks["incoming_projection"] == 128,
        "outgoing_projection_is_injective": ranks["outgoing_projection"] == 128,
        "all_four_spectral_sign_blocks_are_met": all(
            ranks[name] > 0
            for name in (
                "fast_incoming_projection",
                "fast_outgoing_projection",
                "slow_incoming_projection",
                "slow_outgoing_projection",
            )
        ),
        "action_symbol_nonzero_on_zero_form": ranks["action_symbol_image"] == 128,
        "sign_nonzero_on_zero_form": ranks["sign_image"] == 128,
    }
    if not all(checks.values()):
        raise AssertionError({"prime": prime, "checks": checks, "ranks": ranks})
    return {"prime": prime, "ranks": ranks, "checks": checks}


def build() -> dict:
    seed = strict("lab/process/selected-k77-zero-seed-h640-action-closure-controls.json")
    zero_background = strict("lab/process/selected-k77-zero-fermion-coupled-hessian-current-order.json")
    k613 = strict("lab/process/k613-k77-central-parity-tensor-network-obstruction.json")
    packets = [build_prime_packet(prime) for prime in PRIMES]
    assert packets[0]["ranks"] == packets[1]["ranks"]
    ranks = packets[0]["ranks"]
    assert seed["zero_form_seed"]["source_owned"] is True
    assert seed["zero_form_seed"]["seed_rank"] == 128
    assert zero_background["exact_result"]["zero_fermion_current_rank"] == 0
    assert zero_background["exact_result"]["zero_fermion_mixed_hessian_rank"] == 0
    assert k613["reopener"]["minimal_injection_datum"].startswith("an action-owned injection")

    return {
        "schema_version": "1.0",
        "result_id": "K614-K77-ZERO-FORM-CORRECTED-CARRIER-INJECTION",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Composition of the source-owned Omega0(S) field inclusion with K438's corrected H640 carrier and K439's exact spectral/sign split, followed by reconciliation with the active zero-fermion background and K596/K598 ownership requirements.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "carrier": "K438 corrected rank-512 carrier E inside the conditional observed H640=Omega1(S)_512 plus Omega0(S)_128 carrier",
            "source_field": "source-owned independent fermion field nu in Omega0(Y,S), represented fibrewise by the canonical rank-128 zero-form inclusion J0",
            "projectors": "K438 fast/slow projectors and K439 incoming/outgoing projectors on E",
            "background": "the active action branch is zero fermion; a nonzero stationary Omega0 field value is not source- or action-owned",
            "result": "zero-form corrected-carrier injection MAP-TYPE=field-to-carrier inclusion",
            "target": "K596/K598 initial corrected-carrier vector/covector and Riesz packet",
        },
        "cross_characteristic_packets": packets,
        "cross_characteristic_rank_fingerprint": ranks,
        "injection_theorem": {
            "source_owned_zero_form_field": True,
            "canonical_zero_form_inclusion_rank": 128,
            "image_lies_in_corrected_carrier": True,
            "incoming_projection_is_injective": True,
            "outgoing_projection_is_injective": True,
            "fast_projection_is_injective": True,
            "slow_projection_is_injective": True,
            "all_four_action_spectral_sign_blocks_met": True,
            "every_nonzero_zero_form_value_has_nonzero_incoming_and_outgoing_components": True,
            "field_space_is_not_a_selected_field_value": True,
        },
        "background_and_riesz_reconciliation": {
            "active_background": "zero fermion",
            "zero_form_background_value": "0",
            "injection_evaluated_on_active_background_is_zero": True,
            "zero_fermion_current_rank": 0,
            "zero_fermion_mixed_hessian_rank": 0,
            "nonzero_fermion_stationary_solution_owned": False,
            "K441_action_Riesz_return_for_zero_form_background_owned": False,
            "K596_actual_rank_one_packet_released": False,
            "K598_actual_covariant_packet_released": False,
        },
        "decision": {
            "K613_hypothetical_field_to_carrier_map_narrowed": True,
            "source_owned_zero_form_injection_constructed": True,
            "action_owned_nonzero_background_constructed": False,
            "actual_action_owned_soldering_constructed": False,
            "K590_factorized_completion_retracted": False,
            "K613_central_parity_obstruction_retracted": False,
            "selected_source_action_rejected": False,
            "next_exact_input": "Construct and source/action-own one nonzero stationary Omega0 fermion background together with its K441-compatible Riesz return, or supply a different genuinely odd action datum. Then project it through the now-exact J0 packet and apply K596/K598; the active zero-fermion branch evaluates J0 at zero.",
        },
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "Compose the already source-owned Omega0 field inclusion with the exact K438/K439 carrier before searching arbitrary rank-512 maps.",
            "retrieval_collision_result": "The zero-seed result owns Omega0 and K438/K439 own the corrected split, but no predecessor composes them or separates injection ownership from nonzero-background ownership.",
            "strongest_alternative": "A direct nonzero-fermion stationary construction would release a vector only if its source/action coefficients, reality and domain close; current evidence does not own that solution.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating the rank-128 source field or its injective carrier map as a selected nonzero fermion background or an actual K596 rank-one coupling.",
            "strongest_contrary_construction": "On the active zero-fermion branch J0 is evaluated at zero, and the current action has zero fermion current and mixed Hessian there.",
            "weakest_reproducibility_seam": "The 640-dimensional carrier ranks are proved by exact good-characteristic reductions; the action-compatible Riesz return and a nonzero stationary field value remain absent.",
        },
        "claim_ceiling": "Exact cross-characteristic composition of the source-owned Omega0(S) field inclusion with K438/K439: its rank-128 image lies in the corrected carrier, and its fast, slow, incoming and outgoing projections are all injective, meeting all four action spectral/sign blocks. This constructs a field-to-carrier injection but not a selected field value. The active zero-fermion background evaluates the injection at zero and supplies neither a nonzero K441 Riesz return nor an actual K596/K598 packet. No source action is rejected and no nonlinear properness, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion moves.",
    }


def validate(payload: dict) -> None:
    ranks = payload["cross_characteristic_rank_fingerprint"]
    theorem = payload["injection_theorem"]
    background = payload["background_and_riesz_reconciliation"]
    decision = payload["decision"]
    assert ranks["source_zero_form"] == ranks["corrected_image"] == 128
    assert ranks["fast_projection"] == ranks["slow_projection"] == 128
    assert ranks["incoming_projection"] == ranks["outgoing_projection"] == 128
    assert [ranks[key] for key in ("fast_incoming_projection", "fast_outgoing_projection", "slow_incoming_projection", "slow_outgoing_projection")] == [128, 128, 64, 64]
    assert all(theorem[key] for key in ("source_owned_zero_form_field", "image_lies_in_corrected_carrier", "incoming_projection_is_injective", "outgoing_projection_is_injective", "fast_projection_is_injective", "slow_projection_is_injective", "all_four_action_spectral_sign_blocks_met", "every_nonzero_zero_form_value_has_nonzero_incoming_and_outgoing_components", "field_space_is_not_a_selected_field_value"))
    assert background["injection_evaluated_on_active_background_is_zero"]
    assert background["zero_fermion_current_rank"] == background["zero_fermion_mixed_hessian_rank"] == 0
    assert not any(background[key] for key in ("nonzero_fermion_stationary_solution_owned", "K441_action_Riesz_return_for_zero_form_background_owned", "K596_actual_rank_one_packet_released", "K598_actual_covariant_packet_released"))
    assert decision["source_owned_zero_form_injection_constructed"] and not any(decision[key] for key in ("action_owned_nonzero_background_constructed", "actual_action_owned_soldering_constructed", "K590_factorized_completion_retracted", "K613_central_parity_obstruction_retracted", "selected_source_action_rejected"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if not args.demo:
        parser.error("use --demo")
    payload = build()
    validate(payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
