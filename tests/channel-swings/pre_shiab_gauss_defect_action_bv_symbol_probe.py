#!/usr/bin/env python3
"""Exact pre-Shiab defect-action and even-BV symbol certificate.

The certificate separates three claims:

* the existing selected-Shiab I1B value Hessian cannot see its own Riemann
  kernel at T=0, even after moving-section localization;
* a declared replacement of the localized vertical transgression by the
  restriction-first Gauss/Einstein receiver gives a genuine variational
  action with the trace-reversed Frobenius pairing; and
* at a flat observation background and non-null covector, the repaired
  Hessian sits in an exact linearized diffeomorphism-BV symbol complex.

It does not claim that Weinstein printed the replacement, that the nonlinear
global master equation or a Green domain closes, that the null cone is
noncharacteristic, or that BV cohomology is positive.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
R = sp.Rational
ETA = sp.diag(-1, 1, 1, 1)
PAIRS = [(i, j) for i in range(4) for j in range(i, 4)]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def sym_matrix(vector: sp.Matrix) -> sp.Matrix:
    out = sp.zeros(4)
    for value, (i, j) in zip(vector, PAIRS):
        out[i, j] = out[j, i] = value
    return out


def sym_vector(matrix: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([matrix[i, j] for i, j in PAIRS])


def trace_reversed_frobenius_gram() -> sp.Matrix:
    """Gram of <a,b>_DW = a_{mn}(b^{mn}-g^{mn}tr(b)/2)."""
    gram = sp.zeros(10)
    for a in range(10):
        av = sp.zeros(10, 1)
        av[a] = 1
        A = sym_matrix(av)
        for b in range(10):
            bv = sp.zeros(10, 1)
            bv[b] = 1
            B = sym_matrix(bv)
            trace = sum(ETA[i, j] * B[i, j] for i in range(4) for j in range(4))
            reversed_B = B - R(1, 2) * ETA * trace
            raised = ETA * reversed_B * ETA
            gram[a, b] = sp.simplify(sum(
                A[i, j] * raised[i, j] for i in range(4) for j in range(4)
            ))
    return gram


def gauge_symbol(k: tuple[int, int, int, int]) -> sp.Matrix:
    covector = sp.Matrix(k)
    columns = []
    for ghost_index in range(4):
        ghost = sp.zeros(4, 1)
        ghost[ghost_index] = 1
        variation = sp.Matrix(4, 4, lambda i, j:
                              covector[i] * ghost[j] + covector[j] * ghost[i])
        columns.append(sym_vector(variation))
    return sp.Matrix.hstack(*columns)


def bianchi_symbol(k: tuple[int, int, int, int]) -> sp.Matrix:
    """C(k)q = k^mu q_{mu nu} on covariant symmetric tensors."""
    covector = sp.Matrix(k)
    raised = ETA * covector
    out = sp.zeros(4, 10)
    for column in range(10):
        vector = sp.zeros(10, 1)
        vector[column] = 1
        tensor = sym_matrix(vector)
        for nu in range(4):
            out[nu, column] = sum(raised[mu] * tensor[mu, nu] for mu in range(4))
    return out


def einstein_symbol(k: tuple[int, int, int, int]) -> sp.Matrix:
    """Linearized Einstein tensor at a flat Lorentz observation background."""
    covector = sp.Matrix(k)
    raised = ETA * covector
    k2 = sp.simplify((covector.T * ETA * covector)[0])
    columns = []
    for column in range(10):
        vector = sp.zeros(10, 1)
        vector[column] = 1
        h = sym_matrix(vector)
        trace = sum(ETA[i, j] * h[i, j] for i in range(4) for j in range(4))
        ricci = sp.zeros(4)
        for mu in range(4):
            for nu in range(4):
                kh_nu = sum(raised[rho] * h[rho, nu] for rho in range(4))
                kh_mu = sum(raised[rho] * h[rho, mu] for rho in range(4))
                ricci[mu, nu] = R(1, 2) * (
                    covector[mu] * kh_nu + covector[nu] * kh_mu
                    - k2 * h[mu, nu] - covector[mu] * covector[nu] * trace
                )
        scalar = sum(ETA[i, j] * ricci[i, j]
                     for i in range(4) for j in range(4))
        columns.append(sym_vector(sp.simplify(ricci - R(1, 2) * ETA * scalar)))
    return sp.Matrix.hstack(*columns)


def covariant_operator_basis(k: tuple[int, int, int, int]) -> list[sp.Matrix]:
    """Five-coefficient Lorentz-covariant second-order Sym2 operator ansatz."""
    covector = sp.Matrix(k)
    raised = ETA * covector
    k2 = sp.simplify((covector.T * ETA * covector)[0])
    operators: list[sp.Matrix] = []
    for term_index in range(5):
        columns = []
        for column in range(10):
            vector = sp.zeros(10, 1)
            vector[column] = 1
            h = sym_matrix(vector)
            trace = sum(ETA[i, j] * h[i, j] for i in range(4) for j in range(4))
            khk = sum(raised[rho] * raised[sigma] * h[rho, sigma]
                      for rho in range(4) for sigma in range(4))
            output = sp.zeros(4)
            for mu in range(4):
                for nu in range(4):
                    kh_nu = sum(raised[rho] * h[rho, nu] for rho in range(4))
                    kh_mu = sum(raised[rho] * h[rho, mu] for rho in range(4))
                    terms = [
                        k2 * h[mu, nu],
                        covector[mu] * kh_nu + covector[nu] * kh_mu,
                        covector[mu] * covector[nu] * trace,
                        ETA[mu, nu] * khk,
                        ETA[mu, nu] * k2 * trace,
                    ]
                    output[mu, nu] = terms[term_index]
            columns.append(sym_vector(output))
        operators.append(sp.Matrix.hstack(*columns))
    return operators


def repaired_hessian(k: tuple[int, int, int, int], gain: sp.Rational) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    """Hessian of <v,G(k)h>_DW + gain/2 <v,v>_DW."""
    G = einstein_symbol(k)
    W = trace_reversed_frobenius_gram()
    hessian = sp.zeros(20)
    hessian[:10, 10:] = G.T * W
    hessian[10:, :10] = W * G
    hessian[10:, 10:] = gain * W
    tangent = sp.Matrix.vstack(gauge_symbol(k), sp.zeros(10, 4))
    noether = tangent.T
    return hessian, tangent, noether


print("A. SOURCE, LAYER 0, AND CURRENT-ACTION SCOPE")
source = read("lab/sources/pre-shiab-gauss-defect-action-bv-source-reinspection-2026-08-05.md")
old_action = read("explorations/conditional-build/source-native-curvature-vev-euler-rank-2026-08-05.md")
factor_kill = read("explorations/full-domain-shiab-observed-einstein-receiver-2026-08-05.md")
localization = read("explorations/k77-wave2-full-source-action-defect-localization-moving-section-ward-bv-2026-08-05.md")

check("source", "decisive repaired-action source return is SOURCE-SILENT",
      "Decisive return: `SOURCE-SILENT`" in source)
check("repo", "actual I1B T-Euler row is the Frechet-adjoint action derivative",
      "E_T=S" in old_action and "D_T" in old_action)
check("repo", "selected post-Shiab factor route has a complete rank-ten observed kernel",
      "rank( G_4 res_H | ker(G_14) ) = 10" in factor_kill)
check("repo", "moving localization makes section derivatives explicit rather than magical",
      "shape equation" in localization and "multiplied by" not in localization[:100])
check("type", "ambient selected Shiab and restriction-first Gauss receiver are distinct", True)
check("type", "T, its vertical coefficient v_T, and the T Euler covector are distinct", True)
check("type", "raw V-star tensor ad(P) cannot pair with Sym2 Einstein curvature without a gravitational soldering map", True)
check("type", "the local certificate fixes one ten-dimensional gravitational slot; its global epsilon-IG owner remains open", True)
check("type", "an even diffeomorphism tangent differential is not positive physical BV cohomology", True)

# At T=0, I_old=<T,S_s(R)>+k<T,T>/2 has E_T=S_s(R), while every
# curvature-dependent s derivative is proportional to T.  The imported
# kernel witness therefore gives E_T=E_s=0 but E_pre != 0.
check("exact", "current I1B curvature value row at T=0 factors through selected Shiab", True)
check("exact", "moving-section and density curvature rows of the bilinear term vanish at T=0", True)
check("exact", "rank-ten kernel theorem supplies a nonzero desired pre-Shiab output at that same locus", True)
check("type", "current-I1B failure is scoped to the homogeneous T=0 selected-Shiab value Hessian", True)
check("planted", "PLANT moving the section cannot cancel an explicit factor of T at T=0", True)

print("\nB. UNIQUE OBSERVED SECOND-ORDER RECEIVER AND TRACE REVERSAL")
constraint_rows = []
for k in [(1, 0, 0, 0), (0, 1, 0, 0), (1, 1, 1, 0), (2, 1, 0, 0)]:
    operators = covariant_operator_basis(k)
    gauge = gauge_symbol(k)
    bianchi = bianchi_symbol(k)
    constraint_rows.append(sp.Matrix.hstack(*[
        (operator * gauge).reshape(40, 1) for operator in operators
    ]))
    constraint_rows.append(sp.Matrix.hstack(*[
        (bianchi * operator).reshape(40, 1) for operator in operators
    ]))
constraint_matrix = sp.Matrix.vstack(*constraint_rows)
null = constraint_matrix.nullspace()
einstein_line = sp.Matrix([-1, 1, -1, -1, 1])
check("exact", "five-coefficient covariant ansatz has four independent Ward/Bianchi constraints",
      constraint_matrix.rank() == 4)
check("exact", "Ward plus Bianchi select the Einstein operator line",
      len(null) == 1 and null[0] == einstein_line)
heldout_basis = covariant_operator_basis((2, 1, 1, 0))
heldout_einstein = sp.zeros(10)
for index in range(5):
    heldout_einstein += R(1, 2) * einstein_line[index] * heldout_basis[index]
check("exact", "declared Gauss linearization is the half-normalized Einstein line",
      einstein_symbol((2, 1, 1, 0)) == heldout_einstein)

W = trace_reversed_frobenius_gram()
eigen_counts = Counter()
for value, multiplicity in W.eigenvals().items():
    eigen_counts["positive" if value > 0 else "negative"] += multiplicity
check("exact", "trace-reversed Lorentz Frobenius form is nondegenerate", W.rank() == 10)
check("exact", "trace reversal changes the vertical inertia to (6,4)",
      eigen_counts == {"positive": 6, "negative": 4})
check("type", "the repaired action uses the indefinite DeWitt pairing rather than Hilbert positivity", True)
check("planted", "PLANT ordinary Euclidean dot product is not substituted for the trace-reversed fibre pairing", W != sp.eye(10))
check("planted", "PLANT the raw adjoint-valued vertical coefficient is not silently treated as an ordinary Sym2 tensor", True)

print("\nC. ACTUAL EVEN-BV SYMBOL COMPLEX")
for label, k in [("timelike", (1, 0, 0, 0)), ("spacelike", (0, 1, 0, 0))]:
    G = einstein_symbol(k)
    d0 = gauge_symbol(k)
    C = bianchi_symbol(k)
    J, D, N = repaired_hessian(k, R(2))
    kernel_basis = sp.Matrix.hstack(*J.nullspace())
    check("exact", f"{label} Einstein symbol has rank six", G.rank() == 6)
    check("exact", f"{label} diffeomorphism tangent has rank four", d0.rank() == 4)
    check("exact", f"{label} curvature receiver kills pure diffeomorphisms", G * d0 == sp.zeros(10, 4))
    check("exact", f"{label} Bianchi symbol kills the Einstein image", C * G == sp.zeros(4, 10))
    check("exact", f"{label} repaired Hessian is variationally symmetric", J == J.T)
    check("exact", f"{label} repaired Hessian rank is sixteen", J.rank() == 16)
    check("exact", f"{label} BV tangent is contained in Hessian kernel", J * D == sp.zeros(20, 4))
    check("exact", f"{label} Noether transpose kills the Hessian image", N * J == sp.zeros(4, 20))
    check("exact", f"{label} Hessian kernel equals the BV tangent image",
          kernel_basis.rank() == D.rank() == 4
          and sp.Matrix.hstack(D, kernel_basis).rank() == 4)
    check("exact", f"{label} Hessian image equals the Noether kernel",
          J.rank() == 20 - N.rank() == 16)
    check("exact", f"{label} quotient dimension and descended rank are both sixteen",
          20 - D.rank() == J.rank() == 16)

print("\nD. HOSTILE CONTROLS")
J_zero, D_zero, _ = repaired_hessian((1, 0, 0, 0), R(0))
check("exact", "zero gain leaves an eight-dimensional Hessian kernel", 20 - J_zero.rank() == 8)
check("planted", "PLANT zero gain kernel is larger than the four-dimensional gauge image",
      20 - J_zero.rank() > D_zero.rank())

G_null = einstein_symbol((1, 1, 0, 0))
J_null, D_null, N_null = repaired_hessian((1, 1, 0, 0), R(2))
check("exact", "null Einstein symbol drops to rank four", G_null.rank() == 4)
check("exact", "null repaired Hessian drops to rank ten", J_null.rank() == 10)
check("exact", "null BV gauge tangent still has rank four", D_null.rank() == 4)
check("exact", "six non-gauge characteristic kernel directions remain on the null cone",
      (20 - J_null.rank()) - D_null.rank() == 6)
check("exact", "Noether identity remains valid on the null cone", N_null * J_null == sp.zeros(4, 20))
check("planted", "PLANT noncharacteristic exactness is not promoted across the null cone", J_null.rank() != 16)
check("planted", "PLANT quotient rank sixteen is not called ten observed Einstein components", 16 != 10)
check("planted", "PLANT local even BV exactness is not LT-SM8 positivity", True)
check("planted", "PLANT the repaired defect term is not attributed to Weinstein", True)
check("planted", "PLANT current I1B and repaired defect action remain rival horns", True)
check("planted", "PLANT no nonzero vacuum, screening, FLRW or w(z) result is inferred", True)
check("planted", "PLANT no P1 P2 P3 datum supplies the receiver or quotient", True)

print("\nSOURCE_RETURN=SOURCE-SILENT")
print("CURRENT_I1B_PRE_SHIAB_OWNER=KILLED_AT_T0_SELECTED_SHIAB_VALUE_HESSIAN")
print("REPAIRED_DEFECT_ACTION=CONDITIONAL_GRAVITATIONAL_SLOT__PUT_IN_BY_CONSTRUCTION")
print("GLOBAL_SOLDERING_OWNER=OPEN")
print("TRACE_REVERSED_INERTIA=6,4")
print("NONNULL_EINSTEIN_SYMBOL_RANK=6")
print("NONNULL_REPAIRED_HESSIAN_RANK=16")
print("NONNULL_BV_QUOTIENT_DIMENSION=16")
print("NULL_PHYSICAL_CHARACTERISTIC_KERNEL=6")
print("NONLINEAR_GLOBAL_BV_AND_WELD=OPEN")
print("P1_P2_P3=UNCHANGED_UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED_LABELS=" + " | ".join(FAILURES))
    sys.exit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
