#!/usr/bin/env python3
"""Fail-closed surface audit for the v0.197 trace-radial gate."""

from __future__ import annotations

import ast
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
required = [
    "explorations/conditional-build/selected-k77-varpi-radial-half-exchange-gate-2026-08-12.md",
    "explorations/conditional-build/conditional-physics-ledger-v0.197.md",
    "lab/process/conditional-physics-ledger-v0.197.json",
    "lab/process/selected-k77-varpi-radial-half-exchange-gate.json",
    "lab/process/hostile-reviews/2026-08-12-selected-k77-varpi-radial-half-exchange-review.md",
    "lab/sources/selected-k77-varpi-radial-half-exchange-source-return-2026-08-12.md",
    "tests/channel-swings/selected_k77_varpi_radial_half_exchange_probe.py",
    "tests/channel-swings/conditional_physics_ledger_v0197_probe.py",
]
for relative in required:
    assert (ROOT / relative).is_file(), relative

for relative in (
    "lab/process/conditional-physics-ledger-v0.197.json",
    "lab/process/selected-k77-varpi-radial-half-exchange-gate.json",
):
    json.loads((ROOT / relative).read_text(encoding="utf-8"))

for relative in (
    "tests/channel-swings/selected_k77_varpi_radial_half_exchange_probe.py",
    "tests/channel-swings/conditional_physics_ledger_v0197_probe.py",
):
    ast.parse((ROOT / relative).read_text(encoding="utf-8"), filename=relative)

exploration = (ROOT / required[0]).read_text(encoding="utf-8")
review = (ROOT / required[4]).read_text(encoding="utf-8")
source = (ROOT / required[5]).read_text(encoding="utf-8")
assert "target_claim: NONE-NOT-A-KILL" in exploration
assert "half-exchanging component" in exploration
assert "isolated self-wedge vanishes" in exploration
assert "Charge 1" in review and "Charge 2" in review and "Charge 3" in review
assert "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source
assert "SC-GRP-01" in source and "SC-FER-03" in source
print("PASS: v0.197 trace-radial gate surfaces, source polarity and hostile fences are complete.")

