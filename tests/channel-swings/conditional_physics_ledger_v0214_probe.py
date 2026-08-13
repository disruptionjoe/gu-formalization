#!/usr/bin/env python3
"""Strict migration and scope gate for conditional physics ledger v0.214."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative: str):
    def reject(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key}")
            result[key] = value
        return result
    return json.loads((ROOT / relative).read_text(encoding="utf-8"),
                      object_pairs_hook=reject)


ledger = strict("lab/process/conditional-physics-ledger-v0.214.json")
previous = strict("lab/process/conditional-physics-ledger-v0.213.json")
registry = strict("lab/process/selected-k77-i2b-real-primalizer-phase-gate.json")

check("schema", "version and predecessor are exact",
      ledger["schema_version"] == "0.214"
      and ledger["predecessor"].endswith("v0.213.json"))
check("coverage", "denominator and headline verdicts do not move",
      ledger["denominator"] == previous["denominator"]
      and ledger["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"])
check("frontier", "four distinctions close while two ownership routes remain",
      ledger["frontier_delta"] == {
          "headline_delta": "NONE",
          "conditions_closed": 4,
          "conditions_opened": 1,
          "remaining_named_conditions": 2,
      })
check("source", "source return separates norm ownership from Q_B silence",
      "SOURCE_CONFIRMS" in ledger["source_return"]
      and "SOURCE_SILENT" in ledger["source_return"])

rows = {row["id"]: row for row in ledger["rows"]}
check("migration", "exactly the intended live rows cite the new result",
      all(rows[row_id]["evidence"].endswith(
          "selected-k77-i2b-real-primalizer-phase-gate-2026-08-12.md"
      ) for row_id in ("RA-E1", "RA-E3", "LT-SM6")))
check("scope", "RA-E1 remains a missing construction",
      rows["RA-E1"]["verdict"] == "NEEDS"
      and rows["RA-E1"]["reason_kind"] == "MISSING_CONSTRUCTION")
check("scope", "conditional rank four and action-ownership burden both travel",
      "PHASE_EVEN_QB_RANK4_CONDITIONAL" in rows["RA-E1"]["mapping_grade"]
      and "MOVING_REDUCTION_CONTACT_PARENT" in rows["RA-E1"]["mapping_grade"])

new_edges = [edge for edge in ledger["migration_history"]
             if edge["to_version"] == "0.214"]
check("migration", "three append-only migration edges are present",
      {edge["row_id"] for edge in new_edges} == {"RA-E1", "RA-E3", "LT-SM6"}
      and len(new_edges) == 3)
check("migration", "every new edge preserves verdict and reason kind",
      all(edge["old"][:2] == edge["new"][:2] for edge in new_edges))
check("registry", "current pairing and phase-even candidate ranks are exact",
      registry["exact_results"]["current_nonnull_rank"] == 2
      and registry["exact_results"]["phase_even_nonnull_rank"] == 4
      and registry["exact_results"]["phase_even_null_rank"] == 0)
check("registry", "action-owned real projectors do not repair",
      registry["exact_results"]["pplus_ranks_by_base_direction"] == [2, 2, 2, 2]
      and registry["exact_results"]["pminus_ranks_by_base_direction"] == [2, 2, 2, 2])
check("weyl", "two-half scalar weights cannot repair the grade-two block",
      registry["exact_results"]["weyl_half_trace_difference_failures"] == 0
      and registry["exact_results"]["two_half_scalar_weight_max_rank"] == 2)
check("unitary", "phase-even candidate fails the noncompact-unitary plant",
      registry["exact_results"]["u11_phase_even_values"] == ["1", "1681/81"]
      and registry["exact_results"]["phase_even_full_or_block_unitary_invariant"] is False)
check("layer0", "carrier split subgroup and parent remain distinct",
      registry["layer0"]["carrier_halves"] == "C^(32,32)+C^(32,32)"
      and registry["layer0"]["derived_block_subgroup"] == "U(32,32)xU(32,32)"
      and registry["layer0"]["full_parent"] == "U(64,64)")
check("accounting", "no field parameter selector quotient or datum is added",
      all(registry["constraint_accounting"][key] == 0 for key in (
          "new_fields", "new_parameters", "new_data", "new_quotients",
          "new_promoted_selectors"
      )))
check("plant", "rank-four existence is not reported as action selection",
      registry["classification"]["rank_four_candidate_exists"] is True
      and registry["classification"]["candidate_is_source_selected"] is False
      and registry["classification"]["moving_reduction_or_fundamental_symmetry_required"] is True)

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
