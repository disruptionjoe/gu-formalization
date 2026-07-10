#!/usr/bin/env python3
"""Audit the Primary GU interface contract JSON block.

This is a structural contract audit, not a proof of the mathematics. It checks
that the interface file contains the required branch keys, claim keys,
compatibility matrix, and proof-certificate fields with real forbidden inputs.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "explorations" / "cycle-gates-and-audits" / "primary-gu-interface-contract-2026-06-24.md"

EXPECTED_BRANCH_KEYS = {
    "operator_spine",
    "background_stueckelberg",
    "constrained_ig_a_independent",
    "constrained_ig_a_dependent",
    "dynamical_ig_total_current",
    "bare_free_beta_norm",
}

EXPECTED_CLAIM_KEYS = {
    "VZ",
    "EXACT_GR",
    "THETA_XI",
    "Y14_K3_INDEX",
    "SM_FINITE_CONTROL",
    "OBSERVER_CHSH",
}

REQUIRED_INTERFACE_SLOTS = {
    "fields",
    "variations",
    "gauge_group",
    "operator_D_GU",
    "action_S_GU",
    "section_map",
    "source_law",
    "boundary_conditions",
    "reduction_functor",
}

REQUIRED_CERTIFICATE_FIELDS = {
    "claim",
    "proof_grade",
    "dependencies",
    "forbidden_inputs",
    "rollback_condition",
    "citation_language",
}

FORBIDDEN_SENTINELS = {
    "VZ": "Phi_F",
    "EXACT_GR": "weak_field",
    "THETA_XI": "xi",
    "Y14_K3_INDEX": "three_generations",
    "SM_FINITE_CONTROL": "A_F",
    "OBSERVER_CHSH": "Bell",
}


def load_contract(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    match = re.search(
        r"## Machine-Readable Contract\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing Machine-Readable Contract JSON block")
    return json.loads(match.group(1))


def audit_contract(contract: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    interface = contract.get("interface", {})
    slots = set(interface.get("required_slots", []))
    missing_slots = REQUIRED_INTERFACE_SLOTS - slots
    if missing_slots:
        errors.append(f"missing interface slots: {sorted(missing_slots)}")

    fields = set(interface.get("required_fields", []))
    for field in ["theta", "epsilon", "beta", "II_s_H", "Phi_2"]:
        if field not in fields:
            errors.append(f"required field missing: {field}")

    status_enum = set(contract.get("status_enum", []))
    for status in ["typed", "conditional", "branch-local", "blocked", "invalid", "underdefined"]:
        if status not in status_enum:
            errors.append(f"status enum missing: {status}")

    branch_keys = set(contract.get("branch_keys", []))
    if branch_keys != EXPECTED_BRANCH_KEYS:
        errors.append(f"branch keys mismatch: {sorted(branch_keys)}")

    claim_keys = set(contract.get("claim_keys", []))
    if claim_keys != EXPECTED_CLAIM_KEYS:
        errors.append(f"claim keys mismatch: {sorted(claim_keys)}")

    branches = {branch.get("key"): branch for branch in contract.get("branches", [])}
    if set(branches) != EXPECTED_BRANCH_KEYS:
        errors.append(f"branch objects mismatch: {sorted(branches)}")

    for key, branch in branches.items():
        for required in ["variation_rule", "source_law", "current_status", "owns"]:
            if required not in branch:
                errors.append(f"{key}: missing {required}")
        if not isinstance(branch.get("owns"), list) or not branch.get("owns"):
            errors.append(f"{key}: owns must be a nonempty list")

    bare = branches.get("bare_free_beta_norm", {})
    if "theta_zero_no_nonzero_source" not in bare.get("owns", []):
        errors.append("bare_free_beta_norm must own the theta=0 negative result")
    if bare.get("source_law") != "D_A_star_F_A_equals_zero":
        errors.append("bare_free_beta_norm source law must collapse to zero")

    compatibility = contract.get("compatibility", {})
    if set(compatibility) != EXPECTED_BRANCH_KEYS:
        errors.append("compatibility branches do not match branch keys")
    for branch_key in EXPECTED_BRANCH_KEYS:
        row = compatibility.get(branch_key, {})
        if set(row) != EXPECTED_CLAIM_KEYS:
            errors.append(f"{branch_key}: compatibility claims mismatch: {sorted(row)}")
            continue
        for claim, status in row.items():
            if status not in status_enum:
                errors.append(f"{branch_key}/{claim}: invalid status {status!r}")

    if compatibility.get("operator_spine", {}).get("VZ") != "typed":
        errors.append("operator_spine must type the VZ claim")
    if compatibility.get("bare_free_beta_norm", {}).get("THETA_XI") != "invalid":
        errors.append("bare_free_beta_norm must invalidate THETA_XI")
    if compatibility.get("bare_free_beta_norm", {}).get("EXACT_GR") != "invalid":
        errors.append("bare_free_beta_norm must invalidate exact GR")

    certificates = contract.get("certificates", [])
    cert_by_claim = {certificate.get("claim"): certificate for certificate in certificates}
    if set(cert_by_claim) != EXPECTED_CLAIM_KEYS:
        errors.append(f"certificate claims mismatch: {sorted(cert_by_claim)}")

    for claim in EXPECTED_CLAIM_KEYS:
        certificate = cert_by_claim.get(claim, {})
        missing = REQUIRED_CERTIFICATE_FIELDS - set(certificate)
        if missing:
            errors.append(f"{claim}: missing certificate fields {sorted(missing)}")
            continue

        for list_field in ["dependencies", "forbidden_inputs"]:
            values = certificate.get(list_field)
            if not isinstance(values, list) or not values:
                errors.append(f"{claim}: {list_field} must be a nonempty list")

        for text_field in ["proof_grade", "rollback_condition", "citation_language"]:
            value = certificate.get(text_field)
            if not isinstance(value, str) or len(value.strip()) < 12:
                errors.append(f"{claim}: {text_field} is too short")

        sentinel = FORBIDDEN_SENTINELS[claim]
        forbidden_blob = " ".join(certificate.get("forbidden_inputs", []))
        if sentinel not in forbidden_blob:
            errors.append(f"{claim}: forbidden inputs missing sentinel {sentinel!r}")

    return errors


def main(argv: list[str]) -> int:
    path = Path(argv[1]) if len(argv) > 1 else CONTRACT
    contract = load_contract(path)
    errors = audit_contract(contract)

    if errors:
        print("primary GU interface contract audit: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "primary GU interface contract audit: PASS "
        f"({len(contract['branch_keys'])} branches, "
        f"{len(contract['claim_keys'])} claims, "
        f"{len(contract['certificates'])} certificates)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
