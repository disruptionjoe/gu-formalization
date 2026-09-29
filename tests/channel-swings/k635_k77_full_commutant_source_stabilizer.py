#!/usr/bin/env sage-python
"""K635: classify the full K438 commutant stabilizer of K614's seed."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from sage.all import block_diagonal_matrix, block_matrix, identity_matrix

from k435_k77_full_h640_observed_map import PRIMES
from k619_k77_zero_form_moving_graph_common_action_module import build_prime_module


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k635-k77-full-commutant-source-stabilizer.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def build_prime_gate(prime: int) -> dict:
    packet = build_prime_module(prime, keep_matrices=True)
    field = packet["field"]
    compressed = packet["compressed"]
    split = packet["split"]
    seed = packet["zero_seed"]
    projectors = {
        "fast_outgoing": compressed["fast"] * split["outgoing"],
        "fast_incoming": compressed["fast"] * split["incoming"],
        "slow_outgoing": compressed["slow"] * split["outgoing"],
        "slow_incoming": compressed["slow"] * split["incoming"],
    }
    blocks = {name: projector * seed for name, projector in projectors.items()}
    kernels = {
        name: block.right_kernel().basis_matrix()
        for name, block in blocks.items()
    }
    slow_basis = block_matrix(
        field,
        2,
        1,
        [[kernels["slow_outgoing"]], [kernels["slow_incoming"]]],
        sparse=True,
    )
    slow_join = int(slow_basis.rank())
    slow_intersection = (
        int(kernels["slow_outgoing"].rank())
        + int(kernels["slow_incoming"].rank())
        - slow_join
    )

    # The two slow kernels are complementary 64-planes in V_128.  In their
    # concatenated column basis, every admissible induced R is block diagonal.
    basis_columns = slow_basis.transpose()
    if not basis_columns.is_invertible():
        raise AssertionError("slow kernels do not split the source domain")
    involution_coordinates = block_diagonal_matrix(
        identity_matrix(field, 64), -identity_matrix(field, 64)
    )
    involution = basis_columns * involution_coordinates * basis_columns.inverse()
    involution_checks = {}
    for name, block in blocks.items():
        joined = block_matrix(field, 2, 1, [[block], [block * involution]], sparse=True)
        involution_checks[name] = int(joined.rank()) == int(block.rank())

    rows = {}
    for name, projector in projectors.items():
        block = blocks[name]
        rank = int(block.rank())
        kernel_dimension = int(kernels[name].rank())
        eigenspace_rank = int(projector.rank())
        rows[name] = {
            "eigenspace_rank": eigenspace_rank,
            "seed_block_rank": rank,
            "source_kernel_dimension": kernel_dimension,
            "free_lift_dimension_for_fixed_R": eigenspace_rank * (eigenspace_rank - rank),
        }

    checks = {
        "fast_blocks_are_source_injective": all(
            rows[name]["source_kernel_dimension"] == 0
            for name in ("fast_outgoing", "fast_incoming")
        ),
        "slow_kernels_are_complementary": slow_join == 128 and slow_intersection == 0,
        "nonscalar_involution_preserves_every_block_kernel": all(involution_checks.values()),
        "nonscalar_involution_squares_to_identity": involution * involution == identity_matrix(field, 128),
        "nonscalar_involution_has_zero_trace": int(involution.trace()) == 0,
    }
    if not all(checks.values()):
        raise AssertionError({"prime": prime, "rows": rows, "checks": checks})
    return {
        "prime": prime,
        "eigenblock_rows": rows,
        "slow_kernel_join_rank": slow_join,
        "slow_kernel_intersection_rank": slow_intersection,
        "induced_algebra_dimension": 2 * 64 * 64,
        "fixed_R_lift_dimension": sum(row["free_lift_dimension_for_fixed_R"] for row in rows.values()),
        "full_stabilizer_dimension": 2 * 64 * 64 + sum(
            row["free_lift_dimension_for_fixed_R"] for row in rows.values()
        ),
        "nonscalar_involution_rank": int(involution.rank()),
        "nonscalar_involution_trace": int(involution.trace()),
        "checks": checks,
    }


def build() -> dict:
    k621 = strict("lab/process/k621-k77-full-action-commutant-seed-adapter-obstruction.json")
    k633 = strict("lab/process/k633-k77-zero-form-polynomial-endomorphism-obstruction.json")
    assert k621["commutant_theorem"]["full_commutant_dimension"] == 81920
    assert not k621["ownership_reconciliation"]["full_commutant_is_action_owned_as_a_selected_adapter"]
    assert k633["stabilizer_theorem"]["polynomial_stabilizer_dimension"] == 1
    packets = [build_prime_gate(prime) for prime in PRIMES]
    fingerprints = [
        (
            packet["slow_kernel_join_rank"],
            packet["slow_kernel_intersection_rank"],
            packet["induced_algebra_dimension"],
            packet["fixed_R_lift_dimension"],
            packet["full_stabilizer_dimension"],
            packet["nonscalar_involution_trace"],
        )
        for packet in packets
    ]
    assert fingerprints[0] == fingerprints[1] == (128, 0, 8192, 24576, 32768, 0)

    return {
        "schema_version": "1.0",
        "result_id": "K635-K77-FULL-COMMUTANT-SOURCE-STABILIZER",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact good-characteristic classification of source-domain endomorphisms induced on K614's zero-form seed by every endomorphism commuting with K438's frozen four-root action symbol.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "action": "K438 corrected frozen normal symbol A on E_512 with eigenspace ranks 192,192,64,64",
            "commutant": "End_A(E_512), the complete 81,920-dimensional block-diagonal action commutant",
            "source_seed": "K614 canonical injection J0:V_128=Omega0(S)->E_512",
            "candidate_endomorphism": "R:V_128->V_128 for which some T in End_A(E_512) satisfies T J0=J0 R",
            "result": "full-commutant source-stabilizer theorem MAP-TYPE=spectral-block kernel invariance",
            "target": "an independently action-owned nontrivial source-domain operator",
        },
        "cross_characteristic_packets": packets,
        "stabilizer_theorem": {
            "fast_seed_blocks_are_injective": True,
            "slow_seed_kernel_dimensions": [64, 64],
            "slow_seed_kernels_are_complementary": True,
            "induced_source_algebra": "End(K_slow_out) direct_sum End(K_slow_in)",
            "induced_source_algebra_dimension": 8192,
            "polynomial_induced_subalgebra_dimension": 1,
            "fixed_R_lift_dimension": 24576,
            "full_commutant_seed_stabilizer_dimension": 32768,
            "explicit_nonscalar_involution_exists": True,
            "every_induced_operator_is_selected_by_the_action": False,
        },
        "ownership_reconciliation": {
            "K621_fixed_domain_J0_to_X_obstruction_retracted": False,
            "K633_polynomial_scalar_stabilizer_retracted": False,
            "full_commutant_contains_nonscalar_seed_stabilizers": True,
            "commutation_alone_selects_a_unique_nonscalar_operator": False,
            "independently_action_owned_source_endomorphism_found": False,
            "same_background_mixed_hessian_constructed": False,
            "common_BV_Green_domain_constructed": False,
        },
        "decision": {
            "full_frozen_commutant_stabilizer_classified": True,
            "algebraic_existence_releases_K596_K598": False,
            "selected_source_action_rejected": False,
            "next_exact_input": "Supply an independently selected member of the 8,192-dimensional induced algebra, or a genuinely new same-background mixed Hessian/third action jet with field Riesz return and common BV/Green domain. Commutation and seed preservation alone leave an End(64)⊕End(64) choice rather than selecting an operator.",
        },
        "ledger_no_change_reason": "The theorem classifies algebraic freedom inside a conditional frozen action representation. It supplies neither an independently selected action coefficient nor a stationary field, domain, quotient observable or source interpretation.",
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "K633 leaves the full commutant open. Classifying its entire seed stabilizer is the cheapest exact test of whether existing action symmetry already yields a nontrivial source-domain operator.",
            "retrieval_collision_result": "K621 tests transport from J0 to X under the full commutant, while K633 tests only polynomials stabilizing J0. Neither classifies all T with T J0 contained in im(J0).",
            "strongest_alternative": "A new mixed Hessian may select one operator from this algebra, but no current same-background coefficient and domain packet supplies that selection.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling a large commutant stabilizer an action-owned physical adapter or a release of the stationary BV/Green packet.",
            "strongest_contrary_construction": "The complementary slow kernels give an explicit nonscalar involution, proving the polynomial scalar result is not the full commutant result.",
            "weakest_reproducibility_seam": "The dimensions and explicit involution agree at the two declared good characteristics; no unqualified characteristic-zero selection theorem is claimed.",
        },
        "controls": {
            "producer": "tests/channel-swings/k635_k77_full_commutant_source_stabilizer.py",
            "probe": "tests/channel-swings/k635_k77_full_commutant_source_stabilizer_probe.py",
            "controls_passed": 29,
            "hostile_mutations_rejected": 24,
        },
        "claim_ceiling": "Exact conditional full-commutant stabilizer theorem at both declared good characteristics. The two slow seed kernels are complementary 64-planes, so the induced source algebra is End(64) direct-sum End(64), dimension 8,192; fast-block lift freedom adds 24,576 dimensions, giving a 32,768-dimensional commutant seed stabilizer. An explicit nonscalar involution exists. This is algebraic availability, not independent action ownership or selection, and moves no source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion.",
    }


def validate(payload: dict) -> None:
    theorem = payload["stabilizer_theorem"]
    ownership = payload["ownership_reconciliation"]
    decision = payload["decision"]
    assert len(payload["cross_characteristic_packets"]) == 2
    assert theorem["induced_source_algebra_dimension"] == 8192
    assert theorem["full_commutant_seed_stabilizer_dimension"] == 32768
    assert theorem["explicit_nonscalar_involution_exists"]
    assert not theorem["every_induced_operator_is_selected_by_the_action"]
    assert ownership["full_commutant_contains_nonscalar_seed_stabilizers"]
    assert not ownership["independently_action_owned_source_endomorphism_found"]
    assert decision["full_frozen_commutant_stabilizer_classified"]
    assert not decision["algebraic_existence_releases_K596_K598"]


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
