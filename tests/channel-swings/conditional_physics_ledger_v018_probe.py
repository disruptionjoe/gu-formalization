#!/usr/bin/env python3
"""Machine check for conditional-physics ledger v0.18."""

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


ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.18.json")
registry = strict(ROOT / "lab/process/selected-cubic-reduced-numerator-completion-fork.json")
rows = {r["id"]: r for r in ledger["rows"] if r.get("row_status") != "SUPERSEDED"}

check("version and predecessor", ledger["schema_version"] == "0.18" and ledger["predecessor"].endswith("v0.17.json"))
check("denominator frozen", ledger["denominator"]["canonical_target_count"] == 82)
check("coverage frozen", ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("verdict counts frozen", ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6})
check("residue frozen", ledger["residue"]["continuous_real"] == 84 and ledger["residue"]["function_valued_at_least"] == 19 and ledger["residue"]["open_discrete_forks"] == 9)
check("quotient count frozen", ledger["residue"]["quotients_ranked"] == 4)
check("four touched rows exact", registry["ledger"]["touched_rows"] == ["LT-GR2b", "LT-GR3", "LT-GR5", "LT-SM8"])
check("LT-GR2b carries diagonal zero and mixed fork", "Q0Q0_BULK_NUMERATOR_SHELL_ZERO" in rows["LT-GR2b"]["mapping_grade"] and "Q0QM_FULL_MOVING_COMPLETION_FORK" in rows["LT-GR2b"]["mapping_grade"])
check("LT-GR3 keeps loop UV open", "LOOP_UV_OPEN" in rows["LT-GR3"]["mapping_grade"])
check("LT-GR5 keeps augmented torsion mixed completion open", "AUGMENTED_TORSION_MIXED_COMPLETION_AND_DOMAIN_OPEN" in rows["LT-GR5"]["mapping_grade"])
check("LT-SM8 reason kind corrected", rows["LT-SM8"]["verdict"] == "NEEDS" and rows["LT-SM8"]["reason_kind"] == "MISSING_CONSTRUCTION")
check("source return retained", registry["source_return"] == "SOURCE-SILENT")
check("external datum unused", registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})
check("Curt and third lane fences", registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and registry["third_lane"] == "NOT_PROMOTED")

migrations = [m for m in ledger["migrations"] if m["from_version"] == "0.17" and m["to_version"] == "0.18"]
check("four append-only migrations", [m["row_id"] for m in migrations] == ["LT-GR2b", "LT-GR3", "LT-GR5", "LT-SM8"])
check("no meaning changed", all(m["meaning_changed"] is False for m in migrations))

check("PLANT kinematic shell no longer implies unsupplyable positivity row", rows["LT-SM8"]["reason_kind"] != "PROVEN_UNSUPPLYABLE")
check("PLANT diagonal zero does not close mixed row", "Q0QM" in rows["LT-GR2b"]["mapping_grade"])
check("PLANT no Q1 promotion", registry["shell_numerators"]["selected_q0_qm_class"] == "NOT_IDENTIFIED_BY_CURRENT_INHERITED_DATA")
check("PLANT no datum consumption", set(registry["external_datum"].values()) == {"UNUSED"})

if FAILURES:
    print("FAILURES", FAILURES)
    raise SystemExit(1)
print(f"PASS: {COUNT}/{COUNT}")
