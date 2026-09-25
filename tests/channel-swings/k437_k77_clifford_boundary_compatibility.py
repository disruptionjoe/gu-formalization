#!/usr/bin/env sage-python
"""K437 corrected-Clifford versus full K77 boundary compatibility test."""

from __future__ import annotations

import argparse
import json

from sage.all import block_diagonal_matrix, block_matrix, identity_matrix, zero_matrix

from k435_k77_full_h640_observed_map import OBSERVED_SLOTS, PRIMES, canonical_digest
from k436_k77_full_action_boundary_projector import build_boundary_packet


OBSERVED_ONE_FORM_INDICES = OBSERVED_SLOTS[:4]


def image_basis(projector):
    return projector.matrix_from_columns(list(projector.pivots()))


def intersection_dimension(left, right) -> int:
    left_basis = image_basis(left)
    right_basis = image_basis(right)
    joined = block_matrix(left.base_ring(), 1, 2, [[left_basis, right_basis]], sparse=True)
    return int(left_basis.ncols() + right_basis.ncols() - joined.rank())


def build_compatibility_packet(prime: int) -> dict:
    boundary = build_boundary_packet(prime, keep_core=True)
    core = boundary["core"]
    field = core["field"]
    gammas = core["gammas"]
    eta = core["eta"]
    i128 = identity_matrix(field, 128, sparse=True)
    z128 = zero_matrix(field, 128, 128, sparse=True)
    i512 = identity_matrix(field, 512, sparse=True)
    i640 = identity_matrix(field, 640, sparse=True)

    gamma_trace = block_matrix(
        field,
        1,
        4,
        [[field(eta[index]) * gammas[index] for index in OBSERVED_ONE_FORM_INDICES]],
        sparse=True,
    )
    trace_lift = block_matrix(
        field,
        4,
        1,
        [[gammas[index] / field(4)] for index in OBSERVED_ONE_FORM_INDICES],
        sparse=True,
    )
    corrected_one_form = i512 - trace_lift * gamma_trace
    corrected_full = block_diagonal_matrix([corrected_one_form, i128], sparse=True)
    gamma_full = block_matrix(
        field,
        1,
        2,
        [[gamma_trace, z128]],
        sparse=True,
    )
    trace_lift_full = block_matrix(
        field,
        2,
        1,
        [[trace_lift], [z128]],
        sparse=True,
    )

    incoming = boundary["observed_incoming"]
    commutator = corrected_full * incoming - incoming * corrected_full
    boundary_leaves_corrected = (i640 - corrected_full) * incoming * corrected_full
    corrected_leaves_boundary = (i640 - incoming) * corrected_full * incoming
    product = corrected_full * incoming
    common_dim = intersection_dimension(corrected_full, incoming)
    trace_dim = intersection_dimension(trace_lift_full * gamma_full, incoming)

    checks = {
        "clifford_right_inverse": gamma_trace * trace_lift == i128,
        "corrected_projector_idempotent": corrected_full * corrected_full == corrected_full,
        "corrected_projector_rank_512": corrected_full.rank() == 512,
        "corrected_projector_lands_in_gamma_kernel": gamma_full * corrected_full == zero_matrix(field, 128, 640, sparse=True),
        "trace_lift_is_corrected_kernel": corrected_full * trace_lift_full == zero_matrix(field, 640, 128, sparse=True),
        "boundary_projector_rank_320": incoming.rank() == 320,
        "projectors_do_not_commute": not commutator.is_zero(),
        "boundary_does_not_preserve_corrected_range": not boundary_leaves_corrected.is_zero(),
        "corrected_split_does_not_preserve_boundary_range": not corrected_leaves_boundary.is_zero(),
        "ordered_product_not_idempotent": product * product != product,
        "common_intersection_nonempty": common_dim > 0,
        "incoming_trace_lift_intersection_is_trivial": trace_dim == 0,
    }
    if not all(checks.values()):
        raise AssertionError({"checks": checks, "common_dim": common_dim, "trace_dim": trace_dim})

    return {
        "prime": prime,
        "ranks": {
            "observed_carrier": 640,
            "corrected_clifford_range": int(corrected_full.rank()),
            "corrected_trace_lift": int(trace_lift.rank()),
            "incoming_boundary_range": int(incoming.rank()),
            "common_intersection": common_dim,
            "incoming_trace_lift_intersection": trace_dim,
            "commutator": int(commutator.rank()),
            "boundary_preservation_defect": int(boundary_leaves_corrected.rank()),
            "corrected_preservation_defect": int(corrected_leaves_boundary.rank()),
            "ordered_product": int(product.rank()),
            "ordered_product_idempotence_defect": int((product * product - product).rank()),
            "gamma_on_incoming": int((gamma_full * incoming).rank()),
        },
        "digests": {
            "corrected_full_projector": canonical_digest(corrected_full),
            "incoming_boundary_projector": canonical_digest(incoming),
            "projector_commutator": canonical_digest(commutator),
            "boundary_preservation_defect": canonical_digest(boundary_leaves_corrected),
            "corrected_preservation_defect": canonical_digest(corrected_leaves_boundary),
        },
        "checks": checks,
    }


def demo() -> dict:
    packets = [build_compatibility_packet(prime) for prime in PRIMES]
    rank_fingerprints = [row["ranks"] for row in packets]
    assert rank_fingerprints[0] == rank_fingerprints[1]
    return {
        "schema_version": "1.0",
        "result_id": "K437-K77-CLIFFORD-BOUNDARY-COMPATIBILITY",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "typed_composition": {
            "observed_carrier": "O=(T*X_observed tensor S_128) plus Omega0(S_128), rank 512+128=640",
            "corrected_clifford_projector": "diag(I_512-j_B Gamma_B, I_128), with Gamma_B j_B=I_128",
            "boundary_projector": "K436 transported rank-320 incoming projector for outward conormal +dx7",
            "compatibility_law": "a simple common projected Green domain requires mutual range preservation; commuting projectors would provide the canonical intersection projector",
        },
        "cross_characteristic_packets": packets,
        "cross_characteristic_rank_fingerprint": rank_fingerprints[0],
        "decision": {
            "corrected_clifford_projector_constructed_on_actual_observed_carrier": True,
            "boundary_and_corrected_projectors_commute": False,
            "boundary_preserves_corrected_range": False,
            "corrected_split_preserves_incoming_boundary_range": False,
            "canonical_product_intersection_projector_constructed": False,
            "nontrivial_set_theoretic_linear_intersection_exists": True,
            "common_green_domain_derived": False,
            "repair_selected": False,
            "next_exact_input": "derive an action-owned modified split or boundary law whose projectors mutually preserve their ranges, then prove the resulting intersection is closed, Green-compatible, constraint-invariant and compatible with the nonlinear BV/Koszul-Tate differential",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if not args.demo:
        parser.error("use --demo")
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
