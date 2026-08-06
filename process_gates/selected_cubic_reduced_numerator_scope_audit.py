#!/usr/bin/env python3
"""Fail-closed scope audit for the selected-cubic reduced-numerator wave."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]


def strict(path):
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=hook)


registry = strict(ROOT / "lab/process/selected-cubic-reduced-numerator-completion-fork.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.18.json")
report = (ROOT / "explorations/conditional-build/selected-cubic-reduced-numerator-completion-fork-2026-08-05.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-05-selected-cubic-reduced-numerator-review.md").read_text()
source = (ROOT / "lab/sources/selected-cubic-reduced-numerator-source-reinspection-2026-08-05.md").read_text()

assert registry["source_return"] == "SOURCE-SILENT"
assert registry["shell_numerators"]["selected_q0_q0_bulk_class"] == "ZERO_ON_COMPACT_CORE_FREE_SHELL"
assert registry["shell_numerators"]["selected_q0_qm_class"] == "NOT_IDENTIFIED_BY_CURRENT_INHERITED_DATA"
assert registry["symplectic_disposition"]["native_bfv_phase_space"] == "OPEN"
assert registry["symplectic_disposition"]["unrestricted_preboundary_charge"] == "OPEN"
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"
assert ledger["schema_version"] == "0.18"
assert ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84
assert "No Q1 pole, physical-sheet placement or unitarity verdict is claimed" in report
assert "summary_outruns_artifact" in review
assert "rigor_defends_superseded_or_mistyped_object" in review
assert "symplectic_reduction_veto" in review
assert "SOURCE-SILENT" in source

print("SELECTED_CUBIC_REDUCED_NUMERATOR_SCOPE_AUDIT_PASS")
