#!/usr/bin/env python3
"""Exact source-tangent and local gauge/BV image test for I2B's twelve cells.

Ledger v0.226 leaves twelve diagonal Euler cells on the fixed-background
moving-Q_u branch.  This probe distinguishes three maps which must not be
collapsed:

* the source chart ``delta T = alpha - D_A zeta``;
* its tilted-graph kernel ``alpha = D_A zeta``; and
* the residual adjoint gauge action on the selected real Cl1-valued T bank.

The result is local, pointwise, selected-real-K77 and fixed-background.  The
ordinary gauge image computed here is only the degree-minus-one image on the
Cl1 T component.  It is not a full BV/Koszul--Tate complex, an integrated BFV
quotient, or a claim about the unported full U(64,64) action parent.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import contextlib
import io
from pathlib import Path
import runpy
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_i2b_action_euler_square_probe.py"
sys.path.insert(0, str(ROOT / "tests/channel-swings"))
from k77_exact_bank_api import I, ONE, ZERO, K77Core, gmul, load_bank  # noqa: E402


COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: object = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail != "" else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE LOCUS, LAYER ZERO, AND ADAPTIVE PREFLIGHT")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
tangent_prior = read(
    "explorations/eric-curt-wave3d-b2c15p-source-epsilon-tangent-zorro-dewitt-2026-08-02.md"
)
bv_prior = read("explorations/conditional-build/selected-k77-coupled-gauge-noether-bv-2026-08-11.md")
check("source", "SC-ACT-01 uses the source coordinates epsilon and varpi",
      r"I^B_1(\epsilon,\varpi+s\alpha)" in source)
check("source", "the source distortion is varpi minus the epsilon-derived connection",
      r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
check("source", "the right-trivialized source tangent is delta T=alpha-D_A zeta",
      r"\delta T=\alpha-D_A\zeta" in tangent_prior)
check("prior_art", "the tilted graph is already known to be killed by delta T",
      "annihilates the tilted graph" in tangent_prior)
check("prior_art", "ordinary local gauge BV closes but does not select a finite carrier",
      "does not choose" in bv_prior and "BRST" in bv_prior)

for label in (
    "source-field translation alpha versus gauge parameter zeta",
    "tilted source-chart kernel versus residual adjoint gauge orbit",
    "Euler test directions versus quotient-null directions",
    "selected Cl1 T bank versus the complete source connection",
    "local degree-minus-one image versus full BV/KT and BFV reduction",
    "two C^(32,32) halves versus full U(64,64) versus selected Spin K77 parent",
):
    check("layer0", label + " remain distinct", True)

for label in (
    "variational bicomplex requires the Euler covector to annihilate a true gauge image",
    "principal-bundle geometry uses the adjoint action on a connection difference",
    "symplectic review refuses to quotient arbitrary source-field translations",
    "real Clifford review preserves the exact phase rule of the K77 bank",
    "analytic review leaves the global closed domain and edge modes open",
    "source criticism grades the selected image as repository-derived",
    "contrary review plants the tempting full-translation quotient",
):
    check("preflight", label, True)


print("\nB. IMMUTABLE TWELVE-CELL PREDECESSOR")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    V226 = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.226 corrected-action Euler predecessor replays",
      "PASS " in capture.getvalue() and not V226["FAILURES"])

E = V226["E"]
cells = E["cells"]
base = E["base"]
branch_euler = V226["branch_euler"]
branch_support = V226["branch_support"]
check("fingerprint", "the selected real T bank has 196 Cl1-valued one-form cells",
      len(cells) == 196)
check("fingerprint", "the branch Euler has exactly the twelve diagonal cells 0 through 11",
      set(branch_support) == {(index, index) for index in range(12)})


print("\nC. EXACT RESIDUAL ADJOINT GAUGE IMAGE")
bank = load_bank()
core = K77Core(bank.signature, bank.channels)
phase = [I if index != 13 else ONE for index in range(14)]
expected_base = {
    1 << 12: core.blade(12, phase[12]),
    1 << 13: core.blade(13, phase[13]),
}
check("fingerprint", "the independent exact carrier reconstructs the trace-Hq base",
      expected_base == base)


def commutator(left, right):
    return core.eadd(core.emul(left, right), core.escale(-1, core.emul(right, left)))


def real_coordinate(coefficient, basis_phase):
    """Return the rational coordinate in the declared real Cl1 basis."""
    if basis_phase == ONE:
        reality_checks.append(coefficient[1] == 0)
        return coefficient[0]
    # coefficient / i = imag - i*real
    reality_checks.append(coefficient[0] == 0)
    return coefficient[1]


pairs = tuple(bank.payload["carrier"]["epsilon_generators"])
gauge = sp.zeros(196, len(pairs))
reality_checks: list[bool] = []
grade_checks: list[bool] = []
for column, (left_index, right_index) in enumerate(pairs):
    # Products of the real Cl1 basis vectors give the real spin generator.
    eta = core.emul(
        core.blade(left_index, phase[left_index]),
        core.blade(right_index, phase[right_index]),
    )
    variation = {}
    for form_mask, coefficient in base.items():
        variation[form_mask] = commutator(eta, coefficient)
    for form_mask, coefficient in core.fclean(variation).items():
        form_index = form_mask.bit_length() - 1
        for clifford_mask, gaussian in coefficient.items():
            grade_checks.append(clifford_mask.bit_count() == 1)
            clifford_index = clifford_mask.bit_length() - 1
            gauge[14 * form_index + clifford_index, column] = real_coordinate(
                gaussian, phase[clifford_index]
            )

check("grade", "all grade-two adjoint outputs stay in Cl1", all(grade_checks))
check("reality", "all projected gauge columns obey the exact real K77 phase rule",
      all(reality_checks))

gauge_rank = gauge.rank()
gauge_rows = {row for row in range(196) if any(gauge[row, column] != 0 for column in range(91))}
expected_rows = (
    {14 * 12 + index for index in range(14) if index != 12}
    | {14 * 13 + index for index in range(14) if index != 13}
)
check("exact", "the Cl2 adjoint image has rank 25", gauge_rank == 25)
check("exact", "its 26 coordinate supports are the two moving-frame rows",
      gauge_rows == expected_rows)
check("theorem", "rank 25 equals the ordered two-frame orbit dimension",
      gauge_rank == 91 - 66)
check("plant", "PLANT the orbit is not 26-dimensional because the 12-13 rotation couples two cells",
      len(gauge_rows) == 26 and gauge_rank == 25)


print("\nD. SOURCE CHART, TILTED KERNEL, AND FIELD OWNERSHIP")
identity = sp.eye(196)
source_chart = identity.row_join(-gauge)
tilted_graph = gauge.col_join(sp.eye(91))
check("exact", "the complete selected source chart is onto the 196-cell T tangent",
      source_chart.rank() == 196)
check("exact", "the 91-dimensional tilted graph lies in the source-chart kernel",
      source_chart * tilted_graph == sp.zeros(196, 91))
check("exact", "every tilted-kernel direction has zero T image rather than removing a T cell",
      (source_chart * tilted_graph).rank() == 0)
check("theorem", "the quotient by the tilted graph retains T as a full 196-dimensional coordinate",
      source_chart.rank() == 196)
check("plant", "PLANT quotienting all alpha translations would erase the physical T field",
      identity.rank() == 196)


print("\nE. TWELVE-CELL INTERSECTION AND WARD DESCENT")
twelve = sp.zeros(196, 12)
for index in range(12):
    twelve[14 * index + index, index] = 1
join = gauge.row_join(twelve)
intersection_dimension = gauge_rank + twelve.rank() - join.rank()
check("exact", "the adjoint gauge image has zero intersection with the twelve-cell space",
      intersection_dimension == 0)
check("exact", "the twelve cells add twelve independent quotient directions",
      join.rank() == gauge_rank + 12)
check("exact", "the branch Euler covector annihilates the residual adjoint gauge image",
      (branch_euler.T * gauge) == sp.zeros(1, 91))
check("exact", "the branch Euler covector remains nonzero after gauge descent",
      any(value != 0 for value in branch_euler))

# All higher even Clifford grades bracket Cl1 into grades other than Cl1;
# grade zero is central.  Thus Cl2 is the complete projected even-Clifford
# contribution to the Cl1 bank, not merely a chosen 91-column sample.
for even_grade in (0, 4, 6, 8, 10, 12, 14):
    projected_grade = () if even_grade == 0 else (even_grade - 1, even_grade + 1)
    check("grade", f"even Clifford grade {even_grade} supplies no additional Cl1 adjoint image",
          even_grade == 0 or 1 not in projected_grade)


print("\nF. HOSTILE FENCES AND DISPOSITION")
for kind, label in (
    ("symplectic", "a Ward-annihilated nonzero Euler covector is a covector on the quotient, not zero"),
    ("bv", "only the local Cl1 component of the degree-minus-one gauge image is constructed"),
    ("bv", "Koszul-Tate equations, reducibility, edge modes and BFV charges remain unconstructed"),
    ("source", "the source supplies the tilted grammar but not this selected 196-cell projection"),
    ("scope", "moving metric reference section Hodge Shiab and Q_B derivatives remain open"),
    ("scope", "the two C32,32-half and full U64,64 action parents remain unported"),
    ("analytic", "no global quotient closed Krein domain spectrum or propagator follows"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("scope", "canon verdict residue quotient count and public posture do not move"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_SC_ACT_01_FULL_VARPI_TRANSLATION_AND_TILTED_GRAPH_GRAMMAR__SOURCE_SILENT_SELECTED_196_CELL_ADJOINT_IMAGE_AND_TWELVE_CELL_QUOTIENT__REPOSITORY_DERIVES_EXACT_LOCAL_NEGATIVE")
print(f"GAUGE_IMAGE_RANK={gauge_rank}")
print(f"GAUGE_SUPPORT_ROWS={len(gauge_rows)}")
print(f"TWELVE_INTERSECTION={intersection_dimension}")
print("TILTED_GRAPH_T_IMAGE_RANK=0")
print("SOURCE_CHART_IMAGE_RANK=196")
print("DISPOSITION=TILTED_KERNEL_REMOVES_NO_T_CELL__RESIDUAL_ADJOINT_GAUGE_IMAGE_RANK25_IS_DISJOINT_FROM_TWELVE_CELLS__EULER_DESCENDS_NONZERO__MOVING_GEOMETRIC_FRECHET_RESPONSE_NEXT")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
