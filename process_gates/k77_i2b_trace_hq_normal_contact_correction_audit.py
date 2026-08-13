#!/usr/bin/env python3
"""Durability gate for the v0.221 trace-Hq contact correction."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
required = [
    "explorations/conditional-build/conditional-physics-ledger-v0.221.md",
    "explorations/conditional-build/selected-k77-i2b-trace-hq-normal-contact-correction-2026-08-12.md",
    "lab/process/conditional-physics-ledger-v0.221.json",
    "lab/process/hostile-reviews/2026-08-12-selected-k77-i2b-trace-hq-normal-contact-correction-review.md",
    "lab/process/selected-k77-i2b-trace-hq-normal-contact-correction.json",
    "lab/evidence/predecessor-records/i2b-trace-hq-normal-contact-correction.md",
    "lab/sources/selected-k77-i2b-trace-hq-normal-contact-correction-source-return-2026-08-12.md",
    "tests/channel-swings/conditional_physics_ledger_v0221_probe.py",
    "tests/channel-swings/selected_k77_i2b_trace_hq_normal_contact_correction_probe.py",
]
checks = []


def check(name, condition, planted=False):
    checks.append((name, bool(condition), planted))


for relative in required:
    check(f"exists:{relative}", (ROOT / relative).is_file())

registry = json.loads((ROOT / required[4]).read_text())
ledger = json.loads((ROOT / required[2]).read_text())
report = (ROOT / required[1]).read_text()
review = (ROOT / required[3]).read_text()
source = (ROOT / required[6]).read_text()

check("registry_checks", registry["checks"] == {"total": 46, "planted_or_control": 5, "failures": 0})
check("carrier_halves", registry["carrier"]["primary"].startswith("C32_32_PLUS"))
check("block_subgroup", registry["carrier"]["block_subgroup"] == "U32_32_X_U32_32")
check("h_homonym", "HMINUS_EQUALS_X_OF_SPLUS" in registry["carrier"]["h_homonym"])
check("rank_comparison", registry["real_form_comparison"] == {"b_skew_rank_per_normal": 8, "observer_hu_rank_per_normal": 10, "trace_hq_rank_per_normal": 12})
check("rank120_image", registry["live_contact"]["trace_hq_rank"] == 120)
check("rank40_cokernel", registry["live_contact"]["cokernel_rank"] == 40)
check("full_closure_refuted", registry["live_contact"]["full_stabilizer_closure"].startswith("REFUTED"))
check("ledger_current", ledger["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_221")
check("hostile_three_charges", all(f"Charge {index}" in review for index in (1, 2, 3)))
check("required_lenses", all(word in review for word in ("Layer-0", "prior art", "Symplectic", "analytic")))
check("source_silent", "SOURCE-SILENT" in source and "D_varpi H_q" in source)
check("no_status_change", registry["claim_status_change"] == registry["canon_verdict_change"] == registry["public_posture_change"] == "NONE")
check("p1_p2_p3_unchanged", "P1_P2_P3" in registry["accounting"])
check("operator_not_value", "on-shell value" in report.lower(), planted=True)
check("no_global_module", "not yet a global associated" in report.lower(), planted=True)
check("no_120_parameters", "not booked as a coupling" in report.lower(), planted=True)
check("two_halves_not_groups", "not the primary carrier statement" in report.lower(), planted=True)

failed = [name for name, passed, _ in checks if not passed]
exact = sum(not planted for _, _, planted in checks)
planted = sum(planted for _, _, planted in checks)
print(f"CHECKS={exact} exact + {planted} planted; failures={len(failed)}")
if failed:
    print("FAILED=" + ",".join(failed))
    raise SystemExit(1)
print("RESULT=PASS")
