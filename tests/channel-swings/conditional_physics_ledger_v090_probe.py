#!/usr/bin/env python3
"""Append-only integrity gate for conditional physics ledger v0.90."""

from collections import Counter
from pathlib import Path
import json


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

    return json.loads(path.read_text(), object_pairs_hook=hook)


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


old = strict("lab/process/conditional-physics-ledger-v0.89.json")
new = strict("lab/process/conditional-physics-ledger-v0.90.json")
registry = strict("lab/process/signature-generic-cartan-ward-compose.json")

check("ledger", "v0.90 points to immutable v0.89", new["predecessor"].endswith("v0.89.json"))
check("ledger", "denominator is frozen", new["denominator"] == old["denominator"])
check("ledger", "row ids are frozen", [r["id"] for r in new["rows"]] == [r["id"] for r in old["rows"]])
check("ledger", "verdict counts are frozen", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("ledger", "residue and quotients are frozen", new["residue"] == old["residue"])
check("ledger", "frontier closes three and leaves two", new["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 3,
    "conditions_opened": 0,
    "remaining_named_conditions": 2,
})
check("source", "source return confirms the arena", new["source_return"] == "SOURCE-CONFIRMS")

row_ids = ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"]
tail = new["migrations"][-5:]
check("migration", "five v0.90 migrations append in declared order",
      [m["row_id"] for m in tail] == row_ids
      and all(m["from_version"] == "0.89" and m["to_version"] == "0.90" for m in tail))
for row_id in row_ids:
    before = next((r for r in old["rows"] if r.get("id") == row_id), {})
    after = next((r for r in new["rows"] if r.get("id") == row_id), {})
    check("migration", f"{row_id}: verdict and reason kind survive",
          (after.get("verdict"), after.get("reason_kind")) ==
          (before.get("verdict"), before.get("reason_kind")) and bool(before) and bool(after))
    check("migration", f"{row_id}: current evidence points to Cartan composition",
          after.get("evidence") == "signature-generic-cartan-ward-compose-2026-08-08.md")
    check("migration", f"{row_id}: frontier grade preserves selected-action burden",
          "OPEN" in after.get("frontier_grade", "") and (
              "CARTAN" in after.get("frontier_grade", "")
              or "FIELD_LIE" in after.get("frontier_grade", "")
              or "AUGMENTED_TORSION" in after.get("frontier_grade", "")
          ))

check("theorem", "connection Cartan identity is exact", registry["exact_cartan"]["connection_identity"])
check("theorem", "primitive epsilon is reused rather than rebuilt",
      registry["pure_gauge_composition"]["queue_disposition"] == "PRIMITIVE_EPSILON_ALREADY_BUILT__REMOVE_RECONSTRUCTION_DEBT")
check("branch", "K77 and K95 inertias stay distinct",
      registry["branch_controls"]["K77_inertia"] == [7, 7]
      and registry["branch_controls"]["K95_inertia"] == [9, 5])
check("branch", "Hodge operators differ and both local packets pass",
      registry["branch_controls"]["hodge_operators_equal"] is False
      and registry["branch_controls"]["K77_local_naturality"] == "PASS"
      and registry["branch_controls"]["K95_local_naturality"] == "PASS")
check("scope", "selected-action J R zero remains open",
      registry["scope_boundary"]["selected_action_coefficientwise_JR_zero"] == "OPEN")
check("scope", "no datum or residue is consumed",
      not registry["constraint_accounting"]["external_datum_used"]
      and not registry["constraint_accounting"]["residue_change"])
check("scope", "P1 P2 P3 remain unused", registry["external_datum"] == "P1_P2_P3_UNCHANGED_UNUSED")

print("SOURCE_RETURN=SOURCE-CONFIRMS")
print("FRONTIER=CARTAN_PLUS_EPSILON_COMPOSED__K77_K95_HODGE_LOCAL_EXACT__SELECTED_ACTION_FRECHET_OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
