#!/usr/bin/env python3
"""Fail-closed scope audit for the selected grade-one Schur gate."""

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


registry = strict(ROOT / "lab/process/selected-action-grade1-dbt-schur-observation.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.36.json")
report = (ROOT / "explorations/conditional-build/selected-action-grade1-dbt-schur-observation-2026-08-06.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-06-selected-action-grade1-dbt-schur-observation-review.md").read_text()

assert registry["status"] == "EXACT_GRADE1_AUXILIARY_COMPLETION__GENERIC_NULL_POLARIZATIONS_LIFTED__DISCRETE_CAUSAL_CANDIDATE_LOCUS_OPEN"
assert registry["source_return"] == "SOURCE-CONFIRMS_AND_SOURCE-SILENT"
exact = registry["exact_result"]
assert exact["grade1_hessian"]["rank"] == 196
assert exact["grade1_hessian"]["inertia_positive_kappa"] == [97, 99, 0]
assert exact["formal_dbt_euler_ranks"] == {"timelike": 12, "spacelike": 12, "null": 11}
assert exact["full_cross_ranks"] == {"timelike": 13, "spacelike": 15, "null": 15}
assert exact["schur_ranks"] == {"timelike": 13, "spacelike": 15, "null": 14}
assert all(packet["kernel"].startswith("GAUGE4") for packet in exact["normalized_kappa_squared_one"].values())
assert exact["observation"]["paired_receiver"].startswith("PRESERVES_COMPLETE_FULL_CROSS")
assert exact["null_factors"]["N2_extra_kernel_dimension"] == 2
assert exact["null_factors"]["gcd_with_all_nonnul_factors"] == 1
assert "physical graviton identification remains open" in exact["causal_candidate"]
assert registry["ledger_effect"]["verdict_change"] == "LT-GR1 SAME/DERIVED_CONDITIONAL -> NEEDS/MISSING_CONSTRUCTION"
assert registry["free_object_delta"] == 0 and registry["quotient_count_delta"] == 0
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert ledger["schema_version"] == "0.36"
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84 and ledger["residue"]["quotients_ranked"] == 4
assert "The first exploratory calculation Schur-complemented only" in review
assert "superseded" in review.lower()
assert "Mandatory symplectic review" in review
assert "unique two-mode" in report
assert "not the original graph TT plane" in report
assert "No BV/symplectic quotient" in report
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == registry["canon_verdict_change"] == registry["public_posture_change"] == "NONE"

print("SELECTED_ACTION_GRADE1_DBT_SCHUR_OBSERVATION_SCOPE_AUDIT_PASS")
