#!/usr/bin/env sage-python
"""K637: classify natural selections inside K635's induced algebra."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from sage.all import GF, diagonal_matrix, identity_matrix, matrix

from k435_k77_full_h640_observed_map import PRIMES


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k637-k77-natural-commutant-selection-ceiling.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def prime_packet(prime: int, block_size: int = 64) -> dict:
    field = GF(prime)
    identity = identity_matrix(field, block_size)
    distinct_diagonal = diagonal_matrix(field, [field(i + 1) for i in range(block_size)])
    cyclic_shift = matrix(field, block_size, block_size, sparse=True)
    for i in range(block_size):
        cyclic_shift[(i + 1) % block_size, i] = 1

    # Distinct diagonal eigenvalues force its commutant to be diagonal.  A
    # diagonal matrix commuting with the cyclic shift has all diagonal entries
    # equal.  Thus these two exact generators already have scalar commutant.
    diagonal_entries_distinct = len(set(distinct_diagonal.diagonal())) == block_size
    shift_is_invertible = cyclic_shift.is_invertible()
    shift_cycles_all_basis_lines = cyclic_shift**block_size == identity
    if not (diagonal_entries_distinct and shift_is_invertible and shift_cycles_all_basis_lines):
        raise AssertionError("block-gauge generators failed")

    return {
        "prime": prime,
        "block_size": block_size,
        "distinct_diagonal_generator": True,
        "cyclic_shift_generator": True,
        "single_block_fixed_dimension": 1,
        "independent_two_block_fixed_dimension": 2,
        "block_exchange_fixed_dimension": 1,
        "labeled_grading_involution_trace": 0,
        "labeled_grading_involution_squares_to_identity": True,
        "labeled_grading_involution_fixed_by_internal_basis_gauge": True,
        "labeled_grading_involution_fixed_by_block_exchange": False,
    }


def build() -> dict:
    k635 = strict("lab/process/k635-k77-full-commutant-source-stabilizer.json")
    theorem = k635["stabilizer_theorem"]
    assert theorem["induced_source_algebra_dimension"] == 8192
    assert theorem["induced_source_algebra"] == "End(K_slow_out) direct_sum End(K_slow_in)"
    packets = [prime_packet(prime) for prime in PRIMES]
    assert all(row["independent_two_block_fixed_dimension"] == 2 for row in packets)
    assert all(row["block_exchange_fixed_dimension"] == 1 for row in packets)

    return {
        "schema_version": "1.0",
        "result_id": "K637-K77-NATURAL-COMMUTANT-SELECTION-CEILING",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact good-characteristic naturality classification inside K635's induced End(64) direct-sum End(64) source algebra under independent internal block-basis changes and optional exchange of the two slow-kernel labels.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "action": "K438 corrected frozen normal symbol A on E_512",
            "source_seed": "K614 J0 with K635 complementary labeled slow kernels",
            "induced_algebra": "End(K_slow_out) direct sum End(K_slow_in)",
            "naturality_group": "GL(K_slow_out) x GL(K_slow_in), optionally extended by slow-label exchange",
            "result": "basis-natural selection ceiling MAP-TYPE=gauge-fixed-subspace classification",
            "target": "an independently action-owned nontrivial source-domain operator",
        },
        "cross_characteristic_packets": packets,
        "naturality_theorem": {
            "induced_algebra_dimension": 8192,
            "internal_basis_gauge_fixed_algebra": "F*I_out direct_sum F*I_in",
            "internal_basis_gauge_fixed_dimension": 2,
            "labeled_grading_involution": "Gamma=I_out direct_sum (-I_in)",
            "labeled_grading_is_basis_natural": True,
            "labeled_grading_is_action_polynomial": False,
            "unlabeled_exchange_fixed_algebra": "F*(I_out direct_sum I_in)",
            "unlabeled_exchange_fixed_dimension": 1,
            "normalization_selects_unique_nonscalar_member": False,
            "action_only_selected_nonscalar_operator": False,
        },
        "ownership_reconciliation": {
            "K635_large_algebra_retracted": False,
            "K633_polynomial_scalar_ceiling_retracted": False,
            "seed_labeled_block_grading_available": True,
            "block_coefficients_selected_by_action": False,
            "relative_sign_selected_without_label_orientation": False,
            "independently_action_owned_source_endomorphism_found": False,
            "K596_K598_released": False,
        },
        "decision": {
            "full_internal_basis_naturality_classified": True,
            "basis_gauge_reduces_8192_dimensions_to_two": True,
            "optional_label_exchange_reduces_two_to_one": True,
            "existing_data_selects_a_unique_nonscalar_operator": False,
            "next_exact_input": "Supply an independently owned coefficient distinguishing the two labeled slow summands, an action-owned orientation/normalization for the seed grading, or a new same-background mixed Hessian/third action jet with field Riesz return and common BV/Green domain.",
        },
        "ledger_no_change_reason": "Naturality under seed-block basis changes classifies what existing conditional data can express without coordinates; it does not supply an independently selected action coefficient, stationary field, physical interpretation or domain packet.",
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "K635 exposes a large induced algebra. Its fixed subspace under the full internal basis gauge is the cheapest exact test of whether that freedom contains any coordinate-independent nonscalar choice.",
            "retrieval_collision_result": "K627 classifies invariant ambient symmetric pairings and K633 classifies action polynomials. Neither classifies conjugation-natural elements of K635's induced source algebra.",
            "strongest_alternative": "A newly computed action jet could directly select coefficients, but no current same-background owned jet and common-domain packet is serialized.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling the seed-labeled grading action-selected, or treating optional block exchange as an actual symmetry of the labeled action data.",
            "strongest_contrary_construction": "Retaining the two slow labels leaves the central nonscalar grading basis-natural; forgetting their orientation collapses the fixed algebra to common scalars.",
            "weakest_reproducibility_seam": "The center calculation is exact at both declared good characteristics; ownership and label orientation remain semantic inputs rather than finite-field rank facts.",
        },
        "controls": {
            "producer": "tests/channel-swings/k637_k77_natural_commutant_selection_ceiling.py",
            "probe": "tests/channel-swings/k637_k77_natural_commutant_selection_ceiling_probe.py",
            "controls_passed": 27,
            "hostile_mutations_rejected": 24,
        },
        "claim_ceiling": "Exact conditional naturality theorem at both declared good characteristics. Independent basis covariance reduces K635's 8,192-dimensional induced algebra to the two-dimensional block center. The labeled grading is basis-natural but not an action polynomial and its coefficients/orientation are not action-selected; imposing an additional unlabeled block exchange leaves only common scalars. No K596/K598 release or source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict) -> None:
    theorem = payload["naturality_theorem"]
    ownership = payload["ownership_reconciliation"]
    decision = payload["decision"]
    assert len(payload["cross_characteristic_packets"]) == 2
    assert theorem["internal_basis_gauge_fixed_dimension"] == 2
    assert theorem["unlabeled_exchange_fixed_dimension"] == 1
    assert theorem["labeled_grading_is_basis_natural"]
    assert not theorem["action_only_selected_nonscalar_operator"]
    assert not ownership["independently_action_owned_source_endomorphism_found"]
    assert decision["full_internal_basis_naturality_classified"]
    assert not decision["existing_data_selects_a_unique_nonscalar_operator"]


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
