#!/usr/bin/env python3
"""Gate the append-only conditional physics ledger update to v0.229."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OLD_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.228.json"
NEW_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.229.json"
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
      old["schema_version"] == "0.228"
      and new["schema_version"] == "0.229"
      and new["predecessor"].endswith("conditional-physics-ledger-v0.228.json"))
check("ledger", "row IDs and denominator remain immutable",
      list(old_rows) == list(new_rows) and old["denominator"] == new["denominator"])
check("ledger", "only the three declared Higgs/action rows change",
      all(old_rows[row_id] == new_rows[row_id]
          for row_id in old_rows if row_id not in touched))
check("ledger", "touched row verdicts and reason kinds remain unchanged",
      all((old_rows[row_id]["verdict"], old_rows[row_id]["reason_kind"])
          == (new_rows[row_id]["verdict"], new_rows[row_id]["reason_kind"])
          for row_id in touched))
check("ledger", "all three touched rows point to the new exact evidence",
      all(new_rows[row_id]["evidence"]
          == "selected-k77-i2b-source-gauge-bv-image-2026-08-13.md"
          for row_id in touched))

check("accounting", "headline verdict counts remain unchanged",
      old["progress"]["verdict_counts"] == new["progress"]["verdict_counts"])
check("accounting", "raw residue and quotient accounting remain unchanged",
      old["residue"] == new["residue"]
      and new["residue"]["continuous_real"] == 84
      and new["residue"]["quotients_ranked"] == 5)
check("frontier", "one local gauge-quotient condition closes",
      new["frontier_delta"] == {
          "headline_delta": "NONE",
          "conditions_closed": 1,
          "conditions_opened": 0,
          "remaining_named_conditions": 4,
      })
check("source", "source return separates source grammar from repo-derived image",
      "SOURCE_CONFIRMS_SC_ACT_01" in new["source_return"]
      and "SOURCE_SILENT_SELECTED_196_CELL_ADJOINT_IMAGE" in new["source_return"]
      and "REPOSITORY_DERIVES_EXACT_LOCAL_NEGATIVE" in new["source_return"])
check("type", "field translation and gauge parameter remain distinct",
      any("source-field translation alpha versus gauge parameter zeta" in item
          for item in new["layer0_objects_compared"]))
check("type", "Ward descent is not collapsed to stationarity",
      any("Ward-annihilated Euler covector versus zero Euler covector" in item
          for item in new["layer0_objects_compared"]))

check("queue", "the rank-one successor is now the moving geometric Frechet response",
      new["next_work_queue"][0]["rank"] == 1
      and "moving reference/metric/section/Hodge/Shiab/trace-Hq Frechet response"
      in new["next_work_queue"][0]["why"])
check("queue", "the queue forbids a fitted cancellation",
      "without fitting a cancellation" in new["next_work_queue"][0]["why"])
check("disposition", "the three scoped row dispositions are declared",
      {item["row_id"] for item in new["wave_row_dispositions"]} == touched)
check("collision", "the orphaned claim recovery is exposed",
      new["collision_disposition"].startswith("ORPHANED_STALE_GU_CLAIM"))
check("mailbox", "postflight mailbox review records no successor reordering",
      "NONE_CORRECTS_COMPLETED_RESULT_OR_REORDERS_RANK_ONE_SUCCESSOR"
      in new["mailbox_disposition"])

# Firing controls.
check("plant", "PLANT source translation is not booked as a quotient",
      new["residue"]["quotients_ranked"] == old["residue"]["quotients_ranked"])
check("plant", "PLANT no external datum is consumed",
      "P1/P2/P3 remain unchanged" in new["residue"]["meter"])
check("plant", "PLANT full BV/KT remains open",
      "full BV/KT" in new["progress"]["coverage_scope"])
check("plant", "PLANT no physics verdict moves",
      all(new_rows[row_id]["verdict"] == old_rows[row_id]["verdict"] for row_id in touched))

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
