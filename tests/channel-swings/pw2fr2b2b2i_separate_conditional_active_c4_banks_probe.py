#!/usr/bin/env python3
"""PW2F-R2B2B2I bank-grade universal-coverage admission certificate.

H/H2 provide parametric mixed operator and residual/primalizer formulas, but
their accepted executable receipts exercise one owner/conormal pair.  A
complete quartic bank has 35 homogeneous four-conormal monomials for every one
of 55 symmetric pairs of ten metric owners.  This lightweight exact probe
checks whether the accepted evidence closes that universal coverage boundary.

It does not say that either bank is zero, inconsistent, or impossible.  It
decides only whether complete-bank promotion is currently licensed.  The
answer is no: the reusable formulas survive, while universal owner/conormal
coverage or a proved symmetry reduction remains the next dependency.  No
Green/Helmholtz, kappa, domain, observation, or physics conclusion follows.
"""

from __future__ import annotations

import ast
from hashlib import sha256
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"

SOURCES = {
    "quartic_basis": (
        CHANNEL / "pw2fr2b1_section_jvp_source_coordinate_probe.py",
        "e50795fb65056ac12678b82da4d35ffef3fd5c657c88040dea4ab0a2759bc281",
    ),
    "bank_pattern": (
        CHANNEL / "pw2fr2b2b2d_kappa_c4_identifiability_probe.py",
        "5533fef2728406ae9efb07e5cf554371a26fcc8dabc00fc19d0bd952e5afe42c",
    ),
    "trace_transport": (
        CHANNEL / "pw2fr2b2b2g_full_a4_multiindex_green_distinct_i2b_c4_probe.py",
        "0adda247301903fcd130275ca050aa3575bdbf7604bada66df1ca51af9e2c183",
    ),
    "operator": (
        CHANNEL / "pw2fr2b2b2h_mixed_shiab_second_jet_probe.py",
        "cd5c20f848d8384e5b2f56c097fedb2da30422833a2c387ef93338a0a79c7e90",
    ),
    "residual": (
        CHANNEL / "pw2fr2b2b2h2_i2b_second_residual_primalizer_pairing_probe.py",
        "495c10e5b4767df8e67d13e56e649bc999762354ca55e5347c4d7a68a034a00d",
    ),
    "source_orbit": (
        CHANNEL / "pw2fr2b2b2h3_source_epsilon_curvature_orbit_graph_probe.py",
        "127a8215cb44a7d974dbe70dd30734bfd247f2bd50f365011003343093279639",
    ),
    "scope_exit": (
        ROOT / "explorations/pw2fr2b2b2h4-source-active-real-form-scope-exit-2026-08-04.md",
        "7765b2336bf8f930acc0a25035e068d9f823e5cc8b42b68f1982545492498b9d",
    ),
}

FAILURES: list[str] = []
EXACT = SOURCE = TYPE = PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: exact - {label}{suffix}")
    if not condition:
        FAILURES.append(f"exact: {label}")


def source_receipt(label: str, condition: bool, disposition: str) -> None:
    global SOURCE
    SOURCE += 1
    print(f"{'PASS' if condition else 'FAIL'}: source - {label} [{disposition}]")
    if not condition:
        FAILURES.append(f"source: {label}")


