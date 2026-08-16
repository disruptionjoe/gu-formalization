#!/usr/bin/env python3
"""Exact CB-5C source/representation bridge certificate.

This probe models only the trace-sector algebra needed to distinguish the
equation-(12.22) correlated F summand from the horizontal trace of the
post-contraction H210 port.  It contains no action, background, spectrum,
physical quotient, external datum, or family fit.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass, replace
from fractions import Fraction as F
from pathlib import Path


H_DIM = 4
V_DIM = 10
SPIN_TEST_DIM = 3
F_PER_HALF = 64
Q_PER_HALF = 192
Z_PER_HALF = 576
INTERNAL_FAMILY = 16
INTERNAL_RS = 144


Vector = tuple[F, ...]
VectorSpinor = tuple[Vector, ...]


def add(x: Vector, y: Vector) -> Vector:
    return tuple(a + b for a, b in zip(x, y))


def scale(c: F, x: Vector) -> Vector:
    return tuple(c * value for value in x)


def zero_spinor() -> Vector:
    return tuple(F(0) for _ in range(SPIN_TEST_DIM))


def gamma_trace(vector_spinor: VectorSpinor) -> Vector:
    """Abstract exact trace model with Gamma j_n = n I."""
    total = zero_spinor()
    for component in vector_spinor:
        total = add(total, component)
    return total


def clifford_injection(dimension: int, spinor: Vector) -> VectorSpinor:
    """Injection j_n in a faithful trace-sector model."""
    return tuple(spinor for _ in range(dimension))


def correlated_f_pair(spinor: Vector) -> tuple[VectorSpinor, VectorSpinor]:
    horizontal = tuple(
        scale(F(1, H_DIM), x) for x in clifford_injection(H_DIM, spinor)
    )
    normal = tuple(
        scale(F(-1, V_DIM), x) for x in clifford_injection(V_DIM, spinor)
    )
    return horizontal, normal


def ambient_trace(pair: tuple[VectorSpinor, VectorSpinor]) -> Vector:
    return add(gamma_trace(pair[0]), gamma_trace(pair[1]))


def contract_normal_leg(
    graph: tuple[tuple[F, ...], ...], normal_vector_spinor: VectorSpinor
) -> VectorSpinor:
    assert len(graph) == H_DIM
    assert len(normal_vector_spinor) == V_DIM
    output = []
    for row in graph:
        total = zero_spinor()
        for coefficient, component in zip(row, normal_vector_spinor):
            total = add(total, scale(coefficient, component))
        output.append(total)
    return tuple(output)


@dataclass(frozen=True)
class BridgeLedger:
    eq1222_order: tuple[str, str, str] = ("Q", "Z", "F_corr")
    source_imposter_referent: str = "F_corr"
    h210_upstream_owner: str = "Z"
    horizontal_trace_equals_source_f: bool = False
    correlated_normal_partner: str = "CONSTRUCTED_NOT_RECOVERED"
    upstream_f_projection_rank: int = 0
    carrier_adapter_status: str = "EXACT_Z_TO_F_CORR"
    source_reveal_status: str = "SEPARATE_CONDITIONAL_H210_FCORR"
    family_alignment_status: str = "SEPARATE_CONDITIONAL_H210_ALIGN"
    ps_reduction_status: str = "SEPARATE_CONDITIONAL_H210_PSRED"
    retained_ambient_halves: int = 2
    projected_ranks_are_family_counts: bool = False
    internal_144_referent: str = "Z_PARTNER_NOT_F"


LEDGER = BridgeLedger()


def source_checks(repo: Path) -> dict[str, bool]:
    register = (repo / "lab/sources/source-claim-register.yaml").read_text(
        encoding="utf-8"
    )
    extraction = (
        repo / "lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md"
    ).read_text(encoding="utf-8")
    crosswalk = (
        repo
        / "lab/active-research/joe-directed/high-energy-two-plus-one/cb3-h210-source-observation-functor-crosswalk-2026-08-16.md"
    ).read_text(encoding="utf-8")
    artifact = (
        repo
        / "lab/active-research/joe-directed/high-energy-two-plus-one/cb5-h210-source-fq-bridge-2026-08-16.md"
    ).read_text(encoding="utf-8")
    rows = (
        "SC-GEN-03",
        "SC-GEN-05",
        "SC-GEN-06",
        "SC-GEN-53",
        "SC-GEN-57",
        "SC-PRE-52",
        "SC-CHI-50",
        "SC-CHI-51",
        "SC-CHI-53",
        "SC-CHI-54",
    )
    return {
        "all controlling source rows present": all(f"id: {row}" in register for row in rows),
        "eq 12.22 imposter label is third term only": (
            'underbrace "Imposter Third Generation" is attached to the THIRD term'
            in extraction
        ),
        "source says RS remainder reveals imposter": (
            "The Spin 3/2 portion of zeta breaks down under pull back to reveal"
            in register
        ),
        "table 3 ambiguity is preserved": (
            "star notation" in extraction and "never explained in the draft" in extraction
        ),
        "crosswalk separates F from Z partner": (
            "F imposter referent" in crosswalk and "Z partner sector" in crosswalk
        ),
        "artifact carries routing classification": (
            "GU-COMPARATOR-ROUTING" in artifact
            and "BRIDGE_OR_SEMANTIC_BOUNDARY" in artifact
        ),
        "artifact names independent FCORR horn": (
            "H210-FCORR" in artifact
            and "does not discharge this horn" in artifact
        ),
    }


def audit(ledger: BridgeLedger = LEDGER) -> dict[str, bool]:
    here = Path(__file__).resolve()
    repo = here.parents[2]
    spinor = (F(2), F(-3), F(5))
    horizontal, normal = correlated_f_pair(spinor)

    # A Z-shaped toy input: normal gamma trace zero, but graph contraction has
    # nonzero horizontal trace.  Tagging the direct-sum owner as Z means its
    # canonical F projection is zero before contraction.
    z_normal = (
        spinor,
        scale(F(-1), spinor),
        *(zero_spinor() for _ in range(V_DIM - 2)),
    )
    graph = tuple(
        tuple(F(1) if (mu, a) == (0, 0) else F(0) for a in range(V_DIM))
        for mu in range(H_DIM)
    )
    observed = contract_normal_leg(graph, z_normal)
    tau = gamma_trace(observed)
    lifted = correlated_f_pair(tau)

    checks = {
        **source_checks(repo),
        "source order is Q Z F": ledger.eq1222_order == ("Q", "Z", "F_corr"),
        "source imposter referent is Fcorr": ledger.source_imposter_referent == "F_corr",
        "H210 upstream owner is Z": ledger.h210_upstream_owner == "Z",
        "per-half FQZ dimensions close": F_PER_HALF + Q_PER_HALF + Z_PER_HALF == 832,
        "ungraded FQZ dimensions close": 2 * (F_PER_HALF + Q_PER_HALF + Z_PER_HALF) == 1664,
        "F dimension is both-half 128": 2 * F_PER_HALF == 128,
        "Z dimension closes around its two-times-144 factors": 2 * Z_PER_HALF == 8 * INTERNAL_RS,
        "Gamma4 j4 equals four identity": gamma_trace(clifford_injection(H_DIM, spinor)) == scale(F(H_DIM), spinor),
        "Gamma10 j10 equals ten identity": gamma_trace(clifford_injection(V_DIM, spinor)) == scale(F(V_DIM), spinor),
        "correlated horizontal trace is tau": gamma_trace(horizontal) == spinor,
        "correlated normal trace is minus tau": gamma_trace(normal) == scale(F(-1), spinor),
        "correlated pair lies in ambient kernel": ambient_trace((horizontal, normal)) == zero_spinor(),
        "horizontal trace alone is outside ambient kernel": gamma_trace(horizontal) != zero_spinor(),
        "forced horizontal coefficient is one fourth": F(1, H_DIM) == F(1, 4),
        "forced normal coefficient is minus one tenth": F(-1, V_DIM) == F(-1, 10),
        "normal partner is constructed not recovered": ledger.correlated_normal_partner == "CONSTRUCTED_NOT_RECOVERED",
        "horizontal trace is not promoted to source F": ledger.horizontal_trace_equals_source_f is False,
        "Z toy is normal gamma traceless": gamma_trace(z_normal) == zero_spinor(),
        "tilted observation creates nonzero horizontal trace": tau == spinor and tau != zero_spinor(),
        "lifted observed trace lies in Fcorr": ambient_trace(lifted) == zero_spinor(),
        "upstream direct F projection stays zero": ledger.upstream_f_projection_rank == 0,
        "observation lift differs from upstream F projection": tau != zero_spinor() and ledger.upstream_f_projection_rank == 0,
        "carrier adapter is exact Z to Fcorr": ledger.carrier_adapter_status == "EXACT_Z_TO_F_CORR",
        "source reveal needs separate FCORR horn": ledger.source_reveal_status == "SEPARATE_CONDITIONAL_H210_FCORR",
        "family alignment remains separate": ledger.family_alignment_status == "SEPARATE_CONDITIONAL_H210_ALIGN",
        "PS reduction remains separate": ledger.ps_reduction_status == "SEPARATE_CONDITIONAL_H210_PSRED",
        "three horn roles do not collapse": len({ledger.source_reveal_status, ledger.family_alignment_status, ledger.ps_reduction_status}) == 3,
        "both ambient halves retained": ledger.retained_ambient_halves == 2,
        "projected ranks are not family counts": ledger.projected_ranks_are_family_counts is False,
        "internal 144 remains Z partner": ledger.internal_144_referent == "Z_PARTNER_NOT_F",
        "family rank kernel closes without naming family": 3 * INTERNAL_FAMILY - INTERNAL_FAMILY == 32,
        "144 minus 16 is numerical only": INTERNAL_RS - INTERNAL_FAMILY == 128 and ledger.internal_144_referent != "F",
    }
    ast.parse(here.read_text(encoding="utf-8"))
    checks["ast parse"] = True
    return checks


def planted_controls() -> dict[str, bool]:
    mutants = {
        "promote horizontal trace to source F": replace(
            LEDGER, horizontal_trace_equals_source_f=True
        ),
        "collapse H210 upstream owner from Z to F": replace(
            LEDGER, h210_upstream_owner="F_corr"
        ),
        "rename 144 as F": replace(LEDGER, internal_144_referent="F"),
        "claim normal partner was recovered": replace(
            LEDGER, correlated_normal_partner="RECOVERED_ORIGINAL_NORMAL_LEG"
        ),
        "promote H210 alignment": replace(
            LEDGER, family_alignment_status="ESTABLISHED"
        ),
        "omit FCORR source horn": replace(
            LEDGER, source_reveal_status="ESTABLISHED_FROM_EQ1222"
        ),
        "collapse FCORR and ALIGN roles": replace(
            LEDGER,
            source_reveal_status="SEPARATE_CONDITIONAL_H210_ALIGN",
        ),
        "delete conjugate half": replace(LEDGER, retained_ambient_halves=1),
        "add projected ranks as families": replace(
            LEDGER, projected_ranks_are_family_counts=True
        ),
    }
    return {name: not all(audit(mutant).values()) for name, mutant in mutants.items()}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()

    results = audit()
    failed = [name for name, passed in results.items() if not passed]
    for name, passed in results.items():
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    print(f"checks: {len(results) - len(failed)}/{len(results)}")

    if args.selftest:
        controls = planted_controls()
        for name, fired in controls.items():
            print(f"{'FIRE' if fired else 'MISS'} {name}")
        print(f"planted controls: {sum(controls.values())}/{len(controls)}")
        failed.extend(name for name, fired in controls.items() if not fired)

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
