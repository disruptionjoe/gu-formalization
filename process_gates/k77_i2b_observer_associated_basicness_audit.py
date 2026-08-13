#!/usr/bin/env python3
"""Durability gate for the v0.216 observer-associated/basicness packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
required = [
    "explorations/conditional-build/conditional-physics-ledger-v0.216.md",
    "explorations/conditional-build/selected-k77-i2b-observer-associated-basicness-2026-08-12.md",
    "lab/process/conditional-physics-ledger-v0.216.json",
    "lab/process/hostile-reviews/2026-08-12-selected-k77-i2b-observer-associated-basicness-review.md",
    "lab/process/selected-k77-i2b-observer-associated-basicness.json",
    "lab/sources/selected-k77-i2b-observer-associated-basicness-source-return-2026-08-12.md",
    "tests/channel-swings/conditional_physics_ledger_v0216_probe.py",
    "tests/channel-swings/selected_k77_i2b_observer_associated_basicness_probe.py",
]
checks: list[tuple[str, bool, bool]] = []


def check(name: str, condition: bool, planted: bool = False) -> None:
    checks.append((name, bool(condition), planted))


for relative in required:
    check(f"exists:{relative}", (ROOT / relative).is_file())

registry = json.loads((ROOT / "lab/process/selected-k77-i2b-observer-associated-basicness.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.216.json").read_text())
report = (ROOT / required[1]).read_text()
review = (ROOT / required[3]).read_text()
source = (ROOT / required[5]).read_text()

check("registry_zero_failures", registry["checks"]["failures"] == 0)
check("exact_check_receipt", registry["checks"]["exact"] == 40 and registry["checks"]["planted"] == 2)
check("all_live_pairings_covered", registry["checks"]["live_pairings_covered"] == 256)
check("diagonal_naturality_exact", registry["exact_results"]["diagonal_spin_frame_naturality"] == "EXACT")
check("coarse_observation_nonselection", not registry["exact_results"]["coarse_observation_projector_selects_unit_time"])
check("vertical_basicness_refuted", not registry["exact_results"]["vertical_basicness_after_forgetting_u"])
check("full_epsilon_open", registry["exact_results"]["complete_epsilon_IG_composite_ownership"] == "OPEN")
check("dynamic_horn_open", registry["exact_results"]["source_action_dynamic_ownership"] == "OPEN")
check("observer_cost_unbooked", not registry["data_accounting"]["adopted_new_datum"] and not registry["data_accounting"]["booked_residue_change"])
check("ledger_current", ledger["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_216")
check("ledger_headline_unchanged", ledger["frontier_delta"]["headline_delta"] == "NONE")
check("report_layer0_fence", "## Layer-0 and symplectic fence" in report)
check("hostile_three_charges", all(f"Charge {index}" in review for index in (1, 2, 3)))
check("source_silent_visible", "SOURCE-SILENT" in source)
check("no_status_change", registry["claim_status_change"] == registry["canon_verdict_change"] == registry["public_posture_change"] == "NONE")
check("p1_p2_p3_unused", registry["data_accounting"]["p1_p2_p3"] == "UNCHANGED_AND_UNUSED")
check("two_halves_not_connections", "independently varied connections" in source)
check("false_involution_adjoint_rejected", "H_u^-1" in report and "manufactures a covariance failure" in report, planted=True)
check("false_coarse_selector_rejected", "selects the plane, not a future-unit vector" in report, planted=True)
check("false_basicness_rejected", "does not descend" in report, planted=True)

failed = [name for name, passed, _ in checks if not passed]
exact = sum(1 for _, _, planted in checks if not planted)
planted = sum(1 for _, _, is_planted in checks if is_planted)
print(f"CHECKS={exact} exact + {planted} planted; failures={len(failed)}")
if failed:
    print("FAILED=" + ",".join(failed))
    raise SystemExit(1)
print("RESULT=PASS")
