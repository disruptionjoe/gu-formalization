#!/usr/bin/env python3
r"""LEG 2A -- Sp(64) octic trace + local I_16 + Green-Schwarz factorizability.

CONTEXT
-------
The GU local anomaly is the degree-16 form  I_16 = [A-hat(TY14) . ch_R(F)]_16.
The pure-gravitational box term [A-hat(TY14)]_16 is already computed and verified
(tests/ahat_genus_y14_i16.py: validated on the canonical [A-hat]_4,8,12 and on two
independent indices (K3)^4 -> 16, HP^2xHP^2 -> 0). This file builds the GAUGE side
and tests Green-Schwarz (GS) factorizability of the LOCAL anomaly.

WHAT GS FACTORIZABILITY MEANS (D=14)
------------------------------------
I_16 is cancellable by a Green-Schwarz mechanism iff it FACTORIZES, i.e. iff it can
be written as a sum of products of lower-degree closed forms (e.g. X_4 ^ X_12,
X_8 ^ X_8). The obstruction is the IRREDUCIBLE part of degree 16: a single invariant
that is NOT a product of lower invariants. There are two such irreducible channels:
  (gauge)         the PRIMITIVE order-8 Casimir  tr_S F^8|_prim   (a single trace,
                  not a product of lower traces);
  (gravitational) the PRIMITIVE degree-8 Pontryagin  ~ tr R^8     (the p4 monomial of
                  [A-hat(TY14)]_16, irreducible in p1..p4).
If EITHER irreducible coefficient is nonzero in the total anomaly, I_16 does NOT
factorize and GS cannot cancel it locally.

WHAT THIS FILE COMPUTES
-----------------------
(1) The symmetric traces Str_S(F^2), Str_S(F^4), Str_S(F^6), Str_S(F^8) for the
    Sp(2n)-FUNDAMENTAL-type module S = H^64 (2n = 64, rank n = 32), and the
    decomposition of the octic into {primitive order-8 Casimir, products of lower
    Casimirs}. For the fundamental this is EXACT and elementary: the rep weights are
    {+-x_1,...,+-x_n}, so Str_S F^{2m} = 2 P_m with P_m = sum_j x_j^{2m}, and P_4 is
    the primitive order-8 Casimir. The decisive question is whether P_4 is an
    INDEPENDENT Casimir (=> irreducible octic) -- tested by the rank of the
    power-sum Jacobian (rank 4 <=> P_1..P_4 functionally independent <=> P_4 primitive).
(2) CROSS-CHECK of the symmetric-trace machinery BEFORE trusting any Sp(64) number,
    on two textbook SO groups, by TWO independent methods (root/weight power-sums and
    explicit Clifford matrices reusing oq_rk1_cl95_explicit_rep.jordan_wigner_gammas):
       SO(10): spinor/vector index ratio T(16)/T(10) = 2^{n-4} = 2,  quartic identity.
       SO(12): T(32)/T(12) = 4, quartic identity.
       SO(N) adjoint reductions: primitive coeff (N-2),(N-8),(N-32),(N-128) at orders
              2,4,6,8 -- the famous GS reduction factors (N=32 kills order-6, N=128
              kills order-8). These independently exercise the primitive/reducible split.
(3) Combine with [A-hat(TY14)]_16 and the assumed chiral content to emit a DEFINITE
    local factorizability boolean.

HONEST SCOPE (mandatory; the repo has a 'load-bearing and wrong' history -- under-claim)
  * The factorizability verdict is CONDITIONAL on the assumed chiral content
    Omega^0(x)S^+ + Omega^1(x)S^-, and in particular on the multiplicity/chirality
    weighting (n_+ - n_-) it induces. The group-theory facts (Str_S F^8 = 2 P_4; P_4
    primitive for rank 32; SO cross-checks) are unconditional; the WEIGHTING that turns
    them into an anomaly coefficient is part of the assumed content.
  * It is CONDITIONAL on the CONTESTED Sp(64)-vs-Sp(1) gauge-group reading
    (shiab_selector_sp64.py honesty note: the genuine Clifford commutant is Sp(1)=right-H,
    not the full Sp(64)=U(64,H)). "S = H^64 fundamental of Sp(64)" is the GU-canon reading;
    under the Sp(1) commutant reading the gauge octic is a different (smaller-rank) object.
  * The GLOBAL anomaly (eta-invariant / Dai-Freed / bordism) leg stays OPEN. Local
    factorizability is necessary, not sufficient, for full anomaly freedom.
  * Therefore this delivers a CONDITIONAL number and a CONDITIONAL boolean, NOT a
    cancellation claim on canon.
"""

