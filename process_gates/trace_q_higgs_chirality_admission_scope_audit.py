#!/usr/bin/env python3
"""Fail-closed scope audit for the trace-q Higgs/chirality admission test."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]


def strict(path: Path):
    def hook(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key!r}: {path}")
            result[key] = value
        return result
    return json.loads(path.read_text(), object_pairs_hook=hook)


registry = strict(ROOT / "lab/process/trace-q-higgs-chirality-admission-test.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.18.json")
report = (ROOT / "explorations/conditional-build/trace-q-higgs-chirality-admission-test-2026-08-05.md").read_text()
report_normalized = " ".join(report.split())
review = (ROOT / "lab/process/hostile-reviews/2026-08-05-trace-q-higgs-chirality-admission-review.md").read_text()
source = (ROOT / "lab/sources/weinstein-levi-civita-contorsion-reinspection-2026-08-05.md").read_text()
carrier_readme = (ROOT / "tests/carrier-mass/README.md").read_text()

assert registry["source_return"] == "SOURCE-CORRECTS"
assert registry["finite_screen"]["k_definite_eigenspaces"] == 0
assert registry["corrected_route"]["new_external_datum"] is False
assert registry["ledger"]["row_changes"] == "NONE"
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"
assert ledger["schema_version"] == "0.18"
assert ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84
assert "not the Higgs and not a new external datum" in report_normalized
assert "summary_outruns_artifact" in review
assert "rigor_defends_superseded_or_mistyped_object" in review
assert "symplectic_reduction_veto" in review
assert "SOURCE-CORRECTS" in source
assert "trace_q_chiralizer_admission.py" in carrier_readme

print("TRACE_Q_HIGGS_CHIRALITY_ADMISSION_SCOPE_AUDIT_PASS")
