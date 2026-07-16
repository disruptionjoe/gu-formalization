#!/usr/bin/env python
"""Gate for the GR W229 recovery no-go Swing 2 construction attempt.

This is a process/research checkpoint, not a claim-status move. It verifies
that Swing 2 attempted a genuinely different construction family and rejected
target-shaped or branch-mixed cancellations as non-survivors.

Run: python tests/recovery-contract/gr_nogo_swing2_construction_gate.py
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "lab" / "process" / "recovery-no-go-defense-register.json"
NOTE = ROOT / "explorations" / "recovery-nogo-gr-w229-swing2-construction-2026-07-16.md"
TARGET_ID = "RECOVERY-NOGO-GR-W229-VACUUM"
SWING_ID = "SWING-2-GR-W229-CONSTRUCTION-ATTEMPT"

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


def trace_free_eta(matrix: sp.Matrix) -> bool:
    eta = sp.diag(-1, 1, 1, 1)
    return sp.simplify(sum(eta[i, i] * matrix[i, i] for i in range(4))) == 0


def any_nonzero(matrix: sp.Matrix) -> bool:
    return any(sp.simplify(matrix[i, j]) != 0 for i in range(matrix.rows) for j in range(matrix.cols))


def all_zero(matrix: sp.Matrix) -> bool:
    return not any_nonzero(matrix)


def qtf_probe() -> sp.Matrix:
    # Eta-trace-free stand-in for the already computed nonzero Schwarzschild Q^TF(B).
    return sp.diag(3, 1, 1, 1)


def mathematically_cancels(source: sp.Matrix, residual: sp.Matrix) -> bool:
    return all_zero(source + residual)


def admissible_survivor(candidate: dict) -> bool:
    required = {
        "source_owned": True,
        "benchmark_independent": True,
        "trace_free_slot": True,
        "branch_clean": True,
        "has_first_falsification_test": True,
    }
    return all(candidate.get(key) == value for key, value in required.items())


def main() -> None:
    register = load_register()
    target = target_from(register)
    swing = swing_from(target)
    note_text = NOTE.read_text(encoding="utf-8")

    print("=" * 82)
    print("Registry and source presence")
    print("=" * 82)
    check("register exists", REGISTER.exists(), str(REGISTER))
    check("human-readable note exists", NOTE.exists(), str(NOTE))
    check(
        "target reached Swing 3 or later",
        target["challenge_state"]
        in {
            "SWING_3_READY",
            "BOUNDED_NO_GO",
            "CLASS_EXHAUSTED",
            "REFRAMED_SURVIVOR",
            "MORE_CONSTRUCTION_SPACE",
        },
        target["challenge_state"],
    )
    check("source result still branch-local NO_GO", target["current_grade"] == "branch-local NO_GO")
    check("target source result exists", (ROOT / target["source_result"]).exists(), target["source_result"])

    print("")
    print("=" * 82)
    print("Swing 2 record")
    print("=" * 82)
    check("Swing 2 is recorded", swing["state"] == "COMPLETE")
    check("Swing 2 result is NO_SURVIVOR", swing["result"] == "NO_SURVIVOR")
    check("Swing 2 evidence path is the note", swing["evidence"] == NOTE.relative_to(ROOT).as_posix())
    check(
        "Swing 2 test path is this script",
        swing["test"] == "tests/recovery-contract/gr_nogo_swing2_construction_gate.py",
    )
    check("Swing 2 consumed Swing 1 scope", swing["swing_1_scope_consumed"] is True)

    attempted = swing["attempted_constructions"]
    attempted_ids = {item["id"] for item in attempted}
    required_ids = {
        "W203_ULTRALOCAL_LIMIT",
        "FUNDAMENTAL_STIFFNESS_BARE_THETA",
        "AMBIENT_H_CLASS_BALANCE",
        "BOUNDARY_CONDITIONED_ADAPTER",
        "STANDARD_EINSTEIN_COMPARATOR",
    }
    check("all predeclared construction families were classified", required_ids.issubset(attempted_ids))
    check("no actual register candidate is admitted", not any(admissible_survivor(item) for item in attempted))
    check(
        "standard Einstein comparator is rejected as target import",
        any(item["id"] == "STANDARD_EINSTEIN_COMPARATOR" and item["result"] == "INVALID_ESCAPE" for item in attempted),
    )

    print("")
    print("=" * 82)
    print("Cancellation and admissibility detectors")
    print("=" * 82)
    qtf = qtf_probe()
    target_shaped = -qtf
    wrong_shape = sp.eye(4)
    zero_source = sp.zeros(4, 4)
    check("probe residual is nonzero", any_nonzero(qtf))
    check("probe residual is eta-trace-free", trace_free_eta(qtf))
    check("target-shaped source would algebraically cancel", mathematically_cancels(target_shaped, qtf))
    check("metric-proportional source does not cancel", not mathematically_cancels(wrong_shape, qtf))
    check("zero source does not cancel", not mathematically_cancels(zero_source, qtf))

    fake_real_survivor = {
        "source_owned": True,
        "benchmark_independent": True,
        "trace_free_slot": True,
        "branch_clean": True,
        "has_first_falsification_test": True,
    }
    fake_target_import = fake_real_survivor | {"benchmark_independent": False}
    check("admissibility detector accepts a fully sourced fake survivor", admissible_survivor(fake_real_survivor))
    check("admissibility detector rejects target-shaped import", not admissible_survivor(fake_target_import))

    print("")
    print("=" * 82)
    print("Governance boundaries")
    print("=" * 82)
    unchanged = register["artifact_role"]
    check("register disclaims claim-status movement", "changes no claim status" in unchanged)
    check("note records branch-local scope", "branch-local W229 exact-vacuum no-go" in note_text)
    check("note rejects target-shaped source", "target-shaped `S = -Q^TF(B)`" in note_text)
    check("note preserves no-status-movement boundary", "changes no claim status or verdict" in note_text)

    if FAIL:
        print(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            print("  FAIL: " + name)
        raise SystemExit(1)
    print("\nRESULT: ALL PASS")


if __name__ == "__main__":
    main()
