#!/usr/bin/env python3
"""Fail-closed process audit for conditional-physics ledger v0.111."""

from pathlib import Path
import json

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


ledger = load("lab/process/conditional-physics-ledger-v0.111.json")
registry = load("lab/process/selected-k77-source-tangent-branch-stationarity.json")
contract = load("lab/process/functional-channel-operating-contract-v1.0.json")
report = read("explorations/conditional-build/selected-k77-source-tangent-branch-stationarity-2026-08-09.md")
review = read("lab/process/hostile-reviews/2026-08-09-selected-k77-source-tangent-branch-stationarity-review.md")
source = read("lab/sources/selected-k77-source-tangent-branch-source-reinspection-2026-08-09.md")

check("ledger version", ledger["schema_version"] == "0.111")
check("predecessor", ledger["predecessor"].endswith("v0.110.json"))
check("coverage", ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("verdicts", ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("frontier", ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 4,
    "conditions_opened": 1, "remaining_named_conditions": 3})
check("residue", ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == 5)
check("source return", ledger["source_return"] == registry["source_return"]
      and "SOURCE_CONFIRMS" in ledger["source_return"]
      and "SOURCE_SILENT" in ledger["source_return"])

result = registry["exact_result"]
check("branches", len(result["branches"]) == 2)
check("Euler formulas", result["connection_euler"]["directions_checked"] == 1470
      and result["connection_euler"]["grade_two_identically_zero"] == 1274
      and result["connection_euler"]["rational_unisolvent_samples"] == 6)
check("source pullback", result["branch_pullback"]["varpi_euler"].startswith("ZERO_ALL_1470")
      and result["branch_pullback"]["primitive_epsilon_lower_order"].startswith("ZERO_ALL_91")
      and result["branch_pullback"]["primitive_epsilon_endpoint_momentum"] == "NONZERO"
      and result["branch_pullback"]["action_density"] == "ZERO_BOTH_BRANCHES")
check("tangent fence", result["known_source_coordinate_count"] == 1571
      and result["tangent_completeness"] is False
      and result["amplitude_selected_by_source"] is False)
check("controls", registry["controls"]["primary"] == "62/62 PASS"
      and registry["controls"]["independent_sage"] == "21/21 PASS"
      and registry["controls"]["P1_P2_P3_unused"] is True)
check("parents distinct", registry["action_parents"]["collapsed"] is False)

rows = {row["id"]: row for row in ledger["rows"]
        if row.get("row_status") != "SUPERSEDED"}
migrated = ["LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR2d",
            "LT-GR3", "LT-GR5", "LT-GR6"]
for row_id in migrated:
    check(f"{row_id} evidence", rows[row_id]["evidence"]
          == "selected-k77-source-tangent-branch-stationarity-2026-08-09.md")
migrations = [m for m in ledger["migrations"]
              if m["from_version"] == "0.110" and m["to_version"] == "0.111"]
check("seven migrations", [m["row_id"] for m in migrations] == migrated)
check("no meaning changes", all(m["meaning_changed"] is False for m in migrations))

check("report fences", "actual local source variables" in report
      and "not promoted to a complete" in report
      and "endpoint momentum" in report)
check("source typing", "not a source coordinate" in source
      and "does not mention the two" in source)
check("review verdict", "LOCAL_SELECTED_SOURCE_EULER_ONLY" in review)
for lens in ("Layer-0 semantics", "Prior art", "Gauge and differential geometry",
             "Variational bicomplex", "Symplectic geometry",
             "Representation and Clifford algebra", "Microlocal PDE",
             "Krein/operator theory", "Complex/path-integral analysis",
             "Cosmology and source criticism"):
    check(f"review lens {lens}", lens in review)

for relative in ("LANES.yaml", "NEXT-STEPS.md", "RESEARCH-STATUS.md",
                 "explorations/README.md", "lab/process/README.md",
                 "lab/process/agent-context-pack.md",
                 "lab/process/functional-channel-operating-contract-v1.0.md"):
    check(f"current pointer {relative}", "v0.111" in read(relative))
check("contract pointer", contract["standing_ledger"]["ref"].endswith("v0.111.json"))
check("contract gate", contract["active_scientific_directives"][0]["next_gate"]
      == registry["next_gate"])
check("inventory", "(484 Python + 73 Sage)" in read("tests/README.md"))

if FAILURES:
    raise SystemExit("FAIL selected K77 source-tangent branch audit: "
                     + "; ".join(FAILURES))
print("PASS selected K77 source-tangent branch audit")
