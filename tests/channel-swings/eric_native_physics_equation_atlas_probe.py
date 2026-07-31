#!/usr/bin/env python3
"""Contract checks for the Eric-native physics equation replacement atlas.

This is a type/status/dependency certificate. It does not compute the future
stationary background, observation domain, Hessian spectrum, odd Euler
operator, anomaly, generation index, or cosmological prediction.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ATLAS = ROOT / "lab/process/eric-native-physics-equation-replacement-atlas.json"

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
    data = json.loads(ATLAS.read_text())
    rows = {row["id"]: row for row in data["components"]}

    expected = {
        "EM_MAXWELL",
        "GAUGE_YANG_MILLS",
        "FORCE_DECOMPOSITION",
        "DIRAC_MATTER",
        "RS_CHIMERIC",
        "HIGGS_EWSB",
        "YUKAWA_MASS",
        "EINSTEIN_GRAVITY",
        "STRESS_CONSERVATION",
        "COSMO_DISTORTION",
        "FLRW_PP3",
        "QUANTUM_BV",
        "ANOMALY_CONSISTENCY",
        "GENERATION_INDEX",
        "EXTERNAL_DATUM_OBSERVATION",
    }
    required = {
        "standard_job",
        "standard_equation",
        "native_carrier",
        "native_equation",
        "observation_map",
        "status",
        "source_anchors",
        "next_build",
        "kill",
        "datum_use",
    }
    allowed_statuses = {
        "BUILT_NATIVE_PARENT",
        "BUILT_IDENTITY_ONLY",
        "CANDIDATE_SHADOW",
        "CANDIDATE_PARENT",
        "NATIVE_CARRIER_ONLY",
        "PARTIAL_BV",
        "DOWNSTREAM_TEST",
    }

    exact("all fifteen component rows are present once", set(rows) == expected and len(data["components"]) == len(rows))
    exact("every row has the complete replacement contract", all(required <= set(row) for row in rows.values()))
    exact("every construction and kill is nonempty", all(row["next_build"].strip() and row["kill"].strip() for row in rows.values()))
    exact("status vocabulary is closed", all(row["status"] in allowed_statuses for row in rows.values()))
    exact("every row has source provenance", all(row["source_anchors"] for row in rows.values()))
    exact("no row stalls at missing action or datum", all("source action or external datum missing" not in row["next_build"].lower() for row in rows.values()))

    backbone = data["native_backbone"]
    exact("G2/G3 is the declared common native backbone", "I_G2" in backbone["action"] and "E_A=E_T" in backbone["connection_euler"])
    exact("killed compressed Euler shortcut remains recorded", backbone["killed_shortcut"] == "S_epsilon(F_(B+T))+kappa_1 T")
    exact("observation gate includes retract intertwining leakage and equation dual", all(token in backbone["observation_gate"] for token in ("R_s L_s=1", "R_s D_Y L_s=D_X", "1-L_s R_s", "(D L_s)^!")))

    order = data["coherent_dependency_order"]
    exact("construction begins with naturality then observation", order[:2] == ["G3.5_TARGET_BLIND_NATURALITY_AND_ABLATION", "G4_OBSERVATION_RETRACT_DOMAIN_AND_BFV_QUOTIENT"])
    exact("one shared Hessian precedes matter currents and particle labels", order.index("ONE_REDUCED_BOSONIC_HESSIAN") < order.index("G5_MINIMAL_ODD_EXTENSION_AND_ACTION_DERIVED_CURRENTS") < order.index("LOW_ENERGY_MODE_AND_GROUP_IDENTIFICATION"))
    exact("anomaly index and cosmology remain downstream", order[-3:] == ["PHYSICAL_BV_ANOMALY_TEST", "PHYSICAL_INDEX_AND_DATUM_READOUT", "COSMOLOGICAL_STATE_AND_PP3_TEST"])

    exact("Maxwell is a candidate reduced shadow", rows["EM_MAXWELL"]["status"] == "CANDIDATE_SHADOW" and "abelian projection" in rows["EM_MAXWELL"]["native_equation"])
    exact("Yang-Mills uses exact native Euler not Bianchi as dynamics", rows["GAUGE_YANG_MILLS"]["status"] == "BUILT_NATIVE_PARENT" and "E_A=E_T" in rows["GAUGE_YANG_MILLS"]["native_equation"] and "kinematic identity" in rows["GAUGE_YANG_MILLS"]["native_equation"])
    exact("force algebra waits for a frozen quotient Hessian", rows["FORCE_DECOMPOSITION"]["status"] == "CANDIDATE_PARENT" and "Hessian" in rows["FORCE_DECOMPOSITION"]["native_equation"])
    exact("Dirac and RS remain native carriers without copied equations", rows["DIRAC_MATTER"]["status"] == rows["RS_CHIMERIC"]["status"] == "NATIVE_CARRIER_ONLY" and "Future odd Euler" in rows["DIRAC_MATTER"]["native_equation"])
    exact("Higgs is a Hessian candidate not a scalar rename", rows["HIGGS_EWSB"]["status"] == "CANDIDATE_PARENT" and "no independent Higgs potential" in rows["HIGGS_EWSB"]["native_equation"])
    exact("Yukawa keeps the Krein pairing in the physical channel", rows["YUKAWA_MASS"]["status"] == "CANDIDATE_PARENT" and "K e_vertical" in rows["YUKAWA_MASS"]["native_carrier"])
    exact("gravity has a built graph Euler parent and open shadow", rows["EINSTEIN_GRAVITY"]["status"] == "BUILT_NATIVE_PARENT" and "E_g=0" in rows["EINSTEIN_GRAVITY"]["native_equation"])
    exact("conservation is coupled rather than isolated", rows["STRESS_CONSERVATION"]["status"] == "BUILT_IDENTITY_ONLY" and "Coupled Ward identity" in rows["STRESS_CONSERVATION"]["native_equation"])
    exact("cosmology requires observation stress and two distinct scalar modes", "T_obs" in rows["COSMO_DISTORTION"]["observation_map"] and "heavy Higgs-like and light cosmological" in rows["COSMO_DISTORTION"]["next_build"])
    exact("PP3 is a downstream test rather than construction data", rows["FLRW_PP3"]["status"] == "DOWNSTREAM_TEST" and "downstream test" in rows["FLRW_PP3"]["datum_use"])
    exact("BV status is explicitly partial", rows["QUANTUM_BV"]["status"] == "PARTIAL_BV" and "currently resolved gauge sector" in rows["QUANTUM_BV"]["native_equation"])
    exact("anomaly is an obstruction test not a replacement equation", rows["ANOMALY_CONSISTENCY"]["status"] == "DOWNSTREAM_TEST" and "No native replacement equation" in rows["ANOMALY_CONSISTENCY"]["native_equation"])
    exact("generation row forbids block-to-count inference", rows["GENERATION_INDEX"]["status"] == "DOWNSTREAM_TEST" and "three blocks" in rows["GENERATION_INDEX"]["kill"] and "P3" in rows["GENERATION_INDEX"]["datum_use"])
    exact("datum is carried as a conditional equation family", "(I_d,E_d,L_d,R_d,D_d)" in rows["EXTERNAL_DATUM_OBSERVATION"]["standard_equation"] and "For every d" in rows["EXTERNAL_DATUM_OBSERVATION"]["native_equation"])

    planted("a standard equation is copied verbatim as its native replacement", any(row["standard_equation"] == row["native_equation"] for row in rows.values()))
    planted("Bianchi alone is Yang-Mills dynamics", rows["GAUGE_YANG_MILLS"]["native_equation"] == "D_A F_A=0")
    planted("a Clifford carrier is already a physical Dirac equation", rows["DIRAC_MATTER"]["status"] == "BUILT_NATIVE_PARENT")
    planted("any vertical scalar is already the Higgs", rows["HIGGS_EWSB"]["status"] == "BUILT_NATIVE_PARENT")
    planted("the connection automatically emits the Standard Model gauge algebra", rows["FORCE_DECOMPOSITION"]["status"] == "BUILT_NATIVE_PARENT")
    planted("the preboundary two-form already selects a physical polarization", rows["QUANTUM_BV"]["status"] == "BUILT_NATIVE_PARENT")
    planted("three provenance sectors force three generations", "three blocks imply three" in rows["GENERATION_INDEX"]["native_equation"].lower())
    planted("PP3 selects the cosmological mode", "use PP3 to select" in rows["FLRW_PP3"]["next_build"])
    planted("external data may contain the Standard Model", "gauge algebra" in rows["EXTERNAL_DATUM_OBSERVATION"]["datum_use"].lower())

    print(
        "ERIC-NATIVE-PHYSICS-EQUATION-ATLAS: "
        f"{exact_checks} exact checks + {planted_checks} planted failures = "
        f"{exact_checks + planted_checks} PASS"
    )
    print("RESULT: one G2/G3 parent is mapped to fifteen physical jobs and conditional shadows")
    print("RESULT: every open arrow has a bounded construction and decisive kill")
    print("RESULT: one stationary reduced Hessian precedes particle naming and downstream tests")
    print("BOUNDARY: no Maxwell/YM/Dirac/Einstein/Higgs/cosmology/anomaly/count recovery is claimed")


if __name__ == "__main__":
    main()
