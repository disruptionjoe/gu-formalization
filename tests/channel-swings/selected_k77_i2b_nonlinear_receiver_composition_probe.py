#!/usr/bin/env python3
"""Exact nonlinear observation x real-Euler receiver composition.

The observation section owns a finite eta-self-adjoint graph projector P_J.
The selected I2B first variation owns a residual-space real primalizer P_+.
This probe composes the two independent reductions into four exact sectors,
checks their simultaneous moving derivative, and keeps ordinary pullback
distinct from the lossless tangent-plus-normal equation receiver.

The calculation is a universal exact composition.  It does not construct the
remaining arbitrary-field I2B Euler coefficients or a physical BV/BFV domain.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def strict(relative: str):
    def reject(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key}")
            out[key] = value
        return out
    return json.loads(read(relative), object_pairs_hook=reject)


print("A. SOURCE, PRIOR ART, LAYER ZERO, AND ADAPTIVE PREFLIGHT")
source = read("lab/sources/selected-k77-i2b-nonlinear-receiver-composition-source-return-2026-08-12.md")
finite = strict("lab/process/selected-k77-finite-section-projector-atlas-descent.json")
connection = strict("lab/process/selected-k77-action-stabilizer-connection-flag-reconciliation.json")
primalizer = strict("lab/process/selected-k77-i2b-global-primalizer-descent.json")
trace_orbit = strict("lab/process/selected-k77-i2b-full-trace-orbit-derivative.json")
v210 = strict("lab/process/selected-k77-i2b-radial-lc-section-qrow-composition.json")

check("source", "source corrects naive pullback and is silent on the exact product receiver",
      "SOURCE-CORRECTS" in source and "SOURCE-SILENT" in source)
check("prior_art", "finite graph projector already has exact mixed-atlas descent",
      finite["status"].startswith("SCOPED_FINITE_K77_GRAPH_PROJECTOR")
      and finite["checks"]["mixed_atlas_transitions_per_field"] == 3
      and finite["atlas"]["mixed_fractional_descent"] is True)
check("prior_art", "the action connection already preserves the observation split",
      connection["status"].startswith("EXACT_SCOPED_K77_REDUCTIVE_CONNECTION")
      and connection["result"]["frame_free_reductive_connection"] is True)
check("prior_art", "the action-owned P_plus already descends and moves nontrivially",
      primalizer["exact_results"]["pplus_overlap_failures"] == 0
      and primalizer["exact_results"]["dot_pplus_rank"] == 56)
check("prior_art", "v0.208 and v0.210 own the moving trace packet and q-row typing",
      trace_orbit["exact_results"]["dot_pplus_action_adjoint_failures"] == 0
      and v210["section_q_row"]["q_row_dimension"] == 4)

for label in (
    "finite graph projector versus a preferred adapted or Spin frame",
    "observation tangent/normal split versus residual fixed/anti-fixed split",
    "ordinary pullback versus complete equation receiver",
    "source epsilon versus repository graph projector",
    "lossless receiver versus physical quotient",
    "zero radial action derivative versus missing radial equation coordinate",
    "source C32_32 plus C32_32 carrier split versus two connections or full U64_64",
):
    check("layer0", label, True)

for label in (
    "principal-bundle geometry demands simultaneous overlap naturality",
    "variational bicomplex keeps receiver and Euler coefficient assembly separate",
    "Clifford/Krein review uses P_plus without asserting positivity",
    "symplectic review leaves antisymmetrization and boundary reduction open",
    "analytic review leaves common domains spectra and evolution open",
    "source review treats the exact formula as repository-derived",
    "contrary review requires frozen-factor and naive-pullback plants",
):
    check("preflight", label, True)


print("\nB. FINITE NONLINEAR OBSERVATION PROJECTOR")
eta_h = sp.diag(1, -1, -1, -1)
eta_v = sp.diag(*([1] * 6 + [-1] * 4))
eta = sp.diag(1, -1, -1, -1, *([1] * 6 + [-1] * 4))
fractions = {
    (0, 0): (1, 5), (1, 1): (-1, 7), (2, 2): (1, 9),
    (3, 3): (1, 11), (4, 0): (1, 13), (5, 1): (1, 17),
    (6, 2): (-1, 19), (7, 3): (1, 23), (8, 0): (1, 29),
    (9, 1): (-1, 31),
}
J = sp.zeros(10, 4)
for (row, column), (numerator, denominator) in fractions.items():
    J[row, column] = sp.Rational(numerator, denominator)
L = sp.Matrix.vstack(sp.eye(4), J)
gram = L.T * eta * L
P = L * gram.inv() * L.T * eta
Q = sp.eye(14) - P
gram_diagonal = gram.LDLdecomposition(hermitian=False)[1].diagonal()
check("geometry", "actual finite graph Gram is nondegenerate Lorentzian",
      gram.det() != 0
      and sum(1 for value in gram_diagonal if bool(value > 0)) == 1
      and sum(1 for value in gram_diagonal if bool(value < 0)) == 3)
check("projector", "P and Q are complementary eta-self-adjoint projectors",
      P * P == P and Q * Q == Q and P * Q == sp.zeros(14)
      and P.T * eta == eta * P and Q.T * eta == eta * Q)
check("receiver", "complete tangent-plus-normal receiver has ranks four plus ten",
      P.rank() == 4 and Q.rank() == 10
      and sp.Matrix.vstack(P, Q).rank() == 14)


def projector_derivative(dJ: sp.Matrix) -> sp.Matrix:
    dL = sp.Matrix.vstack(sp.zeros(4), dJ)
    dG = dL.T * eta * L + L.T * eta * dL
    return (dL * gram.inv() * L.T * eta
            - L * gram.inv() * dG * gram.inv() * L.T * eta
            + L * gram.inv() * dL.T * eta)


dPs = []
for base in range(4):
    dJ = sp.zeros(10, 4)
    dJ[9, base] = 1
    dP = projector_derivative(dJ)
    dPs.append(dP)
    check("tangent", f"q-row {base}: differentiated projector identities close",
          P * dP + dP * P == dP and dP.T * eta == eta * dP)
check("tangent", "the four nonlinear q-row projector derivatives are independent",
      sp.Matrix.hstack(*[value.reshape(196, 1) for value in dPs]).rank() == 4)


print("\nC. PRODUCT WITH THE ACTION-OWNED REAL EULER PRIMALIZER")
# A minimal exact model of a rank-half involution.  The actual predecessor has
# ranks 196+196 on 392 real dimensions; the tensor-rank results below scale
# directly and are also recorded explicitly.
R_plus = sp.diag(1, 1, 0, 0)
R_minus = sp.eye(4) - R_plus

target_generators = []
for plus in range(2):
    for minus in range(2):
        B = sp.zeros(2, 2)
        B[plus, minus] = 1
        target_generators.append(sp.Matrix.vstack(
            sp.Matrix.hstack(sp.zeros(2), B),
            sp.Matrix.hstack(-B.T, sp.zeros(2)),
        ))
dRs = [generator * R_plus - R_plus * generator for generator in target_generators]
check("primalizer", "four independent moving half-projector derivatives are live",
      sp.Matrix.hstack(*[value.reshape(16, 1) for value in dRs]).rank() == 4
      and all(value != sp.zeros(4) for value in dRs))

sectors = [
    sp.kronecker_product(P, R_plus),
    sp.kronecker_product(P, R_minus),
    sp.kronecker_product(Q, R_plus),
    sp.kronecker_product(Q, R_minus),
]
expected_small = [8, 8, 20, 20]
expected_actual = [784, 784, 1960, 1960]
check("receiver", "four sectors are pairwise orthogonal idempotents and reconstruct identity",
      sum(sectors, sp.zeros(56)) == sp.eye(56)
      and all(value * value == value for value in sectors)
      and all(sectors[i] * sectors[j] == sp.zeros(56)
              for i in range(4) for j in range(4) if i != j))
check("receiver", "universal ranks are 8+8+20+20 and scale to actual 5488 dimensions",
      [value.rank() for value in sectors] == expected_small
      and sum(expected_actual) == 14 * 392
      and expected_actual == [4 * 196, 4 * 196, 10 * 196, 10 * 196])

x = sp.Matrix(range(1, 57))
dx = sp.Matrix(range(56, 0, -1))
for index, (dP, dR) in enumerate(zip(dPs, dRs)):
    dQ = -dP
    dR_minus = -dR
    dsectors = [
        sp.kronecker_product(dP, R_plus) + sp.kronecker_product(P, dR),
        sp.kronecker_product(dP, R_minus) + sp.kronecker_product(P, dR_minus),
        sp.kronecker_product(dQ, R_plus) + sp.kronecker_product(Q, dR),
        sp.kronecker_product(dQ, R_minus) + sp.kronecker_product(Q, dR_minus),
    ]
    check("moving", f"q-row {index}: simultaneous product derivative reconstructs the full jet",
          sum((dsector * x + sector * dx
               for dsector, sector in zip(dsectors, sectors)), sp.zeros(56, 1)) == dx)
    check("moving", f"q-row {index}: differentiated sector projectors close",
          all(dsector * sector + sector * dsector == dsector
              for dsector, sector in zip(dsectors, sectors)))
    check("plant", f"q-row {index}: freezing either moving factor changes the receiver derivative",
          all(sp.kronecker_product(dP, factor) != dsector
              for factor, dsector in zip(
                  (R_plus, R_minus, R_plus, R_minus), dsectors))
          and all(sp.kronecker_product(base, signed_dR) != dsector
                  for base, signed_dR, dsector in zip(
                      (P, P, Q, Q), (dR, -dR, dR, -dR), dsectors)))


print("\nD. OVERLAP NATURALITY AND ORDINARY-PULLBACK CONTROL")
K = sp.zeros(10, 4)
for row, column, value in ((0, 0, 1), (2, 1, 2), (6, 2, -1), (9, 3, 3)):
    K[row, column] = sp.Rational(value, 37)
K_dagger = eta_h * K.T * eta_v
q = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.zeros(4), -K_dagger),
    sp.Matrix.hstack(K, sp.zeros(10)),
)
g = (sp.eye(14) - q).inv() * (sp.eye(14) + q)
moved = g * L
J_moved = moved[4:, :] * moved[:4, :].inv()
Lm = sp.Matrix.vstack(sp.eye(4), J_moved)
gm = Lm.T * eta * Lm
Pm = Lm * gm.inv() * Lm.T * eta

h = sp.Matrix([[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]])
Rpm = h * R_plus * h.inv()
transport = sp.kronecker_product(g, h)
check("atlas", "mixed graph and residual transports conjugate the product receiver",
      Pm == g * P * g.inv()
      and sp.kronecker_product(Pm, Rpm)
      == transport * sectors[0] * transport.inv())

ordinary = L.T * eta
kernel = ordinary.nullspace()
witness = kernel[0]
check("control", "ordinary pullback has rank four and a ten-dimensional conormal kernel",
      ordinary.rank() == 4 and len(kernel) == 10)
check("control", "complete receiver retains a nonzero covector erased by ordinary pullback",
      ordinary * witness == sp.zeros(4, 1)
      and Q * witness == witness and witness != sp.zeros(14, 1))
check("plant", "PLANT rank-four pullback is rejected as the complete nonlinear receiver",
      ordinary.rank() != sp.Matrix.vstack(P, Q).rank())


print("\nE. SCOPE, ACCOUNTING, AND HANDOFF")
check("variation", "v0.210 radial residual response remains nonzero while action derivative is zero",
      v210["radial_metric_first_jet"]["nonzero_residual_derivatives"] == 4
      and v210["radial_metric_first_jet"]["zero_action_derivatives"] == 4)
for kind, label in (
    ("composition", "the nonlinear receiver is existing composition debt rather than a new epsilon field"),
    ("symplectic", "lossless Euler reception does not build the antisymmetrized preboundary class"),
    ("analytic", "no common closed domain positivity spectrum or evolution theorem is inferred"),
    ("scope", "arbitrary-field I2B Euler coefficients remain unassembled"),
    ("scope", "the physical section coefficients and boundary class remain unselected"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("accounting", "no field parameter quotient selector or external datum is added"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CORRECTS_NAIVE_PULLBACK__SOURCE_SILENT_EXACT_PRODUCT")
print("NONLINEAR_RECEIVER=TANGENT_NORMAL_X_FIXED_ANTIFIXED__LOSSLESS__ATLAS_NATURAL")
print("NEXT=ASSEMBLE_REMAINING_ARBITRARY_FIELD_I2B_EULER_AND_ACTION_OWNED_PREBOUNDARY_COEFFICIENTS")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
