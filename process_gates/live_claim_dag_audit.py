#!/usr/bin/env python3
"""Sanity-check the live claim DAG registry embedded in the Markdown ledger."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


DEFAULT_LEDGER = (
    Path(__file__).resolve().parents[1]
    / "explorations"
    / "cycle-gates-and-audits" / "live-claim-dag-fault-finality-ledger-2026-06-24.md"
)


def load_registry(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not match:
        raise ValueError(f"no fenced json registry found in {path}")
    return json.loads(match.group(1))


def audit_registry(registry: dict) -> list[str]:
    errors: list[str] = []

    status_enum = set(registry.get("status_enum", []))
    proof_grade_enum = set(registry.get("proof_grade_enum", []))
    nodes = registry.get("nodes", [])

    if not status_enum:
        errors.append("status_enum is empty")
    if not proof_grade_enum:
        errors.append("proof_grade_enum is empty")
    if not nodes:
        errors.append("nodes is empty")
        return errors

    seen: set[str] = set()
    ids: set[str] = set()
    for index, node in enumerate(nodes):
        node_id = node.get("id")
        if not isinstance(node_id, str) or not node_id:
            errors.append(f"node at index {index} has missing id")
            continue
        if node_id in seen:
            errors.append(f"duplicate node id: {node_id}")
        seen.add(node_id)
        ids.add(node_id)

    for node in nodes:
        node_id = node.get("id", "<missing>")
        status = node.get("status")
        proof_grade = node.get("proof_grade")
        deps = node.get("deps")

        if status not in status_enum:
            errors.append(f"{node_id}: invalid status {status!r}")
        if proof_grade not in proof_grade_enum:
            errors.append(f"{node_id}: invalid proof_grade {proof_grade!r}")
        if not isinstance(deps, list):
            errors.append(f"{node_id}: deps must be a list")
            continue

        for dep in deps:
            if dep == node_id:
                errors.append(f"{node_id}: self dependency")
            if dep not in ids:
                errors.append(f"{node_id}: unknown dependency {dep!r}")

    return errors


def main(argv: list[str]) -> int:
    path = Path(argv[1]) if len(argv) > 1 else DEFAULT_LEDGER
    registry = load_registry(path)
    errors = audit_registry(registry)

    if errors:
        print("live claim DAG audit: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "live claim DAG audit: PASS "
        f"({len(registry['nodes'])} nodes, "
        f"{len(registry['status_enum'])} statuses, "
        f"{len(registry['proof_grade_enum'])} proof grades)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
