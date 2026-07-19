#!/usr/bin/env python
"""Construction-space P4 QM checklist gate.

This is P4-QM-CHECKLIST from the construction-space exploration map. It checks
that the existing QM conditional-fail certificate has been converted into a
per-cell R0 checklist and that C4's boundary-adapter interface is typed without
claiming that a p2c packet exists.

Run: python tests/recovery-contract/construction_space_qm_checklist_p4.py
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MAP = ROOT / "lab" / "process" / "construction-space-map.json"
REGISTER = ROOT / "lab" / "process" / "recovery-no-go-defense-register.json"
NOTE = ROOT / "explorations" / "construction-space-qm-checklist-p4-2026-07-19.md"
QM_GATE = ROOT / "tests" / "recovery-contract" / "qm_physical_sector_conditional_gate.py"

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL") + " :: " + name + ((" -- " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def log(message: str = "") -> None:
    print(message, flush=True)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def cell(map_data: dict, cell_id: str) -> dict:
    for entry in map_data["cells"]:
        if entry["id"] == cell_id:
            return entry
    raise AssertionError(f"missing construction-space cell {cell_id}")


def stage_statuses(conditional: dict) -> dict[str, str]:
    return {stage["stage"]: stage["status"] for stage in conditional["stage_results"]}


def grades(map_data: dict) -> list[str]:
    out: list[str] = []
    for entry in map_data["cells"]:
        for track in entry["tracks"].values():
            grade = track.get("grade")
            if grade:
                out.append(grade)
    return out


def recompute_coverage(map_data: dict) -> dict[str, int]:
    all_grades = grades(map_data)
    return {
        "cells": len(map_data["cells"]),
        "track_cells": sum(len(entry["tracks"]) for entry in map_data["cells"]),
        "dispositioned_track_cells": sum(grade != "OPEN" for grade in all_grades),
        "open": sum(grade == "OPEN" for grade in all_grades),
        "gated": sum(grade == "GATED" for grade in all_grades),
        "r0_failed": sum(grade == "R0_FAIL" for grade in all_grades),
    }


def verification_flags(map_data: dict) -> list[tuple[str, str]]:
    flags: list[tuple[str, str]] = []
    for entry in map_data["cells"]:
        for track_name, track in entry["tracks"].items():
            if track.get("verification_needed") is True:
                flags.append((entry["id"], track_name))
    return flags


def main() -> None:
    map_data = load_json(MAP)
    register = load_json(REGISTER)
    conditional = register["conditional_unitarity"]
    c1 = cell(map_data, "C1-W229-RECORD-CURRENT")
    c4 = cell(map_data, "C4-BOUNDARY-ADAPTER")
    c1_qm = c1["tracks"]["QM"]
    c4_qm = c4["tracks"]["QM"]
    adapter = c4["typed_adapter_interface"]
    note = NOTE.read_text(encoding="utf-8")
    stages = stage_statuses(conditional)

    log("=" * 82)
    log("P4 source presence")
    log("=" * 82)
    check("P4 note exists", NOTE.exists(), str(NOTE))
    check("QM conditional gate exists", QM_GATE.exists(), str(QM_GATE))
    check("map evidence points to P4 note and gate", all(
        needle in c1_qm["evidence"]
        for needle in (
            "construction-space-qm-checklist-p4-2026-07-19.md",
            "construction_space_qm_checklist_p4.py",
            "qm_physical_sector_conditional_gate.py",
        )
    ))

    log("")
    log("=" * 82)
    log("C1-QM checklist conversion")
    log("=" * 82)
    check("conditional item is QM-PHYSICAL-SECTOR", conditional["id"] == "QM-PHYSICAL-SECTOR")
    check("conditional endpoint is COMPLETE_CONDITIONAL_FAIL", conditional["state"] == "COMPLETE_CONDITIONAL_FAIL")
    check("C1-QM grade is conditional hosting", c1_qm["grade"] == "R1_COND")
    check("C1-QM import count remains one", c1_qm["import_count_estimate"] == 1)
    check("C1-QM import is the typed boundary adapter axiom", c1_qm["imports"] == ["typed boundary adapter axiom"])
    check("C1-QM verification flag is cleared", c1_qm.get("verification_needed") is False)
    check("C1-QM note names all six missing certificate families", all(
        phrase in c1_qm["note"]
        for phrase in ("quotient", "state", "observable", "probability", "locality", "dynamics")
    ))

    log("")
    log("=" * 82)
    log("R0 checklist matches conditional-fail certificate")
    log("=" * 82)
    expected_stages = {
        "AdapterInterface": "ASSUMED_TYPED",
        "SourceGeometryCertificate": "PARTIAL",
        "PhysicalFieldComplexCertificate": "MISSING_SOURCE_DEFINED_QUOTIENT",
        "QFTStateSpaceExtractionCertificate": "MISSING",
        "QFTStateExtractionCertificate": "MISSING",
        "ObservableAdmissibilityCertificate": "MISSING",
        "BornProbabilityCertificate": "MISSING",
        "LocalityCausalityCertificate": "CONDITIONAL_ONLY",
        "UnitarityCertificate": "MISSING_QFT_LEVEL",
        "SpinStatisticsCertificate": "MISSING",
        "AnomalyShadowCertificate": "OPEN_RELATIVE_ONLY",
    }
    check("conditional stage statuses are unchanged", stages == expected_stages)
    check("P4 note records six R0 checklist objects", all(
        token in note
        for token in ("Q1", "Q2", "Q3", "Q4", "Q5", "Q6")
    ))
    check("P4 note preserves the geometer/native construction fork", "GU-native Krein/BRST" in note)
    check("P4 note rejects positive-Hilbert assumption shortcut", "positive Hilbert space by assumption" in note)

    log("")
    log("=" * 82)
    log("C4 adapter interface typing")
    log("=" * 82)
    check("C4-QM remains gated, not consumed", c4_qm["grade"] == "GATED")
    check("C4-QM gate stays on frozen p2c packet", "frozen p2c packet" in c4_qm["gate"])
    check("typed adapter status is gated p2c", adapter["status"] == "GATED_P2C")
    check("typed adapter source owner is p2c", adapter["source_owner"] == "possibility-to-capability")
    check("typed adapter requires independence", any("independent" in item for item in adapter["must_supply"]))
    check("typed adapter forbids GU construction", "GU-constructed adapter" in adapter["must_not_supply"])
    check("typed adapter forbids target retuning", "post-target retuning" in adapter["must_not_supply"])

    log("")
    log("=" * 82)
    log("Coverage and handoff")
    log("=" * 82)
    expected_coverage = recompute_coverage(map_data)
    actual_coverage = {key: map_data["coverage"][key] for key in expected_coverage}
    check("coverage arithmetic still matches cell ledger", actual_coverage == expected_coverage, f"{actual_coverage} vs {expected_coverage}")
    check("P4 changed no coverage counts", actual_coverage["dispositioned_track_cells"] == 12 and actual_coverage["open"] == 24)
    check("no verification flags remain after P4", verification_flags(map_data) == [])
    round_six = next((entry for entry in map_data["council_rounds"] if entry["round"] == 6), None)
    check("round 6 council is post-P4", round_six is not None and "P4 complete" in round_six["chairman_synthesis"])
    if round_six is not None:
        check("round 6 P5 is first ranked handoff", round_six["ranked_search_plan"][0]["probe"] == "P5-SOURCE-OBJECT-SPEC")
        check("round 6 P6 remains second ranked handoff", round_six["ranked_search_plan"][1]["probe"] == "P6-CONDITIONAL-INTERIOR")
    check("P4 note says no paper seed", "No paper seed is present." in note)

    if FAIL:
        log(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            log("  FAIL: " + name)
        raise SystemExit(1)
    log("\nRESULT: ALL PASS")


if __name__ == "__main__":
    main()
