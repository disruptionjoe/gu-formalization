#!/usr/bin/env python3
"""Reusable audit for registries carrying rsap_ambient_stratum_discriminator."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_GLOB = "selected-k*.json"
BEGIN = "<!-- RSAP_AMBIENT_STRATUM_DECISION_V1_BEGIN -->"
END = "<!-- RSAP_AMBIENT_STRATUM_DECISION_V1_END -->"
FORBIDDEN_KEYS = {
    "run_id", "envelope_digest", "service_lane", "scheduler",
    "model_effort", "execution_claim", "runtime_receipt",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def pointer(document: Any, value: str) -> Any:
    if not value.startswith("#/"):
        raise ValueError(f"unsupported local JSON pointer: {value}")
    current = document
    for token in value[2:].split("/"):
        token = token.replace("~1", "/").replace("~0", "~")
        current = current[int(token)] if isinstance(current, list) else current[token]
    return current


def external_pointer(root: Path, ref: dict[str, Any]) -> Any:
    document = load(root / ref["path"])
    current: Any = document
    for token in ref["json_pointer"].lstrip("/").split("/"):
        if token:
            current = current[int(token)] if isinstance(current, list) else current[token]
    return current


def forbidden_keys(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        found.update(FORBIDDEN_KEYS.intersection(value))
        for child in value.values():
            found.update(forbidden_keys(child))
    elif isinstance(value, list):
        for child in value:
            found.update(forbidden_keys(child))
    return found


def narrative_summary(root: Path, path: str) -> dict[str, Any]:
    text = (root / path).read_text(encoding="utf-8")
    if text.count(BEGIN) != 1 or text.count(END) != 1:
        raise ValueError("NARRATIVE_DECISION_MARKERS_MISSING_OR_DUPLICATED")
    body = text.split(BEGIN, 1)[1].split(END, 1)[0].strip()
    if not body.startswith("```json") or not body.endswith("```"):
        raise ValueError("NARRATIVE_DECISION_BLOCK_NOT_JSON")
    return json.loads(body[len("```json"): -len("```")].strip())


def validate_registry(registry: dict[str, Any], root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    contract = registry.get("ambient_discriminator_contract")
    if not isinstance(contract, dict):
        return ["MISSING_AMBIENT_DISCRIMINATOR_CONTRACT"]

    required = {
        "contract_id", "contract_version", "schema_ref", "candidate_scope", "typing",
        "ambient_object", "table_refs", "source_refs", "contrary_controls",
        "transfer_decision", "interval_effect", "successor_gate",
        "decision_summary", "mutation_controls",
    }
    if missing := sorted(required - set(contract)):
        errors.append("MISSING_FIELDS:" + ",".join(missing))
    if contract.get("contract_id") != "rsap_ambient_stratum_discriminator":
        errors.append("WRONG_CONTRACT_ID")
    if contract.get("contract_version") != "1.0":
        errors.append("WRONG_CONTRACT_VERSION")
    schema_ref = contract.get("schema_ref")
    if schema_ref != "lab/process/ambient-stratum-contract.schema.json" or not (root / str(schema_ref)).is_file():
        errors.append("BROKEN_SCHEMA_REFERENCE")
    if forbidden := sorted(forbidden_keys(contract)):
        errors.append("PRIVATE_EXECUTION_METADATA:" + ",".join(forbidden))

    candidate_scope = contract.get("candidate_scope", {})
    if candidate_scope.get("included") != "FIXED_CARTAN_SEMISIMPLE_ONE_ROOT_RANK_FOUR_EXTENSIONS":
        errors.append("CANDIDATE_SCOPE_NOT_QUALIFIED")
    if "NONSEMISIMPLE_OR_MULTI_ROOT_AMBIENT_PATHS" not in candidate_scope.get("not_exhausted", []):
        errors.append("NONSEMISIMPLE_MULTI_ROOT_SCOPE_MISSING")

    ambient = contract.get("ambient_object", {})
    required_witnesses = ambient.get("required_witnesses", [])
    owned = ambient.get("owned_witnesses", [])
    selected = ambient.get("selection_status")
    if selected != "TYPE_MISSING" and not set(required_witnesses).issubset(owned):
        errors.append("SELECTION_REQUIRES_OWNED_AMBIENT_WITNESS")
    if ambient.get("owner_status") != "NOT_PROVIDED" and not owned:
        errors.append("OWNER_STATUS_REQUIRES_WITNESS")
    invariant = ambient.get("invariant_tuple", {})
    missing_values = {
        "support_dimension", "support_signature", "intersection_signature",
        "real_support_type", "orbit_closure_parent", "orbit_closure_order",
        "actual_centralizer_component",
    }
    if any(invariant.get(key) != "NOT_PROVIDED" for key in missing_values):
        errors.append("UNOWNED_AMBIENT_INVARIANT_PROMOTED")

    try:
        candidate_rows = pointer(registry, contract["table_refs"]["candidate_extensions"])
        rank_rows = pointer(registry, contract["table_refs"]["rank_schedule"])
    except (KeyError, TypeError, ValueError, IndexError) as exc:
        errors.append("BROKEN_TABLE_POINTER:" + str(exc))
        candidate_rows, rank_rows = [], []

    rank_by_type = {row.get("type"): row for row in rank_rows}
    for row in candidate_rows:
        name = row.get("type")
        roots = row.get("subsystem_root_count")
        expected_centralizer = 7 + roots if isinstance(roots, int) else None
        expected_target = 91 - expected_centralizer if expected_centralizer is not None else None
        expected_ceiling = (98 + expected_target) // 2 if expected_target is not None else None
        if row.get("ambient_centralizer_dimension") != expected_centralizer:
            errors.append(f"CENTRALIZER_FORMULA:{name}")
        if row.get("ambient_target_poisson_rank") != expected_target:
            errors.append(f"TARGET_RANK_FORMULA:{name}")
        if row.get("pointwise_98d_map_rank_ceiling") != expected_ceiling:
            errors.append(f"MAP_CEILING_FORMULA:{name}")
        scheduled = rank_by_type.get(name, {})
        if scheduled.get("target_poisson_rank") != expected_target:
            errors.append(f"RANK_TABLE_TARGET_MISMATCH:{name}")
        if scheduled.get("map_rank_ceiling") != expected_ceiling:
            errors.append(f"RANK_TABLE_CEILING_MISMATCH:{name}")
        if scheduled.get("forced_loss_from_85") != 85 - expected_ceiling:
            errors.append(f"RANK_TABLE_LOSS_MISMATCH:{name}")
        if scheduled.get("map_rank_status") == "ACHIEVED" and not scheduled.get("construction_witness_ref"):
            errors.append("ACHIEVED_RANK_REQUIRES_CONSTRUCTION_WITNESS")
    if sum(row.get("extension_root_multiplicity", 0) for row in candidate_rows) != registry.get("classification", {}).get("outside_root_count"):
        errors.append("MULTIPLICITIES_DO_NOT_EXHAUST_OUTSIDE_ROOTS")

    refs = {ref["id"]: ref for ref in contract.get("source_refs", [])}
    try:
        k80_models = external_pointer(root, refs["k80_relative_models"])
        for control in contract.get("contrary_controls", []):
            if k80_models.get(control["source_key"]) != control["expected_tuple"]:
                errors.append("CONTRARY_CONTROL_MISMATCH:" + control["id"])
        k81_missing = external_pointer(root, refs["k81_missing_joint_type"])
        if k81_missing.get("selected_relative_orbit") != "TYPE_MISSING":
            errors.append("K81_TYPE_MISSING_CONTROL_FAILED")
        k87 = external_pointer(root, refs["k87_resolution"])
        if k87 != "ACHIEVED_AND_BOUND_SATURATING":
            errors.append("K87_SUCCESSOR_RESOLUTION_MISMATCH")
    except (KeyError, TypeError, ValueError, IndexError, FileNotFoundError) as exc:
        errors.append("BROKEN_SOURCE_REFERENCE:" + str(exc))

    transfer = contract.get("transfer_decision", {})
    if transfer.get("ambient_edge") != "DO_NOT_ADD" or transfer.get("rank_schedule_transfer") != "NOT_LICENSED":
        errors.append("TYPE_MISSING_TRANSFER_MUST_BE_PROHIBITED")
    interval = contract.get("interval_effect", {})
    if interval.get("before") != [98, 182] or interval.get("after") != [98, 182] or interval.get("tightened") is not False:
        errors.append("BOUND_INTERVAL_EFFECT_MISMATCH")
    successor = contract.get("successor_gate", {})
    if successor.get("issued", {}).get("scope") != "LOCAL_ONLY" or successor.get("issued", {}).get("rank_ceiling") != 49:
        errors.append("ZERO_CHARGE_LOCAL_ADMISSION_MISMATCH")
    if successor.get("global_glue") != "PROHIBITED_UNTIL_AMBIENT_SUCCESSOR_SELECTED":
        errors.append("ZERO_CHARGE_MUST_NOT_LICENSE_GLOBAL_GLUE")

    try:
        summary = narrative_summary(root, registry["artifact"])
        if summary != contract.get("decision_summary"):
            errors.append("NARRATIVE_DECISION_SUMMARY_DRIFT")
    except (KeyError, ValueError, FileNotFoundError, json.JSONDecodeError) as exc:
        errors.append(str(exc))

    review_text = (root / registry.get("hostile_review", "")).read_text(encoding="utf-8")
    for token in (
        "SELECTION_REQUIRES_OWNED_AMBIENT_WITNESS",
        "ACHIEVED_RANK_REQUIRES_CONSTRUCTION_WITNESS",
        "nonsemisimple or multi-root",
    ):
        if token not in review_text:
            errors.append("HOSTILE_CONTROL_MISSING:" + token)
    return errors


def mutation_errors(registry: dict[str, Any], mutation_id: str) -> list[str]:
    mutated = copy.deepcopy(registry)
    if mutation_id == "same_ranks_wrong_ambient_object":
        mutated["ambient_discriminator_contract"]["ambient_object"]["selection_status"] = "A3+A1"
    elif mutation_id == "ceiling_promoted_without_construction":
        row = mutated["rank_schedule"]["candidate_rows"][0]
        row["map_rank_status"] = "ACHIEVED"
        row.pop("construction_witness_ref", None)
    else:
        raise ValueError(mutation_id)
    return validate_registry(mutated)


def instances() -> list[Path]:
    paths = []
    for path in sorted((ROOT / "lab/process").glob(REGISTRY_GLOB)):
        try:
            if "ambient_discriminator_contract" in load(path):
                paths.append(path)
        except json.JSONDecodeError:
            continue
    return paths


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit", choices=("narrative",))
    args = parser.parse_args()
    paths = instances()
    assert paths, "no ambient-stratum contract instances found"
    if args.emit:
        for path in paths:
            print(json.dumps(load(path)["ambient_discriminator_contract"]["decision_summary"], indent=2))
        return 0
    total_errors: list[str] = []
    for path in paths:
        errors = validate_registry(load(path))
        print(f"{'PASS' if not errors else 'FAIL'} {path.relative_to(ROOT)}")
        total_errors.extend(f"{path.name}:{error}" for error in errors)
    assert not total_errors, "\n".join(total_errors)
    print(f"VERDICT: PASS - {len(paths)} ambient-stratum contract instance(s) close exactly.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
