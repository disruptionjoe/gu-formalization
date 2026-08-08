#!/usr/bin/env python3
"""Integrity checks for conditional physics ledger v0.76."""

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


old = strict("lab/process/conditional-physics-ledger-v0.75.json")
new = strict("lab/process/conditional-physics-ledger-v0.76.json")
registry = strict("lab/process/selected-k77-action-boundary-coefficient-bank.json")

check("schema", "ledger advances once", old["schema_version"] == "0.75" and new["schema_version"] == "0.76")
check("schema", "predecessor is v0.75", new["predecessor"].endswith("v0.75.json"))
check("meter", "coverage remains 82 of 82", new["progress"]["mapped"] == new["progress"]["total"] == 82)
check("meter", "verdict counts remain frozen", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("meter", "residue remains frozen",
      new["residue"]["continuous_real"] == old["residue"]["continuous_real"] == 84
      and new["residue"]["function_valued_at_least"] == old["residue"]["function_valued_at_least"]
      and new["residue"]["open_discrete_forks"] == old["residue"]["open_discrete_forks"])
check("meter", "five scoped quotients remain", new["residue"]["quotients_ranked"] == old["residue"]["quotients_ranked"] == 5)
check("frontier", "frontier delta is 3 closed 1 opened 2 remaining",
      new["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3,
                                "conditions_opened": 1, "remaining_named_conditions": 2})
check("source", "source return types confirmation silence and repo derivation",
      all(marker in new["source_return"] for marker in ("SOURCE-CONFIRMS", "SOURCE-SILENT", "REPO-DERIVES")))

old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
expected = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}
check("rows", "row IDs remain immutable", set(old_rows) == set(new_rows))
check("rows", "exactly five named rows migrate",
      {rid for rid in old_rows if old_rows[rid] != new_rows[rid]} == expected)
for rid in sorted(expected):
    check("rows", f"{rid} verdict remains frozen", new_rows[rid]["verdict"] == old_rows[rid]["verdict"])
    check("rows", f"{rid} reason kind remains frozen", new_rows[rid]["reason_kind"] == old_rows[rid]["reason_kind"])
    check("rows", f"{rid} points to v0.76 evidence",
          new_rows[rid]["evidence"] == "selected-k77-action-boundary-coefficient-bank-2026-08-08.md")
    check("rows", f"{rid} preserves arbitrary-K rejection",
          "P_EQUALS_KT_ACTION_OWNER_REJECTED" in new_rows[rid]["mapping_grade"])
    check("rows", f"{rid} records exact rank-ten action bank",
          "SELECTED_CL1_CL2_ACTION_BANK_RANK10_EXACT" in new_rows[rid]["mapping_grade"])
    check("rows", f"{rid} retains a full/global open fence",
          "OPEN" in new_rows[rid]["mapping_grade"])

migrations = [item for item in new["migrations"]
              if item.get("from_version") == "0.75" and item.get("to_version") == "0.76"]
check("migration", "five append-only migration edges exist",
      len(migrations) == 5 and {item["row_id"] for item in migrations} == expected)
check("registry", "full and normal action ranks are exact",
      registry["exact_results"]["full_bank_rank"] == 14
      and registry["exact_results"]["normal_bank_rank"] == 10)
check("registry", "complete observation is exact and lossless",
      registry["exact_results"]["observation_inverse_exact"] is True
      and registry["exact_results"]["observed_bank_rank"] == 14
      and registry["exact_results"]["observed_normal_rank"] == 10)
check("registry", "raw and observed images are nondegenerate and indefinite",
      registry["exact_results"]["raw_normal_gram_inertia"] == [4, 6, 0]
      and registry["exact_results"]["observed_normal_gram_inertia"] == [5, 5, 0])
check("registry", "normal support fingerprint is frozen",
      registry["exact_results"]["normal_supports"] == [13, 14, 12, 16, 13, 16, 13, 12, 5, 8])
check("registry", "endpoint orientation and independence remain explicit",
      registry["exact_results"]["endpoint_orientation_opposite"] is True
      and registry["exact_results"]["endpoint_banks_independent"] is True)
check("queue", "rank one is full/global extension",
      "full coefficient and bundle carrier" in new["next_work_queue"][0]["why"])
check("scope", "no constraint-accounting movement",
      set(registry["constraint_fence"].values()) <= {0, "UNUSED"})
check("scope", "full coefficient, global BFV and common domain remain fenced",
      any("U(64,64)" in item for item in registry["boundary"])
      and any("BFV" in item for item in registry["boundary"])
      and any("domain" in item for item in registry["boundary"]))

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

