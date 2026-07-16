#!/usr/bin/env python
"""Gate for the cosmology recovery no-go history audit and Swing 1 scope result.

This is a process/research checkpoint, not a claim-status move. It verifies that
the bounded history audit found no prior same-construction clearance, and that
Swing 1 records the minimized branch-local obstruction under the frozen
W203/W229/W230/W236 record-current source-action fingerprint.

Run: python tests/recovery-contract/cosmo_nogo_history_scope_gate.py
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "lab" / "process" / "recovery-no-go-defense-register.json"
NOTE = ROOT / "explorations" / "recovery-nogo-cosmo-scalar-history-scope-2026-07-16.md"
TARGET_ID = "RECOVERY-NOGO-COSMO-SCALAR"
SWING_ID = "SWING-1-COSMO-SCALAR-SCOPE-FORK"

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
        "current s*(theta) FLRW decomposition",
        "gauge-invariant or constrained composite scalar from frozen GU fields",
        "scalar induced by mixing among already-present GU sectors",
        "boundary-conditioned scalar channel under an explicit adapter assumption",
        "standard cosmological SVT variables",
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
    check(
        "target reached or passed Swing 2 ready",
        target["challenge_state"] in {"SWING_2_READY", "SWING_3_READY", "BOUNDED_NO_GO"},
        target["challenge_state"],
    )
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
    check("bounded search names scalar-truncation terms", "scalar-truncation" in audit["search_receipt"]["search_terms"])
    check("bounded search names SVT terms", "SVT" in audit["search_receipt"]["search_terms"])

    encounter_ids = {encounter["id"] for encounter in encounters}
    check("theta canon checked", "THETA-FLRW-CANON" in encounter_ids)
    check("source-forced theta packet checked", "SOURCE-FORCED-THETA-COEFF" in encounter_ids)
    check("theta terrain audit checked", "THETA-RESIDUAL-TERRAIN" in encounter_ids)
    check("H44 background evidence checked", "H44-BACKREACTED-BACKGROUND" in encounter_ids)
    check("W129 distance likelihood evidence checked", "W129-M2-BAND-SWEEP" in encounter_ids)
    check("same-branch fingerprint checked", "RECOVERY-ACTION-FINGERPRINT" in encounter_ids)
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
    check("Swing 1 test path is this script", swing["test"] == "tests/recovery-contract/cosmo_nogo_history_scope_gate.py")

    minimized = set(swing["minimized_obstruction"])
    check("minimized obstruction includes typed theta candidate", "branch has a typed theta / connection-distortion candidate" in minimized)
    check("minimized obstruction includes scalar assumption", "existing KG and distance results use a homogeneous scalar amplitude" in minimized)
    check("minimized obstruction includes field-type failure mode", "canon flags scalar field type as a failure mode" in minimized)
    check("minimized obstruction includes missing scalar projector", "no physical scalar projector for s*(theta)" in minimized)
    check("minimized obstruction includes missing observable map", "no gauge-invariant observable map is frozen" in minimized)
    check("minimized obstruction includes missing SVT action", "no block-diagonal SVT quadratic action is supplied" in minimized)
    check("minimized obstruction includes residue/truncation failure", "non-scalar source, gauge, boundary, vector, tensor, and connection residues are not discharged" in minimized)
    check("construction space includes required forks", has_required_construction_space(swing))

    fake_incomplete_swing = {"construction_space_status": [{"construction": "current s*(theta) FLRW decomposition", "status": "x"}]}
    check("construction-space detector has teeth", not has_required_construction_space(fake_incomplete_swing))

    print("")
    print("=" * 82)
    print("Governance boundaries")
    print("=" * 82)
    unchanged = register["artifact_role"]
    check("register disclaims claim-status movement", "changes no claim status" in unchanged)
    note_text = NOTE.read_text(encoding="utf-8")
    note_text_lower = note_text.lower()
    check("note preserves branch-local scope", "branch-local cosmological perturbation no-go" in note_text)
    check("note forbids importing standard SVT as GU dynamics", "not importable as gu dynamics" in note_text_lower)
    check("note says paper seed is absent", "Paper seed proposal: none." in note_text)

    if FAIL:
        print(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            print("  FAIL: " + name)
        raise SystemExit(1)
    print("\nRESULT: ALL PASS")


if __name__ == "__main__":
    main()
