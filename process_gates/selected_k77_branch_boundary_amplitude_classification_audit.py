#!/usr/bin/env python3
"""Fail-closed process audit for conditional-physics ledger v0.113."""

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


ledger = load("lab/process/conditional-physics-ledger-v0.113.json")
registry = load("lab/process/selected-k77-branch-boundary-amplitude-classification.json")
contract = load("lab/process/functional-channel-operating-contract-v1.0.json")
report = read("explorations/conditional-build/selected-k77-branch-boundary-amplitude-classification-2026-08-09.md")
review = read("lab/process/hostile-reviews/2026-08-09-selected-k77-branch-boundary-amplitude-classification-review.md")
source = read("lab/sources/selected-k77-branch-boundary-source-reinspection-2026-08-09.md")

check("ledger version", ledger["schema_version"] == "0.113")
check("predecessor", ledger["predecessor"].endswith("v0.112.json"))
check("coverage", ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("verdicts", ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("frontier", ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 1,
    "conditions_opened": 1, "remaining_named_conditions": 3})
check("residue", ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == 5)
check("source return", ledger["source_return"] == registry["source_return"]
      and "SOURCE_CONFIRMS" in ledger["source_return"]
      and "SOURCE_SILENT" in ledger["source_return"])

branches = registry["branches"]
check("two branches", len(branches) == 2)
check("opposite charges", [row["real_sign"] for row in branches]
      == ["POSITIVE", "NEGATIVE"] and registry["galois_conjugate_charges"] is True)
check("adjoint zero", all(row["adjoint_moment_map_zero"] is True for row in branches)
      and registry["residual_adjoint_generator_count_checked_per_branch"] == 16384)
check("endpoint ranks", all(row["primitive_endpoint_rank_each"] == 14
                            and row["primitive_two_endpoint_rank"] == 28
                            for row in branches))

horns = registry["horns"]
check("five horns", set(horns) == {
    "RESIDUAL_ADJOINT_BARE_GAUGE", "PRIMITIVE_EPSILON_BARE_GAUGE",
    "CHARGED_BOUNDARY_SYMMETRY", "MINIMAL_EDGE_COMPLETION",
    "ZERO_CHARGE_NEUMANN_LIKE"})
check("horn classifications", "SURVIVE" in horns["RESIDUAL_ADJOINT_BARE_GAUGE"]
      and "OBSTRUCTED" in horns["PRIMITIVE_EPSILON_BARE_GAUGE"]
      and "SURVIVE" in horns["CHARGED_BOUNDARY_SYMMETRY"]
      and "SURVIVE" in horns["MINIMAL_EDGE_COMPLETION"]
      and "EXCLUDED" in horns["ZERO_CHARGE_NEUMANN_LIKE"])
check("edge", registry["edge"]["coefficients"] == [-1, 1]
      and registry["edge"]["unique"] is True
      and registry["edge"]["finite_cell_rank"] == 4
      and registry["edge"]["finite_cell_kernel_dimension"] == 2
      and registry["edge"]["selects_branch"] is False)
check("controls", registry["controls"]["primary"] == "51/51 PASS"
      and registry["controls"]["independent_sage"] == "20/20 PASS"
      and registry["controls"]["generic_v0102_fixture_survives"] is True
      and registry["controls"]["P1_P2_P3_unused"] is True)

rows = {row["id"]: row for row in ledger["rows"]
        if row.get("row_status") != "SUPERSEDED"}
migrated = ["LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR2d",
            "LT-GR3", "LT-GR5", "LT-GR6"]
for row_id in migrated:
    check(f"{row_id} evidence", rows[row_id]["evidence"]
          == "selected-k77-branch-boundary-amplitude-classification-2026-08-09.md")
migrations = [m for m in ledger["migrations"]
              if m["from_version"] == "0.112" and m["to_version"] == "0.113"]
check("seven migrations", [m["row_id"] for m in migrations] == migrated)
check("no meaning changes", all(m["meaning_changed"] is False for m in migrations))

check("report typing", "[Theta,P]=0" in report
      and "rank 14 per endpoint" in report
      and "does not construct a global BFV phase space" in report)
check("source typing", "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source)
check("review verdict", "CANDIDATE_SURVIVES_WITH_LAYER0_SPLIT" in review)
for lens in ("Layer-0 semantics", "Prior art", "Symplectic geometry",
             "Variational bicomplex", "Gauge and differential geometry",
             "Representation and Clifford algebra", "Analytic, PDE and Krein domain",
             "Source criticism"):
    check(f"review lens {lens}", lens in review)

for relative in ("LANES.yaml", "NEXT-STEPS.md", "RESEARCH-STATUS.md",
                 "explorations/README.md", "lab/process/README.md",
                 "lab/process/agent-context-pack.md",
                 "lab/process/functional-channel-operating-contract-v1.0.md"):
    text = read(relative)
    check(f"current or successor pointer {relative}",
          "v0.113" in text or "v0.114" in text)
check("contract successor aware", contract["standing_ledger"]["ref"].endswith("v0.113.json")
      or contract["standing_ledger"]["ref"].endswith("v0.114.json"))
check("contract successor gate", contract["active_scientific_directives"][0]["next_gate"]
      == registry["next_gate"] or "BFV" in contract["active_scientific_directives"][0]["next_gate"])
check("inventory successor aware", "(486 Python + 75 Sage)" in read("tests/README.md")
      or "(487 Python + 76 Sage)" in read("tests/README.md"))

if FAILURES:
    raise SystemExit("FAIL selected K77 branch boundary-amplitude audit: "
                     + "; ".join(FAILURES))
print("PASS selected K77 branch boundary-amplitude audit")
