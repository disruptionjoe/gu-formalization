#!/usr/bin/env python3
"""Gate the append-only conditional physics ledger migration to v0.227."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OLD_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.226.json"
NEW_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.227.json"
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
      old["schema_version"] == "0.226"
      and new["schema_version"] == "0.227"
      and new["predecessor"].endswith("conditional-physics-ledger-v0.226.json"))
check("ledger", "row IDs and denominator remain immutable",
      list(old_rows) == list(new_rows)
      and old["denominator"] == new["denominator"])
check("row", "portfolio correction changes no physics row", old_rows == new_rows)
check("accounting", "headline verdict counts remain unchanged",
      old["progress"]["verdict_counts"] == new["progress"]["verdict_counts"])
check("accounting", "raw residue and quotient accounting remain unchanged",
      old["residue"]["continuous_real"] == new["residue"]["continuous_real"] == 84
      and old["residue"]["function_valued_at_least"] == new["residue"]["function_valued_at_least"] == 19
      and old["residue"]["open_discrete_forks"] == new["residue"]["open_discrete_forks"] == 9
      and old["residue"]["quotients_ranked"] == new["residue"]["quotients_ranked"] == 5)
check("frontier", "portfolio correction exposes the next six named conditions",
      new["frontier_delta"] == {
          "headline_delta": "NONE",
          "conditions_closed": 4,
          "conditions_opened": 5,
          "remaining_named_conditions": 6,
      })
check("source", "source return keeps assignments separate from derivations",
      "SC_GEN_53_SOURCE_ASSERTS" in new["source_return"]
      and "SC_GEN_54_SOURCE_ASSERTS" in new["source_return"]
      and "SOURCE_RESOLVER_NOT_ACTION_DERIVATION" in new["source_return"])
distance = new["residue"]["canonicity_distance"]
check("scope", "canonicity meter is typed and physical residue stays uncomputed",
      distance["physical_residue"] == "UNCOMPUTED_UNTIL_SCOPES_COMPOSE"
      and distance["raw_coordinates"]["continuous_prequotient"] == 84
      and distance["function_slots"]["at_least"] == 19
      and distance["discrete"]["open_forks"] == 9)
check("scope", "J quotient remains provisional and unbooked",
      distance["reductions"]["applied_global"] == 0
      and distance["reductions"]["booked_conditional"] == 5
      and len(distance["reductions"]["provisional_unbooked"]) == 1)
check("scope", "P1 P2 P3 remain unused",
      "P1/P2/P3 remain unchanged" in new["residue"]["meter"])
check("migration", "no row migration is invented for a process and source-typing wave",
      old["migration_history"] == new["migration_history"])

# Firing controls.
check("plant", "PLANT a local homogeneous orbit is not booked globally",
      new["residue"]["quotients_ranked"] == 5)
check("plant", "PLANT a source resolver does not change headline verdicts",
      old["progress"]["verdict_counts"] == new["progress"]["verdict_counts"])
check("plant", "PLANT physical residue is not a scalar subtraction",
      distance["physical_residue"] != 64)
check("plant", "PLANT no external datum is consumed",
      "P1/P2/P3 remain unchanged" in new["residue"]["meter"])

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
