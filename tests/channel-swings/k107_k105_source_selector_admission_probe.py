#!/usr/bin/env python3
"""Exact checked-corpus admission audit for the K105 selector gate."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k107-k105-source-selector-admission-wave.json"
SOURCE_REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
K103 = ROOT / "lab/process/k103-absorbed-source-action-custody-qualification-wave.json"
K104 = ROOT / "lab/process/selected-k104-rsap-source-boundary-variational-owner-census.json"
SHIAB_RECEIPT = ROOT / "lab/sources/gu-action-polarization-domain-source-reinspection-2026-08-05.md"


FIELDS = (
    "source_authenticated_identity",
    "same_K105_Cl77_distortion_448_carrier",
    "coefficient_complete_action_owner",
    "full_distortion_or_boundary_operator",
    "K_self_adjointness",
    "nonzero_O256_blind_symmetry_defect",
    "simple_isolated_K_positive_spectral_line",
    "common_closed_domain_and_Green_compatibility",
)


def failures(data: dict) -> list[str]:
    out: list[str] = []
    rows = data.get("candidate_rows", [])
    if data.get("denominator") != list(FIELDS):
        out.append("denominator")
    if len(rows) != 6 or data.get("result", {}).get("candidate_count") != 6:
        out.append("row_count")
    if any(set(FIELDS) - set(row) for row in rows):
        out.append("row_shape")
    qualified = [row for row in rows if all(row.get(field) is True for field in FIELDS)]
    if qualified or data.get("result", {}).get("qualified_candidate_count") != 0:
        out.append("qualified")
    if data.get("union_rule", {}).get("cross_row_union_allowed") is not False:
        out.append("union")
    result = data.get("result", {})
    if result.get("checked_corpus_admitted_to_K105_selector_gate") is not False:
        out.append("admission")
    if result.get("GU_or_unreleased_source_selector_impossible") is not False:
        out.append("universalization")
    if result.get("physical_state_or_Born_credit") is not False or result.get("canon_verdict_change") != "none":
        out.append("promotion")
    ceiling = data.get("claim_ceiling", "")
    if "six frozen" not in ceiling or "not a theorem" not in ceiling:
        out.append("ceiling")
    return out


def evidence_checks() -> list[tuple[str, bool]]:
    source = SOURCE_REGISTER.read_text()
    k103 = json.loads(K103.read_text())
    k104 = json.loads(K104.read_text())
    shiab = SHIAB_RECEIPT.read_text()
    return [
        ("the source register contains SC-ACT-01", "- id: SC-ACT-01" in source),
        ("the source register contains SC-ACT-04", "- id: SC-ACT-04" in source),
        ("the source register contains SC-ACT-05", "- id: SC-ACT-05" in source),
        ("the source register contains SC-META-52", "- id: SC-META-52" in source),
        ("SC-META-52 records author uncertainty", "does not know how to deal with ultrahyperbolic equations" in source),
        ("K103 custody qualifies no coefficient-complete action", k103["result"]["qualified"] is False),
        ("K104 source census displays no boundary law", k104["source_census"]["balanced_boundary_density_or_domain_law"] == "NOT_DISPLAYED"),
        ("K104 source census displays no zero-flux selection", k104["source_census"]["zero_h_flux_selection"] == "NOT_DISPLAYED"),
        ("the historical Shiab selector is recorded missing", "preferred historical operator was selected" in shiab and "sheet cannot be located" in shiab),
        ("the global physical domain remains source-silent", "SOURCE-SILENT" in shiab and "physical boundary selector" in shiab),
    ]


def selftest(data: dict) -> int:
    if failures(data) or not all(ok for _, ok in evidence_checks()):
        print("BASELINE RED: hostile selftest refused")
        return 1
    updates = (
        ("drop_row", lambda d: d["candidate_rows"].pop()),
        ("drop_field", lambda d: d["candidate_rows"][0].pop(FIELDS[-1])),
        ("qualify_row", lambda d: d["candidate_rows"][0].update({field: True for field in FIELDS})),
        ("invent_qualified_count", lambda d: d["result"].__setitem__("qualified_candidate_count", 1)),
        ("allow_union", lambda d: d["union_rule"].__setitem__("cross_row_union_allowed", True)),
        ("invent_admission", lambda d: d["result"].__setitem__("checked_corpus_admitted_to_K105_selector_gate", True)),
        ("universalize", lambda d: d["result"].__setitem__("GU_or_unreleased_source_selector_impossible", True)),
        ("invent_physics", lambda d: d["result"].__setitem__("physical_state_or_Born_credit", True)),
        ("promote_canon", lambda d: d["result"].__setitem__("canon_verdict_change", "changed")),
        ("erase_scope", lambda d: d.__setitem__("claim_ceiling", "No GU selector exists.")),
    )
    caught = []
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught.append((name, bool(failures(mutant))))
    for name, ok in caught:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(ok for _, ok in caught)}/{len(caught)} caught")
    return 0 if all(ok for _, ok in caught) else 1


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    if "--selftest" in sys.argv:
        return selftest(data)
    checks = evidence_checks()
    checks.extend([
        ("all six candidate rows have the complete eight-field shape", not any(set(FIELDS) - set(row) for row in data["candidate_rows"])),
        ("no frozen candidate supplies all eight selector fields", not any(all(row[field] for field in FIELDS) for row in data["candidate_rows"])),
        ("the manifest forbids cross-row union and universalization", not failures(data)),
    ])
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"K107 K105 SOURCE SELECTOR ADMISSION: {sum(ok for _, ok in checks)}/{len(checks)} pass")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
