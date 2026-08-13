#!/usr/bin/env python3
"""Fail-closed process audit for conditional-physics ledger v0.107."""

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
    return json.loads(
        (ROOT / relative).read_text(encoding="utf-8"),
        object_pairs_hook=unique,
    )


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


ledger = load("lab/process/conditional-physics-ledger-v0.107.json")
registry = load("lab/process/selected-k77-direct-metric-euler.json")
contract = load("lab/methods/research-evidence-contract-v1.0.json")
report = read("explorations/conditional-build/selected-k77-direct-metric-euler-2026-08-09.md")
review = read("lab/process/hostile-reviews/2026-08-09-selected-k77-direct-metric-euler-review.md")

check("ledger schema", ledger["schema_version"] == "0.107")
check("ledger predecessor", ledger["predecessor"].endswith("v0.106.json"))
check("coverage", ledger["progress"]["mapped"] == 82 and ledger["progress"]["total"] == 82)
check("verdicts", ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5
})
check("frontier", ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 1,
    "conditions_opened": 1, "remaining_named_conditions": 5,
})
check("source return", "SOURCE_CONFIRMS_FIRST_ACTION_TWO_CONNECTION" in ledger["source_return"]
      and "DYNAMIC_COSMOLOGICAL_VEV" in ledger["source_return"]
      and "SOURCE_SILENT" in ledger["source_return"])

required_layer0 = {
    "DIRECT_METRIC_PARTIAL_AT_FIXED_B_T",
    "SOURCE_COORDINATE_METRIC_DERIVATIVE_AT_FIXED_VARPI_EPSILON",
    "CO_MOVING_CLIFFORD_FRAME_METRIC_DERIVATIVE",
    "LIFT_INDEPENDENT_TOTAL_FIRST_VARIATION_AT_CONNECTION_CRITICALITY",
    "FOURTEEN_DIMENSIONAL_GIMMEL_VOLUME_TRACE",
    "FOUR_DIMENSIONAL_EINSTEIN_TRACE_REVERSAL",
    "RANK_ONE_COSMOLOGICAL_TRACE_EULER_DEMAND",
    "DYNAMIC_VARPI_VEV_CANCELLATION_TARGET",
}
check("layer0", required_layer0 <= set(ledger["layer0_objects_compared"]))
check("residue", ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == 5)
check("quotients unbooked", "unbooked" in ledger["residue"]["meter"]
      and "220/220/32" in ledger["residue"]["meter"])
check("queue", ledger["next_work_queue"][0]["rows"]
      == ["LT-GR1", "LT-GR2b", "LT-GR2d", "LT-GR3", "LT-GR5", "LT-GR6"]
      and "opposite covector" in ledger["next_work_queue"][0]["why"])

rows = {row["id"]: row for row in ledger["rows"]
        if row.get("row_status") != "SUPERSEDED"}
for row_id in ("LT-GR1", "LT-GR2b", "LT-GR2d", "LT-GR3", "LT-GR5", "LT-GR6"):
    check(f"{row_id} evidence", rows[row_id]["evidence"]
          == "selected-k77-direct-metric-euler-2026-08-09.md")
check("metric row", "RANK1" in rows["LT-GR1"]["frontier_grade"]
      and "KERNEL9" in rows["LT-GR1"]["frontier_grade"])
check("dynamic row", "DYNAMIC_VEV_CANCELLATION_OPEN" in rows["LT-GR2b"]["frontier_grade"])
check("scale row", "FIRST_ACTION_NORMALIZED_TRACE_DEMAND_EXACT_RANK1"
      in rows["LT-GR2d"]["mapping_grade"])
check("two actions", "SECOND_ACTION_FIRST_VARIATION_ZERO" in rows["LT-GR3"]["frontier_grade"])

migrations = [m for m in ledger["migrations"]
              if m["from_version"] == "0.106" and m["to_version"] == "0.107"]
check("six migrations", [m["row_id"] for m in migrations]
      == ["LT-GR1", "LT-GR2b", "LT-GR2d", "LT-GR3", "LT-GR5", "LT-GR6"])
check("migration meanings", all(m["meaning_changed"] is False for m in migrations))

check("registry status", registry["status"].startswith("DIRECT_METRIC_EULER_RANK1"))
metric = registry["exact_result"]["metric_euler"]
check("metric covector", metric["normalized_covector"]
      == ["-7/9126", "0", "0", "0", "7/9126", "0", "0", "7/9126", "0", "7/9126"]
      and metric["rank"] == 1 and metric["kernel_dimension"] == 9)
check("density covector", registry["exact_result"]["gimmel_density"]["covector"]
      == ["-2", "0", "0", "0", "2", "0", "0", "2", "0", "2"])
check("branch", registry["exact_result"]["branch"]["E_B_zero_directions"] == 1470
      and registry["exact_result"]["branch"]["E_T_zero_directions"] == 1470
      and registry["exact_result"]["branch"]["raw_residual_zero"] is True)
check("second action", registry["exact_result"]["second_action"]["first_variation_zero"] is True
      and registry["exact_result"]["second_action"]["cancels_first_action_trace"] is False)
check("generated demand", registry["generated_demand"]["dimension"] == 1
      and registry["generated_demand"]["status"] == "OPEN_COMPATIBILITY_NOT_CANCELLATION")
check("parents", registry["action_parents"]["collapsed"] is False
      and set(registry["action_parents"]) >= {
          "selected_spin_native", "two_U32_32_halves", "full_U64_64"
      })
check("controls", registry["controls"]["primary"] == "45/45 PASS"
      and registry["controls"]["independent_sage"] == "11/11 PASS"
      and registry["controls"]["P1_P2_P3_unused"] is True)

check("report scope", "not a full bosonic saddle" in report
      and "cosmological-type trace demand" in report
      and "No physical scale is derived" in report)
check("review verdict", "CANDIDATE_SURVIVES__RANK_ONE_GENERATED_DEMAND" in review)
for lens in ("Layer-0 semantics", "Prior art", "Variational bicomplex",
             "Symplectic geometry", "Microlocal PDE", "Krein/operator theory",
             "Complex/path-integral analysis", "Source criticism"):
    check(f"review lens {lens}", lens in review)

current_refs = [
    "lab/process/RESEARCH-AGENDA.json", "NEXT-STEPS.md", "RESEARCH-STATUS.md", "explorations/README.md",
    "lab/process/README.md", "lab/process/CURRENT-RESEARCH-CONTEXT.md",
    "lab/methods/research-evidence-contract-v1.0.md",
]
for relative in current_refs:
    check(f"current pointer {relative}", "v0.107" in read(relative))
check("contract pointer", contract["standing_ledger"]["ref"].endswith("v0.107.json"))
check("contract next gate", contract["active_scientific_directives"][0]["next_gate"]
      == registry["next_gate"])

python_count = len(list((ROOT / "tests/channel-swings").glob("*.py")))
sage_count = len(list((ROOT / "tests/channel-swings").glob("*.sage")))
check("inventory prose", f"({python_count} Python + {sage_count} Sage)" in read("tests/README.md"))

if FAILURES:
    raise SystemExit("FAIL selected K77 direct metric Euler audit: " + "; ".join(FAILURES))
print("PASS selected K77 direct metric Euler audit")
