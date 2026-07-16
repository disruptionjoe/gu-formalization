#!/usr/bin/env python
"""Gate for Standard Model selector no-go Swing 2 construction attempts.

This is a process/research checkpoint, not a claim-status move. It verifies
that Swing 2 tested genuinely different selector constructions and rejected
host-only evidence, target import, and assumption-only escapes.

Run: python tests/recovery-contract/sm_nogo_swing2_construction_gate.py
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "lab" / "process" / "recovery-no-go-defense-register.json"
NOTE = ROOT / "explorations" / "recovery-nogo-sm-selector-swing2-construction-2026-07-16.md"
TARGET_ID = "RECOVERY-NOGO-SM-SELECTOR"
SWING_ID = "SWING-2-SM-SELECTOR-CONSTRUCTION-ATTEMPT"

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


def complete_selector(candidate: dict) -> bool:
    required_true = (
        "source_owned",
        "target_free",
        "finite_algebra_selector",
        "gauge_quotient_selector",
        "absolute_hypercharge_selector",
        "chirality_production",
        "physical_higgs_projection",
        "spectrum_closure",
        "unwanted_mode_decoupling",
        "has_first_falsification_test",
    )
    return all(candidate.get(key) is True for key in required_true)


def invalid_survivors(swing: dict) -> list[str]:
    problems: list[str] = []
    for attempt in swing.get("attempted_constructions", []):
        if attempt["result"] == "SURVIVOR_CANDIDATE" and not complete_selector(attempt):
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
    check("target reached Swing 3 ready", target["challenge_state"] == "SWING_3_READY", target["challenge_state"])
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
    check("Swing 2 test path is this script", swing["test"] == "tests/recovery-contract/sm_nogo_swing2_construction_gate.py")

    required = {
        "CURRENT_HOST_BRANCH",
        "GAUGE_QUOTIENT_OBSERVER_SELECTOR",
        "SYMMETRY_BREAKING_CHIRALITY",
        "BOUNDARY_CONDITIONED_PHYSICAL_SECTOR",
        "STANDARD_SM_COMPARATOR",
    }
    check("required construction attempts are present", required.issubset(attempts))
    check("every attempt has a first falsification test", first_tests_present(swing))
    check("no incomplete selector is admitted as a survivor", invalid_survivors(swing) == [])

    current = attempts["CURRENT_HOST_BRANCH"]
    quotient = attempts["GAUGE_QUOTIENT_OBSERVER_SELECTOR"]
    breaking = attempts["SYMMETRY_BREAKING_CHIRALITY"]
    boundary = attempts["BOUNDARY_CONDITIONED_PHYSICAL_SECTOR"]
    comparator = attempts["STANDARD_SM_COMPARATOR"]

    check("current host branch is rejected as incomplete selector", current["result"] == "NO_SURVIVOR")
    check("current host branch lacks finite algebra selector", current["finite_algebra_selector"] is False)
    check("quotient route is target-free but not currently source-owned", quotient["target_free"] is True and quotient["source_owned"] is False)
    check("quotient route lacks global gauge quotient selector", quotient["gauge_quotient_selector"] is False)
    check("symmetry-breaking route lacks chirality production", breaking["chirality_production"] is False)
    check("symmetry-breaking route lacks Higgs and spectrum closure", breaking["physical_higgs_projection"] is False and breaking["spectrum_closure"] is False)
    check("boundary route depends on absent adapter", boundary["adapter_dependency"] == "absent frozen adapter packet")
    check("standard SM comparator is invalid escape", comparator["result"] == "INVALID_ESCAPE")
    check("standard SM comparator rejects target import", comparator["target_import_rejected"] is True)

    fake_complete = {
        "source_owned": True,
        "target_free": True,
        "finite_algebra_selector": True,
        "gauge_quotient_selector": True,
        "absolute_hypercharge_selector": True,
        "chirality_production": True,
        "physical_higgs_projection": True,
        "spectrum_closure": True,
        "unwanted_mode_decoupling": True,
        "has_first_falsification_test": True,
    }
    fake_host_only = fake_complete | {"finite_algebra_selector": False}
    check("selector detector accepts a fully sourced fake selector", complete_selector(fake_complete))
    check("selector detector rejects host-only evidence", not complete_selector(fake_host_only))

    print("")
    print("=" * 82)
    print("Governance boundaries")
    print("=" * 82)
    check("register disclaims claim-status movement", "changes no claim status" in register["artifact_role"])
    note_text = NOTE.read_text(encoding="utf-8")
    note_lower = note_text.lower()
    check("note records no-survivor result", "operational result: `no_survivor`" in note_lower)
    check("note rejects standard finite-algebra import", "standard finite-algebra route is the comparator" in note_lower)
    check("note preserves no status movement", "claim status" in note_lower and "public posture" in note_lower)
    check("note says paper seed is absent", "Paper seed proposal: none." in note_text)

    if FAIL:
        print(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            print("  FAIL: " + name)
        raise SystemExit(1)
    print("\nRESULT: ALL PASS")


if __name__ == "__main__":
    main()
