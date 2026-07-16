#!/usr/bin/env python
"""Gate for cosmology recovery no-go Swing 2 construction attempts.

This is a process/research checkpoint, not a claim-status move. It verifies that
the Swing 2 record tested genuinely different construction classes and rejected
scalar-by-rename, target-SVT import, and assumption-only escapes.

Run: python tests/recovery-contract/cosmo_nogo_swing2_construction_gate.py
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "lab" / "process" / "recovery-no-go-defense-register.json"
NOTE = ROOT / "explorations" / "recovery-nogo-cosmo-scalar-swing2-construction-2026-07-16.md"
TARGET_ID = "RECOVERY-NOGO-COSMO-SCALAR"
SWING_ID = "SWING-2-COSMO-SCALAR-CONSTRUCTION-ATTEMPT"

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL") + " :: " + name + (("  --  " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def load_register() -> dict:
    return json.loads(REGISTER.read_text(encoding="utf-8"))


def target_from(register: dict) -> dict:
    for target in register["targets"]:
        if target["id"] == TARGET_ID:
            return target
    raise AssertionError(f"missing target {TARGET_ID}")


def swing_from(target: dict) -> dict:
    for swing in target["completed_swings"]:
        if swing["id"] == SWING_ID:
            return swing
    raise AssertionError(f"missing swing {SWING_ID}")


def attempts_by_id(swing: dict) -> dict[str, dict]:
    return {attempt["id"]: attempt for attempt in swing.get("attempted_constructions", [])}


def has_required_attempts(swing: dict) -> bool:
    required = {
        "CONSTRAINED_COMPOSITE_SCALAR",
        "MIXED_SECTOR_SCALAR",
        "BOUNDARY_CONDITIONED_SCALAR",
        "STANDARD_SVT_COMPARATOR",
    }
    return required.issubset(attempts_by_id(swing))


def invalid_source_owned_survivors(swing: dict) -> list[str]:
    problems: list[str] = []
    for attempt in swing.get("attempted_constructions", []):
        if attempt["result"] == "SURVIVOR_CANDIDATE" and not attempt.get("source_owned"):
            problems.append(attempt["id"])
    return problems


def first_tests_present(swing: dict) -> bool:
    return all(bool(attempt.get("first_falsification_test")) for attempt in swing.get("attempted_constructions", []))


def main() -> None:
    register = load_register()
    target = target_from(register)
    swing = swing_from(target)
    attempts = attempts_by_id(swing)

    print("=" * 82)
    print("Registry and source presence")
    print("=" * 82)
    check("register exists", REGISTER.exists(), str(REGISTER))
    check("human-readable note exists", NOTE.exists(), str(NOTE))
    check("target moved to Swing 3 ready", target["challenge_state"] == "SWING_3_READY")
    check("source result still branch-local NO_GO", target["current_grade"] == "branch-local NO_GO")
    check("target source result exists", (ROOT / target["source_result"]).exists(), target["source_result"])

    print("")
    print("=" * 82)
    print("Swing 2 construction attempt")
    print("=" * 82)
    check("Swing 2 is recorded", swing["state"] == "COMPLETE")
    check("Swing 2 result is NO_SURVIVOR", swing["result"] == "NO_SURVIVOR")
    check("Swing 2 consumed Swing 1 scope", swing["swing_1_scope_consumed"] is True)
    check("Swing 2 evidence path is the note", swing["evidence"] == NOTE.relative_to(ROOT).as_posix())
    check("Swing 2 test path is this script", swing["test"] == "tests/recovery-contract/cosmo_nogo_swing2_construction_gate.py")
    check("required construction attempts are present", has_required_attempts(swing))
    check("every attempt has a first falsification test", first_tests_present(swing))
    check("no non-source-owned survivor is admitted", invalid_source_owned_survivors(swing) == [])

    composite = attempts["CONSTRAINED_COMPOSITE_SCALAR"]
    mixed = attempts["MIXED_SECTOR_SCALAR"]
    boundary = attempts["BOUNDARY_CONDITIONED_SCALAR"]
    svt = attempts["STANDARD_SVT_COMPARATOR"]

    check("composite scalar is rejected for missing emitted scalar data", composite["result"] == "NO_SURVIVOR")
    check("composite scalar is not source-owned", composite["source_owned"] is False)
    check("composite scalar lacks closed truncation", composite["closed_truncation"] is False)
    check("mixed-sector scalar is rejected for residue accounting", mixed["result"] == "NO_SURVIVOR")
    check("mixed-sector scalar lacks residue discharge", mixed["residue_discharge"] is False)
    check("boundary scalar depends on absent adapter", boundary["result"] == "NO_SURVIVOR")
    check("boundary scalar names adapter dependency", boundary["adapter_dependency"] == "absent frozen adapter packet")
    check("standard SVT is invalid escape", svt["result"] == "INVALID_ESCAPE")
    check("standard SVT is target import", svt["target_import_rejected"] is True)

    fake_swing = {
        "attempted_constructions": [
            {"id": "X", "result": "SURVIVOR_CANDIDATE", "source_owned": False, "first_falsification_test": "x"}
        ]
    }
    check("survivor-source detector has teeth", invalid_source_owned_survivors(fake_swing) == ["X"])

    print("")
    print("=" * 82)
    print("Governance boundaries")
    print("=" * 82)
    check("register disclaims claim-status movement", "changes no claim status" in register["artifact_role"])
    note_text = NOTE.read_text(encoding="utf-8")
    note_text_lower = note_text.lower()
    check("note preserves no status movement", "claim-status move" in note_text_lower)
    check("note rejects standard SVT import", "standard-svt route is a comparator" in note_text_lower)
    check("note says paper seed is absent", "Paper seed proposal: none." in note_text)

    if FAIL:
        print(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            print("  FAIL: " + name)
        raise SystemExit(1)
    print("\nRESULT: ALL PASS")


if __name__ == "__main__":
    main()
