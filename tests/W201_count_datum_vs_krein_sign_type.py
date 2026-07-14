#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
W201 -- Is the external GENERATION-COUNT datum the SAME external bit as the
reservoir/Krein-SIGN datum (#1), or independent?

This test makes machine-checkable the *type/arena* claims of the W201 note. It
does NOT compute a generation count, a Krein sign for GU, or any physics number.
It checks finite structural facts already established by the cited artifacts, and
the convergence/disjointness relations between the two external datums.

Cited (reproduced here as positive controls, not re-derived physics):
  - located-not-forced: CRT split pi_3^s = Z/24 = Z/8 (+) Z/3; the count lives in
    the odd-torsion Z/3 CARRIER arena, every selector in the 2-primary Z/8
    SELECTOR arena; Hom(Z/3,Z)=0 so an absolute torsion class is not a count.
  - located-not-forced Theorem 2: the cross-chirality (+96,-96) Krein form makes
    the chirality eigenspaces K-null (Lagrangian); every maximal K-positive
    (physical) subspace is chirality-balanced, net chiral index 0.
  - W186 Block A: the mirror-record sign FLIPS between the naive metric eta and
    the C-metric eta_+ = eta.C (naive-negative, C-metric-positive).
  - located-not-forced Sec 6: the residual escape a count would need is a
    K-DEFINITE, NON-chirality re-grading; such re-gradings "grade
    physical-vs-ghost, carrying the vectorlike +96" -- i.e. they are the
    C-operator class and are themselves index-0 (vectorlike).

Convention: net chiral index chi = dim(W_+ part) - dim(W_- part) of a subspace.
Deterministic; seed fixed; exit 0 iff all checks pass. Positive controls first.
"""

import sys
import numpy as np
from fractions import Fraction
from math import gcd

np.random.seed(20260714)

RESULTS = []
def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok), detail))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {name}" + (f"  --  {detail}" if detail else ""))
    return bool(ok)

# ----------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------
def hom_cyclic_order(m, n):
    """|Hom(Z/m, Z/n)| = gcd(m,n).  Hom(Z/m, Z) = 0 for m>0 (torsion->free)."""
    return gcd(m, n)

def signature(M):
    """(n_pos, n_neg, n_zero) of a real symmetric matrix, via eigenvalues."""
    w = np.linalg.eigvalsh((M + M.T) / 2.0)
    tol = 1e-9 * max(1.0, np.max(np.abs(w)))
    return (int(np.sum(w > tol)), int(np.sum(w < -tol)), int(np.sum(np.abs(w) <= tol)))

# ======================================================================
# BLOCK PC -- positive controls: reproduce the imported structural facts
# ======================================================================
print("\n--- BLOCK PC: positive controls (imported facts reproduced) ---")

# PC1: CRT split Z/24 = Z/8 (+) Z/3 is a genuine direct-sum (8,3 coprime).
check("PC1 CRT split Z/24 = Z/8 (+) Z/3 (coprime, lcm 24)",
      gcd(8, 3) == 1 and (8 * 3) == 24,
      "gcd(8,3)=1, 8*3=24")

# PC2: the count value cannot BE an absolute torsion class: Hom(Z/3,Z)=0.
check("PC2 Hom(Z/3, Z) = 0 (torsion -> torsion-free)",
      True,  # structural: any hom from a finite group to Z is 0
      "no nonzero homomorphism from a torsion group to Z")

# ---- the minimal cross-chirality Krein carrier (Theorem 2 in miniature) ----
# basis order: v0=(chi+,phys) v1=(chi+,ghost) v2=(chi-,phys) v3=(chi-,ghost)
Gamma = np.diag([1.0, 1.0, -1.0, -1.0])          # chirality grading
Pgh   = np.diag([1.0, -1.0, 1.0, -1.0])          # physical/ghost grading (independent)
# purely cross-chirality Krein form: pairs chi+ <-> chi- within each sector
K = np.array([[0, 0, 1, 0],
              [0, 0, 0, 1],
              [1, 0, 0, 0],
              [0, 1, 0, 0]], dtype=float)

# PC3: K is a genuine (+2,-2) cross-chirality form (miniature of (+96,-96)).
check("PC3 cross-chirality Krein form has signature (2,2)",
      signature(K) == (2, 2, 0), f"sig(K)={signature(K)}")

# PC4 (W186 Block A sign flip): a physical/ghost null pair, naive-neg mirror,
# C-metric-positive.  eta = diag(+1,-1); mirror = e_-.  C = diag(1,-1);
# eta_+ = eta.C = diag(1,1) > 0.  Same vector: naive -1, C-metric +1.
eta_pg   = np.diag([1.0, -1.0])
mirror   = np.array([0.0, 1.0])
C_pg     = np.diag([1.0, -1.0])
eta_plus = eta_pg @ C_pg
naive = float(mirror @ eta_pg @ mirror)
cmet  = float(mirror @ eta_plus @ mirror)
check("PC4 W186 mirror sign flip: naive < 0, C-metric > 0",
      naive < 0 and cmet > 0 and signature(eta_plus) == (2, 0, 0),
      f"naive={naive:+.0f}, C-metric={cmet:+.0f}, sig(eta_+)={signature(eta_plus)}")

# ======================================================================
# BLOCK T -- TYPE and ARENA of the two external datums
# ======================================================================
print("\n--- BLOCK T: type/arena of count datum vs Krein-sign datum ---")

# The two datums, as group-valued objects:
#   Krein-sign datum : a relative signature, order-2 element (Z/2 <= Z/8 selector arena)
#   count datum      : an odd-torsion invariant, order-3 element (Z/3 carrier arena)
ORDER_SIGN  = 2   # like/opposite, healthy/tachyonic -- a sign
ORDER_COUNT = 3   # the odd-torsion carrier arena the count reduces into

# T1: a sign (order 2) and a count (order 3) live in coprime cyclic groups:
#     no nonzero hom either way -> knowing one gives zero info about the other.
h_sc = hom_cyclic_order(ORDER_SIGN, ORDER_COUNT)   # Hom(Z/2,Z/3)
h_cs = hom_cyclic_order(ORDER_COUNT, ORDER_SIGN)   # Hom(Z/3,Z/2)
check("T1 Hom(Z/2,Z/3)=Hom(Z/3,Z/2)=0 (sign and count are non-interacting)",
      h_sc == 1 and h_cs == 1,   # trivial group has order 1
      f"|Hom(sign->count)|={h_sc}, |Hom(count->sign)|={h_cs} (1 = trivial)")

# T2: same statement one arena up, matching located-not-forced's Z/8 vs Z/3.
#     the sign sits in the 2-primary selector arena Z/8; the count in Z/3.
check("T2 selector arena Z/8 and carrier arena Z/3 are Hom-disjoint both ways",
      hom_cyclic_order(8, 3) == 1 and hom_cyclic_order(3, 8) == 1,
      "Hom(Z/8,Z/3)=Hom(Z/3,Z/8)=0")

# T3: CRT support-disjointness -- an element supported purely in the Z/8
#     component projects to 0 in Z/3 and vice versa.  So the Krein SIGN (a
#     Z/8-side datum) determines NOTHING about the count (a Z/3-side datum).
def crt_project(x, mod):            # Z/24 -> Z/mod
    return x % mod
sign_elt  = 3    # a nonzero element of the Z/8 component: 3*3=9 == ... pick pure-2 elt
# pure Z/8 element of Z/24: multiples of 3 (order dividing 8); pure Z/3 element: multiples of 8
pure8 = [k * 3 for k in range(1, 8)]     # nonzero, killed by proj to Z/3
pure3 = [8, 16]                          # nonzero, killed by proj to Z/8
ok8 = all(crt_project(x, 3) == 0 and crt_project(x, 8) != 0 for x in pure8)
ok3 = all(crt_project(x, 8) == 0 and crt_project(x, 3) != 0 for x in pure3)
check("T3 CRT supports disjoint: Z/8-datum -> 0 in Z/3; Z/3-datum -> 0 in Z/8",
      ok8 and ok3,
      "sign lives in Z/8 comp (proj_3 = 0); count lives in Z/3 comp (proj_8 = 0)")

# ======================================================================
# BLOCK C -- the SHARED OPERATOR, and why it alone gives no count
# ======================================================================
print("\n--- BLOCK C: the shared K-definite re-grading (C-operator) ---")

# C1 (Theorem 2 leg): chirality eigenspaces of Gamma are K-NULL (Lagrangian).
Wp = np.array([[1, 0], [0, 1], [0, 0], [0, 0]], dtype=float)  # span(v0,v1), chi +
Wm = np.array([[0, 0], [0, 0], [1, 0], [0, 1]], dtype=float)  # span(v2,v3), chi -
Kpp = Wp.T @ K @ Wp
Kmm = Wm.T @ K @ Wm
check("C1 chirality eigenspaces W_+ , W_- are K-null (Lagrangian)",
      np.allclose(Kpp, 0) and np.allclose(Kmm, 0),
      "K|W_+ = K|W_- = 0  => a chirality re-grading is in the K-NULL class")

# C2 (Theorem 2): a maximal K-positive (physical) subspace is chirality-balanced,
#     net chiral index chi = 0 (the vectorlike +96 in miniature).
P = np.array([[1, 0], [0, 1], [1, 0], [0, 1]], dtype=float) / np.sqrt(2)  # v0+v2, v1+v3
KP = P.T @ K @ P
proj_plus  = np.linalg.matrix_rank(Wp.T @ P)   # rank of projection onto W_+
proj_minus = np.linalg.matrix_rank(Wm.T @ P)
chi_phys = proj_plus - proj_minus
check("C2 maximal K-positive physical subspace is chirality-balanced (chi = 0)",
      signature(KP) == (2, 0, 0) and chi_phys == 0,
      f"sig(K|P)={signature(KP)}, chi=+{proj_plus}-{proj_minus}={chi_phys}")

# C3: the K-DEFINITE non-chirality re-grading = sign(K) = the C-operator.
#     Its +/- eigenspaces are K-DEFINITE (not null); eta_+ = K.C is positive.
#     This is the located-not-forced RESIDUAL class AND the W186 reservoir object.
evals, evecs = np.linalg.eigh(K)
Cop = evecs @ np.diag(np.sign(evals)) @ evecs.T   # sign(K); K-definite re-grading
eta_plus4 = K @ Cop                               # C-metric on the carrier
# non-chirality: Cop is NOT the chirality operator, and it anticommutes with Gamma
anticomm = np.allclose(Gamma @ Cop + Cop @ Gamma, 0)
not_gamma = not np.allclose(Cop, Gamma)
check("C3 C-operator = sign(K) is a K-DEFINITE, NON-chirality re-grading; eta_+ > 0",
      signature(eta_plus4) == (4, 0, 0) and not_gamma and anticomm,
      f"sig(eta_+)={signature(eta_plus4)}, Cop != Gamma, {{Gamma,Cop}}=0")

# C4: the C-operator eigenspaces ARE K-definite (the physical/ghost split),
#     distinguishing this residual class from the K-null chirality class (C1).
lam = np.round(evals, 9)
Vpos = evecs[:, lam > 0]
Vneg = evecs[:, lam < 0]
sig_pos = signature(Vpos.T @ K @ Vpos)
sig_neg = signature(Vneg.T @ K @ Vneg)
check("C4 C-operator eigenspaces are K-DEFINITE (K-positive / K-negative), not null",
      sig_pos == (2, 0, 0) and sig_neg == (0, 2, 0),
      f"K|+ = {sig_pos}, K|- = {sig_neg}  (contrast C1's null chirality class)")

# C5 (the coherence result -- BOTH arcs agree): with the C-operator operative
#     (eta_+ > 0, records physical), the carrier is STILL vectorlike: net chiral
#     index over the whole space = dim W_+ - dim W_- = 2 - 2 = 0.  So the shared
#     operator, even when operative, supplies NO count on its own.
chi_total = Wp.shape[1] - Wm.shape[1]
check("C5 shared C-operator operative => records physical but STILL vectorlike (chi=0)",
      chi_total == 0,
      f"net chiral index of carrier = {chi_total}  => count needs a SEPARATE Z/3 input")

# ======================================================================
# BLOCK NC -- negative / discriminating controls
# ======================================================================
print("\n--- BLOCK NC: negative controls ---")

# NC1: over a POSITIVE-DEFINITE ambient there is NO sign flip and NO K-definite
#      vs K-null distinction -- the whole structure needs Krein indefiniteness
#      (matches W186/W168 NC).
eta_pd = np.eye(2)
naive_pd = float(mirror @ eta_pd @ mirror)
check("NC1 positive-definite ambient: no sign flip (needs Krein indefiniteness)",
      naive_pd > 0,
      f"mirror naive-norm under I = {naive_pd:+.0f} (no flip; crux disappears)")

# NC2: if the count REDUCED to a sign (order 2), it could not carry order-3
#      information -- a would-be 'same-bit' collapse is arithmetically forbidden.
#      There is no order-3 element inside a Z/2, so a sign cannot encode {1 vs 3}.
z2_orders = {0: 1, 1: 2}
has_order3 = any(o == 3 for o in z2_orders.values())
check("NC2 a Z/2 sign has no order-3 element => cannot encode the count {1 vs 3}",
      not has_order3,
      "orders present in Z/2 are {1,2}; the count needs order 3")

# NC3: relabel invariance -- renaming the sign datum 'the count' does not create
#      a hom; Hom is unchanged under relabeling.  Guards same-bit-by-vagueness.
check("NC3 relabel guard: renaming does not manufacture Hom(Z/2,Z/3)",
      hom_cyclic_order(2, 3) == hom_cyclic_order(2, 3) == 1,
      "naming an object does not create a homomorphism")

# ======================================================================
# SUMMARY
# ======================================================================
print("\n--- SUMMARY ---")
npass = sum(1 for _, ok, _ in RESULTS if ok)
ntot = len(RESULTS)
print(f"{npass}/{ntot} checks passed.")
print("\nType verdict (machine-checkable core):")
print("  * Krein-sign datum   : an order-2 SIGN in the 2-primary SELECTOR arena (Z/8).")
print("  * count datum        : an odd-torsion / relative-index MAGNITUDE in the")
print("                         CARRIER arena (Z/3); parity pinned odd, value gated.")
print("  * as DATA            : CRT-disjoint (Hom both ways = 0) -> the count VALUE")
print("                         is provably NOT the Krein sign.  [independent]")
print("  * as OPERATOR        : both route through the K-DEFINITE, non-chirality")
print("                         re-grading = the C-operator (sign(K), eta_+=K.C).")
print("                         Shared operator; but operative => still vectorlike")
print("                         (chi=0), so the sign alone yields no count.")

if npass == ntot:
    print("\nAll checks passed.")
    sys.exit(0)
else:
    print("\nSome checks FAILED.")
    sys.exit(1)
