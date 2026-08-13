#!/usr/bin/env python3
"""Gate the append-only conditional physics ledger update to v0.230."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OLD_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.229.json"
NEW_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.230.json"
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
      old["schema_version"] == "0.229" and new["schema_version"] == "0.230"
      and new["predecessor"].endswith("conditional-physics-ledger-v0.229.json"))
check("ledger", "row IDs and denominator remain immutable",
      list(old_rows) == list(new_rows) and old["denominator"] == new["denominator"])
check("ledger", "only the three declared rows change",
      all(old_rows[row_id] == new_rows[row_id] for row_id in old_rows if row_id not in touched))
check("ledger", "touched verdicts and reason kinds remain unchanged",
      all((old_rows[row_id]["verdict"], old_rows[row_id]["reason_kind"])
          == (new_rows[row_id]["verdict"], new_rows[row_id]["reason_kind"])
          for row_id in touched))
check("ledger", "all touched rows point to the new exact evidence",
      all(new_rows[row_id]["evidence"]
          == "selected-k77-i2b-independent-tangent-queue-correction-2026-08-13.md"
          for row_id in touched))

check("accounting", "headline verdict counts remain unchanged",
      old["progress"]["verdict_counts"] == new["progress"]["verdict_counts"])
check("accounting", "raw residue and quotient accounting remain unchanged",
      old["residue"]["continuous_real"] == new["residue"]["continuous_real"] == 84
      and old["residue"]["quotients_ranked"] == new["residue"]["quotients_ranked"] == 5)
check("frontier", "one mistyped moving-geometry condition closes",
      new["frontier_delta"] == {
          "headline_delta": "NONE", "conditions_closed": 1,
          "conditions_opened": 0, "remaining_named_conditions": 3})
check("source", "source return preserves Q_B and constraint silence",
      "SOURCE_CONFIRMS_INDEPENDENT_VARPI" in new["source_return"]
      and "T_DEPENDENT_QB_OR_CONSTRAINT" in new["source_return"])
check("type", "independent cotangent components remain explicit",
      any("independent varpi/T Euler component" in item
          for item in new["layer0_objects_compared"]))
check("type", "Q_u and Q_B remain distinct",
      any("repository-conditional Q_u" in item for item in new["layer0_objects_compared"]))

check("queue", "rank one is now Q_B/action ownership or a constraint/BV tangent",
      "source Q_B/full-or-two-half action parent" in new["next_work_queue"][0]["why"]
      and "constraint/full BV-KT tangent" in new["next_work_queue"][0]["why"])
check("queue", "the retired geometry-only repair is not requeued",
      "Construct the actual coupled moving reference" not in new["next_work_queue"][0]["why"])
check("disposition", "three scoped row dispositions are declared",
      {item["row_id"] for item in new["wave_row_dispositions"]} == touched)
check("migration", "three v0.229 to v0.230 migrations are append-recorded",
      sum(item.get("from_version") == "0.229" and item.get("to_version") == "0.230"
          for item in new["migration_history"]) == 3)

check("plant", "PLANT no external datum is consumed",
      "P1/P2/P3" in new["migration_policy"] and "do not move" in new["migration_policy"])
check("plant", "PLANT no new quotient is booked",
      old["residue"]["quotients_ranked"] == new["residue"]["quotients_ranked"])
check("plant", "PLANT source Q_B remains open",
      "SOURCE_QB" in new["residue"]["conditional_observer_time_reduction"]["open"])
check("plant", "PLANT no GU-wide no-go is claimed",
      all(new_rows[row_id]["verdict"] == old_rows[row_id]["verdict"] for row_id in touched))

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
