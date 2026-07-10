#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LEG-A (SYMBOL LEG, decisive): adjudication of the -42 (pinned/AGW ghost-subtracted) vs -38
(geometric gamma-traceless Rarita-Schwinger) K-theory conventions on K3, at the SYMBOL level.

WHAT THIS SCRIPT PROVES (exact sympy over Q(i)[x1..x4, t]; polynomial IDENTITIES, no floats,
no numerics in any load-bearing step):

  Q1 (ELLIPTICITY). The compressed symbol sigma_Q(xi) of the gamma-traceless (Rarita-
      Schwinger) operator Q = P_{3/2} (D tensor 1) P_{3/2} on a 4-manifold satisfies
          det sigma_Q(xi) = kappa * (x1^2+x2^2+x3^2+x4^2)^3,   kappa != 0  (exact identity),
      hence sigma_Q(xi) is invertible for every real xi != 0:  Q IS ELLIPTIC.
      Basis-independent certificate: the Gram-corrected A^*A has annihilating polynomial
      (W - q)(W - q/4) = 0 with trace 9q/2  =>  eigenvalues q (mult 4), q/4 (mult 2)
      = the Weitzenboeck factors 1 and ((n-2)/n)^2 at n = 4.  (Ellipticity would fail only
      at n = 2 where (n-2)/n = 0.)

  Q2 (HOMOTOPY / ADDITIVITY). With respect to the twistor splitting
          S^{+-} tensor T_C = V^{+-} (+) iota(S^{-+}),   V^{+-} = ker(delta) rank 6,
      the full twisted-Dirac symbol c(xi) tensor 1_T has block form [[A, B],[C, E]] with
      B, C genuinely NONZERO (it is NOT block-diagonal), and the straight-line path
          sigma_t = [[A, (1-t)B],[(1-t)C, E]],  t in [0,1],
      satisfies det sigma_t = f(t) * q^4 with
          f(t)/f(0) = (1/16)[1 + 3(1-t)^2]^2   (exact identity),
      which has NO real roots at all, a fortiori none in [0,1].  The path stays elliptic:
          [sigma_full] = [sigma_Q] + [E-block]  in K-theory of elliptic symbols,
      so INDEX ADDITIVITY HOLDS.  NEGATIVE CONTROL: a deliberately wrong path (shrinking the
      diagonal blocks instead) provably LEAVES elliptic symbols at t = 1 -- the certificate
      is not vacuous.

  Q2b (WHAT THE EMBEDDED BLOCK IS). E == +(1/2) sigma(xi)^dag == -(1/2) * (the S- -> S+
      Clifford block), i.e. the embedded spin-1/2 block is the REVERSED-chirality Dirac
      symbol scaled by (2-n)/n = -1/2 (the Homma-Semmelmann matrix-form coefficient).
      Since -1/2 connects to 1 inside C\\{0}, [E-block] = [reversed-chirality Dirac].
      THIS is where -42 vs -38 forks: the geometric completion is +[1] (reversed), the
      physics ghost subtraction is -[1] (same chirality); they differ by 2*[Dirac].

  Q3 (EQUIVARIANCE). The unique order-3 spin lift of the Nikulin rotation (S+ trivial,
      S- weights zeta, zeta^2, tr(g|T_C) = -2) commutes with delta, iota, P, preserves the
      splitting, and satisfies  g_cod o sigma_t(xi) = sigma_t(g_T xi) o g_dom  for ALL t:
      the additivity is EQUIVARIANT.  tr(g|V+) - tr(g|V-) = -3 = (trS+ - trS-)(tr T_C + 1);
      the geometric multiplier tr(g|T_C) + 1 = -1 is NOT divisible by 3 (the structural
      kill mechanism of the pinned class, tr - 1 = -3 == 0 mod 3, is ABSENT here).

  CONSEQUENCE (index bookkeeping, exact Fractions; inputs sigma(K3) = -16, p1 = 3 sigma,
  prior-verified ind D = 2, ind_phi D = 2, nu_D = 1/3 -- NO chi(K3), NO A-hat = 3):
      ind(D tensor T_C) = ind(Q) + ind(reversed Dirac)  =>  ind Q = -40 - (-2) = -38,
      ind_phi(Q) = -4 - (-2) = -2 = 6 * (1/3) * (-1)  (Atiyah-Bott cross-check),
      residues: -38 == 1 mod 3 (geometric), -42 == 0 mod 3 (pinned); gap = 2 ind(D) = 4.

  WHAT ADDITIVITY DOES *NOT* LICENSE (BLOCKED, printed at the end): the identification of
  which object (A: ghost-subtracted gravitino complex, -42; B: geometric operator Q, -38)
  is the GU generation-arena carrier.  That is SG4 MISSING-CARRIER, not symbol arithmetic.
  This leg does NOT overturn the pinned -42; it proves the -38 thread is honest mathematics
  about a DIFFERENT (published) operator.

