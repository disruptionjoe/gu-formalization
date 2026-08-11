#!/usr/bin/env python3
"""Fail-closed audit for the v0.176 K77 reality/domain scope packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def strict(path: Path):
    def reject(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=reject)


registry = strict(ROOT / "lab/process/selected-k77-majorana-reality-graded-domain-scope.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.176.json")
report = (ROOT / "explorations/conditional-build/selected-k77-majorana-reality-graded-domain-scope-2026-08-11.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-11-selected-k77-majorana-reality-graded-domain-scope-review.md").read_text()

assert registry["checks"] == {"total": 35, "failures": 0}
assert registry["local_antilinear_reality"].startswith("EXISTS__")
assert registry["even_graph_import"].startswith("REJECTED_AS_CATEGORY_MISMATCH")
assert registry["graded_physical_domain"].startswith("OPEN__")
assert registry["reality_selection"].startswith("SOURCE_SILENT")
assert ledger["schema_version"] == "0.176"
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert "graded odd Green/preboundary" in report
assert "SURVIVES_WITH_SCOPE_REPAIR" in review
assert "U(32,32)" in report and "U(64,64)" in report
assert registry["p1_p2_p3_used"] is False
assert registry["verdict_change"] is False
assert registry["booked_residue_change"] is False
assert registry["quotient_change"] is False
assert registry["canon_verdict_change"] is False
assert registry["public_posture_change"] is False

print("K77_MAJORANA_REALITY_GRADED_DOMAIN_SCOPE_AUDIT_PASS")
