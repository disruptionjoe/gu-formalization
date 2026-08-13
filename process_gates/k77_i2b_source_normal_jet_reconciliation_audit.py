#!/usr/bin/env python3
"""Durability gate for the v0.220 source-normal-jet reconciliation."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
required = [
    "explorations/conditional-build/conditional-physics-ledger-v0.220.md",
    "explorations/conditional-build/selected-k77-i2b-source-normal-jet-reconciliation-2026-08-12.md",
    "lab/process/conditional-physics-ledger-v0.220.json",
    "lab/process/hostile-reviews/2026-08-12-selected-k77-i2b-source-normal-jet-reconciliation-review.md",
    "lab/process/selected-k77-i2b-source-normal-jet-reconciliation.json",
    "lab/evidence/predecessor-records/i2b-source-normal-jet-reconciliation.md",
    "lab/sources/selected-k77-i2b-source-normal-jet-reconciliation-source-return-2026-08-12.md",
    "tests/channel-swings/conditional_physics_ledger_v0220_probe.py",
    "tests/channel-swings/selected_k77_i2b_source_normal_jet_reconciliation_probe.py",
]
checks = []


def check(name, condition, planted=False):
    checks.append((name, bool(condition), planted))


for relative in required:
    check(f"exists:{relative}", (ROOT / relative).is_file())

registry = json.loads((ROOT / "lab/process/selected-k77-i2b-source-normal-jet-reconciliation.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.220.json").read_text())
report = (ROOT / required[1]).read_text()
review = (ROOT / required[3]).read_text()
source = (ROOT / required[6]).read_text()

check("registry_checks", registry["checks"] == {"total": 46, "planted_or_control": 4, "failures": 0})
check("operator_owned", registry["source_operator"]["normal_operator"] == "OWNED")
check("germ_real_restricted", registry["source_operator"]["normal_value"].endswith("RESTRICTED_TO_REAL_U_IMAGE"))
check("dimensions", registry["live_contact"]["response_dimension"] == 16 and registry["live_contact"]["normal_dimension"] == 10)
check("rank80_image", registry["live_contact"]["torsion_jet_rank_at_nonzero_kappa"] == 80)
check("rank80_cokernel", registry["live_contact"]["real_form_cokernel_rank"] == 80)
check("kappa_zero", registry["live_contact"]["kappa_zero_control_rank"] == 0)
check("ledger_current", ledger["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_220")
check("hostile_three_charges", all(f"Charge {index}" in review for index in (1, 2, 3)))
check("required_lenses", all(word in review for word in ("Layer-0", "prior art", "Symplectic", "analytic")))
check("source_silent", "SOURCE-SILENT" in source and "physical first normal germ" in source)
check("no_status_change", registry["claim_status_change"] == registry["canon_verdict_change"] == registry["public_posture_change"] == "NONE")
check("p1_p2_p3_unchanged", "P1_P2_P3" in registry["accounting"])
check("operator_not_value", "operator" in report.lower() and "value" in report.lower(), planted=True)
check("initial_surjectivity_refuted", "initial phrase" in review.lower() and "refuted" in review.lower(), planted=True)
check("no_80_parameters", "not booked as 80 action parameters" in report.lower(), planted=True)
check("arrow_stays_open", "time arrow" in report.lower(), planted=True)

failed = [name for name, passed, _ in checks if not passed]
exact = sum(not planted for _, _, planted in checks)
planted = sum(planted for _, _, planted in checks)
print(f"CHECKS={exact} exact + {planted} planted; failures={len(failed)}")
if failed:
    print("FAILED=" + ",".join(failed))
    raise SystemExit(1)
print("RESULT=PASS")