LITERATURE GATES (against the cached fetched texts in this directory, not memory):
  Homma-Semmelmann arXiv:1804.10602 (CMP 2019) Prop 3.1(i): n=4 ind Q = -19 A-hat = 19 sigma/8;
  Baer-Mazzeo arXiv:2003.11255 (CMP 2021): Q "formally self-adjoint first order elliptic".

FIREWALL: no chi(K3) = 24 input, no /8 manufacture (only the standard AS signature density
-sigma/8 as prior-verified canon), no A-hat = 3, and -38 is NEVER imported -- it falls out
of additivity as -40 + 2.

HOUSE STYLE: exact arithmetic; check()-asserts with global counter; BLOCKED items listed
honestly (they do not fail the run); exit 0 iff every hard assert passes.
"""
import sys, io, os, re
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import sympy as sp
from sympy import I, Rational, symbols, eye, zeros, Matrix, expand, cancel, Poly
from fractions import Fraction as F

NASSERT = 0
BLOCKED = []

def check(c, m):
    global NASSERT
    NASSERT += 1
    assert c, "FAIL[%d]: %s" % (NASSERT, m)

def blocked(m):
    BLOCKED.append(m)

def banner(t):
    print()
    print("=" * 96)
    print(t)
    print("=" * 96)

x1, x2, x3, x4, t = symbols("x1 x2 x3 x4 t", real=True)
XI = (x1, x2, x3, x4)
q = x1**2 + x2**2 + x3**2 + x4**2
GEN = {x1: 1, x2: 2, x3: 3, x4: 5}          # generic rational point (nonzero-witness only)

def dag(M):
    return M.conjugate().T

def is_zero_mat(M):
    return expand(M) == zeros(*M.shape)

# ============================================================================================
banner("A1. Clifford model on R^4 over Q(i): quaternionic sigma(xi); c(xi)^2 = -q; chirality")
# ============================================================================================
def sig(a, b, c_, d):
    """sigma(xi): S+ -> S- Clifford block; quaternion a + bi + cj + dk as 2x2 complex."""
    return Matrix([[a + I*b, c_ + I*d], [-c_ + I*d, a - I*b]])

SIG = [sig(*[1 if j == mu else 0 for j in range(4)]) for mu in range(4)]   # sigma(e_mu)
SIGX = sig(*XI)                                                            # sigma(xi)

check(expand(SIGX.det() - q) == 0, "det sigma(xi) = q = |xi|^2 (exact polynomial identity)")
check(is_zero_mat(dag(SIGX) * SIGX - q * eye(2)), "sigma^dag sigma = q * 1")
check(is_zero_mat(SIGX * dag(SIGX) - q * eye(2)), "sigma sigma^dag = q * 1")
for mu in range(4):
    for nu in range(4):
        anti = dag(SIG[mu]) * SIG[nu] + dag(SIG[nu]) * SIG[mu]
        check(anti == (2 * eye(2) if mu == nu else zeros(2, 2)),
              "Clifford relation on sigma blocks (%d,%d)" % (mu, nu))
# chiral c(xi) on S = S+ (+) S-:  c = [[0, -sigma^dag],[sigma, 0]];  c^2 = -q
CXI = Matrix(sp.BlockMatrix([[zeros(2, 2), -dag(SIGX)], [SIGX, zeros(2, 2)]]))
check(is_zero_mat(CXI * CXI + q * eye(4)), "c(xi)^2 = -|xi|^2 * 1_S (skew convention)")
check(is_zero_mat(CXI[:2, :2]) and is_zero_mat(CXI[2:, 2:]),
      "c(xi) is chirality-ODD: no S+ -> S+ or S- -> S- component (structural)")
print("  sigma(xi) quaternionic, det = q; c(xi)^2 = -q; Clifford contraction will be chirality-ODD")
print("  (chirality-oddness is the structural fact that FORCES the (T_C + 1) completion below)")

# ============================================================================================
banner("A2. Twistor splitting S^{+-} (x) T = V^{+-} (+) iota(S^{-+}): delta, iota, P; ranks 6+2")
# ============================================================================================
# Index ordering on S^{+-} (x) T: stacked (psi_1, psi_2, psi_3, psi_4), psi_mu in C^2; T slow.
# delta(psi (x) e_mu) = gamma^mu psi:  on S+ the gamma block is sigma_mu, on S- it is -sigma_mu^dag.
DELTA_P = Matrix(sp.BlockMatrix([[SIG[0], SIG[1], SIG[2], SIG[3]]]))                 # S+(x)T -> S-
DELTA_M = Matrix(sp.BlockMatrix([[-dag(SIG[0]), -dag(SIG[1]), -dag(SIG[2]), -dag(SIG[3])]]))
# iota(chi) = -(1/4) gamma_mu chi (x) e^mu
IOTA_P = Matrix(sp.BlockMatrix([[Rational(1, 4) * dag(SIG[mu])] for mu in range(4)]))  # S- -> S+(x)T
IOTA_M = Matrix(sp.BlockMatrix([[-Rational(1, 4) * SIG[mu]] for mu in range(4)]))      # S+ -> S-(x)T

check(is_zero_mat(DELTA_P * IOTA_P - eye(2)), "delta+ o iota = id on S- (normalization -(1/4), n=4)")
check(is_zero_mat(DELTA_M * IOTA_M - eye(2)), "delta- o iota = id on S+")
check(is_zero_mat(IOTA_P - Rational(1, 4) * dag(DELTA_P)),
      "iota = (1/4) delta^dag on the + side: the splitting is ORTHOGONAL")
check(is_zero_mat(IOTA_M - Rational(1, 4) * dag(DELTA_M)),
      "iota = (1/4) delta^dag on the - side")
P_P = eye(8) - IOTA_P * DELTA_P      # orthogonal projector onto V+ = ker(delta+)
P_M = eye(8) - IOTA_M * DELTA_M
check(is_zero_mat(P_P * P_P - P_P) and is_zero_mat(P_M * P_M - P_M), "P^2 = P (both sides)")
check(is_zero_mat(dag(P_P) - P_P) and is_zero_mat(dag(P_M) - P_M),
      "P^dag = P: ORTHOGONAL projectors (justifies the Gram-metric adjoint in A4)")
check(is_zero_mat(DELTA_P * P_P) and is_zero_mat(DELTA_M * P_M), "delta o P = 0 (gamma-traceless)")
check(is_zero_mat(P_P * IOTA_P) and is_zero_mat(P_M * IOTA_M), "P o iota = 0")
check(P_P.rank() == 6 and P_M.rank() == 6, "rank V^{+-} = 6 = 2*4 - 2")

VP = DELTA_P.nullspace(); VM = DELTA_M.nullspace()
check(len(VP) == 6 and len(VM) == 6, "nullspace bases of delta^{+-} have 6 vectors")
VPmat = Matrix.hstack(*VP); VMmat = Matrix.hstack(*VM)
check(VPmat.rank() == 6 and VMmat.rank() == 6, "V bases independent")
check(IOTA_P.rank() == 2 and IOTA_M.rank() == 2, "iota injective (rank 2)")
M_DOM = Matrix.hstack(VPmat, IOTA_P)      # adapted basis of S+ (x) T = [V+ | iota(S-)]
M_COD = Matrix.hstack(VMmat, IOTA_M)      # adapted basis of S- (x) T = [V- | iota(S+)]
detMD = M_DOM.det(); detMC = M_COD.det()
check(detMD != 0 and detMC != 0, "adapted bases invertible: the splitting is DIRECT, 8 = 6 + 2")
# K-class bookkeeping (ranks): [V+] - [V-] = ([S+] - [S-]) (x) (T_C + 1_C) requires the
# embedded copies to carry REVERSED chirality -- proven at the symbol level in A3 (E-block).
check(6 - 6 == (2 - 2) * (4 + 1), "K-class rank bookkeeping consistent (0 = 0)")
print("  V^{+-} = ker(delta) rank 6; iota(S^{-+}) rank 2; orthogonal direct splitting confirmed")

# ============================================================================================
banner("A3. Full twisted symbol in adapted bases: blocks [[A,B],[C,E]]; E = REVERSED Dirac * (-1/2)")
# ============================================================================================
# full symbol c(xi) (x) 1_T restricted to S+ (x) T -> S- (x) T: blockwise sigma(xi) (T slow)
SFULL = sp.diag(SIGX, SIGX, SIGX, SIGX)
M_COD_INV = M_COD.inv()
SANG = expand(M_COD_INV * SFULL * M_DOM)
A_blk = SANG[:6, :6]; B_blk = SANG[:6, 6:]; C_blk = SANG[6:, :6]; E_blk = SANG[6:, 6:]

B_gen = B_blk.subs(GEN); C_gen = C_blk.subs(GEN)
check(any(v != 0 for v in B_gen) and any(v != 0 for v in C_gen),
      "B, C GENUINELY NONZERO at a generic rational point: the twisted symbol is NOT "
      "block-diagonal -- the homotopy in A5 is doing real work")

# E-block identification: predicted ((2-n)/n) * [c(xi)|_{S- -> S+}] in the iota labels;
# n = 4: -(1/2) * (-sigma^dag) = +(1/2) sigma^dag.
check(is_zero_mat(E_blk - Rational(1, 2) * dag(SIGX)),
      "E == +(1/2) sigma(xi)^dag == -(1/2) * (S- -> S+ Clifford block): the embedded "
      "spin-1/2 block is the REVERSED-chirality Dirac symbol, coefficient (2-n)/n = -1/2 "
      "(Homma-Semmelmann eq.(1) matrix form)")
check(expand(E_blk.det() - Rational(1, 4) * q) == 0, "det E = q/4 (nonzero for xi != 0)")
# scalar connects to 1 in C*: phase path lam(s) = (1/2) exp(i pi (1-s)) from -1/2 to +1/2,
# |lam| = 1/2 > 0 throughout, then radial 1/2 -> 1.  Hence [E-block] = [reversed Dirac].
s_ = symbols("s", real=True)
lam = Rational(1, 2) * sp.exp(I * sp.pi * (1 - s_))
check(sp.simplify(lam.subs(s_, 0) + Rational(1, 2)) == 0 and
      sp.simplify(lam.subs(s_, 1) - Rational(1, 2)) == 0 and
      sp.simplify(sp.Abs(lam.subs(s_, Rational(1, 3))) - Rational(1, 2)) == 0,
      "-1/2 connects to +1/2 in C\\{0} (|lam| = 1/2 on the phase path); radial to 1: "
      "[E-block] = [REVERSED-chirality Dirac] in K-theory of symbols")
print("  E = (1/2) sigma^dag: REVERSED chirality confirmed at the symbol level.")
print("  => K-class [V+] - [V-] = ([S+] - [S-]) (x) (T_C + 1_C): the geometric completion is +1,")
print("     NOT the physics ghost subtraction -1.  This is the exact origin of -38 vs -42.")

# ============================================================================================
banner("A4. Q1 ELLIPTICITY: det sigma_Q = kappa q^3 (exact identity, kappa != 0); Gram certificate")
# ============================================================================================
detA = expand(A_blk.det())
qgen = q.subs(GEN)
kappa = sp.nsimplify(detA.subs(GEN) / qgen**3)
check(expand(detA - kappa * q**3) == 0,
      "det sigma_Q(xi) = kappa * q^3 as an EXACT POLYNOMIAL IDENTITY in (x1..x4)")
check(kappa != 0, "kappa != 0  =>  sigma_Q(xi) invertible for all real xi != 0: Q IS ELLIPTIC")
print("  det sigma_Q(xi) = %s * q^3  -- Q1 ANSWER: YES, ELLIPTIC (kappa is basis-dependent;" % kappa)
print("  'nonzero constant' is the basis-independent content)")

# Basis-independent certificate via the bundle metric (bases are NOT orthonormal; correct
# with Gram matrices; legitimate because the splitting is orthogonal, A2):
GP6 = dag(VPmat) * VPmat
GM6 = dag(VMmat) * VMmat
# positive-definiteness of the Grams (leading principal minors > 0) -- constant rational
for G6 in (GP6, GM6):
    for kk in range(1, 7):
        check(G6[:kk, :kk].det() > 0, "Gram matrix positive definite (minor %d)" % kk)
W = expand(GP6.inv() * dag(A_blk) * GM6 * A_blk)     # A^* A w.r.t. the true bundle metrics
check(is_zero_mat(expand(dag(GP6 * W) - GP6 * W)),
      "G+ W is Hermitian: W is self-adjoint w.r.t. the positive Gram => diagonalizable, real spec")
ANN = expand((W - q * eye(6)) * (W - Rational(1, 4) * q * eye(6)))
check(is_zero_mat(ANN), "(W - q)(W - q/4) = 0: spectrum of A^*A is contained in {q, q/4}")
trW = expand(W.trace())
check(expand(trW - Rational(9, 2) * q) == 0, "tr(A^*A) = 9q/2")
# multiplicities forced exactly: m1 + m2 = 6, m1*q + m2*q/4 = 9q/2  =>  m1 = 4, m2 = 2
m2 = F(6 - F(9, 2)) / F(1 - F(1, 4)); m1 = 6 - m2
check(m1 == 4 and m2 == 2, "eigenvalues q (mult 4) and q/4 (mult 2) -- FORCED by annihilator+trace")
L = symbols("L")
cp = expand(W.charpoly(L).as_expr())
check(expand(cp - (L - q)**4 * (L - Rational(1, 4) * q)**2) == 0,
      "charpoly(A^*A) = (L - q)^4 (L - q/4)^2 -- the basis-independent ellipticity certificate; "
      "factors 1 and ((n-2)/n)^2 = 1/4 match the published Weitzenboeck factors (n = 4)")
print("  charpoly(A^*A) = (L - q)^4 (L - q/4)^2; ellipticity degenerates only at n = 2 ((n-2)/n = 0)")

# ============================================================================================
banner("A5. Q2 HOMOTOPY: sigma_t = [[A,(1-t)B],[(1-t)C,E]]; det = f(t) q^4; NO roots in [0,1]")
# ============================================================================================
S_t = Matrix(sp.BlockMatrix([[A_blk, (1 - t) * B_blk], [(1 - t) * C_blk, E_blk]]))
detS = expand(S_t.det())
f_t = cancel(detS / q**4)
check(expand(detS - f_t * q**4) == 0,
      "det sigma_t = f(t) * q^4 as an EXACT IDENTITY in (x1..x4, t): all xi-dependence is q^4")
check(f_t.free_symbols <= {t}, "f depends on t only (SO(4)-invariance realized exactly)")
f0 = sp.nsimplify(f_t.subs(t, 0)); f1 = sp.nsimplify(f_t.subs(t, 1))
check(f0 != 0 and f1 != 0, "both endpoints elliptic: f(0) != 0 (full symbol), f(1) != 0 (diagonal)")
# endpoint cross-checks:
check(sp.simplify(f0 - detMD / detMC) == 0,
      "f(0) = det(M_dom)/det(M_cod): det(c(xi) tensor 1)|_{+ -> -} = q^4 exactly (c^2 = -q)")
check(sp.simplify(f1 - kappa * Rational(1, 4)) == 0,
      "f(1) = kappa * (1/4) = det A * det E / q^4: block-diagonal endpoint consistent")
# the load-bearing certificate: normalized f has the predicted closed form and NO real roots
fn = sp.nsimplify(expand(f_t / f0))
fn_pred = expand(Rational(1, 16) * (1 + 3 * (1 - t)**2)**2)
check(expand(fn - fn_pred) == 0,
      "f(t)/f(0) = (1/16)[1 + 3(1-t)^2]^2 EXACTLY -- the mixing-sector formula "
      "[(n-2)^2 + (4n-4)(1-t)^2]^2 / n^4 at n = 4 (basis-independent after normalization)")
fn_poly = Poly(fn, t)
rr = sp.real_roots(fn_poly)
check(rr == [], "f has NO real roots AT ALL (a fortiori none in [0,1])")
check(fn_poly.count_roots(0, 1) == 0, "Sturm count: zero roots in [0,1] (independent route)")
check(sp.nsimplify(fn.subs(t, 1)) == Rational(1, 16) and sp.nsimplify(fn.subs(t, 0)) == 1,
      "min of f/f(0) on [0,1] is 1/16 > 0 at t = 1; value 1 at t = 0")
print("  det sigma_t = f(t) q^4,  f(t)/f(0) = (1/16)[1 + 3(1-t)^2]^2 >= 1/16 > 0 on [0,1]")
print("  Q2 ANSWER: YES -- the path stays elliptic; [sigma_full] = [sigma_Q] + [E-block] in")
print("  K-theory of elliptic symbols  =>  INDEX ADDITIVITY IS CERTIFIED.")

# --- NEGATIVE CONTROL: a wrong path DOES leave elliptic symbols; the certificate detects it.
S_bad_end = Matrix(sp.BlockMatrix([[zeros(6, 6), B_blk], [C_blk, zeros(2, 2)]]))
check(expand(S_bad_end.det()) == 0,
      "NEGATIVE CONTROL: the path [[(1-t)A, B],[C, (1-t)E]] ends at [[0,B],[C,0]] with "
      "det == 0 identically (rank <= 4 < 8): that path LEAVES elliptic symbols at t = 1")
check(S_bad_end.subs(GEN).rank() <= 4, "rank of the bad endpoint <= 4 at a generic point")
print("  negative control: shrinking the DIAGONAL blocks instead kills ellipticity at t = 1 --")
print("  the determinant certificate distinguishes valid from invalid paths (not vacuous).")

# ============================================================================================
banner("A6. Q3 EQUIVARIANCE: order-3 spin lift; splitting and homotopy are g-equivariant")
# ============================================================================================
sq3 = sp.sqrt(3)
zeta = Rational(-1, 2) + sq3 / 2 * I                    # exact primitive cube root of unity
uL = sp.diag(zeta, sp.conjugate(zeta))                  # g on S- (weights zeta, zeta^2)
check(sp.expand(zeta**3 - 1) == 0 and sp.expand(zeta - 1) != 0, "zeta^3 = 1, zeta != 1")
check(is_zero_mat(sp.expand(uL * dag(uL) - eye(2))) and sp.expand(uL.det() - 1) == 0,
      "u_L in SU(2): the lift is special unitary")
check(is_zero_mat(sp.expand(uL**3 - eye(2))), "u_L has order 3 (odd order => unique spin lift)")
check(sp.expand(uL.trace() + 1) == 0, "tr(g|S-) = zeta + zeta^2 = -1;  g|S+ = 1 (trace 2)")
# rotation g_T defined by the intertwining sigma(g_T xi) = u_L sigma(xi) (g|S+ = 1):
c3, s3 = Rational(-1, 2), sq3 / 2
Rrot = Matrix([[c3, -s3], [s3, c3]])
GT = sp.diag(Rrot, Rrot)                                # (z1, z2) -> (zeta z1, zeta z2)
check(is_zero_mat(sp.expand(GT.T * GT - eye(4))) and sp.expand(GT.det() - 1) == 0,
      "g_T in SO(4)")
check(is_zero_mat(sp.expand(GT**3 - eye(4))), "g_T has order 3")
check(sp.expand(GT.trace() + 2) == 0,
      "tr(g|T) = -2 = tr(g|T_C): matches the verified Nikulin local weights (zeta, zeta^{-1})")
gxi = [sum(GT[i, j] * XI[j] for j in range(4)) for i in range(4)]
SUBG = dict(zip(XI, gxi))
check(is_zero_mat(sp.expand(SIGX.subs(SUBG, simultaneous=True) - uL * SIGX)),
      "INTERTWINING: sigma(g_T xi) = u_L sigma(xi) * (g|S+)^{-1} with g|S+ = 1 -- the unique "
      "order-3 spin lift with S+ trivial (the pinned canonical symplectic lift)")
gS = sp.diag(eye(2), uL)
check(is_zero_mat(sp.expand(gS * CXI * sp.diag(eye(2), uL**2) - CXI.subs(SUBG, simultaneous=True))),
      "g_S c(xi) g_S^{-1} = c(g_T xi) at the full Clifford level")
# g on S^{+-} (x) T (T slow in our ordering): kron(GT, g_S-block)
def kron(Aa, Bb):
    return Matrix(sp.kronecker_product(Aa, Bb))
gp8 = kron(GT, eye(2))          # on S+ (x) T
gm8 = kron(GT, uL)              # on S- (x) T
check(is_zero_mat(sp.expand(DELTA_P * gp8 - uL * DELTA_P)), "delta+ is g-equivariant")
check(is_zero_mat(sp.expand(DELTA_M * gm8 - DELTA_M)), "delta- is g-equivariant (S+ trivial)")
check(is_zero_mat(sp.expand(gp8 * IOTA_P - IOTA_P * uL)), "iota (+ side) is g-equivariant")
check(is_zero_mat(sp.expand(gm8 * IOTA_M - IOTA_M)), "iota (- side) is g-equivariant")
check(is_zero_mat(sp.expand(gp8 * P_P - P_P * gp8)) and is_zero_mat(sp.expand(gm8 * P_M - P_M * gm8)),
      "the twistor projectors commute with g: the splitting is phi-equivariant")
h_dom = sp.expand(M_DOM.inv() * gp8 * M_DOM)
h_cod = sp.expand(M_COD.inv() * gm8 * M_COD)
check(is_zero_mat(h_dom[:6, 6:]) and is_zero_mat(h_dom[6:, :6]) and
      is_zero_mat(h_cod[:6, 6:]) and is_zero_mat(h_cod[6:, :6]),
      "g is BLOCK-DIAGONAL in the adapted bases: g preserves V^{+-} and iota(S^{-+})")
check(is_zero_mat(sp.expand(h_dom[6:, 6:] - uL)) and is_zero_mat(sp.expand(h_cod[6:, 6:] - eye(2))),
      "g acts on the iota labels exactly as on S^{-+} (chirality-REVERSED labels confirmed "
      "equivariantly)")
trVp = sp.expand(h_dom[:6, :6].trace()); trVm = sp.expand(h_cod[:6, :6].trace())
check(sp.expand(trVp + 3) == 0, "tr(g|V+) = -3")
check(sp.expand(trVm) == 0, "tr(g|V-) = 0")
check(sp.expand((trVp - trVm) - (2 - (-1)) * (GT.trace() + 1)) == 0,
      "MULTIPLIER IDENTITY: tr(g|V+) - tr(g|V-) = (trS+ - trS-)(tr(g|T_C) + 1) = 3 * (-1) = -3")
# the WHOLE homotopy is g-equivariant (symbolic t):  h_cod sigma_t(xi) = sigma_t(g_T xi) h_dom
LHS = sp.expand(h_cod * S_t)
RHS = sp.expand(Matrix(S_t.subs(SUBG, simultaneous=True)) * h_dom)
check(is_zero_mat(sp.expand(LHS - RHS)),
      "EQUIVARIANCE OF THE HOMOTOPY: g o sigma_t(xi) = sigma_t(g_T xi) o g for ALL t in [0,1] "
      "=> index additivity holds EQUIVARIANTLY for the order-3 action")
# multipliers mod 3: the fork
c_geo = GT.trace() + 1; c_pin = GT.trace() - 1
check(sp.expand(c_geo + 1) == 0 and int(c_geo) % 3 != 0,
      "geometric multiplier tr(g|T_C) + 1 = -1: NOT divisible by 3 -- the structural kill "
      "mechanism of the pinned class is ABSENT for the geometric operator")
check(sp.expand(c_pin + 3) == 0 and int(c_pin) % 3 == 0,
      "pinned multiplier tr(g|T_C) - 1 = -3 == 0 mod 3 (why the pinned rho class is (0,0,0))")
print("  splitting and homotopy are g-equivariant; tr(g|V+) = -3, tr(g|V-) = 0;")
print("  multipliers: geometric -1 (mod 3: alive), pinned -3 (mod 3: killed)")

# ============================================================================================
banner("A7. INDEX BOOKKEEPING on K3 (exact Fractions; -38 DERIVED, never imported)")
# ============================================================================================
SIGMA_K3 = -16                       # prior-verified canon (K3 lattice signature (3,19))
P1 = 3 * SIGMA_K3                    # signature theorem p1 = 3 sigma; NO chi(K3) anywhere
AHAT = F(-SIGMA_K3, 8)               # standard AS density; = 2
check(AHAT == 2, "A-hat(K3) = 2 (from sigma alone; never 3)")
IND_D = int(AHAT)                    # ind(D: S+ -> S-) = +2  [prior-verified: ker+ = 2, ker- = 0]
IND_DT = 4 * IND_D + P1              # A-hat(ch T_C)[K3] = 4*A-hat + p1 = 8 - 48
check(IND_DT == -40, "ind(D tensor T_C) = -40 (= 5 p1/6)")
IND_REV = -IND_D                     # embedded block = REVERSED-chirality Dirac (A3/A6)
check(IND_REV == -2, "ind(D: S- -> S+) = -2")
IND_Q = IND_DT - IND_REV             # additivity CERTIFIED in A5
check(IND_Q == -38, "ind Q = -40 - (-2) = -38  (equivalently ind(D tensor T_C) + ind(D))")
check(F(19 * SIGMA_K3, 8) == -38 and -19 * int(AHAT) == -38,
      "matches Homma-Semmelmann Prop 3.1(i): ind Q = -19 A-hat = 19 sigma/8 -- and -38 was "
      "DERIVED from additivity, not imported")
check((-38) % 3 == 1 and (-42) % 3 == 0,
      "residues mod 3: geometric -38 == 1 (alive), pinned -42 == 0 (killed) -- the verdict fork")
check((-42) - (-38) == -2 * IND_D,
      "the two conventions differ by EXACTLY -2 ind(D): the +-1 orientation of the rank-2 "
      "spin-1/2 completion; both are internally coherent objects")
# equivariant bookkeeping (nu_D = 1/3 and ind_phi(D) = 2 are prior-verified canon):
NU_D = F(1, 3)
IND_PHI_D = 2
IND_PHI_DT = 6 * NU_D * (-2)         # Atiyah-Bott: 6 fixed points, tr(g|T_C) = -2
check(IND_PHI_DT == -4, "ind_phi(D tensor T_C) = 6 * (1/3) * (-2) = -4")
IND_PHI_Q = IND_PHI_DT - (-IND_PHI_D)  # equivariant additivity (certified in A6)
check(IND_PHI_Q == -2, "ind_phi(Q) = -4 - (-2) = -2")
check(6 * NU_D * (-1) == -2,
      "Atiyah-Bott direct route: ind_phi(Q) = 6 * nu_D * (tr(g|T_C) + 1) = 6*(1/3)*(-1) = -2 "
      "-- agrees with equivariant additivity (independent cross-check)")
print("  ind Q = -38 = 19 sigma / 8;  ind_phi(Q) = -2;  residue -38 == 1 mod 3")
print("  pinned rival: -42 = 21 sigma / 8, residue 0 mod 3; gap exactly 2 ind(D) = 4")

# ============================================================================================
banner("A8. LITERATURE GATES against the CACHED FETCHED TEXTS (this directory, not memory)")
# ============================================================================================
HERE = os.path.dirname(os.path.abspath(__file__))
def norm_txt(s):
    s = re.sub(r"\s+", "", s)
    return s.replace("ﬁ", "fi").replace("ﬀ", "ff").replace("ﬃ", "ffi")
try:
    hs_txt = norm_txt(io.open(os.path.join(HERE, "hs-rs-kernel.txt"), encoding="utf-8",
                              errors="replace").read())
    # normalized "(i) n = 4 : ind Q = -19 A-hat(M) = 19/8 sigma(M)"  (minus U+2212, hat U+02C6,
    # sigma U+03C3; the "198" is the PDF-extracted stacked fraction 19/8)
    HS_GATE = "(i)n=4:indQ=−19ˆA(M)=198σ(M)"
    check("Proposition3.1" in hs_txt and HS_GATE in hs_txt,
          "Homma-Semmelmann (arXiv:1804.10602, CMP 2019) Prop 3.1(i) present in the fetched "
          "text: 'n = 4: ind Q = -19 A-hat(M) = 19/8 sigma(M)' -- the PUBLISHED -38 on K3")
    print("  HS Prop 3.1(i) gate: PASS (ind Q = -19 A-hat = 19 sigma/8 at n = 4)")
except (OSError, IOError):
    blocked("HS cached text not found: Prop 3.1(i) gate not re-verified in this run "
            "(the internal -38 derivation above stands independently)")
    print("  HS gate: file missing -> BLOCKED note recorded")
try:
    bm_txt = norm_txt(io.open(os.path.join(HERE, "bm2020.txt"), encoding="utf-8",
                              errors="replace").read())
    BM_GATE = ("iscalledtheRarita-Schwingeroperator.Itisaformallyself-adjoint"
               "firstorderellipticdifferentialoperator")
    check(BM_GATE in bm_txt,
          "Baer-Mazzeo (arXiv:2003.11255, CMP 2021): 'Q ... is a formally self-adjoint first "
          "order elliptic differential operator' present in the fetched text -- the published "
          "ellipticity assertion our A4 re-proves at the symbol level")
    print("  BM ellipticity gate: PASS ('formally self-adjoint first order elliptic')")
except (OSError, IOError):
    blocked("BM cached text not found: published-ellipticity gate not re-verified in this run "
            "(the A4 symbol proof stands independently)")
    print("  BM gate: file missing -> BLOCKED note recorded")

# ============================================================================================
banner("A9. FIREWALL AUDIT + BLOCKED ITEMS + VERDICT")
# ============================================================================================
INPUTS = {"sigma(K3)": -16, "p1 = 3 sigma": -48, "ind D": 2, "ind_phi D": 2,
          "nu_D per point": F(1, 3), "fixed points": 6, "|G|": 3, "tr(g|T_C)": -2}
check(all(v != 24 for v in INPUTS.values()), "FIREWALL: chi(K3) = 24 never an input")
check(AHAT == 2, "FIREWALL: A-hat = 2, never 3; the only /8 is the standard AS signature density")
check(IND_Q == IND_DT + IND_D, "FIREWALL: -38 = -40 + 2 fell out of additivity; never targeted")
print("  firewall clean: inputs = %s" % {k: str(v) for k, v in INPUTS.items()})

# standing BLOCKED items (honest scope limits; they do NOT fail this run):
blocked("GLOBALIZATION: the certificates are pointwise/flat symbol algebra; they globalize "
        "because delta, iota, P are Spin(4)-natural bundle maps and ellipticity/homotopy/index "
        "are symbol-level (Atiyah-Singer). That naturality principle is standard but is NOT "
        "re-proven by this script.")
blocked("CARRIER IDENTIFICATION (the live gate): NOTHING here decides whether the GU "
        "generation-arena operator is (A) the ghost-subtracted gravitino complex "
        "[D tensor (T_C - 1)], index -42, rho classes (0,0,0), or (B) the geometric "
        "gamma-traceless operator Q, index -38, rho classes {0,1,2}/3 nonzero. Both are real, "
        "published, internally coherent objects differing by exactly 2*[Dirac]. This is the "
        "SG4 MISSING-CARRIER identification question -- a program decision, not arithmetic. "
        "This leg does NOT license replacing the pinned -42 in canon.")
blocked("ETA-LEVEL REALS: the symbol homotopy fixes the index and the mod-Z rho classes "
        "(APS III deformation invariance). The exact eta REALS of the honest operator Q ride "
        "the B-leg kernel data and lower-order-term conventions; only mod-Z classes are at "
        "adjudication grade from this leg's input.")
blocked("PRIMARY SOURCES: Homma-Semmelmann verified against the cached fetched arXiv text "
        "(this directory); the CMP journal version and the AGW primary (Nucl.Phys. B234, "
        "paywalled) were not re-fetched by this script.")

print()
print("#" * 96)
print("# LEG-A VERDICT (symbol adjudication of the -38 thread):")
print("#   Q1: sigma_Q IS ELLIPTIC.  det sigma_Q = kappa q^3, kappa != 0 (exact identity);")
print("#       Gram-certificate charpoly (L-q)^4 (L-q/4)^2 = Weitzenboeck factors 1, ((n-2)/n)^2.")
print("#   Q2: the full twisted-Dirac symbol IS homotopic through elliptic symbols to")
print("#       diag(sigma_Q, -(1/2) reversed-Dirac):  det sigma_t = f(t) q^4 with")
print("#       f/f(0) = (1/16)[1+3(1-t)^2]^2, NO real roots => ADDITIVITY CERTIFIED,")
print("#       g-EQUIVARIANTLY for the order-3 Nikulin action.  (Bad paths ARE detected.)")
print("#   LICENSED: ind(D tensor T_C) = ind Q + ind(reversed Dirac) => ind Q = -38 = 19 sigma/8")
print("#       (matches published HS Prop 3.1(i)); ind_phi(Q) = -2; geometric multiplier -1")
print("#       (not 0 mod 3) vs pinned -3 (0 mod 3): the order-3 verdict forks exactly here.")
print("#   NOT LICENSED: which object is the GU generation-arena carrier (SG4) -- see BLOCKED.")
print("#")
print("# BLOCKED items (%d):" % len(BLOCKED))
for i, b in enumerate(BLOCKED, 1):
    print("#   [%d] %s" % (i, b))
print("#")
print("# hard asserts passed: %d;  exit 0" % NASSERT)
print("#" * 96)
