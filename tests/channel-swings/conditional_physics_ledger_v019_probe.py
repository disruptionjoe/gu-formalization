#!/usr/bin/env python3
"""Machine check for conditional-physics ledger v0.19."""

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


ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.19.json")
prior = strict(ROOT / "lab/process/conditional-physics-ledger-v0.18.json")
registry = strict(ROOT / "lab/process/trace-omega-higgs-chirality-compose-reconciliation.json")
rows = {row["id"]: row for row in ledger["rows"] if row.get("row_status") != "SUPERSEDED"}
prior_rows = {row["id"]: row for row in prior["rows"] if row.get("row_status") != "SUPERSEDED"}
touched = ["RA-D2", "RA-G2", "RA-E3", "RA-E5"]

check("version and predecessor", ledger["schema_version"] == "0.19" and ledger["predecessor"].endswith("v0.18.json"))
check("denominator frozen", ledger["denominator"] == prior["denominator"])
check("coverage frozen", ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("verdict counts frozen", ledger["progress"]["verdict_counts"] == prior["progress"]["verdict_counts"])
check("residue frozen", ledger["residue"] == prior["residue"])
check("four touched rows exact", registry["touched_rows"] == touched)
check("all untouched rows byte-equivalent as objects",
      all(rows[row_id] == prior_rows[row_id] for row_id in rows if row_id not in touched))
check("all four verdicts frozen", all(rows[row_id]["verdict"] == prior_rows[row_id]["verdict"] for row_id in touched))
check("all four reason kinds frozen", all(rows[row_id]["reason_kind"] == prior_rows[row_id]["reason_kind"] for row_id in touched))
check("all four distances moved", all(rows[row_id]["distance"] != prior_rows[row_id]["distance"] for row_id in touched))
check("all four evidence pointers moved", all(rows[row_id]["evidence"] == "trace-omega-higgs-chirality-compose-reconciliation-2026-08-05.md" for row_id in touched))
check("RA-D2 falsification preserved", rows["RA-D2"]["reason_kind"] == "GENUINE_FALSIFICATION")
check("RA-E3 revival trigger becomes cell-specific", "varpi one-form cell" in rows["RA-E3"]["revival_trigger"])
migrations = [m for m in ledger["migrations"] if m["from_version"] == "0.18" and m["to_version"] == "0.19"]
check("four append-only migrations", [m["row_id"] for m in migrations] == touched)
check("no meaning changed", all(m["meaning_changed"] is False for m in migrations))
check("migration old triples match predecessor", all(m["old"] == [prior_rows[m["row_id"]]["verdict"], prior_rows[m["row_id"]]["reason_kind"], prior_rows[m["row_id"]]["mapping_grade"]] for m in migrations))
check("migration new triples match successor", all(m["new"] == [rows[m["row_id"]]["verdict"], rows[m["row_id"]]["reason_kind"], rows[m["row_id"]]["mapping_grade"]] for m in migrations))
check("rank one remains moving D3I", ledger["next_work_queue"][0]["rows"] == ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"])
check("rank two is shared four-row gate", ledger["next_work_queue"][1]["rows"] == touched)
check("external datum unused", registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})

check("PLANT bare q is not called the Higgs", registry["boundaries"]["q_role"] == "CANONICAL_EVALUATION_INPUT_NOT_HIGGS")
check("PLANT physical quotient remains open", registry["boundaries"]["physical_bv_krein_quotient"] == "OPEN")
check("PLANT no fifth quotient", ledger["residue"]["quotients_ranked"] == 4)
check("PLANT RA-D2 not silently resolved", rows["RA-D2"]["verdict"] == "OVER_DETERMINED")

if FAILURES:
    print("FAILURES", FAILURES)
    raise SystemExit(1)
print(f"PASS: {COUNT}/{COUNT}")
