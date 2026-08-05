#!/usr/bin/env python3
"""Fail-closed scope audit for pre-contract Wave 0B."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = json.loads((ROOT / "lab/process/precontract-wave-0b-trace-reversal-robustness.json").read_text())
REPORT = (ROOT / "explorations/precontract-wave-0b-trace-reversal-robustness-2026-08-05.md").read_text()
SOURCE = (ROOT / "lab/sources/precontract-wave-0b-trace-fork-source-reinspection-2026-08-05.md").read_text()
REVIEW = (ROOT / "lab/process/hostile-reviews/2026-08-05-precontract-wave-0b-trace-reversal-review.md").read_text()

assert REG["layer0"]["three_way_switch"] == "REJECTED_ILL_TYPED"
assert REG["exact_results"]["ambient_to_observed_scalar_ratio"] == 26
assert REG["exact_results"]["ambient_to_observed_traceless_ricci_ratio"] == 6
assert REG["exact_results"]["scalar_adapter_exists"] is False
assert REG["source_collision"] == "SOURCE-CORRECTS"
assert REG["ambient_result"] == "DISPLAYED_FACTORIZED_AMBIENT_ANSATZ_KILL_RETAINED"
assert REG["observed_result"] == "OPEN_REQUIRES_NONSCALAR_EQUATION_RECEIVER"
assert REG["ledger_disposition"]["reason_kind"] == "SCOPE_ERROR"
assert "not prove no richer observer/vertical adapter exists" in REPORT
assert "The public 2025 conversation does not present three" in SOURCE
assert "HOSTILE POST-REVIEW: PASS AFTER REPAIR" in REVIEW
assert "observed GU gravity" in REVIEW
print("PASS: pre-contract 0B scope and revival fences retained")
