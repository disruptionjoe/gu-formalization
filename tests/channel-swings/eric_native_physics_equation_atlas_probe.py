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
    exact("G2/G3 remains the declared first Einsteinian backbone", "I_G2" in backbone["action"] and "E_A=E_T" in backbone["connection_euler"] and "first Einsteinian parent" in data["thesis"])
    exact("killed compressed Euler shortcut remains recorded", backbone["killed_shortcut"] == "S_epsilon(F_(B+T))+kappa_1 T")
    exact("observation gate separates algebraic dual and Riesz adjoint", all(token in backbone["observation_gate"] for token in ("R_s L_s=1", "R_s D_Y L_s=D_X", "1-L_s R_s", "(D L_s)^vee", "(D L_s)^!", "sharp_X")))

    order = data["coherent_dependency_order"]
    exact("construction begins with C0 then carrier-specific census and port", order[:4] == ["C0_CHIMERIC_ZORRO_REAL_FORM_BRIDGE", "G3.5_TARGET_BLIND_NATURALITY_AND_ABLATION_ON_SURVIVING_CARRIER", "C0_TRIGGERED_G2_G3_CARRIER_PORT_IF_REQUIRED", "G4_OBSERVATION_RETRACT_DOMAIN_AND_BFV_QUOTIENT"])
    exact("odd action completes the first layer after the manuscript bosonic square is typed", order.index("G5_MINIMAL_ODD_EXTENSION_AND_ACTION_DERIVED_CURRENTS") < order.index("MANUSCRIPT_BOSONIC_RESIDUAL_AND_QB_SQUARE") < order.index("COUPLED_EINSTEIN_DIRAC_FIRST_LAYER_AND_FULL_RESIDUAL"))
    exact("total-residual rival and Higgs carrier fork precede staged Hessians", order.index("COUPLED_EINSTEIN_DIRAC_FIRST_LAYER_AND_FULL_RESIDUAL") < order.index("CONJECTURAL_TOTAL_RESIDUAL_QED_SQUARE_RIVAL") < order.index("VARPI_VERSUS_DISTORTION_HIGGS_CARRIER_FORK") < order.index("STAGED_HESSIANS_AND_FACTORIZATION_TEST") < order.index("LOW_ENERGY_MODE_AND_GROUP_IDENTIFICATION"))
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
    exact("Curt iceberg remains a secondary overlay with its own registry", data["source_corpus"]["CURT-ICEBERG-2025"]["grade"].startswith("secondary") and data["curt_iceberg_reconciliation"]["registry"] == "lab/process/curt-iceberg-native-crosswalk.json")
    exact("paired correction points to the axiom graph", data["paired_curt_eric_reconstruction"]["registry"] == "lab/process/paired-curt-eric-gu-axiom-graph.json" and "40 typed axioms" in data["paired_curt_eric_reconstruction"]["coverage"])
    exact("Curt overlay covers every primary callout without inventing Schrodinger", set(data["curt_iceberg_overlay"]) >= expected_callouts and data["curt_iceberg_overlay"]["PSC-SCHRODINGER"] == [])
    exact("C0 overlay carries Zorro chimeric signature and real-form steps", data["curt_iceberg_overlay"]["C0_FOUNDATIONAL_BRIDGE"] == ["CI-06", "CI-07", "CI-09", "CI-10", "CI-11", "CI-12"])
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
    exact("Yang-Mills separates the manuscript bosonic square from the total-residual rival", all(token in crosswalk["PSC-YANG-MILLS"]["native_search_directive"] for token in ("manuscript-exact bosonic residual", "I2_B", "I2_ED", "F^2 comparator")))
    exact("Einstein routes through Layer 0 equation dual and spin two", all(token in crosswalk["PSC-EINSTEIN"]["native_search_directive"] for token in ("Layer 0", "equation-dual", "spin-two")))
    exact("Higgs preserves the connection-versus-distortion extraction fork", all(token in crosswalk["PSC-HIGGS"]["native_search_directive"] for token in ("Pi_Higgs^varpi", "Pi_Higgs^T", "varpi", "T", "K-paired", "gauge-mass")))
    exact("Higgs extraction no longer collides with principal-bundle P_H", "P_H" not in crosswalk["PSC-HIGGS"]["native_search_directive"])
    exact("Dirac routes to the first-layer odd action and second-layer square test", all(token in crosswalk["PSC-DIRAC"]["native_search_directive"] for token in ("minimal odd action", "first Einstein-Dirac layer", "K-paired", "current", "second Yang-Mills-Higgs action")))
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
    print("RESULT: the source-exact bosonic square and conjectural total-residual rival are mapped to fifteen physical jobs and conditional shadows")
    print("RESULT: every open arrow has a bounded construction and decisive kill")
    print("RESULT: ten primary-source callouts route into native carriers/operators rather than stopping")
    print("RESULT: the residual pairing second action and staged Hessians precede particle naming and downstream tests")
    print("BOUNDARY: no Maxwell/YM/Dirac/Einstein/Higgs/cosmology/anomaly/count recovery is claimed")


if __name__ == "__main__":
    main()
