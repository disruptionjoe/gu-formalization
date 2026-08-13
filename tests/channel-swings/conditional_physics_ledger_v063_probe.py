#!/usr/bin/env python3
"""Integrity checks for conditional physics ledger v0.63."""

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


old = strict("lab/process/conditional-physics-ledger-v0.62.json")
new = strict("lab/process/conditional-physics-ledger-v0.63.json")
registry = strict("lab/process/selected-k77-paired-upsilon-xi-green.json")

check("schema", "ledger version advances once", old["schema_version"] == "0.62" and new["schema_version"] == "0.63")
check("schema", "predecessor points to v0.62", new["predecessor"].endswith("v0.62.json"))
check("meter", "coverage remains 82 of 82", new["progress"]["mapped"] == new["progress"]["total"] == 82)
check("meter", "verdict counts remain frozen", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("meter", "residue remains frozen", new["residue"] == old["residue"])
check("frontier", "three conditions close", new["frontier_delta"]["conditions_closed"] == 3)
check("frontier", "no new condition opens", new["frontier_delta"]["conditions_opened"] == 0)
check("frontier", "two named conditions remain", new["frontier_delta"]["remaining_named_conditions"] == 2)
check("source", "source return separates printed Xi from action Euler", "REPO-SUPERSEDES" in new["source_return"] and "ACTION_OWNED_DEGREE14" in new["source_return"])

old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
check("rows", "row IDs remain immutable", set(old_rows) == set(new_rows))
changed = {rid for rid in old_rows if old_rows[rid] != new_rows[rid]}
expected = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}
check("rows", "exactly five named rows migrate", changed == expected)
for rid in sorted(expected):
    check("rows", f"{rid} verdict remains frozen", new_rows[rid]["verdict"] == old_rows[rid]["verdict"])
    check("rows", f"{rid} reason kind remains frozen", new_rows[rid]["reason_kind"] == old_rows[rid]["reason_kind"])
    check("rows", f"{rid} points to v0.63 evidence", new_rows[rid]["evidence"] == "selected-k77-paired-upsilon-xi-green-2026-08-08.md")

migrations = [item for item in new["migrations"]
              if item.get("from_version") == "0.62" and item.get("to_version") == "0.63"]
check("migration", "five append-only migration edges exist", {item["row_id"] for item in migrations} == expected and len(migrations) == 5)
check("registry", "graph and printed density degrees are separated", registry["layer0"]["exact_graph_output"].endswith("DEGREE1") and registry["layer0"]["source_printed_upsilon"].startswith("EXTERIOR_DEGREE13"))
check("registry", "printed Xi supports and family rank are exact", registry["printed_pair"]["source_xi_supports"] == [16, 15, 11, 11] and registry["printed_pair"]["source_xi_family_rank"] == 4)
check("registry", "printed Xi adds rank zero after Upsilon closure", registry["printed_pair"]["xi_independent_rank_after_upsilon_closure"] == 0)
check("registry", "action-owned Green pair remains open", registry["formal_green"]["actual_k77_krein_equation_dual"] is False and registry["formal_green"]["antisymmetrized_presymplectic_current"] is False)
check("scope", "P1 P2 P3 remain unused", registry["p1_p2_p3"] == "UNCHANGED_AND_UNUSED")
check("scope", "no quotient is added", new["residue"]["quotients_ranked"] == 4)
check("scope", "no third lane is promoted", "THIRD_LANE" not in new["status"])

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
