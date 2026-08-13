#!/usr/bin/env python3
"""Fail-closed process audit for conditional-physics ledger v0.110."""

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


ledger = load("lab/process/conditional-physics-ledger-v0.110.json")
registry = load("lab/process/selected-k77-nonconstant-atlas-xi-prolongation.json")
contract = load("lab/methods/research-evidence-contract-v1.0.json")
report = read("explorations/conditional-build/selected-k77-nonconstant-atlas-xi-prolongation-2026-08-09.md")
review = read("lab/process/hostile-reviews/2026-08-09-selected-k77-nonconstant-atlas-xi-prolongation-review.md")
source = read("lab/sources/selected-k77-nonconstant-atlas-xi-source-reinspection-2026-08-09.md")

check("ledger version", ledger["schema_version"] == "0.110")
check("predecessor", ledger["predecessor"].endswith("v0.109.json"))
check("coverage", ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("verdicts", ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5,
})
check("frontier", ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 3,
    "conditions_opened": 1, "remaining_named_conditions": 3,
})
check("residue", ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == 5)
check("source return", ledger["source_return"] == registry["source_return"]
      and "SOURCE_CONFIRMS" in ledger["source_return"]
      and "SOURCE_SILENT" in ledger["source_return"])

result = registry["exact_result"]
check("branches", result["homogeneous_system"]["nonzero_branch_count"] == 2
      and result["branches"] == [
          {"t": "(-2+sqrt(3))/208", "b": "1/208-sqrt(3)/312"},
          {"t": "(-2-sqrt(3))/208", "b": "1/208+sqrt(3)/312"},
      ])
check("Xi rank", result["prolongation"]["jacobian_rank_without_Xi"]
      == result["prolongation"]["jacobian_rank_with_Xi"] == 2
      and result["prolongation"]["source_selects_amplitude"] is False)
check("atlas", all(result["atlas"][key] == "PASS" for key in (
      "affine_connection_direct_sequential", "curvature_covariance",
      "D_B_T_covariance", "off_shell_Xi_covariance")))
check("controls", registry["controls"]["primary"] == "42/42 PASS"
      and registry["controls"]["independent_sage"] == "14/14 PASS"
      and registry["controls"]["P1_P2_P3_unused"] is True)
check("parents distinct", registry["action_parents"]["collapsed"] is False)

rows = {row["id"]: row for row in ledger["rows"]
        if row.get("row_status") != "SUPERSEDED"}
migrated = ["LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR2d",
            "LT-GR3", "LT-GR5", "LT-GR6"]
for row_id in migrated:
    check(f"{row_id} evidence", rows[row_id]["evidence"]
          == "selected-k77-nonconstant-atlas-xi-prolongation-2026-08-09.md")
migrations = [m for m in ledger["migrations"]
              if m["from_version"] == "0.109" and m["to_version"] == "0.110"]
check("seven migrations", [m["row_id"] for m in migrations] == migrated)
check("no meaning changes", all(m["meaning_changed"] is False for m in migrations))

check("report fences", "homogeneous frozen-frame ansatz" in report
      and "not GU-derived dark-energy magnitudes" in report
      and "g^-1 dg" in report)
check("source typing", "redundant when" in source
      and "not, without a separate derivation" in source)
check("review verdict", "GENERIC_AFFINE_AND_SOURCE_REDUNDANCY_GRADE" in review)
for lens in ("Layer-0 semantics", "Prior art", "Gauge and differential geometry",
             "Variational bicomplex", "Symplectic geometry",
             "Spencer/formal integrability", "Microlocal PDE",
             "Krein/operator theory", "Complex/path-integral analysis",
             "Cosmology and source criticism"):
    check(f"review lens {lens}", lens in review)

current_refs = ["lab/process/RESEARCH-AGENDA.json", "NEXT-STEPS.md", "RESEARCH-STATUS.md",
                "explorations/README.md", "lab/process/README.md",
                "lab/process/CURRENT-RESEARCH-CONTEXT.md",
                "lab/methods/research-evidence-contract-v1.0.md"]
for relative in current_refs:
    check(f"current pointer {relative}", "v0.111" in read(relative))
check("contract pointer", contract["standing_ledger"]["ref"].endswith("v0.111.json"))
check("contract gate", contract["active_scientific_directives"][0]["next_gate"]
      == "CLASSIFY_BRANCH_AMPLITUDE_AS_MODULUS_BOUNDARY_CONDITION_OR_GLOBAL_OBSTRUCTION__DECIDE_ACTION_PARENT_AND_COMPLETE_TANGENT__ONLY_THEN_FULL_HESSIAN_BV_COMMON_DOMAIN")
check("inventory", "(484 Python + 73 Sage)" in read("tests/README.md"))

if FAILURES:
    raise SystemExit("FAIL selected K77 nonconstant-atlas/Xi audit: "
                     + "; ".join(FAILURES))
print("PASS selected K77 nonconstant-atlas/Xi audit")
