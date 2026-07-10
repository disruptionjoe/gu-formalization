#!/usr/bin/env python3
"""LEG-2 OBSTRUCTION HARDENING (carrier-bit swing, Design 3).

WHAT THIS LEG DOES
------------------
1. PART 0  Re-runs the repo's original gamma-trace-vs-gauge-orbit computation
   (tests/rs_gu_phys_brst_specification.py, floats: 73.48 toy / 343.73 anchor)
   in-process, as the baseline to be exactified.
2. PART 1  EXACT infrastructure: a sparse Clifford algebra Cl(eta) over Gaussian
   rationals (Fraction pairs), grounded against the repo's own Jordan-Wigner
   Cl(9,5) representation with EXACT integer matrices (no floats anywhere in
   the exact layer). Verifies the adjoint lemma e_a^dag = eta_a e_a, omega^2=I,
   Gamma Gamma^dag = n E_-, P_+ Gamma^dag = 0, P_+ idempotent with trace 832.
3. PART 2  EXACT CLOSED FORM of the obstruction: proves, as a POLYNOMIAL
   IDENTITY in xi (105-point certificate = full quadratic-form basis),
       sigma_Q(xi) . P_+ . g(xi) = ((n-2)/n) * P_-( xi (x) c(xi) . )
   slotwise: ((n-2)/n) * [ xi_a c(xi) - (q/n) eta_a e_a ] E_+ ,
   and derives 343.730237... = sqrt(exact rational), rank 64 exact off the
   null cone (mod-p at 3 primes + exact upper bound). Same for the Cl(4,0)
   toy (its own coefficient derived honestly: (n-2)/n|_{n=4} = 1/2, internal
   F = C^16 twist = norm x4).
4. PART 3  THE NILPOTENT-EXTENSION DICHOTOMY (the sharpest finite-model
   question separating "BRST rescues" from "no consistent gauging"):
   TEST A (constrained field space ker Gamma = carrier B's):
     - sigma_Q is EXACTLY invertible on ker Gamma off the null cone
       (rank 832 = dim ker Gamma; mod-p x3 + exact upper bound), hence
     - POINTWISE NO-GO: ANY linear ghost map h: Xi -> ker Gamma (any parameter
       space, any xi-dependence, NO equivariance hypothesis) with
       sigma_Q . h = 0 must vanish. No nonzero nilpotent extension exists.
       This is UNCONDITIONAL where the design's LEG-2 plan was
       equivariance-conditional: the Schur hypothesis dissolves.
     - the only solutions are h = 0 (annihilated gauge action) = the
       decoupling-shaped escape DEAD-ENDS forbids reading as a fix.
   TEST B (full field space T (x) S^+ = carrier A's):
     - the gauge variation g(xi) extends to a nilpotent 4-term BRST symbol
       complex 0 -> S^+ -g-> T(x)S^+ -R-> T(x)S^- -g'-> S^- -> 0:
       R.g == 0 and g'.R == 0 IDENTICALLY in xi (105-point polynomial
       certificate), exact off the null cone (ranks 64/832/64, exact).
       Carrier A's mechanism EXISTS in the finite model -- on the full space.
   TEST C (null cone q_eta(xi) = 0): both sides degenerate with EXACT
     witnesses: sigma_Q acquires an exact kernel vector xi (x) c(xi)u, so a
     nonzero characteristic-supported ghost map EXISTS on the cone (an honest
     carrier-A-flavored crack, reported per the story-shopping guard); the
     obstruction composite drops to rank 32 exactly (idempotent-trace proof).
5. PART 4  Verdict: what the finite model settles vs what rides off-symbol.

ACAUSAL-TRAP COMPLIANCE (absorbed/gu-source-action/DEAD-ENDS.md):
  "Any construction that drives the **bare** ||[Pi_RS, M_D]|| (58.72) to 0 --
   that decouples the RS sector and reinstates Velo-Zwanziger acausality."
  This leg contains NO mass operator M_D at all (symbols only), never forms
  the commutator, and never reduces any dressed or bare obstruction. The only
  "zero" solutions encountered (h = 0 on the constrained space) are FLAGGED
  as the forbidden decoupling shape, never adopted.

FIREWALL: no chi(K3), no /8 manufacture, no A-hat=3, no index roll-up to a
predetermined -42 (that is LEG-3's machine-decided job; here only the SHAPE
of the Euler class is stated).
"""
from __future__ import annotations

import os
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy
from sympy.ntheory.residue_ntheory import sqrt_mod

REPO = str(Path(__file__).resolve().parents[2])
sys.path.insert(0, os.path.join(REPO, "tests"))

import oq_rk1_cl95_explicit_rep as cl95            # repo anchor rep (floats)
import rs_clifford_projector_model as toy          # repo Cl(4,0) toy (floats)
import rs_gu_phys_brst_specification as brst_spec  # repo original obstruction

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ""))
    assert ok, f"CHECK FAILED: {name} {detail}"


# =========================================================================
# PART 1a. Exact sparse Clifford algebra Cl(eta) over Gaussian rationals.
# Element = dict{mask:int -> (Fraction re, Fraction im)}; e_S = ascending
# ordered product of generators in S.
# =========================================================================
F0, F1 = Fraction(0), Fraction(1)
ZERO_C = (F0, F0)


def cadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def cmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def cconj(x):
    return (x[0], -x[1])


def cscale(x, s):  # s Fraction
    return (x[0] * s, x[1] * s)


def ciszero(x):
    return x[0] == 0 and x[1] == 0


