#!/usr/bin/env python3
"""Contract checks for the Eric-native physics equation replacement atlas.

This is a type/status/dependency certificate. It does not compute the future
stationary background, observation domain, Hessian spectrum, odd Euler
operator, anomaly, generation index, or cosmological prediction.

The source-callout checks require every requested Weinstein passage to route
to a bounded native construction rather than ending at a missing formula.
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
    crosswalk = {row["id"]: row for row in data["requested_source_crosswalk"]}

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

    expected_callouts = {
        "PSC-MAXWELL",
        "PSC-YANG-MILLS",
        "PSC-EINSTEIN",
        "PSC-HIGGS",
        "PSC-DIRAC",
        "PSC-SCHRODINGER",
        "PSC-WEAK",
        "PSC-STRONG",
        "PSC-DARK-ENERGY",
        "PSC-DARK-MATTER",
    }
    exact("all ten requested primary-source callouts are present once", set(crosswalk) == expected_callouts and len(crosswalk) == len(data["requested_source_crosswalk"]))
    exact("every source callout becomes a native search directive", all(row["native_search_directive"].strip() for row in crosswalk.values()))
    exact("every source callout retains a boundary after routing", all(row["boundary"].strip() for row in crosswalk.values()))
    exact("all crosswalk sources resolve in the declared corpus", all(callout["source_id"] in data["source_corpus"] for row in crosswalk.values() for callout in row["callouts"]))
    exact("the two Into the Impossible sources remain distinct", data["source_corpus"]["WG-2021-ITI-REVEALED"]["title"] != data["source_corpus"]["WG-2025-ITI-UCSD"]["title"])
    local_sources = {
        source_id: (ROOT / row["local"]).read_text()
        for source_id, row in data["source_corpus"].items()
        if row.get("local")
    }
    exact("every declared local primary-source transcript exists", len(local_sources) == 3)
    exact("Oxford anchors retain equation dark-sector and Dirac-square passages", all(token in local_sources["WG-OXFORD-PORTAL"] for token in ("00:43:47", "02:08:36", "02:40:24")))
    exact("TOE anchors retain GU-list distortion and dark-recoupling passages", all(token in local_sources["WG-2025-TOE"] for token in ("[01:35:23]", "[02:22:20]", "[02:50:38]")))
    exact("UCSD Into the Impossible anchors retain dark-matter and Higgs passages", all(token in local_sources["WG-2025-ITI-UCSD"] for token in ("[00:38:09]", "[00:42:42]", "[00:43:04]")))
    exact("Maxwell routes to an abelian mode of the same Hessian", "Do not add a separate Maxwell action" in crosswalk["PSC-MAXWELL"]["native_search_directive"] and "same gauge system" in crosswalk["PSC-MAXWELL"]["native_search_directive"])
    exact("Yang-Mills routes through G2 reduction and F2 ablation", "G2" in crosswalk["PSC-YANG-MILLS"]["native_search_directive"] and "F^2 comparator" in crosswalk["PSC-YANG-MILLS"]["native_search_directive"])
    exact("Einstein routes through Layer 0 equation dual and spin two", all(token in crosswalk["PSC-EINSTEIN"]["native_search_directive"] for token in ("Layer 0", "equation-dual", "spin-two")))
    exact("Higgs routes to one vertical action-selected curvature mode", all(token in crosswalk["PSC-HIGGS"]["native_search_directive"] for token in ("vertical ad-valued one-form", "action-selected", "quartic", "K-paired")))
    exact("Dirac routes to one odd action emitting operator mass and current", all(token in crosswalk["PSC-DIRAC"]["native_search_directive"] for token in ("minimal odd action", "Euler/Hessian", "K-paired", "current")))
    exact("Schrodinger absence still routes to a native Hamiltonian test", crosswalk["PSC-SCHRODINGER"]["classification"] == "NO_LOCATED_DIRECT_GU_CLAIM" and all(token in crosswalk["PSC-SCHRODINGER"]["native_search_directive"] for token in ("BV/BFV", "Hamiltonian", "unitary", "i d_t Psi=H_phys Psi")))
    exact("weak and strong route through one action-selected stabilizer", "action-selected maximal compact stabilizer" in crosswalk["PSC-WEAK"]["native_search_directive"] and "same action-selected maximal compact stabilizer" in crosswalk["PSC-STRONG"]["native_search_directive"])
    exact("dark energy routes through distortion stress and two scalar modes", all(token in crosswalk["PSC-DARK-ENERGY"]["native_search_directive"] for token in ("T=A-B", "observation stress", "light cosmological", "heavy Higgs")))
    exact("dark matter routes through the complement of the luminous odd image", all(token in crosswalk["PSC-DARK-MATTER"]["native_search_directive"] for token in ("luminous observation image", "complement", "masses and charges", "high-curvature recoupling")))
    exact("atlas rows point only to existing source callouts", all(set(row.get("primary_source_callout_ids", ())) <= set(crosswalk) for row in rows.values()))
    exact("requested callouts are connected back into the atlas", set().union(*(set(row.get("primary_source_callout_ids", ())) for row in rows.values())) == expected_callouts)

    planted("a standard equation is copied verbatim as its native replacement", any(row["standard_equation"] == row["native_equation"] for row in rows.values()))
    planted("Bianchi alone is Yang-Mills dynamics", rows["GAUGE_YANG_MILLS"]["native_equation"] == "D_A F_A=0")
    planted("a Clifford carrier is already a physical Dirac equation", rows["DIRAC_MATTER"]["status"] == "BUILT_NATIVE_PARENT")
    planted("any vertical scalar is already the Higgs", rows["HIGGS_EWSB"]["status"] == "BUILT_NATIVE_PARENT")
    planted("the connection automatically emits the Standard Model gauge algebra", rows["FORCE_DECOMPOSITION"]["status"] == "BUILT_NATIVE_PARENT")
    planted("the preboundary two-form already selects a physical polarization", rows["QUANTUM_BV"]["status"] == "BUILT_NATIVE_PARENT")
    planted("three provenance sectors force three generations", "three blocks imply three" in rows["GENERATION_INDEX"]["native_equation"].lower())
    planted("PP3 selects the cosmological mode", "use PP3 to select" in rows["FLRW_PP3"]["next_build"])
    planted("external data may contain the Standard Model", "gauge algebra" in rows["EXTERNAL_DATUM_OBSERVATION"]["datum_use"].lower())
    planted("no direct Schrodinger source means the native search stops", not crosswalk["PSC-SCHRODINGER"]["native_search_directive"])
    planted("generic quantum-wave language is a spoken GU Schrodinger equation", crosswalk["PSC-SCHRODINGER"]["classification"] == "DIRECT_GU_REPLACEMENT_AND_FORMULA")
    planted("weak group branching is already a weak-boson field equation", crosswalk["PSC-WEAK"]["classification"] == "DIRECT_STANDARD_BASELINE_AND_GU_REPLACEMENT")
    planted("dark matter is the DESI dark-energy passage", crosswalk["PSC-DARK-MATTER"]["callouts"] == crosswalk["PSC-DARK-ENERGY"]["callouts"])
    planted("2021 GU Revealed and 2025 UCSD are one transcript", data["source_corpus"]["WG-2021-ITI-REVEALED"] == data["source_corpus"]["WG-2025-ITI-UCSD"])

    print(
        "ERIC-NATIVE-PHYSICS-EQUATION-ATLAS: "
        f"{exact_checks} exact checks + {planted_checks} planted failures = "
        f"{exact_checks + planted_checks} PASS"
    )
    print("RESULT: one G2/G3 parent is mapped to fifteen physical jobs and conditional shadows")
    print("RESULT: every open arrow has a bounded construction and decisive kill")
    print("RESULT: ten primary-source callouts route into native carriers/operators rather than stopping")
    print("RESULT: one stationary reduced Hessian precedes particle naming and downstream tests")
    print("BOUNDARY: no Maxwell/YM/Dirac/Einstein/Higgs/cosmology/anomaly/count recovery is claimed")


if __name__ == "__main__":
    main()