from __future__ import annotations

import os
import sys
from fractions import Fraction as Fr
from itertools import product as iproduct

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import ahat_genus_y14_i16 as ahat            # verified [A-hat(TY14)]_16
import oq_rk1_cl95_explicit_rep as cl95      # jordan_wigner_gammas (explicit Clifford)

TOL = 1e-9


# ===========================================================================
# 0. EXACT power-sum algebra.  A "Casimir monomial" of weight m is a tuple of
#    exponents over the primitive power sums (P_1,P_2,P_3,P_4,...);
#    weight(e) = sum_k k*e_k.  We work in exact Fraction arithmetic.
# ===========================================================================
def partitions_weight(m, kmax):
    """All exponent tuples (e_1..e_kmax) with sum k*e_k = m.  Each tuple <-> monomial
    P_1^{e_1} P_2^{e_2} ... ; weight m corresponds to trace order 2m in F."""
    res = []

    def rec(k, rem, acc):
        if k > kmax:
            if rem == 0:
                res.append(tuple(acc))
            return
        maxe = rem // k
        for e in range(maxe + 1):
            rec(k + 1, rem - k * e, acc + [e])
    rec(1, m, [])
    return res


def Pmono_value(expo, xs):
    """Value of the power-sum monomial prod_k P_k^{e_k} at the point xs (list of x_j),
    where P_k = sum_j x_j^{2k}.  Exact if xs are Fractions."""
    val = Fr(1)
    for k, e in enumerate(expo, start=1):
        if e:
            Pk = sum((x ** (2 * k) for x in xs), Fr(0))
            val *= Pk ** e
    return val


def solve_exact(A, b):
    """Solve A x = b exactly over Fractions (A possibly overdetermined-consistent;
    we take the first len(b0) independent rows).  Returns x or raises on inconsistency."""
    # Gaussian elimination with full pivoting on a square subsystem; verify all rows.
    m = len(A)
    n = len(A[0])
    M = [[Fr(A[i][j]) for j in range(n)] + [Fr(b[i])] for i in range(m)]
    piv_rows = []
    col = 0
    r = 0
    while r < m and col < n:
        # find pivot in column col at row >= r
        prow = None
        for i in range(r, m):
            if M[i][col] != 0:
                prow = i
                break
        if prow is None:
            col += 1
            continue
        M[r], M[prow] = M[prow], M[r]
        pv = M[r][col]
        M[r] = [v / pv for v in M[r]]
        for i in range(m):
            if i != r and M[i][col] != 0:
                f = M[i][col]
                M[i] = [M[i][j] - f * M[r][j] for j in range(n + 1)]
        piv_rows.append(col)
        r += 1
        col += 1
    # extract solution
    x = [Fr(0)] * n
    for i, c in enumerate(piv_rows):
        x[c] = M[i][n]
    # consistency on all original rows
    for i in range(m):
        lhs = sum(A[i][j] * x[j] for j in range(n))
        if lhs != b[i]:
            raise ValueError("trace is NOT a polynomial in P_1..P_kmax (inconsistent)")
    return x


def decompose_trace(trace_at, m, kmax, nvars, seed=12345):
    """Express a symmetric trace (given as a callable trace_at(xs)->Fraction, a degree-2m
    invariant) EXACTLY in the primitive power-sum monomial basis of weight m.
    Returns {expo_tuple: Fraction coeff}.  nvars >= m must hold for the basis to be
    independent."""
    monos = partitions_weight(m, kmax)
    npts = len(monos) + 3
    rng = np.random.RandomState(seed)
    rows, rhs = [], []
    for _ in range(npts):
        xs = [Fr(int(rng.randint(1, 50)), int(rng.randint(1, 7))) for _ in range(nvars)]
        rows.append([Pmono_value(e, xs) for e in monos])
        rhs.append(trace_at(xs))
    coeffs = solve_exact(rows, rhs)
    return {monos[i]: coeffs[i] for i in range(len(monos)) if coeffs[i] != 0}, monos


