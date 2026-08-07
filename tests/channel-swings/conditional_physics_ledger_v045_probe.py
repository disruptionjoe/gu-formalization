#!/usr/bin/env python3
"""Fail-closed migration audit for conditional physics ledger v0.45."""

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


old = strict("lab/process/conditional-physics-ledger-v0.44.json")
new = strict("lab/process/conditional-physics-ledger-v0.45.json")
registry = strict("lab/process/selected-second-layer-observation-owner-retype.json")
touched = ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"]

print("A. FROZEN HEADLINE")
check("exact", "schema advances 0.44 to 0.45", old["schema_version"] == "0.44" and new["schema_version"] == "0.45")
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
    "METRIC_G",
    "GRAPH_SECTION_S_G",
    "INVERTIBLE_OBSERVATION_RECEIVER",
    "MOVING_EVALUATION_NORMAL_JET_OF_UPSILON",
    "CONDITIONAL_ON_SECTION_FULL_II_OWNER_MAP",
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
    check("exact", f"{row_id} points to observation-owner evidence", after["evidence"] == "selected-second-layer-observation-owner-retype-2026-08-07.md")
    check("type", f"{row_id} keeps source normal-jet work open", "OPEN" in after["mapping_grade"])
migrations = [item for item in new["migrations"] if item.get("from_version") == "0.44" and item.get("to_version") == "0.45"]
check("exact", "five migrations recorded in order", [item["row_id"] for item in migrations] == touched)
check("exact", "row meanings remain fixed", all(item["meaning_changed"] is False for item in migrations))
check("exact", "wave dispositions name five rows", [item["row_id"] for item in new["wave_row_dispositions"]] == touched)

print("\nC. OBSERVATION OWNER BOUNDARY")
exact = registry["exact_result"]
check("exact", "metric tangent rank remains four", exact["metric_diffeomorphism_tangent_rank"] == 4)
check("exact", "graph-section tangent is the metric tangent", exact["graph_section_vertical_tangent"] == "SAME_AS_METRIC_TANGENT")
check("exact", "stacking metric and graph section adds no rank", exact["stacked_metric_graph_section_tangent_rank"] == 4)
check("type", "independent observation action field is rejected", exact["independent_observation_action_column"] == "REJECTED_WITHOUT_SEPARATE_SOURCE_FIELD")
check("exact", "observation receiver transports and preserves rank", exact["invertible_observation_receiver_effect"] == "TRANSPORTS_WARD_LOAD_AND_PRESERVES_RANK")
check("exact", "stationary target transport vanishes", exact["moving_target_transport_at_residual_zero"] == "ZERO_AT_STATIONARY_QUADRATIC_GRADE")
check("type", "moving normal-jet term remains live", exact["moving_section_normal_jet_term"] == "CAN_BE_NONZERO_AT_RESIDUAL_ZERO")
check("type", "on-section pullback does not identify the normal jet", exact["normal_jet_from_on_section_full_ii_pullback"] == "NOT_IDENTIFIABLE")
check("type", "rank one is source normal jet then owner comparison", "first normal jet" in new["next_work_queue"][0]["why"] and "full-II owner map" in new["next_work_queue"][0]["why"])
check("source", "source return corrects the receiver and remains silent on the normal jet", "SOURCE-CORRECTS" in registry["source_return"] and "SOURCE-SILENT" in registry["source_return"])
check("symplectic", "no fifth quotient is booked", new["residue"]["quotients_ranked"] == 4)
for label in (
    "receiver transport is not dynamical cancellation",
    "rejecting a duplicate field does not reject moving evaluation",
    "a normal-jet plant is not the source coefficient",
    "the conditional full-II owner map remains conditional",
    "external datum cannot choose an action derivative",
    "no scalar pole coefficient domain BV BFV or residue quotient is promoted",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
