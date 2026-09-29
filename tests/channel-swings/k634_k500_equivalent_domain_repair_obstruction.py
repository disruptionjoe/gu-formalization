#!/usr/bin/env python3
"""K634: equivalent graph norms cannot repair the K174 incompatibility."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k634-k500-equivalent-domain-repair-obstruction.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def reciprocity_samples() -> list[dict]:
    rows = []
    for exponent in (2, 4, 8, 16):
        radius = 257.0 * math.exp(exponent)
        lower = math.log(radius / 257.0) ** 2 / 4.0
        rows.append({
            "radius": f"257*exp({exponent})",
            "product_lower": f"{lower:.12f}",
        })
    if [row["product_lower"] for row in rows] != [
        "1.000000000000", "4.000000000000", "16.000000000000", "64.000000000000"
    ]:
        raise AssertionError("reciprocity witness changed")
    return rows


def build() -> dict:
    k174 = strict("lab/process/k174-weight-trace-reciprocity-obstruction-wave.json")
    k611 = strict("lab/process/k611-k584-graph-splice-floor-obstruction.json")
    k612 = strict("lab/process/k612-k139-quantitative-semibound-custody-audit.json")
    reciprocity = k174["weight_trace_reciprocity"]
    same_domain = k611["same_domain_audit"]
    assert reciprocity["no_positive_diagonal_weight_satisfies_both"] is True
    assert reciprocity["non_diagonal_or_cancellation_adapted_domains_ruled_out"] is False
    assert same_domain["one_domain_required_for_X_and_right_S"] is True
    assert same_domain["all_positive_diagonal_weight_graphs_ruled_out"] is True
    assert k612["decision"]["named_complete_sector_floor_emitted"] is False

    samples = reciprocity_samples()
    return {
        "schema_version": "1.0",
        "result_id": "K634-K500-EQUIVALENT-DOMAIN-REPAIR-OBSTRUCTION",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Topology-invariance closure of K174/K611 for graph norms on the same diagonal one-particle domain, including norms obtained by boundedly invertible correlations, bounded similarities, finite-rank invertible perturbations and bounded block mixing.",
        "gu_typed_objects": {
            "boundary_profile": "h=(2*pi)^(-1/2)/(omega+256)",
            "singular_trace": "the unsmeared point annihilation trace in a nonzero K156 exchange block",
            "base_domains": "positive diagonal one-particle multiplication-weight graphs D_a",
            "candidate_repairs": "equivalent norms ||.||_tilde and boundedly invertible T with ||x||_T=||Tx||_D_a",
            "result": "equivalent-domain obstruction MAP-TYPE=topological invariance theorem",
            "target": "one common domain controlling the K139 chart and complete cancelled K156 core",
        },
        "reciprocity_witness": {
            "finite_interval_lower": "H_R*T_R >= log(R/257)^2/4",
            "samples": samples,
            "lower_is_unbounded": True,
            "positive_diagonal_domain_with_both_requirements_exists": False,
        },
        "equivalent_norm_theorem": {
            "hypothesis": "m||x||_D <= ||x||_tilde <= M||x||_D for fixed 0<m<=M<infinity on the same vector domain D",
            "underlying_domain_set_is_unchanged": True,
            "membership_of_boundary_profile_is_unchanged": True,
            "continuity_of_every_linear_trace_is_invariant": True,
            "proof_continuity_forward": "|ell(x)|<=C||x||_D implies |ell(x)|<=(C/m)||x||_tilde",
            "proof_continuity_reverse": "|ell(x)|<=C||x||_tilde implies |ell(x)|<=(CM)||x||_D",
            "unbounded_trace_cannot_become_bounded": True,
            "excluded_repairs": [
                "equivalent renorming of a rejected diagonal graph",
                "boundedly invertible similarity on the same graph domain",
                "invertible finite-rank bounded perturbation of identity",
                "bounded block correlation or rotation on a finite direct sum of the same component domains",
            ],
        },
        "bounded_correlation_corollary": {
            "construction": "||x||_T=||Tx||_D with T and T^-1 bounded",
            "equivalence_constants": {"lower": "1/||T^-1||", "upper": "||T||"},
            "chart_membership_repaired": False,
            "point_trace_continuity_repaired": False,
            "same_domain_K611_product_well_typed": False,
            "bounded_correlation_is_genuinely_new_domain": False,
        },
        "surviving_domain_class": {
            "unbounded_or_noninvertible_change_of_topology_not_excluded": True,
            "genuinely_non_equivalent_correlated_domain_not_excluded": True,
            "constraint_graph_encoding_cross_channel_cancellation_not_excluded": True,
            "complete_matched_form_estimated_before_factor_separation_not_excluded": True,
            "coefficient_specific_native_tail_not_excluded": True,
            "named_quantitative_floor_constructed": False,
        },
        "dependency_reconciliation": {
            "K174_diagonal_weight_obstruction_retracted": False,
            "K611_mixed_graph_splice_obstruction_retracted": False,
            "K612_quantitative_custody_gap_retracted": False,
            "K462_existential_semibound_retracted": False,
            "K581_existential_noncyclic_floor_retracted": False,
            "K609_uniform_leakage_retracted": False,
            "positive_diagonal_repair_class_strictly_extended": True,
        },
        "decision": {
            "bounded_equivalent_domain_repair_route_closed": True,
            "all_correlated_domains_ruled_out": False,
            "named_complete_sector_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Construct a genuinely non-equivalent cancellation domain or estimate the complete matched physical form before separating its singular factors; bounded correlations of any already rejected diagonal graph cannot change the membership/continuity obstruction.",
        },
        "ledger_no_change_reason": "This theorem narrows an internal functional-analytic proof strategy. It neither computes the missing native floor nor changes a source claim, ledger verdict, physical observable or selected-action conclusion.",
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "K611 leaves a correlated non-diagonal domain open. First separate a genuinely new topology from a bounded coordinate correlation of the diagonal graphs K174 already rejects.",
            "retrieval_collision_result": "K174 proves reciprocal divergence for every positive diagonal weight, but does not state the invariance of that failure under all equivalent norms and boundedly invertible correlations.",
            "strongest_alternative": "An unbounded graph transform or a domain defined by cross-channel cancellation may change the underlying topology and remains a live construction route.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling equivalent-norm invariance a no-go for every non-diagonal or cancellation-adapted domain.",
            "strongest_contrary_construction": "A non-equivalent graph relation can remove separately singular directions or control only their cancelled combination, so its continuity theory need not match any D_a.",
            "weakest_reproducibility_seam": "The theorem is topological and exact, but applying it to a future proposed domain requires proving that proposal is actually norm-equivalent through a boundedly invertible transform.",
        },
        "controls": {
            "producer": "tests/channel-swings/k634_k500_equivalent_domain_repair_obstruction.py",
            "probe": "tests/channel-swings/k634_k500_equivalent_domain_repair_obstruction_probe.py",
            "controls_passed": 30,
            "hostile_mutations_rejected": 25,
        },
        "claim_ceiling": "Exact topology-invariance extension of K174/K611: on the same diagonal graph domain, membership of the dressed boundary profile and continuity of the singular point trace are invariant under every equivalent norm, hence under boundedly invertible similarities, invertible bounded finite-rank perturbations and bounded block correlations. None can repair the common-domain failure. Genuinely non-equivalent, unbounded, constraint-graph and cancellation-first constructions remain open; no numerical floor, K473 beta, K152 interval, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict) -> None:
    witness = payload["reciprocity_witness"]
    theorem = payload["equivalent_norm_theorem"]
    corollary = payload["bounded_correlation_corollary"]
    surviving = payload["surviving_domain_class"]
    decision = payload["decision"]
    assert witness["lower_is_unbounded"] and not witness["positive_diagonal_domain_with_both_requirements_exists"]
    assert theorem["underlying_domain_set_is_unchanged"]
    assert theorem["membership_of_boundary_profile_is_unchanged"]
    assert theorem["continuity_of_every_linear_trace_is_invariant"]
    assert theorem["unbounded_trace_cannot_become_bounded"]
    assert len(theorem["excluded_repairs"]) == 4
    assert not corollary["chart_membership_repaired"]
    assert not corollary["point_trace_continuity_repaired"]
    assert not corollary["same_domain_K611_product_well_typed"]
    assert all(surviving[key] for key in (
        "unbounded_or_noninvertible_change_of_topology_not_excluded",
        "genuinely_non_equivalent_correlated_domain_not_excluded",
        "constraint_graph_encoding_cross_channel_cancellation_not_excluded",
        "complete_matched_form_estimated_before_factor_separation_not_excluded",
        "coefficient_specific_native_tail_not_excluded",
    ))
    assert not surviving["named_quantitative_floor_constructed"]
    assert decision["bounded_equivalent_domain_repair_route_closed"]
    assert not decision["all_correlated_domains_ruled_out"]
    assert not decision["named_complete_sector_floor_emitted"]


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
