#!/usr/bin/env python3
"""Fail-closed process audit for conditional-physics ledger v0.105."""

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
    return json.loads(
        (ROOT / relative).read_text(encoding="utf-8"),
        object_pairs_hook=unique,
    )


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


ledger = load("lab/process/conditional-physics-ledger-v0.105.json")
registry = load("lab/process/selected-k77-primitive-epsilon-common-bank.json")
contract = load("lab/methods/research-evidence-contract-v1.0.json")
report = read("explorations/conditional-build/selected-k77-primitive-epsilon-common-bank-2026-08-08.md")
review = read("lab/process/hostile-reviews/2026-08-08-selected-k77-primitive-epsilon-common-bank-review.md")

check("ledger schema", ledger["schema_version"] == "0.105")
check("ledger predecessor", ledger["predecessor"].endswith("v0.104.json"))
check("coverage", ledger["progress"]["mapped"] == 82 and ledger["progress"]["total"] == 82)
check("verdicts", ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5
})
check("frontier", ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 4,
    "conditions_opened": 1, "remaining_named_conditions": 4,
})
check("source return", "SOURCE_CONFIRMS_PRIMITIVE_EPSILON" in ledger["source_return"]
      and "SOURCE_SILENT" in ledger["source_return"])

required_layer0 = {
    "PRIMITIVE_EPSILON_INDEPENDENT_H_VALUED_FIELD_TANGENT_SPIN77_DIM91",
    "DEPENDENT_PHYSICAL_KOSMANN_CARTAN_WARD_ORBIT_DIM4",
    "CONDITIONAL_GAMMA_SOLDERED_EPSILON_ORBIT_DIM4",
    "PRINCIPAL_DELTA_EPSILON_T_MINUS_Q_ETA",
    "LOWER_ORDER_MOVING_SHIAB_DELTA_PHI_COMMUTATOR",
    "COMMON_METRIC10_VARPI24_EPSILON91_FIELD_TANGENT_DIM125",
    "NONNULL_FULL_GRAM_RANK110_TRACE_QUOTIENT220",
    "NULL_FULL_GRAM_RANK16_TRACE_QUOTIENT32",
    "NULL_FULL_IMAGE_ISOTROPIC_EXCESS94",
    "NORMALIZED_FIRST_ACTION_SOURCE_TANGENT_DIM34",
    "ENLARGED_SAME_BACKGROUND_FIRST_ACTION_TANGENT_DIM125",
    "ACTION_DERIVED_BV_DIFFERENTIAL_ON_ENLARGED_TANGENT",
}
check("layer0", required_layer0 <= set(ledger["layer0_objects_compared"]))
check("residue", ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == 5)
check("new quotients unbooked", "not booked" in ledger["residue"]["quotients_ranked_scope"]
      and "220/220/32" in ledger["residue"]["quotients_ranked_scope"])
check("queue", ledger["next_work_queue"][0]["rows"]
      == ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"]
      and "lower-order moving-Shiab epsilon" in ledger["next_work_queue"][0]["why"])

rows = {row["id"]: row for row in ledger["rows"]
        if row.get("row_status") != "SUPERSEDED"}
for row_id in ("LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"):
    check(f"{row_id} evidence", rows[row_id]["evidence"]
          == "selected-k77-primitive-epsilon-common-bank-2026-08-08.md")
    check(f"{row_id} frontier", "PRIMITIVE_EPSILON91" in rows[row_id]["frontier_grade"]
          and "GRAM_RANK110_110_16" in rows[row_id]["frontier_grade"])

migrations = [m for m in ledger["migrations"]
              if m["from_version"] == "0.104" and m["to_version"] == "0.105"]
check("five migrations", [m["row_id"] for m in migrations]
      == ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"])
check("migration meanings", all(m["meaning_changed"] is False for m in migrations))

check("registry status", registry["status"].startswith(
    "SELECTED_SPIN_NATIVE_PRIMITIVE_EPSILON_PRINCIPAL_BANK_EXACT"))
check("dimensions", registry["exact_result"]["field_dimension"] == 125
      and registry["exact_result"]["epsilon_dimension"] == 91
      and registry["exact_result"]["metric_plus_epsilon_rank"] == 97)
check("raw ranks", list(registry["exact_result"]["raw_rank"].values()) == [110, 110, 110])
check("Gram ranks", [registry["exact_result"]["gram"][name]["rank"]
                     for name in ("timelike", "spacelike", "null")] == [110, 110, 16])
check("inertias", [registry["exact_result"]["gram"][name]["inertia"]
                   for name in ("timelike", "spacelike", "null")]
      == [[58, 52, 15], [53, 57, 15], [10, 6, 109]])
check("trace dimensions", [registry["exact_result"]["gram"][name]["green_quotient_dimension"]
                           for name in ("timelike", "spacelike", "null")]
      == [220, 220, 32])
check("null isotropic", registry["exact_result"]["null_extra_isotropic_image_dimension"] == 94)
check("first-action fence", registry["first_action_composition"]["available_source_variable_dimension"] == 34
      and registry["first_action_composition"]["required_common_field_dimension"] == 125
      and registry["first_action_composition"]["direct_sum_admissible"] is False)
check("parent fence", registry["action_parents"] == {
    "selected_spin_native_dimension": 2107,
    "two_U32_32_halves_dimension": 16382,
    "full_U64_64_dimension": 16383,
    "collapsed": False,
})
check("controls", registry["controls"]["primary"] == "52/52 PASS"
      and registry["controls"]["independent_sage_flint"] == "31/31 PASS")
check("data fence", registry["controls"]["P1_P2_P3_unused"] is True)

check("report scope", "principal" in report.lower() and "125" in report
      and "does not close the full action" in report)
check("review verdict", "SURVIVES_WITH_SCOPE_NARROWING__PRINCIPAL_SELECTED_SPIN_NATIVE_BANK_ONLY" in review)
check("required reviews", "Layer-0 semantics" in review and "Analytic/Krein" in review
      and "Symplectic" in review and "Variational" in review)

check("ledger ancestry", reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.105.json"))

if FAILURES:
    raise SystemExit("FAIL selected K77 primitive epsilon bank audit: " + "; ".join(FAILURES))
print("PASS selected K77 primitive epsilon common bank audit")
