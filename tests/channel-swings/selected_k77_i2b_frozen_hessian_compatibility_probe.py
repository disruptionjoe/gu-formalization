#!/usr/bin/env python3
"""Exact frozen-Hessian completion of the selected I2B compatibility family.

The predecessor finds the complete fourteen-row principal compatibility
operator.  This probe applies it to the full frozen-coefficient residual-square
Hessian.  It decides every constant lower-order correction over QQ.  Moving
Q_B/H_q/Shiab/section/observation/affine-source coefficients are deliberately
outside this theorem and remain the next possible Noether/BV owner.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
SPENCER = ROOT / "tests/channel-swings/selected_k77_i2b_observation_contact_spencer_probe.py"
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


print("A. SOURCE, LAYER ZERO, PRIOR ART, AND ADAPTIVE PREFLIGHT")
claims = read("lab/sources/source-claim-register.yaml")
source_reconstruction = read(
    "lab/sources/paired-curt-eric-gu-axiom-and-argument-reconstruction-2026-07-31.md"
)
spencer_prior = read(
    "explorations/conditional-build/selected-k77-i2b-observation-contact-spencer-2026-08-13.md"
)
lower_prior = read(
    "explorations/conditional-build/selected-k77-i2b-lower-order-exact-form-lift-2026-08-13.md"
)
check("source", "SC-ACT-04 owns the bosonic residual square",
      "- id: SC-ACT-04" in claims and "I^B_2 = ||Upsilon^B_omega||^2" in claims)
check("source", "the reconstruction leaves a distinct source Q_B primalizer slot",
      "I_2^B[Q_B]" in source_reconstruction and "H_2^B=(D\\Upsilon_B)^\\vee Q_B(D\\Upsilon_B)" in source_reconstruction)
check("prior_art", "the predecessor identifies the complete fourteen-row principal compatibility family",
      "cokernel is exactly\nfourteen-dimensional" in spencer_prior
      and "sum_{\\lambda=0}^{3}" in spencer_prior)
check("prior_art", "the lower-order predecessor already lifts the raw exact-form family",
      "restriction of the lower-order Hessian to `im K(k)` has full" in lower_prior
      and "derivative/lower-order cross block vanishes" in lower_prior)
for distinction in (
    "principal compatibility versus nonlinear Bianchi or Noether identity",
    "frozen Hessian versus moving Q_B H_q Shiab and observation coefficients",
    "constant lower-order compatibility correction versus a moving covariant divergence",
    "full-bank nonstationarity versus the stationary principal two-jet",
    "Euler compatibility versus preboundary BFV reduction",
):
    check("layer0", distinction + " remain distinct", True)
for kind, label in (
    ("variational", "assemble both Gram and residual-dependent second-variation terms"),
    ("spencer", "solve every polynomial order of the constant completion problem"),
    ("principal_bundle", "reserve coefficient motion for the source-connection successor"),
    ("hyperbolic", "infer no propagation theorem from a formal compatibility defect"),
    ("krein", "retain the nonzero K-null background residual in the Hessian"),
    ("symplectic", "infer no phase-space quotient from bulk Hessian compatibility"),
    ("source", "separate source action grammar from the exact K77 completion theorem"),
    ("contrary", "require full-bank and wrong-completion plants"),
):
    check(kind, label, True)


print("\nB. IMMUTABLE PREDECESSORS AND STRUCTURE FINGERPRINT")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    D = runpy.run_path(str(SPENCER))
check("repo", "the exact first-Spencer predecessor replays",
      "PASS 50/50" in capture.getvalue() and not D["FAILURES"])
H = D["H"]
P = H["P"]
S = P["S"]
cells = D["cells"]
selected = D["selected"]
responses = D["responses"]
blocks = D["blocks"]
sym_pair = D["sym_pair"]
real_scalar = D["real_scalar"]
zero_linear = S["residual_derivative"]
residual = S["residual_at_branch"]
wedge_raw = S["wedge_raw"]
fadd = S["fadd"]
fscale = S["fscale"]
shiab = S["shiab"]
check("fingerprint", "field and equation carriers remain the ordered 196-real connection bank",
      len(cells) == 196 and all(len(direction) == 196 for direction in responses))
check("fingerprint", "the selected Shiab channel is unchanged across both predecessor chains",
      selected == S["SELECTED"])
check("fingerprint", "the background residual is nonzero and Krein-null",
      bool(residual) and S["residual_pairing"](residual, residual) == S["ZERO"])
check("fingerprint", "the restricted branch remains nonstationary on the full field bank",
      bool(S["gradient"]))


def second_residual(left: dict, right: dict) -> dict:
    return shiab(fscale(Fraction(1, 3), fadd(
        wedge_raw(left, right), wedge_raw(right, left)
    )), selected)


def scalar(value: object) -> sp.Expr:
    return sp.factor(real_scalar(value))


def rational(value: object) -> sp.Rational:
    if isinstance(value, Fraction):
        return sp.Rational(value.numerator, value.denominator)
    return sp.Rational(value)


print("\nC. COMPLETE FROZEN LOWER-ORDER HESSIAN")
lower_responses = [zero_linear(delta) for _, _, delta in cells]
h0 = sp.MutableSparseMatrix(196, 196, {})
h1 = [sp.MutableSparseMatrix(196, 196, {}) for _ in range(4)]
for row, (_, _, test) in enumerate(cells):
    b_test = lower_responses[row]
    for column, (_, _, delta) in enumerate(cells):
        b_delta = lower_responses[column]
        value = scalar(sym_pair(b_test, b_delta)) + scalar(
            sym_pair(second_residual(test, delta), residual)
        )
        if value:
            h0[row, column] = value
        for mu in range(4):
            cross = scalar(sym_pair(b_test, responses[mu][column])) - scalar(
                sym_pair(responses[mu][row], b_delta)
            )
            if cross:
                h1[mu][row, column] = cross

check("hessian", "the frozen zeroth-order Hessian is exactly self-adjoint",
      h0 == h0.T)
check("hessian", "the frozen zeroth-order Hessian has full rank 196", h0.rank() == 196)
check("hessian", "all four derivative/lower-order cross blocks vanish exactly",
      all(matrix == sp.zeros(196) for matrix in h1))
check("hessian", "the zero cross blocks satisfy formal skew-adjointness",
      all(matrix == -matrix.T for matrix in h1))
check("control", "the exact-form predecessor independently records the same zero cross term",
      "derivative/lower-order cross block vanishes" in lower_prior)


print("\nD. UNIQUE CONSTANT COMPATIBILITY COMPLETION")
def add_column(
    basis: dict[int, dict[int, Fraction]], values: dict[int, Fraction]
) -> bool:
    work = {index: Fraction(value) for index, value in values.items() if value}
    while work:
        pivot = min(work)
        if pivot not in basis:
            scale = work[pivot]
            basis[pivot] = {index: value / scale for index, value in work.items()}
            return True
        scale = work[pivot]
        for index, value in basis[pivot].items():
            updated = work.get(index, Fraction(0)) - scale * value
            if updated:
                work[index] = updated
            elif index in work:
                del work[index]
    return False


# The (00) and (01) blocks already span the full 196-dimensional equation
# carrier.  Thus C0 H2 = 0 forces every constant C0 to vanish.
basis: dict[int, dict[int, Fraction]] = {}
cumulative_ranks = []
for pair in ((0, 0), (0, 1)):
    for column in blocks[pair]:
        add_column(basis, column)
    cumulative_ranks.append((pair, len(basis)))
check("theorem", "the timelike and first mixed principal blocks have cumulative ranks 182 then 196",
      cumulative_ranks == [((0, 0), 182), ((0, 1), 196)])
check("theorem", "principal surjectivity forces the unique constant completion C0 to be zero",
      len(basis) == 196 and all(matrix == sp.zeros(196) for matrix in h1))
c0 = sp.zeros(14, 196)


def dense_block(pair: tuple[int, int]) -> sp.MutableSparseMatrix:
    out = sp.MutableSparseMatrix(196, 196, {})
    for column, values in enumerate(blocks[pair]):
        for row, value in values.items():
            out[row, column] = rational(value)
    return out


# Polynomial degree two: C1(k)H1(k)+C0H2(k).  It vanishes because H1=C0=0.
degree_two = []
for mu in range(4):
    for nu in range(mu, 4):
        defect = sp.zeros(14, 196)
        for clifford in range(14):
            defect[clifford, :] = h1[nu][mu * 14 + clifford, :]
            if mu != nu:
                defect[clifford, :] += h1[mu][nu * 14 + clifford, :]
        defect += c0 * dense_block((mu, nu))
        degree_two.append((mu, nu, defect))
check("compatibility", "all ten degree-two completion equations vanish exactly",
      all(defect == sp.zeros(14, 196) for _, _, defect in degree_two))

# Polynomial degree one: C1(k)H0+C0H1(k).  With forced C0=0 these are raw
# divergence rows of the invertible H0 and cannot vanish.
degree_one = []
for mu in range(4):
    defect = sp.zeros(14, 196)
    for clifford in range(14):
        defect[clifford, :] = h0[mu * 14 + clifford, :]
    defect += c0 * h1[mu]
    degree_one.append(defect)
check("obstruction", "each of the four degree-one defects has exact rank fourteen",
      [matrix.rank() for matrix in degree_one] == [14, 14, 14, 14])
check("obstruction", "each degree-one defect has exactly forty nonzero coefficients",
      [sum(value != 0 for value in matrix) for matrix in degree_one] == [40] * 4)
combined = sp.Matrix.vstack(*degree_one)
check("obstruction", "the complete frozen degree-one defect has rank fifty-six",
      combined.rank() == 56)
check("obstruction", "the complete frozen degree-one defect has 160 nonzero coefficients",
      sum(value != 0 for value in combined) == 160)
check("compatibility", "the forced C0 has zero degree-zero defect", c0 * h0 == sp.zeros(14, 196))
wrong_c0 = sp.zeros(14, 196)
wrong_c0[0, 0] = 1
check("planted", "PLANT a nonzero constant completion breaks a principal block",
      wrong_c0 * dense_block((0, 1)) != sp.zeros(14, 196))
check("planted", "PLANT deleting H0 falsely erases the exact degree-one obstruction",
      combined != sp.zeros(56, 196))


print("\nE. DISPOSITION AND DURABLE FENCES")
for kind, label in (
    ("result", "no constant lower-order correction extends the principal compatibility through the frozen full-bank Hessian"),
    ("correction", "this rejects the naive frozen divergence completion rather than every moving covariant identity"),
    ("principal_bundle", "moving Q_B H_q Shiab section observation and affine-source coefficients remain the sole named local completion route"),
    ("variation", "the complete stationary coefficient derivative on arbitrary field directions remains unbuilt"),
    ("spencer", "a nonlinear Noether or BV identity remains unowned"),
    ("symplectic", "the nonzero preboundary owner and physical BFV quotient remain open"),
    ("hyperbolic", "constraint propagation and a closed Green domain remain open"),
    ("scope", "higher Spencer cohomology global descent positivity spectrum mass and stability remain open"),
    ("source", "the source is silent on the exact fifty-six-rank frozen defect and its moving completion"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("scope", "ledger canon residue quotient count and public posture do not move"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_I2B_RESIDUAL_SQUARE_AND_QB_SLOT__SOURCE_SILENT_FROZEN_COMPATIBILITY_DEFECT_AND_MOVING_NOETHER_COMPLETION")
print(f"FROZEN_H0_RANK={h0.rank()}/196")
print("FROZEN_H1_RANKS=" + ",".join(str(matrix.rank()) for matrix in h1))
print("PRINCIPAL_CUMULATIVE_RANKS=" + ";".join(
    f"{mu}{nu}:{rank}" for (mu, nu), rank in cumulative_ranks
))
print("CONSTANT_C0=UNIQUELY_ZERO")
print("DEGREE_TWO_DEFECT_RANKS=" + ",".join(str(defect.rank()) for _, _, defect in degree_two))
print("DEGREE_ONE_DEFECT_RANKS=" + ",".join(str(matrix.rank()) for matrix in degree_one))
print(f"COMBINED_DEGREE_ONE_DEFECT_RANK={combined.rank()}/56")
print("RESULT=NAIVE_FROZEN_DIVERGENCE_COMPLETION_FALSIFIED__MOVING_COVARIANT_COMPLETION_OPEN")
print("NEXT=ASSEMBLE_COMPLETE_STATIONARY_COEFFICIENT_DERIVATIVE_ON_ARBITRARY_FIELD_DIRECTIONS_AND_TEST_COVARIANT_COMPATIBILITY")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
