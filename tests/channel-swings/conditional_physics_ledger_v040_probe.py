#!/usr/bin/env python3
"""Fail-closed migration audit for conditional physics ledger v0.40."""

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

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


old = strict("lab/process/conditional-physics-ledger-v0.39.json")
new = strict("lab/process/conditional-physics-ledger-v0.40.json")
registry = strict("lab/process/selected-second-layer-tt-euler-preboundary-helicity.json")

print("A. METER AND PROGRAM FENCES")
check("exact", "schema advances 0.39 to 0.40", old["schema_version"] == "0.39" and new["schema_version"] == "0.40")
check(
    "exact",
    "denominator verdicts and coverage are frozen",
    old["denominator"] == new["denominator"]
    and old["progress"]["verdict_counts"] == new["progress"]["verdict_counts"]
    == {"SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6}
    and new["progress"]["mapped"] == new["progress"]["total"] == 82,
)
check("exact", "residue and four scoped quotients are frozen", old["residue"] == new["residue"] and new["residue"]["quotients_ranked"] == 4)
check("program", "P1 P2 P3 remain unused", registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})
check("program", "Curt and third-lane fences hold", registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and registry["third_lane_gate"] == "NOT_PROMOTED")
check("program", "no claim canon or public posture promotion", all(registry_key not in registry for registry_key in ("claim_status_change", "canon_verdict_change", "public_posture_change")))

print("\nB. APPEND-ONLY ROW MOVEMENT")
touched = ["LT-GR1", "LT-GR3", "LT-GR5", "LT-GR6"]
old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
changed = [row_id for row_id in old_rows if old_rows[row_id] != new_rows[row_id]]
check("exact", "row identities are frozen", set(old_rows) == set(new_rows))
check("exact", "exactly four named rows change", changed == touched)
for row_id in touched:
    before, after = old_rows[row_id], new_rows[row_id]
    check(
        "exact",
        f"{row_id}: verdict reason and summary are frozen",
        before["verdict"] == after["verdict"]
        and before["reason_kind"] == after["reason_kind"]
        and before["summary"] == after["summary"],
    )
    if row_id == "LT-GR1":
        check(
            "exact",
            "LT-GR1: revival trigger now names the complete constrained quotient",
            "complete constrained characteristic quotient" in after["revival_trigger"]
            and "massive spin representation" in after["revival_trigger"],
        )
    else:
        check("exact", f"{row_id}: revival trigger is frozen", before["revival_trigger"] == after["revival_trigger"])
    check("exact", f"{row_id}: evidence points to TT result", after["evidence"] == "selected-second-layer-tt-euler-preboundary-helicity-2026-08-07.md")
    check("exact", f"{row_id}: mapping records helicity two and an open boundary", "HELICITY2" in after["mapping_grade"] and "OPEN" in after["mapping_grade"])

migrations = [item for item in new["migrations"] if item.get("from_version") == "0.39" and item.get("to_version") == "0.40"]
check("exact", "four migrations are recorded in row order", [item["row_id"] for item in migrations] == touched)
check("exact", "all migrations preserve row meanings", all(item["meaning_changed"] is False for item in migrations))
check("exact", "wave dispositions name the same four rows", [item["row_id"] for item in new["wave_row_dispositions"]] == touched)
check("exact", "all row moves are distance or priority only", all("VERDICT" not in item["change"] for item in new["wave_row_dispositions"]))

print("\nC. EXACT CONSTRUCTION DISPOSITION")
coeffs = registry["coefficients"]
exact = registry["exact_results"]
check("exact", "exact fourth and second order coefficients are registered", coeffs["tt_fourth_order"] == "14356/13689" and coeffs["tt_einstein"] == "7688/13689")
check("exact", "exact mass ratio is registered", coeffs["tt_mass_squared"] == "1922/3589")
check("exact", "massless helicity and massive axial weight are separately typed", exact["massless_helicity"] == "PLUS_MINUS_TWO" and exact["massive_axial_spin_weight"] == "PLUS_MINUS_TWO__FULL_SO3_TYPE_OPEN")
check("symplectic", "preboundary current remains live", exact["preboundary"] == "NONZERO_ACTION_DERIVED_ANTISYMMETRIC_CURRENT")
check("krein", "local pole signs are opposite without positivity promotion", exact["pole_green_signs"] == "EQUAL_MAGNITUDE_OPPOSITE_SIGN" and "NO_POSITIVE_ENERGY_OR_LOOP_UNITARITY_CLAIM" in registry["boundaries"])
check("type", "rank one is the complete bosonic constraint quotient", "scalar/vector/constraint characteristic complex" in new["next_work_queue"][0]["why"])
check("type", "coupled nonzero-fermion Hessian remains rank two", "spinor Euler block" in new["next_work_queue"][1]["why"] and "nonzero-fermion Hessian" in new["next_work_queue"][1]["why"])
check("source", "explicit primary-source return is confirm plus silent", "SOURCE-CONFIRMS" in registry["source_return"] and "SOURCE-SILENT" in registry["source_return"])

for label in (
    "TT helicity two is not complete graviton recovery",
    "the massive axial TT plane is not promoted to a full SO3 representation",
    "local Green signs are not global positive energy",
    "a nonzero preboundary current is not a BFV phase space",
    "zero fermions are not the coupled matter Hessian",
    "no coefficient residue quotient or external datum is booked",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
