#!/usr/bin/env python3
"""Fail-closed process audit for conditional-physics ledger v0.114."""

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


ledger = load("lab/process/conditional-physics-ledger-v0.114.json")
registry = load("lab/process/selected-k77-branch-bfv-no-selector.json")
contract = load("lab/methods/research-evidence-contract-v1.0.json")
report = read("explorations/conditional-build/selected-k77-branch-bfv-no-selector-2026-08-09.md")
review = read("lab/process/hostile-reviews/2026-08-09-selected-k77-branch-bfv-no-selector-review.md")
source = read("lab/sources/selected-k77-branch-bfv-source-reinspection-2026-08-09.md")

check("ledger version", ledger["schema_version"] == "0.114")
check("predecessor", ledger["predecessor"].endswith("v0.113.json"))
check("coverage", ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("verdicts", ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("frontier", ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 2,
    "conditions_opened": 1, "remaining_named_conditions": 3})
check("residue", ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == 5)
check("source return", ledger["source_return"] == registry["source_return"]
      and "SOURCE_CONFIRMS" in ledger["source_return"]
      and "SOURCE_SILENT" in ledger["source_return"])

symp = registry["branch_symplectic_equivalence"]
check("branch amplitudes", symp["both_nonzero"] is True
      and symp["opposite_real_signs"] is True)
check("symplectic equivalence", symp["vertical_polarization_preserved"] is True
      and symp["strongness_preserved"] is True
      and symp["selects_branch_or_amplitude"] is False)
check("edge amplitudes", symp["minimal_edge_coefficients"] == [-1, 1]
      and symp["edge_coefficients_amplitude_independent"] is True)

bfv = registry["classical_edge_bfv"]
check("BFV scope", bfv["scope"]
      == "EACH_DECLARED_NONEMPTY_COMPACT_BOUNDARY_EDGE_TORSOR_STRATUM")
check("BFV charge", "mu_a" in bfv["charge"] and "f_ab" in bfv["charge"]
      and "TSTAR_H7" in bfv["coisotropic_ambient"]
      and "REORIENTS_RECORDED_MINUS" in bfv["constraints"])
check("classical CME", bfv["constraint_closure_defects"] == 0
      and bfv["jacobi_defects"] == 0
      and bfv["classical_master_equation"] == "EXACT_COMPONENTWISE")
check("nonabelian plant", "OMISSION_PLANT_FAILS" in bfv["cubic_ghost_term"])
check("both branches close", bfv["branch_plus_closes"] is True
      and bfv["branch_minus_closes"] is True
      and bfv["selects_branch"] is False)
check("open fences", all(value == "OPEN" for value in registry["analytic_fence"].values()))
check("parents separate", registry["action_parent_fence"]["selected"] is False
      and set(registry["action_parent_fence"]) == {
          "spin_native_selected_carrier", "two_u32_32_halves", "full_u64_64", "selected"})
check("controls", registry["controls"]["primary"] == "49/49 PASS"
      and registry["controls"]["independent_sage"] == "21/21 PASS"
      and registry["controls"]["v0103_replay"] == "59/59 PASS"
      and registry["controls"]["v0113_replay"] == "51/51 PASS")

migrated = ["LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR2d",
            "LT-GR3", "LT-GR5", "LT-GR6"]
rows = {row["id"]: row for row in ledger["rows"]
        if row.get("row_status") != "SUPERSEDED"}
for row_id in migrated:
    check(f"{row_id} evidence", rows[row_id]["evidence"]
          == "selected-k77-branch-bfv-no-selector-2026-08-09.md")
migrations = [m for m in ledger["migrations"]
              if m["from_version"] == "0.113" and m["to_version"] == "0.114"]
check("seven migrations", [m["row_id"] for m in migrations] == migrated)
check("no meaning changes", all(m["meaning_changed"] is False for m in migrations))

check("report typing", "v0.103 constructed" in report
      and "classical BFV charge" in report
      and "does not prove" in report)
check("source typing", "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source)
check("review verdict", "CANDIDATE_SURVIVES__CLASSICAL_STRATUMWISE_EDGE_BFV_ONLY" in review)
for lens in ("Symplectic", "BFV/BRST", "Functional/PDE", "Gauge geometry",
             "Representation/Clifford", "Complex/path integral", "Source"):
    check(f"review lens {lens}", lens in review)

check("ledger ancestry", reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.114.json"))

if FAILURES:
    raise SystemExit("FAIL selected K77 branch BFV no-selector audit: "
                     + "; ".join(FAILURES))
print("PASS selected K77 branch BFV no-selector audit")
