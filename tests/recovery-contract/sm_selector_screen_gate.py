#!/usr/bin/env python
"""Recovery contract Standard Model selector screen gate.

This branch-local gate asks whether the frozen W203/W229/W230/W236
record-current action fingerprint supplies a target-free selector for a
complete low-energy Standard Model sector, rather than only a host or relative
representation branch.

Result: NO_GO for complete Standard Model recovery at the current construction
grade. Current evidence positively hosts a Pati-Salam / Spin(10) branch and the
relative chiral-16 hypercharge/anomaly arithmetic survives W222, but the frozen
branch does not supply the finite algebra selector, absolute gauge quotient and
hypercharge selector, chirality-production mechanism, physical Higgs
projection, full surviving-spectrum theorem, or unwanted-mode decoupling
certificate.

This does not change any claim status, canon verdict, public posture, or the
broader recovery lane. It only closes this branch-local selector checkpoint.

Run: python tests/recovery-contract/sm_selector_screen_gate.py
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FINGERPRINT = ROOT / "lab" / "process" / "recovery-contract-action-fingerprint-2026-07-16.json"
MATRIX = ROOT / "lab" / "process" / "recovery-certification-matrix.json"
LEDGER = ROOT / "explorations" / "type-ii1-spectral" / "sm-gauge-higgs-finite-control-extraction-ledger-2026-06-24.md"
W222 = ROOT / "explorations" / "W222-falsify-sm-emergence-anomaly-hypercharge-2026-07-14.md"

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


def contains(text: str, needle: str) -> bool:
    return needle.casefold() in text.casefold()


def sm_item(matrix: dict) -> dict:
    for item in matrix["items"]:
        if item["id"] == "SM-CONSISTENT-SECTOR":
            return item
    raise AssertionError("SM-CONSISTENT-SECTOR item missing from recovery matrix")


@dataclass(frozen=True)
class SmSectorEvidence:
    carrier_branch_present: bool
    relative_hypercharge_packet: bool
    relative_chiral_anomaly_arithmetic: bool
    finite_algebra_selector: bool
    gauge_quotient_selector: bool
    absolute_hypercharge_selector: bool
    chirality_production_mechanism: bool
    physical_higgs_projection: bool
    full_surviving_spectrum_theorem: bool
    unwanted_mode_decoupling: bool


def complete_sm_recovery(evidence: SmSectorEvidence) -> bool:
    return all(
        (
            evidence.carrier_branch_present,
            evidence.relative_hypercharge_packet,
            evidence.relative_chiral_anomaly_arithmetic,
            evidence.finite_algebra_selector,
            evidence.gauge_quotient_selector,
            evidence.absolute_hypercharge_selector,
            evidence.chirality_production_mechanism,
            evidence.physical_higgs_projection,
            evidence.full_surviving_spectrum_theorem,
            evidence.unwanted_mode_decoupling,
        )
    )


def evidence_from_current_records(matrix_item: dict, ledger_text: str, w222_text: str) -> SmSectorEvidence:
    carrier_branch_present = (
        "Pati-Salam branch" in matrix_item["current_honest_ceiling"]
        and "relative Standard Model charge packet" in matrix_item["current_honest_ceiling"]
        and "One-generation SM charge packet" in ledger_text
    )
    relative_hypercharge_packet = contains(w222_text, "hypercharges MATCH the SM exactly") and contains(
        w222_text, "electric-charge multiset EXACTLY"
    )
    relative_chiral_anomaly_arithmetic = contains(w222_text, "anomaly-free by a REAL mechanism") and (
        contains(w222_text, "all four vanish")
        or contains(w222_text, "perturbative gauge-anomaly coefficients of the chiral 16 all vanish")
    )

    # The negative fields below are intentionally derived from the same records
    # that contain the positive host result. This prevents a host-only pass from
    # silently upgrading into complete sector recovery.
    finite_algebra_selector = "No current selector computes this algebra" not in ledger_text
    gauge_quotient_selector = "SM gauge quotient `SU(3) x SU(2) x U(1) / Z_6` | fail" not in ledger_text
    absolute_hypercharge_selector = "Absolute selector for the `U(1)_Y` embedding" not in ledger_text
    chirality_production_mechanism = not (
        contains(w222_text, "chirality is produced") and contains(w222_text, "only by the unbuilt")
    )
    physical_higgs_projection = "Physical Higgs scalar as a 0-form from `theta`/`II_s^H` | open" not in ledger_text
    full_surviving_spectrum_theorem = "no target-free selector" not in matrix_item["current_honest_ceiling"]
    unwanted_mode_decoupling = "extra surviving GU/Type II_1 modes" not in ledger_text

    return SmSectorEvidence(
        carrier_branch_present=carrier_branch_present,
        relative_hypercharge_packet=relative_hypercharge_packet,
        relative_chiral_anomaly_arithmetic=relative_chiral_anomaly_arithmetic,
        finite_algebra_selector=finite_algebra_selector,
        gauge_quotient_selector=gauge_quotient_selector,
        absolute_hypercharge_selector=absolute_hypercharge_selector,
        chirality_production_mechanism=chirality_production_mechanism,
        physical_higgs_projection=physical_higgs_projection,
        full_surviving_spectrum_theorem=full_surviving_spectrum_theorem,
        unwanted_mode_decoupling=unwanted_mode_decoupling,
    )


def main() -> None:
    fingerprint = load_json(FINGERPRINT)
    matrix = load_json(MATRIX)
    ledger_text = read_text(LEDGER)
    w222_text = read_text(W222)
    item = sm_item(matrix)

    log("=" * 82)
    log("PC1 -- a genuinely complete SM sector is accepted")
    log("=" * 82)
    complete_sector = SmSectorEvidence(
        carrier_branch_present=True,
        relative_hypercharge_packet=True,
        relative_chiral_anomaly_arithmetic=True,
        finite_algebra_selector=True,
        gauge_quotient_selector=True,
        absolute_hypercharge_selector=True,
        chirality_production_mechanism=True,
        physical_higgs_projection=True,
        full_surviving_spectrum_theorem=True,
        unwanted_mode_decoupling=True,
    )
    check(
        "PC1  toy complete low-energy SM sector passes the gate",
        complete_sm_recovery(complete_sector),
        "the gate accepts selector plus spectrum, Higgs, chirality, and anomaly closure",
    )

    log("")
    log("=" * 82)
    log("PC2 -- host-only and arithmetic-only evidence is rejected")
    log("=" * 82)
    host_only = SmSectorEvidence(
        carrier_branch_present=True,
        relative_hypercharge_packet=True,
        relative_chiral_anomaly_arithmetic=True,
        finite_algebra_selector=False,
        gauge_quotient_selector=False,
        absolute_hypercharge_selector=False,
        chirality_production_mechanism=False,
        physical_higgs_projection=False,
        full_surviving_spectrum_theorem=False,
        unwanted_mode_decoupling=False,
    )
    check(
        "PC2  Pati-Salam host plus chiral-16 arithmetic does not pass complete recovery",
        not complete_sm_recovery(host_only),
        "selector and physical-sector closure are load-bearing",
    )

    log("")
    log("=" * 82)
    log("C1 -- action fingerprint boundary")
    log("=" * 82)
    branch = fingerprint["branch_local_testing_object"]
    forbidden = fingerprint["quantity_ledger"]["forbidden_as_recovery_evidence"]
    imported = fingerprint["quantity_ledger"]["imported_or_comparator_only"]
    check(
        "C1a  fingerprint is branch-local, not a primary-theory freeze",
        branch["status"] == "CONDITIONAL_BRANCH_LOCAL_TEST_OBJECT" and branch["not_a_primary_theory"],
    )
    check(
        "C1b  standard SM benchmarks are comparator-only in the fingerprint",
        "standard GR/cosmology/SM sector benchmarks" in imported,
    )
    check(
        "C1c  subgroup containment alone is forbidden as recovery evidence",
        "subgroup containment alone" in forbidden,
    )
    check(
        "C1d  the fingerprint itself must not enable claim or public-posture movement",
        "claim-status movement" in branch["must_not_enable"]
        and "public-posture movement" in branch["must_not_enable"],
    )

    log("")
    log("=" * 82)
    log("C2 -- recovery matrix asks exactly this selector screen")
    log("=" * 82)
    check("C2a  SM-CONSISTENT-SECTOR is ready only after the recovery contract", item["state"] == "READY_AFTER_CONTRACT")
    check(
        "C2b  current ceiling says host evidence exists but selector closure does not",
        "carrier hosts a Pati-Salam branch" in item["current_honest_ceiling"]
        and "no target-free selector" in item["current_honest_ceiling"],
    )
    check(
        "C2c  first decisive test names quotient, hypercharge, chirality, Higgs, spectrum, and anomaly",
        "gauge quotient" in item["first_decisive_test"]
        and "hypercharge normalization" in item["first_decisive_test"]
        and "chiral 16" in item["first_decisive_test"]
        and "Higgs projection" in item["first_decisive_test"]
        and "all surviving modes" in item["first_decisive_test"]
        and "anomaly status" in item["first_decisive_test"],
    )
    check(
        "C2d  kill condition rejects host-only subgroup or representation evidence",
        "Host-only subgroup or representation evidence" in item["kill_condition"],
    )

    log("")
    log("=" * 82)
    log("C3 -- prior SM records distinguish host success from selector recovery")
    log("=" * 82)
    check(
        "C3a  ledger verdict is partial host with selector no-go",
        "PARTIAL_HOST_WITH_SELECTOR_NO_GO" in ledger_text,
    )
    check(
        "C3b  finite Connes algebra is imported, not selected",
        "Finite CC algebra `A_F = C + H + M_3(C)` | import" in ledger_text
        and "No current selector computes this algebra" in ledger_text,
    )
    check(
        "C3c  SM gauge quotient is the first target-level derivation failure",
        "SM gauge quotient `SU(3) x SU(2) x U(1) / Z_6` | fail" in ledger_text
        and "first genuine target-level failure" in ledger_text,
    )
    check(
        "C3d  physical Higgs projection and unwanted-mode shadow remain open",
        "Physical Higgs scalar as a 0-form from `theta`/`II_s^H` | open" in ledger_text
        and "extra surviving GU/Type II_1 modes" in ledger_text,
    )

    log("")
    log("=" * 82)
    log("C4 -- W222 is a real relative pass, not a selector theorem")
    log("=" * 82)
    check(
        "C4a  W222 hypercharge and anomaly arithmetic survive",
        contains(w222_text, "hypercharges MATCH the SM exactly")
        and contains(w222_text, "anomaly-free by a REAL mechanism"),
    )
    check(
        "C4b  W222 explicitly grants the chiral shadow rather than deriving it",
        contains(w222_text, "CONDITIONAL on the 4D shadow")
        and contains(w222_text, "being the CHIRAL 16")
        and contains(w222_text, "chirality is produced")
        and contains(w222_text, "only by the unbuilt"),
    )
    check(
        "C4c  W222 locates the residual risk in chirality production",
        contains(w222_text, "onto chirality") and contains(w222_text, "production"),
    )

    log("")
    log("=" * 82)
    log("C5 -- current branch evidence fails complete SM recovery")
    log("=" * 82)
    current = evidence_from_current_records(item, ledger_text, w222_text)
    check("C5a  current evidence has a carrier branch", current.carrier_branch_present)
    check("C5b  current evidence has relative hypercharge and anomaly arithmetic", current.relative_hypercharge_packet and current.relative_chiral_anomaly_arithmetic)
    check("C5c  current evidence lacks a finite algebra selector", not current.finite_algebra_selector)
    check("C5d  current evidence lacks an absolute gauge quotient and hypercharge selector", not current.gauge_quotient_selector and not current.absolute_hypercharge_selector)
    check("C5e  current evidence lacks chirality production and physical Higgs projection", not current.chirality_production_mechanism and not current.physical_higgs_projection)
    check("C5f  current evidence lacks full surviving-spectrum and decoupling closure", not current.full_surviving_spectrum_theorem and not current.unwanted_mode_decoupling)
    check("C5g  current fingerprint does not close complete SM recovery", not complete_sm_recovery(current))

    operational_result = "NO_GO" if not complete_sm_recovery(current) else "CONDITIONAL"
    check(
        "C5h  branch-local complete-SM recovery is NO_GO at this grade",
        operational_result == "NO_GO",
        "relative host/anomaly success remains below target-free selector recovery",
    )
    check(
        "C5i  fingerprint statuses remain non-status-changing",
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
        log("Operational result: NO_GO for complete Standard Model recovery at this checkpoint.")
        log("The current branch hosts a Pati-Salam / Spin(10) SM-shaped packet and W222's")
        log("hypercharge/anomaly arithmetic survives, but no target-free selector or complete")
        log("physical low-energy sector is derived. Claim status, canon verdict, public posture,")
        log("and portfolio state are unchanged.")

    if FAIL:
        log(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            log("  FAIL: " + name)
        raise SystemExit(1)
    log("\nRESULT: ALL PASS")


if __name__ == "__main__":
    main()
