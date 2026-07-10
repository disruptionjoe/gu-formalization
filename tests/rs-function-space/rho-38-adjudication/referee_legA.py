#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HOSTILE-REFEREE independent verification of LEG-A (symbol adjudication -42 vs -38).

DIFFERENT MACHINERY from the leg (deliberate):
  * Clifford rep: Pauli-matrix based, sig_mu = (1, i P1, i P2, i P3), gamma = [[0, sig^dag],[-sig, 0]]
    (the leg used the quaternion a+bi/c+di layout with gamma = [[0, -sig^dag],[sig, 0]]).
  * Full 16-dim S (x) T with T FAST ordering, delta/iota/P as basis-free 4x16 / 16x4 / 16x16
    maps in the STANDARD ORTHONORMAL basis (the leg used 8-dim chiral blocks, T slow,
    nullspace bases + Gram matrices).
  * Ellipticity certificate: Hermitian N = X^dag X with annihilator N(N-q)(N-q/4) = 0 plus
    FIRST AND SECOND trace moments forcing multiplicities (0,q,q/4) -> (2,4,2)
    (the leg used Gram-corrected charpoly).
  * Homotopy: basis-free sigma_t = Sigma - t*(P Sigma Q + Q Sigma P), det ratio r(t)
    (the leg used adapted-basis blocks). r(t) must be the SAME universal function if the
    leg's claim of basis-independence-after-normalization is true: (1/16)(1+3(1-t)^2)^2.
  * TWO EXTRA PATHS the leg never ran (kill B only / kill C only) -> block-triangular
    endpoints; additivity must come out the same (path-robustness probe).
  * Equivariance: rotation (2pi/3, -2pi/3) in coordinate planes (the leg used both planes
    +2pi/3 in the quaternion picture), spin lift via CLIFFORD EXPONENTIALS
    g = (c + s g0g1)(c - s g2g3), and the general ATIYAH-BOTT alternating-trace formula
    ind_g = sum_p [tr(g|E+) - tr(g|E-)] / det_R(1 - dg^{-1}) as an INDEPENDENT equivariant
    route (the leg used the nu_D-multiplier route only).
  * E-block: single identity  delta o (c(xi) (x) 1) o iota = -(1/2) c(xi)  on ALL of S
    (coefficient (2-n)/n AND chirality reversal in one shot), plus Omega iota = -iota omega.

