#!/usr/bin/env python
"""Construction-space P3 retro verification.

This is P3-RETRO-VERIFY from the construction-space exploration map. It checks
that selected retro grades are backed by existing source evidence and clears
only those verification flags:

* C1-W229-RECORD-CURRENT / SM: R1 with six typed imports.
* C1-W229-RECORD-CURRENT / COSMO: R0_FAIL against the frozen sharp list.
* C2-W203-ULTRALOCAL / GR: R0_FAIL inherited from the record-current zero-source
  exact-vacuum obstruction.

Run: python tests/recovery-contract/construction_space_retro_verify_p3.py
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MAP = ROOT / "lab" / "process" / "construction-space-map.json"
REGISTER = ROOT / "lab" / "process" / "recovery-no-go-defense-register.json"
FINGERPRINT = ROOT / "lab" / "process" / "recovery-contract-action-fingerprint-2026-07-16.json"
NOTE = ROOT / "explorations" / "construction-space-retro-verify-p3-2026-07-19.md"

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


def target(register: dict, target_id: str) -> dict:
    for entry in register["targets"]:
        if entry["id"] == target_id:
            return entry
    raise AssertionError(f"missing defense-register target {target_id}")


def swing(target_data: dict, swing_id: str) -> dict:
    for entry in target_data["completed_swings"]:
        if entry["id"] == swing_id:
            return entry
    raise AssertionError(f"missing swing {swing_id}")


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


def construction_statuses(swing_data: dict) -> dict[str, str]:
    return {
        entry["construction"]: entry["status"]
        for entry in swing_data.get("construction_space_status", [])
    }


def contains_any(text: str, needles: list[str]) -> bool:
    lower = text.casefold()
    return any(needle.casefold() in lower for needle in needles)


def main() -> None:
    map_data = load_json(MAP)
    register = load_json(REGISTER)
    fingerprint = load_json(FINGERPRINT)

    c1 = cell(map_data, "C1-W229-RECORD-CURRENT")
    c2 = cell(map_data, "C2-W203-ULTRALOCAL")
    sm_target = target(register, "RECOVERY-NOGO-SM-SELECTOR")
    cosmo_target = target(register, "RECOVERY-NOGO-COSMO-SCALAR")
    gr_target = target(register, "RECOVERY-NOGO-GR-W229-VACUUM")

    sm_track = c1["tracks"]["SM"]
    cosmo_track = c1["tracks"]["COSMO"]
    c2_gr_track = c2["tracks"]["GR"]

    log("=" * 82)
    log("P3 source presence")
    log("=" * 82)
    check("map exists", MAP.exists(), str(MAP))
    check("defense register exists", REGISTER.exists(), str(REGISTER))
    check("P3 note exists", NOTE.exists(), str(NOTE))
    check("P3 evidence paths are recorded in SM, COSMO, and C2-GR rows", all(
        "construction-space-retro-verify-p3-2026-07-19.md" in track["evidence"]
        and "construction_space_retro_verify_p3.py" in track["evidence"]
        for track in (sm_track, cosmo_track, c2_gr_track)
    ))

    log("")
    log("=" * 82)
    log("C1-SM retro R1 import count")
    log("=" * 82)
    expected_imports = [
        "breaking chain to G_SM",
        "global quotient choice",
        "absolute hypercharge normalization",
        "Higgs identification",
        "spectrum completion",
        "decoupling mechanism",
    ]
    sm_minimized = " ".join(swing(sm_target, "SWING-1-SM-SELECTOR-SCOPE-FORK")["minimized_obstruction"])
    sm_resurrection = " ".join(swing(sm_target, "SWING-3-SM-SELECTOR-ADJUDICATION")["resurrection_triggers"])
    check("C1-SM grade remains R1 hosting, not native selection", sm_track["grade"] == "R1")
    check("C1-SM import count is six", sm_track["import_count_estimate"] == 6)
    check("C1-SM imports are exactly the typed hosting imports", sm_track["imports"] == expected_imports)
    check("C1-SM verification flag is cleared", sm_track.get("verification_needed") is False)
    check("SM defense target is bounded no-go", sm_target["challenge_state"] == "BOUNDED_NO_GO")
    check("SM source record names missing selector objects", all(
        phrase in sm_minimized
        for phrase in (
            "A_F",
            "SU(3) x SU(2) x U(1) / Z_6",
            "Physical Higgs projection",
            "surviving spectrum",
        )
    ))
    check("SM resurrection triggers match the six import burden", all(
        contains_any(sm_resurrection, [needle])
        for needle in (
            "finite algebra selector",
            "global gauge quotient",
            "hypercharge normalization",
            "physical Higgs",
            "complete surviving-spectrum",
            "unwanted-mode controls",
        )
    ))

    log("")
    log("=" * 82)
    log("C1-COSMO retro R0 fail")
    log("=" * 82)
    cosmo_swing3 = swing(cosmo_target, "SWING-3-COSMO-SCALAR-ADJUDICATION")
    cosmo_triggers = " ".join(cosmo_swing3["resurrection_triggers"])
    check("C1-COSMO grade remains R0_FAIL", cosmo_track["grade"] == "R0_FAIL")
    check("C1-COSMO verification flag is cleared", cosmo_track.get("verification_needed") is False)
    check("COSMO defense target is bounded no-go", cosmo_target["challenge_state"] == "BOUNDED_NO_GO")
    check("COSMO swing 3 preserves bounded no-go", cosmo_swing3["result"] == "BOUNDED_NO_GO")
    check("COSMO missing objects match frozen sharp list", all(
        phrase in cosmo_triggers
        for phrase in (
            "physical scalar projector",
            "gauge-invariant observable map",
            "block-diagonal SVT quadratic action",
        )
    ))
    check("COSMO row note keeps status scoped to current branch", "current W229 branch" in cosmo_track["note"])

    log("")
    log("=" * 82)
    log("C2-GR inherited R0 fail")
    log("=" * 82)
    gr_swing1 = swing(gr_target, "SWING-1-GR-W229-SCOPE-FORK")
    statuses = construction_statuses(gr_swing1)
    minimized = " ".join(gr_swing1["minimized_obstruction"])
    source_law = fingerprint["source_law"]
    check("C2-GR grade remains R0_FAIL", c2_gr_track["grade"] == "R0_FAIL")
    check("C2-GR verification flag is cleared", c2_gr_track.get("verification_needed") is False)
    check("GR source law records Psi zero implies J zero", source_law["vacuum_rule"] == "Psi = 0 implies J[Psi] = 0.")
    check("GR minimized obstruction records zero source", "Psi=0 in the imported vacuum gives J=0" in minimized)
    check("Swing 1 explicitly names W203 ultralocal inheritance", statuses.get("W203 ultralocal limit") == "same zero-source obstruction unless a different non-record source is supplied")
    check("C2 row note rejects inherited rescue without new source", "same zero-source obstruction" in c2_gr_track["note"])

    log("")
    log("=" * 82)
    log("Coverage and next handoff")
    log("=" * 82)
    expected_coverage = recompute_coverage(map_data)
    actual_coverage = {key: map_data["coverage"][key] for key in expected_coverage}
    check("coverage arithmetic matches cell ledger", actual_coverage == expected_coverage, f"{actual_coverage} vs {expected_coverage}")
    fake_coverage = dict(actual_coverage)
    fake_coverage["open"] += 1
    check("coverage detector has teeth", fake_coverage != expected_coverage)
    remaining_flags = verification_flags(map_data)
    check(
        "P3 target flags are cleared; later P4 may clear the QM flag too",
        remaining_flags in ([], [("C1-W229-RECORD-CURRENT", "QM")]),
        str(remaining_flags),
    )
    round_four = next((entry for entry in map_data["council_rounds"] if entry["round"] == 4), None)
    check("round 4 council is post-P3", round_four is not None and "P3 complete" in round_four["chairman_synthesis"])
    if round_four is not None:
        check("round 4 handoff is P4", round_four["ranked_search_plan"][0]["probe"] == "P4-QM-CHECKLIST")
    final_round = map_data["council_rounds"][-1]
    check("latest council preserves P3-or-later progression", final_round["round"] >= 4)

    log("")
    log("=" * 82)
    log("Governance boundaries")
    log("=" * 82)
    note_text = NOTE.read_text(encoding="utf-8")
    check("P3 note preserves no claim movement", "claim status, canon verdicts, public posture" in note_text)
    check("P3 note says paper seed absent", "Paper seed proposal: none." in note_text)

    if FAIL:
        log(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            log("  FAIL: " + name)
        raise SystemExit(1)
    log("\nRESULT: ALL PASS")


if __name__ == "__main__":
    main()
