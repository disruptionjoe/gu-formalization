#!/usr/bin/env python3
r"""
R4 big-swing certificate 1 of 3 -- Spin(9,5) chiral-spinor Hom-vanishing.

STANDALONE math-ph claim (no GU input):

    dim Hom_{so(9,5)}( S^+ (x) S^+ , Lambda^0 )  =  0 ,

equivalently the 64-dim chiral (Weyl) spinor S^+ of so(9,5) is NOT self-dual:
its dual is the OPPOSITE chirality, S^+ ~= (S^-)^*.  Hence there is no
so(9,5)-invariant bilinear pairing of two same-chirality spinors into the
scalar (trivial) representation Lambda^0.

We prove it three independent ways and print exact certificates:

 (I)  EXPLICIT CLIFFORD / LINEAR ALGEBRA on the real signature (9,5).
      Build the 128-dim Dirac spinor of Cl(9,5), the chirality involution
      omega, and solve the full so-invariance linear system for bilinear
      forms on each chirality block.  Report the exact integer dimensions
      dim Hom(S^+(x)S^+, triv), dim Hom(S^+(x)S^-, triv).

 (II) INDEPENDENT re-derivation with a DIFFERENT gamma construction
      (recursive doubling, not Jordan-Wigner) and a DIFFERENT signature
      Cl(7,7); plus a Euclidean Cl(4,0) / Cl(8,0) self-dual CONTROL where the
      answer is known to be 1 (so the method can see a nonzero when there is
      one -- a genuine non-triviality control).

 (III) EXACT WEIGHT COMBINATORICS (integer, no floating point): the trivial
      rep in S^+(x)S^+ requires a weight w in S^+ with -w also in S^+.
      For so(2r) a chiral weight is an r-tuple of +-1/2 with an EVEN number of
      minus signs; negation sends minus-count m -> r - m.  For r = 7 (odd),
      m even => r - m odd, so -w is ALWAYS in the opposite chirality.
      Zero-weight-in-S^+(x)S^+ count = 0 exactly.  This is the leg formalized
      in Lean (R4_TwoArena.lean, weight_parity section).

All three agree: 0.  Exit 0 on success.
"""
import itertools
import numpy as np


# ----------------------------------------------------------------------------
# Gamma constructions
# ----------------------------------------------------------------------------
def gammas_jordan_wigner(p, q):
    """Jordan-Wigner style: n = p+q Hermitian/anti-Herm gammas, first p square +1,
    last q square -1.  Returns list of 2^(n//2) x 2^(n//2) complex matrices."""
    n = p + q
    assert n % 2 == 0
    r = n // 2
    I = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    herm = []  # 2r Hermitian gammas, each squares to +1
    for k in range(r):
        L, R = [s3] * k, [I] * (r - 1 - k)
        for mid in (s1, s2):
            o = np.array([[1 + 0j]])
            for m in L + [mid] + R:
                o = np.kron(o, m)
            herm.append(o)
    # Now assign signature: first p get +1 (keep Hermitian), last q multiply by i (square -1)
    G = []
    for a in range(n):
        if a < p:
            G.append(herm[a])
        else:
            G.append(1j * herm[a])
    return G


def gammas_recursive(p, q):
    """Independent construction by recursive doubling (Cl(a,b) from Cl(a-1,b-1)
    tensoring Pauli), different basis from Jordan-Wigner.  Build Euclidean +1
    generators then apply signature by i-scaling, matching gammas_jordan_wigner's
    convention (first p square +1)."""
    n = p + q
    assert n % 2 == 0
    r = n // 2
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)

    def build(rr):
        # returns 2rr Hermitian gammas each squaring to +1, dim 2^rr
        if rr == 1:
            return [s1, s2]
        sub = build(rr - 1)
        d = sub[0].shape[0]
        Id = np.eye(d, dtype=complex)
        out = [np.kron(s1, g) for g in sub]
        out.append(np.kron(s2, Id))
        out.append(np.kron(s3, Id))
        return out

    herm = build(r)
    G = []
    for a in range(n):
        G.append(herm[a] if a < p else 1j * herm[a])
    return G


# ----------------------------------------------------------------------------
# Core: dimensions of invariant bilinear forms per chirality block
# ----------------------------------------------------------------------------
def chirality(G):
    """omega = G_1 ... G_n, normalized so omega^2 = I (real +-1 eigenvalues)."""
    om = np.eye(G[0].shape[0], dtype=complex)
    for g in G:
        om = om @ g
    sq = (om @ om)
    # scale so omega^2 = I
    lam2 = sq[0, 0]
    om = om / np.sqrt(complex(lam2))
    return om


