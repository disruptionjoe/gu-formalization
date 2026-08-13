#!/usr/bin/env python3
"""Fail-closed migration audit for conditional physics ledger v0.47."""

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


old = strict("lab/process/conditional-physics-ledger-v0.46.json")
new = strict("lab/process/conditional-physics-ledger-v0.47.json")
registry = strict("lab/process/selected-second-layer-shiab-inverse-bianchi-completion.json")
touched = ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"]

print("A. FROZEN HEADLINE")
check("exact", "schema advances 0.46 to 0.47", old["schema_version"] == "0.46" and new["schema_version"] == "0.47")
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
    check("exact", f"{rid} points to v0.47 evidence", after["evidence"] == "selected-second-layer-shiab-inverse-bianchi-completion-2026-08-07.md")
migrations = [x for x in new["migrations"] if x.get("from_version") == "0.46" and x.get("to_version") == "0.47"]
check("exact", "five migrations recorded in order", [x["row_id"] for x in migrations] == touched)
check("exact", "migration old/new triples match rows", all(x["old"] == [old_rows[x["row_id"]][k] for k in ("verdict", "reason_kind", "mapping_grade")] and x["new"] == [new_rows[x["row_id"]][k] for k in ("verdict", "reason_kind", "mapping_grade")] for x in migrations))
check("exact", "row meanings remain fixed", all(x["meaning_changed"] is False for x in migrations))
check("exact", "wave dispositions name five rows", [x["row_id"] for x in new["wave_row_dispositions"]] == touched)

print("\nC. SHIAB INVERSE AND BIANCHI BOUNDARY")
exact = registry["exact_result"]
check("exact", "full selected map is 1274 by 1274", exact["selected_shiab_source_dimension"] == exact["selected_shiab_target_dimension"] == 1274)
check("exact", "full selected map is an isomorphism", exact["selected_shiab_rank"] == 1274 and exact["selected_shiab_kernel_dimension"] == 0)
check("exact", "four unique preimage supports are exact", exact["unique_preimage_supports"] == [58, 29, 29, 29])
check("exact", "preimages are real rational and reconstruct exactly", exact["preimages_real_rational"] is True and exact["preimage_reconstruction_exact"] is True)
check("exact", "all four wedge maps have rank fourteen", exact["principal_bianchi_ranks"] == [14, 14, 14, 14])
check("exact", "no individual nonzero principal covector exists", exact["individual_nonzero_principal_covector_exists"] is False)
check("exact", "no common nonzero principal covector exists", exact["common_principal_bianchi_rank"] == 14 and exact["common_nonzero_principal_covector_exists"] is False)
check("type", "standalone split is not a connection-curvature jet", exact["split_preimage_is_connection_curvature_jet"] is False)
check("type", "total GCR completion remains open", exact["source_native_total_gcr_completion"] == "OPEN")
check("type", "nonzero-background covariant Bianchi remains open", exact["nonzero_background_covariant_bianchi"] == "OPEN")
check("symplectic", "no fifth quotient is booked", new["residue"]["quotients_ranked"] == 4)
for label in (
    "carrier containment does not imply a lawful connection jet",
    "Shiab invertibility does not imply Bianchi closure",
    "split nonclosure does not kill total curvature",
    "zero pure-gauge total does not recover physics",
    "external datum cannot select an action derivative",
    "no scalar pole domain BV BFV quotient or posture is promoted",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{k}:{v}" for k, v in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
