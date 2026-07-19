#!/usr/bin/env python
"""Construction-space P5 source-object specification gate.

This is P5-SOURCE-OBJECT-SPEC from the construction-space exploration map. It
checks that the frozen source-object interface contract names the four required
legs, preserves forbidden shortcuts, updates the map handoff, and leaves all
claim/status/posture boundaries unchanged.

Run: python tests/recovery-contract/construction_space_source_object_spec_p5.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CONTRACT = ROOT / "lab" / "process" / "source-object-interface-contract.md"
MAP = ROOT / "lab" / "process" / "construction-space-map.json"
PORTFOLIO = ROOT / "lab" / "process" / "research-portfolio.json"
P4_NOTE = ROOT / "explorations" / "construction-space-qm-checklist-p4-2026-07-19.md"

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL") + " :: " + name + ((" -- " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def log(message: str = "") -> None:
    print(message, flush=True)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_contract() -> tuple[str, dict]:
    text = CONTRACT.read_text(encoding="utf-8")
    match = re.search(
        r"## Machine-Readable Contract\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing Machine-Readable Contract JSON block")
    return text, json.loads(match.group(1))


def cell(map_data: dict, cell_id: str) -> dict:
    for entry in map_data["cells"]:
        if entry["id"] == cell_id:
            return entry
    raise AssertionError(f"missing construction-space cell {cell_id}")


def work_item(portfolio: dict, item_id: str) -> dict:
    for item in portfolio["work_items"]:
        if item["id"] == item_id:
            return item
    raise AssertionError(f"missing portfolio item {item_id}")


def recompute_coverage(map_data: dict) -> dict[str, int]:
    grades = [
        track.get("grade")
        for entry in map_data["cells"]
        for track in entry["tracks"].values()
    ]
    return {
        "cells": len(map_data["cells"]),
        "track_cells": sum(len(entry["tracks"]) for entry in map_data["cells"]),
        "dispositioned_track_cells": sum(grade != "OPEN" for grade in grades),
        "open": sum(grade == "OPEN" for grade in grades),
        "gated": sum(grade == "GATED" for grade in grades),
        "r0_failed": sum(grade == "R0_FAIL" for grade in grades),
    }


def leg(contract: dict, leg_id: str) -> dict:
    by_id = {entry["id"]: entry for entry in contract["legs"]}
    if leg_id not in by_id:
        raise AssertionError(f"missing contract leg {leg_id}")
    return by_id[leg_id]


def main() -> None:
    text, contract = load_contract()
    map_data = load_json(MAP)
    portfolio = load_json(PORTFOLIO)

    log("=" * 82)
    log("P5 contract identity")
    log("=" * 82)
    check("contract file exists", CONTRACT.exists(), str(CONTRACT))
    check("contract artifact id is stable", contract["artifact"] == "SOURCE_OBJECT_INTERFACE_CONTRACT")
    check("contract is P5", contract["probe"] == "P5-SOURCE-OBJECT-SPEC")
    check("contract is frozen spec without instance", contract["status"] == "FROZEN_SPEC_NO_INSTANCE")
    check("source owner is p2c", contract["source_owner"] == "possibility-to-capability")
    check("GU remains grade owner", contract["gu_owner"] == "gu-formalization")
    check("all four legs are present", {entry["id"] for entry in contract["legs"]} == {"GR", "QM", "COSMO", "SM"})
    check("p2c handoff is parent-routed", contract["handoffs"]["parent_route_required"] is True)

    log("")
    log("=" * 82)
    log("Shared source object requirements")
    log("=" * 82)
    identity = set(contract["source_requirements"]["identity"])
    sharedness = set(contract["source_requirements"]["sharedness"])
    for required in [
        "frozen_before_target_use",
        "source_owned_not_gu_constructed_from_consequence",
        "provenance_independent_of_gu_result",
        "normalizations_explicit",
        "non_retuning_conditions_explicit",
    ]:
        check(f"identity requires {required}", required in identity)
    for required in [
        "one_source_object_across_GR_QM_COSMO_SM",
        "shared_normalizations_or_explicit_loss_ledger",
        "typed_import_count_for_every_granted_object",
    ]:
        check(f"sharedness requires {required}", required in sharedness)

    log("")
    log("=" * 82)
    log("Leg requirements and forbidden shortcuts")
    log("=" * 82)
    expected_requirements = {
        "GR": {
            "vacuum_supported_source_or_residual_bookkeeping",
            "trace_free_QTF_slot_cancellation_or_evasion_at_order_M2",
            "ambient_H_class_first_variation_or_equivalent_source_tensor",
            "coefficient_frozen_before_schwarzschild_kerr_target_use",
            "linear_cheap_read_clears_preserved",
        },
        "QM": {
            "physical_quotient_or_field_complex",
            "state_space_or_local_algebra",
            "observable_admissibility",
            "probability_rule_with_positivity_and_normalization",
            "locality_or_causal_compatibility",
            "state_preserving_dynamics",
            "negative_norm_physical_state_discharge",
        },
        "COSMO": {
            "physical_scalar_projector",
            "gauge_invariant_observable_map",
            "closed_SVT_quadratic_truncation",
            "non_scalar_residue_discharge",
            "source_object_to_scalar_channel_binding",
        },
        "SM": {
            "source_owned_target_free_selector",
            "chirality_production",
            "three_generations_without_per_generation_adjustable_structure",
            "absolute_hypercharge_normalization",
            "physical_higgs_sector",
            "complete_surviving_spectrum",
            "extra_or_mirror_mode_decoupling",
        },
    }
    expected_forbidden = {
        "GR": "target_shaped_stress_import",
        "QM": "positive_hilbert_space_by_assumption",
        "COSMO": "standard_SVT_variable_as_GU_evidence",
        "SM": "host_group_as_selector",
    }
    for leg_id, required in expected_requirements.items():
        current = leg(contract, leg_id)
        check(f"{leg_id} supplies required slots", required <= set(current["must_supply"]))
        check(f"{leg_id} has forbidden shortcut sentinel", expected_forbidden[leg_id] in current["forbidden_shortcuts"])

    log("")
    log("=" * 82)
    log("Map and portfolio handoff")
    log("=" * 82)
    spec = map_data["source_object_interface_contract"]
    check("map records P5 complete", spec["status"] == "complete" and spec["probe"] == "P5-SOURCE-OBJECT-SPEC")
    check("map points to contract and this test", CONTRACT.as_posix().replace(str(ROOT).replace("\\", "/") + "/", "") in spec["evidence"] and "construction_space_source_object_spec_p5.py" in spec["test"])
    c4 = cell(map_data, "C4-BOUNDARY-ADAPTER")
    check("C4 typed adapter points to contract", c4["typed_adapter_interface"]["contract_ref"] == "lab/process/source-object-interface-contract.md")
    expected_coverage = recompute_coverage(map_data)
    actual_coverage = {key: map_data["coverage"][key] for key in expected_coverage}
    check("coverage arithmetic still matches cell ledger", actual_coverage == expected_coverage, f"{actual_coverage} vs {expected_coverage}")
    check("current coverage has not drifted from the cell ledger", actual_coverage == expected_coverage)
    round_seven = next((entry for entry in map_data["council_rounds"] if entry["round"] == 7), None)
    check("round 7 council is post-P5", round_seven is not None and "P5 complete" in round_seven["chairman_synthesis"])
    if round_seven is not None:
        check("round 7 P6 handoff is preserved", round_seven["ranked_search_plan"][0]["probe"] == "P6-CONDITIONAL-INTERIOR")

    construction = work_item(portfolio, "CONSTRUCTION-SPACE-EXPLORATION")
    dependency = work_item(portfolio, "DEP-NATIVE-SOURCE-DATUM")
    check("portfolio moves next swing to P6", "P5-SOURCE-OBJECT-SPEC completed" in construction["next_swing"] and "P6-CONDITIONAL-INTERIOR" in construction["next_swing"])
    check("DEP native source datum consumes frozen contract", "source-object interface contract" in dependency["next_swing"])

    log("")
    log("=" * 82)
    log("Boundary discipline")
    log("=" * 82)
    check("P4 evidence remains an input", str(P4_NOTE.relative_to(ROOT)).replace("\\", "/") in " ".join(contract["evidence_inputs"]))
    for phrase in [
        "No claim status",
        "canon verdict",
        "public posture",
        "external action",
        "not a global GU verdict",
    ]:
        check(f"contract states boundary: {phrase}", phrase in text)
    check("integration rule stays conditional", "concrete p2c instance is required" in contract["integration_rule"])

    if FAIL:
        log(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            log("  FAIL: " + name)
        raise SystemExit(1)
    log("\nRESULT: ALL PASS")


if __name__ == "__main__":
    main()
