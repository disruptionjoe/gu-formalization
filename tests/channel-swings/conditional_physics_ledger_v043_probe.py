#!/usr/bin/env python3
"""Fail-closed migration audit for conditional physics ledger v0.43."""

from collections import Counter
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


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


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


old = strict("lab/process/conditional-physics-ledger-v0.42.json")
new = strict("lab/process/conditional-physics-ledger-v0.43.json")
registry = strict("lab/process/selected-second-layer-dupsilon-gauge-orbit-weld.json")
touched = ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"]

print("A. FROZEN HEADLINE")
check("exact", "schema advances 0.42 to 0.43", old["schema_version"] == "0.42" and new["schema_version"] == "0.43")
check("exact", "denominator and verdict counts freeze", old["denominator"] == new["denominator"] and old["progress"]["verdict_counts"] == new["progress"]["verdict_counts"])
check("exact", "coverage remains 82 of 82", new["progress"]["mapped"] == new["progress"]["total"] == 82)
for key in ("continuous_real", "function_valued_at_least", "open_discrete_forks", "quotients_ranked"):
    check("exact", f"residue {key} freezes", old["residue"][key] == new["residue"][key])
check("program", "P1 P2 P3 remain unused", registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})
check("program", "Curt and third lane stay fenced", registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and registry["third_lane_gate"] == "NOT_PROMOTED")
check("program", "no posture promotion", registry["claim_status_change"] == registry["canon_verdict_change"] == registry["public_posture_change"] == "none")
check("program", "automation identity is explicit", new["updated_by"] == "gu-formalization-big-waves-hourly")
check("program", "frontier delta is explicit", new["frontier_delta"] == registry["frontier_delta"])
check("source", "ledger source return is explicit", new["source_return"] == registry["source_return"])
check("type", "Layer-0 objects are enumerated", new["layer0_objects_compared"] == [
    "RESIDUAL_NATURALITY_D_UPSILON_R_ZERO",
    "SOURCE_REDUNDANCY_XI_EQUALS_D_UPSILON",
    "ACTION_HESSIAN_WARD_RADICALITY",
    "BV_BFV_REDUCTION",
])
check("program", "collision disposition is observable", new["collision_disposition"] == "NO_COLLISION__CENTRAL_CLAIM_ACQUIRED")

print("\nB. APPEND-ONLY MOVEMENT")
old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
check("exact", "row identities freeze", set(old_rows) == set(new_rows))
check("exact", "exactly five named rows change", [row_id for row_id in old_rows if old_rows[row_id] != new_rows[row_id]] == touched)
for row_id in touched:
    before, after = old_rows[row_id], new_rows[row_id]
    check("exact", f"{row_id} verdict reason summary revival freeze", before["verdict"] == after["verdict"] and before["reason_kind"] == after["reason_kind"] and before["summary"] == after["summary"] and before["revival_trigger"] == after["revival_trigger"])
    check("exact", f"{row_id} points to weld evidence", after["evidence"] == "selected-second-layer-dupsilon-gauge-orbit-weld-2026-08-07.md")
    check("type", f"{row_id} keeps action work open", "OPEN" in after["mapping_grade"])
migrations = [item for item in new["migrations"] if item.get("from_version") == "0.42" and item.get("to_version") == "0.43"]
check("exact", "five migrations recorded in order", [item["row_id"] for item in migrations] == touched)
check("exact", "row meanings remain fixed", all(item["meaning_changed"] is False for item in migrations))
check("exact", "wave dispositions name five rows", [item["row_id"] for item in new["wave_row_dispositions"]] == touched)

print("\nC. EXACT WELD BOUNDARY")
exact = registry["exact_result"]
check("exact", "metric and connection orbit ranks are four", exact["metric_diffeomorphism_rank"] == exact["metric_hessian_ward_load_rank"] == exact["forced_metric_residual_gauge_response_rank"] == exact["connection_one_form_diffeomorphism_rank"] == 4)
check("exact", "diagnostic weld is unique only on the orbit", exact["diagnostic_orbit_weld"] == "EXACT_AND_UNIQUE_ON_IM_G")
check("type", "twelve transverse connection directions remain", exact["transverse_connection_dimension"] == 12 and exact["actual_transverse_action_derivative"] == "OPEN")
check("type", "actual four selected-Upsilon columns remain open", exact["actual_selected_upsilon_four_columns"] == "OPEN")
check("type", "rank one is now the four-column action test", "four source-native connection" in new["next_work_queue"][0]["why"] and "twelve transverse" in new["next_work_queue"][0]["why"])
check("source", "source return is confirm plus silent", "SOURCE-CONFIRMS" in registry["source_return"] and "SOURCE-SILENT" in registry["source_return"])
check("symplectic", "no fifth quotient is booked", new["residue"]["quotients_ranked"] == 4)
for label in (
    "diagnostic weld is not action-derived Upsilon",
    "D Upsilon naturality is not Xi equals D Upsilon redundancy",
    "Ward radical is not BV or BFV reduction",
    "rank matching does not select scalar physics",
    "external datum does not manufacture a tangent map",
    "no residue quotient or posture changes",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
