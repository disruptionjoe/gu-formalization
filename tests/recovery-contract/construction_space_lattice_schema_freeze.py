#!/usr/bin/env python
"""Validate the P-LATTICE-SCHEMA-FREEZE contract.

Run: python tests/recovery-contract/construction_space_lattice_schema_freeze.py
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MAP = ROOT / "lab" / "process" / "construction-space-map.json"
PORTFOLIO = ROOT / "lab" / "process" / "research-portfolio.json"
NOTE = ROOT / "explorations" / "p-lattice-schema-freeze-2026-07-21.md"

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL") + " :: " + name + ((" -- " + detail) if detail else ""))
    if not ok:
        FAIL.append(name)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    data = load(MAP)
    portfolio = load(PORTFOLIO)
    note = NOTE.read_text(encoding="utf-8")
    schema = data["lattice_schema"]
    freeze = data["lattice_schema_freeze"]
    cells = data["cells"]
    work = {item["id"]: item for item in portfolio["work_items"]}

    axes = ["L0", "L1", "L2", "L3", "L4", "L5", "L6", "L7"]
    sides = {"program_native", "conventional", "imported", "mixed_explicit", "unknown"}
    relations = {"baseline_declared_complete", "inherited_c1", "declared_delta", "preserved_across_port", "unknown"}

    check("canonical shape is L0 plus seven axes", schema["ordered_keys"] == axes)
    check("legacy six-axis name is retained", schema["legacy_name"] == "six-axis")
    check("provenance domain is exact", set(schema["construction_side_domain"]) == sides)
    check("relation domain is exact", set(schema["relation_domain"]) == relations)
    check("every axis has a frozen class domain", all(axis in schema["axis_domains"] for axis in axes))
    check("every structural domain admits unknown", all("unknown" in schema["axis_domains"][axis] for axis in axes[1:]))
    check("Layer 0 uses semantic triage", set(schema["axis_domains"]["L0"]) == {"same_object", "homonym", "uncertain"})

    check("11 existing cells retained", len(cells) == 11, str(len(cells)))
    check("44 existing track slots retained", sum(len(cell["tracks"]) for cell in cells) == 44)
    for cell in cells:
        sig = cell.get("axis_signature", {})
        check(f"{cell['id']} total ordered signature", list(sig) == axes)
        for axis, entry in sig.items():
            check(f"{cell['id']} {axis} class in domain", entry["class_id"] in schema["axis_domains"][axis])
            check(f"{cell['id']} {axis} provenance typed", entry["construction_side"] in sides)
            check(f"{cell['id']} {axis} relation typed", entry["relation"] in relations)

    check("schema freeze recorded all 88 unresolved slots", freeze["unresolved_slots"] == 88, str(freeze["unresolved_slots"]))
    check("five compatibility rules frozen", len(schema["compatibility_constraints"]) == 5)
    check("construction side participates in tuple identity", "construction_side" in schema["tuple_canonicalization"]["identity_fields"])
    check("unknown tuples cannot generate", schema["tuple_canonicalization"]["unknown_policy"] == "non_generative_non_deduplicating")
    check("schema freeze generated no cells", freeze["generated_cells"] == 0)
    check("next probe resolves C1", freeze["next_probe"] == "P-LATTICE-SIGNATURE-RESOLUTION-C1")
    check("B5 remains parked", work["B5-MIDDLE-DIFFERENTIAL"]["state"] == "BLOCKED_SOURCE_GAP")
    check("note preserves B5 boundary", "B5-MIDDLE-SOURCE-GAP" in note)

    if FAIL:
        raise SystemExit("FAILED: " + ", ".join(FAIL))
    print("RESULT: ALL PASS")


if __name__ == "__main__":
    main()
