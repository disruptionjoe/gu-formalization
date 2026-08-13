#!/usr/bin/env python3
"""Gate the append-only conditional physics ledger update to v0.228."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OLD_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.227.json"
NEW_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.228.json"
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

check("ledger", "schema advances exactly one append-only version",
      old["schema_version"] == "0.227"
      and new["schema_version"] == "0.228"
      and new["predecessor"].endswith("conditional-physics-ledger-v0.227.json"))
check("ledger", "row IDs, denominator and every physics row remain immutable",
      list(old_rows) == list(new_rows)
      and old["denominator"] == new["denominator"]
      and old_rows == new_rows)
check("accounting", "headline verdict counts remain unchanged",
      old["progress"]["verdict_counts"] == new["progress"]["verdict_counts"])
check("accounting", "raw residue and quotient accounting remain unchanged",
      old["residue"] == new["residue"]
      and new["residue"]["continuous_real"] == 84
      and new["residue"]["quotients_ranked"] == 5)
check("frontier", "one mixed-boost module condition closes without opening a new program",
      new["frontier_delta"] == {
          "headline_delta": "NONE",
          "conditions_closed": 1,
          "conditions_opened": 0,
          "remaining_named_conditions": 5,
      })
check("source", "source confirms carrier grammar but is silent on the kernel theorem",
      "SOURCE_CONFIRM_ONE_FORM_SPINOR_CARRIER_AND_OBSERVATION_PULLBACK" in new["source_return"]
      and "SOURCE_SILENT_ON_RANK1280_KERNEL_MODULE" in new["source_return"])
check("type", "carrier module and selected graph trivialization remain distinct",
      any("normal-covector-spinor carrier versus compact-natural selected graph" in item
          for item in new["layer0_objects_compared"]))
check("queue", "one graph/BV problem replaces ten independent repairs",
      "Do not run ten repairs" in new["next_work_queue"][1]["why"]
      and "action- or BV-owned moving graph correction" in new["next_work_queue"][1]["why"])
check("queue", "the main source/action-owned tangent-BV frontier remains rank one",
      new["next_work_queue"][0]["rank"] == 1
      and "source/action-owned tangent or BV differential" in new["next_work_queue"][0]["why"])
check("scope", "P1 P2 P3 remain unused",
      "P1/P2/P3 remain unchanged" in new["residue"]["meter"])
check("scope", "no physical quotient is booked",
      new["residue"]["quotients_ranked"] == old["residue"]["quotients_ranked"])
check("disposition", "LT-SM3 receives only a scoped wave disposition",
      new["wave_row_dispositions"] == [{
          "row_id": "LT-SM3",
          "disposition": "TEN_PAIRWISE_DISJOINT_RANK128_DEFECTS_SUM_TO_CANONICAL_NSTAR_TENSOR_S_OBSERVATION_KERNEL__FULL_SO6_4_CARRIER_MODULE_EXACT__SELECTED_H640_GRAPH_AND_ZERO_FORM_SEED_TRIVIALIZATION_ONLY_COMPACT_NATURAL__ACTION_BV_GRAPH_CORRECTION_PHYSICAL_COHOMOLOGY_AND_DOMAIN_OPEN",
      }])

# Firing controls.
check("plant", "PLANT module typing does not change the LT-SM3 verdict",
      new_rows["LT-SM3"]["verdict"] == old_rows["LT-SM3"]["verdict"] == "DIFFERS")
check("plant", "PLANT no global quotient is invented",
      new["residue"]["canonicity_distance"]["reductions"]["applied_global"] == 0)
check("plant", "PLANT no external datum is consumed",
      "P1/P2/P3 remain unchanged" in new["residue"]["meter"])

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
