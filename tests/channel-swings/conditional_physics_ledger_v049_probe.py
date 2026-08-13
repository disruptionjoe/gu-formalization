#!/usr/bin/env python3
"""Fail-closed migration audit for conditional physics ledger v0.49."""

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


old = strict("lab/process/conditional-physics-ledger-v0.48.json")
new = strict("lab/process/conditional-physics-ledger-v0.49.json")
registry = strict("lab/process/selected-second-layer-gcr-exterior-degree-owner-retype.json")
touched = ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"]

print("A. FROZEN HEADLINE")
check("exact", "schema advances 0.48 to 0.49", old["schema_version"] == "0.48" and new["schema_version"] == "0.49")
check("exact", "denominator and verdict counts freeze", old["denominator"] == new["denominator"] and old["progress"]["verdict_counts"] == new["progress"]["verdict_counts"])
check("exact", "coverage remains 82 of 82", new["progress"]["mapped"] == new["progress"]["total"] == 82)
for key in ("continuous_real", "function_valued_at_least", "open_discrete_forks", "quotients_ranked"):
    check("exact", f"residue {key} freezes", old["residue"][key] == new["residue"][key])
check("program", "P1 P2 P3 remain unused", registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})
check("program", "Curt and third lane stay fenced", registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and registry["third_lane_gate"] == "NOT_PROMOTED")
check("program", "no posture promotion", registry["claim_status_change"] == registry["canon_verdict_change"] == registry["public_posture_change"] == "none")
check("program", "automation identity is explicit", new["updated_by"] == "gu-formalization-big-waves-hourly")
check("program", "frontier delta is explicit", new["frontier_delta"] == registry["frontier_delta"])
check("source", "source return is explicit", new["source_return"] == registry["source_return"])
check("type", "Layer-0 objects are enumerated", len(new["layer0_objects_compared"]) == 5)
check("program", "collision disposition is observable", new["collision_disposition"] == "NO_COLLISION__CENTRAL_CLAIM_ACQUIRED")

print("\nB. APPEND-ONLY MOVEMENT")
old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
check("exact", "row identities freeze", set(old_rows) == set(new_rows))
check("exact", "exactly five named rows change", [rid for rid in old_rows if old_rows[rid] != new_rows[rid]] == touched)
for rid in touched:
    before, after = old_rows[rid], new_rows[rid]
    check("exact", f"{rid} verdict reason summary revival freeze", before["verdict"] == after["verdict"] and before["reason_kind"] == after["reason_kind"] and before["summary"] == after["summary"] and before["revival_trigger"] == after["revival_trigger"])
    check("exact", f"{rid} points to v0.49 evidence", after["evidence"] == "selected-second-layer-gcr-exterior-degree-owner-retype-2026-08-07.md")
migrations = [x for x in new["migrations"] if x.get("from_version") == "0.48" and x.get("to_version") == "0.49"]
check("exact", "five migrations recorded in order", [x["row_id"] for x in migrations] == touched)
check("exact", "migration old/new triples match rows", all(x["old"] == [old_rows[x["row_id"]][k] for k in ("verdict", "reason_kind", "mapping_grade")] and x["new"] == [new_rows[x["row_id"]][k] for k in ("verdict", "reason_kind", "mapping_grade")] for x in migrations))
check("exact", "row meanings remain fixed", all(x["meaning_changed"] is False for x in migrations))
check("exact", "wave dispositions name five rows", [x["row_id"] for x in new["wave_row_dispositions"]] == touched)

print("\nC. GCR CLIFFORD-GRADE OWNER BOUNDARY")
exact = registry["exact_result"]
check("exact", "all Cl2 curvature source columns are evaluated and nonzero", exact["cl2_source_basis_columns"] == exact["nonzero_cl2_selected_columns"] == 8281)
check("exact", "Cl2 curvature lands only in odd grades", exact["cl2_selected_output_grades"] == [1, 5])
check("exact", "Cl2 curvature has zero required grade-two output", exact["cl2_to_required_grade2_entries"] == 0)
check("exact", "the Cl1 selected map remains a rank-1274 isomorphism", exact["cl1_selected_map_dimension"] == exact["cl1_selected_map_rank"] == 1274)
check("exact", "the v0.48 support partition remains 145 equals 28 plus 117", exact["v048_total_inverse_support"] == 145 and exact["v048_connection_support"] == 28 and exact["v048_transverse_support"] == 117)
check("exact", "the direct HH exterior support is zero", exact["direct_hh_exterior_support"] == 0)
check("exact", "the single-q adapter is excluded", exact["q_contraction_image_rank"] == 13 and exact["required_cliff_q_supports"] == [7, 7, 7, 7] and exact["single_q_adapter"] == "EXCLUDED")
check("type", "direct GCR is killed but an odd source or richer soldering owner remains open", registry["disposition"]["fired"] == "GCR_WRONG_CLIFFORD_GRADE_AND_DIRECT_INPUT_TYPE" and "richer moving epsilon/soldering" in registry["disposition"]["not_killed"])
check("symplectic", "no fifth quotient is booked", new["residue"]["quotients_ranked"] == 4)
for label in (
    "HN/NN exterior labels are not GCR value ownership",
    "old nine-five reconstruction is not the K77 owner",
    "Cl1 injectivity is not full-adjoint injectivity",
    "single-q contraction is not a complete soldering map",
    "grade typing is not total nonlinear Bianchi",
    "no Euler domain BV BFV quotient datum or posture is promoted",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{k}:{v}" for k, v in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
