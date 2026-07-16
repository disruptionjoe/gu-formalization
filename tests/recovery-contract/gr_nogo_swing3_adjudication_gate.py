#!/usr/bin/env python
"""Gate for the GR W229 recovery no-go Swing 3 adjudication.

This is a process/research checkpoint, not a claim-status move. It verifies
that Swing 3 consumed the Swing 2 no-survivor result, preserved the bounded
scope, rejected target import or branch mixing, and recorded exact resurrection
triggers.

Run: python tests/recovery-contract/gr_nogo_swing3_adjudication_gate.py
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "lab" / "process" / "recovery-no-go-defense-register.json"
NOTE = ROOT / "explorations" / "recovery-nogo-gr-w229-swing3-adjudication-2026-07-16.md"
TARGET_ID = "RECOVERY-NOGO-GR-W229-VACUUM"
SWING2_ID = "SWING-2-GR-W229-CONSTRUCTION-ATTEMPT"
SWING3_ID = "SWING-3-GR-W229-ADJUDICATION"

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


def swing_from(target: dict, swing_id: str) -> dict:
    for swing in target["completed_swings"]:
        if swing["id"] == swing_id:
            return swing
    raise AssertionError(f"missing swing {swing_id}")


def has_invalid_import(checks: list[dict]) -> bool:
    return any(
        item.get("target_import_rejected") is True
        and item.get("branch_mixing_rejected") is True
        for item in checks
    )


def main() -> None:
    register = load_register()
    target = target_from(register)
    swing2 = swing_from(target, SWING2_ID)
    swing3 = swing_from(target, SWING3_ID)
    note_text = NOTE.read_text(encoding="utf-8")

    print("=" * 82)
    print("Registry and source presence")
    print("=" * 82)
    check("register exists", REGISTER.exists(), str(REGISTER))
    check("human-readable note exists", NOTE.exists(), str(NOTE))
    check("target moved to bounded no-go", target["challenge_state"] == "BOUNDED_NO_GO")
    check("source result still branch-local NO_GO", target["current_grade"] == "branch-local NO_GO")
    check("target source result exists", (ROOT / target["source_result"]).exists(), target["source_result"])

    print("")
    print("=" * 82)
    print("Prior swing consumed")
    print("=" * 82)
    check("Swing 2 remains recorded", swing2["state"] == "COMPLETE")
    check("Swing 2 result remains NO_SURVIVOR", swing2["result"] == "NO_SURVIVOR")
    check("Swing 2 evidence still exists", (ROOT / swing2["evidence"]).exists(), swing2["evidence"])

    print("")
    print("=" * 82)
    print("Swing 3 record")
    print("=" * 82)
    check("Swing 3 is recorded", swing3["state"] == "COMPLETE")
    check("Swing 3 result is BOUNDED_NO_GO", swing3["result"] == "BOUNDED_NO_GO")
    check("Swing 3 consumed Swing 2", swing3["swing_2_consumed"] is True)
    check("Swing 3 evidence path is the note", swing3["evidence"] == NOTE.relative_to(ROOT).as_posix())
    check(
        "Swing 3 test path is this script",
        swing3["test"] == "tests/recovery-contract/gr_nogo_swing3_adjudication_gate.py",
    )
    check("stop decision is explicit", swing3["stop_decision"] == "BOUNDED_NO_GO")

    checks = swing3["adversarial_checks"]
    check_ids = {item["id"] for item in checks}
    expected = {
        "W229_W203_RECORD_CURRENT",
        "FUNDAMENTAL_STIFFNESS_BARE_THETA",
        "AMBIENT_H_CLASS_BALANCE",
        "BOUNDARY_CONDITIONED_ADAPTER",
        "STANDARD_EINSTEIN_COMPARATOR",
    }
    check("all Swing 2 candidates were adjudicated", expected.issubset(check_ids))
    check("target import and branch mixing were rejected", has_invalid_import(checks))
    check("no reframe survivor is recorded", not any(item["result"] == "REFRAMED_SURVIVOR" for item in checks))

    print("")
    print("=" * 82)
    print("Resurrection trigger")
    print("=" * 82)
    triggers = swing3["resurrection_triggers"]
    rendered = " ".join(triggers)
    check("resurrection trigger names trace-free source tensor", "trace-free exact-vacuum source tensor" in rendered)
    check("resurrection trigger names higher-codimension variation", "higher-codimension" in rendered)
    check("resurrection trigger names bare-theta field equation", "bare-theta" in rendered)
    check("resurrection trigger names frozen boundary adapter", "frozen boundary-adapter return" in rendered)
    provenance_markers = ("source", "frozen", "fixed", "field equation", "provenance")
    check(
        "future reopening requires source ownership",
        all(any(marker in trigger for marker in provenance_markers) for trigger in triggers),
    )

    print("")
    print("=" * 82)
    print("Governance boundaries")
    print("=" * 82)
    unchanged = register["artifact_role"]
    check("register disclaims claim-status movement", "changes no claim status" in unchanged)
    check("note records bounded scope", "bounded defense checkpoint" in note_text)
    check("note preserves no-status-movement boundary", "change claim status" in note_text)
    check("note rejects target-shaped source", "Any future source defined as `-Q^TF(B)`" in note_text)
    check("note says paper seed none", "Paper seed proposal: none." in note_text)

    if FAIL:
        print(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            print("  FAIL: " + name)
        raise SystemExit(1)
    print("\nRESULT: ALL PASS")


if __name__ == "__main__":
    main()
