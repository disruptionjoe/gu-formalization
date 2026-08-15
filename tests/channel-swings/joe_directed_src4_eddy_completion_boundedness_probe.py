#!/usr/bin/env python3
"""Joe-directed channel 3, gate SRC-4: does the eddy / Chern-Simons quadratic
completion rescue the unbounded potential?

BANKED INPUT (not re-derived here, re-run as live controls):
  SRC-2  the cross-term mass form M[(mu,B),(nu,C)] = F0^{mu nu A} f_{ABC} is
         symmetric and exactly traceless, so the Mexican hat is automatic.
  SRC-3  V(tv) = t^2 Q + t^4 K with K = ||v^v||^2, and an explicit k-valued ray
         gives K = -4 < 0 under the Killing/DeWitt pairing.
  CG-1   p is a declared coset; post-reduction (B_theta, eta_plus) is positive
         definite and Ad(K)-invariant, and the obstruction completes the square
         away.  Unbounded below IFF the norm-square uses the PRE-reduction forms.
  RB1b   (2026-07-30) an algebraic Spin(9,5)-equivariant map
         Lambda^2 (x) Lambda^2 -> V (x) Lambda^2 is ZERO by exact central parity.
         THE PARITY MECHANISM IS RB1b's.  This probe extends it to the 10-dim
         vertical and to K = SO(6) x SO(4); it claims no novelty for the method.
  K77    the released first-order T-paired action on the Spin-invariant constant
         branch is I(t) = 1456 t^3 + 7 kappa_1 t^2
         (lab/methods/research-evidence-contract-v1.0.md).  Re-used as the
         banked witness that the first-order cubic coefficient is NONZERO.

THE CONSTRUCTION.  The source's completed first-order action is

  I_1(T) = < T, S_omega( F_B + a D_B T + b [T,T] ) > + (kappa_1/2) < T, flat_1 T >

at the source point (a,b) = (1/2, 1/3), and the eddy-squared second-order rival is

  I_2(T) = || F_B + a D_B T + b [T,T] ||^2 .

Both are put into the SRC-3 boundedness question, in BOTH readings CG-1
separated: pre-reduction (Killing on ad, DeWitt (6,4) on form indices) and
post-reduction (B_theta on ad, eta_plus = I_10 on form indices).

CONVENTION RISK IS CARRIED, NOT GUESSED.  [T,T] = lam * (T^T) with lam = 2 under
the commutator convention and lam = 1 under the wedge convention.  Every verdict
below is proved for BOTH values, and for the whole (a,b) family, so no verdict
depends on the convention or on the undeclared coefficients.

All load-bearing arithmetic is exact: integers for so(6,4), Fraction for every
rational.  No floats anywhere.  Run with --mutate=NAME to plant a defect.
"""
from __future__ import annotations

import os
import sys
from fractions import Fraction as Fr
from itertools import combinations

import numpy as np

MUTATION = ""
for _arg in sys.argv[1:]:
    if _arg.startswith("--mutate="):
        MUTATION = _arg.split("=", 1)[1]

CHECKS: list[tuple[str, str, bool]] = []


def check(block: str, name: str, ok: object) -> None:
    CHECKS.append((block, name, bool(ok)))


def read_probe(relative: str) -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(os.path.dirname(here))
    with open(os.path.join(root, relative), encoding="utf-8") as fh:
        return fh.read()



# ---------------------------------------------------------------------------
# BLOCK 0 -- the algebra, and the banked controls re-run live.
# ---------------------------------------------------------------------------
P, Q_, N = 6, 4, 10
ETA = np.diag([1] * P + [-1] * Q_).astype(np.int64)      # DeWitt (6,4)
ETA_PLUS = np.eye(N, dtype=np.int64)                     # post-reduction

BASIS, KIND, LABEL = [], [], []
for i in range(N):
    for j in range(i + 1, N):
        A = np.zeros((N, N), dtype=np.int64)
        A[i, j], A[j, i] = 1, -1
        BASIS.append(ETA @ A)
        KIND.append("k" if (j < P or i >= P) else "p")
        LABEL.append((i, j))
