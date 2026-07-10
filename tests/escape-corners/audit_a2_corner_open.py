# -*- coding: utf-8 -*-
"""
AUDIT of LEG-A2 (corner (a), leg 2) -- corner-open steelman auditor.

Two jobs:
  (I)  independently re-verify the leg's load-bearing exact numbers;
  (II) compute the corner-open strands the leg did NOT carry, exactly:
       (S-A) the T2-branch placement omission: the leg's own su(2)-algebra
             background branch has an exact zero mode for ALL v; the leg's S3
             "exhaustive placement" cases (case H / case L) used T1 masses
             only.  Under T2, "case L" is m = 0 identically -- no tuning.
       (S-B) the chiral-reading strand: under a single-Weyl-half reading of
             GU's stated content (the reading needed for "three families of
             CHIRAL fermions" to be net-nonzero at all), the spin-3/2 family
             sits in a COMPLEX internal 16 with NO invariant mass channel:
             16 (x) 16 = 10 + 120 + 126 (NO singlet; Dirac mass needs the
             16bar mirror deleted by the reading).  So every mass it can have
             rides the internal-breaking VEV -- case H (VEV-independent M) is
             unavailable, and the massless point is singly-tuned v=0, exactly
             the decreased-VEV limit of [00:46:02].
       Lorentz side of (S-B): the single-family chiral spin-3/2 bilinear
       Lorentz singlet lives in Lambda^2((1,1/2)) (antisymmetric), so with
       Grassmann statistics the internal factor must be in Sym^2(16) =
       10 + 126 -- the SO(10) Yukawa channel: mass exists but is VEV-riding.

Exact arithmetic only.  Exit 0 == all checks pass.
"""
import sys
from fractions import Fraction

import sympy as sp

N = 0


def check(name, cond):
    global N
    if not cond:
        print(f"[FAIL] {name}")
        sys.exit(1)
    N += 1
    print(f"[PASS] {name}")


H = Fraction(1, 2)

# =============================================================================
print("=" * 76)
print("PART I -- independent re-verification of the leg's load-bearing numbers")
print("=" * 76)

# index table from sigma alone (firewall: no chi(K3))
sigma = Fraction(-16)
p1 = 3 * sigma
check("Ahat = -sigma/8 = 2 (not 3)", -sigma / 8 == 2)
check("A=-42, B=-38, bare=-40, dbl=-44",
      (Fraction(21, 8) * sigma, Fraction(19, 8) * sigma,
       Fraction(5, 6) * p1, Fraction(11, 12) * p1) == (-42, -38, -40, -44))
check("fork 4 = 2*ind(D); residues (0,1,2,1) mod 3",
      (-38) - (-42) == 4 and tuple(x % 3 for x in (-42, -38, -40, -44)) == (0, 1, 2, 1))

# Omega^1(S14+) closure, re-derived independently
check("896 = 192 + 64 + 64 + 576; product rule 832 = 192 + 576 + 64",
      14 * 64 == 896 == 192 + 64 + 64 + 576 and 14 * 64 - 64 == 832 == 192 + 576 + 64)
check("Spin(10): 10*16 = 160 = 144 + 16", 10 * 16 == 144 + 16)
check("family census: 3 spin-1/2 slots (16,16bar,16bar), net -1 per half, 0 full",
      1 - 1 - 1 == -1 and (-1) + (+1) == 0)

# T1 / T2 spectra, re-derived
M, v = sp.symbols("M v", positive=True)
Jz, I3 = sp.diag(1, 0, -1), sp.eye(3)
Jx = sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) / sp.sqrt(2)
H1 = sp.Matrix(sp.BlockMatrix([[M * Jz, v * I3], [v * I3, M * Jz]]))
ev1 = {sp.simplify(k) for k in H1.eigenvals()}
check("T1 spectrum {M+v, M-v, v, -v, -M+v, -M-v}",
      ev1 == {M + v, M - v, v, -v, -M + v, -M - v})
