#!/usr/bin/env python3
"""Scope audit for the selected full-Cl2 residual pullback."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def strict(relative):
    path = ROOT / relative
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=hook)


registry = strict("lab/process/selected-second-layer-full-cl2-residual-pullback.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.39.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-second-layer-full-cl2-residual-pullback-2026-08-07.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-07-selected-second-layer-full-cl2-residual-pullback-review.md").read_text()
source = (ROOT / "lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md").read_text()

assert registry["status"] == "FULL_II_PLUS_TRACE__SELECTED_CL2_COMPLETE__TOTAL_RESIDUAL_OTHER_GRADES_OPEN"
assert registry["source_return"] == "SOURCE-CONFIRMS_NORM_SQUARE__SOURCE_SILENT_ON_OWNER_MAP"
exact = registry["exact_result"]
assert exact["target_shape"] == [1274, 100]
assert exact["target_rank"] == 100 and exact["nonzero_entries"] == 640
assert exact["support"] == {"H_HN": 280, "N_NN": 360}
assert exact["full_ii_coefficient"] == "15376/13689"
assert exact["trace_square_coefficient"] == "-340/4563"
assert exact["orthogonal_leakage_trace_increment"] == "4/169"
assert exact["native_inertia"] == [54, 46, 0]

assert ledger["schema_version"] == "0.39"
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["quotients_ranked"] == 4
assert "other-grade" in ledger["next_work_queue"][0]["why"]

assert "640 nonzero" in report and "-340/4563" in report
assert "stationary and quadratic" in report
assert "selected `Cl2` pullback" in review
assert "mandatory_symplectic_lens: completed" in review
assert "summary outran the artifact" in review.lower()
assert "superseded or mistyped object" in review
assert "SOURCE-DISPLAYS-BOSONIC-NORM-SQUARE" in source

directive = contract["active_scientific_directives"][0]
assert "TOTAL_RESIDUAL_OTHER_GRADE_SUPPORT" in directive["next_gate"]
assert directive["source_return"] == registry["source_return"]
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == registry["canon_verdict_change"] == registry["public_posture_change"] == "NONE"

print("SELECTED_SECOND_LAYER_FULL_CL2_RESIDUAL_PULLBACK_SCOPE_AUDIT_PASS")
