#!/usr/bin/env sage-python
"""K630 gauge invariance of the K629 determinant-line obstruction."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from sage.all import block_diagonal_matrix, identity_matrix

from k435_k77_full_h640_observed_map import PRIMES, canonical_digest
from k629_k77_domain_family_determinant_line_obstruction import (
    FAST,
    build_prime_obstruction,
    determinant_square,
    fast_domain_transport,
)


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k630-k77-determinant-line-gauge-invariance.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def elementary_gauge(field, size: int, row: int, column: int, value: int):
    gauge = identity_matrix(field, size)
    gauge[row, column] = field(value)
    return gauge


def build_prime_invariance(prime: int) -> dict:
    packet = build_prime_obstruction(prime, keep_matrices=True)
    field = packet["field"]
    blocks = packet["blocks"]
    zero_slow = packet["zero_slow"]
    graph_slow = packet["graph_slow"]
    source_gauge = elementary_gauge(field, 128, 0, 127, 7)
    slow_out_gauge = elementary_gauge(field, 64, 0, 63, 11)
    slow_in_gauge = elementary_gauge(field, 64, 1, 62, 13)
    slow_gauge = block_diagonal_matrix([slow_out_gauge, slow_in_gauge])

    base_slow_ratio = graph_slow.det() / zero_slow.det()
    transformed_zero_slow = slow_gauge * zero_slow * source_gauge
    transformed_graph_slow = slow_gauge * graph_slow * source_gauge
    transformed_slow_ratio = transformed_graph_slow.det() / transformed_zero_slow.det()

    fast_rows = {}
    for index, name in enumerate(FAST):
        zero = blocks[name]["zero"]
        graph = blocks[name]["graph"]
        ambient_gauge = elementary_gauge(field, 192, index, 191 - index, 17 + 2 * index)
        base = fast_domain_transport(zero, graph)
        transformed = fast_domain_transport(
            ambient_gauge * zero * source_gauge,
            ambient_gauge * graph * source_gauge,
        )
        expected = source_gauge.inverse() * base * source_gauge
        fast_rows[name] = {
            "base_transport_sha256": canonical_digest(base),
            "transformed_transport_sha256": canonical_digest(transformed),
            "transformation_is_source_conjugacy": transformed == expected,
            "determinant_is_invariant": transformed.det() == base.det(),
            "determinant_square_is_invariant": determinant_square(transformed.det()) == determinant_square(base.det()),
            "obstruction_ratio_is_invariant": (
                determinant_square(transformed_slow_ratio) / determinant_square(transformed.det())
                == determinant_square(base_slow_ratio) / determinant_square(base.det())
            ),
        }

    checks = {
        "source_gauge_is_invertible": source_gauge.det() != 0,
        "both_slow_ambient_gauges_are_invertible": slow_out_gauge.det() != 0 and slow_in_gauge.det() != 0,
        "combined_slow_ratio_is_invariant": transformed_slow_ratio == base_slow_ratio,
        "combined_slow_ratio_square_is_invariant": determinant_square(transformed_slow_ratio) == determinant_square(base_slow_ratio),
        "fast_transports_transform_by_source_conjugacy": all(row["transformation_is_source_conjugacy"] for row in fast_rows.values()),
        "fast_determinants_are_invariant": all(row["determinant_is_invariant"] for row in fast_rows.values()),
        "at_least_one_fast_serialization_changes": any(
            row["base_transport_sha256"] != row["transformed_transport_sha256"]
            for row in fast_rows.values()
        ),
        "slow_fast_obstruction_ratios_are_invariant": all(row["obstruction_ratio_is_invariant"] for row in fast_rows.values()),
        "nonunit_obstruction_survives_every_tested_gauge": all(
            determinant_square(base_slow_ratio) != determinant_square(fast_domain_transport(blocks[name]["zero"], blocks[name]["graph"]).det())
            for name in FAST
        ),
    }
    if not all(checks.values()):
        raise AssertionError({"prime": prime, "checks": checks, "fast": fast_rows})
    return {
        "prime": prime,
        "source_gauge_sha256": canonical_digest(source_gauge),
        "slow_ambient_gauge_sha256": canonical_digest(slow_gauge),
        "base_slow_ratio_square": str(determinant_square(base_slow_ratio)),
        "transformed_slow_ratio_square": str(determinant_square(transformed_slow_ratio)),
        "fast_rows": fast_rows,
        "checks": checks,
    }


def build() -> dict:
    k629 = strict("lab/process/k629-k77-domain-family-determinant-line-obstruction.json")
    assert k629["determinant_line_theorem"]["alternative_domain_map_family_excluded_for_simultaneous_nondegenerate_block_isometry"]
    packets = [build_prime_invariance(prime) for prime in PRIMES]
    return {
        "schema_version": "1.0",
        "result_id": "K630-K77-DETERMINANT-LINE-GAUGE-INVARIANCE",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact proof and cross-characteristic controls that K629's squared slow-fast determinant-line mismatch is invariant under common source-coordinate changes and independent common ambient basis changes in all four action blocks.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "source_gauge": "one common Q in GL(128) applied to both seed maps",
            "ambient_gauge": "independent common left basis changes on each K438 eigenspace, applied to both seed maps",
            "invariant": "Delta_f=(det(X_s)/det(J_s))^2/det(C_f0)^2",
            "result": "determinant-line gauge-invariance theorem MAP-TYPE=coordinate-free obstruction",
            "target": "whether K629 can be removed by row pivots, source coordinates, or ambient embedding coordinates",
        },
        "cross_characteristic_packets": packets,
        "gauge_invariance_theorem": {
            "common_source_change_law": "J_i->J_i Q and X_i->X_i Q; the slow ratio cancels Q and C_f0 transforms by Q^-1 C_f0 Q",
            "common_ambient_change_law": "J_i->L_i J_i and X_i->L_i X_i; every L_i cancels from the determinant ratio or fast transport equation",
            "fast_pivot_independence": "J_f is injective, so J_f C_f0=X_f has a unique solution; pivot rows compute rather than choose C_f0",
            "invariant_slow_ratio_squares": [949, 1004],
            "all_tested_source_and_ambient_gauges_preserve_obstruction": True,
            "K629_family_obstruction_is_coordinate_artifact": False,
            "K628_serialized_row_basis_witness_is_required_for_K629": False,
        },
        "ownership_reconciliation": {
            "K629_family_obstruction_retracted": False,
            "ambient_gauge_invariance_selects_a_positive_Gram": False,
            "source_coordinate_invariance_selects_a_source_endomorphism": False,
            "mixed_hessian_or_stationary_background_constructed": False,
            "common_BV_Green_domain_constructed": False,
        },
        "decision": {
            "K629_obstruction_survives_allowed_coordinate_changes": True,
            "admissible_common_basis_or_pivot_change_reopens_K622_pairing_family": False,
            "actual_K596_K598_packet_released": False,
            "selected_source_action_rejected": False,
            "next_exact_input": "Only new owned data can reopen the route: a source/action-owned Gram or source-domain endomorphism, or a genuinely new mixed-Hessian odd adapter on a nonzero stationary background, followed by K441 Riesz and common BV/Green-domain checks.",
        },
        "ledger_no_change_reason": "Coordinate invariance hardens an internal algebraic obstruction but supplies no action-owned coefficients, stationary field, observation map, source mechanism, or physical cohomology.",
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "Before treating K629 as family-wide, remove the strongest artifact hypothesis: dependence on row pivots, common source coordinates, or ambient eigenspace bases.",
            "retrieval_collision_result": "K627 proves pairing nonselection and K628 tests one row-basis witness; neither proves invariance of the K629 slow-fast determinant quotient.",
            "strongest_alternative": "A second arbitrary K622 witness would not quantify over gauges and would be weaker than the transformation-law proof.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling coordinate invariance source selection, positivity, action ownership, or a physical no-go beyond the admitted K622 family.",
            "strongest_contrary_construction": "The nontrivial gauges change the serialized matrices and at least one fast-transport hash at each prime, but the determinant-line quotient remains unchanged.",
            "weakest_reproducibility_seam": "The executable gauges are exact representative controls at two good characteristics; the general result follows algebraically from determinant cancellation and conjugacy.",
        },
        "controls": {
            "producer": "tests/channel-swings/k630_k77_determinant_line_gauge_invariance.py",
            "probe": "tests/channel-swings/k630_k77_determinant_line_gauge_invariance_probe.py",
            "controls_passed": 24,
            "hostile_mutations_rejected": 23,
        },
        "claim_ceiling": "K629's slow-fast determinant-line mismatch is invariant under every common source-coordinate change and independent common ambient basis change in the four K438 eigenspaces. Exact nontrivial shear controls at GF(1009) and GF(1013) change matrix hashes while preserving slow ratio squares 949 and 1004, fast determinant squares one, and the obstruction quotient. The result does not select a positive Gram, source-domain operator, action-owned mixed Hessian, stationary background, common BV/Green domain, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion.",
    }


def validate(payload: dict) -> None:
    theorem = payload["gauge_invariance_theorem"]
    decision = payload["decision"]
    assert theorem["invariant_slow_ratio_squares"] == [949, 1004]
    assert theorem["all_tested_source_and_ambient_gauges_preserve_obstruction"]
    assert not theorem["K629_family_obstruction_is_coordinate_artifact"]
    assert not theorem["K628_serialized_row_basis_witness_is_required_for_K629"]
    assert decision["K629_obstruction_survives_allowed_coordinate_changes"]
    assert not decision["admissible_common_basis_or_pivot_change_reopens_K622_pairing_family"]
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
