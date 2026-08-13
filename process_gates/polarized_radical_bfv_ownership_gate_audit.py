#!/usr/bin/env python3
"""Fail-closed scope audit for the v0.172 polarized-radical BFV gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKS = 0


def strict(relative: str):
    path = ROOT / relative

    def reject_duplicates(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise AssertionError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=reject_duplicates)


def read(relative: str) -> str:
    return (ROOT / relative).read_text()


def check(label: str, condition: object) -> None:
    global CHECKS
    CHECKS += 1
    assert condition, label
    print(f"PASS {label}")


prior = strict("lab/process/conditional-physics-ledger-v0.171.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.172.json")
result = strict("lab/process/selected-k77-polarized-radical-bfv-ownership-gate.json")
report = read("explorations/conditional-build/selected-k77-polarized-radical-bfv-ownership-gate-2026-08-11.md")
review = read("lab/process/hostile-reviews/2026-08-11-selected-k77-polarized-radical-bfv-ownership-gate-review.md")
source = read("lab/sources/selected-k77-polarized-radical-bfv-ownership-gate-source-return-2026-08-11.md")
lanes = read("LANES.yaml")
next_steps = read("NEXT-STEPS.md")
status = read("RESEARCH-STATUS.md")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")

check("ledger advances exactly once", ledger["schema_version"] == "0.172" and ledger["predecessor"].endswith("v0.171.json"))
check("headline counts unchanged", ledger["progress"]["verdict_counts"] == prior["progress"]["verdict_counts"])
check("coverage remains 82 of 82", ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("residue remains 84", ledger["residue"]["continuous_real"] == prior["residue"]["continuous_real"] == 84)
check("five scoped quotients remain", ledger["residue"]["quotients_ranked"] == prior["residue"]["quotients_ranked"] == 5)
check("frontier closes both ownership comparisons", ledger["frontier_delta"]["conditions_closed"] == 2)
check("frontier opens no replacement requirement", ledger["frontier_delta"]["conditions_opened"] == 0)
check("result is zero-fermion scoped", result["branch"] == "ZERO_FERMION_SELECTED_REAL_K77_CONDITIONAL")
check("im Nsharp rank is 128", result["green_radical"]["im_Nsharp_rank"] == 128)
check("pure barred carrier remains 1920", result["green_radical"]["pure_barred_carrier_dimension"] == 1920)
check("radical is observed", result["green_radical"]["observed_rank_each_strict_center_sample"] == 128)
check("independent-dual radical is 256", result["green_radical"]["direct_independent_dual_radical_dimension"] == 256)
check("zero-fermion gauge trace is zero", result["ordinary_gauge"]["zero_fermion_pure_barred_trace_rank"] == 0)
check("small-gauge boundary trace is zero", result["ordinary_gauge"]["small_gauge_complete_tangential_boundary_trace_rank"] == 0)
check("gauge image is not identified with im Nsharp", result["ordinary_gauge"]["equals_im_Nsharp"] is False)
check("unrestricted boundary symmetry remains charged", "CHARGED" in result["ordinary_gauge"]["unrestricted_boundary_before_edge"])
check("generic moving terms remain live", result["moving_preboundary"]["generic_mixed_terms"] == "LIVE")
check("zero-fermion moving terms vanish", result["moving_preboundary"]["zero_fermion_mixed_terms"] == "ZERO")
check("moving form does not lift the tested radical", result["moving_preboundary"]["lifts_polarized_fermion_radical_at_zero_fermion"] is False)
check("edge kernel is the owned rank twenty", result["existing_edge_completion"]["owned_gauge_kernel_dimension"] == 20)
check("existing edge completion has no fermion edge carrier", result["existing_edge_completion"]["fermionic_edge_carrier"] is False)
check("edge quotient leaves radical 256", result["existing_edge_completion"]["post_gauge_quotient_residual_fermion_kernel_dimension"] == 256)
check("edge construction does not own im Nsharp", result["existing_edge_completion"]["owns_im_Nsharp"] is False)
check("nonzero-fermion route remains open", result["open"]["nonzero_fermion_full_coupled_characteristic_comparison"] is True)
check("operator completion remains open", result["open"]["source_admitted_operator_completion"] is True)
check("six rows migrate", len(ledger["wave_row_dispositions"]) == 6)
check("expected rows migrate", {item["row_id"] for item in ledger["wave_row_dispositions"]} == {"RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"})
check("migration chain is exact", {item["from_version"] for item in ledger["migration_history"]} == {"0.171"} and {item["to_version"] for item in ledger["migration_history"]} == {"0.172"})
check("source confirms independent fields", "SOURCE_CONFIRMS" in source and "independent" in source)
check("source silence is explicit", "SOURCE_SILENT" in source and "Nsharp" in source)
check("hostile charge one keeps nonzero branch", "nonzero-fermion" in review and "survive" in review)
check("hostile charge two catches characteristic homonym", "word `characteristic`" in review)
check("hostile charge three lists dispositions", "dissolved" in review and "needs-recheck" in review)
check("symplectic lens is explicit", "Symplectic" in review and "charged" in review)
check("human report records zero-fermion scope", "zero-fermion" in report and "256-dimensional" in report)
check("lanes points at v0.172", "conditional-physics-ledger-v0.172.json" in lanes)
check("contract points at v0.172", contract["standing_ledger"]["ref"].endswith("v0.172.json"))
check("next steps promotes operator completion", "OPERATOR" in next_steps.upper() and "wedge-Shiab" in next_steps)
check("research status carries the surviving radical", "256-dimensional" in status and "zero-fermion" in status)
check("P1 P2 P3 remain unused", result["accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED")
check("canon and public posture do not move", result["accounting"]["canon_change"] is False and result["accounting"]["public_posture_change"] is False)

print(f"PASS: {CHECKS}/{CHECKS} polarized-radical BFV ownership process checks")
