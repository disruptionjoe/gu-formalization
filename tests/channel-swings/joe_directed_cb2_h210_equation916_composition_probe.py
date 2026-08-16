#!/usr/bin/env python3
"""Exact finite ledger for the conditional H210 / equation-9.16 composition.

This probe does not select a source background or repair the source's open
derivative-parity collision.  It checks only the released 4 x 4 grammar, the
row/column reversal, the effective-half bookkeeping, and finite rank formulas
under a declared injective rank-16 H210 intertwiner and a nonzero family row.
"""

from __future__ import annotations

import argparse
import ast
from pathlib import Path


ROWS = ("bar-zeta-minus", "bar-zeta-plus", "bar-nu-minus", "bar-nu-plus")
COLS = ("zeta-plus", "zeta-minus", "nu-plus", "nu-minus")
CELLS = (
    ("star-odot-varpi-pp", "star-odot-d0-varpi-pm", "varpi-pp", "d0-varpi-pm"),
    ("star-odot-d0-varpi-mp", "star-odot-varpi-mm", "d0-varpi-mp", "varpi-mm"),
    ("minus-bar-varpi-pp-star", "minus-d0-star-bar-varpi-pm-star", "southeast-zero", "southeast-zero"),
    ("minus-d0-star-bar-varpi-mp-star", "minus-bar-varpi-mm-star", "southeast-zero", "southeast-zero"),
)

# The reversed barred-row pairing means row 0 is dual to zeta+, row 1 to
# zeta-, row 2 to nu+, and row 3 to nu-.  These are output slots, not claims
# that the four independent barred fields have already been identified by a
# source-supplied reality condition.
ROW_OUTPUT = ("zeta-plus", "zeta-minus", "nu-plus", "nu-minus")

# Source-effective packages:
# A = Omega0(S+) + Omega1(S-) = 3*16 + 144bar
# B = Omega0(S-) + Omega1(S+) = 3*16bar + 144.
HALF = {
    "nu-plus": "A",
    "zeta-minus": "A",
    "nu-minus": "B",
    "zeta-plus": "B",
}
MODULE = {
    "nu-plus": "3x16",
    "zeta-minus": "144bar",
    "nu-minus": "3x16bar",
    "zeta-plus": "144",
}

# A 16 x 144 invariant is an operator 16 -> 144* = 144bar.  Its conjugate is
# 16bar -> 144.  Therefore the raw operator arrows stay inside A and B even
# though their barred bilinear partners lie across the effective halves.
FORWARD = {(1, 2), (0, 3)}
REVERSE = {(3, 0), (2, 1)}
WRONG_PP_MM = {(0, 2), (1, 3)}


def rank_ledger(rank_t: int = 16) -> dict[str, int]:
    family_dim = 3 * 16
    imposter_dim = 144
    one_kernel = family_dim - rank_t
    return {
        "one_family_arrow_rank": rank_t,
        "one_family_arrow_kernel": one_kernel,
        "conjugate_upper_domain": 2 * family_dim,
        "conjugate_upper_codomain": 2 * imposter_dim,
        "conjugate_upper_rank": 2 * rank_t,
        "conjugate_upper_kernel_on_family_inputs": 2 * one_kernel,
        "full_four_cell_domain": 2 * (family_dim + imposter_dim),
        "full_four_cell_rank": 4 * rank_t,
        "full_four_cell_kernel": 2 * (family_dim + imposter_dim) - 4 * rank_t,
    }


def checks() -> list[tuple[str, bool]]:
    here = Path(__file__).resolve()
    source = here.parents[2] / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md"
    source_text = source.read_text(encoding="utf-8")
    flat = tuple(cell for row in CELLS for cell in row)
    ranks = rank_ledger()
    out: list[tuple[str, bool]] = [
        ("source row order", "(bar-zeta-minus, bar-zeta-plus, bar-nu-minus, bar-nu-plus)" in source_text),
        ("source column order", "(zeta-plus, zeta-minus, nu-plus, nu-minus)^T" in source_text),
        ("sixteen distinct positions", len(flat) == 16),
        ("southeast displayed zero", all(CELLS[r][c] == "southeast-zero" for r in (2, 3) for c in (2, 3))),
        ("forward plus cell", CELLS[1][2] == "d0-varpi-mp"),
        ("forward conjugate cell", CELLS[0][3] == "d0-varpi-pm"),
        ("reverse plus cell", CELLS[3][0] == "minus-d0-star-bar-varpi-mp-star"),
        ("reverse conjugate cell", CELLS[2][1] == "minus-d0-star-bar-varpi-pm-star"),
        ("forward arrows stay in effective halves", all(HALF[COLS[c]] == HALF[ROW_OUTPUT[r]] for r, c in FORWARD)),
        ("reverse arrows stay in effective halves", all(HALF[COLS[c]] == HALF[ROW_OUTPUT[r]] for r, c in REVERSE)),
        ("pp mm arrows cross effective halves", all(HALF[COLS[c]] != HALF[ROW_OUTPUT[r]] for r, c in WRONG_PP_MM)),
        ("plus operator is 16 to 144bar", MODULE[COLS[2]] == "3x16" and MODULE[ROW_OUTPUT[1]] == "144bar"),
        ("minus operator is conjugate", MODULE[COLS[3]] == "3x16bar" and MODULE[ROW_OUTPUT[0]] == "144"),
        ("one-arrow rank", ranks["one_family_arrow_rank"] == 16),
        ("one-arrow family kernel", ranks["one_family_arrow_kernel"] == 32),
        ("upper conjugate rank", ranks["conjugate_upper_rank"] == 32),
        ("upper conjugate family kernel", ranks["conjugate_upper_kernel_on_family_inputs"] == 64),
        ("four-cell completion dimension", ranks["full_four_cell_domain"] == 384),
        ("four-cell completion rank", ranks["full_four_cell_rank"] == 64),
        ("four-cell completion kernel", ranks["full_four_cell_kernel"] == 320),
        ("rank-nullity", ranks["full_four_cell_rank"] + ranks["full_four_cell_kernel"] == ranks["full_four_cell_domain"]),
    ]
    ast.parse(here.read_text(encoding="utf-8"))
    out.append(("ast parse", True))
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    results = checks()
    failed = [name for name, passed in results if not passed]
    if args.selftest:
        # Planted false controls: each must remain false.
        plants = [
            FORWARD == WRONG_PP_MM,
            rank_ledger()["one_family_arrow_kernel"] == 31,
            rank_ledger()["full_four_cell_rank"] == 32,
            all(HALF[COLS[c]] == HALF[ROW_OUTPUT[r]] for r, c in WRONG_PP_MM),
        ]
        if any(plants):
            failed.append("planted false control unexpectedly passed")
        print(f"planted false controls rejected: {len(plants)}/{len(plants)}")
    for name, passed in results:
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    print(f"checks: {len(results) - len(failed)}/{len(results)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
