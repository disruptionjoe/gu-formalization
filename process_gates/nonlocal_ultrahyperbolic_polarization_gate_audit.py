#!/usr/bin/env python3
"""Fail-closed scope audit for the v0.170 nonlocal polarization gate."""

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


prior = strict("lab/process/conditional-physics-ledger-v0.169.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.170.json")
result = strict("lab/process/selected-k77-nonlocal-ultrahyperbolic-polarization-gate.json")
report = read("explorations/conditional-build/selected-k77-nonlocal-ultrahyperbolic-polarization-gate-2026-08-11.md")
review = read("lab/process/hostile-reviews/2026-08-11-selected-k77-nonlocal-ultrahyperbolic-polarization-gate-review.md")
source = read("lab/sources/selected-k77-nonlocal-ultrahyperbolic-polarization-gate-source-return-2026-08-11.md")
lanes = read("LANES.yaml")
next_steps = read("NEXT-STEPS.md")
status = read("RESEARCH-STATUS.md")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")

check("ledger advances exactly once", ledger["schema_version"] == "0.170" and ledger["predecessor"].endswith("v0.169.json"))
check("headline counts unchanged", ledger["progress"]["verdict_counts"] == prior["progress"]["verdict_counts"])
check("coverage remains 82 of 82", ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("residue remains 84", ledger["residue"]["continuous_real"] == prior["residue"]["continuous_real"] == 84)
check("five scoped quotients remain", ledger["residue"]["quotients_ranked"] == prior["residue"]["quotients_ranked"] == 5)
check("frontier closes two conditions", ledger["frontier_delta"]["conditions_closed"] == 2)
check("frontier honestly opens four compatibility gates", ledger["frontier_delta"]["conditions_opened"] == 4)
check("scalar donor is not promoted to matrix theorem", result["craig_weinstein"]["alone_repairs_gu_jordan_defect"] is False)
check("actual current operator is tested", result["exact_real_k77"]["operator_dimension"] == 1920)
check("center scalar support retains rank 128 defect", result["exact_real_k77"]["center_jordan_remainder_rank_each"] == 128)
check("matrix polarization is exact", result["gu_matrix_polarization"]["N"] == "E(k)^2-rho(k)^2 I")
check("polarization kernel dimension is 1792", result["gu_matrix_polarization"]["kernel_dimension"] == 1792)
check("strict-center generalized chains are removed", result["gu_matrix_polarization"]["removes_generalized_chains_on_strict_center_cone"] is True)
check("complete observation rank remains", result["gu_matrix_polarization"]["observed_four_vector_plus_nu_rank_retained"] == 640)
check("source selection is absent", result["gu_matrix_polarization"]["source_selected"] is False)
check("action Green remains open", result["open"]["selected_action_compatibility"] and result["open"]["green_isotropy_or_coisotropy"])
check("BFV overlap and nonlinear remain open", result["open"]["bfv_compatibility"] and result["open"]["curved_pseudodifferential_overlap_completion"] and result["open"]["nonlinear_constraint_propagation"])
check("P1 P2 P3 remain unused", result["accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED")
check("six rows migrate", len(ledger["wave_row_dispositions"]) == 6)
check("expected rows migrate", {item["row_id"] for item in ledger["wave_row_dispositions"]} == {"RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"})
check("source return separates the two Weinsteins", "Walter Craig and Steven Weinstein" in source and "Eric Weinstein source" in source)
check("source return records GU silence", "SOURCE-SILENT" in source)
check("hostile charge one blocks the scalar overclaim", "Craig--Weinstein repairs GU" in review)
check("hostile charge two separates support from polarization", "polynomial kernel" in review and "nonlocal support projector" in review)
check("hostile charge three retains live gates", "needs-recheck" in review and "dissolved`: none" in review)
check("human report says conditional rather than physical", "conditional flat principal-domain ingredient" in report)
check("lanes points at v0.170", "conditional-physics-ledger-v0.170.json" in lanes)
check("contract points at v0.170", contract["standing_ledger"]["ref"].endswith("v0.170.json"))
check("next steps names Green successor", "strict-center" in next_steps and "Green" in next_steps)
check("research status carries scoped result", "conditional flat principal-domain ingredient" in status)
check("canon and public posture do not move", result["accounting"]["canon_change"] is False and result["accounting"]["public_posture_change"] is False)

print(f"PASS: {CHECKS}/{CHECKS} nonlocal ultrahyperbolic polarization process checks")
