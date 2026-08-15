#!/usr/bin/env python3
"""Exact coverage probe for the selected-K77 SR-1H carrier census."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CHECKS = 0


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def check(label: str, condition: bool) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


registry = load("lab/process/selected-k77-sr1h-action-owned-point-carrier-census.json")
rows = {row["id"]: row for row in registry["census"]}
expected = {
    "CANONICAL_ZORRO_ZERO_T",
    "HOMOGENEOUS_NONZERO_T_SOURCE_BRANCHES",
    "CANONICAL_BZ_NONZERO_T_ROOTS",
    "SOURCE_INSTABILITY_VERTICAL_CARRIER",
    "SCALAR_CURVATURE_VEV_TRACE_BRANCH",
}
check("exact five-class census", set(rows) == expected)
check("five classes", registry["coverage"]["serialized_candidate_classes"] == 5)
check("seven instances", registry["coverage"]["serialized_candidate_instances"] == 7)

zero_t = load(rows["CANONICAL_ZORRO_ZERO_T"]["evidence"])
check("zero-T disposition", rows["CANONICAL_ZORRO_ZERO_T"]["disposition"] == "KILLED_ACTION_TWO_JET")
check("zero-T registry kill", "OBSTRUCTED" in zero_t["status"])
check("zero-T 9555 repairs", zero_t["symmetric_dt_affine_system"]["variables"] == 9555)
check("zero-T inconsistent", zero_t["symmetric_dt_affine_system"]["consistent"] is False)
check("zero-T certificate 14", zero_t["symmetric_dt_affine_system"]["cokernel_certificate_support"] == 14)

hom = load(rows["HOMOGENEOUS_NONZERO_T_SOURCE_BRANCHES"]["evidence"])
check("homogeneous multiplicity", rows["HOMOGENEOUS_NONZERO_T_SOURCE_BRANCHES"]["multiplicity"] == 2)
check("homogeneous owned branches", hom["owned_nonzero_t_branches"] == 2)
check("homogeneous canonical empty", hom["canonical_zorro_intersection"]["currently_owned_homogeneous_intersection"] == "EMPTY")
check("homogeneous all nine plus", hom["canonical_zorro_intersection"]["plus_branch_nonzero_planes"] == 9)
check("homogeneous all nine minus", hom["canonical_zorro_intersection"]["minus_branch_nonzero_planes"] == 9)
check("source-global open", hom["source_global_zorro_disposition"].startswith("OPEN"))

roots = load(rows["CANONICAL_BZ_NONZERO_T_ROOTS"]["evidence"])
check("canonical roots multiplicity", rows["CANONICAL_BZ_NONZERO_T_ROOTS"]["multiplicity"] == 2)
check("canonical roots killed", "BOTH_ROOTS_KILLED" in roots["status"])
check("affine variables", roots["affine_first_jet"]["variables"] == 9555)
check("affine kernel", roots["affine_first_jet"]["kernel_dimension"] == 5265)
check("direct parity support zero", roots["parity_certificate"]["direct_support"] == 0)
check("Hodge parity support zero", roots["parity_certificate"]["hodge_support"] == 0)
check("density trace survives", roots["joint_fibre"]["density_trace"] == "NONZERO_ON_BOTH_ROOTS")

instability = load(rows["SOURCE_INSTABILITY_VERTICAL_CARRIER"]["evidence"])
check("instability killed", "KILLED_FOR_VRS5" in instability["status"])
check("fixed repair killed", instability["composed_boundedness"]["fixed_natural_repair"] == "KILLED_SR1E")
check("observer repair killed", instability["composed_boundedness"]["observer_Q_u_repair"] == "KILLED_SR1F")
check("constraint unowned", instability["composed_boundedness"]["source_constraint_repair"] == "NOT_OWNED")
check("higher even unowned", instability["composed_boundedness"]["source_higher_even_repair"] == "NOT_OWNED")

scalar = load(rows["SCALAR_CURVATURE_VEV_TRACE_BRANCH"]["evidence"])
check("scalar omission control", rows["SCALAR_CURVATURE_VEV_TRACE_BRANCH"]["disposition"] == "INELIGIBLE_CANONICAL_REALISATION_OPEN")
check("scalar closure owned", "ACTION_OWNED_SCALAR_JET_TRACE_CLOSURE_CONFIRMED" in scalar["status"])
check("scalar not proportional", scalar["canonical_intersection"]["proportional"] is False)
check("scalar amplitude miss", scalar["canonical_intersection"]["old_amplitude_in_sr1c_polynomial"] == "-1397/4")
check("scalar canonical open", scalar["old_scalar_branch"]["status"].endswith("CANONICAL_REALISATION_OPEN"))
check("old graft illegal", scalar["canonical_intersection"]["direct_graft_legal"] is False)

coverage = registry["coverage"]
check("two canonical admitted classes", coverage["canonical_geometry_admitted_classes"] == 2)
check("zero stationarity survivors", coverage["full_local_stationarity_survivors"] == 0)
check("zero eligible backgrounds", coverage["eligible_vrs5_backgrounds"] == 0)
check("future not counted", coverage["unconstructed_future_classes_counted_as_current"] == 0)
check("six reopeners", len(registry["unconstructed_reopeners"]) == 6)
check("rival Zorro open", "DERIVED_RIVAL_ZORRO_CONNECTION_AND_METRIC" in registry["unconstructed_reopeners"])
check("nonzero fermion open", "NONZERO_FERMION_COUPLED_STATIONARY_SADDLE" in registry["unconstructed_reopeners"])

rerank = registry["hypothesis_rerank"]
check("historical votes preserved", rerank["historical_twenty_lens_votes_changed"] is False)
check("H0 first", rerank["first_current_truth_status"] == "H0_EXTERNAL_ORDINARY_QUANTIZATION")
check("HQ blocked not killed", "SURVIVES_BUT_BLOCKED" in rerank["H_Q_star"])
check("HB protected", rerank["H_B"].startswith("PROTECTED"))
check("HD protected", rerank["H_D"].startswith("PROTECTED"))
check("VRS5 scoped close", registry["vrs5"].startswith("CLOSED_AT_CURRENTLY_SERIALIZED"))
check("SR1 missing", registry["sr1"] == "BACKGROUND-MISSING")
check("VRS6 blocked", registry["vrs6"] == "BLOCKED")
check("RSAP first", registry["next_gate"].startswith("RSAP_LOCAL_98D"))

assert CHECKS == 48, CHECKS
print(f"selected_k77_sr1h_action_owned_point_carrier_census_probe: PASS {CHECKS}/48")
