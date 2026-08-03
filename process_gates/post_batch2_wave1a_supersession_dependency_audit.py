#!/usr/bin/env python3
"""Audit the nonterminal Wave-1A Batch-2 absorption contract.

This is a process/type gate.  It checks that the campaign cannot silently
reintroduce the corrected homonyms while waiting for the named Batch-3 fork
resolvers.  It does not validate any GU mathematical claim.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "explorations/cycle-gates-and-audits/post-batch2-wave1a-supersession-dependency-map.json"
REPORT = ROOT / "explorations/cycle-gates-and-audits/post-batch2-wave1a-supersession-dependency-map-2026-08-03.md"
SOURCE_ACTION = ROOT / "explorations/source-action-term-by-term-against-the-spec-2026-07-29.md"
DATUM_LEDGER = ROOT / "explorations/external-datum-ledger-and-the-2plus1-product-rule-2026-07-29.md"


def load_unique_json(path: Path) -> dict:
    def reject_duplicates(pairs: list[tuple[str, object]]) -> dict:
        result: dict = {}
        for key, value in pairs:
            assert key not in result, f"duplicate JSON key: {key}"
            result[key] = value
        return result

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicates)


def assert_contract(data: dict) -> None:
    assert data["artifact_type"] == "supersession_dependency_map"
    assert data["named_gate"] == "POST-B3-LANE-RESELECTION"
    assert data["gate_before"] == "OPEN"
    assert data["gate_after"] == "BATCH2_ABSORBED_AWAITING_BATCH3_FORK_RESOLVERS"
    assert data["route_disposition"] == "DEFER"
    assert data["third_lane_promoted"] is False
    assert data["input_revisions"]["batch2_corrected_main"] == "c8334177045467713c37abad12ca0e183f9dedcb"
    assert data["input_revisions"]["integration_base_after_batch3_process"] == "e53e8ae"

    correction_ids = {row["id"] for row in data["layer0_corrections"]}
    assert correction_ids == {
        "B2-COMPRESSION-NOT-PHYSICAL-OBSERVABLE",
        "B2-J-PARTITION-NOT-RANK",
        "B2-MULTIPLICITY-NOT-INDEX",
        "B2-LAMBDA5-SUPPORT-NOT-MASS",
        "B2-SPIN-INFLOW-NO-Z3",
    }

    dependency_classes = data["batch3_dependency_classes"]
    assert dependency_classes["before_final_wave1_and_wave2"] == ["M-H4", "M-H9"]
    assert dependency_classes["before_expensive_interior_euler"] == ["M-C2", "M-H11"]
    assert dependency_classes["before_boundary_promotion"] == ["M-H5", "M-H7", "M-H8", "M-H10"]
    assert dependency_classes["before_action_mass_anomaly_acceptance"] == ["M-H2", "M-H14"]
    assert dependency_classes["before_cosmology_only"] == ["M-H13"]
    assert data["batch3_process_progress"]["P-C3"] == "ALREADY_DISCHARGED_PROCESS at e53e8ae"
    assert data["batch3_process_progress"]["effect_on_scientific_fork_resolvers"] == "none"

    route_ids = {row["id"] for row in data["route_candidates"]}
    assert route_ids == {
        "CURRENT_INTERIOR_FULL_EULER",
        "ERIC_GUIDED_NATIVE_ACTION",
        "INDEPENDENT_NATIVE_ACTION",
        "BOUNDARY_ODD_PRIMARY_FAMILY",
    }
    independent = next(row for row in data["route_candidates"] if row["id"] == "INDEPENDENT_NATIVE_ACTION")
    assert independent["kind"] == "comparator_route_not_third_lane"
    boundary = next(row for row in data["route_candidates"] if row["id"] == "BOUNDARY_ODD_PRIMARY_FAMILY")
    assert boundary["kind"] == "candidate_family_not_single_route"
    assert set(boundary["subroutes"]) == {"framed_dim13", "string_refinement"}
    assert "no identification" in boundary["subroutes"]["string_refinement"]
    assert "same-object map" in boundary["merge_rule"]

    forbidden = set(data["forbidden_inferences"])
    assert {
        "COMPRESSION_COMMUTANT_IMPLIES_PHYSICAL_FREE_Z2",
        "J_BLOCK_COUNT_IMPLIES_H_RANK",
        "MULTIPLICITY_DECOMPOSITION_IMPLIES_CHIRAL_INDEX",
        "LAMBDA5_SUPPORT_IMPLIES_VEV_OR_MASS",
        "SPIN_DAI_FREED_TRANSPORTS_ORDER3_CLASS",
        "ORDER3_CLASS_IMPLIES_INTEGER_COUNT",
        "DATUM_MANUFACTURES_MISSING_MAP_OR_DOMAIN",
        "REAL_FORM_SELECTED_SILENTLY",
        "MATCHING_DIMENSIONS_ESTABLISH_SAME_OBJECT",
    } <= forbidden

    datum = data["external_datum_state"]
    assert "phase/orientation of the canonical vertical projected RS symbol" in datum["P2"]
    assert "integer-valued" in datum["P3"] and "reinstated" in datum["P3"]
    assert "not P3" in datum["order3_candidate"]
    assert "may not manufacture" in datum["hard_rule"]

    next_gate = data["next_gate"]
    assert next_gate["terminal_outputs"] == ["CONTINUE", "REBASE", "BRANCH", "MERGE", "KILL", "DEFER"]
    assert next_gate["required_output"].startswith("Exactly one")


def assert_owner_surfaces() -> None:
    report = REPORT.read_text(encoding="utf-8")
    action = SOURCE_ACTION.read_text(encoding="utf-8").replace("\n> ", " ")
    ledger = DATUM_LEDGER.read_text(encoding="utf-8").replace("\n> ", " ")
    assert "Batch 2 is now absorbed" in report
    assert "BATCH2_ABSORBED_AWAITING_BATCH3_FORK_RESOLVERS" in report
    assert "WAVE 1A CURRENT-STATE BANNER" in action
    assert "WAVE 1A CURRENT-STATE BANNER" in ledger
    assert "distinct integer-valued count/index datum" in action
    assert "P2 (typed at algebraic-candidate grade" in ledger
    assert "candidate order-3 homotopy carrier is not integer-valued P3" in ledger
    assert "may select among already admissible objects" in ledger


def run_planted_failures(data: dict) -> int:
    plants = []

    wrong_decision = dict(data)
    wrong_decision["route_disposition"] = "CONTINUE"
    plants.append(wrong_decision)

    promoted_lane = dict(data)
    promoted_lane["third_lane_promoted"] = True
    plants.append(promoted_lane)

    missing_real_form = dict(data)
    missing_real_form["batch3_dependency_classes"] = dict(data["batch3_dependency_classes"])
    missing_real_form["batch3_dependency_classes"]["before_final_wave1_and_wave2"] = ["M-H4"]
    plants.append(missing_real_form)

    missing_exact_derivative = dict(data)
    missing_exact_derivative["batch3_dependency_classes"] = dict(data["batch3_dependency_classes"])
    missing_exact_derivative["batch3_dependency_classes"]["before_expensive_interior_euler"] = ["M-H11"]
    plants.append(missing_exact_derivative)

    free_bit = dict(data)
    free_bit["forbidden_inferences"] = [
        item for item in data["forbidden_inferences"]
        if item != "COMPRESSION_COMMUTANT_IMPLIES_PHYSICAL_FREE_Z2"
    ]
    plants.append(free_bit)

    j_rank = dict(data)
    j_rank["forbidden_inferences"] = [
        item for item in data["forbidden_inferences"]
        if item != "J_BLOCK_COUNT_IMPLIES_H_RANK"
    ]
    plants.append(j_rank)

    order3_count = dict(data)
    order3_count["forbidden_inferences"] = [
        item for item in data["forbidden_inferences"]
        if item != "ORDER3_CLASS_IMPLIES_INTEGER_COUNT"
    ]
    plants.append(order3_count)

    datum_magic = dict(data)
    datum_magic["external_datum_state"] = dict(data["external_datum_state"])
    datum_magic["external_datum_state"]["hard_rule"] = "A datum may supply every missing object."
    plants.append(datum_magic)

    p2_untyped = dict(data)
    p2_untyped["external_datum_state"] = dict(data["external_datum_state"])
    p2_untyped["external_datum_state"]["P2"] = "X-sector datum; type unknown"
    plants.append(p2_untyped)

    third_route = dict(data)
    third_route["route_candidates"] = [dict(row) for row in data["route_candidates"]]
    for row in third_route["route_candidates"]:
        if row["id"] == "INDEPENDENT_NATIVE_ACTION":
            row["kind"] = "promoted_third_lane"
    plants.append(third_route)

    rejected = 0
    for plant in plants:
        try:
            assert_contract(plant)
        except AssertionError:
            rejected += 1
    assert rejected == len(plants)
    return rejected


def main() -> int:
    data = load_unique_json(REGISTRY)
    assert_contract(data)
    assert_owner_surfaces()
    planted = run_planted_failures(data)
    print(f"VERDICT: PASS - 37 exact/type assertions + {planted} planted failures")
    print("SCOPE: process/type absorption only; no GU mathematical claim is certified here.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
