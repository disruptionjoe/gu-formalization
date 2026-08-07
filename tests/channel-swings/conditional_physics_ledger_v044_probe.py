#!/usr/bin/env python3
"""Fail-closed migration audit for conditional physics ledger v0.44."""

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


old = strict("lab/process/conditional-physics-ledger-v0.43.json")
new = strict("lab/process/conditional-physics-ledger-v0.44.json")
registry = strict("lab/process/selected-second-layer-actual-source-lift-rank-mismatch.json")
touched = ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"]

print("A. FROZEN HEADLINE")
check("exact", "schema advances 0.43 to 0.44", old["schema_version"] == "0.43" and new["schema_version"] == "0.44")
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
    "COVECTOR_SLOT_ONLY_G_T_PROXY",
    "FULL_TAUTOLOGICAL_SLOT_TRANSPORT",
    "INDEPENDENT_CONNECTION_LIFT_L_D",
    "COMPLETE_SECTION_OBSERVATION_DIFFEO_ORBIT",
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
    check("exact", f"{row_id} points to source-lift evidence", after["evidence"] == "selected-second-layer-actual-source-lift-rank-mismatch-2026-08-07.md")
    check("type", f"{row_id} keeps complete action work open", "OPEN" in after["mapping_grade"])
migrations = [item for item in new["migrations"] if item.get("from_version") == "0.43" and item.get("to_version") == "0.44"]
check("exact", "five migrations recorded in order", [item["row_id"] for item in migrations] == touched)
check("exact", "row meanings remain fixed", all(item["meaning_changed"] is False for item in migrations))
check("exact", "wave dispositions name five rows", [item["row_id"] for item in new["wave_row_dispositions"]] == touched)

print("\nC. SOURCE-CORRECTED RANK BOUNDARY")
exact = registry["exact_result"]
check("exact", "v0.43 proxy rank remains four", exact["v043_covector_slot_proxy_rank"] == 4)
check("exact", "actual connection lift has rank three", exact["actual_independent_connection_diffeomorphism_rank"] == 3)
check("exact", "complete metric generator still has rank four", exact["complete_metric_connection_generator_rank"] == 4)
check("exact", "actual connection kernel is the time generator", exact["actual_connection_kernel"] == [1, 0, 0, 0])
check("exact", "metric load has rank four", exact["metric_ward_load_rank"] == 4)
check("exact", "metric load is nonzero on the connection kernel", exact["metric_ward_load_on_connection_kernel"] == "NONZERO_FOR_ALL_NONZERO_REST_MOMENTUM")
check("exact", "connection-only weld is impossible", exact["connection_only_selected_upsilon_weld"] == "IMPOSSIBLE_AT_CURRENT_PRINCIPAL_GRADE")
check("type", "section observation orbit remains open", exact["section_observation_diffeomorphism_response"] == "OPEN")
check("type", "rank one is now section observation on the time kernel", "section/observation" in new["next_work_queue"][0]["why"] and "time-reparametrization" in new["next_work_queue"][0]["why"])
check("source", "source return corrects the proxy and remains silent on the missing weld", "SOURCE-CORRECTS" in registry["source_return"] and "SOURCE-SILENT" in registry["source_return"])
check("symplectic", "no fifth quotient is booked", new["residue"]["quotients_ranked"] == 4)
for label in (
    "proxy retraction does not erase the proxy theorem",
    "connection-only route kill is not a full-action kill",
    "rank mismatch is not repaired by external datum",
    "section observation tangent is not assumed from prose",
    "principal-grade failure does not kill separately typed lower-order terms",
    "no scalar pole coefficient domain BV BFV or residue quotient is promoted",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
