#!/usr/bin/env python3
"""Scope audit for the selected second-layer I2B/Gauss owner-map result."""

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


registry = strict("lab/process/selected-second-layer-i2b-gauss-owner-map.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.38.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-second-layer-i2b-gauss-owner-map-2026-08-06.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-06-selected-second-layer-i2b-gauss-owner-map-review.md").read_text()
source = (ROOT / "lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md").read_text()

assert registry["status"].startswith("I2B_GAUSS_WRONG_TYPE")
assert registry["source_return"] == "SOURCE-SILENT"
assert registry["exact_result"]["full_cl2_residual_dimension"] == 1274
assert registry["exact_result"]["gauss_dimension"] == 100
assert registry["exact_result"]["gauss_orthogonal_complement_rank"] == 1174
assert registry["exact_result"]["projected_i2b_inertia"] == [54, 46, 0]
assert registry["exact_result"]["projected_full_ii_coefficient"] == "15376/13689"
assert registry["exact_result"]["projected_trace_square_coefficient"] == "-448/4563"
assert registry["exact_result"]["leakage_witness"]["coefficient"] == "2/39"

assert ledger["schema_version"] == "0.38"
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6
}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["quotients_ranked"] == 4
assert "1274-by-100" in ledger["next_work_queue"][0]["why"]
assert "other Clifford-grade" in ledger["next_work_queue"][0]["why"]

assert "Gauss-projected" in report
assert "2/39" in report
assert "1,274-by-100" in report
assert "SOURCE-SILENT" in report
assert "mandatory variational/symplectic check" in report
assert "summary outran the artifact" in review.lower()
assert "superseded or mistyped object" in review
assert "mandatory_symplectic_lens: completed" in review
assert "norm-square architecture" in source

directive = contract["active_scientific_directives"][0]
assert "FULL_1274_BY_100_RESIDUAL_TARGET" in directive["next_gate"]
assert "SOURCE-SILENT" in directive["source_return"]
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == registry["canon_verdict_change"] == registry["public_posture_change"] == "NONE"

print("SELECTED_SECOND_LAYER_I2B_GAUSS_OWNER_MAP_SCOPE_AUDIT_PASS")
