#!/usr/bin/env python3
"""Gate the append-only conditional physics ledger update to v0.231."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OLD_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.230.json"
NEW_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.231.json"
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
evidence = "selected-k77-i2b-source-natural-primalizer-classification-2026-08-13.md"

check("ledger", "schema advances exactly one append-only version",
      old["schema_version"] == "0.230" and new["schema_version"] == "0.231"
      and new["predecessor"].endswith("conditional-physics-ledger-v0.230.json"))
check("ledger", "row IDs and denominator remain immutable",
      list(old_rows) == list(new_rows) and old["denominator"] == new["denominator"])
check("ledger", "only the three declared rows change",
      all(old_rows[row_id] == new_rows[row_id]
          for row_id in old_rows if row_id not in touched))
check("ledger", "touched verdicts and reason kinds remain unchanged",
      all((old_rows[row_id]["verdict"], old_rows[row_id]["reason_kind"])
          == (new_rows[row_id]["verdict"], new_rows[row_id]["reason_kind"])
          for row_id in touched))
check("ledger", "all touched rows point to the new exact evidence",
      all(new_rows[row_id]["evidence"] == evidence for row_id in touched))

check("accounting", "headline verdict counts remain unchanged",
      old["progress"]["verdict_counts"] == new["progress"]["verdict_counts"])
check("accounting", "raw residue and quotient accounting remain unchanged",
      old["residue"]["continuous_real"] == new["residue"]["continuous_real"] == 84
      and old["residue"]["quotients_ranked"] == new["residue"]["quotients_ranked"] == 5)
check("frontier", "fixed-pairing freedom closes and two live exits remain",
      new["frontier_delta"] == {
          "headline_delta": "NONE", "conditions_closed": 1,
          "conditions_opened": 0, "remaining_named_conditions": 2})
check("source", "source return distinguishes source and repository ownership",
      "SOURCE_CONFIRMS_BOSONIC_NORM_SQUARE" in new["source_return"]
      and "SOURCE_SILENT_REAL_K77_QB" in new["source_return"]
      and "REPOSITORY_DERIVES_FIXED_NATURAL" in new["source_return"])
check("type", "full and two-half parent readings remain distinct",
      any("full U(64,64) invariant trace line" in item
          for item in new["layer0_objects_compared"])
      and any("two C^(32,32) carrier halves" in item
              for item in new["layer0_objects_compared"]))
check("type", "fixed and moving primalizers remain distinct",
      any("fixed source-natural Q_B" in item
          for item in new["layer0_objects_compared"]))
check("type", "the bosonic B label is not connection dependence",
      any("bosonic label B on Q_B" in item
          for item in new["layer0_objects_compared"]))

rank_one = new["next_work_queue"][0]["why"]
check("queue", "rank one is the source-derived constraint/full BV-KT tangent",
      "source-derived constraint/full BV-KT tangent" in rank_one)
check("queue", "moving or field-dependent reduction remains a rival",
      "moving reduction" in rank_one)
check("queue", "fixed-pairing search is not requeued",
      "one nonzero scale" in rank_one and "without fitting a subspace" in rank_one)
check("disposition", "three scoped row dispositions are declared",
      {item["row_id"] for item in new["wave_row_dispositions"]} == touched)
check("migration", "three v0.230 to v0.231 migrations are append-recorded",
      sum(item.get("from_version") == "0.230" and item.get("to_version") == "0.231"
          for item in new["migration_history"]) == 3)

contract = (ROOT / "lab/process/functional-channel-operating-contract-v1.0.json")
lanes = (ROOT / "LANES.yaml").read_text(encoding="utf-8")
next_steps = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
contract_json = load_unique(contract)
check("pointer", "machine contract points to v0.231",
      contract_json["standing_ledger"]["ref"] == str(NEW_PATH.relative_to(ROOT)))
check("pointer", "LANES points to both v0.231 surfaces",
      "conditional-physics-ledger-v0.231.json" in lanes
      and "conditional-physics-ledger-v0.231.md" in lanes)
check("pointer", "NEXT-STEPS exposes the fixed-pairing closure",
      "SOURCE-NATURAL PRIMALIZER CLASSIFICATION" in next_steps
      and "fixed `Q_B` freedom" in next_steps
      and "BV--Koszul--Tate tangent" in next_steps)

required = [
    ROOT / "explorations/conditional-build/selected-k77-i2b-source-natural-primalizer-classification-2026-08-13.md",
    ROOT / "lab/sources/selected-k77-i2b-source-natural-primalizer-classification-source-return-2026-08-13.md",
    ROOT / "lab/process/hostile-reviews/2026-08-13-selected-k77-i2b-source-natural-primalizer-classification-review.md",
    ROOT / "tests/channel-swings/selected_k77_i2b_source_natural_primalizer_classification_probe.py",
]
check("artifact", "result source return hostile review and probe all exist",
      all(path.exists() for path in required))

check("plant", "PLANT no external datum is consumed",
      "P1/P2/P3" in new["migration_policy"] and "do not move" in new["migration_policy"])
check("plant", "PLANT no new quotient is booked",
      old["residue"]["quotients_ranked"] == new["residue"]["quotients_ranked"])
check("plant", "PLANT fixed pairing is not called positive",
      "positive" not in new["wave_row_dispositions"][0]["disposition"].lower())
check("plant", "PLANT no GU-wide no-go is claimed",
      all(new_rows[row_id]["verdict"] == old_rows[row_id]["verdict"]
          for row_id in touched))

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