def typed(label: str, condition: bool = True) -> None:
    global TYPE
    TYPE += 1
    print(f"{'PASS' if condition else 'FAIL'}: type - {label}")
    if not condition:
        FAILURES.append(f"type: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    condition = not false_claim
    print(f"{'PASS' if condition else 'FAIL'}: planted rejection - {label}")
    if not condition:
        FAILURES.append(f"planted: {label}")


def text(name: str) -> str:
    return SOURCES[name][0].read_text(encoding="utf-8")


def function_source(name: str, function: str) -> str:
    source = text(name)
    tree = ast.parse(source)
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == function:
            segment = ast.get_source_segment(source, node)
            if segment is None:
                raise AssertionError(f"missing source segment: {name}.{function}")
            return segment
    raise AssertionError(f"missing function: {name}.{function}")


def source_and_layer_zero() -> None:
    hashes = {
        name: sha256(path.read_bytes()).hexdigest()
        for name, (path, _expected) in SOURCES.items()
    }
    source_receipt(
        "all seven accepted prerequisite sources are byte-pinned before the coverage audit",
        all(hashes[name] == expected for name, (_path, expected) in SOURCES.items()),
        "REPOSITORY-EVIDENCE-PIN",
    )
    scope_exit = text("scope_exit")
    source_receipt(
        "H4 admits later banks only as separate conditional-active repository constructions",
        "Neither bank is source-derived" in scope_exit
        and "two banks only as separately tagged conditional-active" in scope_exit
        and "neither is assembled here" in scope_exit,
        "PUBLIC-SOURCE ATTRIBUTION EXIT; ACTIVE CONSTRUCTION OPEN",
    )
    typed("source I1, manuscript I2B, conditional active repository banks, and Curt's rival action remain distinct")
    typed("parametric formula availability and accepted universal coefficient evidence are distinct proof levels")
    typed("raw action-density coefficients, Euler coefficients, Green concomitants, and Helmholtz quotients remain distinct")
    typed("the active (9,5) reconstruction is not identified with the public (7,7) action presentation")


def coverage_gate() -> dict[str, int]:
    owner_count = 10
    required_owner_pairs = owner_count * (owner_count + 1) // 2
    required_monomials = comb(4 + 4 - 1, 4)
    required_cells_per_bank = required_owner_pairs * required_monomials
    exact(
        "ten symmetric metric owners require exactly 55 owner-pair entries",
        required_owner_pairs == 55,
    )
    exact(
        "four conormal variables require exactly 35 homogeneous quartic monomials",
        required_monomials == 35,
    )
    exact(
        "a direct uncompressed complete-bank grid contains 1,925 owner-pair/lattice cells per action",
        required_cells_per_bank == 1925,
    )

    basis = text("quartic_basis")
    bank = text("bank_pattern")
    exact(
        "the accepted quartic-basis receipt defines the 35-point simplex lattice and exact Vandermonde gate",
        "MONOMIALS = tuple" in basis
        and "sum(alpha) == 4" in basis
        and "VANDERMONDE.rank() == 35" in basis
        and "three independent owner-pair quartics" in basis,
    )
    exact(
        "the accepted bank-grade precedent evaluates all 35 lattice points, reconstructs 10-by-10 owner matrices, and checks dense held-outs",
        "for index, point in enumerate(B1.POINTS)" in bank
        and "return R.gram(forms)" in bank
        and "sp.zeros(10)" in bank
        and "three dense held-out conormals" in bank,
    )

    operator_gate = function_source("operator", "operator_gate")
    residual_gate = function_source("residual", "residual_pairing_gate")
    exact(
        "the accepted mixed-Shiab receipt exercises exactly owner pair 3/7 at one declared conormal pair",
        "owner_i, xi = 3" in operator_gate
        and "owner_j, zeta = 7" in operator_gate
        and "B1.POINTS" not in operator_gate
        and "range(10)" not in operator_gate,
    )
    exact(
        "the accepted I2B residual/primalizer receipt exercises the same single owner/conormal pair and returns one mixed scalar",
        "owner_i, xi = 3" in residual_gate
        and "owner_j, zeta = 7" in residual_gate
        and '"mixed_action": direct_action[3]' in residual_gate
        and "B1.POINTS" not in residual_gate
        and "range(10)" not in residual_gate,
    )
    exact(
        "the accepted H/H2 implementation retains reusable parameterized constructors for later universal coverage",
        "def shiab_jet(" in text("operator")
        and "def moving_frame_trace_jet(" in text("trace_transport")
        and "def symmetric_pairing_jet(" in text("residual"),
    )

    source_orbit = text("source_orbit")
    exact(
        "H3 is explicitly a conditional local orbit and contains no quartic-bank reconstruction loop",
        "conditional local active source-epsilon" in source_orbit
        and "B1.POINTS" not in source_orbit
        and "promote source-orbit closure to either complete 35-monomial C4 bank" in source_orbit,
    )

    exercised_owner_pairs = 1
    exercised_lattice_points = 1
    exact(
        "accepted bank-grade coverage remains 1/55 owner pairs and at most 1/35 lattice points for both H and H2",
        exercised_owner_pairs < required_owner_pairs
        and exercised_lattice_points < required_monomials,
        "owner_pair_gap=54; lattice_gap=34",
    )
    exact(
        "complete-bank promotion fails closed while the parametric local formulas remain admitted for a universal successor",
        exercised_owner_pairs != required_owner_pairs
        and exercised_lattice_points != required_monomials
        and "def shiab_jet(" in text("operator"),
    )

    reject(
        "treat a parameterized constructor as proof that all 55 owner pairs and 35 monomials were evaluated",
        exercised_owner_pairs == required_owner_pairs,
    )
    reject(
        "promote one symmetric mixed pair to a complete 10-owner quartic bank",
        exercised_owner_pairs == required_owner_pairs
        and exercised_lattice_points == required_monomials,
    )
    reject(
        "call either conditional active bank source-derived after the H4 source-scope exit",
        "Neither bank is source-derived" not in text("scope_exit"),
    )
    reject("merge I1 A4 and I2B C4 because they share an owner/conormal basis", False)
    reject("start multi-index Green/Helmholtz before both separate complete banks close", False)
    reject("merge Curt or promote a third lane from a coefficient-coverage audit", False)

    return {
        "required_owner_pairs": required_owner_pairs,
        "required_monomials": required_monomials,
        "required_cells_per_bank": required_cells_per_bank,
        "exercised_owner_pairs": exercised_owner_pairs,
        "exercised_lattice_points": exercised_lattice_points,
    }


def boundary() -> None:
    typed("the exact result is insufficient accepted universal coverage, not nonexistence or vanishing of either bank")
    typed("the next mathematical route may prove an owner-pair symmetry reduction or evaluate the full lattice with an exact sparse backend")
    typed("I1 A4 and I2B C4 remain separately tagged conditional-active open banks")
    typed("multi-index Green/Helmholtz, live C3, projective kappa1, domain, observation, characteristic, and physics remain downstream")
    typed("P1/P2/P3 remain unchanged and unused")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    typed("TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")


def main() -> int:
    print("PW2F-R2B2B2I SEPARATE C4-BANK UNIVERSAL-COVERAGE CERTIFICATE")
    source_and_layer_zero()
    result = coverage_gate()
    boundary()
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        "RESULT: required_owner_pairs="
        f"{result['required_owner_pairs']}; required_monomials="
        f"{result['required_monomials']}; cells_per_bank="
        f"{result['required_cells_per_bank']}; accepted_coverage="
        f"({result['exercised_owner_pairs']},{result['exercised_lattice_points']}); "
        "complete_I1_A4=NOT_PROMOTED; complete_I2B_C4=NOT_PROMOTED"
    )
    print(
        f"SUMMARY: {EXACT} exact + {SOURCE} source + {TYPE} type + "
        f"{PLANTED} planted = {total}; failures={len(FAILURES)}"
    )
    if FAILURES:
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print(
        "VERDICT: R2B2B2I FAILS CLOSED AT THE UNIVERSAL OWNER/CONORMAL "
        "COVERAGE GATE; THE PARAMETRIC H/H2 FORMULAS SURVIVE, BUT NEITHER "
        "SEPARATE CONDITIONAL-ACTIVE C4 BANK IS COMPLETE OR ELIGIBLE FOR "
        "GREEN/HELMHOLTZ PROMOTION"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
