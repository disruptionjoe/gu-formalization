#!/usr/bin/env python3
"""Integrity checks for conditional physics ledger v0.67."""

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def strict(relative):
    path = ROOT / relative
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


old = strict("lab/process/conditional-physics-ledger-v0.66.json")
new = strict("lab/process/conditional-physics-ledger-v0.67.json")
registry = strict("lab/process/selected-k77-full-normal-owner-bank.json")

check("schema", "ledger version advances once", old["schema_version"] == "0.66" and new["schema_version"] == "0.67")
check("schema", "predecessor points to v0.66", new["predecessor"].endswith("v0.66.json"))
check("meter", "coverage remains 82 of 82", new["progress"]["mapped"] == new["progress"]["total"] == 82)
check("meter", "verdict counts remain frozen", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("meter", "residue remains frozen", new["residue"] == old["residue"])
check("frontier", "two conditions close", new["frontier_delta"]["conditions_closed"] == 2)
check("frontier", "one splitting condition opens", new["frontier_delta"]["conditions_opened"] == 1)
check("frontier", "three named conditions remain", new["frontier_delta"]["remaining_named_conditions"] == 3)
check("source", "source return separates coefficient restriction from vertical first jet",
      "VERTICAL_COEFFICIENT_RESTRICTION" in new["source_return"]
      and "VERTICAL_B_T_FIRST_JET_LIFT" in new["source_return"])

old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
check("rows", "row IDs remain immutable", set(old_rows) == set(new_rows))
changed = {rid for rid in old_rows if old_rows[rid] != new_rows[rid]}
expected = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}
check("rows", "exactly five named rows migrate", changed == expected)
for rid in sorted(expected):
    check("rows", f"{rid} verdict remains frozen", new_rows[rid]["verdict"] == old_rows[rid]["verdict"])
    check("rows", f"{rid} reason kind remains frozen", new_rows[rid]["reason_kind"] == old_rows[rid]["reason_kind"])
    check("rows", f"{rid} points to v0.67 evidence", new_rows[rid]["evidence"] == "selected-k77-full-normal-owner-bank-2026-08-08.md")
    check("rows", f"{rid} records owner-split correction", "SPLIT" in new_rows[rid]["mapping_grade"])

migrations = [item for item in new["migrations"]
              if item.get("from_version") == "0.66" and item.get("to_version") == "0.67"]
check("migration", "five append-only migration edges exist",
      {item["row_id"] for item in migrations} == expected and len(migrations) == 5)
check("registry", "ten-direction metric bank is exact", registry["exact_result"]["normal_metric_bank_rank"] == 10)
check("registry", "density rank is one", registry["exact_result"]["density_bank_rank"] == 1)
check("registry", "pairing and Hodge banks have rank ten",
      all(registry["exact_result"][key] == 10 for key in (
          "degree1_pairing_bank_rank", "degree2_pairing_bank_rank",
          "degree1_hodge_bank_rank", "degree2_hodge_bank_rank")))
check("registry", "all ten trivialization controls fire", registry["exact_result"]["trivialization_counterexamples"] == 10)
check("registry", "total covector transport is exact", registry["exact_result"]["total_covector_transport"] == "EXACT")
check("registry", "B T vertical lift remains open", registry["owner_disposition"]["B_T_normal_field_lift"] == "OPEN")
check("registry", "seven-owner split is not promoted as intrinsic",
      registry["layer0"]["seven_owner_expansion"] == "TRIVIALIZATION_DEPENDENT")
check("queue", "rank one is the splitting-change basicness test", "splitting change" in new["next_work_queue"][0]["why"])
check("scope", "no new free object is introduced", registry["external_datum"]["free_object_delta"] == 0)
check("scope", "P1 P2 P3 remain unused", set(registry["external_datum"][key] for key in ("P1", "P2", "P3")) == {"UNUSED"})
check("scope", "no quotient is added", new["residue"]["quotients_ranked"] == 4)
check("scope", "no third lane is promoted", "THIRD_LANE" not in new["status"])

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
