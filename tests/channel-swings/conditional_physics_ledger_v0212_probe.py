#!/usr/bin/env python3
"""Strict migration and scope gate for conditional physics ledger v0.212."""

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


ledger = strict("lab/process/conditional-physics-ledger-v0.212.json")
previous = strict("lab/process/conditional-physics-ledger-v0.211.json")
registry = strict("lab/process/selected-k77-i2b-arbitrary-field-euler-green-bank.json")

check("schema", "version and predecessor are exact",
      ledger["schema_version"] == "0.212"
      and ledger["predecessor"].endswith("v0.211.json"))
check("coverage", "denominator and headline verdicts do not move",
      ledger["denominator"] == previous["denominator"]
      and ledger["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"])
check("frontier", "Euler and Green close while two kinetic routes remain",
      ledger["frontier_delta"] == {
          "headline_delta": "NONE",
          "conditions_closed": 2,
          "conditions_opened": 1,
          "remaining_named_conditions": 2,
      })
check("source", "source return separates source arena from repository theorem",
      "SOURCE_CONFIRMS" in ledger["source_return"]
      and "SOURCE_SILENT" in ledger["source_return"])

rows = {row["id"]: row for row in ledger["rows"]}
check("migration", "exactly the intended live rows cite the new result",
      all(rows[row_id]["evidence"].endswith(
          "selected-k77-i2b-arbitrary-field-euler-green-bank-2026-08-12.md"
      ) for row_id in ("RA-E1", "RA-E3", "LT-SM6")))
check("scope", "RA-E1 remains a missing construction",
      rows["RA-E1"]["verdict"] == "NEEDS"
      and rows["RA-E1"]["reason_kind"] == "MISSING_CONSTRUCTION")
check("scope", "Euler rank and zero Green are both carried",
      "EULER_RANK3" in rows["RA-E1"]["mapping_grade"]
      and "PRINCIPAL_GREEN_ZERO" in rows["RA-E1"]["mapping_grade"])

new_edges = [edge for edge in ledger["migration_history"]
             if edge["to_version"] == "0.212"]
check("migration", "three append-only migration edges are present",
      {edge["row_id"] for edge in new_edges} == {"RA-E1", "RA-E3", "LT-SM6"}
      and len(new_edges) == 3)
check("migration", "every new edge preserves verdict and reason kind",
      all(edge["old"][:2] == edge["new"][:2] for edge in new_edges))
check("registry", "registry carries the exact arbitrary Euler theorem",
      registry["field_bank"]["real_dimension"] == 196
      and registry["field_bank"]["euler_supports"] == [14, 12, 12, 2]
      and registry["field_bank"]["euler_family_rank"] == 3)
check("registry", "principal operator is live while physical Green is zero",
      registry["green_bank"]["principal_operator_nonzero"] is True
      and registry["green_bank"]["principal_self_pairing_witness_each_direction"] is True
      and registry["green_bank"]["S_q_supports"] == [0, 0, 0, 0]
      and registry["green_bank"]["H_q_supports"] == [0, 0, 0, 0]
      and registry["green_bank"]["physical_row_rank"] == 0)
check("receiver", "generic Euler reaches and reconstructs both receiver sides",
      registry["receiver"]["observed_nonzero"] is True
      and registry["receiver"]["normal_nonzero"] is True
      and registry["receiver"]["observed_plus_normal_reconstructs"] is True)
check("accounting", "no field, parameter, selector or datum is added",
      all(value == 0 for key, value in registry["accounting"].items()
          if key != "external_data_used")
      and registry["accounting"]["external_data_used"] == [])
check("plant", "zero Green is not filed as a zero principal operator or global no-go",
      registry["green_bank"]["off_family_nonzero_control"] is True
      and "moving metric" in registry["scope"]["open"][0]
      and "expanded action-parent" in registry["scope"]["open"][1])

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
