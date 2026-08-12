#!/usr/bin/env python3
"""Strict migration and scope gate for conditional physics ledger v0.213."""

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


ledger = strict("lab/process/conditional-physics-ledger-v0.213.json")
previous = strict("lab/process/conditional-physics-ledger-v0.212.json")
registry = strict("lab/process/selected-k77-i2b-moving-higgs-principal-hessian.json")

check("schema", "version and predecessor are exact",
      ledger["schema_version"] == "0.213"
      and ledger["predecessor"].endswith("v0.212.json"))
check("coverage", "denominator and headline verdicts do not move",
      ledger["denominator"] == previous["denominator"]
      and ledger["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"])
check("frontier", "three exact distinctions close while two repair burdens remain",
      ledger["frontier_delta"] == {
          "headline_delta": "NONE",
          "conditions_closed": 3,
          "conditions_opened": 1,
          "remaining_named_conditions": 2,
      })
check("source", "source return separates Q_B custody from repository theorem",
      "SOURCE_CONFIRMS" in ledger["source_return"]
      and "SOURCE_SILENT" in ledger["source_return"])

rows = {row["id"]: row for row in ledger["rows"]}
check("migration", "exactly the intended live rows cite the new result",
      all(rows[row_id]["evidence"].endswith(
          "selected-k77-i2b-moving-higgs-principal-hessian-2026-08-12.md"
      ) for row_id in ("RA-E1", "RA-E3", "LT-SM6")))
check("scope", "RA-E1 remains a missing construction",
      rows["RA-E1"]["verdict"] == "NEEDS"
      and rows["RA-E1"]["reason_kind"] == "MISSING_CONSTRUCTION")
check("scope", "first Green and second Hessian are both carried",
      "FIRST_GREEN_ZERO" in rows["RA-E1"]["mapping_grade"]
      and "SECOND_PRINCIPAL_HESSIAN_RANK2" in rows["RA-E1"]["mapping_grade"])

new_edges = [edge for edge in ledger["migration_history"]
             if edge["to_version"] == "0.213"]
check("migration", "three append-only migration edges are present",
      {edge["row_id"] for edge in new_edges} == {"RA-E1", "RA-E3", "LT-SM6"}
      and len(new_edges) == 3)
check("migration", "every new edge preserves verdict and reason kind",
      all(edge["old"][:2] == edge["new"][:2] for edge in new_edges))
check("registry", "registry carries the exact Lorentz rank-two Hessian",
      registry["selected_principal_hessian"]["base_signature"] == [-1, 1, 1, 1]
      and registry["selected_principal_hessian"]["coefficient"] == 8
      and registry["selected_principal_hessian"]["internal_diagonal"] == [1, 1, 0, 0]
      and registry["selected_principal_hessian"]["nonnull_symbol_rank"] == 2)
check("registry", "the two radical responses are live and radial is included",
      registry["selected_principal_hessian"]["internal_radical_dimension"] == 2
      and registry["selected_principal_hessian"]["radical_response_supports"] == [2, 2]
      and registry["selected_principal_hessian"]["radial_direction_in_radical"] is True)
check("selector", "all eight displayed selectors fail the rank-four burden",
      max(registry["controls"]["displayed_shiab_channel_ranks"].values()) == 2
      and registry["controls"]["displayed_channel_rank_four_count"] == 0
      and registry["controls"]["first_action_principal_ranks"] == [0] * 8)
check("layer0", "carrier split subgroup and parent remain distinct",
      registry["layer0"]["carrier_split"] == "C^(32,32)+C^(32,32)"
      and registry["layer0"]["derived_block_subgroup"] == "U(32,32)xU(32,32)"
      and registry["layer0"]["full_parent"] == "U(64,64)"
      and registry["layer0"]["objects_remain_distinct"] is True)
check("accounting", "no field parameter selector quotient or datum is added",
      all(value == 0 for key, value in registry["accounting"].items()
          if key != "external_data_used")
      and registry["accounting"]["external_data_used"] == [])
check("plant", "rank-two incompleteness is not filed as no kinetic response",
      registry["controls"]["v0212_first_green_rank"] == 0
      and registry["selected_principal_hessian"]["nonnull_symbol_rank"] == 2
      and registry["selected_principal_hessian"]["radical_responses_nonzero"] is True)

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
