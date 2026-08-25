#!/usr/bin/env python3
"""Ledger v0.89 append-only signature-rationale migration gate."""

from collections import Counter
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


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


old = strict("lab/process/conditional-physics-ledger-v0.88.json")
new = strict("lab/process/conditional-physics-ledger-v0.89.json")
registry = strict("lab/process/signature-rationale-build-branch-retype.json")

check("ledger", "v0.89 is append-only over v0.88", new["predecessor"].endswith("v0.88.json"))
check("ledger", "active denominator is frozen", new["denominator"] == old["denominator"])
check("ledger", "verdict counts are frozen", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("ledger", "residue is frozen", new["residue"] == old["residue"])
check("ledger", "row ids are frozen", [r["id"] for r in new["rows"]] == [r["id"] for r in old["rows"]])
check("ledger", "source return corrects the rationale", new["source_return"] == "SOURCE-CORRECTS")
check("ledger", "frontier records three closures and one opening", new["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 3,
    "conditions_opened": 1,
    "remaining_named_conditions": 3,
})

rows = ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"]
tail = new["migrations"][-5:]
check("migration", "exactly five v0.89 migrations are appended", [m["row_id"] for m in tail] == rows and all(m["to_version"] == "0.89" for m in tail))
for row_id in rows:
    before = next((r for r in old["rows"] if r.get("id") == row_id), {})
    after = next((r for r in new["rows"] if r.get("id") == row_id), {})
    check("migration", f"{row_id}: verdict and reason kind are frozen",
          (after.get("verdict"), after.get("reason_kind")) ==
          (before.get("verdict"), before.get("reason_kind")) and bool(before) and bool(after))
    check("migration", f"{row_id}: distance is branch-aware",
          "signature-generic" in after.get("distance", "") and "K77" in after.get("distance", ""))
    check("migration", f"{row_id}: evidence points to the retype",
          after.get("evidence") == "signature-rationale-and-build-branch-retype-2026-08-08.md")

check("layer0", "K77 is author asserted", registry["fork_disposition"]["K77"] == "AUTHOR_ASSERTED_CONDITIONAL_BUILD")
check("layer0", "K95 is geometry derived", registry["fork_disposition"]["K95"] == "GEOMETRY_DERIVED_COMPARATOR")
check("layer0", "real forms remain distinct", registry["layer0"]["real_forms_identified"] is False)
check("scope", "no new datum or residue is booked", not registry["accounting"]["external_datum_used"] and not registry["accounting"]["residue_change"])
check("scope", "P1 P2 P3 remain unused", new["residue"] == old["residue"])

print("SOURCE_RETURN=SOURCE-CORRECTS")
print("K77=AUTHOR_ASSERTED_CONDITIONAL")
print("K95=GEOMETRY_DERIVED_COMPARATOR")
print("NEXT=SIGNATURE_GENERIC_WARD_THEN_BRANCH_NATIVE_K77_K95_SPECIALIZATION")
print("CHECKS=" + " ".join(f"{k}:{v}" for k, v in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
