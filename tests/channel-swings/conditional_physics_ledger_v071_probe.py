#!/usr/bin/env python3
"""Integrity checks for conditional physics ledger v0.71."""

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


old = strict("lab/process/conditional-physics-ledger-v0.70.json")
new = strict("lab/process/conditional-physics-ledger-v0.71.json")
registry = strict("lab/process/selected-k77-tilted-edge-bundle-type-bridge.json")

check("schema", "ledger version advances once", old["schema_version"] == "0.70" and new["schema_version"] == "0.71")
check("schema", "predecessor points to v0.70", new["predecessor"].endswith("v0.70.json"))
check("meter", "coverage remains 82 of 82", new["progress"]["mapped"] == new["progress"]["total"] == 82)
check("meter", "verdict counts remain frozen", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("meter", "continuous function and fork residue remain frozen",
      new["residue"]["continuous_real"] == old["residue"]["continuous_real"] == 84
      and new["residue"]["function_valued_at_least"] == old["residue"]["function_valued_at_least"]
      and new["residue"]["open_discrete_forks"] == old["residue"]["open_discrete_forks"])
check("meter", "scoped quotient count remains five",
      old["residue"]["quotients_ranked"] == new["residue"]["quotients_ranked"] == 5)
check("frontier", "two conditions close", new["frontier_delta"]["conditions_closed"] == 2)
check("frontier", "one typed bridge condition opens", new["frontier_delta"]["conditions_opened"] == 1)
check("frontier", "two named conditions remain", new["frontier_delta"]["remaining_named_conditions"] == 2)
check("frontier", "headline remains unchanged", new["frontier_delta"]["headline_delta"] == "NONE")
check("source", "source return separates confirmation from silence",
      "SOURCE-CONFIRMS" in new["source_return"] and "SOURCE-SILENT" in new["source_return"])

old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
check("rows", "row IDs remain immutable", set(old_rows) == set(new_rows))
changed = {rid for rid in old_rows if old_rows[rid] != new_rows[rid]}
expected = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}
check("rows", "exactly five named rows migrate", changed == expected)
for rid in sorted(expected):
    check("rows", f"{rid} verdict remains frozen", new_rows[rid]["verdict"] == old_rows[rid]["verdict"])
    check("rows", f"{rid} reason kind remains frozen", new_rows[rid]["reason_kind"] == old_rows[rid]["reason_kind"])
    check("rows", f"{rid} points to v0.71 evidence", new_rows[rid]["evidence"] == "selected-k77-tilted-edge-bundle-type-bridge-2026-08-08.md")
    check("rows", f"{rid} records exact tilted cocycle", "TILTED_AFFINE_COCYCLE_EXACT" in new_rows[rid]["mapping_grade"])
    check("rows", f"{rid} records killed direct identity", "DIRECT_IDENTITY_KILLED" in new_rows[rid]["mapping_grade"])
    check("rows", f"{rid} keeps typed bridge open", "BRIDGE_OPEN" in new_rows[rid]["mapping_grade"])

migrations = [item for item in new["migrations"]
              if item.get("from_version") == "0.70" and item.get("to_version") == "0.71"]
check("migration", "five append-only migration edges exist",
      {item["row_id"] for item in migrations} == expected and len(migrations) == 5)
check("registry", "tilted cocycle is exact", registry["exact_result"]["tilted_maurer_cartan_cocycle"] == "EXACT")
check("registry", "constant xi kills direct identification",
      registry["exact_result"]["constant_xi_affine_shift"] == "ZERO"
      and registry["exact_result"]["constant_xi_edge_shift"] == "NONZERO"
      and registry["exact_result"]["direct_identity_bridge"] == "KILLED")
check("registry", "natural zero-order bridge has nullity zero",
      registry["exact_result"]["zero_order_glv_vstar_to_scalar_nullity"] == 0)
check("queue", "rank one constructs the typed group-valued bridge",
      "group-valued boundary edge frame" in new["next_work_queue"][0]["why"]
      and "owned differential" in new["next_work_queue"][0]["why"])
check("scope", "no new quotient or coordinate cost is introduced",
      registry["constraint_accounting"]["new_scoped_quotients"] == 0
      and registry["constraint_accounting"]["new_boundary_coordinate_dimension"] == 0)
check("scope", "global edge and BFV constructions remain open",
      registry["construction_disposition"]["group_valued_edge_bundle_with_dressed_presymplectic_form"] == "OPEN"
      and registry["construction_disposition"]["physical_bfv_phase_space"] == "OPEN")
check("scope", "P1 P2 P3 remain unused",
      set(registry["external_datum"][key] for key in ("P1", "P2", "P3")) == {"UNUSED"})
check("scope", "no third lane is promoted", registry["program_fences"]["third_lane"] == "NOT_PROMOTED")

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
