#!/usr/bin/env sage-python
"""K615 zero-form stationarity obstruction in the frozen corrected model."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from sage.all import block_matrix, identity_matrix, zero_matrix

from k435_k77_full_h640_observed_map import PRIMES
from k438_k77_constraint_compressed_boundary_symbol import build_compressed_packet
from k439_k77_compatible_corrected_boundary_split import build_split_packet


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k615-k77-zero-form-stationarity-obstruction.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


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
    action = compressed["compressed"]
    euler = action * zero_seed
    ranks = {
        "zero_form_injection": int(zero_seed.rank()),
        "action_euler_image": int(euler.rank()),
        "outgoing_zero_form": int((split["outgoing"] * zero_seed).rank()),
        "incoming_zero_form": int((split["incoming"] * zero_seed).rank()),
        "outgoing_euler": int((split["outgoing"] * euler).rank()),
        "incoming_euler": int((split["incoming"] * euler).rank()),
        "fast_euler": int((compressed["fast"] * euler).rank()),
        "slow_euler": int((compressed["slow"] * euler).rank()),
    }
    checks = {
        "zero_form_restriction_has_zero_kernel": ranks["action_euler_image"] == 128,
        "both_zero_form_halves_are_injective": ranks["outgoing_zero_form"] == ranks["incoming_zero_form"] == 128,
        "both_euler_halves_are_injective": ranks["outgoing_euler"] == ranks["incoming_euler"] == 128,
        "fast_and_slow_euler_images_are_injective": ranks["fast_euler"] == ranks["slow_euler"] == 128,
    }
    if not all(checks.values()):
        raise AssertionError({"prime": prime, "ranks": ranks, "checks": checks})
    return {"prime": prime, "ranks": ranks, "checks": checks}


def build() -> dict:
    k614 = strict("lab/process/k614-k77-zero-form-corrected-carrier-injection.json")
    k438 = strict("lab/process/k438-k77-constraint-compressed-boundary-symbol.json")
    k440 = strict("lab/process/k440-k77-corrected-boundary-green-domain.json")
    zero_action = strict("lab/process/selected-k77-zero-fermion-coupled-hessian-current-order.json")
    packets = [build_prime_packet(prime) for prime in PRIMES]
    assert packets[0]["ranks"] == packets[1]["ranks"]
    ranks = packets[0]["ranks"]
    assert k438["decision"]["zero_characteristic_root_present"] is False
    assert k440["functional_result"]["kernel_dimension"] == 0
    assert k440["functional_result"]["cokernel_dimension"] == 0
    assert k614["injection_theorem"]["canonical_zero_form_inclusion_rank"] == 128
    assert zero_action["exact_result"]["zero_fermion_current_rank"] == 0

    return {
        "schema_version": "1.0",
        "result_id": "K615-K77-ZERO-FORM-STATIONARITY-OBSTRUCTION",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The K614 source-owned Omega0(S) injection evaluated against K438's frozen corrected action symbol and K440's corrected half-line Green domain, including the direct sum of the source's four independent barred/unbarred fermion slots.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "carrier": "K438 corrected real rank-512 carrier E inside the conditional H640 carrier",
            "source_field": "K614 canonical zero-form inclusion J0: Omega0(S)_128 -> E",
            "operator": "K438 compressed frozen normal action symbol A and K440 D_A=d/dr+A",
            "domain": "K440 H1(R_+,E) domain with Pi_c,out u(0)=0",
            "pairing": "K441 transported positive corrected-carrier pairing used only to represent the Euler covector",
            "result": "frozen zero-form stationarity obstruction MAP-TYPE=restricted-kernel theorem",
            "target": "a nonzero stationary Omega0 background for K596/K598",
        },
        "cross_characteristic_packets": packets,
        "rank_fingerprint": ranks,
        "fibrewise_stationarity_theorem": {
            "equation": "A J0 v = 0",
            "rank_AJ0": 128,
            "kernel_dimension": 0,
            "only_solution": "v=0",
            "nonzero_zero_form_value_has_nonzero_euler_covector": True,
            "nonzero_zero_form_value_is_stationary": False,
        },
        "closed_domain_stationarity_theorem": {
            "equation": "D_A u=0 with Pi_c,out u(0)=0 and u in H1(R_+,E)",
            "K440_kernel_dimension": 0,
            "K440_cokernel_dimension": 0,
            "only_corrected_domain_solution": "u=0",
            "four_source_fermion_slots_direct_sum_kernel_dimension": 0,
            "moving_lower_order_or_nonlinear_operator_covered": False,
            "source_selected_physical_boundary_covered": False,
        },
        "stationarity_riesz_dichotomy": {
            "nonzero_v": "the positive-pairing representative of the frozen Euler covector is nonzero because rank(AJ0)=128, but v is off shell",
            "stationary_v": "the only stationary value is v=0, whose Euler covector and Riesz representative are zero",
            "nonzero_stationary_K441_Riesz_packet_released": False,
        },
        "decision": {
            "K614_field_injection_retracted": False,
            "K440_green_domain_retracted": False,
            "nonzero_stationary_zero_form_in_K440_model_exists": False,
            "four_field_frozen_stationary_background_nonzero": False,
            "moving_nonlinear_nonzero_background_excluded": False,
            "selected_source_action_rejected": False,
            "K596_K598_released_by_stationarity": False,
            "next_exact_input": "Test the natural unsplit off-shell rank-one packet built from J0 v and its A J0 v Euler/Riesz image against K596/K598. Any surviving on-shell route requires a different moving nonlinear operator/domain or a genuinely different odd action datum.",
        },
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "Use K438's no-zero-root symbol and K440's already proved zero kernel before searching for a nonlinear background.",
            "retrieval_collision_result": "K614 proves injection but does not compose it with K440 stationarity; K440 proves zero kernel on all E but does not state the zero-form or four-field consequence.",
            "strongest_alternative": "A moving nonlinear fermion operator could have nonzero stationary solutions, but its lower-order coefficients and common domain are not constructed.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Promoting a frozen corrected-domain zero-kernel theorem into a rejection of every GU fermion background or physical boundary.",
            "strongest_contrary_construction": "Changing the lower-order/nonlinear operator or its boundary domain can create kernel; those data are outside K438/K440 and remain open.",
            "weakest_reproducibility_seam": "The rank-128 restricted-kernel statement is certified at two good characteristics, while the H1 zero-kernel step reuses K440's exact four-block Green theorem.",
        },
        "claim_ceiling": "Exact obstruction for the frozen K438/K440 corrected normal model: A restricted to K614's zero-form image is injective at both good characteristics, and D_A on the corrected H1 trace domain has zero kernel and cokernel. Hence neither one zero-form slot nor the direct sum of the source's four independent fermion slots has a nonzero stationary background in this model. A nonzero chosen value has a nonzero Euler/Riesz representative but is off shell; the only stationary value has zero representative. This does not exclude a moving nonlinear operator/domain, reject the source action, or move source, ledger, canon, paper, public, novelty, prediction, confirmation, or physical conclusions.",
    }


def validate(payload: dict) -> None:
    ranks = payload["rank_fingerprint"]
    fibre = payload["fibrewise_stationarity_theorem"]
    domain = payload["closed_domain_stationarity_theorem"]
    dichotomy = payload["stationarity_riesz_dichotomy"]
    decision = payload["decision"]
    assert ranks["action_euler_image"] == 128
    assert ranks["outgoing_zero_form"] == ranks["incoming_zero_form"] == 128
    assert ranks["outgoing_euler"] == ranks["incoming_euler"] == 128
    assert ranks["fast_euler"] == ranks["slow_euler"] == 128
    assert fibre["kernel_dimension"] == 0 and fibre["nonzero_zero_form_value_has_nonzero_euler_covector"]
    assert not fibre["nonzero_zero_form_value_is_stationary"]
    assert domain["K440_kernel_dimension"] == domain["K440_cokernel_dimension"] == 0
    assert domain["four_source_fermion_slots_direct_sum_kernel_dimension"] == 0
    assert not domain["moving_lower_order_or_nonlinear_operator_covered"]
    assert not dichotomy["nonzero_stationary_K441_Riesz_packet_released"]
    assert not decision["nonzero_stationary_zero_form_in_K440_model_exists"]
    assert not decision["selected_source_action_rejected"]


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
