#!/usr/bin/env python3
"""Controls for the paired Curt--Eric GU axiom and argument graph.

This validates provenance grades, dependencies, anti-collapse rules, atlas
integration, and a small exact residual-square identity.  It does not prove a
GU action, factorization, Higgs, Yukawa sector, field equation, or spectrum.
"""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GRAPH = ROOT / "lab/process/paired-curt-eric-gu-axiom-graph.json"
ATLAS = ROOT / "lab/process/eric-native-physics-equation-replacement-atlas.json"
CURT_REPORT = ROOT / "lab/sources/curt-jaimungal-gu-iceberg-claim-reconciliation-2026-07-31.md"
PAIRED_REPORT = ROOT / "lab/sources/paired-curt-eric-gu-axiom-and-argument-reconstruction-2026-07-31.md"

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


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [
        [sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0)) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def main() -> None:
    data = json.loads(GRAPH.read_text())
    atlas = json.loads(ATLAS.read_text())
    curt_report = CURT_REPORT.read_text()
    paired_report = PAIRED_REPORT.read_text()
    axioms = {row["id"]: row for row in data["axioms"]}
    chains = {row["id"]: row for row in data["argument_chains"]}
    allowed_grades = set(data["grade_vocabulary"])

    exact("all forty axioms are uniquely identified", len(axioms) == len(data["axioms"]) == 40)
    exact("all nine argument chains are uniquely identified", len(chains) == len(data["argument_chains"]) == 9)
    exact("grade vocabulary is the preregistered seven-way split", allowed_grades == {
        "EXPLICIT_CURT",
        "EXPLICIT_ERIC",
        "ERIC_CORRECTION",
        "MANUSCRIPT_DEFINED",
        "NECESSARY_IMPLICATION",
        "PLAUSIBLE_COMPLETION",
        "UNSUPPORTED",
    })
    exact("every axiom uses a declared grade", all(row["grade"] in allowed_grades for row in axioms.values()))
    exact("every axiom carries a source locator and construction gate", all(row["locators"] and row["construction_gate"].strip() for row in axioms.values()))
    exact("every dependency resolves", all(set(row["depends_on"]) <= set(axioms) for row in axioms.values()))
    exact("every chain node resolves", all(set(row["nodes"]) <= set(axioms) for row in chains.values()))
    exact("every source-supported spine is inside its chain", all(set(row["source_supported_spine"]) <= set(row["nodes"]) for row in chains.values()))
    exact("every first open node is inside its chain", all(row["first_open_decisive_node"] in row["nodes"] for row in chains.values()))

    exact("two-layer architecture is an Eric correction", axioms["AX-A01"]["grade"] == "ERIC_CORRECTION" and axioms["AX-A04"]["grade"] == "ERIC_CORRECTION")
    exact("second action is downstream of the first", "AX-A01" in axioms["AX-A04"]["depends_on"])
    exact("draft square is specifically the bosonic residual", axioms["AX-A05"]["grade"] == "MANUSCRIPT_DEFINED" and "Upsilon_omega^B" in axioms["AX-A05"]["statement"])
    exact("total Einstein-Dirac residual square remains a proposed extension", axioms["AX-A05T"]["grade"] == "PLAUSIBLE_COMPLETION" and "non-source-exact" in axioms["AX-A05T"]["statement"] and "Q_B and Q_ED" in axioms["AX-A05T"]["construction_gate"])
    exact("draft residual square remains distinct from spoken factorization", axioms["AX-A05"]["grade"] == "MANUSCRIPT_DEFINED" and axioms["AX-A07"]["grade"] == "EXPLICIT_ERIC")
    exact("factorization gate retains gauge boundary and curvature terms", all(token in axioms["AX-A07"]["construction_gate"] for token in ("gauge", "curvature", "boundary")))
    exact("derivative order separates Einsteinian and Yang-Millsian senses", axioms["AX-A06"]["grade"] == "EXPLICIT_ERIC" and "differential order" in axioms["AX-A06"]["construction_gate"])

    exact("Higgs parent is explicitly an ad-valued one-form", axioms["AX-H01"]["grade"] == "EXPLICIT_ERIC" and "ad-valued one-form" in axioms["AX-H01"]["statement"])
    exact("connection and distortion Higgs carriers remain a typed fork", axioms["AX-H01F"]["grade"] == "NECESSARY_IMPLICATION" and all(token in axioms["AX-H01F"]["construction_gate"] for token in ("phi_varpi", "phi_T", "gauge laws", "non-equivalence")))
    exact("observed Higgs is explicitly not left adjoint-valued", axioms["AX-H03"]["grade"] == "ERIC_CORRECTION" and "must not remain" in axioms["AX-H03"]["statement"])
    exact("scalarization is a required map rather than ordinary pullback", axioms["AX-H02"]["grade"] == "NECESSARY_IMPLICATION" and "contraction" in axioms["AX-H02"]["construction_gate"])
    exact("trace Higgs remains a rival route", axioms["AX-H08"]["grade"] == "EXPLICIT_CURT" and "separate" in axioms["AX-H08"]["construction_gate"])
    exact("physical Higgs chain starts failing at the carrier fork", chains["CHAIN-HIGGS"]["first_open_decisive_node"] == "AX-H01F")

    exact("minimal and Yukawa common origin is explicit Eric", axioms["AX-Y02"]["grade"] == "EXPLICIT_ERIC")
    exact("Krein bilinear is a necessary implication", axioms["AX-Y03"]["grade"] == "NECESSARY_IMPLICATION" and "Krein" in axioms["AX-Y03"]["statement"])
    exact("coefficient-free Yukawa is unsupported", axioms["AX-Y04"]["grade"] == "UNSUPPORTED" and "coefficient" in axioms["AX-Y04"]["name"])
    exact("staged Yukawa is a proposed completion not a source theorem", axioms["AX-Y05"]["grade"] == "PLAUSIBLE_COMPLETION")
    exact("Yukawa chain stops first at the physical bilinear", chains["CHAIN-YUKAWA"]["first_open_decisive_node"] == "AX-Y03")

    exact("Shiab is recorded as a contraction correction", axioms["AX-S03"]["grade"] == "ERIC_CORRECTION" and "never call the Shiab operation a projection" in axioms["AX-S03"]["construction_gate"])
    exact("Euler-covector typing is a necessary inference rather than an Eric quote", axioms["AX-S03E"]["grade"] == "NECESSARY_IMPLICATION" and all(token in axioms["AX-S03E"]["statement"] for token in ("codomain", "density", "pairing", "Euler covector")))
    exact("Step 13 still is kept as rough-note secondary evidence", "rough notes" in data["sources"]["CURT-ICEBERG-STEP13-STILL"]["role"])
    exact("Step 13 still has durable video and image custody", data["sources"]["CURT-ICEBERG-STEP13-STILL"]["source_video_locator"].startswith("00:53:03") and data["sources"]["CURT-ICEBERG-STEP13-STILL"]["supplied_image_sha256"] == "66a6438569fe0e1e5528b3b09de303dfa7c2f992d81ca3a322f27fa64f352fb2" and data["sources"]["CURT-ICEBERG-STEP13-STILL"]["supplied_image_dimensions"] == "1280x960 JPEG")
    exact("Step 13 types the odd carrier without pretending closure", axioms["AX-S04"]["grade"] == "EXPLICIT_CURT" and all(token in axioms["AX-S04"]["construction_gate"] for token in ("odd bracket", "Jacobi", "derivative cocycle")))
    exact("Dirac and generation chains both use the Step 13 carrier", all("AX-S04" in chains[name]["nodes"] for name in ("CHAIN-DIRAC", "CHAIN-GENERATIONS")))

    exact("generation decomposition is not graded as a count theorem", axioms["AX-R05"]["grade"] == "NECESSARY_IMPLICATION" and "P3" in axioms["AX-R05"]["construction_gate"])
    exact("field pullback and equation dual remain separate", axioms["AX-R02"]["grade"] == "NECESSARY_IMPLICATION" and all(token in axioms["AX-R02"]["construction_gate"] for token in ("L^vee", "L^!", "leakage")))
    exact("physical quotient remains mandatory", axioms["AX-R03"]["grade"] == "NECESSARY_IMPLICATION" and "boundary" in axioms["AX-R03"]["construction_gate"])

    paired = atlas["paired_curt_eric_reconstruction"]
    exact("atlas points to the paired graph and report", paired["registry"] == "lab/process/paired-curt-eric-gu-axiom-graph.json" and paired["source_report"] == "lab/sources/paired-curt-eric-gu-axiom-and-argument-reconstruction-2026-07-31.md")
    exact("atlas records forty axioms and nine chains", paired["coverage"] == "40 typed axioms and nine recovery chains")
    order = atlas["coherent_dependency_order"]
    exact("source-exact bosonic square precedes the total-residual rival", order.index("MANUSCRIPT_BOSONIC_RESIDUAL_AND_QB_SQUARE") < order.index("COUPLED_EINSTEIN_DIRAC_FIRST_LAYER_AND_FULL_RESIDUAL") < order.index("CONJECTURAL_TOTAL_RESIDUAL_QED_SQUARE_RIVAL"))
    exact("carrier fork precedes staged Hessians and naming", order.index("CONJECTURAL_TOTAL_RESIDUAL_QED_SQUARE_RIVAL") < order.index("VARPI_VERSUS_DISTORTION_HIGGS_CARRIER_FORK") < order.index("STAGED_HESSIANS_AND_FACTORIZATION_TEST") < order.index("LOW_ENERGY_MODE_AND_GROUP_IDENTIFICATION"))
    exact("old reconciliation declares paired-source supersession", "Paired-source supersession" in curt_report and "second Yang--Mills--Higgs action" in curt_report)
    exact("paired report distinguishes incidence and coefficient claims", "incidence claim" in paired_report and "coefficient claim" in paired_report)
    exact("paired report carries the supplied still", "The supplied Step 13 still" in paired_report and "rough notes" in paired_report)

    swing = data["next_swing"]
    exact("next swing is the staged residual square", swing["id"] == "E6-STAGED-RESIDUAL-SQUARE")
    exact("next swing constructs rather than restates the missing objects", all(any(token in step for step in swing["steps"]) for token in ("I2_B", "I2_ED", "phi_varpi", "phi_T")))
    exact("datum ledger is preserved", all(token in swing["datum_rule"] for token in ("P1", "P2", "P3")))
    exact("eleven anti-collapse controls are present", len(data["anti_collapse_controls"]) == 11)
    exact("five nonclaim families are explicit", len(data["nonclaims"]) == 5)

    # Exact finite control for the only algebraic implication used by the next
    # swing: if Upsilon(x)=Jx at a stationary point, then the Hessian of
    # 1/2<Upsilon,Q Upsilon> is J^T Q J.  Q is indispensable and may be
    # indefinite; this fixture does not identify a GU residual or pairing.
    j = [
        [Fraction(1), Fraction(2)],
        [Fraction(0), Fraction(1)],
        [Fraction(3), Fraction(-1)],
    ]
    q = [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(-1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(2)],
    ]
    h = matmul(matmul(transpose(j), q), j)
    exact("residual-square stationary Hessian is exact J-transpose-Q-J", h == [[Fraction(19), Fraction(-4)], [Fraction(-4), Fraction(5)]])
    q_identity = [[Fraction(int(i == k)) for k in range(3)] for i in range(3)]
    h_identity = matmul(matmul(transpose(j), q_identity), j)
    exact("changing the residual pairing changes the second action Hessian", h_identity != h)

    planted("Curt's iceberg is itself a Weinstein formula source", data["sources"]["CURT-ICEBERG-2025"]["role"] == "primary theorem")
    planted("one first-order action already is Yang-Mills-Higgs", axioms["AX-A04"]["grade"] == "MANUSCRIPT_DEFINED_COMPLETE")
    planted("the manuscript squares the total Einstein-Dirac residual", axioms["AX-A05T"]["grade"] == "MANUSCRIPT_DEFINED")
    planted("spoken square root is a proved factorization", axioms["AX-A07"]["grade"] == "MANUSCRIPT_DEFINED")
    planted("any vertical component is a physical Higgs", chains["CHAIN-HIGGS"]["verdict"] == "PHYSICAL_HIGGS_DERIVED")
    planted("the variational connection and homogeneous distortion are one Higgs carrier", "interchangeable" in axioms["AX-H01F"]["statement"] and "not interchangeable" not in axioms["AX-H01F"]["statement"])
    planted("P_H may denote both the principal bundle and Higgs extraction", "P_H" in axioms["AX-H01F"]["construction_gate"])
    planted("the physical Higgs remains adjoint-valued", "remain adjoint-valued" in axioms["AX-H03"]["construction_gate"])
    planted("ordinary pullback changes a one-form into a scalar", axioms["AX-H02"]["grade"] == "EXPLICIT_ERIC")
    planted("curvature quartic proves a stable vacuum", axioms["AX-H07"]["grade"] == "MANUSCRIPT_DEFINED")
    planted("minimal coupling fixes Yukawa matrices", axioms["AX-Y04"]["grade"] == "EXPLICIT_ERIC")
    planted("bare operator proves the cross-chiral mass term", axioms["AX-Y03"]["grade"] == "MANUSCRIPT_DEFINED")
    planted("the Krein bilinear may omit the branch-dependent real structure", "reality" not in axioms["AX-Y03"]["construction_gate"])
    planted("the Step 13 table proves a Lie superalgebra", axioms["AX-S04"]["grade"] == "MANUSCRIPT_DEFINED")
    planted("Shiab is a projection", axioms["AX-S03"]["statement"] == "The relevant Shiab-type operation is a projection.")
    planted("three carrier pieces prove three generations", chains["CHAIN-GENERATIONS"]["verdict"] == "THREE_GENERATIONS_DERIVED")
    planted("a maximal compact is the selected physical group", axioms["AX-R04"]["grade"] == "MANUSCRIPT_DEFINED")
    planted("field pullback is physical equation recovery", axioms["AX-R02"]["grade"] == "EXPLICIT_CURT")
    planted("the indefinite residual pairing can be omitted", h == h_identity)
    planted("the next swing consumes P3 as a block count", "infer" in swing["datum_rule"] and "from a decomposition" not in swing["datum_rule"])

    print(
        "PAIRED-CURT-ERIC-AXIOM-GRAPH: "
        f"{exact_checks} exact checks + {planted_checks} planted failures = "
        f"{exact_checks + planted_checks} PASS"
    )
    print("RESULT: 40 axioms and nine recovery chains retain source and inference grades")
    print("RESULT: the manuscript bosonic square remains distinct from the conjectural total Einstein-Dirac residual square")
    print("RESULT: the Higgs extraction, Krein bilinear, residual pairing, and factorization remain explicit gates")
    print("BOUNDARY: no Higgs, Yukawa matrix, physical equation, gauge selection, generation count, or cosmology is claimed")


if __name__ == "__main__":
    main()
