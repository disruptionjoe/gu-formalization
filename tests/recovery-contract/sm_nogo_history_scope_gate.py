#!/usr/bin/env python
"""Recovery no-go Standard Model selector history/scope gate.

This gate checks the bounded history audit and Swing 1 scope result for
RECOVERY-NOGO-SM-SELECTOR. It does not move claim status, canon verdict, public
posture, or portfolio state.

Run: python tests/recovery-contract/sm_nogo_history_scope_gate.py
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
NOTE = ROOT / "explorations" / "recovery-nogo-sm-selector-history-scope-2026-07-16.md"
REGISTER = ROOT / "lab" / "process" / "recovery-no-go-defense-register.json"
SOURCE = ROOT / "explorations" / "recovery-contract-sm-selector-screen-2026-07-16.md"
SOURCE_TEST = ROOT / "tests" / "recovery-contract" / "sm_selector_screen_gate.py"

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL") + " :: " + name + (("  --  " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def log(message: str = "") -> None:
    print(message, flush=True)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def target(register: dict) -> dict:
    for item in register["targets"]:
        if item["id"] == "RECOVERY-NOGO-SM-SELECTOR":
            return item
    raise AssertionError("RECOVERY-NOGO-SM-SELECTOR missing from register")


def contains(text: str, needle: str) -> bool:
    return needle.casefold() in text.casefold()


def main() -> None:
    note = read_text(NOTE)
    source = read_text(SOURCE)
    source_test = read_text(SOURCE_TEST)
    register = load_json(REGISTER)
    item = target(register)

    log("=" * 82)
    log("C1 -- source no-go remains branch-local and status-neutral")
    log("=" * 82)
    check("C1a  source result is NO_GO", "operational_result: NO_GO" in source)
    check(
        "C1b  source no-go names selector and complete sector missing objects",
        "target-free selector" in source
        and "SU(3) x SU(2) x U(1) / Z_6" in source
        and "physical Higgs projection" in source
        and "surviving spectrum" in source,
    )
    check(
        "C1c  source gate rejects host-only recovery",
        "complete-SM recovery is NO_GO" in source_test
        and "subgroup containment alone" in source_test,
    )

    log("")
    log("=" * 82)
    log("C2 -- history audit found no prior same-construction clearance")
    log("=" * 82)
    audit = item["history_audit"]
    encounters = {enc["id"]: enc for enc in audit["prior_encounters"]}
    required_encounters = {
        "SM-FINITE-CONTROL-LEDGER",
        "TYPEII1-SELECTOR-OR-NOGO",
        "FINITE-CONTROL-PROVENANCE-AUDIT",
        "PHI-OBS-CONTRACT-GATE",
        "FIXED-DATA-PHI-OBS-SECTOR-LEDGER",
        "W222-SM-HYPERCHARGE-ANOMALY",
    }
    check("C2a  audit state is complete no-prior-clearance", audit["state"] == "COMPLETE_NO_PRIOR_CLEARANCE_FOUND")
    check("C2b  audit result is NO_PRIOR_CLEARANCE_FOUND", audit["result"] == "NO_PRIOR_CLEARANCE_FOUND")
    check("C2c  required prior encounters are recorded", required_encounters <= set(encounters))
    check(
        "C2d  none of the prior encounters clears the current obstruction",
        all(not enc["clears_current_obstruction"] for enc in encounters.values()),
    )
    check(
        "C2e  note records the same audit result",
        "Result: `NO_PRIOR_CLEARANCE_FOUND`." in note
        and "No prior result clears the full current" in note
        and "obstruction for the frozen branch" in note,
    )

    log("")
    log("=" * 82)
    log("C3 -- Swing 1 scope/fork is typed")
    log("=" * 82)
    swing = item["completed_swings"][0]
    check(
        "C3a  target moved to Swing 2 ready or later",
        item["challenge_state"]
        in {
            "SWING_2_READY",
            "SWING_3_READY",
            "BOUNDED_NO_GO",
            "CLASS_EXHAUSTED",
            "REFRAMED_SURVIVOR",
            "MORE_CONSTRUCTION_SPACE",
        },
        item["challenge_state"],
    )
    check("C3b  completed swing result is SCOPE_CONFIRMED", swing["result"] == "SCOPE_CONFIRMED")
    check("C3c  swing evidence and test point to this note and gate", swing["evidence"] == NOTE.relative_to(ROOT).as_posix() and swing["test"] == Path(__file__).relative_to(ROOT).as_posix())
    check(
        "C3d  minimized obstruction includes all selector-critical missing objects",
        "A_F" in " ".join(swing["minimized_obstruction"])
        and "SU(3) x SU(2) x U(1) / Z_6" in " ".join(swing["minimized_obstruction"])
        and "Chirality production" in " ".join(swing["minimized_obstruction"])
        and "Physical Higgs projection" in " ".join(swing["minimized_obstruction"])
        and "surviving spectrum" in " ".join(swing["minimized_obstruction"]),
    )
    check(
        "C3e  note records Layer 0 through L7 signature",
        "Layer 0 semantic alignment" in note
        and "L1 substrate" in note
        and "L7 positivity or state-space metric" in note,
    )

    log("")
    log("=" * 82)
    log("C4 -- construction-space boundaries preserve comparator discipline")
    log("=" * 82)
    statuses = {entry["construction"]: entry["status"] for entry in swing["construction_space_status"]}
    check(
        "C4a  current host branch remains scoped no-go",
        statuses.get("current GU-native Pati-Salam or Spin(10) host branch") == "SCOPE_CONFIRMED_NO_GO",
    )
    check(
        "C4b  standard finite algebra/SM structures are comparator-only",
        "standard finite algebra and Standard Model structures" in statuses
        and "comparators only" in statuses["standard finite algebra and Standard Model structures"],
    )
    check(
        "C4c  boundary-conditioned route is explicit-assumption only",
        "boundary-conditioned physical-sector selection under an explicit adapter assumption" in statuses
        and "not current-branch clearance" in statuses["boundary-conditioned physical-sector selection under an explicit adapter assumption"],
    )
    check(
        "C4d  note preserves no status movement",
        contains(note, "No claim status")
        and contains(note, "canon verdict")
        and contains(note, "public posture")
        and contains(note, "portfolio surface moves"),
    )

    log("")
    log("=" * 82)
    log("VERDICT")
    log("=" * 82)
    if not FAIL:
        log("Operational result: SCOPE_CONFIRMED for the SM selector no-go defense.")
        log("The current branch hosts relative SM-shaped evidence but lacks target-free")
        log("complete low-energy Standard Model selector recovery.")

    if FAIL:
        log(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            log("  FAIL: " + name)
        raise SystemExit(1)
    log("\nRESULT: ALL PASS")


if __name__ == "__main__":
    main()