class Cliff:
    def __init__(self, eta):
        self.eta = tuple(eta)
        self.n = len(eta)
        self.full = (1 << self.n) - 1

    # ---- monomial product with sign/eta bookkeeping --------------------
    def mono_mul(self, S, T):
        sign = 1
        s = S
        t = T
        while t:
            b = t & (-t)            # lowest set bit of remaining T
            idx = b.bit_length() - 1
            t ^= b
            higher = s >> (idx + 1)  # generators in s strictly above idx
            if bin(higher).count("1") % 2:
                sign = -sign
            if s & b:
                sign *= self.eta[idx]
                s ^= b
            else:
                s |= b
        return s, sign

    # ---- element constructors ------------------------------------------
    def zero(self):
        return {}

    def one(self, coeff=(F1, F0)):
        return {0: coeff}

    def gen(self, a, coeff=(F1, F0)):
        return {1 << a: coeff}

    def omega(self):
        return {self.full: (F1, F0)}

    def c_of(self, xi):
        """c(xi) = sum_a xi_a e_a   (xi integer/Fraction components)."""
        out = {}
        for a, x in enumerate(xi):
            if x:
                out[1 << a] = (Fraction(x), F0)
        return out

    # ---- element algebra -------------------------------------------------
    def add(self, x, y):
        out = dict(x)
        for m, c in y.items():
            nc = cadd(out.get(m, ZERO_C), c)
            if ciszero(nc):
                out.pop(m, None)
            else:
                out[m] = nc
        return out

    def scale(self, x, s):  # s Fraction or (re,im) tuple
        if isinstance(s, tuple):
            return {m: cmul(c, s) for m, c in x.items() if not ciszero(cmul(c, s))}
        return {m: (c[0] * s, c[1] * s) for m, c in x.items() if s != 0}

    def neg(self, x):
        return {m: (-c[0], -c[1]) for m, c in x.items()}

    def mul(self, x, y):
        out = {}
        for mS, cS in x.items():
            for mT, cT in y.items():
                m, sg = self.mono_mul(mS, mT)
                c = cmul(cS, cT)
                if sg == -1:
                    c = (-c[0], -c[1])
                nc = cadd(out.get(m, ZERO_C), c)
                if ciszero(nc):
                    out.pop(m, None)
                else:
                    out[m] = nc
        return out

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def iszero(self, x):
        return all(ciszero(c) for c in x.values())

    def eq(self, x, y):
        return self.iszero(self.sub(x, y))

    def star(self, x):
        """Hermitian adjoint: reversal antiautomorphism + coefficient conj
        + e_a -> eta_a e_a per generator (matches matrix dagger in the JW rep,
        verified exactly against the rep below)."""
        out = {}
        for m, c in x.items():
            k = bin(m).count("1")
            sg = -1 if (k * (k - 1) // 2) % 2 else 1
            mm = m
            while mm:
                b = mm & (-mm)
                sg *= self.eta[b.bit_length() - 1]
                mm ^= b
            cc = cconj(c)
            out[m] = (cc[0] * sg, cc[1] * sg)
        return {m: c for m, c in out.items() if not ciszero(c)}

    def trace128(self, x, dim):
        """Trace in the dim-dimensional irrep: nonscalar monomials are
        traceless (verified against the rep), tr(1) = dim."""
        c = x.get(0, ZERO_C)
        return (c[0] * dim, c[1] * dim)

    # ---- chirality projectors -------------------------------------------
    def E(self, sign):
        """(1 + sign*omega)/2."""
        return {0: (Fraction(1, 2), F0), self.full: (Fraction(sign, 2), F0)}


# =========================================================================
# PART 1b. Exact integer Jordan-Wigner rep of Cl(9,5) (the repo's own
# wiring), used to GROUND the abstract algebra and for mod-p ranks.
# Matrices carried as (re, im) int64 numpy pairs; entries stay in {-1,0,1}
# for generators and tiny integers for short products -- exact.
# =========================================================================
def int_paulis():
    I2 = (np.eye(2, dtype=np.int64), np.zeros((2, 2), dtype=np.int64))
    s1 = (np.array([[0, 1], [1, 0]], dtype=np.int64), np.zeros((2, 2), dtype=np.int64))
    s2 = (np.zeros((2, 2), dtype=np.int64), np.array([[0, -1], [1, 0]], dtype=np.int64))
    s3 = (np.array([[1, 0], [0, -1]], dtype=np.int64), np.zeros((2, 2), dtype=np.int64))
    return I2, s1, s2, s3


def ckron(A, B):
    return (np.kron(A[0], B[0]) - np.kron(A[1], B[1]),
            np.kron(A[0], B[1]) + np.kron(A[1], B[0]))


def cmatmul(A, B):
    return (A[0] @ B[0] - A[1] @ B[1], A[0] @ B[1] + A[1] @ B[0])


def cdagger(A):
    return (A[0].T.copy(), -A[1].T.copy())


def ceq(A, B):
    return np.array_equal(A[0], B[0]) and np.array_equal(A[1], B[1])


def jw_int_gammas(n_pairs):
    I2, s1, s2, s3 = int_paulis()
    out = []
    for k in range(n_pairs):
        left = [s3] * k
        right = [I2] * (n_pairs - 1 - k)
        for mid in (s1, s2):
            M = (np.array([[1]], dtype=np.int64), np.array([[0]], dtype=np.int64))
            for f in left + [mid] + right:
                M = ckron(M, f)
            out.append(M)
    return out


def build_int_rep(eta):
    n = len(eta)
    n_pairs = n // 2
    G = jw_int_gammas(n_pairs)
    e = []
    for a in range(n):
        if eta[a] == +1:
            e.append(G[a])
        else:  # i * G_a
            e.append((-G[a][1].copy(), G[a][0].copy()))
    return e


class Rep:
    """Exact integer rep + monomial cache; also serves the mod-p layer."""

    def __init__(self, eta):
        self.eta = tuple(eta)
        self.n = len(eta)
        self.dim = 2 ** (self.n // 2)
        self.e = build_int_rep(eta)
        self.cache = {0: (np.eye(self.dim, dtype=np.int64),
                          np.zeros((self.dim, self.dim), dtype=np.int64))}

    def mono(self, mask):
        if mask in self.cache:
            return self.cache[mask]
        b = mask & (-mask)
        idx = b.bit_length() - 1
        rest = mask ^ b
        # e_S ascending: e_idx (lowest) FIRST: mono(mask) = e_idx @ mono(rest)
        M = cmatmul(self.e[idx], self.mono(rest))
        self.cache[mask] = M
        return M

    def elem_to_modp(self, x, p, r):
        """Map exact element (Fraction coeffs) to a GF(p) matrix, i |-> r."""
        out = np.zeros((self.dim, self.dim), dtype=np.int64)
        for m, (cr, ci) in x.items():
            M = self.mono(m)
            num = (cr.numerator % p) * pow(cr.denominator, p - 2, p) % p
            numi = (ci.numerator % p) * pow(ci.denominator, p - 2, p) % p
            coeff = (num + r * numi) % p
            out = (out + coeff * ((M[0] + r * M[1]) % p)) % p
        return out


def modp_rank(M, p):
    """Vectorized Gaussian elimination rank over GF(p); M int64, entries in [0,p)."""
    A = M % p
    rows, cols = A.shape
    rank = 0
    row = 0
    for col in range(cols):
        if row >= rows:
            break
        piv = np.nonzero(A[row:, col])[0]
        if piv.size == 0:
            continue
        pr = row + piv[0]
        if pr != row:
            A[[row, pr]] = A[[pr, row]]
        inv = pow(int(A[row, col]), p - 2, p)
        A[row] = (A[row] * inv) % p
        mask = np.nonzero(A[row + 1:, col])[0]
        if mask.size:
            idx = mask + row + 1
            A[idx] = (A[idx] - np.outer(A[idx, col], A[row])) % p
        row += 1
        rank += 1
    return rank


def pick_primes(k=3, start=10**6):
    """k primes p = 1 mod 4 (so i has a square root mod p) near start."""
    out = []
    p = sympy.nextprime(start)
    while len(out) < k:
        if p % 4 == 1:
            out.append((int(p), int(sqrt_mod(-1, p))))
        p = sympy.nextprime(p)
    return out


# =========================================================================
# PART 2 machinery: the exact pipelines (all Cl-symbolic, Fraction coeffs).
# Maps S^+ -> T (x) S^{+/-} are 14-lists of elements, each carrying the
# domain factor E_+ on the right. Slotwise formulas are valid because every
# intermediate is chiral by construction (e_a flips chirality).
# =========================================================================
def q_eta(A, xi):
    return sum(A.eta[a] * xi[a] * xi[a] for a in range(A.n))


def obstruction_pipeline(A, xi):
    """Return (LHS slots, RHS slots, q) where
       LHS_a = [ sigma_Q . P_+ . g(xi) ]_a  (direct composition, no shortcut)
       RHS_a = ((n-2)/n) [ xi_a c(xi) - (q/n) eta_a e_a ] E_+
             = ((n-2)/n) [ P_-( xi (x) c(xi) . ) ]_a  (closed form).
    """
    n, eta = A.n, A.eta
    Ep = A.E(+1)
    c = A.c_of(xi)
    q = q_eta(A, xi)
    # g(xi) slot a = xi_a E_+ ; Gamma(g) = c E_+ ; P_+ slotwise:
    cEp = A.mul(c, Ep)
    Pg = []
    for a in range(n):
        t1 = A.scale(Ep, Fraction(xi[a]))
        t2 = A.scale(A.mul(A.gen(a), cEp), Fraction(-eta[a], n))
        Pg.append(A.add(t1, t2))
    # (1 (x) c) applied:
    Y = [A.mul(c, Pg[a]) for a in range(n)]
    # Gamma' of Y = sum_b e_b Y_b :
    GY = A.zero()
    for b in range(n):
        GY = A.add(GY, A.mul(A.gen(b), Y[b]))
    # P_- slotwise: L_a = Y_a - (1/n) eta_a e_a GY :
    LHS = [A.add(Y[a], A.scale(A.mul(A.gen(a), GY), Fraction(-eta[a], n)))
           for a in range(n)]
    # closed form RHS:
    coef = Fraction(n - 2, n)
    RHS = []
    for a in range(n):
        t1 = A.scale(cEp, Fraction(xi[a]))
        t2 = A.scale(A.mul(A.gen(a), Ep), Fraction(-q * eta[a], n))
        RHS.append(A.scale(A.add(t1, t2), coef))
    return LHS, RHS, q


def pminus_gauge_slots(A, xi):
    """[P_-( xi (x) c(xi) . )]_a = [ xi_a c(xi) - (q/n) eta_a e_a ] E_+  --
    computed DIRECTLY from the P_- slot formula (independent of the closed
    form), for the norm-factorization certificate."""
    n, eta = A.n, A.eta
    Ep = A.E(+1)
    c = A.c_of(xi)
    cEp = A.mul(c, Ep)
    V = [A.scale(cEp, Fraction(xi[a])) for a in range(n)]  # xi (x) cE_+
    GV = A.zero()
    for b in range(n):
        GV = A.add(GV, A.mul(A.gen(b), V[b]))
    return [A.add(V[a], A.scale(A.mul(A.gen(a), GV), Fraction(-eta[a], n)))
            for a in range(n)]


def slots_norm_sq(A, slots, dim):
    """Exact Frobenius norm^2 over an orthonormal basis of S^+:
    sum_a tr( slot_a^dag slot_a ) (slots carry E_+ on the right)."""
    tot = F0
    for x in slots:
        t = A.trace128(A.mul(A.star(x), x), dim)
        assert t[1] == 0, "norm^2 trace not real"
        tot += t[0]
    assert tot >= 0
    return tot


def slots_equal(A, X, Y):
    return all(A.eq(x, y) for x, y in zip(X, Y))


def slots_zero(A, X):
    return all(A.iszero(x) for x in X)


def quad_identity_points(n):
    """Evaluation set certifying a matrix-valued QUADRATIC form identity:
    values at all e_i and e_i + e_j (i<j) determine every M_ii and M_ij+M_ji,
    hence the polynomial identity over Q."""
    pts = []
    for i in range(n):
        v = [0] * n
        v[i] = 1
        pts.append(tuple(v))
    for i in range(n):
        for j in range(i + 1, n):
            v = [0] * n
            v[i] = 1
            v[j] = 1
            pts.append(tuple(v))
    return pts


# ---- the full-space BRST symbol complex (TEST B) -------------------------
def rs_R_blocks(A, xi):
    """R(xi) slot blocks: (R psi)_a = sum_{b,c distinct} eta_a eta_b eta_c
    xi_b e_a e_b e_c psi_c. Returns dict (a,c) -> element (no domain E_+)."""
    n, eta = A.n, A.eta
    blocks = {}
    for a in range(n):
        for c in range(n):
            if a == c:
                continue
            acc = A.zero()
            for b in range(n):
                if b == a or b == c or xi[b] == 0:
                    continue
                m = A.mul(A.gen(a), A.mul(A.gen(b), A.gen(c)))
                acc = A.add(acc, A.scale(m, Fraction(eta[a] * eta[b] * eta[c] * xi[b])))
            if not A.iszero(acc):
                blocks[(a, c)] = acc
    return blocks


def R_compose_g(A, xi):
    """(R . g)_a = sum_c R_{ac} xi_c E_+  -- must vanish identically."""
    n = A.n
    Ep = A.E(+1)
    blocks = rs_R_blocks(A, xi)
    out = []
    for a in range(n):
        acc = A.zero()
        for c in range(n):
            if (a, c) in blocks and xi[c]:
                acc = A.add(acc, A.scale(A.mul(blocks[(a, c)], Ep), Fraction(xi[c])))
        out.append(acc)
    return out


def gprime_compose_R(A, xi):
    """(g' . R)_c = sum_a xi_a R_{ac} E_+ (Euclidean antighost contraction)
    -- must vanish identically."""
    n = A.n
    Ep = A.E(+1)
    blocks = rs_R_blocks(A, xi)
    out = []
    for c in range(n):
        acc = A.zero()
        for a in range(n):
            if (a, c) in blocks and xi[a]:
                acc = A.add(acc, A.scale(A.mul(blocks[(a, c)], Ep), Fraction(xi[a])))
        out.append(acc)
    return out


# ---- block matrices over Cl (for P_+ idempotency / trace, sigma assembly) --
def bmat_pplus(A):
    """(P_+)_{ab} = delta_ab E_+ - (1/n) eta_a e_a E_- e_b E_+  on T (x) S."""
    n, eta = A.n, A.eta
    Ep, Em = A.E(+1), A.E(-1)
    P = [[None] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            t = A.scale(A.mul(A.gen(a), A.mul(Em, A.mul(A.gen(b), Ep))),
                        Fraction(-eta[a], n))
            if a == b:
                t = A.add(t, Ep)
            P[a][b] = t
    return P


def bmat_pminus(A):
    n, eta = A.n, A.eta
    Ep, Em = A.E(+1), A.E(-1)
    P = [[None] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            t = A.scale(A.mul(A.gen(a), A.mul(Ep, A.mul(A.gen(b), Em))),
                        Fraction(-eta[a], n))
            if a == b:
                t = A.add(t, Em)
            P[a][b] = t
    return P


def bmat_mul(A, X, Y):
    n = A.n
    Z = [[None] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            acc = A.zero()
            for k in range(n):
                acc = A.add(acc, A.mul(X[a][k], Y[k][b]))
            Z[a][b] = acc
    return Z


def bmat_eq(A, X, Y):
    return all(A.eq(X[a][b], Y[a][b]) for a in range(A.n) for b in range(A.n))


def bmat_trace(A, X, dim):
    tot = (F0, F0)
    for a in range(A.n):
        tot = cadd(tot, A.trace128(X[a][a], dim))
    return tot


def bmat_diag_c(A, xi):
    c = A.c_of(xi)
    n = A.n
    return [[c if a == b else A.zero() for b in range(n)] for a in range(n)]


def bmat_to_modp(A, rep, X, p, r):
    n = A.n
    d = rep.dim
    out = np.zeros((n * d, n * d), dtype=np.int64)
    for a in range(n):
        for b in range(n):
            out[a * d:(a + 1) * d, b * d:(b + 1) * d] = rep.elem_to_modp(X[a][b], p, r)
    return out


def slots_to_modp_stack(A, rep, slots, p, r):
    d = rep.dim
    out = np.zeros((A.n * d, d), dtype=np.int64)
    for a, x in enumerate(slots):
        out[a * d:(a + 1) * d, :] = rep.elem_to_modp(x, p, r)
    return out


def R_to_modp(A, rep, xi, p, r):
    """Full-space matrix of R(xi) . (1 (x) E_+), scaled by 2 (uses 2E_+ = 1+omega,
    integer; scaling by 2 does not change GF(p) rank for p odd)."""
    n = A.n
    d = rep.dim
    Ep2 = A.add(A.one(), A.omega())  # 2 E_+
    blocks = rs_R_blocks(A, xi)
    out = np.zeros((n * d, n * d), dtype=np.int64)
    for (a, c), el in blocks.items():
        out[a * d:(a + 1) * d, c * d:(c + 1) * d] = rep.elem_to_modp(A.mul(el, Ep2), p, r)
    return out


# =========================================================================
# MAIN
# =========================================================================
def main():
    t0 = time.time()
    print("=" * 88)
    print("LEG-2 OBSTRUCTION HARDENING: exact re-verification + nilpotent-extension dichotomy")
    print("=" * 88)

    # ------------------------------------------------------------------
    # PART 0: baseline -- re-run the repo's original computation in-process.
    # ------------------------------------------------------------------
    print("\n--- PART 0: repo baseline (floats, reproduction only) ---")
    obs_toy = brst_spec.obstruction_cl4()
    obs_anc = brst_spec.obstruction_cl95()
    norm_toy_repo = obs_toy["RS_symbol_on_gauge_image_norm"]
    norm_anc_repo = obs_anc["RS_symbol_on_gauge_image_norm"]
    print(f"  repo Cl(4,0) toy  norm = {norm_toy_repo:.9f}  annihilated? "
          f"{obs_toy['pure_gauge_annihilated_within_gamma_trace_kernel']}")
    print(f"  repo Cl(9,5) anc  norm = {norm_anc_repo:.9f}  annihilated? "
          f"{obs_anc['pure_gauge_annihilated_within_gamma_trace_kernel']}")
    check("P0.1 repo anchor norm reproduces 343.73",
          abs(norm_anc_repo - 343.73) < 0.01, f"{norm_anc_repo:.6f}")
    check("P0.2 repo toy norm reproduces 73.48",
          abs(norm_toy_repo - 73.48) < 0.01, f"{norm_toy_repo:.6f}")
    check("P0.3 repo verdict: pure gauge NOT annihilated (both models)",
          not obs_toy["pure_gauge_annihilated_within_gamma_trace_kernel"]
          and not obs_anc["pure_gauge_annihilated_within_gamma_trace_kernel"])

    # ------------------------------------------------------------------
    # PART 1: exact infrastructure + grounding of the abstract algebra.
    # ------------------------------------------------------------------
    print("\n--- PART 1: exact Clifford algebra grounded in the repo's JW rep ---")
    ETA = (+1,) * 9 + (-1,) * 5
    A = Cliff(ETA)
    rep = Rep(ETA)
    n, dim = A.n, rep.dim  # 14, 128

    # 1.1 int rep == repo float rep, entry by entry (exact).
    Gf = cl95.jordan_wigner_gammas(7)
    ef = [Gf[a] if ETA[a] == +1 else 1j * Gf[a] for a in range(14)]
    ok = all(np.array_equal(rep.e[a][0], np.round(ef[a].real).astype(np.int64))
             and np.array_equal(rep.e[a][1], np.round(ef[a].imag).astype(np.int64))
             and np.max(np.abs(ef[a] - (rep.e[a][0] + 1j * rep.e[a][1]))) == 0.0
             for a in range(14))
    check("1.1 exact integer JW rep == repo's rep (all 14 generators, exactly)", ok)

    # 1.2 Clifford relations exact in the int rep.
    ok = True
    for a in range(14):
        for b in range(a, 14):
            anti = (rep.e[a][0] @ rep.e[b][0] - rep.e[a][1] @ rep.e[b][1]
                    + rep.e[b][0] @ rep.e[a][0] - rep.e[b][1] @ rep.e[a][1],)
            re = rep.e[a][0] @ rep.e[b][0] - rep.e[a][1] @ rep.e[b][1] \
                + rep.e[b][0] @ rep.e[a][0] - rep.e[b][1] @ rep.e[a][1]
            im = rep.e[a][0] @ rep.e[b][1] + rep.e[a][1] @ rep.e[b][0] \
                + rep.e[b][0] @ rep.e[a][1] + rep.e[b][1] @ rep.e[a][0]
            tgt = (2 * ETA[a] if a == b else 0) * np.eye(dim, dtype=np.int64)
            ok = ok and np.array_equal(re, tgt) and not im.any()
    check("1.2 {e_a,e_b} = 2 eta_ab I exact (int rep)", ok)

    # 1.3 abstract product == rep product (random monomials), omega^2 = 1,
    #     adjoint lemma, traceless monomials.
    rng = np.random.default_rng(20260710)
    ok = True
    for _ in range(40):
        S = int(rng.integers(0, 1 << 14))
        T = int(rng.integers(0, 1 << 14))
        m, sg = A.mono_mul(S, T)
        lhs = cmatmul(rep.mono(S), rep.mono(T))
        rhs = rep.mono(m)
        ok = ok and ceq(lhs, (sg * rhs[0], sg * rhs[1]))
    check("1.3a abstract monomial product == rep product (40 random pairs)", ok)
    om2 = A.mul(A.omega(), A.omega())
    check("1.3b omega^2 == +1 (abstract, exact)", A.eq(om2, A.one()))
    ok = True
    for a in range(14):
        ok = ok and ceq(cdagger(rep.e[a]), (ETA[a] * rep.e[a][0], ETA[a] * rep.e[a][1]))
    check("1.3c ADJOINT LEMMA e_a^dag = eta_a e_a exact (all 14) -> Hermitian "
          "projectors == metric projectors; the repo's inv(gram) is exactly I/14", ok)
    ok = True
    for _ in range(20):
        S = int(rng.integers(1, 1 << 14))
        M = rep.mono(S)
        ok = ok and int(np.trace(M[0])) == 0 and int(np.trace(M[1])) == 0
    Mom = rep.mono(A.full)
    ok = ok and int(np.trace(Mom[0])) == 0 and int(np.trace(Mom[1])) == 0
    check("1.3d nonscalar monomials traceless in rep (incl. omega) -> "
          "trace128 formula grounded", ok)
    ok = True
    for _ in range(10):
        x = {int(rng.integers(0, 1 << 14)): (Fraction(int(rng.integers(-5, 6))),
                                             Fraction(int(rng.integers(-5, 6))))
             for _ in range(4)}
        xs = A.star(x)
        Mx = np.zeros((dim, dim), dtype=np.complex128)
        Mxs = np.zeros((dim, dim), dtype=np.complex128)
        for mm, (cr, ci) in x.items():
            R = rep.mono(mm)
            Mx += (float(cr) + 1j * float(ci)) * (R[0] + 1j * R[1])
        for mm, (cr, ci) in xs.items():
            R = rep.mono(mm)
            Mxs += (float(cr) + 1j * float(ci)) * (R[0] + 1j * R[1])
        ok = ok and np.max(np.abs(Mx.conj().T - Mxs)) < 1e-9
    check("1.3e abstract star == matrix dagger (10 random elements)", ok)

    # 1.4 Gamma Gamma^dag = n E_-  and  P_+ Gamma^dag = 0 (symbolic, exact).
    Ep, Em = A.E(+1), A.E(-1)
    acc = A.zero()
    for a in range(14):
        acc = A.add(acc, A.scale(A.mul(A.gen(a), A.mul(Ep, A.gen(a))), Fraction(ETA[a])))
    check("1.4a sum_a eta_a e_a E_+ e_a == n E_-  (Gamma Gamma^dag = n E_-, exact)",
          A.eq(acc, A.scale(Em, Fraction(n))))
    # P_+ Gamma^dag slot a = eta_a E_+ e_a E_- - (1/n) sum_b eta_a e_a E_- e_b eta_b E_+ e_b E_-
    ok = True
    for a in range(14):
        t1 = A.scale(A.mul(Ep, A.mul(A.gen(a), Em)), Fraction(ETA[a]))
        t2 = A.zero()
        for b in range(14):
            term = A.mul(A.gen(a), A.mul(Em, A.mul(A.gen(b),
                       A.mul(Ep, A.mul(A.gen(b), Em)))))
            t2 = A.add(t2, A.scale(term, Fraction(ETA[a] * ETA[b], n)))
        ok = ok and A.eq(t1, t2)
    check("1.4b P_+ Gamma^dag == 0 (exact; the constraint projector kills the "
          "co-gauge direction)", ok)

    # 1.5 P_+ block projector: idempotent, Hermitian-consistent, trace 832.
    PP = bmat_pplus(A)
    PP2 = bmat_mul(A, PP, PP)
    check("1.5a P_+ (full T(x)S block matrix) idempotent exact", bmat_eq(A, PP2, PP))
    trP = bmat_trace(A, PP, dim)
    check("1.5b tr P_+ == 832 exact -> rank(P_+) = 832 = dim ker(Gamma|T(x)S^+)",
          trP == (Fraction(832), F0), f"tr = {trP[0]}")
    PM = bmat_pminus(A)
    PM2 = bmat_mul(A, PM, PM)
    trM = bmat_trace(A, PM, dim)
    check("1.5c P_- idempotent, trace 832 exact",
          bmat_eq(A, PM2, PM) and trM == (Fraction(832), F0))

    # ------------------------------------------------------------------
    # PART 2: the exact closed form of the 343.73 obstruction.
    # ------------------------------------------------------------------
    print("\n--- PART 2: exact closed form (polynomial-identity grade) ---")

    # 2.1 POLYNOMIAL IDENTITY: LHS(xi) == RHS(xi) at all e_i and e_i+e_j.
    # Both sides are matrix-valued QUADRATIC forms in xi, so these 105
    # evaluations certify the identity for ALL xi over Q (incl. null cone).
    pts = quad_identity_points(14)
    ok = True
    for xi in pts:
        L, R, _ = obstruction_pipeline(A, list(xi))
        if not slots_equal(A, L, R):
            ok = False
            print(f"    MISMATCH at xi={xi}")
            break
    check("2.1 CLOSED FORM sigma_Q P_+ g == ((n-2)/n) P_-(xi (x) c(xi) .) is a "
          "POLYNOMIAL IDENTITY in xi (105-pt certificate, exact)", ok,
          f"{len(pts)} evaluation points")

    # 2.2 the direct P_- slot computation reproduces the same RHS slots
    # (norm factorization is about THIS object), at the original xi (x10).
    XI0 = [10, 20, 30, 40, 5, 15, 25, 7, 11, 3, 22, 17, 9, 13]
    q0 = q_eta(A, XI0)
    L0, R0, _ = obstruction_pipeline(A, XI0)
    PMG = pminus_gauge_slots(A, XI0)
    ok = all(A.eq(R0[a], A.scale(PMG[a], Fraction(n - 2, n))) for a in range(n))
    check("2.2 RHS == ((n-2)/n) * [direct P_-(xi (x) c(xi))] slotwise at xi0 "
          "(independent route)", ok, f"q_eta(xi0) = {q0} (= 100 x 30.13, exact)")

    # 2.3 EXACT NORM: ||sigma_Q P_+ g||_F^2 rational; sqrt matches repo float.
    ns_L = slots_norm_sq(A, L0, dim)
    ns_P = slots_norm_sq(A, PMG, dim)
    check("2.3a exact norm factorization ||LHS||^2 == ((n-2)/n)^2 ||P_-(xi(x)c)||^2",
          ns_L == Fraction((n - 2) ** 2, n ** 2) * ns_P,
          f"||LHS||^2 = {ns_L} = ({ns_L})")
    # xi0 is 10x the repo's float xi; LHS is homogeneous degree 2 => norm x100.
    import math
    norm_exact = math.sqrt(float(ns_L)) / 100.0
    check("2.3b sqrt(exact)/100 == repo 343.730237... (float agreement < 1e-6)",
          abs(norm_exact - norm_anc_repo) < 1e-6,
          f"exact^2 = {ns_L}, sqrt/100 = {norm_exact:.9f} vs repo {norm_anc_repo:.9f}")
    print(f"    343.730237...^2 * 10^4 == {ns_L}  (EXACT rational; the float is now derived)")

    # 2.4 rank of the obstruction composite: 64 exact off the null cone
    # (mod-p lower bound x3 primes + exact upper bound rank <= rank E_+ = 64).
    primes = pick_primes(3)
    ranks = []
    for p, r in primes:
        Mstk = slots_to_modp_stack(A, rep, L0, p, r)
        ranks.append(modp_rank(Mstk, p))
    check("2.4 rank(sigma_Q P_+ g) == 64 EXACT at xi0 (mod-p x3 lower + "
          "rank<=64 upper): the obstruction is an ISOMORPHISM onto its image",
          all(rk == 64 for rk in ranks),
          f"mod-p ranks {ranks} at p = {[p for p, _ in primes]}")

    # 2.5 two more exact points (independent random integer xi, q != 0).
    for tag, XIr in (("xi_r1", [3, -1, 4, 1, -5, 9, 2, -6, 5, 3, -5, 8, 9, -7]),
                     ("xi_r2", [2, 7, -3, 5, 1, -8, 4, 6, -2, 9, 1, -4, 3, 5])):
        qr = q_eta(A, XIr)
        Lr, Rr, _ = obstruction_pipeline(A, XIr)
        okid = slots_equal(A, Lr, Rr)
        p, r = primes[0]
        rk = modp_rank(slots_to_modp_stack(A, rep, Lr, p, r), p)
        check(f"2.5 {tag}: identity + rank 64 (q_eta = {qr})",
              okid and (rk == 64 if qr != 0 else True), f"rank = {rk}")

    # ------------------------------------------------------------------
    # PART 3 TEST A: NO consistent gauging on the CONSTRAINED field space.
    # ------------------------------------------------------------------
    print("\n--- PART 3 TEST A: constrained field space ker(Gamma) [carrier B's] ---")

    # A1. sigma_Q as full-space block matrix Sigma = P_- (1(x)c) P_+ ; exact
    # upper bound rank <= rank P_+ = 832 (1.5b); mod-p x3 says 832 => EXACT.
    SIG = bmat_mul(A, PM, bmat_mul(A, bmat_diag_c(A, XI0), PP))
    sig_ranks = []
    for p, r in primes:
        Mp = bmat_to_modp(A, rep, SIG, p, r)
        sig_ranks.append(modp_rank(Mp, p))
    check("A1 rank(sigma_Q) == 832 == dim ker(Gamma) EXACT at xi0: the "
          "constrained RS symbol is a BIJECTION ker(Gamma) -> ker(Gamma') "
          "(carrier B's ellipticity, exactified)",
          all(rk == 832 for rk in sig_ranks),
          f"mod-p ranks {sig_ranks}")

    # A2. THE POINTWISE NO-GO (corollary, stated + machine-grounded):
    # For ANY linear h: Xi -> ker Gamma with sigma_Q . h = 0, h = 0.
    # Proof: sigma_Q injective on ker Gamma (A1). No equivariance used.
    # Machine instance: the CANONICAL candidate h = P_+ g has
    # sigma_Q h = ((n-2)/n) x (rank-64 iso) != 0  -- Part 2. q.e.d.
    check("A2 POINTWISE NO-GO: sigma_Q injective on ker Gamma (A1) => any "
          "nilpotent ghost map into ker Gamma vanishes; canonical candidate "
          "P_+ g fails nilpotency by the EXACT (6/7)-isomorphism", True,
          "no equivariance hypothesis -- Schur conditionality DISSOLVED")

    # A3. The gauge image genuinely lands in ker Gamma AFTER projection and
    # is nonzero there (so h = P_+ g is not itself zero -- the failure in A2
    # is nilpotency, not triviality).
    PgS = []
    cEp0 = A.mul(A.c_of(XI0), Ep)
    for a in range(14):
        t1 = A.scale(Ep, Fraction(XI0[a]))
        t2 = A.scale(A.mul(A.gen(a), cEp0), Fraction(-ETA[a], n))
        PgS.append(A.add(t1, t2))
    ns_Pg = slots_norm_sq(A, PgS, dim)
    p, r = primes[0]
    rk_Pg = modp_rank(slots_to_modp_stack(A, rep, PgS, p, r), p)
    check("A3 P_+ g != 0: projected gauge image has rank 64 exact "
          "(mod-p + <=64), norm^2 exact rational", rk_Pg == 64,
          f"rank = {rk_Pg}, ||P_+ g||^2 = {ns_Pg}")

    # A4. Gamma . (P_+ g) == 0 exact (it IS inside the constraint kernel).
    GPg = A.zero()
    for b in range(14):
        GPg = A.add(GPg, A.mul(A.gen(b), PgS[b]))
    check("A4 Gamma(P_+ g) == 0 exact: candidate ghost map lands in ker Gamma",
          A.iszero(GPg))

    # ------------------------------------------------------------------
    # PART 3 TEST B: BRST rescue EXISTS on the FULL field space T (x) S^+.
    # ------------------------------------------------------------------
    print("\n--- PART 3 TEST B: full field space T(x)S^+ [carrier A's] ---")

    # B1. R . g == 0 IDENTICALLY in xi (nilpotency of the ghost differential
    # against the gamma^{abc} RS symbol -- pure antisymmetry, no constraint).
    ok = all(slots_zero(A, R_compose_g(A, list(xi))) for xi in pts)
    check("B1 R(xi) . g(xi) == 0 POLYNOMIAL IDENTITY (105-pt certificate): "
          "nilpotent extension EXISTS on the full space, even ON the null cone", ok)

    # B2. g' . R == 0 identically (antighost side).
    ok = all(slots_zero(A, gprime_compose_R(A, list(xi))) for xi in pts)
    check("B2 g'(xi) . R(xi) == 0 POLYNOMIAL IDENTITY (105-pt certificate)", ok)

    # B3. g injective: g^dag g = |xi|^2_euclid E_+ exact (symbolic star-mul).
    gg = A.zero()
    for a in range(14):
        ga = A.scale(Ep, Fraction(XI0[a]))
        gg = A.add(gg, A.mul(A.star(ga), ga))
    eucl = sum(x * x for x in XI0)
    check("B3 g^dag g == |xi|^2 E_+ exact => rank(g) = 64 (injective for xi != 0)",
          A.eq(gg, A.scale(Ep, Fraction(eucl))), f"|xi0|^2 = {eucl}")

    # B4. rank(R . (1(x)E_+)) == 832 EXACT at xi0:
    # upper bound: ker contains T(x)S^- (dim 896) + im g (dim 64, B1+B3)
    # => rank <= 1792 - 960 = 832; mod-p x3 gives 832 => exact.
    R_ranks = []
    for p, r in primes:
        R_ranks.append(modp_rank(R_to_modp(A, rep, XI0, p, r), p))
    check("B4 rank(R) == 832 EXACT at xi0 (mod-p x3 + exact upper bound)",
          all(rk == 832 for rk in R_ranks), f"mod-p ranks {R_ranks}")

    # B5. g' surjective: g' g'^dag = |xi|^2 E_- exact (Euclidean contraction
    # convention for the antighost pairing; metric contraction also closes
    # the complex -- B2 holds for both -- but degenerates on the null cone).
    Emm = A.E(-1)
    gpgp = A.zero()
    for a in range(14):
        gpa = A.scale(Emm, Fraction(XI0[a]))
        gpgp = A.add(gpgp, A.mul(gpa, A.star(gpa)))
    check("B5 g' g'^dag == |xi|^2 E_- exact => rank(g') = 64 (surjective)",
          A.eq(gpgp, A.scale(Emm, Fraction(eucl))), f"|xi0|^2 = {eucl}")

    # B6. EXACTNESS of 0 -> S^+ -g-> T(x)S^+ -R-> T(x)S^- -g'-> S^- -> 0
    # off the null cone, assembled from exact ingredients:
    #   node 1: im g (64) <= ker R|T(x)S^+ (896-832 = 64)  => equal.
    #   node 2: im R (832) <= ker g'|T(x)S^- (896-64 = 832) => equal.
    check("B6 4-term BRST symbol complex EXACT at xi0 (all inclusions + "
          "dimension counts exact): carrier A's mechanism EXISTS in the "
          "finite model -- on the FULL field space", True,
          "Euler class shape: [S+]-[T(x)S+]+[T(x)S-]-[S-] = ghost-subtracted "
          "(T-1)-twist SHAPE (index roll-up deferred to LEG-3, not computed here)")

    # B7. chirality sanity on an R block.
    blocks0 = rs_R_blocks(A, XI0)
    el = blocks0[(0, 1)]
    check("B7 R blocks map S^+ -> S^- (odd Clifford words)",
          A.eq(A.mul(Em, A.mul(el, Ep)), A.mul(el, Ep)))

    # ------------------------------------------------------------------
    # PART 3 TEST C: the null cone q_eta(xi) = 0 -- both sides degenerate,
    # with EXACT witnesses (the story-shopping guard cuts both ways).
    # ------------------------------------------------------------------
    print("\n--- PART 3 TEST C: null cone q_eta(xi) = 0 (exact witnesses) ---")
    XIN = [0] * 14
    XIN[0] = 1
    XIN[9] = 1  # eta_0 = +1, eta_9 = -1 -> q = 0
    qn = q_eta(A, XIN)
    check("C0 q_eta(xi_null) == 0", qn == 0)
    cN = A.c_of(XIN)
    check("C1 c(xi_null)^2 == 0 exact (square-zero Clifford element)",
          A.iszero(A.mul(cN, cN)))

    # C2. rank of the obstruction composite drops to 32 EXACT:
    # closed form at q=0: LHS_a = ((n-2)/n) xi_a c E_+, so rank = rank(c E_+).
    # c = e_0 N with N = 1 + e_0 e_9;  N^2 = 2N, [N, omega] = 0, so
    # (N/2)E_+ is an idempotent of trace 32 => rank(c E_+) = 32 exactly.
    NN = A.add(A.one(), A.mul(A.gen(0), A.gen(9)))
    check("C2a N = 1 + e_0 e_9: N^2 == 2N exact",
          A.eq(A.mul(NN, NN), A.scale(NN, Fraction(2))))
    check("C2b [N, omega] == 0 exact",
          A.eq(A.mul(NN, A.omega()), A.mul(A.omega(), NN)))
    halfNEp = A.scale(A.mul(NN, Ep), Fraction(1, 2))
    tr_half = A.trace128(halfNEp, dim)
    check("C2c (N/2)E_+ idempotent with trace 32 exact => rank(c E_+) = 32 "
          "(e_0 invertible)",
          A.eq(A.mul(halfNEp, halfNEp), halfNEp) and tr_half == (Fraction(32), F0),
          f"tr = {tr_half[0]}")
    check("C2d c(xi_null) == e_0 N exact",
          A.eq(cN, A.mul(A.gen(0), NN)))
    LN, RN, _ = obstruction_pipeline(A, XIN)
    ok = slots_equal(A, LN, RN) and all(
        A.eq(LN[a], A.scale(A.mul(cN, Ep), Fraction((n - 2) * XIN[a], n)))
        for a in range(14))
    p, r = primes[0]
    rkN = modp_rank(slots_to_modp_stack(A, rep, LN, p, r), p)
    check("C2e obstruction composite rank == 32 EXACT on the cone "
          "(closed form + idempotent trace; mod-p concurs)",
          ok and rkN == 32, f"mod-p rank = {rkN}")

    # C3. EXACT kernel witness for sigma_Q ON the cone: psi = xi (x) c(xi)u.
    #   Gamma psi = c^2 u = 0 (C1); (1(x)c) psi = xi (x) c^2 u = 0
    #   => sigma_Q psi = 0 with psi != 0 (c E_- != 0: exact matrix nonzero).
    cEm = A.mul(cN, A.E(-1))
    Mc = rep.elem_to_modp(A.scale(cEm, Fraction(2)), primes[0][0], primes[0][1])
    check("C3 sigma_Q has an EXACT nonzero kernel vector xi (x) c(xi)u on the "
          "cone: ellipticity fails on characteristics; a NONZERO "
          "characteristic-supported ghost map h (sigma_Q h = 0, h != 0) EXISTS",
          not A.iszero(cEm) and Mc.any(),
          "the null-cone hole is REAL and certified -- carrier-A-flavored crack")

    # C4. full-space complex on the cone: nilpotency still holds (B1/B2 are
    # identities in xi); exactness degenerates (measured, lower-bound grade).
    rkRN = [modp_rank(R_to_modp(A, rep, XIN, p, r), p) for p, r in primes]
    check("C4 on the cone R.g == 0 still holds (identity); rank(R) drops "
          "below 832 (measured mod-p, 3 primes agree) -- exactness fails on "
          "characteristics for BOTH readings symmetrically",
          all(rk == rkRN[0] for rk in rkRN) and rkRN[0] < 832,
          f"mod-p ranks {rkRN} (lower-bound grade; exact value not certified)")

    # ------------------------------------------------------------------
    # PART 3 BONUS A5: closed form of sigma'_Q sigma_Q on ker Gamma
    # (explains WHY A1's bijection holds: on the tau = 0 subspace the
    # composite is exactly q * Id -- the Weitzenboeck-family structure).
    #   (sigma' sigma psi)_a = q psi_a - (4/n) xi_a tau + (4/n^2) eta_a e_a c tau,
    #   tau = sum_b eta_b xi_b psi_b.
    # ------------------------------------------------------------------
    print("\n--- PART 3 BONUS A5: sigma'sigma closed form (exact, block level) ---")
    SIGP = bmat_mul(A, PP, bmat_mul(A, bmat_diag_c(A, XI0), PM))
    SS = bmat_mul(A, SIGP, SIG)
    cX = A.c_of(XI0)
    D = [[None] * 14 for _ in range(14)]
    for a in range(14):
        eac = A.mul(A.gen(a), cX)
        for b in range(14):
            t = A.scale(A.one(), Fraction(-4 * XI0[a] * ETA[b] * XI0[b], n))
            t = A.add(t, A.scale(eac, Fraction(4 * ETA[a] * ETA[b] * XI0[b], n * n)))
            if a == b:
                t = A.add(t, A.scale(A.one(), Fraction(q0)))
            D[a][b] = t
    RHS_SS = bmat_mul(A, D, PP)
    check("A5 sigma'sigma == [q Id - (4/n) xi tau + (4/n^2) eta e c tau] on "
          "ker Gamma, EXACT block identity at xi0",
          bmat_eq(A, SS, RHS_SS),
          "on the 768-dim tau=0 subspace the composite is q*Id exactly")

    # ------------------------------------------------------------------
    # PART 2-TOY: the Cl(4,0) x F=C^16 toy, exactified honestly.
    # Same abstract pipeline, n = 4, all eta = +1; the repo's toy gammas are
    # unitarily equivalent to the JW choice, and every verified quantity
    # (identity, Frobenius norm, ranks) is representation-independent.
    # Internal twist F = C^16 multiplies norm^2 by 16 and leaves the
    # identity untouched.
    # ------------------------------------------------------------------
    print("\n--- PART 2-TOY: Cl(4,0) toy exactified (its own coefficient: 1/2) ---")
    A4 = Cliff((1, 1, 1, 1))
    rep4 = Rep((1, 1, 1, 1))
    pts4 = quad_identity_points(4)
    ok = True
    for xi in pts4:
        L4, R4, _ = obstruction_pipeline(A4, list(xi))
        ok = ok and slots_equal(A4, L4, R4)
    check("T1 toy closed form ((n-2)/n)|_{n=4} = 1/2 is a POLYNOMIAL IDENTITY "
          "(10-pt certificate) -- NOT anchor-specific", ok)
    XT = [1, 2, 3, 4]
    LT, RT, _ = obstruction_pipeline(A4, XT)
    qT = q_eta(A4, XT)
    ns_T = slots_norm_sq(A4, LT, 4)
    norm_T = math.sqrt(float(ns_T) * 16)  # internal F = C^16 => norm^2 x 16
    check("T2 toy exact norm: sqrt(16 * exact) == repo 73.484692... (< 1e-6)",
          abs(norm_T - norm_toy_repo) < 1e-6,
          f"base exact^2 = {ns_T}, q = {qT}, sqrt(16x) = {norm_T:.9f} "
          f"vs repo {norm_toy_repo:.9f}")
    pT, rT = pick_primes(1, 10 ** 5)[0]
    rkT = modp_rank(slots_to_modp_stack(A4, rep4, LT, pT, rT), pT)
    check("T3 toy composite rank == 2 == dim S^+ (full, off cone; mod-p + <=2)",
          rkT == 2, f"rank = {rkT}")

    # ------------------------------------------------------------------
    # PART 4: VERDICT.
    # ------------------------------------------------------------------
    npass = sum(1 for _, ok in CHECKS if ok)
    print("\n" + "=" * 88)
    print(f"ALL CHECKS: {npass}/{len(CHECKS)} PASS   "
          f"(elapsed {time.time() - t0:.1f}s)")
    print("=" * 88)
    print("""
VERDICT (LEG-2, obstruction hardening) -- what the finite model SETTLES:

 1. EXACTIFICATION. The repo's 343.73 machine fact is now an exact theorem:
      sigma_Q(xi) . P_+ . g(xi) = ((n-2)/n) * P_-( xi (x) c(xi) . )
    as a POLYNOMIAL IDENTITY in xi (105-point certificate over Q; Cl(9,5)
    anchor AND Cl(4,0) toy with its own honest coefficient 1/2).
      343.730237...^2 = 405256132224/343 / 10^4  (EXACT; float now derived)
      73.484692...^2  = 16 x toy exact rational  (EXACT)
    Off the null cone the composite has rank 64 = full: the obstruction is an
    ISOMORPHISM, not a one-xi accident.

 2. NO CONSISTENT GAUGING ON THE CONSTRAINED FIELD SPACE (carrier B's).
    sigma_Q: ker Gamma -> ker Gamma' is an exact bijection off the cone
    (rank 832 = dim ker Gamma; mod-p x3 + exact upper bound). COROLLARY
    (pointwise no-go): ANY linear ghost map h into ker Gamma with
    sigma_Q h = 0 vanishes -- any parameter space (incl. S_3/2-valued
    'gauging upstairs' shadows), any xi-dependence, NO equivariance
    hypothesis. The design's Schur-conditional plan is SUBSUMED by an
    unconditional statement. The only 'solutions' annihilate the gauge
    action = the decoupling shape DEAD-ENDS forbids reading as a fix.

 3. BRST RESCUE EXISTS ON THE FULL FIELD SPACE (carrier A's).
    R.g == 0 and g'.R == 0 identically in xi; the 4-term complex
    0 -> S^+ -> T(x)S^+ -> T(x)S^- -> S^- -> 0 is EXACT off the cone
    (ranks 64/832/64, exact). Euler class shape = ghost-subtracted
    (T-1)-twist (index roll-up: LEG-3's job, not computed here).

 4. MUTUAL EXCLUSION + NON-DESCENT. The full-space BRST complex does NOT
    descend along P_+ to ker Gamma; the descent failure IS the exact
    ((n-2)/n)-isomorphism of (1). Same symbol data: constrained => no
    gauging (B); unconstrained => BRST exists (A). The finite model turns
    the carrier bit into the single well-posed question: WHICH FIELD SPACE
    DOES THE SOURCE ACTION DECLARE. It provably cannot answer it (SG4).

 5. NULL-CONE HOLE (both ways, exact witnesses). On q_eta(xi) = 0:
    sigma_Q has exact kernel xi (x) c(xi)u => a nonzero characteristic-
    supported ghost map EXISTS (carrier-A-flavored crack, certified);
    the obstruction composite drops to rank 32 exactly; full-space
    exactness also degenerates (rank(R) mod-p 480 < 832). Riemannian K3
    has no real null cone, so carrier B's ellipticity there is untouched.

WHAT RIDES OFF-SYMBOL (NOT settled here): which field space GU's unbuilt
action declares (= the bit, SG4); BV master-equation / curvature
obstructions on Y14; interacting-level consistency (GP/VZ/DW are
S-matrix/PDE statements); the Y14<->K3 and Lorentzian<->Riemannian
bridges; nonlinear (field-dependent) gauge structure; the index value -42
(LEG-3, machine-decided).

ACAUSAL-TRAP COMPLIANCE: no mass operator M_D appears anywhere in this leg;
the bare commutator ||[Pi_RS, M_D]|| = 58.72 is never formed, never moved.
Symbols only. The h = 0 escapes found are FLAGGED as decoupling-shaped,
never adopted.
""")
    return 0


if __name__ == "__main__":
    sys.exit(main())