# ===========================================================================
# 1. Root/weight traces (EXACT) for the classical reps we need.
# ===========================================================================
def tr_vector(xs, m):
    """tr_V F^{2m} for the defining rep of SO(2n)/Sp(2n): weights {+-x_j} -> 2 P_m."""
    return 2 * sum((x ** (2 * m) for x in xs), Fr(0))


def tr_spinor(xs, m, chir=+1):
    """tr_{S^chir} F^{2m} for the SO(2n) chiral spinor: weights (1/2) sum eps_j x_j over
    sign vectors eps with prod(eps) = chir (chir=+1 -> even # of -1 -> S^+)."""
    n = len(xs)
    half = Fr(1, 2)
    tot = Fr(0)
    for eps in iproduct((1, -1), repeat=n):
        if (1 if eps.count(-1) % 2 == 0 else -1) != chir:
            continue
        w = half * sum((Fr(s) * x for s, x in zip(eps, xs)), Fr(0))
        tot += w ** (2 * m)
    return tot


def tr_adjoint_so(xs, m):
    """tr_adj F^{2m} for SO(2n) adjoint (antisymmetric tensor): weights {+-x_i+-x_j, i<j}
    plus n zeros."""
    n = len(xs)
    tot = Fr(0)
    for i in range(n):
        for j in range(i + 1, n):
            for si in (1, -1):
                for sj in (1, -1):
                    w = Fr(si) * xs[i] + Fr(sj) * xs[j]
                    tot += w ** (2 * m)
    return tot  # the n zero-weights contribute 0


def irreducible_part(coeffs):
    """Coefficient of the single primitive Casimir P_m of weight m (the monomial with a
    lone P_m, i.e. exponent tuple (0,...,0,1) of length m). Everything else is reducible
    (a product of lower Casimirs)."""
    for expo, c in coeffs.items():
        if sum(expo) == 1 and expo[-1] == 1 and len(expo) >= 1:
            # lone top power sum P_{len(expo)} ; only when its index == weight m
            if (len(expo)) * 1 == sum(k * e for k, e in enumerate(expo, 1)):
                return c
    return Fr(0)


def fmt_poly(coeffs):
    names = {1: "P1", 2: "P2", 3: "P3", 4: "P4"}

    def mono(expo):
        parts = []
        for k, e in enumerate(expo, 1):
            if e == 1:
                parts.append(names[k])
            elif e > 1:
                parts.append(f"{names[k]}^{e}")
        return "*".join(parts) if parts else "1"
    return "  ".join(f"({c}){mono(e)}" for e, c in sorted(coeffs.items()))


