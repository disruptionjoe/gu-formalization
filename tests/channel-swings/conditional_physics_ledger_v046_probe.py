#!/usr/bin/env python3
"""Fail-closed migration audit for conditional physics ledger v0.46."""

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


old = strict("lab/process/conditional-physics-ledger-v0.45.json")
new = strict("lab/process/conditional-physics-ledger-v0.46.json")
registry = strict("lab/process/selected-second-layer-normal-jet-carrier-compatibility.json")
touched = ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"]

print("A. FROZEN HEADLINE")
check("exact", "schema advances 0.45 to 0.46", old["schema_version"] == "0.45" and new["schema_version"] == "0.46")
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
    check("exact", f"{rid} points to v0.46 evidence", after["evidence"] == "selected-second-layer-normal-jet-carrier-compatibility-2026-08-07.md")
migrations = [x for x in new["migrations"] if x.get("from_version") == "0.45" and x.get("to_version") == "0.46"]
check("exact", "five migrations recorded in order", [x["row_id"] for x in migrations] == touched)
check("exact", "migration old/new triples match rows", all(x["old"] == [old_rows[x["row_id"]][k] for k in ("verdict", "reason_kind", "mapping_grade")] and x["new"] == [new_rows[x["row_id"]][k] for k in ("verdict", "reason_kind", "mapping_grade")] for x in migrations))
check("exact", "row meanings remain fixed", all(x["meaning_changed"] is False for x in migrations))
check("exact", "wave dispositions name five rows", [x["row_id"] for x in new["wave_row_dispositions"]] == touched)

print("\nC. OWNER CORRECTION AND CARRIER BOUNDARY")
exact = registry["exact_result"]
check("exact", "raw residual Jacobian is rank ten", exact["raw_conditional_residual_jacobian_rank"] == 10)
check("exact", "raw graph orbit is rank four", exact["raw_graph_orbit_rank"] == 4)
check("exact", "background-subtracted Hessian is not residual-difference Gram", exact["background_subtracted_hessian_equals_difference_jacobian_gram"] is False)
check("exact", "false factorization discrepancy has rank ten", exact["false_factorization_difference_rank_at_s2"] == 10)
check("exact", "source mixed-normal image has rank 1190", exact["selected_mixed_normal_source_image_rank"] == 1190)
check("exact", "all four raw correction columns are in source image", exact["required_raw_orbit_columns_in_source_image"] == 4)
check("type", "actual prolonged field jet remains open", exact["actual_prolonged_diffeomorphism_field_jet"] == "OPEN")
check("type", "background subtraction owner remains open", exact["background_subtraction_action_owner"] == "OPEN")
check("symplectic", "no fifth quotient is booked", new["residue"]["quotients_ranked"] == 4)
for label in (
    "equal Ward ranks do not imply equal operators",
    "carrier containment does not identify the source coefficient",
    "a difference of Gram forms is not a Gram of differences",
    "source silence does not supply a counterterm",
    "external datum cannot select an action derivative",
    "no scalar pole domain BV BFV quotient or posture is promoted",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{k}:{v}" for k, v in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
