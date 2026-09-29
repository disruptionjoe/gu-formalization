#!/usr/bin/env sage-python
"""K621 fixed-domain seed transport under the full K438 action commutant."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from sage.all import block_matrix

from k435_k77_full_h640_observed_map import PRIMES
from k619_k77_zero_form_moving_graph_common_action_module import build_prime_module


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k621-k77-full-action-commutant-seed-adapter-obstruction.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def build_prime_gate(prime: int, keep_matrices: bool = False) -> dict:
    packet = build_prime_module(prime, keep_matrices=True)
    field = packet["field"]
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
    rows = {}
    for name, projector in projectors.items():
        zero_block = projector * zero_seed
        graph_block = projector * graph
        zero_rank = int(zero_block.rank())
        graph_rank = int(graph_block.rank())
        stacked = block_matrix(field, 2, 1, [[zero_block], [graph_block]], sparse=True)
        stacked_rank = int(stacked.rank())
        block_dimension = int(projector.rank())
        transport_exists = stacked_rank == zero_rank
        rows[name] = {
            "eigenspace_rank": block_dimension,
            "zero_seed_block_rank": zero_rank,
            "graph_seed_block_rank": graph_rank,
            "row_space_join_rank": stacked_rank,
            "row_space_intersection_rank": zero_rank + graph_rank - stacked_rank,
            "fixed_domain_commutant_transport_exists": transport_exists,
            "solution_affine_dimension_if_nonempty": (
                block_dimension * (block_dimension - zero_rank)
                if transport_exists
                else None
            ),
        }

    checks = {
        "fast_blocks_admit_fixed_domain_transport": all(
            rows[name]["fixed_domain_commutant_transport_exists"]
            and rows[name]["row_space_join_rank"] == 128
            and rows[name]["row_space_intersection_rank"] == 128
            for name in ("fast_outgoing", "fast_incoming")
        ),
        "slow_row_spaces_are_disjoint": all(
            rows[name]["row_space_join_rank"] == 128
            and rows[name]["row_space_intersection_rank"] == 0
            for name in ("slow_outgoing", "slow_incoming")
        ),
        "slow_blocks_obstruct_fixed_domain_transport": all(
            not rows[name]["fixed_domain_commutant_transport_exists"]
            for name in ("slow_outgoing", "slow_incoming")
        ),
        "full_fixed_domain_transport_is_obstructed": not all(
            row["fixed_domain_commutant_transport_exists"] for row in rows.values()
        ),
    }
    if not all(checks.values()):
        raise AssertionError({"prime": prime, "rows": rows, "checks": checks})
    public = {"prime": prime, "eigenblock_rows": rows, "checks": checks}
    if keep_matrices:
        public.update(packet)
        public["projectors"] = projectors
    return public


def build() -> dict:
    k619 = strict("lab/process/k619-k77-zero-form-moving-graph-common-action-module.json")
    k620 = strict("lab/process/k620-k77-action-functional-calculus-selection-obstruction.json")
    assert k619["common_module_theorem"]["filtrations_equal_from_depth_3"]
    assert not k620["seed_adapter_theorem"]["arbitrary_commutant_or_domain_endomorphism_tested"]
    packets = [build_prime_gate(prime) for prime in PRIMES]
    assert packets[0]["eigenblock_rows"] == packets[1]["eigenblock_rows"]
    rows = packets[0]["eigenblock_rows"]
    return {
        "schema_version": "1.0",
        "result_id": "K621-K77-FULL-ACTION-COMMUTANT-SEED-ADAPTER-OBSTRUCTION",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact test of whether any endomorphism commuting with K438's four-root action sends K614's fixed-parameter zero-form seed map to K617's moving-graph seed map.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "action": "K438 corrected frozen normal symbol A with eigenspace ranks 192,192,64,64",
            "commutant": "End_A(E), the complete block-diagonal endomorphism algebra on the four distinct A eigenspaces",
            "seed_maps": "K614 J0 and K617 X as maps from the same fixed Omega0(S)_128 coordinate domain into E",
            "result": "fixed-domain full-commutant obstruction MAP-TYPE=eigenblock row-space criterion",
            "target": "an A-commuting corrected-carrier endomorphism T satisfying T J0 = X",
        },
        "cross_characteristic_packets": packets,
        "eigenblock_fingerprint": rows,
        "commutant_theorem": {
            "full_commutant_dimension": 81920,
            "polynomial_functional_calculus_dimension": 4,
            "distinct_roots_force_block_diagonal_commutant": True,
            "block_equation_criterion": "T_i J_i = X_i is solvable iff row(X_i) is contained in row(J_i)",
            "fast_block_solution_affine_dimensions": [12288, 12288],
            "slow_block_row_space_intersections": [0, 0],
            "slow_block_row_space_joins": [128, 128],
            "fixed_domain_commuting_adapter_exists": False,
            "obstruction_location": "both rank-64 slow eigenspaces",
        },
        "ownership_reconciliation": {
            "K620_polynomial_obstruction_retracted": False,
            "full_commutant_is_action_owned_as_a_selected_adapter": False,
            "fixed_domain_nonpolynomial_commutant_adapter_excluded": True,
            "source_domain_reparameterization_tested": False,
            "mixed_hessian_or_domain_adapter_excluded": False,
            "nonzero_stationary_background_constructed": False,
        },
        "decision": {
            "K619_common_module_retracted": False,
            "K620_functional_calculus_obstruction_strengthened": True,
            "actual_K596_K598_packet_released": False,
            "selected_source_action_rejected": False,
            "next_exact_input": "Test the strongest same-data repair: allow one invertible endomorphism of the Omega0(S)_128 source domain and ask whether the two seeds then lie in the same End_A(E) orbit. Even a positive orbit result remains noncanonical and does not supply action ownership, a stationary background, or a common BV/Green domain.",
        },
        "ledger_no_change_reason": "The obstruction is internal to the conditional frozen corrected-carrier model and tests no stationary solution, mixed Hessian, gauge-reduced class, observation map, or physical cohomology. SC-ACT-01/02 and SC-CHI-01/51 and every v0.263 ledger row remain unchanged.",
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "K620 leaves arbitrary commutants open; the exact row-space criterion tests the complete commutant without fitting or serializing an arbitrary 512-by-512 operator.",
            "retrieval_collision_result": "K607/K610/K613 classify natural homogeneous action data and K620 classifies R[A], but no predecessor tests End_A(E) against the particular K614/K617 seed maps.",
            "strongest_alternative": "A source-domain reparameterization or moving mixed Hessian may avoid the fixed-coordinate equation and is tested or retained separately.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling failure of T J0=X for a fixed source parameterization failure of every block-commutant orbit equivalence or field-dependent adapter.",
            "strongest_contrary_construction": "Both fast blocks admit large affine families of fixed-domain solutions; the obstruction comes only from the two disjoint slow-domain row spaces.",
            "weakest_reproducibility_seam": "The conclusion is cross-characteristic and depends on exact spectral projectors plus row-space joins rather than a characteristic-zero expanded matrix proof.",
        },
        "claim_ceiling": "Exact cross-characteristic obstruction for fixed-domain transport by the full K438 action commutant. The two rank-64 slow block row spaces are disjoint, so no A-commuting T satisfies T J0=X, despite large solution families in both fast blocks. This does not exclude a simultaneous source-domain reparameterization, field-dependent mixed Hessian, nonstationary construction, or common BV/Green domain and moves no source, ledger, canon, paper, public, novelty, prediction, confirmation, or physical conclusion.",
    }


def validate(payload: dict) -> None:
    theorem = payload["commutant_theorem"]
    ownership = payload["ownership_reconciliation"]
    decision = payload["decision"]
    assert len(payload["cross_characteristic_packets"]) == 2
    assert theorem["full_commutant_dimension"] == 81920
    assert theorem["slow_block_row_space_intersections"] == [0, 0]
    assert theorem["slow_block_row_space_joins"] == [128, 128]
    assert not theorem["fixed_domain_commuting_adapter_exists"]
    assert ownership["fixed_domain_nonpolynomial_commutant_adapter_excluded"]
    assert not ownership["source_domain_reparameterization_tested"]
    assert decision["K620_functional_calculus_obstruction_strengthened"]
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
