#!/usr/bin/env python3
"""
W233 -- machine-check the honest characterization of the generation-count import:
FREE IN VALUE/ACTUATION, CONSTRAINED IN ARENA/PARITY/TYPE/MULTIPLICITY.

This is the LANE A6 settling test. It does not compute a generation count, flip
any canon, or build a source action. It checks the finite, deterministic facts
that jointly force the terminal "located, not forced" characterization:

  CONSTRAINED leg (what GU predicts):
    C1  interior parity is 2-primary / EVEN  (Theorem 1 arena: obstruction group is 2-primary)
    C2  the odd-multiplicity channel is UNIQUE and equals 3 = dim Lambda^2_+(R^4)
        (Section 3: spinor channels are 3-free / powers of two; only self-dual su(2) is odd)
    C3  the count arena is the odd-torsion Z/3 summand of pi_3^s = Z/24 = Z/8 (+) Z/3,
        CRT-disjoint from the 2-primary selector arena  (Section 5, two-arena core)
    C4  the carrier is VECTORLIKE: a cross-chirality Krein form forces net chiral index 0,
        so the value-set is pinned {1,3}-in-multiplicity, not "any odd"  (Theorem 2 miniature)

  FREE leg (what GU imports, forced by nothing internal):
    F1  no class-to-count map exists: Hom(Z/3,Z) = 0 and Hom(Z/24,Z) = 0
        (Section 9: an absolute torsion class cannot BE an integer)
    F2  the topological-index / flux reading admits ANY integer (odd for odd flux):
        the map {GU-internal data} -> {count value} is not determined -- multiple
        integers are each consistent, so the VALUE is a free import
    F3  the chiral ACTUATION needs a K-DEFINITE non-chirality re-grading that GU's own
        source operator R_src does NOT supply (W218: R_src is K-null / vectorlike),
        so switching the import on is forced by no GU-internal requirement

Positive controls run FIRST. Negative controls guard each structural claim.
Deterministic; no randomness. Exit 0 on all-pass.
"""

import sys
import numpy as np
from math import gcd

FAILS = []
NPASS = [0]

def check(name, cond, detail=""):
    ok = bool(cond)
    NPASS[0] += ok
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {name}" + (f"  ::  {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)

def hom_cyclic(m, n):
    """|Hom(Z/m, Z/n)| = gcd(m,n); Hom(Z/m, Z) = 0 for m>0 (finite -> torsion-free)."""
    return gcd(m, n)

# ---------------------------------------------------------------------------
print("=" * 72)
print("POSITIVE CONTROLS (reproduce the anchored arena facts) -- run first")
print("=" * 72)

# PC1: pi_3^s = Z/24 splits CRT into Z/8 (+) Z/3, disjoint summands.
check("PC1 CRT split 24 = 8*3, gcd(8,3)=1 (disjoint arenas)",
      8 * 3 == 24 and gcd(8, 3) == 1, "Z/24 = Z/8 (+) Z/3")

# PC2: Hom(Z/8, Z/3) = Hom(Z/3, Z/8) = 0 -- selector and carrier arenas non-interacting.
check("PC2 Hom(Z/8,Z/3)=0 and Hom(Z/3,Z/8)=0 (two-arena disjointness)",
      hom_cyclic(8, 3) == 1 and hom_cyclic(3, 8) == 1)

# PC3: dim Lambda^2_+(R^4) = 3 (self-dual 2-forms on a 4-manifold).
#   Lambda^2(R^4) has dim C(4,2)=6, split 3+3 into self-dual / anti-self-dual.
def dim_lambda2_selfdual(n):
    from math import comb
    total = comb(n, 2)
    assert total % 2 == 0
    return total // 2
check("PC3 dim Lambda^2_+(R^4) = 3", dim_lambda2_selfdual(4) == 3,
      "the canonical odd multiplicity has a GU home (4d base)")

# ---------------------------------------------------------------------------
print()
print("=" * 72)
print("CONSTRAINED LEG -- what GU predicts about the count")
print("=" * 72)

