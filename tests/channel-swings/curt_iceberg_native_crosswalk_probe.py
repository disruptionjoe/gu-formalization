#!/usr/bin/env python3
"""Source/status controls for the Curt iceberg native crosswalk.

This probe checks coverage, provenance separation, and anti-overclaim gates.
It does not prove any Geometric Unity field, equation, spectrum, or physical
recovery.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CROSSWALK = ROOT / "lab/process/curt-iceberg-native-crosswalk.json"
ATLAS = ROOT / "lab/process/eric-native-physics-equation-replacement-atlas.json"
CLOSURE = ROOT / "lab/process/eric-source-directed-native-closure-certificate.json"

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


def main() -> None:
    data = json.loads(CROSSWALK.read_text())
    atlas = json.loads(ATLAS.read_text())
    closure = json.loads(CLOSURE.read_text())
    steps = data["recap_steps"]
    rows = {row["id"]: row for row in data["cross_cutting_recovery_claims"]}
    forks = {row["id"]: row for row in data["load_bearing_forks"]}
    atlas_ids = {row["id"] for row in atlas["components"]}
    claim_ids = {row["id"] for row in steps} | set(rows)

    exact("source video and transcript are pinned", data["source"]["official_video"].endswith("AThFAxF7Mgw") and "podscripts.co" in data["source"]["transcript_mirror"])
    exact("source is graded as secondary exposition", "secondary" in data["source"]["grade"])
    exact("three layers plus recovery gate remain distinct", set(data["three_layer_rule"]) == {"curt_layer", "eric_layer", "repo_layer", "recovery_gate"})
    exact("atlas points to this exact source registry", atlas["curt_iceberg_reconciliation"]["registry"] == "lab/process/curt-iceberg-native-crosswalk.json")
    exact("every atlas overlay claim resolves", all(set(ids) <= claim_ids for ids in atlas["curt_iceberg_overlay"].values()))

    exact("all thirty recap steps are present once and ordered", [row["step"] for row in steps] == list(range(1, 31)))
    exact("all thirty step ids are unique", len({row["id"] for row in steps}) == 30)
    exact("every recap step has a timestamp", all(row["timestamp"].strip() for row in steps))
    exact("every recap step separates Eric support repo status and emergence", all({"eric_support", "repo_status", "emergence_status"} <= set(row) for row in steps))
    exact("every recap step routes to the live atlas", all(row["atlas_targets"] and set(row["atlas_targets"]) <= atlas_ids for row in steps))

    exact("all four load-bearing forks are explicit", set(forks) == {"FORK-SIGNATURE", "FORK-STRUCTURE-GROUP", "FORK-GAUGE-SELECTION", "FORK-GENERATIONS"})
    exact("signature fork preserves both surfaces", all(token in forks["FORK-SIGNATURE"]["curt_surface"] + forks["FORK-SIGNATURE"]["active_repo_surface"] for token in ("(7,7)", "(9,5)", "(4,6)", "(6,4)")))
    exact("real-form fork preserves U and right-H groups", "U(64,64)" in forks["FORK-STRUCTURE-GROUP"]["curt_surface"] and "Sp(32,32;H)" in forks["FORK-STRUCTURE-GROUP"]["active_repo_surface"])
    exact("gauge containment is not dynamic selection", forks["FORK-GAUGE-SELECTION"]["status"] == "CONTAINMENT_BUILT__DYNAMICAL_SELECTION_OPEN")
    exact("generation pieces are not a count", forks["FORK-GENERATIONS"]["status"] == "THREE_PIECES_BUILT__THREE_PHYSICAL_GENERATIONS_NOT_DERIVED" and "no decomposition" in forks["FORK-GENERATIONS"]["rule"])

    exact("fourteen cross-cutting claims are present", set(rows) == {f"CI-X{i:02d}" for i in range(1, 15)})
    exact("every cross-cutting claim becomes a construction directive", all(row["directive"].strip() for row in rows.values()))
    exact("physical pullback keeps Euler and domain gates open", "EULER_PULLBACK_DOMAIN_AND_INTERTWINING_OPEN" in rows["CI-X01"]["repo_grade"])
    exact("one-family 16 is not family multiplicity", "ONE_GENERATION_16" in rows["CI-X02"]["repo_grade"] and "never as evidence of three" in rows["CI-X02"]["directive"])
    exact("SU32 path retains finite reduction and selector burden", "VACUUM_SELECTION_OPEN" in rows["CI-X03"]["repo_grade"] and "hypercharge" in rows["CI-X03"]["directive"])
    exact("proton decay remains an untested calculation", rows["CI-X04"]["repo_grade"] == "UNTESTED_PHENOMENOLOGY" and "decay-amplitude" in rows["CI-X04"]["directive"])
    exact("three-generation strong claim fails Layer 0", "LAYER0_FAIL_AS_COUNT" in rows["CI-X05"]["repo_grade"])
    exact("Yukawa incidence is separated from coefficient freedom", "COEFFICIENT_FREE_CLAIM_NOT_SUPPORTED" in rows["CI-X06"]["source_grade"] and "Yukawa constant" in rows["CI-X06"]["directive"])
    exact("CKM and PMNS require two mass operators", "two action-selected noncommuting mass operators" in rows["CI-X07"]["directive"])
    exact("Dirac remains a conditional physical readout", "PHYSICAL_DOMAIN_AND_4D_SYMBOL_OPEN" in rows["CI-X08"]["repo_grade"])
    exact("Dirac domain follows the C0-selected reality structure", all(token in rows["CI-X08"]["directive"] for token in ("C0-selected", "right-H only if", "kill")))
    exact("Klein-Gordon is explicitly Curt reconstruction", "NO_SPECIFIC_SOURCE_NOTES" in rows["CI-X09"]["source_grade"] and rows["CI-X09"]["repo_grade"] == "NO_Y14_KLEIN_GORDON_RECOVERY")
    exact("Einstein and Yang-Mills retain physical recovery gates", "PHYSICAL_SPIN2_RECOVERY_OPEN" in rows["CI-X10"]["repo_grade"] and "ORDINARY_F2_YM_RECOVERY_OPEN" in rows["CI-X11"]["repo_grade"])
    exact("cosmological constant retains state amplitude and PP3 gates", all(token in rows["CI-X12"]["directive"] for token in ("state", "amplitude", "PP3", "DESI")))
    exact("dark sector is not off-observation complement", "off-observation complement" in rows["CI-X13"]["directive"])
    exact("inevitability rhetoric is charged to surplus ledger", rows["CI-X14"]["repo_grade"] == "CONDITIONAL_ARCHITECTURE_ONLY" and "constraint-surplus" in rows["CI-X14"]["directive"])

    exact("recap step 18 retains open physical recovery", steps[17]["id"] == "CI-18" and steps[17]["emergence_status"].startswith("OPEN_"))
    exact("source and active Clifford dimensions remain separately typed", all(token in steps[10]["curt_claim"] for token in ("Spin(7,7)", "128", "64")) and "FORKED" in steps[10]["repo_status"])
    exact("recap step 20 does not overstate the complex", steps[19]["repo_status"] == "PARTIAL_ORDINARY_GAUGE_BV__KINEMATIC_GAMMA_MAPS_ONLY" and steps[19]["emergence_status"].startswith("OPEN_"))
    exact("recap step 21 does not overstate seesaw masses", steps[20]["repo_status"] == "KINEMATIC_SEESAW_FIXTURES_ONLY")
    exact("recap step 23 rejects block-to-generation inference", steps[22]["repo_status"] == "DECOMPOSITION_BUILT__COUNT_INFERENCE_REFUTED")
    exact("recap step 24 does not rename any scalar Higgs", "DOUBLET" in steps[23]["emergence_status"] and "PHOTON_KERNEL" in steps[23]["emergence_status"])
    exact("recap step 25 keeps two scalar identifications testable", "PARTICLE_IDENTIFICATIONS_OPEN" in steps[24]["repo_status"])
    exact("recap step 27 retains physical bilinear and flavour gates", all(token in steps[26]["emergence_status"] for token in ("KREIN_BILINEAR", "CHIRAL_REPRESENTATIONS", "FLAVOUR_COEFFICIENTS")))
    exact("recap step 30 is not a cosmological prediction", steps[29]["repo_status"] == "DISTORTION_COSMO_CARRIER_ONLY" and "PP3" in steps[29]["emergence_status"])

    exact("new C0 bridge precedes carrier census port and C1", data["atlas_integration"]["reordered_next_swing"].startswith("C0:") and all(token in data["atlas_integration"]["reordered_next_swing"] for token in ("census", "port", "C1")))
    exact("C0 includes the tautological musical map", any("musical map" in item and "pi*TX" in item for item in data["atlas_integration"]["new_prerequisites"]))
    exact("closure certificate still claims no generation count", closure["generation_count_claimed"] is False)
    exact("closure certificate still reports open Y14 readouts", all(row["y14_emergence_status"] == "OPEN" for row in closure["readouts"]))
    exact("nonclaims cover group generation flavour equations and cosmology", len(data["nonclaims"]) == 5 and all(data["nonclaims"]))

    planted("Curt exposition is a primary Weinstein theorem", data["source"]["grade"] == "primary Weinstein theorem")
    planted("7,7 and 9,5 are silently interchangeable", forks["FORK-SIGNATURE"]["status"] == "RESOLVED_IDENTICAL")
    planted("U6464 equals Sp3232H without a bridge", forks["FORK-STRUCTURE-GROUP"]["status"] == "RESOLVED_IDENTICAL")
    planted("maximal compact containment selects the physical gauge group", "selection built" in forks["FORK-GAUGE-SELECTION"]["status"].lower())
    planted("three carrier pieces are three observed generations", "THREE_PHYSICAL_GENERATIONS_DERIVED" in forks["FORK-GENERATIONS"]["status"])
    planted("one 16-dimensional packet is three families", "three families derived" in rows["CI-X02"]["repo_grade"].lower())
    planted("minimal coupling fixes all Yukawa coefficients", "COEFFICIENT_FREE_CLAIM_SUPPORTED" in rows["CI-X06"]["source_grade"])
    planted("residual gauge freedom already predicts CKM and PMNS", rows["CI-X07"]["repo_grade"].startswith("BUILT"))
    planted("Curt located Eric's Klein-Gordon formula", "PRIMARY_FORMULA" in rows["CI-X09"]["source_grade"])
    planted("G2 parent is already Einstein gravity", rows["CI-X10"]["repo_grade"] == "PHYSICAL_EINSTEIN_RECOVERED")
    planted("G2 parent is already ordinary Yang-Mills", rows["CI-X11"]["repo_grade"] == "PHYSICAL_YANG_MILLS_RECOVERED")
    planted("constant connection component fixes observed Lambda", rows["CI-X12"]["repo_grade"] == "COSMOLOGICAL_CONSTANT_DERIVED")
    planted("proton stability follows from SU32 containment", rows["CI-X04"]["repo_grade"] == "PROTON_DECAY_AVOIDED")
    planted("dark matter is the off-observation kernel", "identify dark matter with off-observation" in rows["CI-X13"]["directive"].lower())
    planted("the finite U2 fixture is Y14 emergence", closure["planted_standard_model_fixture_is_emergence_evidence"] is True)
    planted("the iceberg changes the next swing to conventional equations", "independent standard equations" in data["atlas_integration"]["reordered_next_swing"].lower())

    print(
        "CURT-ICEBERG-NATIVE-CROSSWALK: "
        f"{exact_checks} exact checks + {planted_checks} planted failures = "
        f"{exact_checks + planted_checks} PASS"
    )
    print("RESULT: all 30 recap steps and 14 cross-cutting claims are source-graded")
    print("RESULT: four load-bearing forks remain explicit and non-transferable")
    print("RESULT: C0 precedes carrier-specific census/port and then C1/G4")
    print("BOUNDARY: no SM selection, generation count, PDE recovery, flavour matrix, or cosmology is claimed")


if __name__ == "__main__":
    main()