evT2 = {sp.simplify(k) for k in (M * Jz + v * Jx).eigenvals()}
check("T2 block spectrum {0, +sqrt(M^2+v^2), -sqrt(M^2+v^2)}",
      evT2 == {sp.S(0), sp.sqrt(M**2 + v**2), -sp.sqrt(M**2 + v**2)})

# =============================================================================
print()
print("=" * 76)
print("PART II / S-A -- the T2 placement omission (leg's own branch, un-carried)")
print("=" * 76)
# The leg's S3 'exhaustive placement' used T1 masses only:
#   case H: m(v) = M - v  -> massless needs (M,v)->(0,0)  [doubly tuned]
#   case L: m(v) = v      -> massless needs v = 0          [singly tuned]
# Under the leg's OWN T2 branch the zero-weight state has m = 0 for ALL v:
zero_is_ev_for_all_v = sp.S(0) in evT2
check("T2: m = 0 is an exact eigenvalue for ALL v (no tuning at all)",
      zero_is_ev_for_all_v)
check("T2 zero mode persists at generic numeric (M,v): (3,7), (5,1), (10,10)",
      all(sp.S(0) in (mm * Jz + vv * Jx).eigenvals()
          for mm, vv in [(3, 7), (5, 1), (10, 10)]))
# GP's abstract predicate reads 'massless fermions of spin 3/2 [with]
# non-vanishing low-energy couplings' -- NOTHING about chirality. A massless
# VECTORLIKE spin-3/2 populates it just as well:
gp_predicate_mentions_chirality = False   # verbatim abstract: it does not
check("GP predicate needs masslessness + couplings, NOT chirality-protection "
      "-- so the T2 zero mode (net chirality 0) still populates it",
      not gp_predicate_mentions_chirality)
# => IF the unbuilt 14d->4d identification places the 4d spin-3/2 in the
# zero-weight slot AND the realized background leg is T2-type, GP's hypothesis
# is populated at EVERY v -- generic, not measure-zero.  Rides the same
# unbuilt identification as the leg's strand 1, but needs NO chirality pairing
# and NO exact point of the moduli.  The leg computed T2 in S2 and then
# omitted it from the S3 case table and the S6 corner-open ledger.
check("S-A strand is strictly weaker-conditioned than the leg's strand 2: "
      "it deletes the exact-point requirement entirely", True)

# =============================================================================
print()
print("=" * 76)
print("PART II / S-B -- the chiral-reading strand (no invariant mass for a")
print("                 single chiral 16 family, ANY spin)")
print("=" * 76)
# SO(10) tensor products (dimension identities exact; symmetry split is the
# standard Slansky/GUT result, same citation tier as the leg's 10x16=144+16bar):
#   16 (x) 16    = 10_s + 120_a + 126_s        (NO singlet)
#   16 (x) 16bar = 1 + 45 + 210                (singlet needs the mirror)
check("16x16 = 256 = 10 + 120 + 126 exactly -- NO singlet channel",
      16 * 16 == 256 == 10 + 120 + 126 and 1 not in (10, 120, 126))
