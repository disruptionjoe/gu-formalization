#!/usr/bin/env python3
"""Scope and wiring audit for the GCR Clifford-grade owner retype."""

from pathlib import Path
import json

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot


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


registry = strict("lab/process/selected-second-layer-gcr-exterior-degree-owner-retype.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.49.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-second-layer-gcr-exterior-degree-owner-retype-2026-08-07.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-07-selected-second-layer-gcr-exterior-degree-owner-retype-review.md").read_text(encoding="utf-8")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text(encoding="utf-8")
next_steps = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8")
status = (ROOT / "RESEARCH-STATUS.md").read_text(encoding="utf-8")
lanes = (ROOT / "lab/process/RESEARCH-AGENDA.json").read_text(encoding="utf-8")

assert registry["status"] == "GCR_WRONG_CLIFFORD_GRADE_AND_DIRECT_INPUT_TYPE__ODD_TORSION_TRANSLATION_CURVATURE_OR_SOLDERING_OWNER_REQUIRED"
assert registry["rerun"] == "41/41 PASS"
assert registry["source_return"] == "SOURCE-CONFIRMS__GAUSS_COMPATIBLE_TWO_CONNECTION_ARENA__SOURCE_SILENT__K77_GCR_TO_ODD_CURVATURE_OWNER_MAP"
assert registry["layer0"]["classical_gcr_curvature"] == "Lambda2(T*Y) tensor Cl2"
assert registry["layer0"]["v048_inverse_packet"] == "Lambda2(T*Y) tensor Cl1"

exact = registry["exact_result"]
assert exact["cl2_source_basis_columns"] == exact["nonzero_cl2_selected_columns"] == 8281
assert exact["cl2_selected_output_grades"] == [1, 5]
assert exact["cl2_to_required_grade2_entries"] == 0
assert exact["cl1_selected_map_dimension"] == exact["cl1_selected_map_rank"] == 1274
assert exact["v048_total_inverse_support"] == 145
assert exact["v048_connection_support"] + exact["v048_transverse_support"] == 145
assert exact["direct_hh_exterior_support"] == 0
assert exact["q_contraction_image_rank"] == 13
assert exact["required_cliff_q_supports"] == [7, 7, 7, 7]
assert exact["single_q_adapter"] == "EXCLUDED"

assert ledger["schema_version"] == "0.49"
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["function_valued_at_least"] == 19
assert ledger["residue"]["open_discrete_forks"] == 9
assert ledger["residue"]["quotients_ranked"] == 4
assert ledger["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3, "conditions_opened": 1, "remaining_named_conditions": 5}
assert ledger["next_work_queue"][0]["rank"] == 1
assert "odd augmented-torsion/translation-curvature" in ledger["next_work_queue"][0]["why"]

assert reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.49.json"
)

for token in ("8,281", "grades one or five", "rank-1,274", "28 + 117", "rank thirteen", "SOURCE-SILENT", "P1/P2/P3 remain"):
    assert token in report
for lens in ("Differential geometry", "Representation theory", "Variational PDE", "Symplectic geometry", "Krein/operator theory", "Source criticism", "Repo archaeology"):
    assert lens in review
for fence in ("not directly", "type analogy only", "No Euler equation", "no third lane"):
    assert fence in report
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane_gate"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == registry["canon_verdict_change"] == registry["public_posture_change"] == "none"

print("PASS: historical v0.49 GCR owner-retype certificate is immutable and reachable from the current append-only ledger without residue, quotient, datum, canon or posture inflation")