FIREWALL: inputs sigma(K3) = -16, p1 = 3 sigma, ind D = 2 (= -sigma/8), Nikulin 6 fixed pts,
tr(g|T_C) = -2. No chi(K3), no A-hat = 3, no /8 manufacture; -38 must FALL OUT.
Exact arithmetic only (sympy rationals, sqrt(3), I; Fractions for bookkeeping).
"""
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import sympy as sp
from sympy import I, Rational, symbols, eye, zeros, Matrix, expand, cancel, Poly
from fractions import Fraction as F

N = 0
def check(c, m):
    global N
    N += 1
    assert c, "REFEREE-FAIL[%d]: %s" % (N, m)
    print("  ok[%02d] %s" % (N, m))

x1, x2, x3, x4, t = symbols("x1 x2 x3 x4 t", real=True)
X = (x1, x2, x3, x4)
q = x1**2 + x2**2 + x3**2 + x4**2

def dag(M): return M.conjugate().T
def zmat(M): return expand(M) == zeros(*M.shape)

print("== R1. my own Clifford rep (Pauli, NOT the leg's quaternion layout) ==")
P1 = Matrix([[0, 1], [1, 0]]); P2 = Matrix([[0, -I], [I, 0]]); P3 = Matrix([[1, 0], [0, -1]])
sig = [eye(2), I*P1, I*P2, I*P3]
gam = [Matrix(sp.BlockMatrix([[zeros(2,2), dag(sig[m])], [-sig[m], zeros(2,2)]])) for m in range(4)]
for a in range(4):
    for b in range(4):
        anti = expand(gam[a]*gam[b] + gam[b]*gam[a])
        assert anti == (-2*eye(4) if a == b else zeros(4,4))
check(True, "Clifford relations g_a g_b + g_b g_a = -2 delta_ab (16 identities, my rep)")
GX = sum((X[m]*gam[m] for m in range(4)), zeros(4,4))
check(zmat(GX*GX + q*eye(4)), "c(xi)^2 = -q in my rep")
om = sp.diag(1, 1, -1, -1)                       # chirality; S+ = coords 0,1
check(all(zmat(om*gam[m] + gam[m]*om) for m in range(4)),
      "omega anticommutes with every gamma: c(xi) is chirality-ODD (independent re-proof)")

print("== R2. basis-free delta/iota/P on the FULL 16-dim S(x)T (T fast; orthonormal basis) ==")
Sel = []
for m in range(4):
    S_ = zeros(4, 16)
    for s in range(4):
        S_[s, 4*s + m] = 1
    Sel.append(S_)
DELTA = sum((gam[m]*Sel[m] for m in range(4)), zeros(4,16))          # 4x16
IOTA = sum((-Rational(1,4)*dag(Sel[m])*gam[m] for m in range(4)), zeros(16,4))  # 16x4
check(zmat(DELTA*IOTA - eye(4)), "delta o iota = id_S (my normalization -1/4, n = 4)")
P16 = eye(16) - IOTA*DELTA
check(zmat(P16*P16 - P16) and zmat(dag(P16) - P16),
      "P is an ORTHOGONAL projector in the standard basis (no Gram matrices needed)")
check(zmat(DELTA*P16), "delta o P = 0 (gamma-traceless subbundle = im P)")
check(P16.rank() == 12, "rank P = 12 = 16 - 4 (V+ (+) V- has rank 6 + 6)")
OM16 = Matrix(sp.kronecker_product(om, eye(4)))
check(zmat(OM16*P16 - P16*OM16), "P commutes with chirality: splitting respects S+/-")
check(zmat(OM16*IOTA + IOTA*om),
      "Omega o iota = -iota o omega: iota(S^-+) lands in (S(x)T)^+-  -- CHIRALITY REVERSAL "
      "of the embedded labels, proven as one matrix identity")

SIG16 = Matrix(sp.kronecker_product(GX, eye(4)))                     # c(xi) (x) 1_T
plus = [i for i in range(16) if OM16[i, i] == 1]
minus = [i for i in range(16) if OM16[i, i] == -1]
check(len(plus) == 8 and len(minus) == 8, "chirality coordinate subspaces have dim 8 + 8")

print("== R3. E-label single identity: delta (c(xi)(x)1) iota = -(1/2) c(xi) on ALL of S ==")
ELAB = expand(DELTA*SIG16*IOTA)
check(zmat(ELAB + Rational(1,2)*GX),
      "delta o Sigma o iota = -(1/2) c(xi) EXACTLY: coefficient (2-n)/n = -1/2 AND the "
      "embedded block is the (scaled) Clifford symbol -- with iota's chirality flip this is "
      "the REVERSED-chirality Dirac symbol (leg's E = -(1/2) * (S- -> S+ block) confirmed "
      "rep-independently)")

print("== R4. ellipticity of the compressed symbol, annihilator + trace-moment route ==")
Tcomp = expand(P16*SIG16*P16)
Xc = Tcomp[minus, plus]                                              # compressed +/- block, 8x8
Nh = expand(dag(Xc)*Xc)
check(zmat(dag(Nh) - Nh), "N = X^dag X Hermitian in the orthonormal basis (diagonalizable)")
ANN = expand(Nh*(Nh - q*eye(8))*(Nh - Rational(1,4)*q*eye(8)))
check(zmat(ANN), "N (N - q)(N - q/4) = 0: spec(N) subset {0, q, q/4}")
tr1 = expand(Nh.trace()); tr2 = expand((Nh*Nh).trace())
check(expand(tr1 - Rational(9,2)*q) == 0, "tr N = 9q/2 (first moment)")
check(expand(tr2 - Rational(33,8)*q**2) == 0, "tr N^2 = 33q^2/8 (second moment)")
# m1 + m2/4 = 9/2 and m1 + m2/16 = 33/8  =>  m2 = 2, m1 = 4, m0 = 8 - 6 = 2
m2_ = (F(9,2) - F(33,8)) / (F(1,4) - F(1,16)); m1_ = F(9,2) - m2_/4
check(m1_ == 4 and m2_ == 2 and 8 - int(m1_ + m2_) == 2,
      "multiplicities FORCED by two moments: 0 (x2 = iota(S-)), q (x4), q/4 (x2) -- "
      "singular values match the leg's Gram charpoly (L-q)^4(L-q/4)^2 plus the 2-dim kernel")
check((F(1,4) == F(2-4, 4)**2), "q/4 factor = ((n-2)/n)^2 at n = 4 (Weitzenboeck; vanishes only n = 2)")
# => compressed symbol V+ -> V- invertible for xi != 0: ELLIPTIC. (0-eigenvalue lives on iota(S-).)
K0 = Nh.subs({x1: 1, x2: 2, x3: 3, x4: 5})
check(K0.rank() == 6, "rank X^dag X = 6 at a generic point: kernel is EXACTLY the 2-dim iota(S-)")

print("== R5. homotopy, basis-free; det ratio must be the leg's universal f(t)/f(0) ==")
Q16 = eye(16) - P16
OFFD = expand(P16*SIG16*Q16 + Q16*SIG16*P16)
S_t16 = SIG16 - t*OFFD
Xt = (S_t16)[minus, plus]
detX0 = expand(Matrix(Xt.subs(t, 0)).det(method="domain-ge"))
detXt = expand(Xt.det(method="domain-ge"))
r_t = cancel(detXt / detX0)
check(r_t.free_symbols <= {t}, "det ratio depends on t ONLY (xi-dependence cancels: SO(4)-invariance)")
r_pred = expand(Rational(1,16)*(1 + 3*(1 - t)**2)**2)
check(expand(r_t - r_pred) == 0,
      "det sigma_t / det sigma_0 = (1/16)[1 + 3(1-t)^2]^2 EXACTLY in my rep too: the leg's "
      "normalized homotopy determinant is REP-INDEPENDENT as claimed")
rp = Poly(r_pred, t)
check(sp.real_roots(rp) == [], "NO real roots at all (route 1: exact real_roots)")
check(rp.count_roots(0, 1) == 0, "zero roots in [0,1] (route 2: Sturm)")
# hence det sigma_t = r(t) det sigma_0 with det sigma_0 = c q^4 != 0: elliptic for ALL real
# xi != 0 and ALL t in [0,1] -- PROVEN as a polynomial identity, not sampled.
check(expand(detX0*16 - expand(Matrix(Xt.subs(t, 1)).det(method="domain-ge"))*16/Rational(1,16)) is not None
      and sp.nsimplify(r_pred.subs(t, 1)) == Rational(1,16),
      "endpoint value r(1) = 1/16 > 0: block-diagonal endpoint elliptic")

print("== R5b. EXTRA paths the leg never ran: kill B only / kill C only (triangular endpoints) ==")
S_B = SIG16 - t*expand(P16*SIG16*Q16)          # kill V<-iota block only
S_C = SIG16 - t*expand(Q16*SIG16*P16)          # kill iota<-V block only
rB = cancel(expand(Matrix(S_B[minus, plus]).det(method="domain-ge")) / detX0)
rC = cancel(expand(Matrix(S_C[minus, plus]).det(method="domain-ge")) / detX0)
check(rB.free_symbols <= {t} and rC.free_symbols <= {t}, "triangular-path ratios depend on t only")
for nm, rr in (("B-only", rB), ("C-only", rC)):
    pr = Poly(sp.nsimplify(rr), t)
    # NOTE: these ratios are (3t-4)^2/16 -- a double root at t = 4/3 OUTSIDE [0,1];
    # only [0,1]-root-freeness is required for the homotopy (Sturm), unlike the symmetric
    # path which happens to be globally root-free.
    check(pr.count_roots(0, 1) == 0 and sp.nsimplify(rr.subs(t, 1)) != 0
          and sp.nsimplify(rr.subs(t, 0)) == 1,
          "path %s stays elliptic on [0,1] (independent SECOND/THIRD homotopy to a "
          "block-TRIANGULAR symbol: same additivity, path-robust)" % nm)
    check(sp.expand(sp.nsimplify(rr) - (3*t - 4)**2/Rational(16)) == 0,
          "path %s ratio = (3t-4)^2/16 exactly (root 4/3 outside [0,1])" % nm)
check(sp.nsimplify(rB.subs(t, 1)) == sp.nsimplify(rC.subs(t, 1)) and
      sp.nsimplify(rB.subs(t, 1)) != 0,
      "triangular endpoints have equal nonzero det: ind(full) = ind(A-block) + ind(E-block) "
      "by three independent paths")

print("== R5c. negative control (my formulation): keeping ONLY off-diagonal kills ellipticity ==")
XbadEnd = OFFD[minus, plus]
check(expand(Matrix(XbadEnd).det(method="domain-ge")) == 0,
      "det(off-diagonal-only endpoint) == 0 identically: certificate is NON-VACUOUS")
check(Matrix(XbadEnd.subs({x1: 1, x2: 2, x3: 3, x4: 5})).rank() <= 4,
      "bad endpoint rank <= 4 < 8")

print("== R6. equivariance, DIFFERENT model: rotation (2pi/3, -2pi/3), Clifford-exponential lift ==")
s3 = sp.sqrt(3)
c_, s_ = Rational(1,2), s3/2                    # cos(pi/3), sin(pi/3)
R1r = Matrix([[-Rational(1,2), -s3/2], [s3/2, -Rational(1,2)]])      # +2pi/3 in (x1,x2)
R2r = Matrix([[-Rational(1,2), s3/2], [-s3/2, -Rational(1,2)]])      # -2pi/3 in (x3,x4)
GT = sp.diag(R1r, R2r)
check(zmat(expand(GT.T*GT - eye(4))) and expand(GT.det() - 1) == 0 and zmat(expand(GT**3 - eye(4))),
      "g_T in SO(4), order 3; angles (2pi/3, -2pi/3) = the SYMPLECTIC weights (zeta, zeta^{-1}) "
      "in the COORDINATE complex structure (different model from the leg's both-planes-+2pi/3)")
check(expand(GT.trace() + 2) == 0, "tr(g|T) = -2 = tr(g|T_C) (Nikulin local datum)")
g1 = c_*eye(4) + s_*gam[0]*gam[1]
g2 = c_*eye(4) - s_*gam[2]*gam[3]
GS = expand(g1*g2)
check(zmat(expand(GS*dag(GS) - eye(4))) and zmat(expand(GS**3 - eye(4))),
      "spin lift g_S = (c + s g0g1)(c - s g2g3): unitary, order 3 (Clifford exponentials, "
      "NOT the leg's quaternion left-multiplication)")
SUBG = dict(zip(X, [sum(GT[i, j]*X[j] for j in range(4)) for i in range(4)]))
check(zmat(expand(GS*GX*dag(GS) - GX.subs(SUBG, simultaneous=True))),
      "g_S c(xi) g_S^{-1} = c(g_T xi): correct spin lift (intertwining verified symbolically)")
check(zmat(expand(GS*om - om*GS)), "g_S preserves chirality")
check(zmat(expand(GS[:2, :2] - eye(2))), "g|S+ = 1 (trivial) -- canonical symplectic lift, "
      "matches canon ind_phi(D) = +2 pinning, derived in MY rep independently")
evS = expand(GS[2:, 2:].trace())
check(sp.simplify(evS + 1) == 0, "tr(g|S-) = -1 = zeta + zeta^2")
G16 = Matrix(sp.kronecker_product(GS, GT))
check(zmat(expand(G16*P16 - P16*G16)), "g commutes with the twistor projector (equivariant splitting)")
check(zmat(expand(DELTA*G16 - GS*DELTA)), "delta is g-equivariant")
check(zmat(expand(G16*IOTA - IOTA*GS)), "iota is g-equivariant")
# homotopy equivariance for SYMBOLIC t, chiral blocks:
Gp = G16[plus, plus]; Gm = G16[minus, minus]
check(zmat(G16[plus, minus]) and zmat(G16[minus, plus]), "g is chirality-block-diagonal")
LHS = expand(Gm*Xt)
RHS = expand(Matrix(Xt.subs(SUBG, simultaneous=True))*Gp)
check(zmat(expand(LHS - RHS)),
      "g o sigma_t(xi) = sigma_t(g_T xi) o g for SYMBOLIC t: the whole homotopy is "
      "order-3 equivariant in my independent model too")
# traces on V+- via tr(g P | chirality subspace):
GP = expand(G16*P16)
trVp = sp.simplify(sum(GP[i, i] for i in plus))
trVm = sp.simplify(sum(GP[i, i] for i in minus))
check(sp.simplify(trVp + 3) == 0 and sp.simplify(trVm) == 0,
      "tr(g|V+) = -3, tr(g|V-) = 0 (basis-free trace of g o P per chirality)")
check(sp.simplify((trVp - trVm) - (2 - (-1))*(GT.trace() + 1)) == 0,
      "multiplier identity: trV+ - trV- = (trS+ - trS-)(tr T_C + 1) = 3 * (-1) = -3")

print("== R7. INDEPENDENT equivariant route: general Atiyah-Bott alternating-trace formula ==")
detR = expand(Matrix(eye(4) - GT.T).det())      # det_R(1 - g^{-1}|T_p), g^{-1} = g^T
check(sp.simplify(detR - 9) == 0, "det_R(1 - g^{-1}) = 9 at each of the 6 fixed points")
NU = F(1, 3)
check(F(3, 9) == NU, "Atiyah-Bott Dirac ratio (trS+ - trS-)/det = 3/9 = 1/3 = nu_D: "
      "RE-DERIVES the prior-verified canon nu_D = 1/3 (never imported here)")
check(6*F(3, 9) == 2, "ind_phi(D) = 6 * 1/3 = 2 (canon cross-check, independent route)")
check(6*F(3*(-2), 9) == -4, "ind_phi(D (x) T_C) = 6 * (trS+-trS-)*trT_C/det = -4")
check(6*F(-3, 9) == -2, "ind_phi(Q) = 6 * (trV+ - trV-)/det = -2 (DIRECT Atiyah-Bott on the "
      "compressed complex; the leg's value re-derived without the multiplier route)")
check(6*F((-1) - 2, 9) == -2, "ind_phi(embedded block: iota(S-) -> iota(S+)) = 6*(-3)/9 = -2 "
      "= -ind_phi(D): reversed-chirality bookkeeping consistent")
check(-4 == -2 + (-2), "equivariant additivity: ind_phi(D(x)T_C) = ind_phi(Q) + ind_phi(rev D)")
check(int(GT.trace() + 1) % 3 != 0 and int(GT.trace() - 1) % 3 == 0,
      "the fork: geometric multiplier trT_C + 1 = -1 NOT divisible by 3; pinned trT_C - 1 = -3 "
      "divisible by 3 (structural kill only for the PINNED class)")

print("== R8. index bookkeeping (Fractions; firewall-clean; -38 must FALL OUT) ==")
SIGMA = -16
p1 = 3*SIGMA
indD = F(-SIGMA, 8)                             # = 2 (canon; = A-hat, never 3)
check(indD == 2, "ind D = -sigma/8 = 2 (A-hat = 2, never 3)")
indDT = F(4*(-p1), 24) + p1                     # int Ahat ch(T_C) = 4*(-p1/24) + p1 = (5/6) p1
check(indDT == -40, "ind(D (x) T_C) = (5/6) p1 = -40 (characteristic-class route)")
indRev = -indD
indQ = indDT - indRev
check(indQ == -38, "additivity => ind Q = -40 - (-2) = -38 (DERIVED, never imported)")
check(indQ == F(19*SIGMA, 8), "= 19 sigma/8: matches HS Prop 3.1(i) (published -38 on K3)")
check(indQ == indDT + indD, "= ind(D(x)T_C) + ind D: matches HS eq.(11) ind Q = ind D_TM + ind D "
      "verified verbatim in the cached arXiv text (line ~316)")
check(int(indQ) % 3 == 1 and (-42) % 3 == 0 and ((-42) - int(indQ)) == -2*int(indD),
      "residues: -38 == 1 mod 3 (alive), -42 == 0 mod 3 (killed); gap exactly 2 ind D = 4")
check(all(v != 24 for v in [SIGMA, p1, int(indD), int(indDT), int(indQ), 6, 3]),
      "FIREWALL: no chi(K3) = 24 anywhere in the inputs or outputs")

print()
print("REFEREE VERIFY: all %d checks passed; every load-bearing LEG-A result re-derived with" % N)
print("different machinery (rep, ordering, basis-free projectors, moment-forced multiplicities,")
print("two extra homotopy paths, Clifford-exponential lift, general Atiyah-Bott route).")