# ===========================================================================
# 2. CROSS-CHECK A: explicit-Clifford-matrix traces vs the root formula (SO(10),SO(12)).
#    Independent of the root method: builds real matrices and takes numpy traces.
# ===========================================================================
def explicit_so_spinor_check(n):
    """Build SO(2n) in vector (J_ab) and chiral-spinor (Sigma_ab) reps from explicit
    Hermitian gammas; for a random algebra element compare tr_{S+}F^{2m} (numpy) to the
    EXACT root prediction, and report the index ratio T(S+)/T(V)."""
    G = cl95.jordan_wigner_gammas(n)            # 2n Hermitian gammas, size 2^n, Euclidean
    N = 2 * n
    dim = 2 ** n
    Iden = np.eye(dim, dtype=complex)
    # chirality Gamma_* = (-i)^n G_0...G_{2n-1}  (Hermitian, squares to I)
    chir = ((-1j) ** n) * Iden.copy()
    for a in range(N):
        chir = chir @ G[a]
    Pp = 0.5 * (Iden + chir)                    # S^+ projector

    def Sigma(a, b):                            # spinor generator (anti-Hermitian)
        return 0.25 * (G[a] @ G[b] - G[b] @ G[a])

    def Jvec(a, b):                             # vector generator, same algebra element
        M = np.zeros((N, N), dtype=complex)
        M[a, b] += 1.0
        M[b, a] -= 1.0
        return M

    rng = np.random.RandomState(7)
    theta = {(a, b): rng.randn() for a in range(N) for b in range(a + 1, N)}
    Fs = np.zeros((dim, dim), dtype=complex)
    Fv = np.zeros((N, N), dtype=complex)
    for (a, b), t in theta.items():
        Fs += t * Sigma(a, b)
        Fv += t * Jvec(a, b)

    # x_j from the vector rep: eigenvalues of Fv are +- i x_j
    ev = np.linalg.eigvals(Fv)
    xs_num = sorted({round(abs(z.imag), 9) for z in ev if z.imag > 1e-9})
    xs = [Fr(int(round(v * 10 ** 6)), 10 ** 6) for v in xs_num]  # rationalize for the formula

    out = {"n": n, "N": N}
    # index ratio at order 2 (numpy, exact-rep-independent)
    t2_Splus = np.trace(Pp @ Fs @ Fs)
    t2_V = np.trace(Fv @ Fv)
    out["index_ratio_T(S+)/T(V)"] = float((t2_Splus / t2_V).real)
    out["index_ratio_predicted_2^(n-4)"] = 2.0 ** (n - 4)
    # quartic numeric vs root prediction (signs: Fs,Fv anti/real -> recompute both numerically)
    t4_Splus = np.trace(Pp @ np.linalg.matrix_power(Fs, 4)).real
    t4_V = np.trace(np.linalg.matrix_power(Fv, 4)).real
    t2_V_r = t2_V.real
    pred_t4_Splus = 2.0 ** (n - 5) * (0.75 * t2_V_r ** 2 - t4_V)
    out["t4_Splus_numpy"] = float(t4_Splus)
    out["t4_Splus_root_formula"] = float(pred_t4_Splus)
    out["quartic_rel_err"] = float(abs(t4_Splus - pred_t4_Splus) / (abs(t4_Splus) + 1e-30))
    out["index_ratio_ok"] = abs(out["index_ratio_T(S+)/T(V)"] - 2.0 ** (n - 4)) < 1e-6
    out["quartic_ok"] = out["quartic_rel_err"] < 1e-6
    return out


# ===========================================================================
# 3. Sp(2n) explicit-matrix sanity for the fundamental octic.
# ===========================================================================
def explicit_sp_fundamental_traces(n, xs_int):
    """Build a Cartan element of sp(2n) in the 2n-dim fundamental and check
    tr F^{2m} = 2 (-1)^m sum x_j^{2m} for m=1..4 (numpy vs elementary)."""
    diag = [1j * x for x in xs_int] + [-1j * x for x in xs_int]
    F = np.diag(diag).astype(complex)
    # verify F is in sp(2n): F^T Omega + Omega F = 0, Omega = [[0,I],[-I,0]]
    I = np.eye(n)
    Omega = np.block([[np.zeros((n, n)), I], [-I, np.zeros((n, n))]])
    sp_defect = float(np.max(np.abs(F.T @ Omega + Omega @ F)))
    res = {"sp_defect": sp_defect}
    for m in range(1, 5):
        num = np.trace(np.linalg.matrix_power(F, 2 * m)).real
        elem = 2 * ((-1) ** m) * sum(x ** (2 * m) for x in xs_int)
        res[f"tr_F^{2*m}"] = (float(num), float(elem), abs(num - elem) < 1e-6)
    return res


