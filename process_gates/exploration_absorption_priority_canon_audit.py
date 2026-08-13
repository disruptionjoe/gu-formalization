#!/usr/bin/env python3
"""Fail-closed audit for the 2026-08-10 carrier-scope canon correction."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_unique(path: Path):
    def hook(pairs):
        out = {}
        for key, value in pairs:
            assert key not in out, f"duplicate JSON key {key!r} in {path}"
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=hook)


def require_text(path: str, needles: list[str]) -> None:
    text = (ROOT / path).read_text()
    for needle in needles:
        assert needle in text, f"missing {needle!r} in {path}"


def main() -> None:
    ledger = load_unique(ROOT / "lab/process/conditional-physics-ledger-v0.131.json")
    assert ledger["schema_version"] == "0.131"
    assert ledger["predecessor"].endswith("v0.130.json")
    assert ledger["progress"]["verdict_counts"] == {
        "SAME": 32,
        "DIFFERS": 19,
        "NEEDS": 26,
        "OVER_DETERMINED": 5,
    }
    assert ledger["residue"]["continuous_real"] == 84
    assert ledger["residue"]["function_valued_at_least"] == 19
    assert ledger["residue"]["open_discrete_forks"] == 9
    assert ledger["residue"]["quotients_ranked"] == 5
    assert len(ledger["migrations"]) == 645
    migrated = [m["row_id"] for m in ledger["migrations"] if m["to_version"] == "0.131"]
    assert migrated == ["RA-F1", "RA-F2", "RA-D2", "RA-G2", "LT-SM3", "AC-F1"]
    assert ledger["frontier_delta"] == {
        "headline_delta": "NONE",
        "conditions_closed": 0,
        "conditions_opened": 3,
        "remaining_named_conditions": 4,
    }

    require_text(
        "canon/generation-carrier-identification-scope-correction-2026-08-10.md",
        ["fixed `192`", "planted `192`", "does not show that `W` is wrong", "40", "does not establish"],
    )
    for path in [
        "canon/enum-completeness-class-c-RESULTS.md",
        "canon/antilinear-bound-RESULTS.md",
        "canon/carrier-dirac-mass-capstone-RESULTS.md",
        "canon/hessian-z3-carrier-occupancy-RESULTS.md",
        "canon/ghost-parity-krein-synthesis.md",
        "canon/six-axis-candidate-krein-positivity-dg.md",
    ]:
        require_text(path, ["CARRIER-SELECTION SCOPE CORRECTION (2026-08-10)"])

    require_text("CANON.md", ["Canon Scope Correction 2026-08-10", "non-discriminating"])
    require_text(
        "lab/process/exploration-absorption-priorities-2026-08-10.md",
        [
            "action-owned reduction plus carrier discrimination",
            "silent Hermitization",
            "Do not call the states dark matter",
            "spin-2 ghost Yukawa coefficient",
            "F_2`/UNSAT",
            "`Q(B)` is deprioritized",
        ],
    )
    require_text(
        "lab/process/hostile-reviews/2026-08-10-exploration-absorption-and-carrier-scope-review.md",
        [
            "SCOPE_CORRECTION_SURVIVES__NO_SCIENTIFIC_VERDICT_CHANGE",
            "Symplectic",
            "SURVIVES_WITH_TWO_SCOPES",
            "No additional canon promotion",
        ],
    )
    require_text(
        "attention/20260810-canon-promotion-generation-carrier-scope-correction.md",
        ["awareness notice", "case AGAINST", "Reversal"],
    )

    contract = load_unique(ROOT / "lab/process/functional-channel-operating-contract-v1.0.json")
    assert contract["standing_ledger"]["ref"].endswith("v0.131.json")
    assert "carrier_selection_directive" in contract["standing_ledger"]

    whole = "\n".join(
        (ROOT / path).read_text()
        for path in [
            "canon/generation-carrier-identification-scope-correction-2026-08-10.md",
            "lab/process/exploration-absorption-priorities-2026-08-10.md",
            "explorations/conditional-build/conditional-physics-ledger-v0.131.md",
        ]
    )
    forbidden = [
        "40 dark-matter",
        "T1-T4 are canon",
        "the 192 carrier is wrong",
        "canonical GU Fredholm operator exists",
    ]
    for phrase in forbidden:
        assert phrase not in whole, f"forbidden inflation: {phrase}"

    print("exploration absorption/canon audit: 50/50 PASS")


if __name__ == "__main__":
    main()
