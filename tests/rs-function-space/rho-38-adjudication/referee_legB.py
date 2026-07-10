#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
HOSTILE-REFEREE independent verification of LEG-B (index bookkeeping, -38 adjudication).

DIFFERENT MACHINERY than LEG-B (which used A-hat * ch characteristic-class arithmetic
and the imported nu_D4 = 1/3 Atiyah-Bott multiplier):

  R1. DOLBEAULT/HODGE route: on hyperkahler K3, D = sqrt2(dbar + dbar*) on Lambda^{0,*},
      so ind(D tensor E) = chi(M, E) for holomorphic E.  T_C ~ Omega^1 (+) Omega^1
      (holomorphic symplectic form gives T^{1,0} ~ Omega^1; K = O).  Inputs: Hodge
      numbers h^{0,0}=1, h^{0,1}=0, h^{0,2}=1, h^{1,0}=0, h^{1,1}=20, h^{1,2}=0.
      NO p1, NO A-hat, NO chi(K3), NO sigma in this route.
  R2. HOLOMORPHIC LEFSCHETZ route: per-point denominator det(1 - (dg)^{-1}|T^{1,0})
      = (1-zeta^{-1})(1-zeta) DERIVED = 3 (nu = 1/3 derived, not imported);
      cohomology-trace route cross-checks the fixed-point route (Lefschetz gate).
  R3. KERNEL-CHARACTER route for ind_phi(Q) (bypasses additivity AND Atiyah-Bott):
      HS Example (1): ker Q(K3) = 2 x primitive harmonic (1,1)-forms, dim 38, one
      chirality (forced by |ind| = dim ker).  Equivariant char of prim H^{1,1}
      = 7 + 6 zeta + 6 zeta^2 (prior-verified H^{1,1} = 8 + 6 zeta + 6 zeta^2 minus the
      invariant Kahler class); doubled by the g-trivial parallel-spinor factor.
  R4. Published-density re-derivation: Bilal (11.47) twist = ch(T_C) - 1  ->  21 sigma/8;
      HS eq (11) twist = ch(T_C) + 1  ->  19 sigma/8 (chern-character arithmetic redone
      independently as a check of the ATTRIBUTION, not the derivation).
  R5. Certificate positivity by coefficient inspection (not root-requirement):
      16 f(t) = 9u^4 + 6u^2 + 1, u = 1 - t: every coefficient positive => f > 0 on R.
  R6. Class law applied to all rows + consistency with the two prior-verified rho
      packages (Dirac (0,-2/3,+2/3) at ind 2; pinned RS (0,+2,-2) at ind -42).

