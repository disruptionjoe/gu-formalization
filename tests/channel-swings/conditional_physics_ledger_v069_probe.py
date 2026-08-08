#!/usr/bin/env python3
"""Integrity checks for conditional physics ledger v0.69."""

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


old = strict("lab/process/conditional-physics-ledger-v0.68.json")
new = strict("lab/process/conditional-physics-ledger-v0.69.json")
registry = strict("lab/process/selected-k77-contact-presymplectic-gauge-basicness.json")

check("schema", "ledger version advances once", old["schema_version"] == "0.68" and new["schema_version"] == "0.69")
check("schema", "predecessor points to v0.68", new["predecessor"].endswith("v0.68.json"))
check("meter", "coverage remains 82 of 82", new["progress"]["mapped"] == new["progress"]["total"] == 82)
check("meter", "verdict counts remain frozen", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("meter", "residue remains frozen", new["residue"] == old["residue"])
check("frontier", "two conditions close", new["frontier_delta"]["conditions_closed"] == 2)
check("frontier", "one boundary condition opens", new["frontier_delta"]["conditions_opened"] == 1)
check("frontier", "two named conditions remain", new["frontier_delta"]["remaining_named_conditions"] == 2)
check(
    "source",
    "source return separates silence from repo-derived boundary moment map",
    "SOURCE-SILENT" in new["source_return"]
    and "REPO-DERIVES" in new["source_return"]
    and "BOUNDARY_MOMENT_MAP" in new["source_return"],
)

old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
check("rows", "row IDs remain immutable", set(old_rows) == set(new_rows))
changed = {rid for rid in old_rows if old_rows[rid] != new_rows[rid]}
expected = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}
check("rows", "exactly five named rows migrate", changed == expected)
for rid in sorted(expected):
    check("rows", f"{rid} verdict remains frozen", new_rows[rid]["verdict"] == old_rows[rid]["verdict"])
    check("rows", f"{rid} reason kind remains frozen", new_rows[rid]["reason_kind"] == old_rows[rid]["reason_kind"])
    check("rows", f"{rid} points to v0.69 evidence", new_rows[rid]["evidence"] == "selected-k77-contact-presymplectic-gauge-basicness-2026-08-08.md")
    check("rows", f"{rid} records small-gauge basicness", "SMALL_GAUGE_BASIC" in new_rows[rid]["mapping_grade"])
    check("rows", f"{rid} keeps boundary reduction open", "BOUNDARY" in new_rows[rid]["mapping_grade"])

migrations = [
    item
    for item in new["migrations"]
    if item.get("from_version") == "0.68" and item.get("to_version") == "0.69"
]
check(
    "migration",
    "five append-only migration edges exist",
    {item["row_id"] for item in migrations} == expected and len(migrations) == 5,
)
check("registry", "actual Levi-Civita contact symbol has rank ten", registry["exact_result"]["spin_levi_civita_symbol_rank"] == 10)
check("registry", "diagonal two-connection Ward kernel is rank ten", registry["exact_result"]["diagonal_contact_kernel_dimension"] == 10)
check("registry", "small gauge contracts to zero", registry["exact_result"]["small_gauge_contraction"] == "ZERO")
check("registry", "fixed-gauge Lie derivative vanishes", registry["exact_result"]["all_fixed_gauge_lie_derivative"] == "ZERO")
check("registry", "boundary contraction is a live moment-map derivative", "MOMENT_MAP" in registry["exact_result"]["unrestricted_boundary_contraction"])
check("registry", "all ten K77 boundary charges are live", registry["exact_result"]["k77_normal_boundary_charges_nonzero"] == 10)
check("queue", "rank one is boundary-domain or edge-mode selection", "boundary gauge domain" in new["next_work_queue"][0]["why"] and "edge-mode" in new["next_work_queue"][0]["why"])
check("scope", "physical boundary condition remains unselected", not registry["constraint_accounting"]["boundary_condition_selected"])
check("scope", "no edge mode has been inserted", not registry["constraint_accounting"]["edge_mode_added"])
check("scope", "no new free object is introduced", registry["external_datum"]["free_object_delta"] == 0)
check("scope", "P1 P2 P3 remain unused", set(registry["external_datum"][key] for key in ("P1", "P2", "P3")) == {"UNUSED"})
check("scope", "no quotient is added", new["residue"]["quotients_ranked"] == 4)
check("scope", "no third lane is promoted", registry["program_fences"]["third_lane"] == "NOT_PROMOTED")

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
