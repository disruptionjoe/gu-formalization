#!/usr/bin/env python3
"""Gate the append-only conditional physics ledger migration to v0.226."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OLD_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.225.json"
NEW_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.226.json"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def load_unique(path: Path) -> dict:
    def hook(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key!r} in {path}")
            result[key] = value
        return result

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


old = load_unique(OLD_PATH)
new = load_unique(NEW_PATH)
old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
touched = {"RA-E1", "RA-E3", "LT-SM6"}

check("ledger", "schema advances exactly one append-only version",
      old["schema_version"] == "0.225"
      and new["schema_version"] == "0.226"
      and new["predecessor"].endswith("conditional-physics-ledger-v0.225.json"))
check("ledger", "row IDs and denominator remain immutable",
      list(old_rows) == list(new_rows)
      and old["denominator"] == new["denominator"])
check("ledger", "only declared rows change",
      all(old_rows[row_id] == new_rows[row_id]
          for row_id in old_rows if row_id not in touched))

for row_id in touched:
    before = old_rows[row_id]
    after = new_rows[row_id]
    check("row", f"{row_id} verdict and reason kind do not move",
          (before["verdict"], before["reason_kind"])
          == (after["verdict"], after["reason_kind"]))
    check("row", f"{row_id} points to the corrected square evidence",
          after["evidence"] == "selected-k77-i2b-action-euler-square-2026-08-12.md")
    check("row", f"{row_id} names distinct Frechet maps and fixed-background equality",
          "FRECHET" in after["mapping_grade"]
          and "FIXED_BACKGROUND" in after["mapping_grade"])

check("accounting", "headline verdict counts remain unchanged",
      old["progress"]["verdict_counts"] == new["progress"]["verdict_counts"])
check("accounting", "residue and quotient accounting remain unchanged except typed frontier text",
      old["residue"]["continuous_real"] == new["residue"]["continuous_real"] == 84
      and old["residue"]["function_valued_at_least"] == new["residue"]["function_valued_at_least"] == 19
      and old["residue"]["open_discrete_forks"] == new["residue"]["open_discrete_forks"] == 9
      and old["residue"]["quotients_ranked"] == new["residue"]["quotients_ranked"] == 5)
check("frontier", "one comparison closes and one named construction remains",
      new["frontier_delta"] == {
          "headline_delta": "NONE",
          "conditions_closed": 1,
          "conditions_opened": 0,
          "remaining_named_conditions": 1,
      })
check("source", "source return grades the corrected square as repo-composed",
      new["source_return"]
      == "SOURCE_CONFIRMS_FIRST_ACTION_AND_PRINTED_ENDPOINT_FORMULAS__SOURCE_SILENT_CORRECTED_E_ACT_SQUARE__REPO_CONSTRUCTS_EXACT_LOCAL_RIVAL")
check("scope", "next gate requires an action-owned tangent or BV reduction",
      "DERIVE_SOURCE_ACTION_OWNED_TANGENT_OR_BV_REDUCTION" in
      new["residue"]["conditional_observer_time_reduction"]["open"])
check("scope", "P1 P2 P3 remain unused",
      "P1/P2/P3 remain unchanged" in new["residue"]["meter"])

migrations = [
    item for item in new["migration_history"]
    if item.get("from_version") == "0.225" and item.get("to_version") == "0.226"
]
check("migration", "exactly the three declared migrations are appended",
      {item["row_id"] for item in migrations} == touched and len(migrations) == 3)
check("migration", "all new migrations preserve meaning discipline",
      all(item["meaning_changed"] is True for item in migrations))

# Firing controls.
check("plant", "PLANT the corrected square does not change a verdict",
      new_rows["RA-E1"]["verdict"] != "SAME")
check("plant", "PLANT the fixed-background equality is not a global identity",
      "moving reference" in new_rows["RA-E1"]["distance"])
check("plant", "PLANT no quotient is booked by the wave",
      new["residue"]["quotients_ranked"] == old["residue"]["quotients_ranked"])
check("plant", "PLANT source ownership is not promoted",
      "SOURCE_SILENT" in new["source_return"])
check("plant", "PLANT no external datum is consumed",
      "P1/P2/P3 remain unchanged" in new["residue"]["meter"])

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
