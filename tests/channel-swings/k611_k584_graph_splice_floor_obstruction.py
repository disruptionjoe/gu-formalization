#!/usr/bin/env python3
"""K611 rejects a mixed-topology numerical floor extraction.

The tempting estimate combines a Hilbert/number-graph Neumann inverse with a
free-energy-graph bound for the normal-ordered core.  K173 and K174 prove that
those bounds do not coexist on one admissible diagonal-weight graph.  This
compiler makes the failed multiplication explicit and preserves the valid
existential semibound and K609 leakage certificate.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k611-k584-graph-splice-floor-obstruction.json"


def strict(path: str) -> dict[str, Any]:
    return json.loads((ROOT / path).read_text())


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k173 = strict("lab/process/k173-two-graph-tail-obstruction-wave.json")
    k174 = strict("lab/process/k174-weight-trace-reciprocity-obstruction-wave.json")
    k462 = strict("lab/process/k462-k152-center-zero-coercivity-extraction.json")
    k581 = strict("lab/process/k581-k500-noncyclic-semibound-inheritance.json")
    k584 = strict("lab/process/k584-k581-noncyclic-floor-identifiability.json")
    k609 = strict("lab/process/k609-k500-complete-uniform-leakage-enclosure.json")

    # Arithmetic of the rejected proposal.  The numbers are internally
    # consistent, but the second inverse factor is unavailable on the graph
    # on which the core bound lives.
    q_h = Fraction(1, 6)
    proposed_q_d = Fraction(1, 3)
    core_graph_relative = Fraction(5, 12)
    scalar_piece = Fraction(3, 25)
    proposed_core_piece = (1 / (1 - q_h)) * core_graph_relative * (1 / (1 - proposed_q_d))
    proposed_total = scalar_piece + proposed_core_piece

    free = k173["two_graph_replay"]
    quarter = k174["quarter_graph"]
    reciprocity = k174["weight_trace_reciprocity"]

    return {
        "schema_version": "1.0",
        "result_id": "K611-K584-GRAPH-SPLICE-FLOOR-OBSTRUCTION",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The proposed K584 numerical complete-sector floor obtained by multiplying a K139 Hilbert/number-graph chart inverse bound with a K156 free-energy-graph normal-ordered-core bound.",
        "gu_typed_objects": {
            "carrier": "K162 hard-core C3 tensor antisymmetric Fock q00/q10/q01 sectors",
            "form": "the fixed K139/K168 center-zero form after exact endpoint cancellation",
            "pairing": "physical positive M=S* S Hilbert geometry",
            "result": "same-domain floor-route obstruction MAP-TYPE=topology-typecheck",
            "target": "K584's missing named complete-sector lower witness",
        },
        "rejected_candidate_arithmetic": {
            "hilbert_chart_contraction_assumed": qstr(q_h),
            "free_graph_chart_contraction_assumed": qstr(proposed_q_d),
            "normal_ordered_core_graph_relative_assumed": qstr(core_graph_relative),
            "scalar_resolvent_piece": qstr(scalar_piece),
            "proposed_core_resolvent_piece": qstr(proposed_core_piece),
            "proposed_total": qstr(proposed_total),
            "arithmetic_is_internally_consistent": proposed_total == Fraction(87, 100),
            "operator_norm_product_is_well_typed": False,
            "candidate_floor_certified": False,
        },
        "same_domain_audit": {
            "required_product": "||S||_(H->H) ||X||_(D->H) ||S||_(D->D)",
            "one_domain_required_for_X_and_right_S": True,
            "free_energy_graph_controls_normal_ordered_core": True,
            "free_energy_graph_has_finite_chart_contraction": free["free_energy_graph_finite_q_D"],
            "free_energy_failure": free["free_energy_graph_reason"],
            "particle_number_graph_chart_contraction_upper": free["particle_number_graph_q_D_upper"],
            "particle_number_graph_has_finite_core_bound": free["particle_number_graph_finite_B"],
            "particle_number_failure": free["particle_number_graph_reason"],
            "quarter_graph_chart_contraction_upper": quarter["G_graph_contraction_upper"],
            "quarter_graph_has_complete_core_bound": quarter["complete_W_graph_to_Hilbert_bounded"],
            "all_positive_diagonal_weight_graphs_ruled_out": reciprocity["no_positive_diagonal_weight_satisfies_both"],
            "non_diagonal_or_cancellation_adapted_domains_ruled_out": reciprocity["non_diagonal_or_cancellation_adapted_domains_ruled_out"],
        },
        "dependency_reconciliation": {
            "K462_existential_complete_sector_semibound_preserved": k462["continuum_composition"]["existential_center_zero_coercivity_proved"],
            "K581_existential_noncyclic_floor_preserved": k581["native_composition"]["existential_native_noncyclic_floor_proved"],
            "K584_identifiability_obstruction_preserved": not k584["decision"]["current_native_named_r0_serialized"],
            "K609_uniform_leakage_preserved": k609["decision"]["complete_K500_uniform_leakage_strictly_below_one_third"],
            "K609_reused_as_floor_evidence": False,
            "K139_or_K156_retracted": False,
        },
        "decision": {
            "mixed_graph_numerical_floor_route_rejected": True,
            "named_complete_sector_floor_emitted": False,
            "named_noncyclic_floor_emitted": False,
            "K473_released": False,
            "native_K152_interval_emitted": False,
            "surviving_routes": [
                "extract explicit constants from K139's original matched physical-form semiboundedness proof",
                "prove a direct cancellation-adapted quadratic-form lower bound on the physical IBC domain",
                "construct a correlated non-diagonal domain on which the complete cancelled core and chart are jointly controlled",
            ],
            "next_exact_input": "Produce one cancellation-adapted same-domain lower estimate for the complete matched form; do not multiply particle-number/Hilbert chart bounds by free-energy-graph core bounds or estimate the singular exchange factors separately.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact topology audit of one proposed numerical floor route. Its rational Neumann arithmetic reaches 87/100, but the operator product is ill-typed because the chart and complete normal-ordered core bounds live on incompatible graphs; K174 rules out every positive diagonal-weight repair. K462/K581 existential semiboundedness and K609 leakage remain valid, while no numerical floor, K473 beta, K152 interval, source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion follows.",
    }


def validate(payload: dict[str, Any]) -> None:
    a = payload["rejected_candidate_arithmetic"]
    s = payload["same_domain_audit"]
    r = payload["dependency_reconciliation"]
    d = payload["decision"]
    assert a["proposed_core_resolvent_piece"] == "3/4"
    assert a["proposed_total"] == "87/100" and a["arithmetic_is_internally_consistent"]
    assert not a["operator_norm_product_is_well_typed"] and not a["candidate_floor_certified"]
    assert s["one_domain_required_for_X_and_right_S"] and s["free_energy_graph_controls_normal_ordered_core"]
    assert not s["free_energy_graph_has_finite_chart_contraction"]
    assert s["particle_number_graph_chart_contraction_upper"] == "3/4"
    assert not s["particle_number_graph_has_finite_core_bound"]
    assert s["quarter_graph_chart_contraction_upper"] == "131/300"
    assert not s["quarter_graph_has_complete_core_bound"]
    assert s["all_positive_diagonal_weight_graphs_ruled_out"]
    assert not s["non_diagonal_or_cancellation_adapted_domains_ruled_out"]
    assert all((r["K462_existential_complete_sector_semibound_preserved"], r["K581_existential_noncyclic_floor_preserved"], r["K584_identifiability_obstruction_preserved"], r["K609_uniform_leakage_preserved"]))
    assert not r["K609_reused_as_floor_evidence"] and not r["K139_or_K156_retracted"]
    assert d["mixed_graph_numerical_floor_route_rejected"] and not d["named_complete_sector_floor_emitted"]
    assert not d["named_noncyclic_floor_emitted"] and not d["K473_released"] and not d["native_K152_interval_emitted"]
    assert len(d["surviving_routes"]) == 3


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