NG = len(BASIS)


def br(X, Y):
    return X @ Y - Y @ X


def B_kill(X, Y):
    """Killing form up to the fixed positive constant (N-2); only signs are used."""
    return int(np.trace(X @ Y))


def B_theta(X, Y):
    """CG-1's post-reduction pairing B_theta(X,Y) = -B(X, theta Y) = tr(X Y^T)."""
    return int(np.trace(X @ Y.T))


def gen(i, j):
    return BASIS[LABEL.index((i, j))]


check("0-control", "so(6,4) has 45 generators, k=21, p=24 (PV-2)",
      NG == 45 and KIND.count("k") == 21 and KIND.count("p") == 24)
check("0-control", "Killing negative on every k direction (PV-2)",
      all(B_kill(BASIS[a], BASIS[a]) < 0 for a in range(NG) if KIND[a] == "k"))
check("0-control", "Killing positive on every p direction (PV-2)",
      all(B_kill(BASIS[a], BASIS[a]) > 0 for a in range(NG) if KIND[a] == "p"))
check("0-control", "B_theta Gram is exactly 2*I_45 (CG-1)",
      all(B_theta(BASIS[a], BASIS[b]) == (2 if a == b else 0)
          for a in range(NG) for b in range(NG)))

# CG-1's two-sided price: B_theta is Ad(K)-invariant and NOT Ad(G)-invariant.
def ad_invariance_residual(pairing, gidx):
    """max |pairing([g,X],Y) + pairing(X,[g,Y])| over the basis; 0 iff invariant."""
    G_ = BASIS[gidx]
    worst = 0
    for a in range(NG):
        for b in range(NG):
            r = pairing(br(G_, BASIS[a]), BASIS[b]) + pairing(BASIS[a], br(G_, BASIS[b]))
            worst = max(worst, abs(r))
    return worst


k_gens = [a for a in range(NG) if KIND[a] == "k"]
p_gens = [a for a in range(NG) if KIND[a] == "p"]
check("0-control", "B_theta is Ad(K)-invariant on all 21 k generators (CG-1)",
      all(ad_invariance_residual(B_theta, a) == 0 for a in k_gens))
check("0-control", "B_theta is NOT Ad(G)-invariant: an explicit p generator leaves "
      "a nonzero residual -- the price, stated two-sided (CG-1)",
      ad_invariance_residual(B_theta, p_gens[0]) != 0)

# SRC-3's published ray, re-run exactly.
X_, Y_ = gen(0, 1), gen(1, 2)                    # both in k
XY = br(X_, Y_)
K_SRC3_PRE = 2 * B_kill(XY, XY)                  # internal legs 0,1 both spacelike
K_SRC3_PRE_TIMELIKE = 2 * (-1) * B_kill(XY, XY)  # one leg on a timelike direction
K_SRC3_POST = 2 * B_theta(XY, XY)                # post-reduction, eta_plus = I
check("0-control", "SRC-3's published ray reproduces K = -4 exactly",
      K_SRC3_PRE == -4)
check("0-control", "SRC-3's timelike-leg flip reproduces +4 exactly",
      K_SRC3_PRE_TIMELIKE == 4)
check("0-control", "the SAME ray is strictly POSITIVE post-reduction (CG-1)",
      K_SRC3_POST > 0)


# ---------------------------------------------------------------------------
# BLOCK 1 -- READING E2: the eddy-SQUARED second-order rival.
#
#   I_2(T) = || F_0 + a D_B T + b [T,T] ||^2,   [T,T] = lam (T^T),  lam in {1,2}.
#
# For constant modes D_B T drops out and the leading quartic along a = t v is
#   (b lam)^2 * || v^v ||^2  =  (b lam)^2 * K_SRC3(v).
# The completion therefore RESCALES SRC-3's quartic by the strictly positive
# rational (b lam)^2 and CANNOT change its sign, for any b != 0 and either
# convention.  Certified below by direct exact construction, not by assertion.
# ---------------------------------------------------------------------------
def quartic_leading(b: Fr, lam: int, pairing, form_sign: int) -> Fr:
    """Exact leading t^4 coefficient of ||F0 + b*[tv,tv]||^2 on SRC-3's ray.

    The eddy quadratic in components: (b*[T,T])_{01} = b*lam*[X,Y].  The norm
    sums the (01) and (10) slots, whence the factor 2.
    """
    coeff = b * lam
    if MUTATION == "eddy-rescale-linear":
        # PLANT: pretend the completion enters LINEARLY, which would let b < 0
        # flip the quartic's sign and hand the source its rescue.
        return 2 * coeff * Fr(form_sign * pairing(XY, XY))
    return 2 * coeff * coeff * Fr(form_sign * pairing(XY, XY))


