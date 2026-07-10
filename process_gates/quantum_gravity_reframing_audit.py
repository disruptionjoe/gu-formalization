#!/usr/bin/env python3
"""Audit the quantum-gravity reframing no-go map.

This is a governance/status audit, not a proof of the physics. It checks that
the Markdown artifact carries the required status categories, no-go decisions,
claim certificates, and forbidden-rhetoric replacements.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MAP_PATH = ROOT / "explorations" / "firewall-and-two-geometries" / "quantum-gravity-reframing-no-go-map-2026-06-24.md"

EXPECTED_DECISIONS = {
    "WITTEN": "BYPASSED",
    "DISTLER_GARIBALDI": "BYPASSED",
    "VZ": "RELOCATED",
    "ANOMALY": "RELOCATED",
    "EXACT_GR": "STILL_OWED",
    "MEASUREMENT": "RELOCATED",
    "QUANTUM_RECOVERY": "STILL_OWED",
}

EXPECTED_CERTIFICATES = {
    "NOT-QG-FRAMING",
    "SOURCE-GEOMETRY",
    "QFT-RECOVERY",
    "GR-RECOVERY",
}

REQUIRED_CERTIFICATE_FIELDS = {
    "claim",
    "status",
    "proof_grade",
    "dependencies",
    "forbidden_inputs",
    "rollback_condition",
    "citation_language",
}

REQUIRED_FORBIDDEN_IDS = {
    "not_quantizing_gr_solves_qft",
    "gu_solves_qg_by_reframing",
    "source_geometry_solves_quantum",
    "weak_field_equals_exact_gr",
    "observer_finality_solves_measurement",
    "vz_verified",
    "k3_three_generations",
}

SUPPORTING_SCHEMA_SENTINELS = {
    "explorations/firewall-and-two-geometries/source-geometry-not-quantized-gravity-contract-2026-06-24.md",
    "explorations/cycle-gates-and-audits/qft-shadow-extraction-certificate-2026-06-24.md",
    "explorations/geometry-curvature-emergence/gr-shadow-recovery-certificate-2026-06-24.md",
}


def load_contract(path: Path) -> tuple[str, dict[str, Any]]:
    text = path.read_text(encoding="utf-8")
    match = re.search(
        r"## Machine-Readable Reframing Contract\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing Machine-Readable Reframing Contract JSON block")
    return text, json.loads(match.group(1))


def require_nonempty_string(value: Any, label: str, errors: list[str]) -> None:
    if not isinstance(value, str) or len(value.strip()) < 8:
        errors.append(f"{label} must be a substantive string")


def audit_contract(text: str, contract: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    decision_enum = set(contract.get("decision_enum", []))
    if decision_enum != {"BYPASSED", "RELOCATED", "STILL_OWED"}:
        errors.append(f"decision_enum mismatch: {sorted(decision_enum)}")

    status_enum = set(contract.get("claim_status_enum", []))
    for status in [
        "BYPASSED_AS_PRIMARY_FRAMING",
        "REPLACEMENT_OBJECTIVE_SPECIFIED_OPEN",
        "STILL_OWED",
        "SPECIFICATION_OPEN",
    ]:
        if status not in status_enum:
            errors.append(f"claim_status_enum missing {status}")

    rows = contract.get("no_go_rows", [])
    row_by_id = {row.get("id"): row for row in rows}
    if set(row_by_id) != set(EXPECTED_DECISIONS):
        errors.append(f"no_go_rows ids mismatch: {sorted(row_by_id)}")
    else:
        for row_id, expected_decision in EXPECTED_DECISIONS.items():
            row = row_by_id[row_id]
            if row.get("decision") != expected_decision:
                errors.append(
                    f"{row_id}: expected {expected_decision}, got {row.get('decision')!r}"
                )
            for field in [
                "conventional_objective",
                "gu_replacement",
                "remaining_proof_obligation",
                "forbidden_shortcut",
            ]:
                require_nonempty_string(row.get(field), f"{row_id}.{field}", errors)

    certificates = contract.get("certificates", [])
    cert_by_claim = {cert.get("claim"): cert for cert in certificates}
    if set(cert_by_claim) != EXPECTED_CERTIFICATES:
        errors.append(f"certificate claims mismatch: {sorted(cert_by_claim)}")
    else:
        for claim, cert in cert_by_claim.items():
            missing = REQUIRED_CERTIFICATE_FIELDS - set(cert)
            if missing:
                errors.append(f"{claim}: missing certificate fields {sorted(missing)}")
                continue
            if cert.get("status") not in status_enum:
                errors.append(f"{claim}: invalid status {cert.get('status')!r}")
            for list_field in ["dependencies", "forbidden_inputs"]:
                values = cert.get(list_field)
                if not isinstance(values, list) or len(values) < 2:
                    errors.append(f"{claim}: {list_field} must contain at least two entries")
            for text_field in ["proof_grade", "rollback_condition", "citation_language"]:
                require_nonempty_string(cert.get(text_field), f"{claim}.{text_field}", errors)

    if cert_by_claim.get("QFT-RECOVERY", {}).get("status") != "STILL_OWED":
        errors.append("QFT-RECOVERY must stay STILL_OWED")
    if cert_by_claim.get("GR-RECOVERY", {}).get("status") != "STILL_OWED":
        errors.append("GR-RECOVERY must stay STILL_OWED")
    if (
        cert_by_claim.get("SOURCE-GEOMETRY", {}).get("status")
        != "REPLACEMENT_OBJECTIVE_SPECIFIED_OPEN"
    ):
        errors.append("SOURCE-GEOMETRY must be specified-open, not closed")

    forbidden = contract.get("forbidden_rhetoric", [])
    forbidden_by_id = {item.get("id"): item for item in forbidden}
    if set(forbidden_by_id) != REQUIRED_FORBIDDEN_IDS:
        errors.append(f"forbidden rhetoric ids mismatch: {sorted(forbidden_by_id)}")
    else:
        for item_id, item in forbidden_by_id.items():
            require_nonempty_string(item.get("phrase"), f"{item_id}.phrase", errors)
            require_nonempty_string(
                item.get("allowed_replacement"),
                f"{item_id}.allowed_replacement",
                errors,
            )

    for sentinel in SUPPORTING_SCHEMA_SENTINELS:
        if sentinel not in text:
            errors.append(f"supporting schema input not cited: {sentinel}")
        if sentinel not in contract.get("supporting_schema_inputs", []):
            errors.append(f"supporting schema input absent from JSON: {sentinel}")

    if contract.get("first_missing_proof_object") != "QG-SHADOW-01":
        errors.append("first_missing_proof_object must be QG-SHADOW-01")

    child_blockers = set(contract.get("first_child_blockers", []))
    for blocker in [
        "QFTStateSpaceExtractionCertificate",
        "QFTStateExtractionCertificate",
        "ObservableAdmissibilityCertificate",
        "ELProjectedGRShadowTheorem",
    ]:
        if blocker not in child_blockers:
            errors.append(f"first_child_blockers missing {blocker}")

    return errors


def main(argv: list[str]) -> int:
    path = Path(argv[1]) if len(argv) > 1 else MAP_PATH
    text, contract = load_contract(path)
    errors = audit_contract(text, contract)

    if errors:
        print("quantum gravity reframing audit: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "quantum gravity reframing audit: PASS "
        f"({len(contract['no_go_rows'])} no-go rows, "
        f"{len(contract['certificates'])} certificates, "
        f"{len(contract['forbidden_rhetoric'])} forbidden-rhetoric guards)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