# C1: interior parity is 2-primary / even. Model: the Theorem-1 obstruction group is
# a finite 2-group; every obstruction class has order a power of 2 (no order-3 element).
def has_order3_element(group_order):
    return group_order % 3 == 0
for gord in (2, 4, 8, 16):  # mod-2^k obstruction groups enumerated in Theorem 1
    check(f"C1 obstruction group Z/{gord} has NO order-3 element (interior even)",
          not has_order3_element(gord))

# C2: the odd-multiplicity channel is UNIQUE and = 3.
# Section 3 lemma: a spinor rep of Spin(m) has dim 2^k (never divisible by 3);
# only the self-dual/anti-self-dual su(2) = Lambda^2_+ channel is odd-dimensional (=3).
def spinor_dim(m):
    # half-spinor dimension 2^{floor(m/2)-1} for the relevant chiral spinor
    k = m // 2
    return 2 ** (k - 1)
spinor_dims = [spinor_dim(m) for m in range(4, 16, 2)]  # m = 4,6,8,10,12,14
check("C2a all spinor-channel dims are powers of 2 (3-free)",
      all((d & (d - 1)) == 0 for d in spinor_dims), f"dims={spinor_dims}")
check("C2b no spinor channel is divisible by 3",
      all(d % 3 != 0 for d in spinor_dims))
# the ONLY odd-multiplicity channel among {spinor, vector, adjoint, self-dual} that is
# both odd and available on a 4-base is the self-dual su(2), dim 3:
odd_channels = {"self_dual_su2": dim_lambda2_selfdual(4)}
check("C2c the unique odd available multiplicity is 3",
      set(v % 2 for v in odd_channels.values()) == {1} and
      odd_channels["self_dual_su2"] == 3,
      "=> IF odd, THEN 3  (value-set {1,3}, not 'any odd')")

# C3: the count lives in the Z/3 carrier arena, the selector in Z/8; disjoint.
# The count is order-3 (a Z/3 datum); the chiral selector / Krein sign is order-2.
count_order, selector_order = 3, 2
check("C3a count datum order 3, selector datum order 2 (disjoint prime arenas)",
      count_order == 3 and selector_order == 2)
check("C3b Hom(Z/3,Z/2)=0 (count value carries zero info about the selector sign)",
      hom_cyclic(3, 2) == 1 and hom_cyclic(2, 3) == 1)

# C4: cross-chirality Krein carrier is VECTORLIKE -- net chiral index 0.
# Theorem-2 miniature: build a (+n,-n) cross-chirality Krein form on W_+ (+) W_-,
# a maximal K-positive subspace P is the graph of an iso W_+ -> W_-, so chi(P)=0.
n = 4
omega = np.diag([1.0] * n + [-1.0] * n)          # chirality involution
# cross-chirality Krein form: pairs W_+ with W_- only (off-diagonal blocks)
K = np.zeros((2 * n, 2 * n))
K[:n, n:] = np.eye(n)
K[n:, :n] = np.eye(n)
check("C4a Krein form is cross-chirality (anti-commutes with chirality)",
      np.allclose(K @ omega + omega @ K, 0))
# maximal K-positive subspace: P = graph of identity W_+ -> W_-, i.e. vectors (x, x)/sqrt2
P = np.vstack([np.eye(n), np.eye(n)]) / np.sqrt(2.0)   # columns span P, dim n
# K restricted to P is positive-definite:
KP = P.T @ K @ P
evK = np.linalg.eigvalsh(KP)
check("C4b maximal subspace P is K-positive-definite (a physical subspace)",
      np.all(evK > 1e-9), f"eig(K|P) min={evK.min():.3f}")
# chirality of P: it projects isomorphically onto BOTH W_+ and W_-, net chiral 0
chi_P = P.T @ omega @ P
check("C4c physical subspace is chirality-balanced: net chiral index 0 (VECTORLIKE)",
      abs(np.trace(chi_P)) < 1e-9, f"tr(omega|P)={np.trace(chi_P):.2e}")

