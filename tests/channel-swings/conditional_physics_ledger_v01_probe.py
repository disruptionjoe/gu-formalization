#!/usr/bin/env python3
"""Exact structural checks for the conditional physics ledger v0.1."""

from collections import Counter
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEDGER_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.1.json"
SCHEMA_PATH = ROOT / "lab/process/conditional-physics-ledger-schema-v0.1.json"
COUNTS = Counter()
FAILURES = []


def no_duplicate_object(pairs):
    keys = [key for key, _ in pairs]
    if len(keys) != len(set(keys)):
        raise ValueError("duplicate JSON key")
    return dict(pairs)


def load(path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=no_duplicate_object)


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


ledger = load(LEDGER_PATH)
schema = load(SCHEMA_PATH)
rows = ledger["rows"]
aliases = ledger["aliases"]
row_by_id = {row["id"]: row for row in rows}

print("A. DENOMINATOR AND COVERAGE")
expected_a = {f"CB-A:{group}{i}" for group, stop in (("A",8),("B",9),("C",6),("D",4),("E",7),("F",3),("G",4)) for i in range(1, stop+1)}
expected_b = {"CB-B:GR-1","CB-B:GR-1b","CB-B:GR-2","CB-B:GR-3","CB-B:GR-4","CB-B:GR-5","CB-B:GR-6","CB-B:GR-7","CB-B:SM-1","CB-B:SM-2","CB-B:SM-3","CB-B:SM-3b","CB-B:SM-4","CB-B:SM-5","CB-B:SM-6","CB-B:SM-7","CB-B:SM-8","CB-B:SM-9"}
expected_c = {f"CB-C:{group}{i}" for group, stop in (("A",7),("B",5),("C",2),("D",5),("E",1),("F",5),("G",2)) for i in range(1, stop+1)}
represented = {row["source_row"] for row in rows} | {alias["source_row"] for alias in aliases}

check("exact", "CB-A has 41 enumerated source rows", len(expected_a) == 41)
check("exact", "CB-B has 18 enumerated source rows", len(expected_b) == 18)
check("exact", "CB-C has 27 enumerated source rows", len(expected_c) == 27)
check("exact", "all 86 source rows are represented exactly by a target or alias", represented == expected_a | expected_b | expected_c)
check("exact", "the canonical denominator is 78 unique rows", len(rows) == len(row_by_id) == 78)
check("exact", "eight source rows are explicit aliases", len(aliases) == 8)
check("exact", "axis counts are 35 representation 17 Lagrangian 26 anomaly",
      Counter(row["axis"] for row in rows) == {"REPRESENTATION":35,"LAGRANGIAN":17,"ANOMALY_CONSISTENCY":26})
check("planted", "PLANT aggregate SM-9 is not double-counted as a canonical target", "CB-B:SM-9" not in {row["source_row"] for row in rows})
check("planted", "PLANT Dai-Freed free column is not independent of I16", "CB-C:B3" not in {row["source_row"] for row in rows})

print("\nB. TAXONOMY AND REQUIRED ROW INFORMATION")
required = set(schema["properties"]["rows"]["items"]["required"])
check("exact", "every row carries all required information fields", all(required <= set(row) for row in rows))
check("exact", "every distance is nonempty", all(row["distance"].strip() for row in rows))
check("exact", "every revival trigger is nonempty", all(row["revival_trigger"].strip() for row in rows))
check("exact", "every evidence pointer is nonempty", all(row["evidence"].strip() for row in rows))
known = ledger["taxonomy"]["verdict_kinds"]
check("exact", "every current kind is registered under its verdict", all(row["reason_kind"] in known[row["verdict"]] for row in rows))
check("exact", "SAME distinguishes derived imported and partial agreement", {"DERIVED","IMPORTED","DERIVED_PARTIAL"} <= {r["reason_kind"] for r in rows if r["verdict"]=="SAME"})
check("exact", "NEEDS distinguishes one bit construction and proven-unsupplyable", {"ONE_BIT","MISSING_CONSTRUCTION","PROVEN_UNSUPPLYABLE"} <= {r["reason_kind"] for r in rows if r["verdict"]=="NEEDS"})
check("exact", "DIFFERS distinguishes prediction convention and inert statement", {"PREDICTION","CONVENTION_ARTIFACT","STATED_INERT"} <= {r["reason_kind"] for r in rows if r["verdict"]=="DIFFERS"})
check("exact", "OVER_DETERMINED uses all four diagnostic kinds", {r["reason_kind"] for r in rows if r["verdict"]=="OVER_DETERMINED"} == {"GENUINE_FALSIFICATION","FORK_ARTIFACT","SCOPE_ERROR","STALE_PREMISE"})