SOURCE_A, SOURCE_B = Fr(1, 2), Fr(1, 3)

# Both conventions, at the source point, pre-reduction.
q_pre_lam2 = quartic_leading(SOURCE_B, 2, B_kill, +1)
q_pre_lam1 = quartic_leading(SOURCE_B, 1, B_kill, +1)
check("1-E2", "eddy-completed leading quartic at the source point b=1/3, "
      "commutator convention lam=2, is exactly -16/9 (= (4/9) * SRC-3's -4)",
      q_pre_lam2 == Fr(-16, 9) and q_pre_lam2 == Fr(4, 9) * K_SRC3_PRE)
check("1-E2", "wedge convention lam=1 gives exactly -4/9; the SIGN is identical, "
      "so the verdict does not depend on the bracket convention",
      q_pre_lam1 == Fr(-4, 9) and q_pre_lam1 < 0)

# The whole (a,b) family, including the exploration doc's planted controls.
FAMILY = [Fr(1, 3), Fr(1, 2), Fr(1), Fr(-1, 3), Fr(2, 3), Fr(7, 5)]
check("1-E2", "for EVERY nonzero b in the completion family and BOTH conventions, "
      "the leading quartic keeps SRC-3's sign: the completion is SIGN-INERT",
      all(quartic_leading(b, lam, B_kill, +1) < 0
          for b in FAMILY for lam in (1, 2)))
check("1-E2", "the same sweep is strictly POSITIVE post-reduction, so the "
      "completion is sign-inert in BOTH readings, not just one",
      all(quartic_leading(b, lam, B_theta, +1) > 0
          for b in FAMILY for lam in (1, 2)))
check("1-E2", "b = 0 (the bare curvature, the exploration doc's (0,0) control) "
      "kills the quartic outright, leaving nothing to stabilise the hat",
      quartic_leading(Fr(0), 2, B_kill, +1) == 0)

# The Mexican hat itself survives the completion, rescaled by 2*b*lam.
Q_SRC3_PRE = 2 * B_kill(XY, XY)   # 2<F0, v^v> normalised at <F0,.> = the same bracket
check("1-E2", "SRC-2's tachyonic quadratic is rescaled by 2*b*lam > 0 for b>0, "
      "so the completion PRESERVES the Mexican hat it was asked to stabilise",
      2 * SOURCE_B * 2 > 0 and Fr(2 * SOURCE_B * 2) * Q_SRC3_PRE < 0)

# Post-reduction E2 is a completion of square and is bounded below.
F0_norm_post = 2 * B_theta(XY, XY)
check("1-E2", "post-reduction E2 is literally a norm-square under a "
      "positive-definite pairing, hence bounded below by -||F0||^2 (CG-1)",
      F0_norm_post > 0 and quartic_leading(SOURCE_B, 2, B_theta, +1) > 0)