def projectors(om, tol=1e-9):
    d = om.shape[0]
    Pp = 0.5 * (np.eye(d, dtype=complex) + om)
    Pm = 0.5 * (np.eye(d, dtype=complex) - om)
    return Pp, Pm


def block_basis(P, tol=1e-9):
    """Orthonormal columns spanning range(P) (a chirality subspace)."""
    w, V = np.linalg.eigh(0.5 * (P + P.conj().T))
    return V[:, w > 0.5]


def so_generators(G, spanning=True):
    """so(p,q) spinor generators sigma_ab = 1/4 [G_a, G_b].  With spanning=True
    return only the adjacent set sigma_{a,a+1} (a=0..n-2), which Lie-generates
    all of so(n): invariance under them is equivalent to full so-invariance, and
    it is far cheaper.  spanning=False returns all a<b pairs (redundant check)."""
    n = len(G)
    gens = []
    if spanning:
        for a in range(n - 1):
            gens.append(0.25 * (G[a] @ G[a + 1] - G[a + 1] @ G[a]))
    else:
        for a in range(n):
            for b in range(a + 1, n):
                gens.append(0.25 * (G[a] @ G[b] - G[b] @ G[a]))
    return gens


def invariant_form_dim(gens, Ua, Ub, tol=1e-6):
    """dim of the space of bilinear forms B: (col Ua) x (col Ub) -> C that are
    so-invariant.  A bilinear form on the ambient spinor is x^T Bfull y with
    Bfull sigma + sigma^T Bfull = 0 for every so generator sigma.  Restricting
    to the chirality blocks and writing Bfull = conj(Ua) M Ub^T pairs col(Ua)
    with col(Ub); the block equation for each generator is
        A_g M + M Bk_g = 0,   A_g = Ua^T sigma^T conj(Ua),  Bk_g = Ub^dagger sigma Ub.
    As a linear map on vec(M):  L_g = I (x) A_g + Bk_g^T (x) I.
    We accumulate the Hermitian NORMAL matrix  T = sum_g L_g^dagger L_g
    (na*nb square, built one generator at a time -- no giant stack) whose null
    space is exactly the common solution space.  dim = # near-zero eigenvalues."""
    na = Ua.shape[1]
    nb = Ub.shape[1]
    D = na * nb
    T = np.zeros((D, D), dtype=complex)
    Ina, Inb = np.eye(na), np.eye(nb)
    for s in gens:
        A = Ua.T @ (s.T) @ np.conj(Ua)       # na x na
        Bk = Ub.conj().T @ s @ Ub            # nb x nb
        L = np.kron(Inb, A) + np.kron(Bk.T, Ina)   # D x D
        T += L.conj().T @ L
    T = 0.5 * (T + T.conj().T)
    ev = np.linalg.eigvalsh(T)
    scale = max(1.0, ev[-1])
    dim = int(np.sum(ev < tol * scale))
    gap_lo = ev[dim - 1] if dim > 0 else float("nan")
    gap_hi = ev[dim] if dim < D else float("nan")
    return dim, gap_lo, gap_hi


def report_signature(p, q, gam_fn, label):
    G = gam_fn(p, q)
    d = G[0].shape[0]
    # verify Clifford relations
    maxrel = 0.0
    eta = [1.0] * p + [-1.0] * q
    for a in range(len(G)):
        for b in range(len(G)):
            lhs = G[a] @ G[b] + G[b] @ G[a]
            rhs = (2 * eta[a] * (1.0 if a == b else 0.0)) * np.eye(d)
            maxrel = max(maxrel, np.linalg.norm(lhs - rhs))
    om = chirality(G)
    om2 = np.linalg.norm(om @ om - np.eye(d))
    Pp, Pm = projectors(om)
    Up, Um = block_basis(Pp), block_basis(Pm)
    gens = so_generators(G)
    dpp, gap_pp, _ = invariant_form_dim(gens, Up, Up)
    dpm, _, _ = invariant_form_dim(gens, Up, Um)
    print(f"  [{label}] Cl({p},{q}) dim spinor={d}, Weyl={Up.shape[1]}/{Um.shape[1]}; "
          f"Clifford residual={maxrel:.1e}, ||omega^2-I||={om2:.1e}")
    print(f"      dim Hom(S^+ (x) S^+, triv) = {dpp}   "
          f"dim Hom(S^+ (x) S^-, triv) = {dpm}")
    return dpp, dpm


