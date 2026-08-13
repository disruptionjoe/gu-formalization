#!/usr/bin/env python3
"""Gate the append-only conditional physics ledger update to v0.233."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OLD_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.232.json"
NEW_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.233.json"
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
evidence = "selected-k77-i2b-minimal-covariant-reduction-action-ownership-2026-08-13.md"

check("ledger", "schema advances exactly one append-only version",
      old["schema_version"] == "0.232" and new["schema_version"] == "0.233"
      and new["predecessor"].endswith("conditional-physics-ledger-v0.232.json"))
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
check("accounting", "residue quotient and canonicity accounting remain unchanged",
      old["residue"]["continuous_real"] == new["residue"]["continuous_real"]
      and old["residue"]["function_valued_at_least"] == new["residue"]["function_valued_at_least"]
      and old["residue"]["open_discrete_forks"] == new["residue"]["open_discrete_forks"]
      and old["residue"]["quotients_ranked"] == new["residue"]["quotients_ranked"]
      and old["residue"]["canonicity_distance"] == new["residue"]["canonicity_distance"])
check("frontier", "minimal existing completions close and one nonlinear owner remains",
      new["frontier_delta"] == {
          "headline_delta": "NONE", "conditions_closed": 1,
          "conditions_opened": 0, "remaining_named_conditions": 1})
check("source", "source return records confirmation silence and repository derivation",
      "SOURCE_CONFIRMS_TWO_C32_32_HALVES" in new["source_return"]
      and "SOURCE_SILENT_OMEGA_J4_PENALTY_MULTIPLIER" in new["source_return"]
      and "REPOSITORY_DERIVES_COMPLETE_LOCAL" in new["source_return"])

compared = new["layer0_objects_compared"]
check("type", "fixed and moving reductions remain distinct",
      any("fixed omega or J4 constraint versus genuinely moving" in item
          for item in compared))
check("type", "penalty first variation and Hessian remain distinct",
      any("quadratic penalty first variation versus its nonzero Hessian" in item
          for item in compared))
check("type", "constraint rank and multiplier-field rank remain distinct",
      any("effective multiplier-field rank and constraint surplus" in item
          for item in compared))
check("type", "current carrier and every source Higgs placement remain distinct",
      any("current half-exchanging Cl1 Higgs-like carrier" in item
          for item in compared))

rank_one = new["next_work_queue"][0]["why"]
check("queue", "rank one is a nonlinear source-action owner or carrier retyping",
      "genuinely nonlinear source-action owner" in rank_one
      and "retype the carrier" in rank_one)
check("queue", "rank one forbids rerunning the exhausted minimal family",
      "Do not rerun fixed projectors, penalties or a free multiplier" in rank_one)
check("queue", "rank one demands positive constraint surplus",
      "positive constraint surplus" in rank_one)

check("disposition", "three scoped row dispositions are declared",
      {item["row_id"] for item in new["wave_row_dispositions"]} == touched)
check("migration", "three v0.232 to v0.233 migrations are append-recorded",
      sum(item.get("from_version") == "0.232" and item.get("to_version") == "0.233"
          for item in new["migration_history"]) == 3)

contract_json = load_unique(ROOT / "lab/methods/research-evidence-contract-v1.0.json")
lanes = (ROOT / "lab/process/RESEARCH-AGENDA.json").read_text(encoding="utf-8")
next_steps = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
check("pointer", "machine contract points to v0.233",
      contract_json["standing_ledger"]["ref"] == str(NEW_PATH.relative_to(ROOT)))
check("pointer", "LANES points to both v0.233 surfaces",
      "conditional-physics-ledger-v0.233.json" in lanes
      and "conditional-physics-ledger-v0.233.md" in lanes)
check("pointer", "NEXT-STEPS exposes the exhausted minimal family",
      "MINIMAL COVARIANT-REDUCTION ACTION OWNERSHIP" in next_steps
      and "zero-surplus" in next_steps and "nonlinear source-action" in next_steps)

required = [
    ROOT / "explorations/conditional-build/selected-k77-i2b-minimal-covariant-reduction-action-ownership-2026-08-13.md",
    ROOT / "lab/sources/selected-k77-i2b-minimal-covariant-reduction-action-ownership-source-return-2026-08-13.md",
    ROOT / "lab/process/hostile-reviews/2026-08-13-selected-k77-i2b-minimal-covariant-reduction-action-ownership-review.md",
    ROOT / "tests/channel-swings/selected_k77_i2b_minimal_covariant_reduction_action_ownership_probe.py",
]
check("artifact", "result source return hostile review and probe all exist",
      all(path.exists() for path in required))

check("plant", "PLANT no external datum is consumed",
      "P1/P2/P3" in new["migration_policy"] and "do not move" in new["migration_policy"])
check("plant", "PLANT no new quotient is booked",
      old["residue"]["quotients_ranked"] == new["residue"]["quotients_ranked"])
check("plant", "PLANT no universal action no-go is claimed",
      "nonlinear source-action owner" in new["progress"]["coverage_scope"])
check("plant", "PLANT no free multiplier is promoted",
      "zero local surplus" in new["progress"]["coverage_scope"])
check("plant", "PLANT no unique source Higgs is inferred",
      "unique authorial Higgs identification" in new["migration_history"][-2]["scope"])

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
