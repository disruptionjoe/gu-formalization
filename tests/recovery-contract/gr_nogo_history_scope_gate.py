#!/usr/bin/env python
"""Gate for the GR W229 recovery no-go history audit and Swing 1 scope result.

This is a process/research checkpoint, not a claim-status move. It verifies that
the bounded history audit found no prior same-construction clearance, and that
Swing 1 records the minimized branch-local obstruction under the frozen W229
record-current source law.

Run: python tests/recovery-contract/gr_nogo_history_scope_gate.py
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "lab" / "process" / "recovery-no-go-defense-register.json"
NOTE = ROOT / "explorations" / "recovery-nogo-gr-w229-history-scope-2026-07-16.md"
TARGET_ID = "RECOVERY-NOGO-GR-W229-VACUUM"
SWING_ID = "SWING-1-GR-W229-SCOPE-FORK"

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


def same_construction_conflict(encounters: list[dict]) -> bool:
    return any(
        encounter.get("same_frozen_construction") is True
        and encounter.get("clears_current_obstruction") is True
        for encounter in encounters
    )


def has_required_construction_space(swing: dict) -> bool:
    statuses = {
        item["construction"]: item["status"]
        for item in swing.get("construction_space_status", [])
    }
    required = (
        "frozen W229 record-current nonlocal branch",
        "W203 ultralocal limit",
        "fundamental-stiffness or bare-theta branch",
        "boundary-conditioned adapter response",
        "standard Einstein dynamics",
    )
    return all(key in statuses for key in required)


def main() -> None:
    register = load_register()
    target = target_from(register)
    audit = target["history_audit"]
    encounters = audit["prior_encounters"]
    swings = target["completed_swings"]
    swing = next(s for s in swings if s["id"] == SWING_ID)

    print("=" * 82)
    print("Registry and source presence")
    print("=" * 82)
    check("register exists", REGISTER.exists(), str(REGISTER))
    check("human-readable note exists", NOTE.exists(), str(NOTE))
    check("target moved to Swing 2 ready", target["challenge_state"] == "SWING_2_READY")
    check("source result still branch-local NO_GO", target["current_grade"] == "branch-local NO_GO")
    check("target source result exists", (ROOT / target["source_result"]).exists(), target["source_result"])

    print("")
    print("=" * 82)
    print("History audit")
    print("=" * 82)
    check(
        "audit state records no prior same-construction clearance",
        audit["state"] == "COMPLETE_NO_PRIOR_CLEARANCE_FOUND",
        audit["state"],
    )
    check("audit result vocabulary is explicit", audit["result"] == "NO_PRIOR_CLEARANCE_FOUND")
    check("bounded search names searched surfaces", len(audit["search_receipt"]["searched_surfaces"]) >= 7)
    check("bounded search names mechanism terms", "Q^TF" in audit["search_receipt"]["search_terms"])

    encounter_ids = {encounter["id"] for encounter in encounters}
    check("RFAIL-03 checked", "RFAIL-03" in encounter_ids)
    check("W225 checked", "W225" in encounter_ids)
    check("W236 checked", "W236" in encounter_ids)
    check("W238 checked", "W238" in encounter_ids)
    check("W229 checked", "W229" in encounter_ids)
    check("no same-construction clearance exists in audit", not same_construction_conflict(encounters))

    fake_conflict = [
        {"same_frozen_construction": True, "clears_current_obstruction": True},
    ]
    check("conflict detector has teeth", same_construction_conflict(fake_conflict))

    print("")
    print("=" * 82)
    print("Swing 1 scope and fork")
    print("=" * 82)
    check("Swing 1 is recorded", swing["state"] == "COMPLETE")
    check("Swing 1 result is SCOPE_CONFIRMED", swing["result"] == "SCOPE_CONFIRMED")
    check("Swing 1 consumed the history audit", swing["history_audit_consumed"] is True)
    check("Swing 1 evidence path is the note", swing["evidence"] == NOTE.relative_to(ROOT).as_posix())
    check("Swing 1 test path is this script", swing["test"] == "tests/recovery-contract/gr_nogo_history_scope_gate.py")

    minimized = set(swing["minimized_obstruction"])
    check("minimized obstruction includes nonzero QTF", "principled Schwarzschild Q^TF(B) is nonzero" in minimized)
    check("minimized obstruction includes record-current source", "the W229 source law uses record current J[Psi]" in minimized)
    check("minimized obstruction includes Psi vacuum", "Psi=0 in the imported vacuum gives J=0" in minimized)
    check("minimized obstruction includes theta zero", "finite positive screened operator gives theta=0" in minimized)
    check("minimized obstruction blocks tuning", "kappa and Z_U cannot tune a zero tensor into -Q^TF(B)" in minimized)
    check("construction space includes required forks", has_required_construction_space(swing))

    fake_incomplete_swing = {"construction_space_status": [{"construction": "frozen W229 record-current nonlocal branch", "status": "x"}]}
    check("construction-space detector has teeth", not has_required_construction_space(fake_incomplete_swing))

    print("")
    print("=" * 82)
    print("Governance boundaries")
    print("=" * 82)
    unchanged = register["artifact_role"]
    check("register disclaims claim-status movement", "changes no claim status" in unchanged)
    note_text = NOTE.read_text(encoding="utf-8")
    note_text_lower = note_text.lower()
    check("note preserves branch-local scope", "branch-local exact-vacuum GR no-go" in note_text)
    check("note forbids importing Einstein dynamics", "not importable as gu dynamics" in note_text_lower)

    if FAIL:
        print(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            print("  FAIL: " + name)
        raise SystemExit(1)
    print("\nRESULT: ALL PASS")


if __name__ == "__main__":
    main()