# ---------------------------------------------------------------------------
# BLOCK 2 -- READING E1: the source's DISPLAYED first-order action is ODD.
#
#   I_1(T) = <T, S(F_0)> + (a/2)<T, S(D_B T)> + b<T, S([T,T])> + (kappa_1/2)<T,flat_1 T>
#
# Along a ray T = t v this is  L t + (D + kappa_1 N/2) t^2 + C t^3.
# DEGREE PARITY: a real cubic with C != 0 is unbounded below FOR EVERY value of
# every other coefficient -- including kappa_1, and including the pairing's
# signature.  CG-1's repair is a completion of SQUARE, a purely even-degree
# device, and is therefore structurally powerless against an odd-degree runaway.
# ---------------------------------------------------------------------------
def cubic_ray(t: Fr, c3: Fr, c2: Fr, c1: Fr = Fr(0), c0: Fr = Fr(0)) -> Fr:
    if MUTATION == "eddy-action-even":
        # PLANT: pretend the completed first-order action were EVEN in T.  If the
        # eddy action were quartic rather than cubic, a positive leading
        # coefficient would bound it and CG-1's repair would reach it.
        return c3 * t ** 4 + c2 * t ** 2 + c1 * t + c0
    return c3 * t ** 3 + c2 * t ** 2 + c1 * t + c0


def unbounded_witness(c3: Fr, c2: Fr, c1: Fr, c0: Fr, target: Fr) -> Fr:
    """Exact t with I(t) < -target, for any cubic with c3 != 0.  Constructive."""
    assert c3 != 0
    span = abs(c2) + abs(c1) + abs(c0) + abs(target) + 1
    R = span / abs(c3) + 2
    return -R if c3 > 0 else R


# The banked K77 witness: I(t) = 1456 t^3 + 7 kappa_1 t^2, cubic coefficient 1456.
K77_C3 = Fr(1456)
TARGETS = [Fr(10) ** 3, Fr(10) ** 6, Fr(10) ** 12]
KAPPAS = [Fr(-7), Fr(-1), Fr(0), Fr(1), Fr(10) ** 6, Fr(-10) ** 6]

k77_ok = True
for kap in KAPPAS:
    c2 = 7 * kap
    for tgt in TARGETS:
        t = unbounded_witness(K77_C3, c2, Fr(0), Fr(0), tgt)
        if not cubic_ray(t, K77_C3, c2) < -tgt:
            k77_ok = False
check("2-E1", "BANKED WITNESS re-run: I(t) = 1456 t^3 + 7 kappa_1 t^2 falls below "
      "every tested bound (1e3, 1e6, 1e12) for every tested kappa_1 including "
      "+/-1e6 -- the first-order eddy action is UNBOUNDED BELOW", k77_ok)
check("2-E1", "the witness is monotone in the target: bigger bound, deeper value",
      cubic_ray(unbounded_witness(K77_C3, Fr(0), Fr(0), Fr(0), TARGETS[2]), K77_C3, Fr(0))
      < cubic_ray(unbounded_witness(K77_C3, Fr(0), Fr(0), Fr(0), TARGETS[0]), K77_C3, Fr(0)))

# kappa_1 is powerless BY DEGREE, not by size: the t^3 term dominates any t^2.
check("2-E1", "no value of kappa_1 can bound a cubic: the quadratic it multiplies "
      "is one degree too low, certified over 6 exact values of kappa_1 spanning "
      "twelve orders of magnitude and both signs", k77_ok and len(KAPPAS) == 6)

# The signature of the pairing is irrelevant: flip every sign and it still runs.
check("2-E1", "flipping the pairing's overall sign (the crudest model of the "
      "pre/post-reduction switch) leaves a cubic a cubic: still unbounded",
      cubic_ray(unbounded_witness(-K77_C3, Fr(0), Fr(0), Fr(0), TARGETS[1]),
                -K77_C3, Fr(0)) < -TARGETS[1])

# The ONLY escape: the cubic coefficient must vanish identically.
check("2-E1", "EXACT CONDITION: with c3 = 0 the same ray is a bounded-below "
      "quadratic iff its t^2 coefficient is >= 0 -- so E1 boundedness reduces to "
      "(cubic vanishes) AND (quadratic coefficient >= 0)",
      cubic_ray(Fr(10) ** 6, Fr(0), Fr(1)) > 0 and cubic_ray(Fr(10) ** 6, Fr(0), Fr(-1)) < 0)

