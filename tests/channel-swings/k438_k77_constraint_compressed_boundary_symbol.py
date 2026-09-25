#!/usr/bin/env sage-python
"""K438 constraint-compressed K77 boundary symbol on the actual carrier."""

from __future__ import annotations

import argparse
import json

from sage.all import block_diagonal_matrix, block_matrix, identity_matrix, zero_matrix

from k435_k77_full_h640_observed_map import PRIMES, canonical_digest
from k436_k77_full_action_boundary_projector import build_boundary_packet
from k437_k77_clifford_boundary_compatibility import image_basis


OBSERVED_ONE_FORM_INDICES = (0, 7, 8, 9)


def build_compressed_packet(prime: int, keep_matrices: bool = False) -> dict:
    boundary = build_boundary_packet(prime, keep_core=True)
    core = boundary["core"]
    field = core["field"]
    gammas = core["gammas"]
    eta = core["eta"]
    i128 = identity_matrix(field, 128, sparse=True)
    i512 = identity_matrix(field, 512, sparse=True)
    i640 = identity_matrix(field, 640, sparse=True)
    z128 = zero_matrix(field, 128, 128, sparse=True)

    gamma_trace = block_matrix(
        field, 1, 4,
        [[field(eta[index]) * gammas[index] for index in OBSERVED_ONE_FORM_INDICES]],
        sparse=True,
    )
    trace_lift = block_matrix(
        field, 4, 1,
        [[gammas[index] / field(4)] for index in OBSERVED_ONE_FORM_INDICES],
        sparse=True,
    )
    corrected = block_diagonal_matrix([i512 - trace_lift * gamma_trace, i128], sparse=True)
    gamma_full = block_matrix(field, 1, 2, [[gamma_trace, z128]], sparse=True)
    reduced = boundary["observed_reduced"]
    compressed = corrected * reduced * corrected
    compressed2 = compressed * compressed
    slow = field(576) / field(575) * (corrected - compressed2)
    fast = (field(576) * compressed2 - corrected) / field(575)
    corrected_basis = image_basis(corrected)
    restricted = corrected_basis.solve_right(compressed * corrected_basis)

    polynomial_residual = (
        field(576) * compressed2 * compressed2
        - field(577) * compressed2
        + corrected
    )
    checks = {
        "corrected_projector_idempotent": corrected * corrected == corrected,
        "corrected_rank_512": corrected.rank() == 512,
        "gamma_annihilates_corrected_range": gamma_full * corrected == zero_matrix(field, 128, 640, sparse=True),
        "compressed_is_constraint_endomorphism": corrected * compressed == compressed and compressed * corrected == compressed,
        "compressed_rank_512": compressed.rank() == 512,
        "quartic_identity": polynomial_residual.is_zero(),
        "restricted_characteristic_factorization": restricted.charpoly() == (restricted.base_ring()["x"].gen()**2 - 1)**192 * (restricted.base_ring()["x"].gen()**2 - field(1) / field(576))**64,
        "restricted_minimal_polynomial": restricted.minpoly() == (restricted.base_ring()["x"].gen()**2 - 1) * (restricted.base_ring()["x"].gen()**2 - field(1) / field(576)),
        "fast_slow_complementary": fast + slow == corrected,
        "fast_slow_disjoint": fast * slow == zero_matrix(field, 640, 640, sparse=True),
        "fast_projector_rank_384": fast * fast == fast and fast.rank() == 384,
        "slow_projector_rank_128": slow * slow == slow and slow.rank() == 128,
        "uncompressed_involution_defect_rank_128": (compressed2 - corrected).rank() == 128,
        "original_symbol_constraint_leak_rank_128": ((i640 - corrected) * reduced * corrected).rank() == 128,
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    row = {
        "prime": prime,
        "ranks": {
            "observed_carrier": 640,
            "corrected_carrier": 512,
            "compressed_symbol": int(compressed.rank()),
            "fast_abs_one_block": int(fast.rank()),
            "slow_abs_one_over_24_block": int(slow.rank()),
            "uncompressed_involution_defect": int((compressed2 - corrected).rank()),
            "original_constraint_leak": int(((i640 - corrected) * reduced * corrected).rank()),
        },
        "digests": {
            "corrected_projector": canonical_digest(corrected),
            "compressed_symbol": canonical_digest(compressed),
            "fast_projector": canonical_digest(fast),
            "slow_projector": canonical_digest(slow),
        },
        "checks": checks,
    }
    if keep_matrices:
        row.update({
            "field": field,
            "corrected": corrected,
            "gamma_full": gamma_full,
            "reduced": reduced,
            "compressed": compressed,
            "fast": fast,
            "slow": slow,
            "old_incoming": boundary["observed_incoming"],
        })
    return row


def public_packet(row: dict) -> dict:
    hidden = {"field", "corrected", "gamma_full", "reduced", "compressed", "fast", "slow", "old_incoming"}
    return {key: value for key, value in row.items() if key not in hidden}


def demo() -> dict:
    packets = [public_packet(build_compressed_packet(prime)) for prime in PRIMES]
    fingerprints = [row["ranks"] for row in packets]
    assert fingerprints[0] == fingerprints[1]
    return {
        "schema_version": "1.0",
        "result_id": "K438-K77-CONSTRAINT-COMPRESSED-BOUNDARY-SYMBOL",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "construction": {
            "carrier": "actual rank-640 observed H640 carrier with corrected Clifford projector P of rank 512",
            "input_symbol": "K436 transported reduced normal symbol S_7",
            "compressed_symbol": "A=P S_7 P on im(P)",
            "exact_identity": "576 A^4 - 577 A^2 + P = 0",
            "spectral_blocks": "A has characteristic factors (x^2-1)^192 and (x^2-1/576)^64 on im(P)",
            "ownership": "A is determined by the already fixed action symbol, oriented conormal and corrected Clifford constraint; no fitted complement is introduced",
        },
        "cross_characteristic_packets": packets,
        "cross_characteristic_rank_fingerprint": fingerprints[0],
        "decision": {
            "constraint_compressed_symbol_constructed": True,
            "zero_characteristic_root_present": False,
            "compressed_symbol_is_involution": False,
            "slow_characteristic_block_rank": 128,
            "action_and_constraint_determine_spectral_blocks": True,
            "physical_boundary_selected": False,
            "nonlinear_bv_kt_compatibility_proved": False,
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
