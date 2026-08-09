#!/usr/bin/env python3
"""Fail-closed process audit for conditional-physics ledger v0.104."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
FAILURES = []


def check(label, condition):
    if not condition:
        FAILURES.append(label)


def unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"), object_pairs_hook=unique)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


ledger = load("lab/process/conditional-physics-ledger-v0.104.json")
registry = load("lab/process/selected-k77-stationary-gram-boundary-strata.json")
contract = load("lab/process/functional-channel-operating-contract-v1.0.json")
report = read("explorations/conditional-build/selected-k77-stationary-gram-boundary-strata-2026-08-08.md")
review = read("lab/process/hostile-reviews/2026-08-08-selected-k77-stationary-gram-boundary-strata-review.md")

check("ledger schema", ledger["schema_version"] == "0.104")
check("ledger predecessor", ledger["predecessor"].endswith("v0.103.json"))
check("coverage", ledger["progress"]["mapped"] == 82 and ledger["progress"]["total"] == 82)
check("verdicts", ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5
})
check("frontier", ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 4,
    "conditions_opened": 1, "remaining_named_conditions": 4
})
check("source return", "SOURCE-CONFIRMS_RESIDUAL_NORM_SQUARE" in ledger["source_return"]
      and "SOURCE_SILENT" in ledger["source_return"])

required_layer0 = {
    "RECTANGULAR_34_TO_1470_RAW_RESIDUAL_PRINCIPAL_MAP",
    "COVECTOR_VALUED_PARTIAL_STATIONARY_GRAM_A_TRANSPOSE_KLOC_A",
    "FIELD_VALUED_OPERATOR_ADJOINT_REQUIRING_FIELD_RIESZ",
    "NONNULL_PARTIAL_GRAM_RANK22_TRACE_QUOTIENT44",
    "NULL_PARTIAL_GRAM_RANK14_TRACE_QUOTIENT28",
    "NULL_ISOTROPIC_IMAGE_EXCESS8",
    "SOBOLEV_REGULARITY_COMPATIBILITY_WITH_H7_HMINUS7",
    "EDGE_DISTORTION_CARRIER_SOLDERING_MAP",
    "INDEPENDENT_PRIMITIVE_EPSILON_RESIDUAL_COLUMNS",
    "FULL_FIRST_PLUS_SECOND_ACTION_COMMON_STATIONARY_SYMBOL",
    "TANGENTIAL_COLLAR_OPERATOR_AND_MAXIMAL_DOMAIN",
}
check("layer0", required_layer0 <= set(ledger["layer0_objects_compared"]))

check("residue", ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == 5)
check("partial quotients unbooked", "not booked" in ledger["residue"]["quotients_ranked_scope"]
      and "44/44/28" in ledger["residue"]["quotients_ranked_scope"])
check("queue", ledger["next_work_queue"][0]["rows"] == ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"]
      and "independent-epsilon" in ledger["next_work_queue"][0]["why"])

rows = {row["id"]: row for row in ledger["rows"] if row.get("row_status") != "SUPERSEDED"}
for row_id in ("LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"):
    check(f"{row_id} evidence", rows[row_id]["evidence"] == "selected-k77-stationary-gram-boundary-strata-2026-08-08.md")
    check(f"{row_id} frontier", "GRAM_RANK22_22_14" in rows[row_id]["frontier_grade"]
          or "GRAM_RANK22_22_14" in rows[row_id]["mapping_grade"])

migrations = [m for m in ledger["migrations"] if m["from_version"] == "0.103" and m["to_version"] == "0.104"]
check("five migrations", [m["row_id"] for m in migrations] == ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"])
check("migration meanings", all(m["meaning_changed"] is False for m in migrations))

check("registry status", registry["status"] == "PARTIAL_STATIONARY_GRAM_STRATA_SURVIVE__FULL_COMMON_DOMAIN_OPEN")
check("ranks", [registry["exact_result"]["strata"][name]["gram_rank"]
                 for name in ("timelike", "spacelike", "null")] == [22, 22, 14])
check("inertias", [registry["exact_result"]["strata"][name]["inertia"]
                    for name in ("timelike", "spacelike", "null")]
      == [[12, 10, 12], [13, 9, 12], [8, 6, 20]])
check("trace dimensions", [registry["exact_result"]["strata"][name]["green_quotient_dimension"]
                            for name in ("timelike", "spacelike", "null")] == [44, 44, 28])
check("null isotropic", registry["exact_result"]["null_extra_isotropic_image_dimension"] == 8)
check("unbooked", registry["exact_result"]["quotient_booking"] == "UNBOOKED_DIAGNOSTIC")
check("controls", registry["controls"]["primary"] == "60/60 PASS"
      and registry["controls"]["independent_sage_flint"] == "34/34 PASS")
check("data fence", registry["controls"]["P1_P2_P3_unused"] is True)
check("parent fence", registry["action_parents"] == {
    "selected_spin_native_dimension": 2107,
    "two_U32_32_halves_dimension": 16382,
    "full_U64_64_dimension": 16383,
    "collapsed": False,
})

check("report scope", "does **not** build" in report and "full common GU domain" in report
      and "trace soldering" in report)
check("review verdict", "PARTIAL_STATIONARY_GRAM_STRATA_SURVIVE__FULL_COMMON_DOMAIN_AND_EDGE_CARRIER_IDENTIFICATION_REJECTED" in review)
check("required reviews", "Layer-0 semantics" in review and "Analytic" in review and "Symplectic" in review)

current_refs = [
    "LANES.yaml", "NEXT-STEPS.md", "RESEARCH-STATUS.md", "explorations/README.md",
    "lab/process/README.md", "lab/process/agent-context-pack.md",
    "lab/process/functional-channel-operating-contract-v1.0.md",
]
for relative in current_refs:
    check(f"current pointer {relative}", "v0.104" in read(relative))
check("contract pointer", contract["standing_ledger"]["ref"].endswith("v0.104.json"))
check("contract next gate", contract["active_scientific_directives"][0]["next_gate"] == registry["next_gate"])

python_count = len(list((ROOT / "tests/channel-swings").glob("*.py")))
sage_count = len(list((ROOT / "tests/channel-swings").glob("*.sage")))
check("inventory prose", f"({python_count} Python + {sage_count} Sage)" in read("tests/README.md"))

if FAILURES:
    raise SystemExit("FAIL selected K77 stationary Gram strata audit: " + "; ".join(FAILURES))
print("PASS selected K77 stationary Gram strata audit")
