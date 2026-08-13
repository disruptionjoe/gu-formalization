#!/usr/bin/env python3
"""Fail-closed migration audit for conditional physics ledger v0.48."""

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


old = strict("lab/process/conditional-physics-ledger-v0.47.json")
new = strict("lab/process/conditional-physics-ledger-v0.48.json")
registry = strict("lab/process/selected-second-layer-nonnull-koszul-gcr-split.json")
touched = ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"]

print("A. FROZEN HEADLINE")
check("exact", "schema advances 0.47 to 0.48", old["schema_version"] == "0.47" and new["schema_version"] == "0.48")
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
    check("exact", f"{rid} points to v0.48 evidence", after["evidence"] == "selected-second-layer-nonnull-koszul-gcr-split-2026-08-07.md")
migrations = [x for x in new["migrations"] if x.get("from_version") == "0.47" and x.get("to_version") == "0.48"]
check("exact", "five migrations recorded in order", [x["row_id"] for x in migrations] == touched)
check("exact", "migration old/new triples match rows", all(x["old"] == [old_rows[x["row_id"]][k] for k in ("verdict", "reason_kind", "mapping_grade")] and x["new"] == [new_rows[x["row_id"]][k] for k in ("verdict", "reason_kind", "mapping_grade")] for x in migrations))
check("exact", "row meanings remain fixed", all(x["meaning_changed"] is False for x in migrations))
check("exact", "wave dispositions name five rows", [x["row_id"] for x in new["wave_row_dispositions"]] == touched)

print("\nC. NON-NULL KOSZUL/GCR BOUNDARY")
exact = registry["exact_result"]
check("exact", "rest covector is non-null", exact["principal_covector"] == "e0" and exact["principal_covector_norm_squared"] == -1)
check("exact", "metric-normalized contraction exists", exact["metric_normalized_contraction_exists"] is True)
check("exact", "connection supports are exact", exact["connection_supports"] == [7, 7, 7, 7] and exact["total_connection_support"] == 28)
check("exact", "transverse supports are exact", exact["transverse_supports"] == [51, 22, 22, 22] and exact["total_transverse_support"] == 117)
check("exact", "both four-column families have rank four", exact["connection_family_rank"] == exact["transverse_family_rank"] == 4)
check("exact", "selected-Shiab reconstruction is exact and both images nonzero", exact["selected_shiab_reconstruction_exact"] is True and exact["connection_selected_image_nonzero"] is True and exact["transverse_selected_image_nonzero"] is True)
check("type", "source-native GCR identification remains open", exact["source_native_gcr_identification"] == "OPEN")
check("type", "null split is unavailable and screen-dependent", exact["null_metric_normalized_split"] == "UNAVAILABLE" and exact["null_auxiliary_screen_dependence"] == "EXACT_CONTROL")
check("symplectic", "no fifth quotient is booked", new["residue"]["quotients_ranked"] == 4)
for label in (
    "Koszul remainder is not source-owned GCR",
    "test covector is not an external datum",
    "principal Bianchi is not nonlinear covariant Bianchi",
    "support is not multiplicity or particle count",
    "non-null split does not close the null branch",
    "no scalar pole domain BV BFV quotient or posture is promoted",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{k}:{v}" for k, v in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
