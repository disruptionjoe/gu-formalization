#!/usr/bin/env python3
"""Fail-closed process audit for conditional-physics ledger v0.109."""

from pathlib import Path
import json

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot

ROOT = Path(__file__).resolve().parents[1]
FAILURES = []


def check(label, condition):
    if not condition:
        FAILURES.append(label)


def unique(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def load(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"),
                      object_pairs_hook=unique)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


ledger = load("lab/process/conditional-physics-ledger-v0.109.json")
registry = load("lab/process/selected-k77-source-euler-two-to-one.json")
contract = load("lab/methods/research-evidence-contract-v1.0.json")
report = read("explorations/conditional-build/selected-k77-source-euler-two-to-one-2026-08-09.md")
review = read("lab/process/hostile-reviews/2026-08-09-selected-k77-source-euler-two-to-one-review.md")
source = read("lab/sources/selected-k77-source-euler-two-to-one-source-reinspection-2026-08-09.md")

check("ledger version", ledger["schema_version"] == "0.109")
check("ledger predecessor", ledger["predecessor"].endswith("v0.108.json"))
check("coverage", ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("verdicts unchanged", ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5,
})
check("frontier", ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 3,
    "conditions_opened": 2, "remaining_named_conditions": 4,
})
check("residue", ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == 5)
check("source return", ledger["source_return"] == registry["source_return"]
      and "SOURCE_CORRECTS" in ledger["source_return"]
      and "SOURCE_SILENT" in ledger["source_return"])

family = registry["exact_result"]["family"]
check("one amplitude family", family == {"f": "t^2/3",
      "u": "-t/312-4t^2/3", "local_amplitudes": 1,
      "source_selects_t": False})
equations = registry["exact_result"]["equations"]
check("two equations", equations["rank"] == 2
      and equations["determinant"] == -97344)
rep = registry["exact_result"]["v0108_representative"]
check("v0108 retyped", rep["status"] == "EXACT_MEMBER_NOT_UNIQUE_SOURCE_VACUUM"
      and rep["independent_B_equation"] == "RECONSTRUCTION_CONDITION_NOT_SOURCE_EULER")
geometry = registry["exact_result"]["local_geometry"]
check("local geometry", geometry["connection_and_T_one_jet"] == "EXACT"
      and geometry["point_differential_bianchi"] == "PASS"
      and geometry["nonconstant_affine_connection_descent"] == "OPEN")
check("controls", registry["controls"]["primary"] == "45/45 PASS"
      and registry["controls"]["independent_sage"] == "18/18 PASS"
      and registry["controls"]["P1_P2_P3_unused"] is True)
check("parents distinct", registry["action_parents"]["collapsed"] is False)

rows = {row["id"]: row for row in ledger["rows"]
        if row.get("row_status") != "SUPERSEDED"}
migrated = ["LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR2d",
            "LT-GR3", "LT-GR5", "LT-GR6"]
for row_id in migrated:
    check(f"{row_id} evidence", rows[row_id]["evidence"]
          == "selected-k77-source-euler-two-to-one-2026-08-09.md")
migrations = [m for m in ledger["migrations"]
              if m["from_version"] == "0.108" and m["to_version"] == "0.109"]
check("seven migrations", [m["row_id"] for m in migrations] == migrated)
check("no meaning changes", all(m["meaning_changed"] is False for m in migrations))

check("report correction", "one common amplitude rather than two" in report
      and "zero local freedom" in report and "Retracted" in report)
check("source field typing", "not on independent" in source
      and "not a source-field Euler equation" in source)
check("review verdict", "SOURCE_TWO_TO_ONE_LOCAL_ONE_JET_GRADE" in review)
for lens in ("Layer-0 semantics", "Prior art", "Gauge and differential geometry",
             "Variational bicomplex", "Symplectic geometry",
             "Bianchi and integrability", "Microlocal PDE",
             "Krein/operator theory", "Complex/path-integral analysis",
             "Cosmology and source criticism"):
    check(f"review lens {lens}", lens in review)

check("ledger ancestry", reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.109.json"))

if FAILURES:
    raise SystemExit("FAIL selected K77 source-Euler two-to-one audit: "
                     + "; ".join(FAILURES))
print("PASS selected K77 source-Euler two-to-one audit")
