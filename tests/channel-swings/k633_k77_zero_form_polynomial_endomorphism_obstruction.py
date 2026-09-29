#!/usr/bin/env sage-python
"""K633: classify K438 polynomials preserving K614's zero-form seed."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from sage.all import matrix

from k435_k77_full_h640_observed_map import PRIMES
from k619_k77_zero_form_moving_graph_common_action_module import build_prime_module


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k633-k77-zero-form-polynomial-endomorphism-obstruction.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def build_prime_gate(prime: int) -> dict:
    packet = build_prime_module(prime, keep_matrices=True)
    field = packet["field"]
    action = packet["action"]
    zero_seed = packet["zero_seed"]

    # Rows of quotient_map annihilate im(J0), so quotient_map * B is the
    # class of a 512x128 matrix B modulo maps landing in im(J0).
    seed_rows = zero_seed.column_space().basis_matrix()
    quotient_map = seed_rows.right_kernel().basis_matrix()
    powers = []
    current = action * zero_seed
    for _degree in range(1, 4):
        powers.append(current)
        current = action * current
    quotient_columns = [list((quotient_map * power).list()) for power in powers]
    coefficient_matrix = matrix(
        field,
        len(quotient_columns[0]),
        3,
        lambda row, column: quotient_columns[column][row],
    )

    seed_rank = int(zero_seed.rank())
    action_seed_rank = int((action * zero_seed).rank())
    joined_rank = int(zero_seed.augment(action * zero_seed).rank())
    quotient_rank = int(coefficient_matrix.rank())
    nonconstant_nullity = int(coefficient_matrix.right_kernel().dimension())
    checks = {
        "seed_is_injective": seed_rank == 128,
        "first_action_image_has_full_seed_rank": action_seed_rank == 128,
        "first_action_image_is_transverse_to_seed": joined_rank == 256,
        "three_nonconstant_quotient_classes_are_independent": quotient_rank == 3,
        "nonconstant_polynomial_stabilizer_is_zero": nonconstant_nullity == 0,
    }
    if not all(checks.values()):
        raise AssertionError({"prime": prime, "checks": checks})
    return {
        "prime": prime,
        "seed_rank": seed_rank,
        "action_seed_rank": action_seed_rank,
        "seed_action_seed_join_rank": joined_rank,
        "seed_action_seed_intersection_rank": seed_rank + action_seed_rank - joined_rank,
        "nonconstant_quotient_coefficient_rank": quotient_rank,
        "nonconstant_stabilizer_nullity": nonconstant_nullity,
        "checks": checks,
    }


def build() -> dict:
    k438 = strict("lab/process/k438-k77-constraint-compressed-boundary-symbol.json")
    k614 = strict("lab/process/k614-k77-zero-form-corrected-carrier-injection.json")
    k619 = strict("lab/process/k619-k77-zero-form-moving-graph-common-action-module.json")
    k620 = strict("lab/process/k620-k77-action-functional-calculus-selection-obstruction.json")
    k631 = strict("lab/process/k631-k77-owned-input-type-census.json")
    k632 = strict("lab/process/k632-k77-owned-input-composition-closure.json")
    assert k438["cross_characteristic_result"]["minimal_polynomial_on_im_P"] == "(x^2-1)(x^2-1/576)"
    assert k614["injection_theorem"]["canonical_zero_form_inclusion_rank"] == 128
    assert k619["common_module_theorem"]["depth_2_hull_ranks"]["zero_form"] == 256
    assert not k620["seed_adapter_theorem"]["scalar_polynomial_p_with_pA_J0_equals_X_exists"]
    assert k631["census_theorem"]["single_candidate_matching_source_domain_endomorphism"] is False
    assert k632["reachable_signature_counts"]["owned_V_128_to_V_128_endomorphisms"] == 0

    packets = [build_prime_gate(prime) for prime in PRIMES]
    fingerprints = [
        (
            packet["seed_rank"],
            packet["action_seed_rank"],
            packet["seed_action_seed_join_rank"],
            packet["nonconstant_quotient_coefficient_rank"],
            packet["nonconstant_stabilizer_nullity"],
        )
        for packet in packets
    ]
    assert fingerprints[0] == fingerprints[1] == (128, 128, 256, 3, 0)

    return {
        "schema_version": "1.0",
        "result_id": "K633-K77-ZERO-FORM-POLYNOMIAL-ENDOMORPHISM-OBSTRUCTION",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact good-characteristic classification of polynomials in K438's four-root corrected action symbol whose restriction along K614's canonical zero-form injection lands back in that same source-owned seed image.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "action": "K438 corrected frozen normal symbol A on E_512 with minimal polynomial (x^2-1)(x^2-1/576)",
            "source_seed": "K614 canonical injection J0: V_128=Omega0(S) -> E_512",
            "candidate_endomorphism": "R:V_128->V_128 satisfying p(A)J0=J0R for p of degree below four",
            "quotient_test": "classes of AJ0, A^2J0 and A^3J0 in Hom(V_128,E_512/im(J0))",
            "result": "source-seed polynomial-stabilizer theorem MAP-TYPE=quotient linear system",
            "target": "independently action-owned nontrivial V_128 endomorphism",
        },
        "cross_characteristic_packets": packets,
        "stabilizer_theorem": {
            "functional_calculus_dimension": 4,
            "representative_degree_bound": 3,
            "first_action_seed_intersection_rank": 0,
            "nonconstant_quotient_classes_tested": ["AJ0", "A^2J0", "A^3J0"],
            "nonconstant_quotient_classes_independent": True,
            "polynomial_stabilizer_dimension": 1,
            "polynomial_stabilizer_basis": ["identity"],
            "every_polynomial_preserving_seed_image_is_constant_modulo_minimal_polynomial": True,
            "every_induced_source_endomorphism_is_scalar": True,
            "nontrivial_owned_source_endomorphism_obtained": False,
        },
        "ownership_reconciliation": {
            "K614_source_owned_injection_retracted": False,
            "K619_common_action_module_retracted": False,
            "K620_seed_adapter_obstruction_retracted": False,
            "K632_current_composition_closure_sharpened": True,
            "scalar_identity_counts_as_new_action_coefficient": False,
            "arbitrary_commutant_or_mixed_hessian_excluded": False,
            "nonzero_stationary_background_constructed": False,
            "common_BV_Green_domain_constructed": False,
        },
        "decision": {
            "frozen_action_polynomial_route_to_new_V128_endomorphism_closed": True,
            "independently_owned_V128_endomorphism_found": False,
            "actual_K596_K598_packet_released": False,
            "selected_source_action_rejected": False,
            "next_exact_input": "Supply an independently action-owned operator outside R[A]—for example a nonpolynomial commutant or same-background mixed Hessian—with its source-domain return and common BV/Green domain; the frozen four-root polynomial calculus induces only scalar identities on J0(V_128).",
        },
        "ledger_no_change_reason": "The theorem classifies one conditional frozen action algebra relative to an existing source-owned injection. It adds no selected nonzero field value, mixed action coefficient, stationary solution, quotient observable or source interpretation.",
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "K632 leaves an owned V_128 endomorphism as an exact reopener. Before demanding a new action jet, test whether the already-owned four-root action algebra restricts through J0.",
            "retrieval_collision_result": "K619 proves the J0 Krylov hull reaches rank 384 and K620 excludes a polynomial J0-to-X adapter, but neither classifies the self-stabilizer of im(J0).",
            "strongest_alternative": "An operator in the larger commutant or a moving mixed Hessian could preserve J0(V_128) nontrivially; those classes are explicitly outside this polynomial test.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling the scalar polynomial stabilizer a no-go for the full commutant, nonlinear action jets or a future source-owned domain operator.",
            "strongest_contrary_construction": "The identity polynomial always induces the scalar identity on V_128, so the stabilizer is one-dimensional rather than empty.",
            "weakest_reproducibility_seam": "The coefficient system is certified at the two declared good characteristics; no unqualified characteristic-zero physical selection theorem is claimed.",
        },
        "controls": {
            "producer": "tests/channel-swings/k633_k77_zero_form_polynomial_endomorphism_obstruction.py",
            "probe": "tests/channel-swings/k633_k77_zero_form_polynomial_endomorphism_obstruction_probe.py",
            "controls_passed": 28,
            "hostile_mutations_rejected": 24,
        },
        "claim_ceiling": "Exact conditional stabilizer theorem at both declared good characteristics: AJ0 is transverse to J0, the quotient classes of AJ0, A^2J0 and A^3J0 are independent, and the degree-below-four polynomial stabilizer of im(J0) is therefore exactly the constants. K438's frozen polynomial action calculus induces only scalar identities on V_128 and supplies no new owned source-domain endomorphism. This does not test the full commutant, a nonlinear mixed Hessian or future action data, and moves no source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion.",
    }


def validate(payload: dict) -> None:
    theorem = payload["stabilizer_theorem"]
    ownership = payload["ownership_reconciliation"]
    decision = payload["decision"]
    assert len(payload["cross_characteristic_packets"]) == 2
    assert all(packet["nonconstant_quotient_coefficient_rank"] == 3 for packet in payload["cross_characteristic_packets"])
    assert all(packet["nonconstant_stabilizer_nullity"] == 0 for packet in payload["cross_characteristic_packets"])
    assert theorem["polynomial_stabilizer_dimension"] == 1
    assert theorem["polynomial_stabilizer_basis"] == ["identity"]
    assert theorem["every_induced_source_endomorphism_is_scalar"]
    assert not theorem["nontrivial_owned_source_endomorphism_obtained"]
    assert ownership["K632_current_composition_closure_sharpened"]
    assert not ownership["arbitrary_commutant_or_mixed_hessian_excluded"]
    assert decision["frozen_action_polynomial_route_to_new_V128_endomorphism_closed"]
    assert not decision["independently_owned_V128_endomorphism_found"]


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