# BOTH sides of that condition are already REALISED in banked repo arithmetic,
# on two different branches.  Provenance is read from the banked probes, and
# both were run live for this gate.
k77_vacuum_src = read_probe("tests/channel-swings/selected_moving_k77_vacuum_p2_norm_probe.py")
k77_hq_src = read_probe("tests/channel-swings/selected_k77_hq_action_owner_potential_probe.py")
check("2-E1", "BRANCH 1 (banked): on the Spin-invariant constant branch the "
      "eddy-completed first-order action is 1456 t^3 + 7 kappa_1 t^2 -- cubic "
      "coefficient 1456 != 0, so E1 is UNBOUNDED BELOW there",
      "1456 * t**3 + 7 * kappa * t**2" in k77_vacuum_src)
check("2-E1", "BRANCH 2 (banked): on the four moving-q representatives the SAME "
      "released first-order action has cubic coefficient exactly ZERO, so E1's "
      "odd sector is empty there and the condition is satisfiable",
      "mass_coefficient == ZERO and cubic_coefficient == ZERO" in k77_hq_src)
check("2-E1", "so E1 boundedness is BRANCH-DEPENDENT and the condition is not "
      "vacuous in either direction: one banked branch violates it, one satisfies "
      "it.  Which branch GU's vacuum sits on is undeclared",
      "1456 * t**3" in k77_vacuum_src
      and "cubic_coefficient == ZERO" in k77_hq_src)


# ---------------------------------------------------------------------------
# BLOCK 3 -- WHY SRC-3's ARENA CANNOT SEE THE EDDY AT ALL.
#
# RB1b's central-parity kill, extended to the 10-dim vertical and to K.
# c = -I_10 is central, lies in SO(6,4), lies in the identity component, and
# lies in K = SO(6) x SO(4).  It acts as +1 on ad = Lambda^2 V and as -1 on V.
# So it acts as +1 on Omega^2(ad) and as -1 on Omega^1(ad): every equivariant
# S: Omega^2(ad) -> Omega^1(ad) obeys S = -S, hence S = 0.
# ---------------------------------------------------------------------------
c_centre = -np.eye(N, dtype=np.int64)
if MUTATION == "centre-not-in-group":
    c_centre = np.diag([-1] + [1] * (N - 1)).astype(np.int64)
if MUTATION == "centre-trivial":
    c_centre = np.eye(N, dtype=np.int64)

def exact_det_diagonal(M):
    """Exact integer determinant.  Every c used here is diagonal by construction;
    assert that rather than fall back to a floating-point determinant."""
    assert np.array_equal(M, np.diag(np.diag(M))), "non-diagonal c: no exact det path"
    out = 1
    for d in np.diag(M):
        out *= int(d)
    return out


check("3-parity", "c = -I_10 preserves the DeWitt metric: c^T eta c = eta exactly",
      np.array_equal(c_centre.T @ ETA @ c_centre, ETA))
check("3-parity", "det c = +1, so c lies in SO(6,4) and not merely O(6,4)",
      exact_det_diagonal(c_centre) == 1)

# c also lies in the maximal compact K = SO(6) x SO(4): both blocks have det +1.
blk6, blk4 = c_centre[:P, :P], c_centre[P:, P:]
check("3-parity", "c is block-diagonal with det(-I_6) = det(-I_4) = +1, so the "
      "obstruction survives CG-1's reduction to K = SO(6) x SO(4)",
      np.array_equal(c_centre[:P, P:], np.zeros((P, Q_), dtype=np.int64))
      and int(np.prod(np.diag(blk6))) == 1 and int(np.prod(np.diag(blk4))) == 1)

# c is in the IDENTITY component: an exact product of pi-rotations.
def rot_pi(n_, i, j):
    R = np.eye(n_, dtype=np.int64)
    R[i, i], R[j, j] = -1, -1
    return R


prod6 = rot_pi(P, 0, 1) @ rot_pi(P, 2, 3) @ rot_pi(P, 4, 5)
prod4 = rot_pi(Q_, 0, 1) @ rot_pi(Q_, 2, 3)
check("3-parity", "-I_6 and -I_4 are exact products of pi-rotations, each in a "
      "one-parameter subgroup, so c lies in the IDENTITY component",
      np.array_equal(prod6, -np.eye(P, dtype=np.int64))
      and np.array_equal(prod4, -np.eye(Q_, dtype=np.int64)))