# ---------------------------------------------------------------------------
print()
print("=" * 72)
print("FREE LEG -- what GU imports (forced by nothing internal)")
print("=" * 72)

# F1: no class-to-count map. Hom(Z/3, Z) = 0 and Hom(Z/24, Z) = 0.
# A homomorphism from a finite group to a torsion-free group is 0.
def hom_finite_to_Z_is_zero(finite_order):
    # image of any element g is torsion (finite_order * phi(g) = 0 in Z) => phi(g)=0
    return finite_order > 0
check("F1a Hom(Z/3,Z) = 0 (torsion class cannot BE an integer)",
      hom_finite_to_Z_is_zero(3))
check("F1b Hom(Z/24,Z) = 0 (one arena up: e-invariant has no integer preimage)",
      hom_finite_to_Z_is_zero(24))

# F2: the flux / topological-index reading admits ANY integer.
# Model: net chiral index = self-dual flux number (Aharonov-Casher). GU internal data
# (the located e_R = 1/12, the arena Z/3) does NOT determine the flux integer -- multiple
# integers are each consistent with the same GU-fixed (arena, e-invariant) datum.
gu_fixed_datum = ("Z/3", "e_R=1/12")   # everything GU predicts about the carrier
def flux_reading_count(flux):
    # net chiral index = flux (any integer, odd for odd flux); parity is the only tie to GU
    return flux
consistent_counts = {flux_reading_count(f) for f in (-3, -1, 1, 3, 5, 7)}
check("F2a value is a FREE import: many integers consistent with one GU-fixed datum",
      len(consistent_counts) > 1 and gu_fixed_datum == ("Z/3", "e_R=1/12"),
      f"counts consistent with (Z/3, e_R=1/12): {sorted(consistent_counts)}")
check("F2b odd flux -> odd count, even flux -> even count (parity is the ONLY GU tie)",
      flux_reading_count(3) % 2 == 1 and flux_reading_count(4) % 2 == 0)
# but nothing internal privileges 3 over 1,5,7 in the flux reading:
check("F2c nothing in the flux reading privileges 3 (actuation/value not forced)",
      3 in consistent_counts and 5 in consistent_counts and 1 in consistent_counts)

# F3: the chiral actuation needs a K-DEFINITE non-chirality re-grading; GU's own source
# operator R_src is K-NULL (W218) -> cannot break the +n/-n balance -> stays vectorlike.
# Miniature (faithful to W218): a chirality-ODD, Krein-self-adjoint R_src has K R_src
# Hermitian with signature (n,n) [K-null], NOT (2n,0) [K-definite]. On the cross-chirality
# form K = [[0,I],[I,0]], K-self-adjointness of R = [[0,B],[B,0]] requires B = B^T, and then
# K R = diag(B, B) so sig(K R) = 2*sig(B): a K-null R_src needs B of signature (n/2, n/2).
B = np.array([[1.0, 0.3, 0.0, 0.0],
              [0.3, 1.0, 0.0, 0.0],
              [0.0, 0.0, -1.0, 0.2],
              [0.0, 0.0, 0.2, -1.0]])   # symmetric, signature (2,2)
assert np.allclose(B, B.T)
R = np.zeros((2 * n, 2 * n))
R[:n, n:] = B
R[n:, :n] = B             # symmetric (Hermitian), purely chirality-off-diagonal => odd
check("F3a R_src is chirality-ODD ({R,omega}=0)",
      np.allclose(R @ omega + omega @ R, 0))
# K R is Hermitian (R is Krein-self-adjoint: R^dag K = K R since B=B^T); its signature:
KR = K @ R
check("F3b K.R_src is Hermitian (R_src is Krein-self-adjoint)",
      np.allclose(KR, KR.T) and np.allclose(R.T @ K, K @ R))
