#!/usr/bin/env python
"""Gate for the QM physical-sector conditional sufficiency certificate.

This gate checks that the post-Swing-1 conditional unitarity interleave reached
a status-neutral endpoint. It does not move claim status, canon verdict, public
posture, or portfolio state.

Run: python tests/recovery-contract/qm_physical_sector_conditional_gate.py
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "lab" / "process" / "recovery-no-go-defense-register.json"
NOTE = ROOT / "explorations" / "recovery-qm-physical-sector-conditional-sufficiency-2026-07-16.md"
QFT_SOURCE = ROOT / "explorations" / "cycle-gates-and-audits" / "qft-shadow-extraction-certificate-2026-06-24.md"
BRST_SOURCE = ROOT / "explorations" / "hourly-cycles" / "hourly-cycle2-rs-physical-quotient-brst-complex-gate-2026-06-24.md"
W169_SOURCE = ROOT / "explorations" / "W169-c-operator-perturbative-construction-2026-07-14.md"
W173_SOURCE = ROOT / "explorations" / "W173-brst-cohomology-mirror-sector-2026-07-14.md"

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL") + " :: " + name + (("  --  " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def stage_statuses(conditional: dict) -> dict[str, str]:
    return {stage["stage"]: stage["status"] for stage in conditional["stage_results"]}


def main() -> None:
    register = load_json(REGISTER)
    conditional = register["conditional_unitarity"]
    stages = stage_statuses(conditional)
    note = read_text(NOTE)
    qft_source = read_text(QFT_SOURCE)
    brst_source = read_text(BRST_SOURCE)
    w169 = read_text(W169_SOURCE)
    w173 = read_text(W173_SOURCE)

    print("=" * 82)
    print("C1 -- register endpoint")
    print("=" * 82)
    check("C1a  conditional unitary item is QM-PHYSICAL-SECTOR", conditional["id"] == "QM-PHYSICAL-SECTOR")
    check("C1b  interleave reached conditional-fail endpoint", conditional["state"] == "COMPLETE_CONDITIONAL_FAIL")
    check("C1c  operational result is CONDITIONAL_FAIL", conditional["result"] == "CONDITIONAL_FAIL")
    check("C1d  evidence path points to note", conditional["evidence"] == NOTE.relative_to(ROOT).as_posix())
    check("C1e  test path points to this gate", conditional["test"] == Path(__file__).relative_to(ROOT).as_posix())
    check("C1f  required outcome vocabulary is preserved", set(conditional["required_outcomes"]) == {"CONDITIONAL_COMPLETE", "CONDITIONAL_FAIL", "UNDERDEFINED"})

    print("")
    print("=" * 82)
    print("C2 -- adapter assumption is typed but assumption-capped")
    print("=" * 82)
    adapter = conditional["adapter_interface"]
    check("C2a  adapter interface is explicitly typed", adapter["status"] == "TYPED_AS_EXPLICIT_ASSUMPTION")
    check("C2b  adapter axiom is named", "BoundaryAdapterAxiom" in adapter["axiom"])
    check("C2c  adapter does not supply state space", "QFT state space" in adapter["does_not_supply"])
    check("C2d  adapter does not supply observables", "GU-admissible observables" in adapter["does_not_supply"])
    check("C2e  note says adapter is not constructed", "It does not construct the adapter" in note)

    print("")
    print("=" * 82)
    print("C3 -- stage statuses stop before quantum recovery")
    print("=" * 82)
    expected = {
        "AdapterInterface": "ASSUMED_TYPED",
        "SourceGeometryCertificate": "PARTIAL",
        "PhysicalFieldComplexCertificate": "MISSING_SOURCE_DEFINED_QUOTIENT",
        "QFTStateSpaceExtractionCertificate": "MISSING",
        "QFTStateExtractionCertificate": "MISSING",
        "ObservableAdmissibilityCertificate": "MISSING",
        "BornProbabilityCertificate": "MISSING",
        "LocalityCausalityCertificate": "CONDITIONAL_ONLY",
        "UnitarityCertificate": "MISSING_QFT_LEVEL",
        "SpinStatisticsCertificate": "MISSING",
        "AnomalyShadowCertificate": "OPEN_RELATIVE_ONLY",
    }
    check("C3a  every required stage is present with expected status", stages == expected)
    missing = set(conditional["first_missing_objects"])
    check("C3b  first missing objects include source-defined BRST differential", "source-defined gauge/BRST differential d_RS,-1" in missing)
    check("C3c  first missing objects include QFT state space", "QFTStateSpaceExtractionCertificate" in missing)
    check("C3d  first missing objects include observable certificate", "ObservableAdmissibilityCertificate" in missing)
    check("C3e  first missing objects include unitarity certificate", "UnitarityCertificate" in missing)

    print("")
    print("=" * 82)
    print("C4 -- source evidence supports the endpoint")
    print("=" * 82)
    check("C4a  QFT source blocks before state extraction", "CURRENT_REPO_BLOCKED_BEFORE_STATE_SPACE_AND_STATE_EXTRACTION" in qft_source)
    check("C4b  BRST source names the missing quotient differential", "MISSING_SOURCE_DEFINED_GAUGE_BRST_DIFFERENTIAL" in brst_source and "d_RS,-1" in brst_source)
    check("C4c  W169 is not all-orders QFT unitarity", "No all-orders proof" in w169 and "No QFT amplitude" in w169)
    check("C4d  W173 remains quantization-dependent", "QUANTIZATION-DEPENDENT" in w173 and "Y14 curvature" in w173)

    print("")
    print("=" * 82)
    print("C5 -- note preserves status boundaries and next-work handoff")
    print("=" * 82)
    check("C5a  note records conditional fail", "Operational result: `CONDITIONAL_FAIL`." in note)
    check("C5b  note names first missing objects", "## 5. First Missing Objects" in note and "d_RS,-1" in note)
    check("C5c  note preserves no status movement", "No claim status, canon verdict, public posture" in note)
    check("C5d  note says paper seed is absent", "Paper seed proposal: none." in note)
    check("C5e  next work resumes Swing 2 defense", "resume Lane 1 no-go defense with GR Swing 2" in note)

    if FAIL:
        print(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            print("  FAIL: " + name)
        raise SystemExit(1)
    print("\nRESULT: ALL PASS")


if __name__ == "__main__":
    main()
