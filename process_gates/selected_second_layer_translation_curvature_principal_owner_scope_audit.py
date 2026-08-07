#!/usr/bin/env python3
"""Scope and wiring audit for fixed-B translation-curvature partial ownership."""

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

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


registry = strict("lab/process/selected-second-layer-translation-curvature-principal-owner.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.51.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-second-layer-translation-curvature-principal-owner-2026-08-07.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-07-selected-second-layer-translation-curvature-principal-owner-review.md").read_text(encoding="utf-8")
context = (ROOT / "lab/process/agent-context-pack.md").read_text(encoding="utf-8")
next_steps = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8")
status = (ROOT / "RESEARCH-STATUS.md").read_text(encoding="utf-8")
lanes = (ROOT / "LANES.yaml").read_text(encoding="utf-8")

assert registry["status"] == "FIXED_B_TRANSLATION_CURVATURE_PARTIAL_OWNER_EXACT__TRANSVERSE_MOVING_SOLDERING_OWNER_OPEN"
assert registry["rerun"] == "45/45 PASS"
assert registry["exact_result"]["q_wedge_full_image_dimension"] == 182
assert registry["exact_result"]["q_wedge_selected_hn_nn_coordinates"] == 140
assert registry["exact_result"]["fixed_b_owned_support"] == 28
assert registry["exact_result"]["transverse_unowned_support"] == 117
assert registry["exact_result"]["owned_family_rank"] == registry["exact_result"]["transverse_family_rank"] == 4
assert registry["exact_result"]["fixed_b_disposition"] == "PARTIAL_OWNER"
assert registry["exact_result"]["t_wedge_t_differential_order"] == 0
assert registry["exact_result"]["t_wedge_t_variation_clifford_parity"] == "EVEN"

assert ledger["schema_version"] == "0.51"
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["function_valued_at_least"] == 19
assert ledger["residue"]["open_discrete_forks"] == 9
assert ledger["residue"]["quotients_ranked"] == 4
assert ledger["next_work_queue"][0]["rank"] == 1
assert "117-coefficient transverse" in ledger["next_work_queue"][0]["why"]

assert tuple(map(int, contract["standing_ledger"]["ref"].removesuffix(".json").rsplit("v", 1)[1].split("."))) >= (0, 51)
directive = contract["active_scientific_directives"][0]
assert "FIXED_B_DB_T_SUPPORT28_PARTIAL_OWNER_EXACT" in directive["status"]
assert directive["next_run_method"]["target"] == "ACTUAL_RAW_UPSILON_NORMAL_JET_ON_FOUR_GRAPH_COLUMNS_OR_SOURCE_OWNED_NONZERO_STATIONARY_BACKGROUND"
assert "CONSTRUCT_ACTUAL_RAW_UPSILON_NORMAL_JET_OR_SOURCE_OWNED_NONZERO_BACKGROUND" in directive["next_gate"]
assert "SYMPLECTIC_GEOMETRY" in directive["next_run_method"]["mandatory_reviews"]

for token in ("rank `182`", "`140`", "= 28", "= 117", "partial owner", "SOURCE-SILENT", "P1/P2/P3 remain"):
    assert token in report
for lens in ("Source geometry", "Differential geometry", "Representation theory", "Variational PDE", "Symplectic geometry", "Krein/operator theory", "Source criticism", "Repo archaeology"):
    assert lens in review
for token in ("Fixed-`B` `D_B T` owns the 28", "Ledger v0.52"):
    assert token in context
assert "FIXED-B TRANSLATION-CURVATURE PARTIAL OWNER" in next_steps
assert "ledger v0.51" in status
assert "conditional-physics-ledger-v0.52.json" in lanes
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane_gate"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == registry["canon_verdict_change"] == registry["public_posture_change"] == "none"

print("PASS: fixed-B D_B T owns exactly support 28, the successor retypes support 117 beyond the residual-zero connection class, and ledger/contract wiring forbids Euler, quotient, datum, canon or posture inflation")