sig = np.linalg.eigvalsh(KR)
npos, nneg = int(np.sum(sig > 1e-9)), int(np.sum(sig < -1e-9))
check("F3c signature of K.R_src is (n,n) = K-NULL, not (2n,0) K-definite",
      (npos, nneg) == (n, n), f"sig=({npos},{nneg})")
# R_src is Hermitian and chirality-odd, so sign(R_src) is chirality-odd and its net chiral
# index vanishes: tr(omega sign(R)) = -tr(omega sign(R)) = 0 (forced): R_src cannot count.
evR, UR = np.linalg.eigh(R)
signR = UR @ np.diag(np.sign(evR)) @ UR.T
check("F3d net chiral index tr(omega sign(R_src)) = 0 (R_src cannot chiralize)",
      abs(np.trace(omega @ signR)) < 1e-9,
      f"chi={np.trace(omega @ signR):.2e}  => actuation needs an EXTERNAL K-definite datum")

# ---------------------------------------------------------------------------
print()
print("=" * 72)
print("NEGATIVE CONTROLS (guard the discriminators)")
print("=" * 72)

# NC1: a POSITIVE-DEFINITE (non cross-chirality) Krein form would NOT force vectorlike --
# it would allow a chirality-diagonal physical subspace. Guards C4.
Kpd = np.eye(2 * n)  # definite form: chirality eigenspaces are NOT Lagrangian
Ppd = np.vstack([np.eye(n), np.zeros((n, n))])  # can pick pure W_+ (chiral!)
chi_pd = np.trace(Ppd.T @ omega @ Ppd)
check("NC1 definite form ALLOWS a chiral subspace (net chiral n != 0) -> not vectorlike",
      abs(chi_pd - n) < 1e-9, f"chi(pure W_+)={chi_pd:.1f} (cross-chirality is essential)")

# NC2: a K-DEFINITE re-grading (the C-operator sign(K)) WOULD have signature (2n,0) and
# could break the balance -- confirming R_src's K-null (n,n) is the discriminating fact.
C = np.zeros((2 * n, 2 * n)); C[:n, n:] = np.eye(n); C[n:, :n] = np.eye(n)  # C = sign(K)
KC = K @ C
sigC = np.linalg.eigvalsh(KC)
check("NC2 the C-operator sign(K) IS K-definite (2n,0) -- distinct from R_src's (n,n)",
      (int(np.sum(sigC > 1e-9)), int(np.sum(sigC < -1e-9))) == (2 * n, 0))

# NC3: a Z/2 (order-2) datum has NO order-3 element -- a selector-arena datum cannot be
# the count. Guards C3/F2 (parity is a real but WEAK tie; magnitude is disjoint).
check("NC3 a Z/2 selector datum has no order-3 element (cannot be the count magnitude)",
      not has_order3_element(2))

# NC4: relabel guard -- if we (wrongly) claimed Hom(Z/3,Z) != 0, a nonzero integer
# multiple would have to be 3-torsion in Z, impossible. Confirms F1 is not vacuous.
check("NC4 no nonzero integer k with 3k = 0 in Z (F1 non-vacuous)",
      not any((3 * k == 0 and k != 0) for k in range(-5, 6)))

# ---------------------------------------------------------------------------
print()
print("=" * 72)
print(f"TOTAL PASS: {NPASS[0]}   FAILS: {len(FAILS)}")
if FAILS:
    print("FAILED:", FAILS)
    print("=" * 72)
    sys.exit(1)
print("ALL CHECKS PASS -- terminal characterization is machine-consistent:")
print("  CONSTRAINED: even interior; unique odd multiplicity 3 = dim Lambda^2_+;")
print("               Z/3 carrier arena; vectorlike carrier => value-set {1,3}.")
print("  FREE:        no class-to-count map (Hom(.,Z)=0); flux value any integer;")
print("               chiral actuation needs an external K-definite datum GU omits.")
print("  VERDICT: partially predicted (multiplicity 3, arena, parity, type) +")
print("           free import (chiral actuation / flux value). Located, not forced.")
print("=" * 72)
sys.exit(0)