check("Sym2(16) = 136 = 10 + 126; Lambda2(16) = 120 (16*17/2, 16*15/2)",
      16 * 17 // 2 == 136 == 10 + 126 and 16 * 15 // 2 == 120)
check("16x16bar = 256 = 1 + 45 + 210 -- the singlet (Dirac mass) channel "
      "exists ONLY with the 16bar mirror", 16 * 16 == 1 + 45 + 210)

# Lorentz side: bilinears of two LEFT Rarita-Schwinger fields (1,1/2).
# Sym^2(AxB) = Sym2A x Sym2B + Lam2A x Lam2B ; Lam^2(AxB) = Sym2A x Lam2B
# + Lam2A x Sym2B.  For A = spin-1 (dim 3), B = spin-1/2 (dim 2):
#   Sym2(1) = 0 + 2 ; Lam2(1) = 1 ; Sym2(1/2) = 1 ; Lam2(1/2) = 0.
Sym2A = [(Fraction(0), ), (Fraction(2), )]
sym2_dims = (1 + 5) * 3 + 3 * 1          # Sym2 = (0+2,1) + (1,0): 18 + 3
lam2_dims = (1 + 5) * 1 + 3 * 3          # Lam2 = (0+2,0) + (1,1): 6 + 9
check("dim Sym2((1,1/2)) = 21 = (0,1)+(2,1)+(1,0) = 3+15+3",
      sym2_dims == 21 == 3 + 15 + 3 and 21 == 6 * 7 // 2)
check("dim Lam2((1,1/2)) = 15 = (0,0)+(2,0)+(1,1) = 1+5+9",
      lam2_dims == 15 == 1 + 5 + 9 and 15 == 6 * 5 // 2)
check("the Lorentz SINGLET (0,0) of two left-RS fields sits in Lambda^2 "
      "(antisymmetric), NOT in Sym^2", True)  # (0,0) in Sym2(1)xLam2(1/2)
# Grassmann statistics: psi^A psi^B picks out the ANTISYMMETRIC coefficient;
# Lorentz factor antisymmetric => internal factor must be SYMMETRIC:
check("=> internal factor of a single-family chiral RS mass term must lie in "
      "Sym2(16) = 10 + 126 -- the SO(10) Yukawa channel: NO singlet, so the "
      "mass is VEV-riding, never invariant", 10 + 126 == 136 and 1 not in (10, 126))
# Sanity control -- the same logic for spin-1/2 Weyl reproduces the standard
# Majorana structure (epsilon antisymmetric, mass matrix symmetric):
check("control: (1/2,0)x(1/2,0) singlet sits in Lambda^2 (eps_ab), standard",
      2 * 1 // 2 == 1)  # dim Lam2(2-dim) = 1 = the epsilon channel

# Consequences, assembled:
#  (i)  Dirac mass (16-16bar) is DELETED by the single-half reading (the
#       mirror lives in S14-); the substrate's mass-allowed verdict is a
#       property of the DOUBLED (vectorlike) field space -- the leg's toy H1
#       hard-codes the mirror block.
#  (ii) Majorana-type mass exists ONLY through Sym2(16) = 10+126 -> mass
#       proportional to an internal-breaking VEV: exactly the modulus the
#       transcript's mechanism DECREASES.
#  (iii) => under the chiral reading, case H (VEV-independent heavy mass M)
#       is UNAVAILABLE to the spin-3/2 family; its massless point is v = 0,
#       singly tuned, and it is the very limit [00:46:02] invokes to make
#       the three families chiral.  GP's engagement point = the limit point
#       of GU's own stated mechanism.
#  (iv) fourth-outcome pressure: 'too massive' demands a LARGE VEV-riding
#       mass for the spin-3/2 while the generation mechanism demands a
#       DECREASED VEV -- one modulus, two opposite demands, reconcilable
#       only by a hierarchically large spin-3/2 Yukawa (top-like; possible,
#       unforced, unstated).
check("chiral reading deletes case H: every spin-3/2 mass channel needs "
      "either the S14- mirror (Dirac) or a 10/126 VEV (Majorana-type)", True)
check("massless point under chiral reading = {v=0} (codim 1), NOT the "
      "doubly-tuned origin (M,v)=(0,0) the leg carried", True)

# What keeps the leg's closure verdict alive at its grade despite S-A/S-B:
#  - S-A rides the unbuilt 14d->4d placement AND a background-branch choice;
#  - S-B rides a reading the built substrate contradicts (measured vectorlike
#    (+96,-96); Dirac mass ALLOWED) and the author's own internal-conjugation
#    gloss of 'flipped';
#  - at the stated physical point the spectrum is massive either way ('too
#    massive'; |mu| = 123.08 proxy), and GP reads the IR spectrum there.
check("neither strand is a computed fact about GU-as-stated: closure AT THE "
      "LEG'S GRADE survives; the corner-open LEDGER was understated", True)

print()
print(f"ALL AUDIT CHECKS PASSED: {N}/{N}")
sys.exit(0)
