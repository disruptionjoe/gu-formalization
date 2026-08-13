#!/usr/bin/env python3
"""Durability gate for the v0.219 full-contact identifiability result."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
required = [
    "explorations/conditional-build/conditional-physics-ledger-v0.219.md",
    "explorations/conditional-build/selected-k77-i2b-full-contact-identifiability-2026-08-12.md",
    "lab/process/conditional-physics-ledger-v0.219.json",
    "lab/process/hostile-reviews/2026-08-12-selected-k77-i2b-full-contact-identifiability-review.md",
    "lab/process/selected-k77-i2b-full-contact-identifiability.json",
    "lab/sources/selected-k77-i2b-full-contact-identifiability-source-return-2026-08-12.md",
    "tests/channel-swings/conditional_physics_ledger_v0219_probe.py",
    "tests/channel-swings/selected_k77_i2b_full_contact_identifiability_probe.py",
]
checks = []


def check(name, condition, planted=False):
    checks.append((name, bool(condition), planted))


for relative in required:
    check(f"exists:{relative}", (ROOT / relative).is_file())

registry = json.loads((ROOT / "lab/process/selected-k77-i2b-full-contact-identifiability.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.219.json").read_text())
report = (ROOT / required[1]).read_text()
review = (ROOT / required[3]).read_text()
source = (ROOT / required[5]).read_text()

check("registry_checks", registry["checks"] == {"total": 45, "planted": 3, "failures": 0})
check("normal_jet_unbuilt", registry["owned_contact"]["ambient_first_normal_jet"] == "UNBUILT_AND_SOURCE_SILENT")
check("paired_data_identical", registry["paired_completions"]["restricted_data"] == "IDENTICAL")
check("three_outcomes", set(registry["paired_completions"]["outcomes"]) == {"PRESERVE_A_POSITIVE", "DESTROY_TO_A_ZERO", "CREATE_FROM_A_ZERO"})
check("discriminant", registry["discriminant"] == "(a0+q*s)^2+a1^2+a2^2+a3^2=0")
check("route_live", registry["verdict"].endswith("OBSERVER_PATH_REMAINS_LIVE"))
check("ledger_current", ledger["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_219")
check("hostile_three_charges", all(f"Charge {index}" in review for index in (1, 2, 3)))
check("required_lenses", all(word in review for word in ("Layer-0", "Prior art", "Symplectic", "Analytic")))
check("source_silent", "SOURCE_SILENT_AMBIENT_FIRST_NORMAL_JET" in source)
check("no_status_change", registry["claim_status_change"] == registry["canon_verdict_change"] == registry["public_posture_change"] == "NONE")
check("p1_p2_p3_unchanged", "P1_P2_P3" in registry["accounting"])
check("countermodels_not_candidates", "countermodels" in source, planted=True)
check("not_full_contact_answer", "identifiability theorem" in report, planted=True)
check("no_fitted_q", "do not fit" in report.lower(), planted=True)
check("arrow_stays_open", "not a time arrow" in report, planted=True)

failed = [name for name, passed, _ in checks if not passed]
exact = sum(not planted for _, _, planted in checks)
planted = sum(planted for _, _, planted in checks)
print(f"CHECKS={exact} exact + {planted} planted; failures={len(failed)}")
if failed:
    print("FAILED=" + ",".join(failed))
    raise SystemExit(1)
print("RESULT=PASS")
