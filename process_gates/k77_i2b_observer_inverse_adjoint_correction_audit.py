#!/usr/bin/env python3
"""Durability gate for the v0.217 observer inverse-adjoint correction."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
required = [
    "explorations/conditional-build/conditional-physics-ledger-v0.217.md",
    "explorations/conditional-build/selected-k77-i2b-observer-inverse-adjoint-correction-2026-08-12.md",
    "lab/process/conditional-physics-ledger-v0.217.json",
    "lab/process/hostile-reviews/2026-08-12-selected-k77-i2b-observer-inverse-adjoint-correction-review.md",
    "lab/process/selected-k77-i2b-observer-inverse-adjoint-correction.json",
    "lab/sources/selected-k77-i2b-observer-inverse-adjoint-correction-source-return-2026-08-12.md",
    "tests/channel-swings/conditional_physics_ledger_v0217_probe.py",
    "tests/channel-swings/selected_k77_i2b_observer_inverse_adjoint_correction_probe.py",
]
checks: list[tuple[str, bool, bool]] = []


def check(name: str, condition: bool, planted: bool = False) -> None:
    checks.append((name, bool(condition), planted))


for relative in required:
    check(f"exists:{relative}", (ROOT / relative).is_file())

registry = json.loads((ROOT / "lab/process/selected-k77-i2b-observer-inverse-adjoint-correction.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.217.json").read_text())
report = (ROOT / required[1]).read_text()
review = (ROOT / required[3]).read_text()
source = (ROOT / required[5]).read_text()

check("registry_zero_failures", registry["checks"]["failures"] == 0)
check("exact_check_receipt", registry["checks"]["exact"] == 17 and registry["checks"]["planted"] == 1)
check("correct_block_order", registry["correction"]["correct_fixed_field_blocks"] == ["-328/9 I4", "+8 I4", "+8 I4", "+8 I4"])
check("correct_inverse_adjoint", registry["correction"]["correct_adjoint"] == "H_U_INVERSE_A_DAGGER_H_U")
check("naturality_survives", registry["surviving_result"]["diagonal_spin_frame_naturality"] == "EXACT")
check("basicness_still_refuted", registry["surviving_result"]["vertical_basicness"] == "REFUTED_WITH_CORRECT_INVERSE_ADJOINT")
check("rb4_already_built", registry["prior_art"]["rb4_moving_u_so3"] == "ALREADY_CONSTRUCTED")
check("rb5_coarse_flag_refuted", registry["prior_art"]["rb5_coarse_epsilon_flag"] == "REFUTED")
check("current_action_untested", registry["prior_art"]["current_sc_act_04_u_euler"] == "UNTESTED")
check("ledger_current", ledger["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_217")
check("headline_unchanged", ledger["frontier_delta"]["headline_delta"] == "NONE")
check("report_layer0_symplectic", "## Layer-0 and symplectic fence" in report)
check("hostile_three_charges", all(f"Charge {index}" in review for index in (1, 2, 3)))
check("source_silent_visible", "SOURCE-SILENT" in source)
check("no_status_change", registry["claim_status_change"] == registry["canon_verdict_change"] == registry["public_posture_change"] == "NONE")
check("p1_p2_p3_unchanged", "P1_P2_P3" in registry["accounting"])
check("old_blocks_named_as_wrong", "old v0.215/v0.216 control" in report, planted=True)
check("duplicate_successor_rejected", "duplicate work" in report, planted=True)
check("no_euler_inflation", "not an Euler equation" in report, planted=True)

failed = [name for name, passed, _ in checks if not passed]
exact = sum(1 for _, _, planted in checks if not planted)
planted = sum(1 for _, _, is_planted in checks if is_planted)
print(f"CHECKS={exact} exact + {planted} planted; failures={len(failed)}")
if failed:
    print("FAILED=" + ",".join(failed))
    raise SystemExit(1)
print("RESULT=PASS")
