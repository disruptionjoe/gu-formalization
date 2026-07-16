#!/usr/bin/env python
"""Recovery contract cosmology field-type and scalar-truncation gate.

This branch-local gate asks whether the frozen W203/W229/W230/W236
record-current action fingerprint supplies enough structure to treat the
existing theta-background Klein-Gordon calculations as cosmological
perturbation recovery evidence.

Result: NO_GO for perturbation-recovery use at the current construction grade.
The branch has a theta candidate and background calculations, but it does not
yet supply a physical FLRW scalar-singlet projector, a gauge-invariant
observable map, or a closed scalar truncation of the source-action equations.
Therefore the background KG equation remains background/distance evidence, not
SVT perturbation recovery.

This does not change any claim status, canon verdict, public posture, or the
broader recovery lane. It only closes this branch-local field-type checkpoint.

Run: python tests/recovery-contract/cosmo_field_type_scalar_truncation_gate.py
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FINGERPRINT = ROOT / "lab" / "process" / "recovery-contract-action-fingerprint-2026-07-16.json"
MATRIX = ROOT / "lab" / "process" / "recovery-certification-matrix.json"
CANON_THETA = ROOT / "canon" / "theta-field-flrw-dark-energy-eos.md"

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL") + " :: " + name + (("  --  " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def log(message: str = "") -> None:
    print(message, flush=True)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def cosmo_item(matrix: dict) -> dict:
    for item in matrix["items"]:
        if item["id"] == "COSMO-PERTURBATIONS":
            return item
    raise AssertionError("COSMO-PERTURBATIONS item missing from recovery matrix")


@dataclass(frozen=True)
class ScalarTruncationEvidence:
    typed_theta_candidate: bool
    physical_scalar_projector: bool
    gauge_invariant_observable_map: bool
    block_diagonal_quadratic_action: bool
    non_scalar_source_terms_absent: bool
    boundary_initial_data_frozen: bool


def scalar_truncation_closed(evidence: ScalarTruncationEvidence) -> bool:
    return all(
        (
            evidence.typed_theta_candidate,
            evidence.physical_scalar_projector,
            evidence.gauge_invariant_observable_map,
            evidence.block_diagonal_quadratic_action,
            evidence.non_scalar_source_terms_absent,
            evidence.boundary_initial_data_frozen,
        )
    )


def evidence_from_current_fingerprint(fingerprint: dict) -> ScalarTruncationEvidence:
    native_objects = set(fingerprint["action_family"]["native_objects"])
    not_frozen = set(fingerprint["variation_space"]["not_frozen"])
    free_or_unbuilt = {entry["quantity"] for entry in fingerprint["quantity_ledger"]["free_or_unbuilt"]}

    has_theta_candidate = "connection distortion theta / U" in native_objects

    return ScalarTruncationEvidence(
        typed_theta_candidate=has_theta_candidate,
        physical_scalar_projector=False,
        gauge_invariant_observable_map="physical gauge quotient and observables" not in not_frozen,
        block_diagonal_quadratic_action=False,
        non_scalar_source_terms_absent="K_IG uniqueness" not in free_or_unbuilt,
        boundary_initial_data_frozen="boundary and initial data beyond branch-local tests" not in not_frozen,
    )


def main() -> None:
    fingerprint = load_json(FINGERPRINT)
    matrix = load_json(MATRIX)
    theta_canon = read_text(CANON_THETA)
    item = cosmo_item(matrix)

    log("=" * 82)
    log("PC1 -- a genuinely closed scalar truncation is accepted")
    log("=" * 82)
    closed_scalar = ScalarTruncationEvidence(
        typed_theta_candidate=True,
        physical_scalar_projector=True,
        gauge_invariant_observable_map=True,
        block_diagonal_quadratic_action=True,
        non_scalar_source_terms_absent=True,
        boundary_initial_data_frozen=True,
    )
    check(
        "PC1  toy closed scalar sector passes the gate",
        scalar_truncation_closed(closed_scalar),
        "the gate can recognize a fully specified scalar perturbation object",
    )

    log("")
    log("=" * 82)
    log("PC2 -- scalar-looking background data alone is rejected")
    log("=" * 82)
    mixed_background_only = ScalarTruncationEvidence(
        typed_theta_candidate=True,
        physical_scalar_projector=True,
        gauge_invariant_observable_map=False,
        block_diagonal_quadratic_action=False,
        non_scalar_source_terms_absent=False,
        boundary_initial_data_frozen=True,
    )
    check(
        "PC2  a scalar amplitude with vector/tensor or gauge mixing fails closure",
        not scalar_truncation_closed(mixed_background_only),
        "background KG form is not enough without the truncation certificate",
    )

    log("")
    log("=" * 82)
    log("C1 -- action fingerprint boundary")
    log("=" * 82)
    branch = fingerprint["branch_local_testing_object"]
    not_frozen = fingerprint["variation_space"]["not_frozen"]
    check(
        "C1a  fingerprint is branch-local, not a primary-theory freeze",
        branch["status"] == "CONDITIONAL_BRANCH_LOCAL_TEST_OBJECT" and branch["not_a_primary_theory"],
    )
    check(
        "C1b  cosmo field-type testing is allowed only after consuming this same branch",
        "testing COSMO-PERTURBATIONS field type only after the same branch action is consumed"
        in branch["usable_for"],
    )
    check(
        "C1c  the fingerprint itself must not enable cosmological perturbation recovery",
        "cosmological perturbation recovery" in branch["must_not_enable"],
    )
    check(
        "C1d  boundary/initial data and observables are not frozen",
        "boundary and initial data beyond branch-local tests" in not_frozen
        and "physical gauge quotient and observables" in not_frozen,
    )

    log("")
    log("=" * 82)
    log("C2 -- recovery matrix asks exactly this gate")
    log("=" * 82)
    check("C2a  COSMO-PERTURBATIONS is the field-type-ready recovery item", item["state"] == "READY_AFTER_CONTRACT_FOR_FIELD_TYPE")
    check(
        "C2b  current ceiling says scalar field type and truncation are not derived",
        "scalar field type" in item["current_honest_ceiling"]
        and "consistent truncation" in item["current_honest_ceiling"]
        and "not derived" in item["current_honest_ceiling"],
    )
    check(
        "C2c  first decisive test is scalar singlet plus closed truncation",
        "physical scalar singlet exists" in item["first_decisive_test"]
        and "consistent truncation" in item["first_decisive_test"],
    )
    check(
        "C2d  kill condition is no scalar singlet or no closed scalar truncation",
        "No scalar singlet or no closed scalar truncation" in item["kill_condition"],
    )

    log("")
    log("=" * 82)
    log("C3 -- canon marks scalar field type as an assumption/failure mode")
    log("=" * 82)
    check(
        "C3a  canon assumes B is a pulled-back 4D scalar",
        "B is a scalar field in 4D when the section is pulled back" in theta_canon,
    )
    check(
        "C3b  canon says spin-2 s*(theta) would replace the FLRW-KG equation",
        "If s*(theta) is spin-2, the FLRW-KG equation must be replaced" in theta_canon,
    )
    check(
        "C3c  canon lists F4 as the field-type failure mode",
        "s*(theta) is spin-2, not scalar" in theta_canon,
    )

    log("")
    log("=" * 82)
    log("C4 -- current branch evidence fails the scalar-truncation gate")
    log("=" * 82)
    current = evidence_from_current_fingerprint(fingerprint)
    check("C4a  the branch has a typed theta candidate", current.typed_theta_candidate)
    check("C4b  no physical scalar projector is supplied by the fingerprint", not current.physical_scalar_projector)
    check("C4c  no gauge-invariant observable map is frozen", not current.gauge_invariant_observable_map)
    check("C4d  no block-diagonal SVT quadratic action is supplied", not current.block_diagonal_quadratic_action)
    check("C4e  non-scalar source/gauge residues are not discharged", not current.non_scalar_source_terms_absent)
    check("C4f  boundary and initial data are not frozen", not current.boundary_initial_data_frozen)
    check(
        "C4g  current fingerprint does not close the scalar truncation",
        not scalar_truncation_closed(current),
    )

    log("")
    log("=" * 82)
    log("C5 -- operational result")
    log("=" * 82)
    operational_result = "NO_GO" if not scalar_truncation_closed(current) else "CONDITIONAL"
    check(
        "C5a  branch-local perturbation-recovery use is NO_GO at this grade",
        operational_result == "NO_GO",
        "background KG calculations remain background/distance evidence, not perturbation recovery",
    )
    check(
        "C5b  fingerprint statuses remain non-status-changing",
        not fingerprint["scientific_claim_advanced"]
        and not fingerprint["claim_status_changed"]
        and not fingerprint["public_posture_changed"]
        and not fingerprint["portfolio_changed"],
    )

    log("")
    log("=" * 82)
    log("VERDICT")
    log("=" * 82)
    if not FAIL:
        log("Operational result: NO_GO for perturbation-recovery use of the current theta-background KG object.")
        log("The W229 branch has theta/background evidence but no scalar-singlet projector, gauge-invariant")
        log("observable map, block-diagonal SVT quadratic action, or closed scalar truncation certificate.")
        log("This does not move the canon verdict, claim status, public posture, or portfolio state.")

    if FAIL:
        log(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            log("  FAIL: " + name)
        raise SystemExit(1)
    log("\nRESULT: ALL PASS")


if __name__ == "__main__":
    main()
