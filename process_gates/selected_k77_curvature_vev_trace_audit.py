#!/usr/bin/env python3
"""Fail-closed process audit for conditional-physics ledger v0.108."""

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


ledger = load("lab/process/conditional-physics-ledger-v0.108.json")
registry = load("lab/process/selected-k77-curvature-vev-trace-closure.json")
contract = load("lab/methods/research-evidence-contract-v1.0.json")
report = read("explorations/conditional-build/selected-k77-curvature-vev-trace-closure-2026-08-09.md")
review = read("lab/process/hostile-reviews/2026-08-09-selected-k77-curvature-vev-trace-review.md")
source = read("lab/sources/selected-k77-curvature-vev-trace-source-reinspection-2026-08-09.md")

check("ledger version", ledger["schema_version"] == "0.108")
check("ledger predecessor", ledger["predecessor"].endswith("v0.107.json"))
check("coverage", ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("verdicts unchanged", ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5,
})
check("frontier", ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 2,
    "conditions_opened": 1, "remaining_named_conditions": 4,
})
check("residue", ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == 5)
check("source return", ledger["source_return"] == registry["source_return"]
      and "SOURCE_CONFIRMS" in ledger["source_return"]
      and "SOURCE_SILENT" in ledger["source_return"])

layer0 = set(ledger["layer0_objects_compared"])
check("layer0 carrier", {"SOURCE_DYNAMIC_VEV_CONNECTION_DISTORTION_CARRIER",
      "EXISTING_ACTION_T_OMEGA_CARRIER", "DERIVATIVE_CURVATURE_FIRST_JET_CELL",
      "INDEPENDENT_ZERO_ORDER_FIELD", "GLOBAL_CONNECTION_CURVATURE_REALISATION",
      "OBSERVED_EINSTEIN_EQUATION"} <= layer0)

branch = registry["exact_result"]["branch"]
check("branch", branch == {"B_star": "(1/208)Phi1", "T_star": "-(1/104)Phi1",
      "r_star": "1/129792", "nonzero_T_horn_unique": True})
constraints = registry["exact_result"]["constraints"]
check("zero local freedom", constraints["field_values"] == 3
      and constraints["independent_equations"] == 3
      and constraints["jacobian_rank"] == 3
      and constraints["jacobian_determinant"] == -624
      and constraints["local_freedom"] == 0
      and constraints["new_action_coefficients"] == 0)
action = registry["exact_result"]["action"]
check("action cancellation", action == {"noncurvature_value": "7/21632",
      "derivative_curvature_value": "-7/21632", "total_value": "0"})
finite = registry["exact_result"]["finite_euler"]
check("finite Euler", finite["B_zero_directions"] == 1470
      and finite["T_zero_directions"] == 1470
      and finite["raw_residual_zero"] is True
      and finite["metric_volume_covector_zero_directions"] == 10)
check("controls", registry["controls"]["primary"] == "43/43 PASS"
      and registry["controls"]["independent_sage"] == "16/16 PASS"
      and registry["controls"]["global_realisation_not_promoted"] is True
      and registry["controls"]["P1_P2_P3_unused"] is True)
check("parents distinct", registry["action_parents"]["collapsed"] is False)

rows = {row["id"]: row for row in ledger["rows"]
        if row.get("row_status") != "SUPERSEDED"}
migrated = ["LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR2d",
            "LT-GR3", "LT-GR5", "LT-GR6"]
for row_id in migrated:
    check(f"{row_id} evidence", rows[row_id]["evidence"]
          == "selected-k77-curvature-vev-trace-closure-2026-08-09.md")
migrations = [m for m in ledger["migrations"]
              if m["from_version"] == "0.107" and m["to_version"] == "0.108"]
check("seven migrations", [m["row_id"] for m in migrations] == migrated)
check("no meaning changes", all(m["meaning_changed"] is False for m in migrations))

check("report fences", "scalar-jet grade" in report
      and "independent zero-order algebraic field" in report
      and "not the observed dark-energy magnitude" in report)
check("source carrier fence", "SAME-CARRIER" in source
      and "not globally identified coefficientwise" in source)
check("review verdict", "CANDIDATE_SURVIVES__LOCAL_SCALAR_JET_GRADE_ONLY" in review)
for lens in ("Layer-0 semantics", "Prior art", "Variational bicomplex",
             "Symplectic geometry", "Bianchi and integrability",
             "Microlocal PDE", "Krein/operator theory",
             "Complex/path-integral analysis", "Source criticism"):
    check(f"review lens {lens}", lens in review)

check("ledger ancestry", reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.108.json"))

if FAILURES:
    raise SystemExit("FAIL selected K77 curvature/VEV trace audit: "
                     + "; ".join(FAILURES))
print("PASS selected K77 curvature/VEV trace audit")
