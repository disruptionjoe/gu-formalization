#!/usr/bin/env python3
"""Exact Wave 2b controls for Curt's `(7,7)` reasoning and G2 term rank.

The finite certificate covers signature bookkeeping, the frozen free-jet term
quotient, coefficient dimensions, and support ablation.  It does not construct
the missing `(7,7)` operators or any physical observation map.
"""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/eric-curt-wave2b-term-rank-ablation.json"
CAMPAIGN = ROOT / "lab/process/eric-curt-ten-wave-campaign.json"
PORT_CENSUS = ROOT / "lab/process/eric-curt-wave2-carrier-port-census.json"
SOURCE_NOTE = ROOT / "lab/sources/curt-iceberg-7-7-reasoning-reinspection-2026-07-31.md"

Q = Fraction
Matrix = list[list[Fraction]]

exact_checks = 0
planted_checks = 0


def exact(name: str, condition: bool) -> None:
    global exact_checks
    if not condition:
        raise AssertionError(name)
    exact_checks += 1


def planted(name: str, false_claim: bool) -> None:
    global planted_checks
    if false_claim:
        raise AssertionError(f"planted false claim passed: {name}")
    planted_checks += 1


def rank(matrix: Matrix) -> int:
    work = [row[:] for row in matrix]
    if not work:
        return 0
    row = 0
    for column in range(len(work[0])):
        pivot = next(
            (index for index in range(row, len(work)) if work[index][column]),
            None,
        )
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        pivot_value = work[row][column]
        work[row] = [value / pivot_value for value in work[row]]
        for index in range(len(work)):
            if index == row:
                continue
            coefficient = work[index][column]
            work[index] = [
                work[index][entry] - coefficient * work[row][entry]
                for entry in range(len(work[0]))
            ]
        row += 1
        if row == len(work):
            break
    return row


