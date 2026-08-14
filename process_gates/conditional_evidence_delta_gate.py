#!/usr/bin/env python3
"""Validate native, versionless conditional-evidence deltas without Runtime metadata."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DELTA_DIR = ROOT / "lab/process/conditional-evidence-deltas"
INDEX_PATH = DELTA_DIR / "index.json"
SCHEMA_PATH = DELTA_DIR / "delta.schema.json"
SHA256 = re.compile(r"^[0-9a-f]{64}$")
DELTA_ID = re.compile(r"^[A-Z0-9][A-Z0-9._-]+$")
STATUSES = {"pending", "integrated", "duplicate", "deferred", "conflicting", "withdrawn"}
DISPOSITIONS = {"incorporated", "duplicate", "deferred", "conflicting"}
FORBIDDEN_KEYS = {
    "run_id",
    "lane_id",
    "schedule",
    "model",
    "effort",
    "execution_claim",
    "receipt",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def find_forbidden(value: Any, prefix: str = "$") -> list[str]:
    errors: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key in FORBIDDEN_KEYS:
                errors.append(f"{prefix}.{key}: private execution key is forbidden")
            errors.extend(find_forbidden(child, f"{prefix}.{key}"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            errors.extend(find_forbidden(child, f"{prefix}[{index}]"))
    return errors


def require_string_list(value: Any, label: str, *, nonempty: bool) -> list[str]:
    errors: list[str] = []
    if not isinstance(value, list):
        return [f"{label}: expected array"]
    if nonempty and not value:
        errors.append(f"{label}: must not be empty")
    if any(not isinstance(item, str) or not item for item in value):
        errors.append(f"{label}: entries must be nonempty strings")
    if len(value) != len(set(value)):
        errors.append(f"{label}: entries must be unique")
    return errors


def validate_delta(data: Any, path: Path) -> list[str]:
    errors: list[str] = []
    label = path.relative_to(ROOT).as_posix()
    if not isinstance(data, dict):
        return [f"{label}: expected object"]
    required = {
        "schema_version", "delta_id", "status", "base", "affected_rows",
        "result_refs", "source_disposition", "claim_ceiling", "proposed_effect",
        "conflict_keys", "integration",
    }
    missing = required - set(data)
    extra = set(data) - required
    if missing:
        errors.append(f"{label}: missing keys {sorted(missing)}")
    if extra:
        errors.append(f"{label}: unexpected keys {sorted(extra)}")
    if errors:
        return errors
    if data["schema_version"] != "1.0":
        errors.append(f"{label}: schema_version must be 1.0")
    if not isinstance(data["delta_id"], str) or not DELTA_ID.fullmatch(data["delta_id"]):
        errors.append(f"{label}: invalid delta_id")
    if data["status"] not in STATUSES:
        errors.append(f"{label}: invalid status")
    base = data["base"]
    if not isinstance(base, dict) or set(base) != {"ledger_ref", "ledger_sha256"}:
        errors.append(f"{label}: base must contain only ledger_ref and ledger_sha256")
    elif not isinstance(base["ledger_ref"], str) or not base["ledger_ref"]:
        errors.append(f"{label}: base ledger_ref must be nonempty")
    elif not isinstance(base["ledger_sha256"], str) or not SHA256.fullmatch(base["ledger_sha256"]):
        errors.append(f"{label}: base ledger_sha256 must be lowercase SHA-256")
    errors.extend(require_string_list(data["affected_rows"], f"{label}.affected_rows", nonempty=True))
    errors.extend(require_string_list(data["result_refs"], f"{label}.result_refs", nonempty=True))
    errors.extend(require_string_list(data["conflict_keys"], f"{label}.conflict_keys", nonempty=False))
    for key in ("source_disposition", "claim_ceiling"):
        if not isinstance(data[key], str) or not data[key]:
            errors.append(f"{label}.{key}: must be nonempty string")
    effect = data["proposed_effect"]
    if not isinstance(effect, dict) or set(effect) != {"summary", "requested_row_changes"}:
        errors.append(f"{label}: proposed_effect has wrong shape")
    else:
        if not isinstance(effect["summary"], str) or not effect["summary"]:
            errors.append(f"{label}: proposed_effect.summary must be nonempty")
        errors.extend(require_string_list(effect["requested_row_changes"], f"{label}.proposed_effect.requested_row_changes", nonempty=False))
    integration = data["integration"]
    if data["status"] == "pending" and integration is not None:
        errors.append(f"{label}: pending delta must have null integration")
    if data["status"] in {"integrated", "duplicate", "deferred", "conflicting"}:
        if not isinstance(integration, dict) or integration.get("disposition") not in DISPOSITIONS:
            errors.append(f"{label}: dispositioned delta needs a valid integration record")
        elif data["status"] == "integrated" and integration.get("disposition") != "incorporated":
            errors.append(f"{label}: integrated status requires incorporated disposition")
        elif data["status"] == "integrated" and not integration.get("canonical_ledger_ref"):
            errors.append(f"{label}: incorporated delta requires canonical ledger ref")
    errors.extend(f"{label}: {error}" for error in find_forbidden(data))
    return errors


def main() -> int:
    errors: list[str] = []
    load_json(SCHEMA_PATH)
    index = load_json(INDEX_PATH)
    if not isinstance(index, dict) or set(index) != {"schema_version", "integration_cursor", "deltas"}:
        errors.append("index.json: expected schema_version, integration_cursor, and deltas")
    elif index["schema_version"] != "1.0" or not isinstance(index["deltas"], list):
        errors.append("index.json: invalid schema_version or deltas")
    else:
        ids: list[str] = []
        paths: list[str] = []
        for entry in index["deltas"]:
            if not isinstance(entry, dict) or set(entry) != {"delta_id", "path", "status"}:
                errors.append("index.json: every entry needs exactly delta_id, path, status")
                continue
            ids.append(entry["delta_id"])
            paths.append(entry["path"])
            if entry["status"] not in STATUSES:
                errors.append(f"index.json: invalid status for {entry['delta_id']}")
        if len(ids) != len(set(ids)):
            errors.append("index.json: duplicate delta_id")
        if len(paths) != len(set(paths)):
            errors.append("index.json: duplicate path")

    files = sorted(path for path in DELTA_DIR.glob("*.json") if path.name not in {"index.json", "delta.schema.json"})
    by_id: dict[str, tuple[str, str]] = {}
    for path in files:
        data = load_json(path)
        errors.extend(validate_delta(data, path))
        if isinstance(data, dict) and "delta_id" in data and "status" in data:
            by_id[data["delta_id"]] = (path.relative_to(ROOT).as_posix(), data["status"])

    if isinstance(index, dict) and isinstance(index.get("deltas"), list):
        indexed = {entry["delta_id"]: (entry["path"], entry["status"]) for entry in index["deltas"] if isinstance(entry, dict) and set(entry) == {"delta_id", "path", "status"}}
        if indexed != by_id:
            errors.append("index.json: entries do not exactly match delta files")

    if errors:
        for error in errors:
            print(f"FAIL|conditional_evidence_delta|{error}")
        return 1
    print(f"PASS|conditional_evidence_delta|files={len(files)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