# ----------------------------------------------------------------------------
# (III) exact weight combinatorics
# ----------------------------------------------------------------------------
def weight_zero_count_same_chirality(r):
    """Exact integer count of chiral weights w of so(2r) (r-tuples of +-1 with an
    EVEN number of -1) such that -w is ALSO an even-chirality weight.
    (Using +-1 in place of +-1/2 is an overall scale; the sign pattern is what
    matters.)  Returns (count_same_chirality_zero_pairs, total_even_weights)."""
    same = 0
    total = 0
    for signs in itertools.product((+1, -1), repeat=r):
        minus = sum(1 for s in signs if s == -1)
        if minus % 2 == 0:               # w in S^+
            total += 1
            neg = tuple(-s for s in signs)
            neg_minus = sum(1 for s in neg if s == -1)
            if neg_minus % 2 == 0:       # -w also in S^+
                same += 1
    return same, total


# ============================================================================
if __name__ == "__main__":
    print("=" * 78)
    print("(I) EXPLICIT Cl(9,5) -- primary computation (Jordan-Wigner gammas)")
    print("=" * 78)
    dpp_95, dpm_95 = report_signature(9, 5, gammas_jordan_wigner, "primary")
    assert dpp_95 == 0, dpp_95
    assert dpm_95 == 1, dpm_95

    print()
    print("=" * 78)
    print("(II) INDEPENDENT re-derivations and controls")
    print("=" * 78)
    print(" -- same (9,5), DIFFERENT gamma construction (recursive doubling):")
    a, b = report_signature(9, 5, gammas_recursive, "recursive")
    assert a == 0 and b == 1, (a, b)

    print(" -- DIFFERENT signature Cl(7,7) (n=14 too; chirality-flip expected):")
    a, b = report_signature(7, 7, gammas_jordan_wigner, "Cl(7,7)")
    assert a == 0 and b == 1, (a, b)

    print(" -- CONTROL Cl(4,0), n=4 (r=2 even): S^+ IS self-dual, expect Hom(S^+xS^+)=1:")
    a, b = report_signature(4, 0, gammas_jordan_wigner, "Cl(4,0) control")
    assert a == 1, ("control failed to see nonzero", a)

    print(" -- CONTROL Cl(8,0), n=8 (r=4 even): S^+ self-dual, expect Hom(S^+xS^+)=1:")
    a, b = report_signature(8, 0, gammas_jordan_wigner, "Cl(8,0) control")
    assert a == 1, ("control failed", a)

    print()
    print("=" * 78)
    print("(III) EXACT WEIGHT COMBINATORICS (integer arithmetic)")
    print("=" * 78)
    for r in (7, 5, 3, 2, 4, 6):
        same, total = weight_zero_count_same_chirality(r)
        parity = "ODD r -> flips chirality" if r % 2 else "EVEN r -> self-dual"
        print(f"  so({2*r}): chiral weights={total:3d}, "
              f"weight-zero pairs inside S^+(x)S^+ = {same:3d}   [{parity}]")
        if r % 2 == 1:
            assert same == 0, (r, same)
        else:
            assert same == total, (r, same, total)   # every w has -w in S^+

    same7, total7 = weight_zero_count_same_chirality(7)
    print()
    print(f"  so(14) [Spin(9,5), Spin(7,7)]: zero-weight count in S^+(x)S^+ = {same7} "
          f"of {total7} chiral weights.")
    assert same7 == 0

    print()
    print("#" * 78)
    print("# VERDICT: dim Hom_{so(9,5)}(S^+ (x) S^+, Lambda^0) = 0")
    print("#   -- explicit Cl(9,5): 0 ; recursive-basis Cl(9,5): 0 ; Cl(7,7): 0 ;")
    print("#      controls Cl(4,0)/Cl(8,0) correctly return 1 ; weight count: 0.")
    print("#   S^+ is NOT self-dual for so(9,5); its dual is S^- (dim Hom(S^+ (x) S^-)=1).")
    print("#   n=14 => r=7 ODD is the exact reason (charge conjugation flips chirality).")
    print("#" * 78)
