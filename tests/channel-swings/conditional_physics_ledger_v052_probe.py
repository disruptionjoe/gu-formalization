#!/usr/bin/env python3
"""Fail-closed append-only checks for residual-zero owner retype v0.52."""

from collections import Counter
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
FAILURES = []
COUNTS = Counter()
MIGRATED = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}


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


old = strict("lab/process/conditional-physics-ledger-v0.51.json")
new = strict("lab/process/conditional-physics-ledger-v0.52.json")
result = strict("lab/process/selected-second-layer-transverse117-residual-zero-owner-class.json")
old_rows = {r["id"]: r for r in old["rows"]}
new_rows = {r["id"]: r for r in new["rows"]}

check("exact", "schema advances exactly", old["schema_version"] == "0.51" and new["schema_version"] == "0.52")
check("exact", "row IDs and denominator freeze", set(old_rows) == set(new_rows) and old["denominator"] == new["denominator"])
check("exact", "only five row records migrate", {r for r in old_rows if old_rows[r] != new_rows[r]} == MIGRATED)
check("exact", "unmigrated rows freeze", all(old_rows[r] == new_rows[r] for r in old_rows if r not in MIGRATED))
check("exact", "verdicts and reason kinds freeze", all((old_rows[r]["verdict"], old_rows[r]["reason_kind"]) == (new_rows[r]["verdict"], new_rows[r]["reason_kind"]) for r in old_rows))
check("exact", "headline counts freeze", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("exact", "residue and quotients freeze", new["residue"] == old["residue"])
check("exact", "five append-only migrations exist", {m["row_id"] for m in new["migrations"] if m.get("from_version") == "0.51" and m.get("to_version") == "0.52"} == MIGRATED)
check("exact", "support partition remains 28 plus 117", result["exact_result"]["connection_q_exact_support"] == 28 and result["exact_result"]["transverse_support"] == 117 and 28 + 117 == 145)
check("exact", "support intersection is zero", result["exact_result"]["support_intersection"] == 0)
check("control", "nonzero background control remains live", result["exact_result"]["nonzero_background_control"] == "LIVE")
check("source", "source return types epsilon and remains silent on owner", new["source_return"] == result["source_return"])
check("program", "frontier closes three and opens one typed fork", new["frontier_delta"] == result["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3, "conditions_opened": 1, "remaining_named_conditions": 5})
check("program", "P1 P2 P3 remain unused", result["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})
check("program", "Curt and third lane remain fenced", result["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and result["third_lane_gate"] == "NOT_PROMOTED")

for label in (
    "route kill is not full action kill",
    "zero background is not nonzero background",
    "source epsilon is not diffeomorphism soldering",
    "normal-jet carrier is not coefficient equality",
    "principal Bianchi is not total naturality",
    "distance migration is not verdict movement",
    "source silence is not refutation",
    "symplectic review is not BV promotion",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{k}:{v}" for k, v in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
