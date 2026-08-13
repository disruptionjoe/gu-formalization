#!/usr/bin/env python3
"""Gate the append-only conditional physics ledger update to v0.235."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OLD_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.234.json"
NEW_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.235.json"
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
evidence = "selected-k77-i2b-real-curvature-euler-image-2026-08-13.md"

check("ledger", "schema advances exactly one append-only version",
      old["schema_version"] == "0.234" and new["schema_version"] == "0.235"
      and new["predecessor"].endswith("conditional-physics-ledger-v0.234.json"))
check("ledger", "row IDs and denominator remain immutable",
      list(old_rows) == list(new_rows) and old["denominator"] == new["denominator"])
check("ledger", "only the three declared rows change",
      all(old_rows[row_id] == new_rows[row_id]
          for row_id in old_rows if row_id not in touched))
check("ledger", "touched verdicts and reason kinds remain unchanged",
      all((old_rows[row_id]["verdict"], old_rows[row_id]["reason_kind"])
          == (new_rows[row_id]["verdict"], new_rows[row_id]["reason_kind"])
          for row_id in touched))
check("ledger", "all touched rows point to the exact Euler-image evidence",
      all(new_rows[row_id]["evidence"] == evidence for row_id in touched))

check("accounting", "headline verdict counts remain unchanged",
      old["progress"]["verdict_counts"] == new["progress"]["verdict_counts"])
check("accounting", "residue quotient and canonicity accounting remain unchanged",
      old["residue"]["continuous_real"] == new["residue"]["continuous_real"]
      and old["residue"]["function_valued_at_least"] == new["residue"]["function_valued_at_least"]
      and old["residue"]["open_discrete_forks"] == new["residue"]["open_discrete_forks"]
      and old["residue"]["quotients_ranked"] == new["residue"]["quotients_ranked"]
      and old["residue"]["canonicity_distance"] == new["residue"]["canonicity_distance"])
check("frontier", "one pointwise route closes and three routes remain",
      new["frontier_delta"] == {
          "headline_delta": "NONE", "conditions_closed": 1,
          "conditions_opened": 0, "remaining_named_conditions": 3})
check("source", "source return types the parent halves and derivative-jet silence",
      "SOURCE_CONFIRMS_I2B_FULL_U64_64_PARENT_AND_TWO_C32_32_HALVES" in new["source_return"]
      and "SOURCE_SILENT_DERIVATIVE_DEPENDENT_REAL_BACKGROUND_JET" in new["source_return"])

compared = new["layer0_objects_compared"]
check("type", "pointwise curvature values and derivative jets remain distinct",
      any("pointwise real full-U(64,64) curvature values" in item for item in compared))
check("type", "residual and Euler images remain distinct",
      any("curvature residual image versus its exact Euler" in item for item in compared))
check("type", "complex control and real solution remain distinct",
      any("unrestricted complex target preimage" in item for item in compared))

rank_one = new["next_work_queue"][0]["why"]
for route in ("derivative-dependent real source-connection jet", "nonzero-fermion", "full-field BV"):
    check("queue", f"rank one preserves the {route} route", route in rank_one)
check("queue", "rank one forbids another pointwise curvature-value search",
      "Do not search another pointwise curvature/background value" in rank_one)
check("queue", "rank one carries the Bianchi/descent burden",
      "Bianchi/descent" in rank_one)

check("disposition", "three scoped row dispositions are declared",
      {item["row_id"] for item in new["wave_row_dispositions"]} == touched)
check("migration", "three v0.234 to v0.235 migrations are append-recorded",
      sum(item.get("from_version") == "0.234" and item.get("to_version") == "0.235"
          for item in new["migration_history"]) == 3)

required = [
    ROOT / "explorations/conditional-build/selected-k77-i2b-real-curvature-euler-image-2026-08-13.md",
    ROOT / "lab/sources/selected-k77-i2b-real-curvature-euler-image-source-return-2026-08-13.md",
    ROOT / "lab/process/hostile-reviews/2026-08-13-selected-k77-i2b-real-curvature-euler-image-review.md",
    ROOT / "tests/channel-swings/selected_k77_i2b_real_curvature_euler_image_probe.py",
]
check("artifact", "result source return hostile review and probe all exist",
      all(path.exists() for path in required))

check("plant", "PLANT no external datum is consumed",
      "P1/P2/P3" in new["migration_policy"] and "do not move" in new["migration_policy"])
check("plant", "PLANT no new quotient or residue is booked",
      old["residue"]["continuous_real"] == new["residue"]["continuous_real"]
      and old["residue"]["quotients_ranked"] == new["residue"]["quotients_ranked"])
check("plant", "PLANT no full GU action no-go is claimed",
      "full GU action remains open" in new["progress"]["coverage_scope"])
check("plant", "PLANT complex solvability is not called a real solution",
      "complex" in new_rows["LT-SM6"]["distance"] and "no admissible real preimage" in new_rows["LT-SM6"]["distance"])
check("plant", "PLANT the block subgroup is not confused with the carrier halves",
      "C^(32,32)+C^(32,32)" in new_rows["RA-E3"]["distance"] and "block subgroup" in new_rows["RA-E3"]["distance"])

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
