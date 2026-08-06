#!/usr/bin/env python3
"""Machine check for conditional-physics ledger v0.21."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
FAILURES = []
COUNT = 0


def strict(path):
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=hook)


def check(label, condition):
    global COUNT
    COUNT += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} {label}")
    if not ok:
        FAILURES.append(label)


ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.21.json")
prior = strict(ROOT / "lab/process/conditional-physics-ledger-v0.20.json")
registry = strict(ROOT / "lab/process/selected-cubic-gauge-rotated-lc-ward-owner.json")
rows = {row["id"]: row for row in ledger["rows"] if row.get("row_status") != "SUPERSEDED"}
prior_rows = {row["id"]: row for row in prior["rows"] if row.get("row_status") != "SUPERSEDED"}
touched = ["LT-GR1", "LT-GR2b", "LT-GR5", "LT-GR6", "LT-SM8"]

check("version and predecessor", ledger["schema_version"] == "0.21" and ledger["predecessor"].endswith("v0.20.json"))
check("denominator frozen", ledger["denominator"] == prior["denominator"])
check("coverage frozen", ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("verdict counts frozen", ledger["progress"]["verdict_counts"] == prior["progress"]["verdict_counts"])
check("residue frozen", ledger["residue"] == prior["residue"])
check("five touched rows exact", registry["ledger_rows"] == touched)
check("all untouched rows object-equivalent", all(rows[row_id] == prior_rows[row_id] for row_id in rows if row_id not in touched))
check("all five verdicts frozen", all(rows[row_id]["verdict"] == prior_rows[row_id]["verdict"] for row_id in touched))
check("all five reason kinds frozen", all(rows[row_id]["reason_kind"] == prior_rows[row_id]["reason_kind"] for row_id in touched))
check("all five distances moved", all(rows[row_id]["distance"] != prior_rows[row_id]["distance"] for row_id in touched))
check("all five evidence pointers moved", all(rows[row_id]["evidence"] == "selected-cubic-gauge-rotated-lc-ward-owner-2026-08-06.md" for row_id in touched))
check("LT-GR3 deliberately unchanged", rows["LT-GR3"] == prior_rows["LT-GR3"])
check("LT-GR2b separates intrinsic zero from LC nonzero", "INTRINSIC_DISTORTION_Q0QM_ZERO" in rows["LT-GR2b"]["mapping_grade"] and "LC_FIRST_JET_Q0QM_REPRESENTATIVE_NONZERO" in rows["LT-GR2b"]["mapping_grade"])
check("LT-GR1 records second-jet and Ward boundaries", "SECOND_JET_T_ONLY_RADIAL_CHANNEL_ZERO" in rows["LT-GR1"]["mapping_grade"] and "GAUGE_GAUGE_RANK5" in rows["LT-GR1"]["mapping_grade"])
check("LT-SM8 stays missing construction", rows["LT-SM8"]["reason_kind"] == "MISSING_CONSTRUCTION")
migrations = [m for m in ledger["migrations"] if m["from_version"] == "0.20" and m["to_version"] == "0.21"]
check("five append-only migrations", [m["row_id"] for m in migrations] == touched)
check("no meaning changed", all(m["meaning_changed"] is False for m in migrations))
check("migration old triples match predecessor", all(m["old"] == [prior_rows[m["row_id"]]["verdict"], prior_rows[m["row_id"]]["reason_kind"], prior_rows[m["row_id"]]["mapping_grade"]] for m in migrations))
check("migration new triples match successor", all(m["new"] == [rows[m["row_id"]]["verdict"], rows[m["row_id"]]["reason_kind"], rows[m["row_id"]]["mapping_grade"]] for m in migrations))
check("rank one fuses LC and Ward", ledger["next_work_queue"][0]["rows"] == ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"] and "rank-five gauge-gauge block" in ledger["next_work_queue"][0]["why"] and "co-moving epsilon/Ward" in ledger["next_work_queue"][0]["why"])
check("rank two remains shared Higgs chirality gate", ledger["next_work_queue"][1]["rows"] == ["RA-D2", "RA-G2", "RA-E3", "RA-E5"])
check("external datum unused", registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})

check("PLANT source confirms owner only", registry["source_return"] == "SOURCE-CONFIRMS" and "NOT_COEFFICIENT_OR_QUOTIENT" in registry["source_scope"])
check("PLANT nonzero is not quotient", registry["quotient_test"]["disposition"] == "NONZERO_REPRESENTATIVE_WARD_REQUIRED")
check("PLANT no fifth quotient", ledger["residue"]["quotients_ranked"] == 4 and registry["quotient_test"]["fifth_quotient"] == "NOT_COUNTED")
check("PLANT no LT-GR3 migration", all(m["row_id"] != "LT-GR3" for m in migrations))
check("PLANT zero new construction cost", registry["cost"] == {"new_fields": 0, "new_coefficients": 0, "new_selectors": 0, "new_real_form_identifications": 0})

if FAILURES:
    print("FAILURES", FAILURES)
    raise SystemExit(1)
print(f"PASS: {COUNT}/{COUNT}")
