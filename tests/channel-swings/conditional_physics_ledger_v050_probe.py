#!/usr/bin/env python3
"""Fail-closed append-only and AC-G1 propagation checks for ledger v0.50."""

from collections import Counter
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
FAILURES = []
COUNTS = Counter()


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


old = strict("lab/process/conditional-physics-ledger-v0.49.json")
new = strict("lab/process/conditional-physics-ledger-v0.50.json")
result = strict("lab/process/ac-g1-propagation-pointer-baseline.json")

old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
active = [row for row in new["rows"] if row.get("row_status") != "SUPERSEDED"]

check("exact", "schema advances exactly", old["schema_version"] == "0.49" and new["schema_version"] == "0.50")
check("exact", "active denominator freezes", new["denominator"]["canonical_target_count"] == old["denominator"]["canonical_target_count"] == 82)
check("exact", "one record and one superseded row are added", new["denominator"]["row_record_count"] == old["denominator"]["row_record_count"] + 1 and new["denominator"]["historical_superseded_count"] == old["denominator"]["historical_superseded_count"] + 1)
check("exact", "old row IDs freeze and one successor appends", set(new_rows) == set(old_rows) | {"AC-G1a"})
check("exact", "all predecessor rows except AC-G1 are byte-equivalent", all(new_rows[rid] == old_rows[rid] for rid in old_rows if rid != "AC-G1"))
check("type", "AC-G1 is retained and superseded", new_rows["AC-G1"]["row_status"] == "SUPERSEDED" and new_rows["AC-G1"]["successors"] == ["AC-G1a"])
check("type", "successor owns settled-horn missing construction", new_rows["AC-G1a"]["verdict"] == "NEEDS" and new_rows["AC-G1a"]["reason_kind"] == "MISSING_CONSTRUCTION" and "Cl(7,7)" in new_rows["AC-G1a"]["summary"])
check("exact", "active row count remains 82", len(active) == 82)
check("exact", "active verdict counts move one stale premise to needs", Counter(row["verdict"] for row in active) == Counter({"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}))
check("exact", "residue and quotient headline freezes", all(new["residue"][key] == old["residue"][key] for key in ("continuous_real", "function_valued_at_least", "open_discrete_forks", "quotients_ranked")))
check("exact", "AC-G1 migration points to AC-G1a", any(m.get("row_id") == "AC-G1" and m.get("from_version") == "0.49" and m.get("to_version") == "0.50" and m.get("successor_id") == "AC-G1a" for m in new["migrations"]))
check("program", "independent disposition is recorded", next(x for x in new["over_determined_escalations"] if x["row_id"] == "AC-G1")["status"].startswith("ADJUDICATED_STALE_PREMISE"))
check("source", "settled horn returns source silence", new["source_return"] == result["source_return"] == "SOURCE-SILENT__SETTLED_CL77_ANOMALY_REPLACEMENT_GROUP_OR_RECEPTACLE")
check("program", "P1 P2 P3 remain unused", result["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})
check("program", "Curt and third lane remain fenced", result["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and result["third_lane_gate"] == "NOT_PROMOTED")

for label in (
    "Sp64 pincer defusal is not full anomaly cancellation",
    "Cl95 horn is not settled Cl77 horn",
    "supersession is not deletion",
    "needs construction is not anomaly falsification",
    "historical baseline is not current head truth",
    "scope correction is not canon promotion",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{k}:{v}" for k, v in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