def classify_kind(verdict, kind):
    return "KNOWN" if kind in known.get(verdict, ()) else "NEW_KIND_REQUIRED"

check("planted", "PLANT an unrecognized kind creates NEW_KIND_REQUIRED rather than forced fit", classify_kind("NEEDS", "RHYME") == "NEW_KIND_REQUIRED")

print("\nC. PROGRESS METER AND RESIDUE")
verdicts = Counter(row["verdict"] for row in rows)
expected_verdicts = {"SAME":32,"DIFFERS":18,"NEEDS":22,"OVER_DETERMINED":6}
check("exact", "verdict counts recompute to 32 18 22 6", verdicts == expected_verdicts)
check("exact", "coverage recomputes to 78 of 78", ledger["progress"]["mapped"] == ledger["progress"]["total"] == len(rows))
check("exact", "coverage is explicitly scoped to v0.1 rather than construction completion", "not a claim" in ledger["progress"]["coverage_scope"])
check("exact", "residue carries 83 real and at least 19 function-valued slots", ledger["residue"]["continuous_real"] == 83 and ledger["residue"]["function_valued_at_least"] >= 19)
check("exact", "ten open forks and zero ranked quotients remain visible", ledger["residue"]["open_discrete_forks"] == 10 and ledger["residue"]["quotients_ranked"] == 0)

meter = f"Ledger v0.1 — {len(rows)}/{ledger['denominator']['canonical_target_count']} target rows mapped; " + " · ".join(f"{verdicts[k]} {k.replace('_','-')}" for k in ("SAME","DIFFERS","NEEDS","OVER_DETERMINED"))
print("METER " + meter)
print("RESIDUE " + ledger["residue"]["meter"])

print("\nD. ESCALATION AND PROGNOSIS")
overs = {row["id"] for row in rows if row["verdict"] == "OVER_DETERMINED"}
escalated = {entry["row_id"] for entry in ledger["over_determined_escalations"]}
check("exact", "all and only six over-determined rows have escalation owners", overs == escalated and len(overs) == 6)
check("exact", "0B and 0C independently adjudicated their assigned over-determined rows",
      [e["row_id"] for e in ledger["over_determined_escalations"] if e["status"].startswith("ADJUDICATED")] == ["LT-GR1b", "LT-SM3b"])
check("exact", "opposite-prognosis NEEDS rows remain distinguishable", row_by_id["LT-GR1"]["reason_kind"] == "ONE_BIT" and row_by_id["LT-SM8"]["reason_kind"] == "PROVEN_UNSUPPLYABLE")
check("exact", "opposite-prognosis SAME rows remain distinguishable", row_by_id["RA-A7"]["reason_kind"] == "DERIVED" and row_by_id["AC-E1"]["reason_kind"] == "IMPORTED")
check("planted", "PLANT an over-determined finder cannot mark an unreviewed row resolved",
      all(e["status"] == "ESCALATED_PENDING_DISPOSITION" for e in ledger["over_determined_escalations"] if e["row_id"] not in {"LT-GR1b", "LT-SM3b"}))

print("\nCOUNTS " + " ".join(f"{k}={v}" for k,v in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS total={sum(COUNTS.values())}")
