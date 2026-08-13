#!/usr/bin/env python3
"""Durability gate for the v0.218 constrained observer Euler/Ward result."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
required = [
    "explorations/conditional-build/conditional-physics-ledger-v0.218.md",
    "explorations/conditional-build/selected-k77-i2b-constrained-observer-euler-ward-2026-08-12.md",
    "lab/process/conditional-physics-ledger-v0.218.json",
    "lab/process/hostile-reviews/2026-08-12-selected-k77-i2b-constrained-observer-euler-ward-review.md",
    "lab/process/selected-k77-i2b-constrained-observer-euler-ward.json",
    "lab/sources/selected-k77-i2b-constrained-observer-euler-ward-source-return-2026-08-12.md",
    "tests/channel-swings/conditional_physics_ledger_v0218_probe.py",
    "tests/channel-swings/selected_k77_i2b_constrained_observer_euler_ward_probe.py",
]
checks: list[tuple[str, bool, bool]] = []


def check(name: str, condition: bool, planted: bool = False) -> None:
    checks.append((name, bool(condition), planted))


for relative in required:
    check(f"exists:{relative}", (ROOT / relative).is_file())

registry = json.loads((ROOT / "lab/process/selected-k77-i2b-constrained-observer-euler-ward.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.218.json").read_text())
report = (ROOT / required[1]).read_text()
review = (ROOT / required[3]).read_text()
source = (ROOT / required[5]).read_text()

check("registry_zero_failures", registry["checks"]["failures"] == 0)
check("exact_check_receipt", registry["checks"]["exact"] == 51 and registry["checks"]["planted"] == 3)
check("ward_coverage", registry["checks"]["ward_pairings_covered"] == 768)
check("exact_tensor", registry["finite_result"]["observer_tensor_00"] == "DIAG_MINUS_8_X4_PLUS_8_X12")
check("mixed_zero", registry["finite_result"]["observer_tensor_mixed"] == "ZERO")
check("simple_line_scoped", registry["finite_result"]["simple_line_condition"] == "A_SUM_FIRST_FOUR_SQUARES_POSITIVE")
check("flat_control", registry["finite_result"]["flat_condition"] == "A_ZERO")
check("arrow_not_selected", registry["finite_result"]["arrow_selected"] is False)
check("full_action_open", registry["ownership"]["full_sc_act_04_observer_selection"] == "OPEN")
check("ledger_current", ledger["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_218")
check("headline_unchanged", ledger["frontier_delta"]["headline_delta"] == "NONE")
check("report_layer0", "## Layer-0 and source fence" in report)
check("hostile_three_charges", all(f"Charge {index}" in review for index in (1, 2, 3)))
check("symplectic_lens", "Symplectic" in review or "symplectic" in review)
check("source_silent_visible", "SOURCE_SILENT_HU_OBSERVER_TENSOR" in source)
check("no_status_change", registry["claim_status_change"] == registry["canon_verdict_change"] == registry["public_posture_change"] == "NONE")
check("p1_p2_p3_unchanged", "P1_P2_P3" in registry["accounting"])
check("conditional_not_source_selected", "conditional observer completion" in report.lower(), planted=True)
check("negative_hessian_not_positivity", "not a positivity or stability theorem" in report, planted=True)
check("a_zero_retained", "A=0" in report or "A = 0" in report, planted=True)
check("arrow_retained_open", "no time arrow or ray" in report, planted=True)

failed = [name for name, passed, _ in checks if not passed]
exact = sum(1 for _, _, planted in checks if not planted)
planted = sum(1 for _, _, is_planted in checks if is_planted)
print(f"CHECKS={exact} exact + {planted} planted; failures={len(failed)}")
if failed:
    print("FAILED=" + ",".join(failed))
    raise SystemExit(1)
print("RESULT=PASS")
