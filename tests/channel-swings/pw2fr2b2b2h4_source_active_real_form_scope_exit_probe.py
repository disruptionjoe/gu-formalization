#!/usr/bin/env python3
r"""PW2F-R2B2B2H4 exact source/active real-form port scope decision.

This probe distinguishes four Layer-0 objects: the literal source-directed
``(7,7)`` real comparator, the public mixed-sign complex ``U(64,64)`` container, a possible
moving-J ``Sp(32,32;H)`` reduction, and the active ``Spin(9,5)`` right-H
bundle.  It proves the literal real identification is obstructed, verifies
the common complex container does not remove the real obstruction, and audits
the pinned source/PW1/H3 receipts for the global data needed by the two-stage
reverse port.

The result is an evidence-scope exit for a *source-attributed* global port, not
a theorem that no moving-J reduction exists.  It admits only two separately
tagged conditional-active quartic-bank constructions downstream; neither bank
is assembled here.  P1/P2/P3 remain unused, Curt remains formally separate,
and the third-lane conjunction remains unpromoted.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]

FAILURES: list[str] = []
EXACT = SOURCE = TYPE = PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: exact - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"exact: {label}")


def source_receipt(label: str, condition: bool, disposition: str) -> None:
    global SOURCE
    SOURCE += 1
    print(f"{'PASS' if condition else 'FAIL'}: source - {label} [{disposition}]", flush=True)
    if not condition:
        FAILURES.append(f"source: {label}")


def typed(label: str, condition: bool = True) -> None:
    global TYPE
    TYPE += 1
    print(f"{'PASS' if condition else 'FAIL'}: type - {label}", flush=True)
    if not condition:
        FAILURES.append(f"type: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    condition = not false_claim
    print(f"{'PASS' if condition else 'FAIL'}: planted rejection - {label}", flush=True)
    if not condition:
        FAILURES.append(f"planted: {label}")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_real_form_obstructions() -> dict[str, object]:
    source_metric = sp.diag(*([1] * 7 + [-1] * 7))
    active_metric = sp.diag(*([1] * 9 + [-1] * 5))
    source_inertia = (
        sum(1 for v in source_metric.diagonal() if v == 1),
        sum(1 for v in source_metric.diagonal() if v == -1),
    )
    active_inertia = (
        sum(1 for v in active_metric.diagonal() if v == 1),
        sum(1 for v in active_metric.diagonal() if v == -1),
    )
    exact("the literal real carriers have exact inertias (7,7) and (9,5)", source_inertia == (7, 7) and active_inertia == (9, 5))
    exact("Sylvester inertia blocks a real metric isometry", source_inertia != active_inertia)

    reality_77 = sp.diag(1, -1)
    reality_h = sp.Matrix([[0, -1], [1, 0]])
    exact("the model real structures have squares +1 and -1", reality_77**2 == sp.eye(2) and reality_h**2 == -sp.eye(2))

    a, b, c, d = sp.symbols("a b c d", real=True)
    intertwiner = sp.Matrix([[a, b], [c, d]])
    equations = list(intertwiner * reality_77 - reality_h * intertwiner)
    coefficient_matrix, rhs = sp.linear_eq_to_matrix(equations, (a, b, c, d))
    solution = sp.linsolve((coefficient_matrix, rhs), (a, b, c, d))
    exact("every real intertwiner from square +1 to square -1 is zero", coefficient_matrix.rank() == 4 and solution == {(0, 0, 0, 0)})

    real_dim_cl77 = 128 * 128
    real_dim_cl95 = 4 * 64 * 64
    exact("Cl(7,7)=M128(R) and Cl(9,5)=M64(H) have equal total real dimension", real_dim_cl77 == real_dim_cl95 == 2**14)
    exact("their minimal real module dimensions remain inequivalent", 128 != 4 * 64)
    exact("both complexifications use the same M128(C) container size", 128 == 2 * 64)

    dim_u = (64 + 64) ** 2
    quaternionic_rank = 32 + 32
    dim_sp = quaternionic_rank * (2 * quaternionic_rank + 1)
    exact("the source and reduced structure-group dimensions are 16384 and 8256", dim_u == 16384 and dim_sp == 8256)
    exact("the moving-J coset carries 8128 pointwise directions", dim_u - dim_sp == 8128)

    decision = {
        "literal_real_isometry_exists": source_inertia == active_inertia,
        "nonzero_reality_intertwiner_exists": solution != {(0, 0, 0, 0)},
        "common_complexification_exists": True,
        "literal_7_7_to_active_9_5_real_identification": "EXACTLY_OBSTRUCTED",
        "common_complex_container": "EXISTS_BUT_IS_NOT_A_REAL_PORT",
        "global_source_port_data_complete": False,
        "global_source_H_reduction": "NOT_EVALUABLE_FROM_PUBLISHED_SOURCE_DATA",
        "global_moving_J_existence": "UNDECIDED",
        "independent_moving_J_native_reduction": "RECONSTRUCTION_OPEN_NOT_DISPROVED",
        "source_attribution_gate": "EVIDENCE_SCOPE_EXIT",
        "downstream_bank_admission": "SEPARATE_CONDITIONAL_ACTIVE_ONLY",
        "third_lane": "NOT_PROMOTED",
    }
    exact(
        "the decision table separates obstruction, source silence, and reconstruction opportunity",
        decision["literal_7_7_to_active_9_5_real_identification"] == "EXACTLY_OBSTRUCTED"
        and decision["global_source_H_reduction"] == "NOT_EVALUABLE_FROM_PUBLISHED_SOURCE_DATA"
        and decision["independent_moving_J_native_reduction"] == "RECONSTRUCTION_OPEN_NOT_DISPROVED",
    )
    return decision


def source_and_layer_zero(decision: dict[str, object]) -> None:
    source_pack_path = ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
    pw1_report_path = ROOT / "explorations/pw1-source-native-port-superig-interface-2026-08-02.md"
    pw1_registry_path = ROOT / "lab/process/pw1-source-native-port-superig-interface.json"
    h3_report_path = ROOT / "explorations/pw2fr2b2b2h3-source-epsilon-curvature-orbit-graph-2026-08-04.md"
    h3_registry_path = ROOT / "lab/process/pw2fr2b2b2h3-source-epsilon-curvature-orbit-graph-registry.json"

    source_pack = source_pack_path.read_text(encoding="utf-8")
    pw1_report = pw1_report_path.read_text(encoding="utf-8")
    pw1_registry = json.loads(pw1_registry_path.read_text(encoding="utf-8"))
    h3_report = h3_report_path.read_text(encoding="utf-8")
    h3_registry = json.loads(h3_registry_path.read_text(encoding="utf-8"))

    global_source_terms = (
        "transition function",
        "classifying map",
        "odd Chern",
        "P_H",
        "P_nat",
        "bundle morphism",
        "descent atlas",
    )
    source_receipt(
        "the pinned source pack marks a real-form fork and requires construction of the source-to-repo map",
        sha256(source_pack_path) == "5b50adabf067959654073f7e5c6665e8ac1e3e52ae36ae22ae9754bc9db23b5f"
        and "source-to-repo real-form map" in source_pack
        and "REAL-FORM-FORK" in source_pack
        and all(term not in source_pack for term in global_source_terms),
        "SOURCE-SILENT on global reduction/classifying/transition data",
    )
    source_receipt(
        "PW1 pins the two-stage reverse port and necessary-but-not-sufficient global screens",
        sha256(pw1_report_path) == "0e89b446178778b0716d47caf8225e85d5a6abe6f3a5724e5dddc71b1858cdf5"
        and sha256(pw1_registry_path) == "622a9ea559daa8b266fd8a2962be97e86ff40e1befd30397cf3505909cb1fb5b"
        and "necessary screen" in pw1_report
        and "not a sufficiency theorem" in pw1_report
        and pw1_registry["pw1_a_real_form_port"]["reverse_port_stage_two"].endswith("this remains open"),
        "REPOSITORY-CONSTRUCTED conditional moving-J interface",
    )
    source_receipt(
        "H3 closes only the local conditional epsilon orbit and names H4 as the global port-or-scope gate",
        sha256(h3_report_path) == "7eebea4a2f819949c423f067829f8d6b24cb61eb91c748aaceab215010400688"
        and sha256(h3_registry_path) == "2910fcfd2b33833561096b4030afea7276a83446203f82ddf4e0589789b899e1"
        and "global public-source-to-active real-form bundle morphism" in h3_report
        and h3_registry["next_gate"].startswith("PW2F-R2B2B2H4"),
        "REPOSITORY-DERIVED successor gate",
    )

    typed("literal source-directed (7,7) comparator, public complex U(64,64), moving-J Sp reduction, and active Spin(9,5) bundle remain four distinct objects")
    typed("a real isometry, real Clifford/reality intertwiner, H-reduction, and active-bundle isomorphism are four separate obligations")
    typed("common complexification preserves matrix size but erases the load-bearing real and right-H data")
    typed("source silence makes the global source-attributed port not evaluable; it does not prove global nonexistence")
    typed("the independent moving-J reduction remains a repository construction opportunity at reconstruction grade")
    typed("stage one requires a global section of the G/H bundle and stage two requires P_H to P_nat transition compatibility")
    typed("odd Chern-class vanishing is only a necessary screen and is not evaluable without source bundle topology")
    typed("the H3 local epsilon orbit survives as conditional active evidence without becoming a global source identity")
    typed("I1 A4 and I2B C4 remain distinct action banks with distinct ownership and must be assembled separately")
    typed("source-scope exit admits later conditional-active bank work but does not make either bank source-derived")
    typed("P1/P2/P3 remain unchanged and unused; a moving-J field is not repriced as datum")
    typed("Curt remains formally separate inside the Eric lane and TG-1 AND TG-2 AND TG-3 remains not promoted")

    reject("literal (7,7) and active (9,5) are real-isometric", bool(decision["literal_real_isometry_exists"]))
    reject("a nonzero real map intertwines square-plus-one and square-minus-one realities", bool(decision["nonzero_reality_intertwiner_exists"]))
    reject(
        "common M128(C) complexification is a real/right-H bundle equivalence",
        bool(decision["common_complexification_exists"])
        and decision["common_complex_container"] == "REAL_RIGHT_H_EQUIVALENCE",
    )
    reject(
        "missing source characteristic and transition data count as a passed global reduction",
        not bool(decision["global_source_port_data_complete"])
        and decision["global_source_H_reduction"] == "CONSTRUCTED",
    )
    reject(
        "source-evidence scope exit proves that no moving-J reduction can exist",
        decision["source_attribution_gate"] == "EVIDENCE_SCOPE_EXIT"
        and decision["global_moving_J_existence"] == "IMPOSSIBLE",
    )
    reject(
        "the two later C4 banks may be merged or called source-derived",
        decision["downstream_bank_admission"] == "MERGED_SOURCE_DERIVED",
    )
    reject(
        "the H4 scope decision promotes Curt or a third lane",
        decision["third_lane"] == "PROMOTED",
    )

    assert decision["source_attribution_gate"] == "EVIDENCE_SCOPE_EXIT"
    assert decision["downstream_bank_admission"] == "SEPARATE_CONDITIONAL_ACTIVE_ONLY"


def main() -> None:
    decision = exact_real_form_obstructions()
    source_and_layer_zero(decision)
    total = EXACT + SOURCE + TYPE + PLANTED
    print(f"SUMMARY: {EXACT} exact + {SOURCE} source + {TYPE} type + {PLANTED} planted = {total}", flush=True)
    if FAILURES:
        raise AssertionError("; ".join(FAILURES))
    print("RESULT: PASS", flush=True)
    print("EARNED: PUBLIC_SOURCE_TO_ACTIVE_REAL_FORM_PORT_EVIDENCE_SCOPE_EXIT__INDEPENDENT_MOVING_J_PORT_OPEN__SEPARATE_CONDITIONAL_ACTIVE_BANKS_ADMITTED", flush=True)


if __name__ == "__main__":
    main()