# ===========================================================================
# 4. MAIN
# ===========================================================================
def main():
    print("=" * 84)
    print("LEG 2A  Sp(64) octic trace + local I_16 + Green-Schwarz factorizability")
    print("=" * 84)

    # ----------------------------------------------------------------------
    # CROSS-CHECK 1 (machinery validation BEFORE any Sp(64) number):
    #   SO(10)/SO(12) spinor index ratios + quartic, by root-formula AND explicit matrices,
    #   plus SO(N) adjoint primitive-coefficient reductions (N-2,N-8,N-32,N-128).
    # ----------------------------------------------------------------------
    print("\n[CROSS-CHECK 1a] SO(2n) spinor trace machinery: root-formula vs explicit Clifford")
    cc_ok = True
    for n in (5, 6):                                   # SO(10), SO(12)
        # --- root-formula decompositions (exact) ---
        c2, _ = decompose_trace(lambda xs: tr_spinor(xs, 1), 1, 1, n)
        c4, _ = decompose_trace(lambda xs: tr_spinor(xs, 2), 2, 2, n)
        ratio_root = c2[(1,)] / (tr_vector([Fr(1)] + [Fr(0)] * (n - 1), 1) / 1)  # not used directly
        # index ratio T(S+)/T(V) at order 2: tr_S F^2 = 2^{n-3} P1, tr_V F^2 = 2 P1
        idx_ratio = Fr(c2[(1,)], 2)                    # (coeff of P1 in tr_S)/(coeff in tr_V=2)
        # --- explicit-matrix cross-check ---
        ex = explicit_so_spinor_check(n)
        ok = (idx_ratio == Fr(2) ** (n - 4)) and ex["index_ratio_ok"] and ex["quartic_ok"]
        cc_ok = cc_ok and ok
        rep = {5: "SO(10) spinor=16", 6: "SO(12) spinor=32"}[n]
        print(f"  {rep}:")
        print(f"     tr_S F^2 = ({c2[(1,)]}) P1   tr_V F^2 = (2) P1   "
              f"=> T(S+)/T(V) = {idx_ratio} (root)  [predict 2^(n-4)={2**(n-4)}]")
        print(f"     tr_S F^4 = {fmt_poly(c4)}   (P2 primitive coeff = {c4.get((0,1), Fr(0))})")
        print(f"     explicit-matrix index ratio = {ex['index_ratio_T(S+)/T(V)']:.6f} "
              f"(predict {ex['index_ratio_predicted_2^(n-4)']:.0f}) "
              f"[{'OK' if ex['index_ratio_ok'] else 'FAIL'}]")
        print(f"     explicit-matrix quartic vs root-formula rel.err = {ex['quartic_rel_err']:.2e} "
              f"[{'OK' if ex['quartic_ok'] else 'FAIL'}]")
        print(f"     => {rep} machinery {'VALIDATED' if ok else 'FAILED'}")

    print("\n[CROSS-CHECK 1b] SO(N) adjoint primitive coefficient at orders 2,4,6,8")
    print("    (textbook GS reductions: (N-2),(N-8),(N-32),(N-128); N=32 kills order6, "
          "N=128 kills order8)")
    adj_ok = True
    for n in (5, 6, 8, 16, 64):                        # SO(10),12,16,32,128
        N = 2 * n
        line = [f"  SO({N}):"]
        for m, expect in ((1, N - 2), (2, N - 8), (3, N - 32), (4, N - 128)):
            cm, _ = decompose_trace(lambda xs: tr_adjoint_so(xs, m), m, m, max(n, m + 1))
            # primitive Casimir unit C_{2m} := tr_v F^{2m} = 2 P_m, so the coefficient in
            # textbook (vector-trace) units is (coeff of P_m)/2.
            prim = irreducible_part(cm) / 2
            good = (prim == Fr(expect))
            adj_ok = adj_ok and good
            line.append(f"ord{2*m}:prim={prim}(exp {expect}){'ok' if good else 'X'}")
        print("   ".join(line))
    print(f"  adjoint primitive-coefficient reductions all match textbook: {adj_ok}")

    machinery_ok = cc_ok and adj_ok
    print(f"\n  >>> TRACE MACHINERY VALIDATED (SO(10)/SO(12) + adjoint reductions): {machinery_ok}")
    assert machinery_ok, "trace machinery cross-check FAILED -- do not trust Sp(64) numbers"

    # ----------------------------------------------------------------------
    # (1) Sp(64) = Sp(2n), 2n=64, n=32: fundamental S=H^64 symmetric traces + octic split.
    # ----------------------------------------------------------------------
    print("\n" + "=" * 84)
    print("[Sp(64) FUNDAMENTAL  S = H^64  (2n=64, rank n=32)]  symmetric traces")
    print("=" * 84)
    nSp = 32
    # exact decompositions of the fundamental traces (weights {+-x_j}, j=1..32)
    sp_tr = {}
    for m in range(1, 5):
        cm, monos = decompose_trace(lambda xs: tr_vector(xs, m), m, m, nSp)
        sp_tr[m] = cm
        print(f"  Str_S F^{2*m:<2d} = {fmt_poly(cm)}")
    octic = sp_tr[4]
    prim8_P = irreducible_part(octic)         # coeff in P-units (= 2: Str_S F^8 = 2 P4)
    prim8 = prim8_P / 2                        # coeff in primitive Casimir units C_8 = tr_v F^8 = 2 P4
    reducible8 = {e: c for e, c in octic.items() if not (sum(e) == 1 and e[-1] == 1)}
    print("\n  OCTIC DECOMPOSITION  Str_S F^8 = [primitive C_8] + [products of lower Casimirs]")
    print("     (primitive Casimir unit C_8 := tr_v F^8 = 2 P4, the textbook/vector normalization):")
    print(f"     Str_S F^8 = {fmt_poly(octic)}  (in P-units)  =  ({prim8}) C_8  (in primitive units)")
    print(f"     primitive order-8 Casimir coefficient   = {prim8}  (C_8 units)  = {prim8_P} (P4 units)")
    print(f"     reducible (product) part                = "
          f"{fmt_poly(reducible8) if reducible8 else '0  (pure primitive)'}")

    # Is P4 an INDEPENDENT Casimir for rank 32?  Jacobian rank test of (P1,P2,P3,P4).
    def jac_rank(n):
        rng = np.random.RandomState(3)
        x = rng.rand(n) + 0.5
        J = np.zeros((4, n))
        for k in range(1, 5):           # P_k = sum x^{2k}; dP_k/dx_j = 2k x_j^{2k-1}
            J[k - 1, :] = 2 * k * x ** (2 * k - 1)
        return int(np.linalg.matrix_rank(J, tol=1e-9))
    rk32 = jac_rank(32)
    rk3 = jac_rank(3)                   # control: Sp(6) rank 3 -> P4 NOT independent
    print(f"\n  primitive-independence test (Jacobian rank of P1,P2,P3,P4):")
    print(f"     rank(n=32, Sp(64)) = {rk32}  (==4 => P4 independent => octic IRREDUCIBLE)")
    print(f"     control rank(n=3, Sp(6)) = {rk3}  (==3 => P4 reducible there; validates the test)")
    octic_irreducible = (prim8 != 0) and (rk32 == 4)
    assert rk3 == 3 and rk32 == 4, "Jacobian-rank irreducibility test self-check failed"
    print(f"     => Sp(64) fundamental octic has a NONZERO irreducible Casimir: {octic_irreducible}")

    # explicit 64x64 matrix sanity for the fundamental traces
    xs_int = list(range(1, nSp + 1))
    exsp = explicit_sp_fundamental_traces(nSp, xs_int)
    print(f"\n  explicit sp(64) Cartan-element check (64x64 matrices), sp-defect={exsp['sp_defect']:.1e}:")
    for m in range(1, 5):
        num, elem, ok = exsp[f"tr_F^{2*m}"]
        print(f"     tr F^{2*m:<2d}: numpy={num:.4g}  elementary 2*(-1)^{m}*sum x^{2*m}={elem:.4g}  "
              f"[{'OK' if ok else 'FAIL'}]")

    # ----------------------------------------------------------------------
    # (2)/(3) Assemble local I_16 irreducible content + factorizability boolean.
    # ----------------------------------------------------------------------
    print("\n" + "=" * 84)
    print("[LOCAL I_16 = [A-hat(TY14) . ch_S(F)]_16]  irreducible-channel assembly")
    print("=" * 84)

    # gravitational irreducible (primitive p4 ~ tr R^8) from the verified [A-hat]_16
    a16 = ahat.ahat_graded()[4]
    p4_grav = a16[(0, 0, 0, 1)]                          # -1/2419200, verified nonzero
    print(f"  gravitational irreducible: [A-hat(TY14)]_16 p4 coeff = {p4_grav}  (!= 0)")

    # assumed chiral content Omega^0(x)S^+ + Omega^1(x)S^- :
    #   form-bundle ranks  rank(Omega^p) = C(14,p):  Omega^0 -> 1, Omega^1 -> 14
    #   gravitational net chiral count  Ngrav = dim(S)*( (+1)*rank0 + (-1)*rank1 )
    #   gauge        net chiral weight  Wgauge =          (+1)*rank0 + (-1)*rank1
    from math import comb
    rank0, rank1 = comb(14, 0), comb(14, 1)             # 1, 14
    dimS = 64
    Wgauge = (+1) * rank0 + (-1) * rank1                 # = -13
    Ngrav = dimS * Wgauge                                # = -832
    print(f"  assumed content: Omega^0(x)S^+ (rank {rank0}, chir +1) + Omega^1(x)S^- "
          f"(rank {rank1}, chir -1)")
    print(f"     net gauge chiral weight   (n_+ - n_-) = {Wgauge}")
    print(f"     net gravitational count   dim(S)*(n_+ - n_-) = {Ngrav}")

    # ch_8(F) = (i/2pi)^8/8! tr_S F^8 ; i^8=1.  Irreducible gauge octic coefficient
    # (in units of (2pi)^{-8}) = Wgauge * (1/8!) * prim8 .
    from math import factorial
    gauge_irr = Fr(Wgauge) * Fr(1, factorial(8)) * prim8
    grav_irr = Fr(Ngrav) * p4_grav
    print(f"\n  IRREDUCIBLE degree-16 coefficients of the TOTAL local anomaly:")
    print(f"     gauge  tr_S F^8|prim  coeff (x (2pi)^-8) = Wgauge/8! * {prim8} = {gauge_irr}")
    print(f"     grav   tr R^8 (p4)    coeff             = Ngrav * {p4_grav}    = {grav_irr}")

    gauge_block = (gauge_irr != 0)
    grav_block = (grav_irr != 0)
    local_factorizable = (not gauge_block) and (not grav_block)
    print("\n  GREEN-SCHWARZ LOCAL FACTORIZABILITY:")
    print(f"     irreducible gauge octic present?         {gauge_block}")
    print(f"     irreducible gravitational tr R^8 present? {grav_block}")
    print(f"     ==> local_factorizable (CONDITIONAL)      = {local_factorizable}")

    # ----------------------------------------------------------------------
    print("\n" + "=" * 84)
    print("RESULT (CONDITIONAL -- read the honest scope)")
    print("=" * 84)
    print(f"  * Str_S F^8 (Sp(64) fundamental) = 2 P4 = 2 x (primitive order-8 Casimir),")
    print(f"    reducible/product part = 0; the primitive Casimir is INDEPENDENT at rank 32")
    print(f"    (Jacobian rank 4; control Sp(6) rank 3). So the gauge octic is IRREDUCIBLE.")
    print(f"  * Trace machinery cross-checked two ways on SO(10) (T(16)/T(10)=2) and SO(12)")
    print(f"    (T(32)/T(12)=4), plus SO(N) adjoint reductions (N-2,N-8,N-32,N-128): all PASS.")
    print(f"  * Under the assumed content Omega^0(x)S^+ + Omega^1(x)S^- and the (CONTESTED)")
    print(f"    Sp(64) gauge reading, BOTH irreducible channels are nonzero:")
    print(f"       gauge  tr_S F^8|prim coeff = {gauge_irr} != 0")
    print(f"       grav   tr R^8       coeff = {grav_irr} != 0")
    print(f"    => LOCAL I_16 does NOT Green-Schwarz factorize: local_factorizable = "
          f"{local_factorizable}.")
    print(f"  * This is NOT a cancellation/verdict claim. It is conditional on the assumed")
    print(f"    chiral content + the Sp(64)-vs-Sp(1) reading; the global eta/Dai-Freed/bordism")
    print(f"    leg stays OPEN. (A non-factorizable local anomaly is, if anything, a NEGATIVE")
    print(f"    result for anomaly-freedom under these assumptions -- under-claimed deliberately.)")
    print("=" * 84)

    return {
        "machinery_ok": machinery_ok,
        "Str_S_F8_primitive_coeff": str(prim8),
        "Str_S_F8_reducible_part": fmt_poly(reducible8) if reducible8 else "0",
        "octic_irreducible": octic_irreducible,
        "jacobian_rank_n32": rk32,
        "jacobian_rank_n3_control": rk3,
        "grav_p4_coeff": str(p4_grav),
        "Wgauge": Wgauge,
        "Ngrav": Ngrav,
        "gauge_irr_coeff": str(gauge_irr),
        "grav_irr_coeff": str(grav_irr),
        "local_factorizable_conditional": local_factorizable,
    }


if __name__ == "__main__":
    main()