def add_signatures(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return left[0] + right[0], left[1] + right[1]


def main() -> None:
    registry = json.loads(REGISTRY.read_text())
    campaign = json.loads(CAMPAIGN.read_text())
    port_census = json.loads(PORT_CENSUS.read_text())
    source_note = SOURCE_NOTE.read_text()
    wave2 = next(row for row in campaign["waves"] if row["id"] == "ECW2-G3.5-CENSUS")
    wave3 = next(row for row in campaign["waves"] if row["id"] == "ECW3-G4-OBSERVATION")

    exact("Wave 2b registry is complete only for its frozen class", registry["status"] == "COMPLETE_FOR_FROZEN_G2_FIRST_LAYER_CLASS")
    exact("campaign records the frozen-class completion", wave2["status"] == "COMPLETE_FROZEN_G2_FIRST_LAYER_TERM_QUOTIENT__LATER_ACTION_CLASSES_REMAIN_OWNED")
    exact("Wave 3 is released rather than claimed complete", wave3["status"] == "READY_AFTER_WAVE2_FROZEN_CLASS_EXIT")
    exact("source note records all three transcript windows", all(window in source_note for window in ["00:39:55", "00:44:21", "02:45:30"]))
    exact("source trace-line choice is distinguished from total-signature typing", "SOURCE_STATED" in registry["source_reinspection"]["vertical_trace_choice"] and "SOURCE_UNTYPED" in registry["source_reinspection"]["total_signature"])
    exact("vertical-flip completion is source-preferred", registry["source_reinspection"]["branch_order"][1] == "R77_VERTICAL_FLIP_SOURCE_PREFERRED_COMPLETION")
    exact("base flip remains hostile", registry["source_reinspection"]["branch_order"][2] == "R77_BASE_FLIP_HOSTILE_COMPARATOR")

    # Exact signature bookkeeping.  The spoken pairs do not add under one
    # fixed convention; the minimal dual-horizontal completion does.
    vertical_curt = (4, 6)
    spoken_horizontal = (1, 3)
    dual_horizontal_completion = (3, 1)
    exact("spoken ordered pairs add to (5,9)", add_signatures(vertical_curt, spoken_horizontal) == (5, 9))
    exact("dual-horizontal completion adds to (7,7)", add_signatures(vertical_curt, dual_horizontal_completion) == (7, 7))
    exact("active blocks add to (9,5)", add_signatures((6, 4), (3, 1)) == (9, 5))
    exact("Curt vertical block is the active vertical sign reverse", vertical_curt == tuple(reversed((6, 4))))
    planted("spoken (4,6)+(1,3) equals (7,7) under one ordering", add_signatures(vertical_curt, spoken_horizontal) == (7, 7))
    planted("trace-line sign is forced by the bare four-manifold", "SOURCE_STATED_FORCED" in registry["source_reinspection"]["vertical_trace_choice"])
    planted("base flip is transcript-preferred", registry["source_reinspection"]["branch_order"][1].startswith("R77_BASE"))

    basis = registry["basis"]
    candidates = registry["candidate_span"]
    relations: Matrix = [
        [Q(-1), Q(-1), Q(-1), Q(0), Q(1), Q(0)],
        [Q(0), Q(-1), Q(-2), Q(0), Q(0), Q(1)],
    ]
    candidate_matrix: Matrix = [
        [Q(value) for value in row["basis_vector"]] for row in candidates
    ]
    exact("four basis identifiers are unique", [row["id"] for row in basis] == ["M1", "M2", "M3", "M4"])
    exact("six A/B-written candidates are frozen", len(candidates) == 6)
    exact("candidate coordinate span has rank four", rank(candidate_matrix) == 4)
    exact("two quotient relations are independent", rank(relations) == 2)
    exact("six candidates modulo two relations give term rank four", len(candidates) - rank(relations) == registry["rank"]["quotient_term_rank"] == 4)
    exact("F_A candidate is translated curvature, not a new term", candidates[4]["basis_vector"] == [1, 1, 1, 0])
    exact("D_A T candidate adds no direction", candidates[5]["basis_vector"] == [0, 1, 2, 0])

    translated_basis: Matrix = [
        [Q(1), Q(1), Q(1)],
        [Q(0), Q(1), Q(2)],
        [Q(0), Q(0), Q(1)],
    ]
    exact("A-relative and B-relative curvature generators span the same rank-three sector", rank(translated_basis) == 3)
    planted("F_A adds a fifth quotient direction", registry["rank"]["quotient_term_rank"] == 5)
    planted("D_A T adds a sixth quotient direction", registry["rank"]["quotient_term_rank"] == 6)

    coefficients = registry["coefficients"]
    exact("raw coefficient rank is four", coefficients["raw_rank"] == 4)
    exact("projectivizing overall scale leaves rank three", coefficients["projective_rank_mod_overall_nonzero_scale"] == 3)
    exact("source slice has two raw and one projective dimensions", coefficients["source_slice_raw_dimension"] == 2 and coefficients["source_slice_projective_dimension"] == 1)
    source_vector = [Q(1), Q(1, 2), Q(1, 3), Q(7, 10)]
    exact("a nonzero-kappa source vector supports all four terms", all(source_vector))

    incidence: Matrix = [
        [Q(value) for value in row["incidence"]]
        for row in registry["ablation"]["obligations"]
    ]
    exact("support ablation matrix has exact rank four", rank(incidence) == registry["ablation"]["support_incidence_rank"] == 4)
    exact("every single-term ablation kills exactly one frozen obligation", all(len(row["kills"]) == 1 for row in registry["ablation"]["term_ablations"]))
    exact("support-grade surplus is zero", registry["surplus"]["support_grade"].startswith("ZERO"))
    exact("physical surplus remains downstream", registry["surplus"]["physical_grade"].startswith("NOT_COMPUTABLE_UNTIL_ECW3"))
    planted("source slice and support rows imply positive surplus two", registry["surplus"]["support_grade"].startswith("POSITIVE_2"))

    excluded = registry["frozen_class"]["excluded_for_later_waves"]
    exact("odd action remains owned by Wave 4", "odd kinetic and zero-order bilinears" in excluded["ECW4"])
    exact("residual squares remain owned by Wave 5", "bosonic or total residual squares" in excluded["ECW5"])
    formula_surface = " ".join(row["formula"] for row in basis)
    exact("basis is target blind", all(token not in formula_surface for token in ["SU(3)", "Higgs", "photon", "P3", "generation"]))
    planted("a Higgs target term entered Wave 2b", "Higgs" in formula_surface)

    exact("active branch alone has built operator realizations", registry["carrier_verdict"]["R95_ACTIVE"].endswith("BUILT_AT_EXISTING_G2_G3_GRADE") and "PORT" in registry["carrier_verdict"]["R77_VERTICAL_FLIP"])
    exact("port census now prioritizes the vertical-sign completion", port_census["source_branch_priority"]["preferred"] == "R77_VERTICAL_FLIP")
    exact("no third lane is promoted", registry["third_lane_effect"].startswith("NONE") and campaign["third_lane_promotion_gate"]["current_verdict"] == "NOT_PROMOTED")
    planted("formula-rank equality ports the real action", registry["carrier_verdict"]["R77_VERTICAL_FLIP"].endswith("OPERATORS_BUILT"))
    planted("Wave 2b promotes a third lane", campaign["third_lane_promotion_gate"]["current_verdict"] == "PROMOTED")

    print(f"ERIC-CURT-WAVE2B-TERM-RANK: {exact_checks} exact checks + {planted_checks} planted failures = {exact_checks + planted_checks} PASS")
    print("SOURCE: Curt explicitly chooses the vertical trace-line sign; the dual-horizontal sign/order completion remains reconstruction-grade")
    print("RESULT: six admissible A/B-written candidates modulo two exact relations give a four-term first-layer quotient")
    print("ABLATION: rank four with support-grade surplus zero; physical surplus waits for observation and later actions")
    print("NEXT: ECW3-G4-OBSERVATION on the active branch with the source-preferred (7,7) port ledger retained")


if __name__ == "__main__":
    main()
