#!/usr/bin/env sage-python
"""K439 canonical compatible split from the K438 compressed symbol."""

from __future__ import annotations

import argparse
import json

from sage.all import identity_matrix, zero_matrix

from k435_k77_full_h640_observed_map import PRIMES, canonical_digest
from k437_k77_clifford_boundary_compatibility import intersection_dimension
from k438_k77_constraint_compressed_boundary_symbol import build_compressed_packet


def build_split_packet(prime: int, keep_matrices: bool = False) -> dict:
    compressed_row = build_compressed_packet(prime, keep_matrices=True)
    field = compressed_row["field"]
    corrected = compressed_row["corrected"]
    gamma_full = compressed_row["gamma_full"]
    compressed = compressed_row["compressed"]
    old_incoming = compressed_row["old_incoming"]
    i640 = identity_matrix(field, 640, sparse=True)

    sign = (field(13823) * compressed - field(13248) * compressed**3) / field(575)
    incoming = (corrected - sign) / field(2)
    outgoing = (corrected + sign) / field(2)

    checks = {
        "sign_supported_on_corrected_carrier": corrected * sign == sign and sign * corrected == sign,
        "sign_involution_on_corrected_carrier": sign * sign == corrected,
        "incoming_idempotent": incoming * incoming == incoming,
        "outgoing_idempotent": outgoing * outgoing == outgoing,
        "incoming_outgoing_complementary_on_corrected": incoming + outgoing == corrected,
        "incoming_outgoing_disjoint": incoming * outgoing == zero_matrix(field, 640, 640, sparse=True),
        "incoming_rank_256": incoming.rank() == 256,
        "outgoing_rank_256": outgoing.rank() == 256,
        "constraint_annihilates_both": gamma_full * incoming == zero_matrix(field, 128, 640, sparse=True) and gamma_full * outgoing == zero_matrix(field, 128, 640, sparse=True),
        "compressed_symbol_preserves_both": (i640 - incoming) * compressed * incoming == zero_matrix(field, 640, 640, sparse=True) and (i640 - outgoing) * compressed * outgoing == zero_matrix(field, 640, 640, sparse=True),
        "orientation_reversal_swaps_halves": (-field(13823) * compressed + field(13248) * compressed**3) / field(575) == -sign,
        "old_and_new_incoming_intersection_rank_192": intersection_dimension(old_incoming, incoming) == 192,
        "new_incoming_adds_rank_64_outside_old": ((i640 - old_incoming) * incoming).rank() == 64,
        "old_incoming_constraint_leak_rank_128": (gamma_full * old_incoming).rank() == 128,
        "new_incoming_constraint_leak_zero": (gamma_full * incoming).rank() == 0,
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    row = {
        "prime": prime,
        "ranks": {
            "corrected_carrier": int(corrected.rank()),
            "canonical_incoming": int(incoming.rank()),
            "canonical_outgoing": int(outgoing.rank()),
            "old_new_incoming_intersection": intersection_dimension(old_incoming, incoming),
            "new_incoming_outside_old": int(((i640 - old_incoming) * incoming).rank()),
            "old_incoming_constraint_leak": int((gamma_full * old_incoming).rank()),
            "new_incoming_constraint_leak": int((gamma_full * incoming).rank()),
        },
        "digests": {
            "sign_involution": canonical_digest(sign),
            "canonical_incoming": canonical_digest(incoming),
            "canonical_outgoing": canonical_digest(outgoing),
        },
        "checks": checks,
    }
    if keep_matrices:
        row.update({
            "field": field,
            "corrected": corrected,
            "compressed": compressed,
            "sign": sign,
            "incoming": incoming,
            "outgoing": outgoing,
        })
    return row


def public_packet(row: dict) -> dict:
    hidden = {"field", "corrected", "compressed", "sign", "incoming", "outgoing"}
    return {key: value for key, value in row.items() if key not in hidden}


def demo() -> dict:
    packets = [public_packet(build_split_packet(prime)) for prime in PRIMES]
    fingerprints = [row["ranks"] for row in packets]
    assert fingerprints[0] == fingerprints[1]
    return {
        "schema_version": "1.0",
        "result_id": "K439-K77-COMPATIBLE-CORRECTED-BOUNDARY-SPLIT",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "native_to_observed",
        "canonical_functional_calculus": {
            "sign_polynomial": "J=(13823 A-13248 A^3)/575",
            "interpolation": "J maps eigenvalues +1,+1/24 to +1 and -1,-1/24 to -1",
            "incoming": "Pi_c,in=(P-J)/2",
            "outgoing": "Pi_c,out=(P+J)/2",
            "no_fit": "all coefficients are fixed uniquely by odd cubic interpolation on the four K438 characteristic roots",
            "orientation": "A -> -A implies J -> -J and exchanges Pi_c,in with Pi_c,out",
        },
        "cross_characteristic_packets": packets,
        "cross_characteristic_rank_fingerprint": fingerprints[0],
        "decision": {
            "canonical_constraint_compatible_split_constructed": True,
            "modified_split_uses_fitted_parameter": False,
            "mutual_constraint_preservation": True,
            "orientation_reversal_complementarity": True,
            "physical_boundary_selected": False,
            "global_calderon_projector_constructed": False,
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
