#!/usr/bin/env python3
"""Strict migration and scope gate for conditional physics ledger v0.210."""

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


ledger = strict("lab/process/conditional-physics-ledger-v0.210.json")
previous = strict("lab/process/conditional-physics-ledger-v0.209.json")
registry = strict("lab/process/selected-k77-i2b-radial-lc-section-qrow-composition.json")

check("schema", "version and predecessor are exact",
      ledger["schema_version"] == "0.210"
      and ledger["predecessor"].endswith("v0.209.json"))
check("coverage", "denominator and headline verdicts do not move",
      ledger["denominator"] == previous["denominator"]
      and ledger["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"])
check("frontier", "two conditions close and one scoped nonlinear condition remains",
      ledger["frontier_delta"] == {
          "headline_delta": "NONE",
          "conditions_closed": 2,
          "conditions_opened": 1,
          "remaining_named_conditions": 1,
      })
check("source", "source return separates grammar from repository calculation",
      "SOURCE_CONFIRMS" in ledger["source_return"]
      and "SOURCE_SILENT" in ledger["source_return"])

rows = {row["id"]: row for row in ledger["rows"]}
check("migration", "exactly the intended live rows cite the new result",
      all(rows[row_id]["evidence"].endswith(
          "selected-k77-i2b-radial-lc-section-qrow-composition-2026-08-12.md"
      ) for row_id in ("RA-E1", "RA-E3", "LT-SM6")))
check("scope", "RA-E1 remains NEEDS missing construction",
      rows["RA-E1"]["verdict"] == "NEEDS"
      and rows["RA-E1"]["reason_kind"] == "MISSING_CONSTRUCTION")
check("scope", "nonlinear observation and complete Euler remain explicit",
      "NONLINEAR_OBSERVATION" in rows["RA-E1"]["mapping_grade"]
      and "COMPLETE_EULER_OPEN" in rows["RA-E1"]["mapping_grade"])

new_edges = [edge for edge in ledger["migration_history"]
             if edge["to_version"] == "0.210"]
check("migration", "three append-only migration edges are present",
      {edge["row_id"] for edge in new_edges} == {"RA-E1", "RA-E3", "LT-SM6"}
      and len(new_edges) == 3)
check("migration", "every new edge preserves verdict and reason kind",
      all(edge["old"][:2] == edge["new"][:2] for edge in new_edges))
check("registry", "registry carries exact rank and grade controls",
      registry["section_q_row"]["inherits_v0208_moving_first_variation_failures"] == 0
      and registry["radial_metric_first_jet"]["radial_restriction_rank"] == 4
      and registry["radial_metric_first_jet"]["nonzero_residual_derivatives"] == 4
      and registry["radial_metric_first_jet"]["zero_action_derivatives"] == 4
      and registry["radial_metric_first_jet"]["grade_one_control"] == "8/3")
check("accounting", "residue, quotients and external data remain unchanged",
      registry["accounting"]["residue_delta"] == 0
      and registry["accounting"]["quotient_delta"] == 0
      and set(registry["accounting"]["external_datum"].values()) == {"UNUSED"})
check("plant", "PLANT local closure is rejected as complete Euler closure",
      registry["scope"]["complete_euler"] == "OPEN")

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
