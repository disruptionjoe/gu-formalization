#!/usr/bin/env python3
"""Exact ledger certificate for the CB-3 H210 source/observation crosswalk.

This is deliberately not a field-equation or spectrum calculation.  It checks
the source-owned F/Z referents, the two non-isomorphic operations both called
"pullback" in nearby prose, and the conditional CB-1/CB-2 rank ledger.  The
H210 horn and family row are declared inputs; observation survival remains
TYPE_MISSING.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass, replace
from fractions import Fraction
from pathlib import Path


@dataclass(frozen=True)
class Crosswalk:
    eq1222_terms: tuple[str, str, str] = ("Q", "Z", "F")
    imposter_term: str = "F"
    partner_term: str = "Z"
    associated_bundle_rank: int = 14
    differential_pullback_rank: int = 4
    normal_rank: int = 10
    retain_conjugate_port: bool = True
    family_row_status: str = "declared-not-source-selected"
    alignment_status: str = "TYPE_MISSING"
    observation_status: str = "TYPE_MISSING"
    arrow_a: tuple[str, str] = ("16", "144bar")
    arrow_b: tuple[str, str] = ("16bar", "144")


LEDGER = Crosswalk()

# Draft dimensions under its own grading convention.
F_GRADED = 64
F_UNGRADED = 128
Z_GRADED = 576
Z_UNGRADED = 1152
INTERNAL_FAMILY = 16
INTERNAL_RS = 144
TABLE3_NAMED_SHAPE = (6, 3, 3, 2, 1, 1)


def rank_exact(matrix: list[list[int]]) -> int:
    """Gaussian rank over Q, with no floating point."""
    a = [[Fraction(x) for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((i for i in range(rank, rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = a[rank][col]
        a[rank] = [x / scale for x in a[rank]]
        for i in range(rows):
            if i != rank and a[i][col]:
                factor = a[i][col]
                a[i] = [x - factor * y for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


def graph_pullback_matrix(k: list[list[int]]) -> list[list[int]]:
    """Matrix of ds^*: H^* + N^* -> T^*X for ds=(I,K)."""
    return [
        [int(mu == nu) for nu in range(4)] + k[mu]
        for mu in range(4)
    ]


def pull_covector(k: list[list[int]], covector: list[int]) -> list[int]:
    assert len(covector) == 14
    return [
        covector[mu]
        + sum(k[mu][a] * covector[4 + a] for a in range(10))
        for mu in range(4)
    ]


def source_checks(repo: Path) -> dict[str, bool]:
    register = (repo / "lab/sources/source-claim-register.yaml").read_text(encoding="utf-8")
    extraction = (
        repo / "lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md"
    ).read_text(encoding="utf-8")
    decider = (repo / "explorations/draft-fqz-map-decider-2026-08-03.md").read_text(
        encoding="utf-8"
    )
    he1 = (
        repo
        / "lab/active-research/joe-directed/high-energy-two-plus-one/he1-imposter-separation-invariant-2026-08-14.md"
    ).read_text(encoding="utf-8")
    return {
        "all controlling source rows present": all(
            f"id: {row}" in register
            for row in ("SC-GEN-03", "SC-GEN-05", "SC-GEN-06", "SC-GEN-53", "SC-PRE-52")
        ),
        "eq 12.22 label is third term only": (
            'underbrace "Imposter Third Generation" is attached to the THIRD term'
            in extraction
        ),
        "table 3 host remains ambiguous": "star notation" in extraction
        and "never explained in the draft" in extraction,
        "fqz decider maps F and Z distinctly": (
            "F maps to S(V)⊗S(W)" in decider
            and "Z is 2⊗144-shaped = S(V)⊗RS(W)" in decider
        ),
        "he1 forbids renaming 144 as imposter": "Nothing here renames the imposter." in he1,
        "source predicts third-family 144 combination": (
            "third generation will combine" in " ".join(register.split())
            and "Pati-Salam-level unification" in " ".join(register.split())
        ),
    }


def audit(ledger: Crosswalk = LEDGER) -> dict[str, bool]:
    here = Path(__file__).resolve()
    repo = here.parents[2]
    k = [[0] * 10 for _ in range(4)]
    for mu, value in enumerate((2, -1, 3, 1)):
        k[mu][mu] = value
    flat = [[0] * 10 for _ in range(4)]
    pure_normal = [0] * 14
    pure_normal[4] = 1

    family_domain = 3 * INTERNAL_FAMILY
    h210_rank = INTERNAL_FAMILY
    checks = {
        **source_checks(repo),
        "eq 12.22 order is Q Z F": ledger.eq1222_terms == ("Q", "Z", "F"),
        "F alone is imposter referent": (
            ledger.imposter_term == "F"
            and ledger.partner_term == "Z"
            and ledger.imposter_term != ledger.partner_term
            and ledger.eq1222_terms[-1] == ledger.imposter_term
        ),
        "F dimensions close": 2 * F_GRADED == F_UNGRADED == 128,
        "Z dimensions close around internal 144": (
            2 * Z_GRADED == Z_UNGRADED == 4 * 2 * INTERNAL_RS
        ),
        "table 3 named shape is one internal family": sum(TABLE3_NAMED_SHAPE) == INTERNAL_FAMILY,
        "128 residual is only numerical homonym": INTERNAL_RS - sum(TABLE3_NAMED_SHAPE) == 128,
        "associated restriction retains H plus N": (
            ledger.associated_bundle_rank == ledger.differential_pullback_rank + ledger.normal_rank
            and ledger.associated_bundle_rank == 14
        ),
        "differential pullback has rank four": (
            ledger.differential_pullback_rank == 4
            and rank_exact(graph_pullback_matrix(k)) == 4
        ),
        "nonflat graph contracts a normal covector": pull_covector(k, pure_normal) == [2, 0, 0, 0],
        "flat graph kills that normal covector": pull_covector(flat, pure_normal) == [0, 0, 0, 0],
        "two pullbacks are not identified": ledger.associated_bundle_rank != ledger.differential_pullback_rank,
        "H210 ports are conjugate pair": (
            ledger.arrow_a == ("16", "144bar")
            and ledger.arrow_b == ("16bar", "144")
            and ledger.retain_conjugate_port
        ),
        "conditional family rank packet closes": (
            h210_rank == 16
            and family_domain - h210_rank == 32
            and h210_rank + (family_domain - h210_rank) == family_domain
        ),
        "family row is not promoted": ledger.family_row_status == "declared-not-source-selected",
        "H210 alignment horn is not promoted": ledger.alignment_status == "TYPE_MISSING",
        "observation survival is not promoted": ledger.observation_status == "TYPE_MISSING",
    }
    ast.parse(here.read_text(encoding="utf-8"))
    checks["ast parse"] = True
    return checks


def planted_controls() -> dict[str, bool]:
    """Each mutant must make the ledger audit fail somewhere."""
    mutants = {
        "rename whole 144 as imposter": replace(LEDGER, imposter_term="Z"),
        "move eq 12.22 label to Z": replace(LEDGER, eq1222_terms=("Q", "F", "Z")),
        "collapse associated restriction to rank four": replace(LEDGER, associated_bundle_rank=4),
        "delete conjugate half": replace(LEDGER, retain_conjugate_port=False),
        "promote declared family row to source-selected": replace(LEDGER, family_row_status="source-selected"),
        "promote H210 alignment": replace(LEDGER, alignment_status="ESTABLISHED"),
        "promote observation survival": replace(LEDGER, observation_status="ESTABLISHED"),
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