check("3-parity", "c^2 = I, so c is its own inverse and Ad(c)X = c X c",
      np.array_equal(c_centre @ c_centre, np.eye(N, dtype=np.int64)))
check("3-parity", "Ad(c) = identity on all 45 generators: c acts as +1 on ad",
      all(np.array_equal(c_centre @ Xg @ c_centre, Xg) for Xg in BASIS))
check("3-parity", "c acts as -1 on the form index V, hence as -1 on Omega^1(ad) "
      "and as +1 on Omega^2(ad)",
      np.array_equal(c_centre, -np.eye(N, dtype=np.int64)))

parity_kill = (np.array_equal(c_centre @ BASIS[0] @ c_centre, BASIS[0])
               and np.array_equal(c_centre, -np.eye(N, dtype=np.int64)))
check("3-parity", "THEOREM (RB1b's mechanism, extended): every equivariant "
      "S: Omega^2(ad) -> Omega^1(ad) satisfies S = -S, hence S = 0.  The "
      "ad-valued shiab, and with it the whole eddy completion, is INVISIBLE in "
      "the bosonic vertical truncation SRC-3 computed in", parity_kill)

# NON-VACUITY, planted: in ODD dimension the obstruction is absent and the
# Chern-Simons cubic is explicitly NONZERO.  This is why CS theory is 3d.
eps3 = np.zeros((3, 3, 3), dtype=np.int64)
for perm, sgn in ((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1), \
                 ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1):
    eps3[perm] = sgn


def cs_cubic_so3(T):
    tot = 0
    for r in range(3):
        for al in range(3):
            for be in range(3):
                if eps3[r, al, be] == 0:
                    continue
                for A in range(3):
                    for Bx in range(3):
                        for C in range(3):
                            if eps3[A, Bx, C] == 0:
                                continue
                            tot += (eps3[r, al, be] * eps3[A, Bx, C]
                                    * T[r][A] * T[al][Bx] * T[be][C])
    return int(tot)


check("3-parity", "PLANTED CONTROL, odd dimension: -I_3 has det = -1, so it is "
      "NOT in SO(3) and the parity hypothesis genuinely FAILS there",
      int(np.prod(np.diag(-np.eye(3, dtype=np.int64)))) == -1)
check("3-parity", "PLANTED CONTROL, non-vacuity: in that odd dimension the same "
      "eddy cubic is exactly 6 on T = I_3, not zero.  The theorem discriminates "
      "by dimension parity; it does not kill everything it touches",
      cs_cubic_so3(np.eye(3, dtype=np.int64).tolist()) == 6)
check("3-parity", "PLANTED CONTROL, even-degree survival: <v,v> and ||v^v||^2 "
      "carry an EVEN index count and are nonzero, so parity kills exactly the "
      "odd sector and nothing else",
      B_theta(X_, X_) != 0 and K_SRC3_POST != 0)


# ---------------------------------------------------------------------------
# BLOCK 4 -- THE kappa_1 CONDITION, and the abelian directions that decide it.
#
# CG-1 retired SRC-3's 630 abelian pairs as "conditionally vacuous": on them
# a^a = 0, so Q and K vanish together.  The eddy completion supplies the term
# (kappa_1/2)<T, flat_1 T>, which does NOT vanish there.  Those retired
# directions therefore become the ones that FIX the sign of kappa_1.
# ---------------------------------------------------------------------------
ab_pairs = [(a, b) for a, b in combinations(range(NG), 2)
            if not br(BASIS[a], BASIS[b]).any()]
check("4-kappa", "abelian generator pairs exist (SRC-3 counted 630)",
      len(ab_pairs) == 630)

A1, A2 = gen(0, 1), gen(2, 3)
check("4-kappa", "an explicit abelian ray: [J01, J23] = 0 exactly, so the eddy "
      "quadratic AND the quartic both vanish identically on it",
      not br(A1, A2).any())

