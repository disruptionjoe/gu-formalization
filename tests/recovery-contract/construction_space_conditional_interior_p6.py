#!/usr/bin/env python
"""Construction-space P6 conditional interior gate.

This is P6-CONDITIONAL-INTERIOR from the construction-space exploration map. It
checks that conditional grades consume the frozen P5 source-object interface as
one typed import, keep C4 gated until an actual p2c packet exists, and hand off
to a shared-normalization ledger without moving claim status.

Run: python tests/recovery-contract/construction_space_conditional_interior_p6.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MAP = ROOT / "lab" / "process" / "construction-space-map.json"
CONTRACT = ROOT / "lab" / "process" / "source-object-interface-contract.md"
NOTE = ROOT / "explorations" / "construction-space-conditional-interior-p6-2026-07-19.md"

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL") + " :: " + name + ((" -- " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def log(message: str = "") -> None:
    print(message, flush=True)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_contract() -> dict:
    text = CONTRACT.read_text(encoding="utf-8")
    match = re.search(
        r"## Machine-Readable Contract\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing Machine-Readable Contract JSON block")
    return json.loads(match.group(1))


def cell(map_data: dict, cell_id: str) -> dict:
    for entry in map_data["cells"]:
        if entry["id"] == cell_id:
            return entry
    raise AssertionError(f"missing construction-space cell {cell_id}")


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
        "conditional": sum(grade in {"R0_COND", "R1_COND"} for grade in grades),
    }


def p6_track(map_data: dict, cell_id: str, track_name: str) -> dict:
    return cell(map_data, cell_id)["tracks"][track_name]


def latest_council(map_data: dict) -> dict:
    return map_data["council_rounds"][-1]


def main() -> None:
    map_data = load_json(MAP)
    contract = load_contract()
    note = NOTE.read_text(encoding="utf-8")

    log("=" * 82)
    log("P6 source presence")
    log("=" * 82)
    check("P6 note exists", NOTE.exists(), str(NOTE))
    check("P6 map block is complete", map_data["conditional_interior_probe"]["status"] == "complete")
    check("P6 map block names this probe", map_data["conditional_interior_probe"]["probe"] == "P6-CONDITIONAL-INTERIOR")
    check("P6 map block points to note and test", all(
        needle in map_data["conditional_interior_probe"]["evidence"] + " " + map_data["conditional_interior_probe"]["test"]
        for needle in (
            "construction-space-conditional-interior-p6-2026-07-19.md",
            "construction_space_conditional_interior_p6.py",
        )
    ))

    log("")
    log("=" * 82)
    log("Conditional grades")
    log("=" * 82)
    expected = {
        ("C9-AMBIENT-H-CLASS", "GR"),
        ("C6-SOURCE-OWNED-BREAKING", "SM"),
        ("C7-COMPOSITE-SCALAR", "COSMO"),
        ("C8-MIXED-SECTOR-SCALAR", "COSMO"),
    }
    for cell_id, track_name in sorted(expected):
        track = p6_track(map_data, cell_id, track_name)
        with_label = f"{cell_id}/{track_name}"
        check(f"{with_label} is R0_COND", track["grade"] == "R0_COND")
        check(f"{with_label} has one shared typed import", track["import_count_estimate"] == 1)
        check(f"{with_label} imports frozen shared interface", track["imports"] == ["frozen shared source-object interface"])
        check(f"{with_label} verification flag cleared", track.get("verification_needed") is False)
        check(f"{with_label} points to P6 evidence", "construction-space-conditional-interior-p6-2026-07-19.md" in track["evidence"])
        check(f"{with_label} preserves no-instance gate", "No concrete source instance exists" in track["note"] or "no concrete source instance exists" in track["note"])

    c4 = cell(map_data, "C4-BOUNDARY-ADAPTER")
    check("C4 remains gated on actual p2c packet", all(
        track["grade"] == "GATED" for track in c4["tracks"].values()
    ))
    check("C1-QM conditional hosting remains intact", p6_track(map_data, "C1-W229-RECORD-CURRENT", "QM")["grade"] == "R1_COND")

    log("")
    log("=" * 82)
    log("Shared corridor")
    log("=" * 82)
    corridor = map_data["conditional_interior_probe"]["conditional_corridors"][0]
    check("corridor id is stable", corridor["id"] == "P6-CORRIDOR-A")
    check("corridor is not an instance", corridor["status"] == "CONDITIONAL_NOT_INSTANCE")
    check("corridor minimum grade is R0_COND", corridor["minimum_grade"] == "R0_COND")
    check("corridor uses one shared import", corridor["shared_import_count"] == 1)
    check("corridor names all four legs", set(corridor["legs"]) == {"GR", "QM", "COSMO", "SM"})
    check("contract still requires one source object", "one_source_object_across_GR_QM_COSMO_SM" in contract["source_requirements"]["sharedness"])
    check("note rejects per-sector repairs", "Per-sector repairs are a failure mode" in note)

    log("")
    log("=" * 82)
    log("Coverage and handoff")
    log("=" * 82)
    expected_coverage = recompute_coverage(map_data)
    actual_coverage = {key: map_data["coverage"][key] for key in expected_coverage}
    check("coverage arithmetic matches cell ledger", actual_coverage == expected_coverage, f"{actual_coverage} vs {expected_coverage}")
    check("P6 adds three new dispositions and one gate-to-conditional regrade", actual_coverage["dispositioned_track_cells"] == 15 and actual_coverage["open"] == 21 and actual_coverage["conditional"] == 5)
    final_round = latest_council(map_data)
    check("latest council is post-P6", final_round["round"] == 8 and "P6 complete" in final_round["chairman_synthesis"])
    check("P7 is next ranked handoff", final_round["ranked_search_plan"][0]["probe"] == "P7-SHARED-NORMALIZATION-LEDGER")

    log("")
    log("=" * 82)
    log("Boundary discipline")
    log("=" * 82)
    for phrase in [
        "No claim status",
        "canon verdict",
        "public posture",
        "external action",
    ]:
        check(f"P6 note states boundary: {phrase}", phrase in note)
    check("source contract remains frozen spec, not instance", contract["status"] == "FROZEN_SPEC_NO_INSTANCE")
    check("integration still needs concrete instance", "concrete p2c instance is required" in contract["integration_rule"])

    if FAIL:
        log(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            log("  FAIL: " + name)
        raise SystemExit(1)
    log("\nRESULT: ALL PASS")


if __name__ == "__main__":
    main()