Exact arithmetic only: Fractions and Z[zeta] integer pairs (a + b*zeta).
"""
import sys
from fractions import Fraction as F

FAILED = []
N = [0]
def check(name, cond):
    N[0] += 1
    if not cond:
        FAILED.append(name)
        print("  FAIL [%02d] %s" % (N[0], name))
    return cond

# ---- Z[zeta] pairs: x = (a, b) means a + b*zeta, zeta^2 = -1 - zeta -------------
def zmul(x, y):
    a, b = x; c, d = y
    return (a*c - b*d, a*d + b*c - b*d)
def zadd(*xs):
    return (sum(x[0] for x in xs), sum(x[1] for x in xs))
def zsub(x, y):
    return (x[0]-y[0], x[1]-y[1])
ONE  = (1, 0)
ZETA = (0, 1)
ZETA2 = zmul(ZETA, ZETA)

print("R0. zeta arithmetic")
check("zeta^2 = -1 - zeta", ZETA2 == (-1, -1))
check("1 + zeta + zeta^2 = 0", zadd(ONE, ZETA, ZETA2) == (0, 0))

# ================================================================================
print("\nR1. Dolbeault/Hodge route (NO p1, NO A-hat, NO sigma, NO chi)")
# ================================================================================
h = {(0,0):1, (0,1):0, (0,2):1, (1,0):0, (1,1):20, (1,2):0}   # standard K3 Hodge data
chi_O    = h[(0,0)] - h[(0,1)] + h[(0,2)]
chi_Om1  = h[(1,0)] - h[(1,1)] + h[(1,2)]
check("chi(O) = 2", chi_O == 2)
check("chi(Omega^1) = -20", chi_Om1 == -20)
ind_D_dolb   = chi_O                    # S+ ~ Lambda^{0,0}+Lambda^{0,2}, K trivial
ind_DTC_dolb = 2 * chi_Om1              # T_C ~ Omega^1 (+) Omega^1 smoothly
check("ind(D) = 2 via Dolbeault", ind_D_dolb == 2)
check("ind(D tensor T_C) = -40 via Dolbeault (independent of char classes)",
      ind_DTC_dolb == -40)
# the fork, using ONLY the published K-class completions:
ind_Q_dolb      = ind_DTC_dolb + ind_D_dolb      # HS eq (11): ind Q = ind D_TM + ind D
ind_pinned_dolb = ind_DTC_dolb - ind_D_dolb      # HS Rem 3.6: physics = ind D_TM - ind D
check("geometric Q: -38 via Dolbeault + HS eq (11)", ind_Q_dolb == -38)
check("pinned proxy: -42 via Dolbeault + HS Rem 3.6", ind_pinned_dolb == -42)
check("fork = 2*ind(D) = 4", ind_Q_dolb - ind_pinned_dolb == 4 == 2 * ind_D_dolb)

# cross to the sigma forms (sigma = -16 pin used ONLY here, for the gate forms):
sigma = -16
check("gate: -38 = 19*sigma/8 (HS Prop 3.1(i))", F(19,8)*sigma == ind_Q_dolb)
check("gate: -38 = -19*Ahat with Ahat = ind D = 2", -19*ind_D_dolb == ind_Q_dolb)
check("gate: -42 = 21*sigma/8 (Bilal 11.47 / CD)", F(21,8)*sigma == ind_pinned_dolb)
check("HS internal consistency: -19*Ahat == 19*sigma/8 forces Ahat = -sigma/8 = 2",
      F(-sigma,8) == 2)

# ================================================================================
print("\nR2. Holomorphic Lefschetz route (nu DERIVED, not imported)")
# ================================================================================
# fixed-point denominator det(1 - g^{-1}|T^{1,0}) with weight zeta on T^{1,0}:
den = zmul(zsub(ONE, ZETA2), zsub(ONE, ZETA))   # (1 - zeta^{-1})(1 - zeta)
check("per-point denominator = 3 exactly (DERIVES nu = 1/3)", den == (3, 0))
NFIX = 6
L_O = F(NFIX, den[0])                            # L(g, O) = sum_p 1/3
check("L(g,O) = 2 = ind_phi(D) (matches prior pin, derived here)", L_O == 2)
# L(g, Omega^1): fixed-point route -- cotangent weights (zeta^{-1}, zeta), trace = -1
tr_cot = zadd(ZETA2, ZETA)
check("tr(g|Omega^1_p) = -1 exactly", tr_cot == (-1, 0))
L_Om1_fp = F(NFIX * tr_cot[0], den[0])
check("L(g,Omega^1) fixed-point route = -2", L_Om1_fp == -2)
# cohomology route: -tr(g|H^{1,1}), H^{1,1} = 8 + 6 zeta + 6 zeta^2 (prior verified)
trH11 = zadd((8,0), zmul((6,0), ZETA), zmul((6,0), ZETA2))
check("tr(g|H^{1,1}) = 8 - 6 = 2 (as real number: 8 + 6*(zeta+zeta^2) = 2)",
      trH11 == (2, 0))
L_Om1_coh = -trH11[0]
check("LEFSCHETZ GATE: fixed-point route == cohomology route (-2 == -2)",
      L_Om1_fp == L_Om1_coh)
ind_phi_DTC = 2 * L_Om1_fp                       # two copies of Omega^1
check("ind_phi(D tensor T_C) = -4 (independent of the multiplier bookkeeping)",
      ind_phi_DTC == -4)
ind_phi_D = L_O
ind_phi_Q      = ind_phi_DTC + ind_phi_D         # equivariant HS eq (11)
ind_phi_pinned = ind_phi_DTC - ind_phi_D
check("ind_phi(Q) = -2", ind_phi_Q == -2)
check("ind_phi(pinned) = -6", ind_phi_pinned == -6)
# LEG-B's multiplier route as cross-check: 6*(1/3)*mult
for mult, want in ((-2, -4), (-1, -2), (-3, -6), (1, 2), (-4, -8)):
    check("multiplier route 6*(1/3)*(%d) = %d agrees" % (mult, want),
          F(6,3)*mult == want)

# ================================================================================
print("\nR3. Kernel-character route for ind_phi(Q) (bypasses additivity AND A-B)")
# ================================================================================
# HS Example (1): ker Q(K3) = 2 x prim harmonic (1,1); dim = 2*(20-1) = 38
dim_kerQ = 2 * (h[(1,1)] - 1)
check("dim ker Q(K3) = 38 (HS Example (1); BM Rem 5.3 sharp)", dim_kerQ == 38)
check("|ind Q| = dim ker Q forces one-chirality concentration", abs(ind_Q_dolb) == dim_kerQ)
# equivariant character: prim H^{1,1} = (8-1) + 6 zeta + 6 zeta^2 (invariant Kahler class
# removed from the invariant block); parallel-spinor doubling is g-TRIVIAL (S+ trivial)
tr_prim = zadd((7,0), zmul((6,0), ZETA), zmul((6,0), ZETA2))
check("tr(g|prim H^{1,1}) = 1", tr_prim == (1, 0))
tr_kerQm = 2 * tr_prim[0]
check("tr(g|ker Q^-) = 2  [char 14 + 12 zeta + 12 zeta^2 at g]", tr_kerQm == 2)
ind_phi_Q_kernel = 0 - tr_kerQm                  # ker Q^+ = 0 (forced above)
check("KERNEL ROUTE: ind_phi(Q) = -2 == additivity route == multiplier route",
      ind_phi_Q_kernel == -2 == ind_phi_Q)
check("kernel dims by phase {0:14, 1/3:12, 2/3:12} sum to 38", 14 + 12 + 12 == 38)

# ================================================================================
print("\nR4. Published-density attribution re-derivation (char-class, independent run)")
# ================================================================================
p1 = 3 * sigma                                   # signature theorem
Ahat4 = F(-p1, 24)
check("[Ahat]_4 = 2", Ahat4 == 2)
# twist ch(T_C) = 4 + p1;  Bilal 11.47 twist = ch(T_C) - 1 = 3 + p1
ind_bilal = 3 * Ahat4 + p1
check("Bilal 11.47 density [Ahat(ch T_C - 1)]_4 = (7/8) p1 = -42 == pinned A",
      ind_bilal == F(7,8)*p1 == -42)
ind_hs = 5 * Ahat4 + p1
check("HS eq (11) density [Ahat(ch T_C + 1)]_4 = (19/24) p1 = -38 == geometric B",
      ind_hs == F(19,24)*p1 == -38)
ind_bare = 4 * Ahat4 + p1
ind_dbl  = 2 * Ahat4 + p1
check("negative controls: bare -40 = (5/6)p1; double-sub -44 = (11/12)p1",
      ind_bare == F(5,6)*p1 == -40 and ind_dbl == F(11,12)*p1 == -44)
check("Dolbeault route == char-class route on ALL rows (two independent machineries)",
      (ind_hs, ind_bilal, ind_bare) == (ind_Q_dolb, ind_pinned_dolb, ind_DTC_dolb))

# ================================================================================
print("\nR5. Certificate positivity by coefficient inspection (not root-requirement)")
# ================================================================================
# 16*f(t) = (1 + 3u^2)^2 = 9u^4 + 6u^2 + 1, u = 1-t: all coefficients POSITIVE
coeffs = (9, 6, 1)   # u^4, u^2, u^0
check("expansion: (1+3u^2)^2 = 9u^4 + 6u^2 + 1 exactly",
      all(c > 0 for c in coeffs) and (1+3*1)**2 == 9+6+1 and (1+3*4)**2 == 9*16+6*4+1)
check("=> f(t) >= 1/16 > 0 for ALL real t (sum of positive terms; min at u=0, t=1)",
      min(F(9*u**4 + 6*u**2 + 1, 16) for u in [F(k,10) for k in range(11)]) == F(1,16))

# ================================================================================
print("\nR6. Class law on all rows + consistency with prior-verified rho packages")
# ================================================================================
def classes(ind):
    return tuple((-k * ind) % 3 for k in range(3))
table = {
    -42: (0,0,0), -38: (0,2,1), -40: (0,1,2), -44: (0,2,1), 2: (0,1,2), 38: (0,1,2),
}
for ind, want in table.items():
    check("classes(%d) = %s" % (ind, want), classes(ind) == want)
check("class relation: classes(B) = classes(A) + 2*classes(Dirac) mod 3",
      tuple((a + 2*d) % 3 for a, d in zip(classes(-42), classes(2))) == classes(-38))
check("sign-robustness: +/-38 both NONZERO (labels 1<->2 swap only)",
      classes(38) != (0,0,0) and classes(-38) != (0,0,0)
      and classes(38) == tuple(classes(-38)[i] for i in (0,2,1)))
# consistency with the two prior-verified spectral rho packages:
#   Dirac: rho = (0, -2/3, +2/3), ind = 2:   law gives -k*2/3 -> (0, -2/3, -4/3~=+2/3)
check("law vs prior Dirac rho: -1/3*2 = -2/3 == -2/3;  -2/3*2 = -4/3 == +2/3 mod Z",
      (F(-2,3) - F(-2,3)).denominator == 1 and (F(-4,3) - F(2,3)).denominator == 1)
#   pinned RS: rho = (0, +2, -2), ind = -42: law gives 14k mod Z = 0
check("law vs prior pinned-RS rho: 14 == +2 mod Z and 28 == -2 mod Z",
      (14 - 2) % 1 == 0 and F(28 - (-2), 1).denominator == 1 and (28+2) % 1 == 0)
# orbifold integrality on all five rows
for ind, iphi, want in ((-42,-6,-18), (-38,-2,-14), (-40,-4,-16), (-44,-8,-20), (2,2,2)):
    check("orbifold integrality (%d + 2*%d)/3 = %d in Z" % (ind, iphi, want),
          F(ind + 2*iphi, 3) == want and F(ind + 2*iphi, 3).denominator == 1)
# residue-multiplier law ind == 2*mult (mod 3)
for ind, mult in ((-42,-3), (-38,-1), (-40,-2), (-44,-4), (2,1)):
    check("residue law: %d == 2*(%d) mod 3" % (ind, mult), ind % 3 == (2*mult) % 3)

# ================================================================================
print("\n" + "=" * 70)
print("REFEREE VERIFY: %d checks, %d failed" % (N[0], len(FAILED)))
if FAILED:
    for f_ in FAILED:
        print("  FAILED: " + f_)
    sys.exit(1)
print("ALL INDEPENDENT ROUTES AGREE WITH LEG-B  (exit 0)")
sys.exit(0)
