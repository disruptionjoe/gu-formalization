#!/usr/bin/env python3
"""Fail-closed wiring audit for conditional-physics ledger v0.6."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def strict(relative: str):
    path = ROOT / relative

    def pairs(items):
        keys = [key for key, _ in items]
        assert len(keys) == len(set(keys)), f"duplicate key in {path}"
        return dict(items)

    return json.loads(path.read_text(), object_pairs_hook=pairs)


ledger = strict("lab/process/conditional-physics-ledger-v0.6.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
registry = strict("lab/process/k77-epsilon-gravitational-soldering-weld.json")
lanes = (ROOT / "LANES.yaml").read_text()
view = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.6.md").read_text()
report = (ROOT / "explorations/conditional-build/k77-epsilon-gravitational-soldering-weld-2026-08-05.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-05-k77-epsilon-gravitational-soldering-weld-review.md").read_text()

rows = {row["id"]: row for row in ledger["rows"]}
active = [row for row in rows.values() if row.get("row_status") != "SUPERSEDED"]
directive = contract["active_scientific_directives"][0]

assert ledger["schema_version"] == "0.6"
assert ledger["predecessor"].endswith("conditional-physics-ledger-v0.5.json")
assert len(active) == 82 and len(rows) == 83
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6
}
assert ledger["residue"]["continuous_real"] == 83
assert ledger["residue"]["quotients_ranked"] == 1
assert "conditional local" in ledger["residue"]["quotients_ranked_scope"]
assert rows["LT-GR2c"]["verdict"] == "NEEDS"
assert rows["LT-GR2c"]["reason_kind"] == "MISSING_CONSTRUCTION"
assert "SIGMA_RANK10" in rows["LT-GR2c"]["mapping_grade"]
assert "SAME_STRATUM_ORTHOGONAL_WELD_EXACT" in rows["LT-GR2c"]["mapping_grade"]
assert "BULK_DEFECT_NORMALIZATION" in rows["LT-GR2c"]["mapping_grade"]

assert contract["standing_ledger"]["ref"].endswith("v0.6.json")
assert contract["standing_ledger"]["human_ref"].endswith("v0.6.md")
assert "conditional-physics-ledger-v0.6.json" in lanes
assert directive["source_return"] == "SOURCE-SILENT"
assert directive["next_gate"] == "CONSTRUCT_GLOBAL_FULL_EPSILON_IG_REDUCTION_OR_OBSTRUCTION_AND_TYPED_BULK_DEFECT_SUPPORT_NORMALIZATION__THEN_ASSEMBLE_NONLINEAR_EVEN_BV_AND_NULL_GREEN_DOMAIN"

assert registry["receiver"]["rank_on_grade1_carrier"] == 10
assert registry["projector"]["projector_rank"] == 10
assert registry["projector"]["right_inverse_exact"] is True
assert registry["projector"]["isometry_exact"] is True
assert registry["projector"]["projector_idempotent"] is True
assert registry["projector"]["projector_self_adjoint"] is True
assert registry["equivariance_boundary"]["independent_lorentz_equivariant_sym2_bilinear_maps_lower_bound"] == 5
assert registry["action_weld"]["old_receiver_reconstruction"] == "EXACT"
assert registry["action_weld"]["bulk_defect_support"] == "OPEN"
assert registry["ward_bv"]["nonlinear_CME"] == "OPEN"
assert registry["source_return"] == "SOURCE-SILENT"
assert registry["residue"]["P1_P2_P3"] == "UNCHANGED_UNUSED"

assert "itself is one line" in report
assert "same-stratum" in report
assert "SOURCE-SILENT" in report
assert "summary outruns the artifact" in review
assert "superseded object" in review
assert "action and support hostile review" in review
assert "82/82" in view and "K77 sigma_epsilon: rank 10" in view

print("PASS: v0.6 wires the exact K77 rank-ten receiver and same-stratum orthogonal weld to the global-reduction/bulk-defect/BV/domain gate without booking physical recovery")
