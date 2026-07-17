#!/usr/bin/env python
"""Gate for the Standard Model selector no-go Swing 3 adjudication.

This is a process/research checkpoint, not a claim-status move. It verifies
that Swing 3 consumed the Swing 2 no-survivor result, preserved bounded scope,
rejected host-only relabeling, target import, branch mixing, and absent-adapter
escapes, and recorded exact resurrection triggers.

Run: python tests/recovery-contract/sm_nogo_swing3_adjudication_gate.py
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "lab" / "process" / "recovery-no-go-defense-register.json"
NOTE = ROOT / "explorations" / "recovery-nogo-sm-selector-swing3-adjudication-2026-07-17.md"
TARGET_ID = "RECOVERY-NOGO-SM-SELECTOR"
SWING2_ID = "SWING-2-SM-SELECTOR-CONSTRUCTION-ATTEMPT"
SWING3_ID = "SWING-3-SM-SELECTOR-ADJUDICATION"

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


def checks_by_id(swing: dict) -> dict[str, dict]:
    return {item["id"]: item for item in swing.get("adversarial_checks", [])}


def all_imports_rejected(checks: list[dict]) -> bool:
    return all(
        item.get("target_import_rejected") is True
        and item.get("branch_mixing_rejected") is True
        for item in checks
    )


def has_required_checks(swing: dict) -> bool:
    expected = {
        "CURRENT_HOST_BRANCH",
        "GAUGE_QUOTIENT_OBSERVER_SELECTOR",
        "SYMMETRY_BREAKING_CHIRALITY",
        "BOUNDARY_CONDITIONED_PHYSICAL_SECTOR",
        "STANDARD_SM_COMPARATOR",
    }
    return expected.issubset(checks_by_id(swing))


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
        swing3["test"] == "tests/recovery-contract/sm_nogo_swing3_adjudication_gate.py",
    )
    check("stop decision is explicit", swing3["stop_decision"] == "BOUNDED_NO_GO")
    check("construction space is bounded", swing3["construction_space_bounded"] is True)

    checks = swing3["adversarial_checks"]
    by_id = checks_by_id(swing3)
    check("all Swing 2 candidates were adjudicated", has_required_checks(swing3))
    check("target import and branch mixing were rejected", all_imports_rejected(checks))
    check("host-only relabeling is rejected", by_id["CURRENT_HOST_BRANCH"]["host_only_relabeling_rejected"] is True)
    check("quotient route still lacks source selector", by_id["GAUGE_QUOTIENT_OBSERVER_SELECTOR"]["source_selector_absent"] is True)
    check("chirality route rejects granted chiral shadow", by_id["SYMMETRY_BREAKING_CHIRALITY"]["granted_chiral_shadow_rejected"] is True)
    check(
        "boundary route records absent adapter",
        by_id["BOUNDARY_CONDITIONED_PHYSICAL_SECTOR"]["adapter_dependency"] == "absent frozen adapter packet",
    )
    check("standard SM remains invalid escape", by_id["STANDARD_SM_COMPARATOR"]["result"] == "INVALID_ESCAPE_PRESERVED")
    check("no reframe survivor is recorded", not any(item["result"] == "REFRAMED_SURVIVOR" for item in checks))

    fake_swing = {
        "adversarial_checks": [
            {"id": "X", "target_import_rejected": True, "branch_mixing_rejected": False}
        ]
    }
    check("target-import detector has teeth", not all_imports_rejected(fake_swing["adversarial_checks"]))

    print("")
    print("=" * 82)
    print("Resurrection trigger")
    print("=" * 82)
    triggers = swing3["resurrection_triggers"]
    rendered = " ".join(triggers)
    check("resurrection trigger names finite algebra selector", "finite algebra selector" in rendered)
    check("resurrection trigger names global gauge quotient", "global gauge quotient" in rendered)
    check("resurrection trigger names chirality production", "chirality-production" in rendered)
    check("resurrection trigger names frozen boundary adapter", "frozen boundary-adapter return" in rendered)
    check("resurrection trigger names surviving spectrum theorem", "complete surviving-spectrum theorem" in rendered)
    provenance_markers = ("source-owned", "frozen", "provenance", "emitted", "fixed")
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
    check("note rejects standard finite algebra import", "standard finite algebra" in note_text and "invalid escape" in note_text)
    check("note says paper seed none", "Paper seed proposal: none." in note_text)

    if FAIL:
        print(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            print("  FAIL: " + name)
        raise SystemExit(1)
    print("\nRESULT: ALL PASS")


if __name__ == "__main__":
    main()
