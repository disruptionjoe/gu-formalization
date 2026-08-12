#!/usr/bin/env python3
"""Durability gate for the v0.215 observer-time Hermitian-reduction packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
required = [
    "explorations/conditional-build/conditional-physics-ledger-v0.215.md",
    "explorations/conditional-build/selected-k77-i2b-observer-time-hermitian-reduction-2026-08-12.md",
    "lab/process/conditional-physics-ledger-v0.215.json",
    "lab/process/hostile-reviews/2026-08-12-selected-k77-i2b-observer-time-hermitian-reduction-review.md",
    "lab/process/selected-k77-i2b-observer-time-hermitian-reduction.json",
    "lab/sources/selected-k77-i2b-observer-time-hermitian-reduction-source-return-2026-08-12.md",
    "tests/channel-swings/conditional_physics_ledger_v0215_probe.py",
    "tests/channel-swings/selected_k77_i2b_observer_time_hermitian_reduction_probe.py",
]
checks: list[tuple[str, bool, bool]] = []


def check(name: str, condition: bool, planted: bool = False) -> None:
    checks.append((name, bool(condition), planted))


for relative in required:
    check(f"exists:{relative}", (ROOT / relative).is_file())

registry = json.loads((ROOT / "lab/process/selected-k77-i2b-observer-time-hermitian-reduction.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.215.json").read_text())
report = (ROOT / required[1]).read_text()
review = (ROOT / required[3]).read_text()
source = (ROOT / required[5]).read_text()

check("registry_zero_failures", registry["checks"] == {"exact": 47, "planted": 2, "failures": 0})
check("trace_rank_zero", registry["exact_results"]["geometry_trace_response_rank"] == 0)
check("observer_rank_four", registry["exact_results"]["observer_time_response_rank"] == 4)
check("observer_cost_unbooked", not registry["data_accounting"]["adopted_new_datum"] and not registry["data_accounting"]["booked_residue_change"])
check("ledger_current", ledger["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_215")
check("ledger_headline_unchanged", ledger["frontier_delta"]["headline_delta"] == "NONE")
check("report_layer0_fence", "## Layer-0 fence" in report)
check("report_symplectic_fence", "symplectic review" in report)
check("hostile_three_charges", all(f"Charge {index}" in review for index in (1, 2, 3)))
check("source_silent_visible", "SOURCE-SILENT" in source)
check("no_status_change", registry["claim_status_change"] == registry["canon_verdict_change"] == registry["public_posture_change"] == "NONE")
check("p1_p2_p3_unused", registry["data_accounting"]["p1_p2_p3"] == "UNCHANGED_AND_UNUSED")
check("two_halves_not_connections", "not automatically two independent connections" in source)
check("false_trace_owner_rejected", "live-response rank is zero" in report, planted=True)
check("false_positive_majorant_rejected", "positive Hilbert majorant" in report and "indefinite Hermitian" in report, planted=True)
check("false_basicness_rejected", "not proof that changing `u` is gauge" in report, planted=True)

failed = [name for name, passed, _ in checks if not passed]
exact = sum(1 for _, _, planted in checks if not planted)
planted = sum(1 for _, _, is_planted in checks if is_planted)
print(f"CHECKS={exact} exact + {planted} planted; failures={len(failed)}")
if failed:
    print("FAILED=" + ",".join(failed))
    raise SystemExit(1)
print("RESULT=PASS")
