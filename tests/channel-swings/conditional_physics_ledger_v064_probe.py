#!/usr/bin/env python3
"""Integrity checks for conditional physics ledger v0.64."""

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


old = strict("lab/process/conditional-physics-ledger-v0.63.json")
new = strict("lab/process/conditional-physics-ledger-v0.64.json")
registry = strict("lab/process/selected-k77-action-owned-degree14-companion.json")

check("schema", "ledger version advances once", old["schema_version"] == "0.63" and new["schema_version"] == "0.64")
check("schema", "predecessor points to v0.63", new["predecessor"].endswith("v0.63.json"))
check("meter", "coverage remains 82 of 82", new["progress"]["mapped"] == new["progress"]["total"] == 82)
check("meter", "verdict counts remain frozen", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("meter", "residue remains frozen", new["residue"] == old["residue"])
check("frontier", "one condition closes", new["frontier_delta"]["conditions_closed"] == 1)
check("frontier", "no new condition opens", new["frontier_delta"]["conditions_opened"] == 0)
check("frontier", "one named condition remains", new["frontier_delta"]["remaining_named_conditions"] == 1)
check("source", "source return separates printed Xi from the derived action companion",
      "PRINTED_XI" in new["source_return"] and "ACTION_COMPANION_EQUALS" in new["source_return"])

old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
check("rows", "row IDs remain immutable", set(old_rows) == set(new_rows))
changed = {rid for rid in old_rows if old_rows[rid] != new_rows[rid]}
expected = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}
check("rows", "exactly five named rows migrate", changed == expected)
for rid in sorted(expected):
    check("rows", f"{rid} verdict remains frozen", new_rows[rid]["verdict"] == old_rows[rid]["verdict"])
    check("rows", f"{rid} reason kind remains frozen", new_rows[rid]["reason_kind"] == old_rows[rid]["reason_kind"])
    check("rows", f"{rid} points to v0.64 evidence", new_rows[rid]["evidence"] == "selected-k77-action-owned-degree14-companion-2026-08-08.md")

migrations = [item for item in new["migrations"]
              if item.get("from_version") == "0.63" and item.get("to_version") == "0.64"]
check("migration", "five append-only migration edges exist",
      {item["row_id"] for item in migrations} == expected and len(migrations) == 5)
check("registry", "the action companion uses both Euler owners plus moving Shiab",
      registry["layer0"]["action_companion"] == "D_B_ADJOINT_E_B_MINUS_E_T_PLUS_D_EPSILON_SHIAB_ADJOINT_K_S")
check("registry", "all nine epsilon units pass", registry["exact_fixture"]["all_nine_epsilon_units"] is True)
check("registry", "all three action pieces remain live",
      all(registry["exact_fixture"][key] is True for key in ("e_b_live", "e_t_live", "moving_shiab_live")))
check("registry", "naive D_A E_T is rejected", registry["exact_fixture"]["naive_d_a_e_t_rejected_both_signs"] is True)
check("registry", "moving observation and symplectic owners remain open",
      registry["open"]["moving_hodge_krein_section_target_green"] is True
      and registry["open"]["antisymmetrized_presymplectic_current"] is True)
check("scope", "P1 P2 P3 remain unused", registry["p1_p2_p3"] == "UNCHANGED_AND_UNUSED")
check("scope", "no quotient is added", new["residue"]["quotients_ranked"] == 4)
check("scope", "no third lane is promoted", "THIRD_LANE" not in new["status"])

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
