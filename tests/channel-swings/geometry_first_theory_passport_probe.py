#!/usr/bin/env python3
"""Semantic and hostile-mutation gate for the GU geometry-first passport."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PASSPORT = ROOT / "lab/specifications/theory-passport/gu-geometry-first-v0.1.yaml"
SCHEMA = ROOT / "lab/specifications/theory-passport/theory-passport-v0.1.schema.json"
AGENDA = ROOT / "lab/process/RESEARCH-AGENDA.json"
PROGRAM = ROOT / "RESEARCH-PROGRAM.md"

PROGRAM_ID = "GU-GEOMETRY-FIRST-DYNAMICAL-UNIFICATION"
AGENDA_ID = "CONDITIONAL-BUILD-REVERSE-SCAFFOLD"
BURDENS = ["action_causal_closure", "physical_state_space", "observable_export"]
FROZEN = {
    "action_coefficients", "vacuum_background", "stabilizer_spectrum",
    "causal_domain_boundary", "physical_quotient_state_pairing",
    "projection_parameters", "held_out_consequence",
}
COMPARATORS = {
    "general_relativity", "standard_model", "ordinary_qft_eft_quantization",
    "thermodynamics_cosmology", "non_gu_unification", "null_or_rival_model",
}


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict), f"{path}: root must be an object"
    return value


def violations(p: dict) -> list[str]:
    errors: list[str] = []
    program = p.get("program", {})
    if program.get("id") != PROGRAM_ID or program.get("agenda_item") != AGENDA_ID:
        errors.append("program identity drift")
    truth = p.get("truth_status", {})
    if truth.get("grade") != "research_architecture_only" or truth.get("claim_effect") != "none":
        errors.append("architecture promoted into evidence")
    if truth.get("current_root_candidate_set") != []:
        errors.append("empty B2 root candidate set changed")

    path = p.get("critical_path", [])
    if [row.get("id") for row in path] != BURDENS or [row.get("order") for row in path] != [1, 2, 3]:
        errors.append("critical path order changed")
    expected_dependencies = [[], [BURDENS[0]], [BURDENS[1]]]
    if [row.get("depends_on") for row in path] != expected_dependencies:
        errors.append("critical path can be skipped")
    if any(row.get("status") != "blocked" for row in path):
        errors.append("an unsatisfied burden was opened or satisfied")
    required = [set(row.get("required_objects", [])) for row in path]
    if not {"real_coefficient_complete_action", "euler_noether_system", "common_principal_polynomial",
            "shared_cauchy_surfaces", "hyperbolicity", "physical_causal_domain_boundary",
            "green_boundary_form"}.issubset(required[0]):
        errors.append("action/causal/boundary burden incomplete")
    if not {"coupled_gauge_bv_bfv_complex", "common_closed_domain", "reduced_physical_cohomology",
            "conserved_positive_pairing", "local_to_global_descent", "holonomy_factorization"}.issubset(required[1]):
        errors.append("physical state or local-to-global burden incomplete")
    if not {"normal_mode_reduction", "controlled_memory_kernel_or_process", "preparation",
            "intervention", "detector", "record", "finite_observable", "held_out_consequence"}.issubset(required[2]):
        errors.append("observable process burden incomplete")

    wall = p.get("freeze_wall", {})
    if wall.get("timing") != "before_observable_scoring" or set(wall.get("frozen_before_scoring", [])) != FROZEN:
        errors.append("freeze wall incomplete or late")
    null = p.get("null_hypothesis", {})
    if null.get("id") != "H0" or null.get("status") != "live":
        errors.append("null hypothesis not live")
    if set(p.get("comparators", [])) != COMPARATORS:
        errors.append("held-out comparator set changed")
    export = p.get("export_contract", {})
    if export.get("target") != "dynamic-unity" or export.get("status") != "not_ready":
        errors.append("export opened without a qualified payload")
    if len(set(export.get("required_payload", []))) < 5:
        errors.append("qualified export payload incomplete")
    if p.get("promotion", {}).get("scientific_promotions") != []:
        errors.append("scientific promotion present")
    return errors


def main() -> int:
    passport = load(PASSPORT)
    schema = load(SCHEMA)
    assert schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema"
    assert not violations(passport), violations(passport)

    agenda = load(AGENDA)
    item = next(row for row in agenda["work_items"] if row["id"] == AGENDA_ID)
    assert item["program_identity"] == PROGRAM_ID
    assert item["theory_passport_ref"] == "lab/specifications/theory-passport/gu-geometry-first-v0.1.yaml"
    assert item["critical_path"]["ordered_burdens"] == BURDENS
    assert item["critical_path"]["skip_policy"] == "forbidden"
    assert item["export_status"] == "NOT_READY"
    assert PROGRAM_ID in PROGRAM.read_text(encoding="utf-8")

    mutations = []
    p = deepcopy(passport); p["critical_path"][0]["required_objects"].remove("real_coefficient_complete_action"); mutations.append(p)
    p = deepcopy(passport); p["critical_path"][2]["status"] = "satisfied"; mutations.append(p)
    p = deepcopy(passport); p["critical_path"][1]["depends_on"] = []; mutations.append(p)
    p = deepcopy(passport); p["null_hypothesis"]["status"] = "retired"; mutations.append(p)
    p = deepcopy(passport); p["critical_path"][1]["required_objects"].remove("conserved_positive_pairing"); mutations.append(p)
    p = deepcopy(passport); p["critical_path"][0]["required_objects"].remove("green_boundary_form"); mutations.append(p)
    p = deepcopy(passport); p["freeze_wall"]["frozen_before_scoring"].remove("held_out_consequence"); mutations.append(p)
    p = deepcopy(passport); p["export_contract"]["status"] = "ready"; mutations.append(p)
    p = deepcopy(passport); p["promotion"]["scientific_promotions"] = ["unification established"]; mutations.append(p)

    for index, mutation in enumerate(mutations, 1):
        assert violations(mutation), f"planted mutation {index} escaped"
    print(f"PASS geometry-first theory passport: 11 positive contracts, {len(mutations)}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
