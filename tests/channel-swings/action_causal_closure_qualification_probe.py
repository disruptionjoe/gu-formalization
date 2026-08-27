#!/usr/bin/env python3
"""Custody gate for the action/causal closure candidate qualification."""

from __future__ import annotations

import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/action-causal-closure-qualification-v0.1.json"
PASSPORT = ROOT / "lab/specifications/theory-passport/gu-geometry-first-v0.1.yaml"

REQUIRED = [
    "real_coefficient_complete_action",
    "frozen_fields_constraints",
    "euler_noether_system",
    "common_principal_polynomial",
    "shared_cauchy_surfaces",
    "hyperbolicity",
    "physical_causal_domain_boundary",
    "green_boundary_form",
]
STATES = {"qualified", "partial", "absent", "wrong_object"}
IDS = {
    "K77-I1B-MIXED-ORDER",
    "K95-B5-STRICT-RS",
    "K77-OBSERVED-INCOMING-PROJECTOR",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def validate(registry: dict, passport: dict) -> list[str]:
    errors: list[str] = []
    if registry.get("required_objects") != REQUIRED:
        errors.append("eight-object burden denominator drifted")
    packets = registry.get("candidate_packets", [])
    if {row.get("id") for row in packets} != IDS:
        errors.append("candidate packet census drifted")
    if len(packets) != 3:
        errors.append("expected exactly three candidate packets")
    for packet in packets:
        cells = packet.get("cells", {})
        if list(cells) != REQUIRED:
            errors.append(f"{packet.get('id')}: cell order or denominator drifted")
        for key, cell in cells.items():
            if cell.get("state") not in STATES:
                errors.append(f"{packet.get('id')}:{key}: invalid qualification state")
            if not str(cell.get("reason", "")).strip():
                errors.append(f"{packet.get('id')}:{key}: missing reason")
        if packet.get("overall") != "not_qualified":
            errors.append(f"{packet.get('id')}: current packet must remain not_qualified")
        if all(cell.get("state") == "qualified" for cell in cells.values()):
            errors.append(f"{packet.get('id')}: silently closes the complete burden")
        for ref in packet.get("evidence_refs", []):
            if not (ROOT / ref).is_file():
                errors.append(f"{packet.get('id')}: missing evidence {ref}")
    composition = registry.get("composability", {})
    if composition.get("cross_packet_union_allowed") is not False:
        errors.append("cross-packet union must remain forbidden")
    result = registry.get("result", {})
    if result.get("burden_status") != "blocked":
        errors.append("burden status moved without one complete packet")
    if result.get("qualified_candidate_ids") != []:
        errors.append("qualified candidate set must remain empty")
    if result.get("current_root_candidate_set") != []:
        errors.append("root candidate set must remain empty")
    if "one source-authenticated or owner-native real coefficient-complete K77 action" not in result.get("exact_reopener", ""):
        errors.append("exact one-packet K77 reopener drifted")
    action = passport.get("critical_path", [{}])[0]
    if action.get("id") != "action_causal_closure" or action.get("status") != "blocked":
        errors.append("passport first burden must remain blocked")
    expected_refs = {str(REGISTRY.relative_to(ROOT)), registry.get("result_ref")}
    if not expected_refs.issubset(set(action.get("evidence_refs", []))):
        errors.append("passport does not bind both qualification evidence refs")
    if passport.get("truth_status", {}).get("current_root_candidate_set") != []:
        errors.append("passport root candidate set moved")
    if passport.get("export_contract", {}).get("status") != "not_ready":
        errors.append("passport export opened prematurely")
    return errors


def main() -> int:
    registry = load(REGISTRY)
    passport = load(PASSPORT)
    checks = [
        "denominator", "candidate census", "cell states", "evidence paths",
        "no complete candidate", "no cross-packet union", "passport block",
        "empty root", "fail-closed export", "exact reopener",
    ]
    errors = validate(registry, passport)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    mutations = []
    mutant = copy.deepcopy(registry)
    mutant["composability"]["cross_packet_union_allowed"] = True
    mutations.append(("union", mutant, passport))
    mutant = copy.deepcopy(registry)
    mutant["result"]["burden_status"] = "satisfied"
    mutations.append(("burden", mutant, passport))
    mutant = copy.deepcopy(registry)
    mutant["result"]["qualified_candidate_ids"] = ["K77-I1B-MIXED-ORDER"]
    mutations.append(("candidate", mutant, passport))
    mutant = copy.deepcopy(registry)
    mutant["candidate_packets"][0]["cells"][REQUIRED[3]]["state"] = "qualified"
    mutant["candidate_packets"][0]["overall"] = "qualified"
    mutations.append(("cell", mutant, passport))
    mutant = copy.deepcopy(registry)
    mutant["candidate_packets"][1]["evidence_refs"].append("missing.md")
    mutations.append(("evidence", mutant, passport))
    mutated_passport = copy.deepcopy(passport)
    mutated_passport["critical_path"][0]["status"] = "satisfied"
    mutations.append(("passport-status", registry, mutated_passport))
    mutated_passport = copy.deepcopy(passport)
    mutated_passport["truth_status"]["current_root_candidate_set"] = ["synthetic"]
    mutations.append(("root", registry, mutated_passport))
    mutant = copy.deepcopy(registry)
    mutant["result"]["exact_reopener"] = "find something"
    mutations.append(("reopener", mutant, passport))

    caught = sum(bool(validate(reg, pp)) for _, reg, pp in mutations)
    print(f"PASS {len(checks)}/{len(checks)} action/causal qualification checks")
    print(f"PASS {caught}/{len(mutations)} hostile mutations rejected")
    return 0 if caught == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
