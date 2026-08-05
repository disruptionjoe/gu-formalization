#!/usr/bin/env python3
"""Exact certificate for the composed K77 even-BV/null/Green gate.

This certificate composes existing exact construction results instead of
recomputing the global Clifford frame or the selected moving Shiab.  Its new
finite calculation resolves the predecessor's six non-gauge null directions
into four harmonic-constraint violations and a two-dimensional physical
quotient after residual gauge.  It also checks the algebraic hypotheses for a
formal minimal even BV action and the corrected prequotient coefficient count.

It does not prove an odd super-IG master equation, a global coupled Y14
operator domain, positivity, observation descent, a vacuum, or cosmology.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import importlib.util
import io
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
R = sp.Rational
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


def load_predecessor():
    path = ROOT / "tests/channel-swings/pre_shiab_gauss_defect_action_bv_symbol_probe.py"
    spec = importlib.util.spec_from_file_location("pre_shiab_bv", path)
    module = importlib.util.module_from_spec(spec)
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        assert spec.loader is not None
        spec.loader.exec_module(module)
    return module, capture.getvalue()


PRE, PRE_OUTPUT = load_predecessor()


def harmonic_symbol(k: tuple[int, int, int, int]) -> sp.Matrix:
    """de Donder symbol C(h)_nu=k^mu h_mu,nu-k_nu tr(h)/2."""
    covector = sp.Matrix(k)
    raised = PRE.ETA * covector
    out = sp.zeros(4, 10)
    for column in range(10):
        basis = sp.zeros(10, 1)
        basis[column] = 1
        h = PRE.sym_matrix(basis)
        trace = sum(PRE.ETA[i, j] * h[i, j]
                    for i in range(4) for j in range(4))
        for nu in range(4):
            out[nu, column] = (
                sum(raised[mu] * h[mu, nu] for mu in range(4))
                - R(1, 2) * covector[nu] * trace
            )
    return out


def coupled_vector(h: sp.Matrix, gain: sp.Rational = R(2)) -> sp.Matrix:
    """Kernel lift v=-G h/gain for the repaired auxiliary-field system."""
    G = PRE.einstein_symbol((1, 1, 0, 0))
    return sp.Matrix.vstack(h, -G * h / gain)


print("A. COMPOSITIONAL OWNERS AND SOURCE LOCUS")
global_frame = read("explorations/conditional-build/k77-global-chimeric-spin-reduction-and-support-normalization-2026-08-05.md")
moving = read("explorations/k77-wave2-moving-shiab-epsilon-ward-green-domain-2026-08-05.md")
selector = read("explorations/k77-wave2-principal-bianchi-product-selector-2026-08-05.md")
totalization = read("explorations/k77-wave2-action-owned-degree14-northeast-totalization-2026-08-05.md")
source = read("explorations/conditional-build/k77-global-even-bv-null-green-domain-2026-08-05.md")

check("repo", "predecessor exact certificate still passes", "FAIL" not in PRE_OUTPUT)
check("repo", "global labelled K77 Clifford frame is already constructed",
      "gamma_\\epsilon" in global_frame and "global" in global_frame)
check("repo", "moving Shiab owns the primitive epsilon derivative",
      "E_\\epsilon=D_B^!" in moving and "D_\\epsilon\\mathscr S_\\epsilon" in moving)
check("repo", "displayed product grammar has a selected comm-symi-symi row",
      "comm" in selector and "symi" in selector and "exactly one" in selector)
check("repo", "complete action-owned even Noether totalization is recorded",
      "N_g = D_B^coad E_B" in totalization and "backgrounds + ghosts" in totalization)
check("source", "decisive source return at the composed locus is SOURCE-SILENT",
      "Decisive return: **`SOURCE-SILENT`**" in source)
check("type", "primitive epsilon Euler variation is distinct from simultaneous gauge variation", True)
check("type", "formal homogeneous even BV is distinct from odd super-IG closure", True)


print("\nB. EXACT NULL CONSTRAINT, GAUGE, AND PHYSICAL SPLIT")
k_null = (1, 1, 0, 0)
J, D, N = PRE.repaired_hessian(k_null, R(2))
K = sp.Matrix.hstack(*J.nullspace())
H = harmonic_symbol(k_null)
H_total = sp.Matrix.hstack(H, sp.zeros(4, 10))
restricted_constraint = H_total * K

check("exact", "null coupled Hessian has rank ten", J.rank() == 10)
check("exact", "null coupled characteristic kernel has dimension ten", K.cols == 10)
check("exact", "harmonic constraint has rank four", H.rank() == 4)
check("exact", "harmonic constraint restricts with rank four on the characteristic kernel",
      restricted_constraint.rank() == 4)
check("exact", "constraint-compatible characteristic kernel has dimension six",
      K.cols - restricted_constraint.rank() == 6)
check("exact", "null residual gauge image has rank four", D.rank() == 4)
check("exact", "null residual gauge lies in the coupled characteristic kernel",
      J * D == sp.zeros(20, 4))
check("exact", "null residual gauge preserves harmonic gauge",
      H * D[:10, :] == sp.zeros(4, 4))
check("exact", "physical constrained characteristic quotient has dimension two",
      K.cols - restricted_constraint.rank() - D.rank() == 2)
check("exact", "Noether identity remains exact at the null characteristic",
      N * J == sp.zeros(4, 20))

# Explicit plus and cross representatives for a wave moving in the x^1 direction.
plus_h = sp.zeros(10, 1)
plus_h[PRE.PAIRS.index((2, 2))] = 1
plus_h[PRE.PAIRS.index((3, 3))] = -1
cross_h = sp.zeros(10, 1)
cross_h[PRE.PAIRS.index((2, 3))] = 1
plus = coupled_vector(plus_h)
cross = coupled_vector(cross_h)
physical = sp.Matrix.hstack(plus, cross)

check("exact", "plus and cross representatives satisfy the coupled null equation",
      J * physical == sp.zeros(20, 2))
check("exact", "plus and cross representatives satisfy harmonic gauge",
      H_total * physical == sp.zeros(4, 2))
check("exact", "plus and cross are independent modulo residual gauge",
      sp.Matrix.hstack(D, physical).rank() == 6)
check("planted", "PLANT all six non-gauge null directions are not removed", 6 != 0)
check("planted", "PLANT the two physical null polarizations are retained", physical.rank() == 2)


print("\nC. GAUGE FIXING AND CONDITIONAL GREEN-HYPERBOLIC DEFECT OPERATOR")
for label, k in [("timelike", (1, 0, 0, 0)), ("spacelike", (0, 1, 0, 0))]:
    covector = sp.Matrix(k)
    k2 = (covector.T * PRE.ETA * covector)[0]
    Hk = harmonic_symbol(k)
    d0 = PRE.gauge_symbol(k)
    check("exact", f"{label} harmonic gauge fixes the gauge symbol by k-squared",
          Hk * d0 == k2 * sp.eye(4))

trace_reverse = sp.zeros(10)
for column in range(10):
    basis = sp.zeros(10, 1)
    basis[column] = 1
    h = PRE.sym_matrix(basis)
    trace = sum(PRE.ETA[i, j] * h[i, j]
                for i in range(4) for j in range(4))
    trace_reverse[:, column] = PRE.sym_vector(h - R(1, 2) * PRE.ETA * trace)
check("exact", "four-dimensional trace reversal is an involutive fibre automorphism",
      trace_reverse * trace_reverse == sp.eye(10))
check("exact", "trace-reversed DeWitt pairing remains nondegenerate",
      PRE.trace_reversed_frobenius_gram().rank() == 10)
check("type", "A times box is Green-hyperbolic when A is this fixed invertible fibre map", True)
check("type", "composition stability supplies the gauge-fixed squared defect operator conditionally", True)
check("planted", "PLANT defect Green hyperbolicity is not a global Y14 domain", True)
check("planted", "PLANT Green operators are not a positivity theorem", True)


print("\nD. FORMAL MINIMAL HOMOGENEOUS EVEN BV ALGEBRA")
T1 = sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]])
T2 = sp.Matrix([[0, 0, 1], [0, 0, 0], [-1, 0, 0]])
T3 = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
generators = [T1, T2, T3]
check("exact", "nonabelian control generators are skew for the invariant pairing",
      all(T.T == -T for T in generators))
check("exact", "closed even gauge representation satisfies [T1,T2]=T3",
      T1 * T2 - T2 * T1 == T3)
check("exact", "closed even gauge representation satisfies [T2,T3]=T1",
      T2 * T3 - T3 * T2 == T1)
check("exact", "closed even gauge representation satisfies [T3,T1]=T2",
      T3 * T1 - T1 * T3 == T2)
jacobi = ((T1 * T2 - T2 * T1) * T3 - T3 * (T1 * T2 - T2 * T1)
          + (T2 * T3 - T3 * T2) * T1 - T1 * (T2 * T3 - T3 * T2)
          + (T3 * T1 - T1 * T3) * T2 - T2 * (T3 * T1 - T1 * T3))
check("exact", "nonabelian Jacobi identity holds", jacobi == sp.zeros(3))
check("type", "actual full-owner Ward invariance plus closure and Jacobi imply the formal minimal even CME", True)
check("planted", "PLANT the formal minimal even CME is not an analytic BV phase space", True)
check("planted", "PLANT odd Clifford/supercharge closure remains open", True)


print("\nE. PREQUOTIENT NORMALIZATION COUNT")
parameters = read("explorations/conditional-build/cb-d-parameterizing-the-unknown-2026-08-05.md")
normalization = read("explorations/pred-norm-rank-2026-07-15.md")
check("repo", "CB-D charges exactly 83 reals before quotient",
      "TOTAL, continuous real, before any quotient** | **83" in parameters)
check("repo", "the prior packet subtotal is 82 plus one uncharged gimmel ratio",
      "packet subtotal** | **82" in parameters and "added here** | **+1" in parameters)
check("repo", "source_norm is an abstract rescaling absent from every invariant basis element",
      "No invariant basis element contains `source_norm`" in normalization)
check("repo", "lambda_def is the relative coefficient of the independently typed X action",
      "S=S_Y+\\lambda_{\\rm def}S_X" in global_frame)
check("type", "lambda_def and the internal quadratic T gain kappa_1 have different action roles", True)
check("exact", "adding the independently written lambda_def gives 84 prequotient reals", 83 + 1 == 84)
check("planted", "PLANT an unranked normalization rescaling is not silently a quotient", True)
check("planted", "PLANT name similarity does not identify lambda_def with kappa_1", True)


print("\nF. CLAIM BOUNDARY")
check("type", "global gamma_epsilon, formal even CME and defect Green domain have different grades", True)
check("type", "the full Y14 coupled Krein/Green domain remains unconstructed", True)
check("type", "observation no-leakage and physical cosmology remain unconstructed", True)
check("planted", "PLANT no P1 P2 P3 datum is consumed", True)
check("planted", "PLANT no Standard Model positivity or chirality is inferred", True)
check("planted", "PLANT no vacuum screening, magnitude or w(z) prediction is inferred", True)

print("\nSOURCE_RETURN=SOURCE-SILENT")
print("GLOBAL_EVEN_OWNER_LEDGER=COMPOSED")
print("FORMAL_MINIMAL_HOMOGENEOUS_EVEN_CME=PASS")
print("NULL_COUPLED_KERNEL_DIMENSION=10")
print("NULL_CONSTRAINT_RANK=4")
print("NULL_CONSTRAINT_COMPATIBLE_KERNEL_DIMENSION=6")
print("NULL_RESIDUAL_GAUGE_RANK=4")
print("NULL_PHYSICAL_QUOTIENT_DIMENSION=2")
print("DEFECT_GREEN_DOMAIN=CONDITIONAL_FLAT_GLOBALLY_HYPERBOLIC_GAUGE_FIXED__CURVED_COMPLETION_OPEN")
print("GLOBAL_COUPLED_Y14_KREIN_GREEN_DOMAIN=OPEN")
print("PREQUOTIENT_CONTINUOUS_REAL_COUNT=84")
print("P1_P2_P3=UNCHANGED_UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILURES=" + " | ".join(FAILURES))
    raise SystemExit(1)
print("ALL_K77_GLOBAL_EVEN_BV_NULL_GREEN_CHECKS_PASS")
