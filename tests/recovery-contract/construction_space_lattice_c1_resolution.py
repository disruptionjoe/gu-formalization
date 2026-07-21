"""Validate conservative C1 lattice-signature resolution.

Run: python tests/recovery-contract/construction_space_lattice_c1_resolution.py
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MAP = ROOT / "lab" / "process" / "construction-space-map.json"
PORTFOLIO = ROOT / "lab" / "process" / "research-portfolio.json"
NOTE = ROOT / "explorations" / "p-lattice-signature-resolution-c1-2026-07-21.md"

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
    resolution = data["lattice_signature_resolution_c1"]
    cells = data["cells"]
    c1 = next(cell for cell in cells if cell["id"] == "C1-W229-RECORD-CURRENT")
    work = {item["id"]: item for item in portfolio["work_items"]}

    check("C1 resolution is partial without enumeration", resolution["status"] == "COMPLETE_PARTIAL_NO_ENUMERATION")
    check("exactly one C1 slot resolved", resolution["resolved_slots"] == 1)
    check("L5 is the specific-object class", c1["axis_signature"]["L5"]["class_id"] == "a_specific_object")
    check("L5 construction side is program native", c1["axis_signature"]["L5"]["construction_side"] == "program_native")
    check("L5 carries owner evidence", len(c1["axis_signature"]["L5"].get("evidence", [])) == 2)

    expected_unknown = {"L0", "L1", "L2", "L3", "L4", "L6", "L7"}
    actual_unknown = {
        axis
        for axis, entry in c1["axis_signature"].items()
        if entry["class_id"] in {"unknown", "uncertain"}
    }
    check("seven C1 slots remain unresolved", actual_unknown == expected_unknown, str(sorted(actual_unknown)))

    unresolved = sum(
        entry["class_id"] in {"unknown", "uncertain"}
        for cell in cells
        for entry in cell["axis_signature"].values()
    )
    check("lattice has 87 unresolved slots", unresolved == 87, str(unresolved))
    check("no inheritance propagated", resolution["propagated_inheritance_slots"] == 0)
    check("no cells generated", resolution["generated_cells"] == 0)
    check("no cells graded", resolution["graded_cells"] == 0)
    check("next probe requires a C1 source packet", resolution["next_probe"] == "P-LATTICE-C1-SOURCE-PACKET")
    check("B5 remains source-blocked", work["B5-MIDDLE-DIFFERENTIAL"]["state"] == "BLOCKED_SOURCE_GAP")
    check("note preserves Krein compatibility debt", "COMP-L7-KREIN" in note)
    check("note preserves B5 boundary", "B5-MIDDLE-SOURCE-GAP" in note)

    if FAIL:
        raise SystemExit("FAILED: " + ", ".join(FAIL))
    print("RESULT: ALL PASS")


if __name__ == "__main__":
    main()
