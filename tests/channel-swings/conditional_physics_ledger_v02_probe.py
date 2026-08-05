#!/usr/bin/env python3
"""Structural and provenance checks for conditional physics ledger v0.2."""

from collections import Counter
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def strict(path):
    def pairs(items):
        keys = [key for key, _ in items]
        if len(keys) != len(set(keys)):
            raise ValueError(f"duplicate key in {path}")
        return dict(items)
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=pairs)


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


v1_path = ROOT / "lab/process/conditional-physics-ledger-v0.1.json"
v2_path = ROOT / "lab/process/conditional-physics-ledger-v0.2.json"
view1_path = ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.1.md"
v1 = strict(v1_path)
v2 = strict(v2_path)
rows1 = {row["id"]: row for row in v1["rows"]}
rows2 = {row["id"]: row for row in v2["rows"]}

print("A. IMMUTABLE PREDECESSOR AND DENOMINATOR")
check("provenance", "v0.1 machine ledger retains its pinned digest",
      hashlib.sha256(v1_path.read_bytes()).hexdigest() == "563565dfd0b8df7d159a4198553a3011a164b196d50e1fb9cdde0bb4d6b2d05b")
check("provenance", "v0.1 human view retains its pinned digest",
      hashlib.sha256(view1_path.read_bytes()).hexdigest() == "edef0a157f999384d796aa308a5d690ea810c08450fe11a7d6998fdf162897d4")
check("exact", "v0.2 names v0.1 as predecessor", v2["predecessor"].endswith("v0.1.json"))
check("exact", "all 78 row IDs and meanings remain present", set(rows1) == set(rows2) and len(rows2) == 78)
check("exact", "the source denominator and aliases remain 86/78/8",
      v2["denominator"]["source_row_count"] == 86
      and v2["denominator"]["canonical_target_count"] == 78
      and len(v2["aliases"]) == 8)
check("exact", "axis counts remain 35/17/26",
      Counter(r["axis"] for r in rows2.values()) ==
      {"REPRESENTATION":35,"LAGRANGIAN":17,"ANOMALY_CONSISTENCY":26})

print("\nB. EXACTLY ONE SCOPED EVIDENCE MIGRATION")
migrations = {item["row_id"]: item for item in v2["migrations"]}
changed = {rid for rid in rows1 if rows1[rid] != rows2[rid]}
check("exact", "only LT-GR1b changed", changed == {"LT-GR1b"})
check("exact", "migration list matches changed rows", set(migrations) == changed)
check("exact", "neither migration changes the row meaning", all(not m["meaning_changed"] for m in migrations.values()))
check("exact", "LT-GR1 remains byte-equivalent at row grade", rows2["LT-GR1"] == rows1["LT-GR1"])
check("exact", "LT-GR1b becomes a selected-route genuine falsification",
      rows2["LT-GR1b"]["verdict"] == "OVER_DETERMINED"
      and rows2["LT-GR1b"]["reason_kind"] == "GENUINE_FALSIFICATION"
      and "SELECTED_POST_SHIAB" in rows2["LT-GR1b"]["mapping_grade"]
      and "FACTORIZATION_ONLY" in rows2["LT-GR1b"]["construction_scope"])
check("type", "LT-GR1b distance points to an independent pre-Shiab route",
      "pre-Shiab" in rows2["LT-GR1b"]["distance"])
check("type", "LT-GR1b revival permits a different information-preserving Shiab",
      "kernel" in rows2["LT-GR1b"]["revival_trigger"])
check("planted", "PLANT selected-route falsification is not rewritten as GU-wide falsification",
      "selected" in migrations["LT-GR1b"]["scope"])

print("\nC. COUNTS, TAXONOMY, AND QUEUE")
verdicts = Counter(row["verdict"] for row in rows2.values())
check("exact", "verdict counts remain 32/18/22/6",
      verdicts == {"SAME":32,"DIFFERS":18,"NEEDS":22,"OVER_DETERMINED":6})
check("exact", "coverage remains 78/78 and is not construction completion",
      v2["progress"]["mapped"] == v2["progress"]["total"] == 78
      and "not a claim" in v2["progress"]["coverage_scope"])
check("exact", "residue remains explicit and unranked",
      v2["residue"]["continuous_real"] == 83
      and v2["residue"]["function_valued_at_least"] >= 19
      and v2["residue"]["quotients_ranked"] == 0)
check("exact", "every row kind remains registered under its verdict",
      all(row["reason_kind"] in v2["taxonomy"]["verdict_kinds"][row["verdict"]]
          for row in rows2.values()))
check("exact", "all six over-determined rows retain independent owners",
      {e["row_id"] for e in v2["over_determined_escalations"]}
      == {rid for rid,row in rows2.items() if row["verdict"] == "OVER_DETERMINED"})
check("exact", "next queue leads with Gauss receiver action ownership",
      v2["next_work_queue"][0]["rows"] == ["LT-GR1", "LT-GR1b"]
      and "Gauss" in v2["next_work_queue"][0]["why"])


def classify(verdict, kind):
    return "KNOWN" if kind in v2["taxonomy"]["verdict_kinds"].get(verdict, []) else "NEW_KIND_REQUIRED"


check("planted", "PLANT unknown kinds remain new kinds rather than forced fits",
      classify("NEEDS", "RHYME") == "NEW_KIND_REQUIRED")
check("planted", "PLANT flat verdict counts do not erase evidence migration progress",
      "1 scoped evidence migration" in v2["progress"]["meter"])

print("\nCOUNTS " + " ".join(f"{k}={v}" for k,v in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS total={sum(COUNTS.values())}")
