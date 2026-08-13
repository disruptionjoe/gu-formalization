#!/usr/bin/env python3
"""Fail-closed scope audit for the v0.171 polarized Green-dual gate."""

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


prior = strict("lab/process/conditional-physics-ledger-v0.170.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.171.json")
result = strict("lab/process/selected-k77-polarized-green-dual-gate.json")
report = read("explorations/conditional-build/selected-k77-polarized-green-dual-gate-2026-08-11.md")
review = read("lab/process/hostile-reviews/2026-08-11-selected-k77-polarized-green-dual-gate-review.md")
source = read("lab/sources/selected-k77-polarized-green-dual-gate-source-return-2026-08-11.md")
lanes = read("lab/process/RESEARCH-AGENDA.json")
next_steps = read("NEXT-STEPS.md")
status = read("RESEARCH-STATUS.md")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")

check("ledger advances exactly once", ledger["schema_version"] == "0.171" and ledger["predecessor"].endswith("v0.170.json"))
check("headline counts unchanged", ledger["progress"]["verdict_counts"] == prior["progress"]["verdict_counts"])
check("coverage remains 82 of 82", ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82)
check("residue remains 84", ledger["residue"]["continuous_real"] == prior["residue"]["continuous_real"] == 84)
check("five scoped quotients remain", ledger["residue"]["quotients_ranked"] == prior["residue"]["quotients_ranked"] == 5)
check("frontier closes the direct Green compatibility question", ledger["frontier_delta"]["conditions_closed"] == 1)
check("frontier opens owned quotient and modified-observation demands", ledger["frontier_delta"]["conditions_opened"] == 2)
check("actual carrier dimension is retained", result["exact_real_k77"]["carrier_dimension_each_field"] == 1920)
check("actual normal coefficient is used", "four-field" in result["exact_real_k77"]["normal_green_coefficient"])
check("Green adjoint identity is exact", result["exact_real_k77"]["green_adjoint_identity_exact"] is True)
check("both polarizations remain square-zero", result["exact_real_k77"]["N_and_Nsharp_square_zero"] is True)
check("direct dual kernel has left radical 128", result["direct_dual_kernel"]["left_radical_dimension"] == 128)
check("direct dual kernel has right radical 128", result["direct_dual_kernel"]["right_radical_dimension"] == 128)
check("direct dual kernel is not promoted", result["direct_dual_kernel"]["nondegenerate"] is False)
check("observed-x dual kernel rank drop is recorded", result["direct_dual_kernel"]["naive_barred_observation_ranks"]["observed_x"] == 512)
check("perfect algebraic dual has dimension 1792", result["perfect_algebraic_dual"]["dimension"] == 1792)
check("perfect dual is not called gauge or BV", result["perfect_algebraic_dual"]["source_or_action_owned_as_gauge_or_bv"] is False)
check("observation is live on quotient directions", result["perfect_algebraic_dual"]["naive_observation_rank_on_quotient_directions_each"] == 128)
check("naive observation does not descend", result["perfect_algebraic_dual"]["naive_observation_descends"] is False)
check("one-sided ingredient remains explicit", "ONE_SIDED" in result["status"])
check("action BV match remains open", result["open"]["action_owned_characteristic_or_bv_image_match"] is True)
check("moving Green and observation remain open", result["open"]["full_moving_boson_fermion_preboundary_form"] and result["open"]["modified_observation_basicness"])
check("six rows migrate", len(ledger["wave_row_dispositions"]) == 6)
check("expected rows migrate", {item["row_id"] for item in ledger["wave_row_dispositions"]} == {"RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"})
check("source confirms independent dual fields", "SOURCE-CONFIRMS" in source and "independent" in source)
check("source silence is explicit", "SOURCE-SILENT" in source and "Nsharp" in source)
check("hostile charge one prevents action-domain overclaim", "one-sided principal evolution" in review)
check("hostile charge two prevents BV relabeling", "silently" in review and "gauge" in review)
check("hostile charge three keeps operator completion separate", "operator-completion" in review)
check("symplectic lens is explicit", "symplectic" in review and "coisotropic" in review)
check("human report records scoped adverse result", "scoped adverse" in report.lower())
check("lanes points at v0.171", "conditional-physics-ledger-v0.171.json" in lanes)
check("contract points at v0.171", contract["standing_ledger"]["ref"].endswith("v0.171.json"))
check("next steps names owned-image successor", "im Nsharp" in next_steps and "moment map" in next_steps)
check("research status carries the nonbasic quotient", "does not descend" in status and "rank-128" in status)
check("P1 P2 P3 remain unused", result["accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED")
check("canon and public posture do not move", result["accounting"]["canon_change"] is False and result["accounting"]["public_posture_change"] is False)

print(f"PASS: {CHECKS}/{CHECKS} polarized Green-dual process checks")
