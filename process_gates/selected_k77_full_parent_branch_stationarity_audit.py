#!/usr/bin/env python3
"""Fail-closed process audit for conditional-physics ledger v0.112."""

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


ledger = load("lab/process/conditional-physics-ledger-v0.112.json")
registry = load("lab/process/selected-k77-full-parent-branch-stationarity.json")
successor = load("lab/process/selected-k77-branch-boundary-amplitude-classification.json")
contract = load("lab/process/functional-channel-operating-contract-v1.0.json")
report = read("explorations/conditional-build/selected-k77-full-parent-branch-stationarity-2026-08-09.md")
review = read("lab/process/hostile-reviews/2026-08-09-selected-k77-full-parent-branch-stationarity-review.md")
source = read("lab/sources/selected-k77-action-parent-source-reinspection-2026-08-09.md")

check("ledger version", ledger["schema_version"] == "0.112")
check("predecessor", ledger["predecessor"].endswith("v0.111.json"))
check("coverage", ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("verdicts", ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("frontier", ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 2,
    "conditions_opened": 0, "remaining_named_conditions": 3})
check("residue", ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == 5)
check("source return", ledger["source_return"] == registry["source_return"]
      and "TWO_C32_32" in ledger["source_return"]
      and "SOURCE_SILENT" in ledger["source_return"])

result = registry["exact_result"]
check("parent dimensions", result["full_real_internal_dimension"] == 16384
      and result["block_even_dimension"] == 8192
      and result["half_exchanging_odd_dimension"] == 8192)
check("full varpi", result["varpi_pointwise_direction_count"] == 229376
      and result["E_T_support_count"] == 14
      and result["E_T_support_grade"] == 1
      and result["both_branches_full_varpi_zero"] is True)
check("epsilon and endpoint", result["both_branches_full_epsilon_bulk_zero"] is True
      and result["both_branches_endpoint_momentum_nonzero"] is True)
check("nonvacuity", result["generic_grade5_support"] == 476)
check("scope fences", result["parent_selected"] is False
      and result["functional_tangent_complete"] is False)
check("controls", registry["controls"]["primary"] == "34/34 PASS"
      and registry["controls"]["independent_sage"] == "20/20 PASS"
      and registry["controls"]["P1_P2_P3_unused"] is True)

rows = {row["id"]: row for row in ledger["rows"]
        if row.get("row_status") != "SUPERSEDED"}
migrated = ["LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR2d",
            "LT-GR3", "LT-GR5", "LT-GR6"]
for row_id in migrated:
    check(f"{row_id} evidence", rows[row_id]["evidence"]
          == "selected-k77-full-parent-branch-stationarity-2026-08-09.md")
migrations = [m for m in ledger["migrations"]
              if m["from_version"] == "0.111" and m["to_version"] == "0.112"]
check("seven migrations", [m["row_id"] for m in migrations] == migrated)
check("no meaning changes", all(m["meaning_changed"] is False for m in migrations))

check("report fences", "229,376" in report
      and "does not settle the action-parent" in report.lower()
      and "endpoint momentum" in report)
check("source typing", "two copies of `C^(32,32)`" in source
      and "SOURCE-SILENT" in source)
check("review verdict", "POINTWISE_INTERNAL_PARENT_COMPATIBILITY_ONLY" in review)
for lens in ("Layer-0 semantics", "Prior art", "Representation and Clifford algebra",
             "Variational bicomplex", "Symplectic geometry", "Gauge geometry",
             "Microlocal PDE and Krein/operator theory",
             "Complex/path-integral analysis"):
    check(f"review lens {lens}", lens in review)

for relative in ("LANES.yaml", "NEXT-STEPS.md", "RESEARCH-STATUS.md",
                 "explorations/README.md", "lab/process/README.md",
                 "lab/process/agent-context-pack.md",
                 "lab/process/functional-channel-operating-contract-v1.0.md"):
    check(f"current pointer {relative}", "v0.113" in read(relative))
check("contract pointer", contract["standing_ledger"]["ref"].endswith("v0.113.json"))
check("contract gate", contract["active_scientific_directives"][0]["next_gate"]
      == successor["next_gate"])
check("inventory", "(486 Python + 75 Sage)" in read("tests/README.md"))

if FAILURES:
    raise SystemExit("FAIL selected K77 full-parent branch audit: "
                     + "; ".join(FAILURES))
print("PASS selected K77 full-parent branch audit")