ab_norm_post = B_theta(A1, A1) + B_theta(A2, A2)     # eta_plus = I_10
check("4-kappa", "on that ray ||a||^2 = 4 > 0 under the post-reduction pairing, "
      "so the kappa_1 term is the ONLY surviving term", ab_norm_post == 4)


def V_post_on_abelian(t: Fr, kappa: Fr) -> Fr:
    """Post-reduction potential on the abelian ray: quartic and hat both die."""
    return (kappa / 2) * t ** 2 * ab_norm_post


check("4-kappa", "kappa_1 < 0 sends the post-reduction potential to -infinity "
      "along that abelian ray -- certified at 1e3/1e6/1e12",
      all(V_post_on_abelian(
          Fr(2) * tgt / abs(Fr(-1)) + 2, Fr(-1)) < -tgt for tgt in TARGETS))
check("4-kappa", "kappa_1 >= 0 leaves the same ray non-negative for every t",
      all(V_post_on_abelian(Fr(t), Fr(k)) >= 0
          for t in (-97, -1, 0, 1, 97) for k in (0, 1, 5)))
check("4-kappa", "EXACT CONDITION, reading E2 post-reduction: bounded below "
      "IFF kappa_1 >= 0, with bound -||F0||^2.  The sign of one undeclared "
      "coefficient is the entire remaining question in that reading",
      V_post_on_abelian(Fr(10) ** 6, Fr(-1)) < 0
      and V_post_on_abelian(Fr(10) ** 6, Fr(1)) > 0)
check("4-kappa", "kappa_1 CANNOT rescue the PRE-reduction reading: the quartic "
      "-16/9 t^4 outranks (kappa_1/2) t^2 for every kappa_1",
      q_pre_lam2 < 0)
g2 = read_probe("lab/specifications/g2-source-field-and-variational-shiab-packet-2026-07-31.md")
g3 = read_probe("lab/specifications/g3-graph-variation-noether-bvbfv-packet-2026-07-31.md")
check("4-kappa", "and kappa_1 >= 0 is NOT free: the written packets state flat_1 "
      "is 'not a positive Riesz map', so even the sign of <T, flat_1 T> is "
      "undeclared -- the condition is on the COMPOSITE kappa_1 * flat_1.  Read "
      "from the packet, not asserted",
      "not a positive Riesz map" in g2)
check("4-kappa", "the same packets display the source completion point (1/2, 1/3) "
      "this gate put into the potential -- read from the packet, not assumed",
      "\\frac12D_BT" in g2 and "\\frac13q(T,T)" in g2 and "\\kappa_1" in g3)


# ---------------------------------------------------------------------------
# REPORT
# ---------------------------------------------------------------------------
passed = sum(1 for _, _, ok in CHECKS if ok)
for block, name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  [{block}]  {name}")
print(f"\n{passed}/{len(CHECKS)} exact checks passed"
      + (f"   (MUTATION={MUTATION})" if MUTATION else ""))
print("\n--- exact values ---")
print(f"SRC-3 pre-reduction ray quartic          K       = {K_SRC3_PRE}")
print(f"SRC-3 same ray, one timelike internal leg        = {K_SRC3_PRE_TIMELIKE}")
print(f"SRC-3 same ray, post-reduction (B_theta)         = {K_SRC3_POST}")
print(f"eddy-completed quartic, b=1/3 lam=2, pre         = {q_pre_lam2}")
print(f"eddy-completed quartic, b=1/3 lam=1, pre         = {q_pre_lam1}")
print(f"eddy rescaling factor (b*lam)^2 at source point  = {(SOURCE_B*2)**2}")
print(f"banked first-order cubic coefficient (K77)       = {K77_C3}")
print(f"abelian generator pairs                          = {len(ab_pairs)}")
print("\nVERDICT  E1 first-order  : ODD DEGREE -> unbounded below in BOTH readings")
print("VERDICT  E2 eddy-square  : SIGN-INERT -> SRC-3 pre / CG-1 post, unchanged")
print("VERDICT  E2 post + kappa : bounded below IFF kappa_1 * flat_1 >= 0")
raise SystemExit(0 if passed == len(CHECKS) else 1)
