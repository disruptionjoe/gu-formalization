#!/usr/bin/env python3
"""Integrity checks for conditional physics ledger v0.62."""

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


old = strict("lab/process/conditional-physics-ledger-v0.61.json")
new = strict("lab/process/conditional-physics-ledger-v0.62.json")
registry = strict("lab/process/selected-k77-observation-jet-euler-preboundary-sufficiency.json")

check("schema", "ledger version advances once", old["schema_version"] == "0.61" and new["schema_version"] == "0.62")
check("schema", "predecessor points to v0.61", new["predecessor"].endswith("v0.61.json"))
check("meter", "coverage remains 82 of 82", new["progress"]["mapped"] == new["progress"]["total"] == 82)
check("meter", "verdict counts remain frozen", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("meter", "residue remains frozen", new["residue"] == old["residue"])
check("frontier", "two conditions close", new["frontier_delta"]["conditions_closed"] == 2)
check("frontier", "one condition opens", new["frontier_delta"]["conditions_opened"] == 1)
check("frontier", "two named conditions remain", new["frontier_delta"]["remaining_named_conditions"] == 2)
check("source", "source return names paired first variation", "PAIRED_UPSILON_XI" in new["source_return"])

old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
check("rows", "row IDs remain immutable", set(old_rows) == set(new_rows))
changed = {rid for rid in old_rows if old_rows[rid] != new_rows[rid]}
expected = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}
check("rows", "exactly five named rows migrate", changed == expected)
for rid in sorted(expected):
    check("rows", f"{rid} verdict remains frozen", new_rows[rid]["verdict"] == old_rows[rid]["verdict"])
    check("rows", f"{rid} reason kind remains frozen", new_rows[rid]["reason_kind"] == old_rows[rid]["reason_kind"])
    check("rows", f"{rid} points to v0.62 evidence", new_rows[rid]["evidence"] == "selected-k77-observation-jet-euler-preboundary-sufficiency-2026-08-07.md")

migrations = [item for item in new["migrations"]
              if item.get("from_version") == "0.61" and item.get("to_version") == "0.62"]
check("migration", "five append-only migration edges exist", {item["row_id"] for item in migrations} == expected and len(migrations) == 5)
check("registry", "null response is injective", registry["null_response"]["rank"] == 1470 and registry["null_response"]["nullity"] == 0)
check("registry", "principal symbol is live", registry["principal_symbol"]["rank"] == 650 and registry["principal_symbol"]["graph_family_rank"] == 4)
check("registry", "paired action dual remains open", registry["boundary"]["paired_upsilon_xi_equation_dual_built"] is False)
check("scope", "P1 P2 P3 remain unused", registry["p1_p2_p3"] == "UNCHANGED_AND_UNUSED")
check("scope", "no quotient is added", new["residue"]["quotients_ranked"] == 4)
check("scope", "no third lane is promoted", "THIRD_LANE" not in new["status"])

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
