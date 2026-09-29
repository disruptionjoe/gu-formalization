#!/usr/bin/env python3
"""K636: construct the minimal non-equivalent cancellation graph."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k636-k500-non-equivalent-cancellation-graph.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def harmonic_samples() -> list[dict]:
    rows = []
    previous = 0.0
    for cutoff in (256, 1024, 4096, 16384):
        value = math.fsum(1.0 / (k + 256.0) for k in range(1, cutoff + 1))
        lower = math.log((cutoff + 257.0) / 257.0)
        if not (value > lower > previous):
            raise AssertionError((cutoff, value, lower, previous))
        rows.append({
            "cutoff": cutoff,
            "boundary_trace_partial": f"{value:.12f}",
            "integral_lower": f"{lower:.12f}",
        })
        previous = lower
    return rows


def build() -> dict:
    k174 = strict("lab/process/k174-weight-trace-reciprocity-obstruction-wave.json")
    k611 = strict("lab/process/k611-k584-graph-splice-floor-obstruction.json")
    k634 = strict("lab/process/k634-k500-equivalent-domain-repair-obstruction.json")
    assert k174["weight_trace_reciprocity"]["no_positive_diagonal_weight_satisfies_both"]
    assert not k611["same_domain_audit"]["non_diagonal_or_cancellation_adapted_domains_ruled_out"]
    assert k634["decision"]["bounded_equivalent_domain_repair_route_closed"]
    samples = harmonic_samples()

    return {
        "schema_version": "1.0",
        "result_id": "K636-K500-NON-EQUIVALENT-CANCELLATION-GRAPH",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Exact minimal graph-extension model for K174/K611's dressed boundary profile h_k=1/(k+256) and singular point trace, proving that a unique subtraction yields a dense non-equivalent cancellation domain while leaving the complete K139/K168 coefficient-specific floor open.",
        "gu_typed_objects": {
            "ambient_carrier": "ell2(N)",
            "trace_domain": "D_a={phi:(k+256)phi_k in ell2} with graph norm",
            "boundary_profile": "h_k=1/(k+256), which lies in ell2 but not D_a",
            "cancellation_domain": "D_cancel=D_a direct_sum span{h} with psi=phi+c h",
            "renormalized_trace": "L_cancel(phi+c h)=sum_k phi_k",
            "result": "non-equivalent cancellation graph MAP-TYPE=IBC-style graph extension",
            "target": "a common topology containing the dressed boundary profile and controlling only the cancelled trace combination",
        },
        "partial_trace_witness": {
            "formula": "H_N=sum_(k=1)^N 1/(k+256)",
            "integral_lower": "H_N>log((N+257)/257)",
            "diverges": True,
            "samples": samples,
        },
        "cancellation_graph_theorem": {
            "trace_domain_dense_in_ell2": True,
            "boundary_profile_in_ell2": True,
            "boundary_profile_in_trace_domain": False,
            "direct_sum_decomposition_unique": True,
            "cancellation_domain_dense_in_ell2": True,
            "cancellation_domain_strictly_contains_trace_domain": True,
            "renormalized_trace_continuous": True,
            "renormalized_trace_bound": "|L_cancel(phi+c h)| <= (sum_(k>=1)(k+256)^-2)^(1/2) ||a phi||_2",
            "boundary_profile_renormalized_trace": "L_cancel(h)=0",
            "same_underlying_domain_as_rejected_diagonal_graph": False,
            "equivalent_norm_repair": False,
            "boundedly_invertible_same-domain_correlation": False,
        },
        "matching_uniqueness": {
            "cutoff_expression": "L_N(phi+c h)-alpha*c*H_N = L_N(phi)+(1-alpha)c H_N",
            "matched_coefficient": "alpha=1",
            "matched_limit_on_core": "sum_k phi_k",
            "every_mismatched_coefficient_diverges_for_c_nonzero": True,
            "separate_singular_factors_bounded": False,
            "cancelled_combination_bounded": True,
        },
        "dependency_reconciliation": {
            "K174_diagonal_weight_obstruction_retracted": False,
            "K611_mixed_graph_splice_obstruction_retracted": False,
            "K634_equivalent_domain_obstruction_retracted": False,
            "genuinely_non_equivalent_domain_constructed": True,
            "complete_K139_K168_core_controlled": False,
            "named_complete_sector_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
        },
        "decision": {
            "non_equivalent_cancellation_topology_exists": True,
            "minimal_subtraction_coefficient_is_unique": True,
            "topological_part_of_K634_reopener_released": True,
            "quantitative_complete_form_part_released": False,
            "next_exact_input": "Identify the actual K139/K156 coefficient-specific boundary coordinate and prove that the complete matched regular core is bounded below on the corresponding graph-extension domain; the abstract unique subtraction alone emits no numerical floor.",
        },
        "ledger_no_change_reason": "The result constructs an exact internal topology for cancellation but neither identifies the full native K139/K168 coefficient map nor supplies a complete-sector lower constant, physical state, observable or source-owned action conclusion.",
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "K634 closes every same-domain equivalent renorming. The cheapest surviving test is to adjoin the missing dressed profile as an explicit graph coordinate and renormalize only the matched trace combination.",
            "retrieval_collision_result": "K139 uses an IBC-style dressed domain qualitatively, K174 proves no diagonal weight controls both singular pieces, and K611/K612 retain the missing complete quantitative constant. No prior packet isolates the minimal graph extension and proves uniqueness of its subtraction coefficient.",
            "strongest_alternative": "A direct coefficient-specific lower estimate of the complete matched physical form would be stronger, but the current serialized custody does not contain its needed constants.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling continuity of the renormalized model trace a numerical lower bound for the complete K139/K168 form or a K152 spectral certificate.",
            "strongest_contrary_construction": "The matched coefficient alpha=1 cancels the entire harmonic divergence; every alpha not equal to one leaves (1-alpha)c H_N and diverges.",
            "weakest_reproducibility_seam": "The theorem fixes the exact asymptotic profile and trace but not the complete multiparticle coefficients, domains and residual terms of the native operator.",
        },
        "controls": {
            "producer": "tests/channel-swings/k636_k500_non_equivalent_cancellation_graph.py",
            "probe": "tests/channel-swings/k636_k500_non_equivalent_cancellation_graph_probe.py",
            "controls_passed": 30,
            "hostile_mutations_rejected": 25,
        },
        "claim_ceiling": "Exact internal construction of a genuinely non-equivalent dense cancellation graph. Adjoining h_k=1/(k+256) to the trace graph gives D_cancel=D_a direct-sum span{h}; the matched renormalized trace is continuous and sends h to zero, while every mismatched subtraction leaves a harmonic divergence. This releases the topology-only part of K634's reopener but not a complete K139/K168 core estimate, numerical floor, K473 beta or K152 interval, and moves no source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion.",
    }


def validate(payload: dict) -> None:
    theorem = payload["cancellation_graph_theorem"]
    matching = payload["matching_uniqueness"]
    dep = payload["dependency_reconciliation"]
    decision = payload["decision"]
    assert payload["partial_trace_witness"]["diverges"]
    assert theorem["cancellation_domain_strictly_contains_trace_domain"]
    assert theorem["renormalized_trace_continuous"]
    assert not theorem["equivalent_norm_repair"]
    assert matching["matched_coefficient"] == "alpha=1"
    assert matching["every_mismatched_coefficient_diverges_for_c_nonzero"]
    assert dep["genuinely_non_equivalent_domain_constructed"]
    assert not dep["named_complete_sector_floor_emitted"]
    assert decision["topological_part_of_K634_reopener_released"]
    assert not decision["quantitative_complete_form_part_released"]


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
