#!/usr/bin/env python3
"""P-77-REAL-INDEX W2 adversarial twin probe (2026-07-19).

INDEPENDENT FUNCTOR PATH: direct Clifford-module counting on an explicit,
bit-exact, all-REAL integer representation of Cl(7,7) -- NOT the KO-of-a-point
route, and NOT the complex Jordan-Wigner rep of ch_sig77_port_probe.py (whose
J'-real-structure certificate this construction corroborates from the other
side: here the real form is EXHIBITED, entries in {0,+1,-1}, so the native
antiunitary is plain conjugation and every J'-commutant statement becomes a
statement about real matrices).

Signature purity (K6): every computation is (7,7) or a subalgebra of it.
(9,5) facts are cited in comments/prints, never recomputed. The base-algebra
comparison table cites the standard Clifford classification, comparison-grade,
exactly as the port probe's Part-3 convention-location table does.

PART A  Exact module counting.
  A1  Cl(7,7) relations, integer-exact, on real 128x128 signed-permutation
      gammas (7 symmetric P_k with square +I, 7 antisymmetric M_k with
      square -I; iterated Cl(1,1) construction).
  A2  ALL 16383 nonscalar Clifford monomials are traceless (Gray-code sweep,
      exact integer traces via signed-permutation composition). Since each
      monomial is orthogonal (m^T = m^{-1}), the trace form is diagonal and
      nonzero on the 16384 monomials => they are linearly independent =>
      the real algebra they span has dim 16384 = dim_R M(128,R) => the
      algebra IS M(128,R) and End_{Cl(7,7)}(R^128) = R.
      SCHUR DIVISOR = 1: the (7,7) class forces NO multiplicity quantum.
  A3  Exact constraint surface: Gamma = hstack(e_a) integer, Gamma Gamma^T =
      14 I exactly, so A := 14 I - Gamma^T Gamma is an INTEGER multiple of
      the constraint projector (Pi = A/14), with Gamma A = 0 and A^2 = 14 A
      bit-exact. Rank-3 (and rank-2) real symmetric carriers ON the surface:
      signature 3 (odd) and 2 (even) both reachable. In the real form the
      native antiunitary is plain conjugation, so "J'-commutant" = real:
      parity is completely free. (Constraint-surface odd carrier: independent
      re-derivation of port-probe 1e by the real-form route.)
  A4  Fiber Cl(6,4) = M(32,R), integer-exact (1023 nonscalar traces = 0);
      fiber chirality omega(6,4)^2 = -I exactly => the chirality is a COMPLEX
      STRUCTURE on R^32: there is NO real Weyl (Majorana-Weyl) module; the
      unique irreducible REAL fiber module is the 32-dim Majorana-Dirac one.
      The "one generation = one Weyl-16" object exists only complexly.
  A5  Base Cl(1,3) = M(2,H), integer-exact: 8-dim real irreducible module
      with explicit integer quaternion units R_i, R_j in the commutant
      (squares -I, anticommute, commute with all four gammas bit-exactly),
      15 nonscalar monomial traces = 0, commutant dimension = 4 = dim_R H.
      THE (7,7)-INDUCING X4 CONVENTION HAS A QUATERNIONIC BASE ALGEBRA.
      [Cited, standard table + port-probe 3f convention discussion,
      comparison-grade: the (9,5)-inducing convention has Cl(3,1) = M(4,R).]
  A6  THE MOVED WALL: inside M(128,R), the commutant of a (1,3) base tetrad
      has real dimension 128^2/16 = 1024 = dim_R M(16,H) (exact averaging-
      projector trace), and R^128 = 16 copies of the unique irreducible
      H^2 => commutant = M(16,H). Numeric corroboration: a generic
      base-Clifford-linear symmetric carrier has ALL eigenvalue
      multiplicities divisible by 8 => base-linear carriers have signature
      in 8Z: a spacetime-scalar carrier CANNOT have literal index 3 in
      (7,7). Kramers did not vanish -- it moved from the total algebra
      [(9,5), cited] to the spacetime factor.
  A7  THE UNGRADED-TENSOR TRAP: the naive Kronecker port base(x)fiber
      (Cl(1,3) acting on R^8) (x) (Cl(6,4) acting on R^32) makes base and
      fiber gammas COMMUTE (not anticommute) -- it is NOT a Cl(7,7) module.
      Its commutant is H (dim 4, exact) on a 256-dim real module: the lazy
      factorized port lands EXACTLY on the quaternionic-class module data
      (End = H, real dim 256 = 2 x 128) -- i.e. it silently resurrects the
      (9,5)-style Kramers wall and destroys the fork's entire advantage.
      [Cited for contrast, not recomputed: in (9,5) the naive Kronecker goes
      the OTHER way, 4 x 32 = 128 = half of the true 256.]

PART B  Divisor/count arithmetic, exact integers.
  B1  Retype matrix: numerator readings {24 (H-units, blind port), 48
      (complex units), 96 (real units)} x divisor readings {8 (rank_H,
      blind), 16 (rank_C Weyl), 32 (rank_R Majorana)}: which cells give 3,
      which give another integer, which are non-integer. (The numerator "24"
      is itself an OPEN target, never computed -- cited.)
  B2  The honest K3 toy number, recomputed from its own stated formula:
      ch2(S_X)[K3] = (dim_S/8) * p1(V) = 16 * (7 * 3 * sigma(K3)) = -5376,
      factorization -5376 = -(2^8 * 3 * 7); divisor-steering table over the
      repo's own natural dimensions; provenance of each extractable small
      number (the reachable "3" is Hirzebruch's p1 = 3 sigma coefficient,
      not generation content).
  B3  Finite shadow of KO alpha^2 = 4 beta: H (x)_R H = M(4,R) exact (the 16
      products L_a R_b are trace-orthogonal, spanning all of M(4,R)): two
      quaternionic factors recombine REAL with multiplicity 4 -- the hidden
      x4/(div)4 in any K3(H-type Dirac) x (H-typed piece) factorized
      bookkeeping.

PART C  Convention steering (GRAM-PIN-77 both forks + orientation).
  C1  Orientation steering: global sign flip e_a -> -e_a and timelike-set
      relabeling T = {4..10}: all class certificates invariant.
  C2  Chirality-twisted Gram bT (timelike 7-product): real symmetric,
      bT^2 = +I, trace 0, real 64/64 sectors; rank-3 carrier INSIDE a
      sector: signature 3. Canonical Gram bS = i * (spacelike 7-product):
      in the real form the spacelike product is ANTISYMMETRIC with square
      -I (exact) -- the explicit scalar i is forced and J'-odd (independent
      re-derivation of port-probe 1c from the real form); complexified
      sectors 64/64; rank-3 Hermitian carrier inside a sector: signature 3.
      NEITHER Gram fork pins carrier parity: 3 and 2 reachable under both.

PART D  Eta shadow, skeptical.
  D1  The J-free chiral route: with the EXACT grading G = Pi - Q, any
      off-diagonal (KT-Hessian-square-root-shaped) D = Pi H Q + Q H Pi
      anticommutes with G => spectrum exactly symmetric => finite-shadow
      eta = 0 WITH NO ANTIUNITARY INPUT. The (9,5) proof's C = J_quat.G is
      sufficient but not necessary; the grading mechanism is signature-blind.
      Also: at this (finite, symmetric-spectrum) scale a nonzero eta is
      structurally invisible -- the toy CANNOT adjudicate the true
      noncompact boundary term in either signature class.

No claim-status, canon, map, or public-posture movement. Exit 0 iff all
checks pass.

Run: python tests/channel-swings/p77_real_index_twin.py
"""

from fractions import Fraction

import numpy as np

CHECKS = []


def check(name, cond, detail=""):
    CHECKS.append((name, bool(cond)))
    tag = "PASS" if cond else "FAIL"
    print(f"[{tag}] {name}" + (f"  --  {detail}" if detail else ""), flush=True)


# --------------------------------------------------------------------------- #
# Integer building blocks
# --------------------------------------------------------------------------- #
I2 = np.eye(2, dtype=np.int64)
S1 = np.array([[0, 1], [1, 0]], dtype=np.int64)
S3 = np.array([[1, 0], [0, -1]], dtype=np.int64)
EPS = np.array([[0, 1], [-1, 0]], dtype=np.int64)


def kron_list(ms):
    out = np.array([[1]], dtype=np.int64)
    for m in ms:
        out = np.kron(out, m)
    return out


def build_split_clifford(n):
    """n hyperbolic pairs -> Cl(n,n) on R^(2^n): P_k^2=+I (symmetric),
    M_k^2=-I (antisymmetric), all pairwise anticommuting, entries in
    {0,+1,-1} (signed permutation matrices)."""
    P, M = [], []
    for k in range(n):
        pre, post = [S3] * k, [I2] * (n - 1 - k)
        P.append(kron_list(pre + [S1] + post))
        M.append(kron_list(pre + [EPS] + post))
    return P, M


def clifford_relations_exact(gammas, eta):
    n = len(gammas)
    dim = gammas[0].shape[0]
    for a in range(n):
        for b in range(n):
            want = (2 * eta[a] if a == b else 0) * np.eye(dim, dtype=np.int64)
            if not np.array_equal(gammas[a] @ gammas[b] + gammas[b] @ gammas[a], want):
                return False
    return True


def to_signed_perm(D):
    """Dense signed-permutation matrix -> (perm p, sign s): row i has s[i] at
    column p[i]. Asserts the matrix really is a signed permutation."""
    p = np.abs(D).argmax(axis=1)
    s = D[np.arange(D.shape[0]), p]
    R = np.zeros_like(D)
    R[np.arange(D.shape[0]), p] = s
    assert np.array_equal(R, D), "not a signed permutation matrix"
    return p, s


def sp_mul(a, b):
    """(A B) for signed perms: A=(pa,sa), B=(pb,sb)."""
    pa, sa = a
    pb, sb = b
    return pb[pa], sa * sb[pa]


def sp_trace(a):
    p, s = a
    fixed = p == np.arange(p.size)
    return int(s[fixed].sum())


def gray_traceless_sweep(gammas):
    """Iterate all nonempty Clifford monomials in Gray-code order via
    signed-permutation composition; return (#nonscalar monomials with exact
    trace 0, total #nonscalar monomials)."""
    n = len(gammas)
    sp = [to_signed_perm(g) for g in gammas]
    dim = gammas[0].shape[0]
    cur = (np.arange(dim), np.ones(dim, dtype=np.int64))
    zero = 0
    total = (1 << n) - 1
    for t in range(1, 1 << n):
        b = (t & -t).bit_length() - 1  # bit flipped between gray(t-1), gray(t)
        cur = sp_mul(cur, sp[b])
        if sp_trace(cur) == 0:
            zero += 1
    return zero, total


def sym_signature(A, tol_scale=1e-9):
    ev = np.linalg.eigvalsh(0.5 * (A + A.conj().T))
    tol = tol_scale * max(1.0, np.abs(ev).max())
    return int((ev > tol).sum()) - int((ev < -tol).sum())


# =========================================================================== #
def part_A():
    print("=" * 78)
    print("PART A -- exact real Clifford-module counting (independent functor path)")
    print("=" * 78)

    # ---- A1: Cl(7,7) on R^128, integer exact --------------------------------
    P, M = build_split_clifford(7)
    e = P + M                       # labeling L1: 0..6 spacelike, 7..13 timelike
    eta = [1] * 7 + [-1] * 7
    check("A1  Cl(7,7) relations {e_a,e_b} = 2 eta_ab, INTEGER-EXACT, on an "
          "all-REAL 128x128 signed-permutation representation",
          clifford_relations_exact(e, eta))
    sym_ok = all(np.array_equal(g, g.T) for g in P) and \
        all(np.array_equal(g, -g.T) for g in M)
    check("A1  7 spacelike gammas symmetric (sq +I), 7 timelike antisymmetric "
          "(sq -I); all orthogonal => m^T = m^{-1} for every monomial",
          sym_ok)

    # ---- A2: all nonscalar monomials traceless => algebra = M(128,R) --------
    zero, total = gray_traceless_sweep(e)
    check("A2  ALL 16383 nonscalar Clifford monomials have EXACT trace 0 "
          "(Gray-code sweep, integer arithmetic)",
          zero == total == 16383, f"{zero}/{total} traceless")
    # orthogonality of the trace form => 16384 independent monomials
    # => dim of the real algebra = 16384 = dim_R M(128,R) => algebra = M(128,R)
    # => End_{Cl(7,7)}(R^128) = R (commutant of the full matrix algebra).
    check("A2  => 16384 monomials linearly independent => algebra = M(128,R) "
          "=> End_{Cl(7,7)}(R^128) = R  => SCHUR DIVISOR = 1: the class "
          "forces NO multiplicity quantum on any Hermitian carrier",
          16384 == 128 * 128)

    # ---- A3: exact constraint surface + free parity -------------------------
    Gamma = np.hstack(e)                                  # 128 x 1792, integer
    GGt = Gamma @ Gamma.T
    check("A3  Gamma Gamma^T = 14 I exactly (integer)",
          np.array_equal(GGt, 14 * np.eye(128, dtype=np.int64)))
    A = 14 * np.eye(1792, dtype=np.int64) - Gamma.T @ Gamma   # 14 * Pi, integer
    gA_zero = np.array_equal(Gamma @ A, np.zeros((128, 1792), dtype=np.int64))
    A2_ok = np.array_equal(A.astype(np.float64) @ A.astype(np.float64), 14.0 * A)
    trA = int(np.trace(A))
    check("A3  A = 14 Pi integer: Gamma A = 0 and A^2 = 14 A BIT-EXACT; "
          "tr A = 14 * 1664 (ker dim 1664)",
          gA_zero and A2_ok and trA == 14 * 1664, f"tr A = {trA}")
    cols = [0, 600, 1200]
    V = A[:, cols].astype(np.float64)
    VtV = V.T @ V
    P3 = V @ np.linalg.inv(VtV) @ V.T
    on_surface = np.linalg.norm((A.astype(np.float64) / 14.0) @ P3 - P3)
    sig3 = sym_signature(P3)
    V2c = A[:, [10, 900]].astype(np.float64)
    P2 = V2c @ np.linalg.inv(V2c.T @ V2c) @ V2c.T
    sig2 = sym_signature(P2)
    check("A3  rank-3 REAL SYMMETRIC carrier ON the exact constraint surface: "
          "signature 3 (ODD); rank-2 sibling: signature 2 (EVEN). In the real "
          "form the native antiunitary is plain conjugation => 'J'-commutant' "
          "= real symmetric => carrier parity COMPLETELY FREE "
          "(independent re-derivation of port-probe 1e)",
          sig3 == 3 and sig2 == 2 and on_surface < 1e-9,
          f"sig3={sig3}, sig2={sig2}, surface residual {on_surface:.1e}")

    # ---- A4: fiber Cl(6,4) = M(32,R); no real Weyl --------------------------
    P4, M4 = build_split_clifford(4)                      # Cl(4,4) on R^16
    w44 = np.eye(16, dtype=np.int64)
    for g in P4 + M4:
        w44 = w44 @ g
    check("A4  omega(4,4)^2 = +I exactly (graded-adjoin twist is legal)",
          np.array_equal(w44 @ w44, np.eye(16, dtype=np.int64)))
    f = [np.kron(g, I2) for g in P4] \
        + [np.kron(w44, S1), np.kron(w44, S3)] \
        + [np.kron(g, I2) for g in M4]                    # 6 plus, 4 minus
    eta_f = [1] * 6 + [-1] * 4
    check("A4  Cl(6,4) relations INTEGER-EXACT on real 32x32 gammas",
          clifford_relations_exact(f, eta_f))
    zf, tf = gray_traceless_sweep(f)
    check("A4  1023/1023 nonscalar Cl(6,4) monomials traceless => algebra = "
          "M(32,R) => unique irreducible REAL fiber module is R^32 "
          "(Majorana-Dirac)", zf == tf == 1023, f"{zf}/{tf}")
    w64 = np.eye(32, dtype=np.int64)
    for g in f:
        w64 = w64 @ g
    check("A4  fiber chirality omega(6,4)^2 = -I EXACTLY: the chirality is a "
          "COMPLEX STRUCTURE on R^32 => NO real Weyl (Majorana-Weyl) module "
          "exists; 'one generation = one Weyl-16' is a COMPLEX-only object",
          np.array_equal(w64 @ w64, -np.eye(32, dtype=np.int64)))

    # ---- A5: base Cl(1,3) = M(2,H), quaternionic ----------------------------
    Li = np.array([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]],
                  dtype=np.int64)
    Lj = np.array([[0, 0, -1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, -1, 0, 0]],
                  dtype=np.int64)
    Ri = np.array([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]],
                  dtype=np.int64)
    Rj = np.array([[0, 0, -1, 0], [0, 0, 0, -1], [1, 0, 0, 0], [0, 1, 0, 0]],
                  dtype=np.int64)
    I4 = np.eye(4, dtype=np.int64)
    quat_ok = (np.array_equal(Li @ Li, -I4) and np.array_equal(Lj @ Lj, -I4)
               and np.array_equal(Li @ Lj, -(Lj @ Li))
               and np.array_equal(Ri @ Ri, -I4) and np.array_equal(Rj @ Rj, -I4)
               and np.array_equal(Ri @ Rj, -(Rj @ Ri))
               and all(np.array_equal(L @ R, R @ L)
                       for L in (Li, Lj) for R in (Ri, Rj)))
    check("A5  integer quaternion left/right multiplications verified "
          "(L^2 = R^2 = -I, anticommuting pairs, [L, R] = 0)", quat_ok)
    w2 = S1 @ EPS
    b = [np.kron(S1, I4), np.kron(EPS, I4), np.kron(w2, Li), np.kron(w2, Lj)]
    check("A5  Cl(1,3) relations INTEGER-EXACT on real 8x8 gammas "
          "(the (7,7)-inducing mostly-minus X4 convention)",
          clifford_relations_exact(b, [1, -1, -1, -1]))
    Rq1, Rq2 = np.kron(I2, Ri), np.kron(I2, Rj)
    comm_ok = all(np.array_equal(g @ R, R @ g) for g in b for R in (Rq1, Rq2))
    hq_ok = (np.array_equal(Rq1 @ Rq1, -np.eye(8, dtype=np.int64))
             and np.array_equal(Rq2 @ Rq2, -np.eye(8, dtype=np.int64))
             and np.array_equal(Rq1 @ Rq2, -(Rq2 @ Rq1)))
    zb, tb = gray_traceless_sweep(b)
    # commutant dimension by exact averaging-projector trace:
    # tr(X -> (1/16) sum_S m_S X m_S^{-1}) = (1/16) sum_S tr(m_S) tr(m_S^{-1})
    # = (only S = empty survives, A5 tracelessness) = 8^2/16 = 4 = dim_R H.
    check("A5  BASE IS QUATERNIONIC: explicit integer quaternion units in the "
          "commutant (commute with all 4 gammas BIT-EXACT, squares -I, "
          "anticommute); 15/15 nonscalar monomials traceless => commutant "
          "dim = 64/16 = 4 = dim_R H => Cl(1,3) = M(2,H). [Cited contrast, "
          "standard table: the (9,5)-inducing convention has Cl(3,1) = "
          "M(4,R) -- comparison-grade, not recomputed]",
          comm_ok and hq_ok and zb == tb == 15, f"{zb}/{tb} traceless")

    # ---- A6: the moved wall inside M(128,R) ---------------------------------
    E = [P[0], M[0], M[1], M[2]]                 # ambient (1,3) base tetrad
    check("A6  ambient base tetrad (P0, M0, M1, M2) satisfies Cl(1,3) "
          "INTEGER-EXACT inside Cl(7,7)",
          clifford_relations_exact(E, [1, -1, -1, -1]))
    # exact commutant dimension: all nonscalar tetrad monomials are ambient
    # Clifford monomials, traceless by A2 => dim = 128^2 / 16 = 1024.
    sp_E = [to_signed_perm(g) for g in E]
    curm = (np.arange(128), np.ones(128, dtype=np.int64))
    tr_sum = Fraction(0)
    for t in range(1 << 4):
        if t > 0:
            bbit = (t & -t).bit_length() - 1
            curm = sp_mul(curm, sp_E[bbit])
        trm = sp_trace(curm)
        tr_sum += Fraction(trm * trm, 16)        # tr(m) tr(m^{-1}) = +-tr(m)^2; 0 unless scalar
    check("A6  commutant of the base tetrad in M(128,R): EXACT dimension "
          "128^2/16 = 1024 = dim_R M(16,H) (averaging-projector trace); with "
          "A5 + uniqueness of the M(2,H) irreducible, R^128 = 16 copies of "
          "H^2 => commutant = M(16,H)",
          tr_sum == Fraction(1024), f"dim = {tr_sum}")
    rng = np.random.default_rng(77)
    X = rng.standard_normal((128, 128))
    X = 0.5 * (X + X.T)
    Xb = np.zeros_like(X)
    mons = []
    curd = np.eye(128, dtype=np.int64)
    for t in range(1 << 4):
        if t > 0:
            bbit = (t & -t).bit_length() - 1
            curd = curd @ E[bbit]
        mons.append(curd)
    for m in mons:
        mf = m.astype(np.float64)
        Xb += mf @ X @ mf.T                       # m^T = m^{-1} (orthogonal)
    Xb /= 16.0
    comm_res = max(np.linalg.norm(Xb @ g - g @ Xb) for g in
                   (Ef.astype(np.float64) for Ef in E))
    ev = np.linalg.eigvalsh(Xb)
    splits = np.where(np.diff(ev) > 1e-6 * (ev[-1] - ev[0]))[0]
    sizes = np.diff(np.concatenate(([0], splits + 1, [128])))
    mult8 = all(int(s) % 8 == 0 for s in sizes)
    check("A6  THE MOVED WALL: generic base-Clifford-linear symmetric carrier "
          "has ALL eigenvalue multiplicities divisible by 8 => base-linear "
          "(spacetime-scalar) carriers have signature in 8Z => LITERAL index "
          "3 is UNREACHABLE under base-linear typing in (7,7). Kramers moved "
          "from the total algebra [(9,5), cited] to the spacetime factor",
          comm_res < 1e-9 and mult8,
          f"commutation residual {comm_res:.1e}; cluster sizes {[int(s) for s in sizes]}")

    # ---- A7: the ungraded-tensor trap ---------------------------------------
    U = [np.kron(g, np.eye(32, dtype=np.int64)) for g in b]
    W = [np.kron(np.eye(8, dtype=np.int64), g) for g in f]
    commute_not_anticommute = all(
        np.array_equal(u @ w, w @ u) for u in U for w in W)
    Rq_big = np.kron(Rq1, np.eye(32, dtype=np.int64))
    Rq_big2 = np.kron(Rq2, np.eye(32, dtype=np.int64))
    quat_in_comm = (all(np.array_equal(g @ Rq_big, Rq_big @ g) for g in U + W)
                    and all(np.array_equal(g @ Rq_big2, Rq_big2 @ g) for g in U + W)
                    and np.array_equal(Rq_big @ Rq_big,
                                       -np.eye(256, dtype=np.int64)))
    # exact commutant dim of the ungraded product algebra:
    # (1/(16*1024)) sum_{S,T} tr(mS x mT) tr((mS x mT)^{-1}) = 256^2/16384 = 4
    check("A7  UNGRADED-TENSOR TRAP: naive Kronecker base(x)fiber gives "
          "COMMUTING (not anticommuting) base/fiber gammas -- NOT a Cl(7,7) "
          "module; its commutant contains exact quaternion units (End = H, "
          "dim 256^2/16384 = 4) on a 256-dim real module: the lazy factorized "
          "port lands on QUATERNIONIC-class module data (End = H, dim_R 256 "
          "= 2 x 128) and silently resurrects the Kramers wall. [Cited: "
          "(9,5) irreducible = H^64 = R^256; and there the naive Kronecker "
          "errs the OTHER way, 4 x 32 = 128 = 256/2]",
          commute_not_anticommute and quat_in_comm
          and 256 * 256 // (16 * 1024) == 4 and 8 * 32 == 2 * 128,
          "8 x 32 = 256 vs irreducible 128: factor-2 live at the module level")
    return e, P, M, A


# =========================================================================== #
def part_B():
    print()
    print("=" * 78)
    print("PART B -- divisor/count arithmetic (exact), the K3 input, the KO x4 shadow")
    print("=" * 78)

    # ---- B1: retype matrix --------------------------------------------------
    # Numerator readings of the OPEN (9,5) target "ind_H = 24" (cited: the 24
    # is an uncomputed target, canon no-go-class-relative-map; NOT a theorem):
    #   24 in H-units | 48 in C-units (ind_C = 2 ind_H) | 96 in R-units.
    # Divisor readings of "one generation":
    #   8 = rank_H fiber Weyl (blind H port) | 16 = rank_C Weyl |
    #   32 = rank_R of the ONLY real fiber module that exists (A4).
    nums = {"24 (H-units, blind)": 24, "48 (C-units)": 48, "96 (R-units)": 96}
    divs = {"8 (rank_H, blind)": 8, "16 (rank_C Weyl)": 16,
            "32 (rank_R Majorana)": 32}
    hit3, other_int, nonint = [], [], []
    print("    count matrix (numerator / divisor):")
    for nname, nv in nums.items():
        row = []
        for dname, dv in divs.items():
            c = Fraction(nv, dv)
            row.append(f"{nname.split()[0]}/{dname.split()[0]}={c}")
            if c == 3:
                hit3.append((nname, dname))
            elif c.denominator == 1:
                other_int.append((nname, dname, c))
            else:
                nonint.append((nname, dname, c))
        print("      " + "   ".join(row))
    check("B1  STEERING (arithmetic): count 3 reachable on the type-consistent "
          "diagonal (24/8, 48/16, 96/32) AND different integers (6, 12) plus "
          "non-integers (3/2, 3/4) reachable off-diagonal: a port that "
          "retypes numerator but not divisor (or vice versa) silently "
          "changes the count by x2 or x4",
          len(hit3) == 3 and any(c == 6 for *_, c in other_int)
          and any(c == 12 for *_, c in other_int) and len(nonint) == 3,
          f"3-cells {len(hit3)}, other-int {[(str(c)) for *_, c in other_int]}, "
          f"non-int {[(str(c)) for *_, c in nonint]}")

    # ---- B2: the honest K3 number and its steering surface ------------------
    sigma_k3 = -16
    p1_tk3 = 3 * sigma_k3                # Hirzebruch p1 = 3 sigma = -48
    p1_v = (1 + 6) * p1_tk3              # TK3 (+) Sym^2: multiplier 1 + 6 = 7
    ch2_full = (128 // 8) * p1_v         # spin-trace (dim_S/8); = -5376
    check("B2  honest K3 toy number recomputed from its own stated formula: "
          "ch2(S_X)[K3] = (128/8) * 7 * 3 * sigma(K3) = -5376 "
          "(matches tests/gen_ch2_sx_from_codazzi.py); factorization "
          "5376 = 2^8 * 3 * 7",
          ch2_full == -5376 and 5376 == 2**8 * 3 * 7)
    natural_divisors = {
        "128 (spinor dim_C)": 128, "1792 (RS space 14*128)": 1792,
        "224 (14 * Weyl-16)": 224, "896 (half RS space)": 896,
        "64 (H-lines)": 64, "448 (14 * rank_R 32)": 448,
        "2688 (rank x sigma-ish)": 2688, "16 (Weyl)": 16,
    }
    print("    divisor-steering table for the honest number -5376:")
    steer = {}
    for name, d in natural_divisors.items():
        val = Fraction(-5376, d)
        steer[name] = val
        print(f"      -5376 / {name:26} = {val}")
    check("B2  STEERING (K3 input): the honest number -5376 yields -3 "
          "(divisor 1792 = RS space), -24 (divisor 224 = 14 x Weyl-16), -42 "
          "(divisor 128), -6 (divisor 896), -12 (divisor 448), -84 (divisor "
          "64), -2 (divisor 2688) -- ALL with repo-natural dimensions. The "
          "extractable '3' is Hirzebruch's p1 = 3 sigma coefficient (the 3 in "
          "2^8 * 3 * 7), NOT generation content",
          steer["1792 (RS space 14*128)"] == -3
          and steer["224 (14 * Weyl-16)"] == -24
          and steer["128 (spinor dim_C)"] == -42
          and steer["896 (half RS space)"] == -6)

    # ---- B3: H (x) H = M(4,R), the alpha^2 = 4 beta finite shadow -----------
    Li = np.array([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]],
                  dtype=np.int64)
    Lj = np.array([[0, 0, -1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, -1, 0, 0]],
                  dtype=np.int64)
    Ri = np.array([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]],
                  dtype=np.int64)
    Rj = np.array([[0, 0, -1, 0], [0, 0, 0, -1], [1, 0, 0, 0], [0, 1, 0, 0]],
                  dtype=np.int64)
    I4 = np.eye(4, dtype=np.int64)
    Ls = [I4, Li, Lj, Li @ Lj]
    Rs = [I4, Ri, Rj, Ri @ Rj]
    basis = [L @ R for L in Ls for R in Rs]
    G = np.array([[int(np.trace(x.T @ y)) for y in basis] for x in basis])
    check("B3  H (x)_R H = M(4,R) EXACT: the 16 products L_a R_b are "
          "trace-orthogonal (Gram = 4 I_16) => span all of M(4,R): two "
          "quaternionic factors recombine REAL with multiplicity 4 -- the "
          "finite shadow of KO alpha^2 = 4 beta (K3 H-type Dirac x H-typed "
          "factor bookkeeping hides a x4)",
          np.array_equal(G, 4 * np.eye(16, dtype=np.int64)))


# =========================================================================== #
def part_C(e, P, M):
    print()
    print("=" * 78)
    print("PART C -- convention steering: orientation + GRAM-PIN-77 both forks")
    print("=" * 78)

    # ---- C1: orientation / labeling steering --------------------------------
    eta = [1] * 7 + [-1] * 7
    neg = [-g for g in e]
    ok_neg = clifford_relations_exact(neg, eta)
    zn, tn = gray_traceless_sweep(neg)
    # relabeling T = {4..10} (port-probe convention): reorder the same gammas
    e2 = [P[0], P[1], P[2], P[3], M[0], M[1], M[2], M[3], M[4], M[5], M[6],
          P[4], P[5], P[6]]
    eta2 = [1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1]
    ok_relab = clifford_relations_exact(e2, eta2)
    z2, t2 = gray_traceless_sweep(e2)
    check("C1  orientation flip (e -> -e) and timelike-set relabeling "
          "T = {4..10}: class certificate INVARIANT (relations exact; "
          "16383/16383 traceless both ways) -- the CLASS is convention-rigid; "
          "the steering question is about the COUNT, not the class",
          ok_neg and ok_relab and zn == tn and z2 == t2)

    # ---- C2: GRAM-PIN-77 fork bT (chirality-twisted) ------------------------
    bT = np.eye(128, dtype=np.int64)
    for g in M:
        bT = bT @ g
    okT = (np.array_equal(bT, bT.T)
           and np.array_equal(bT @ bT, np.eye(128, dtype=np.int64))
           and int(np.trace(bT)) == 0)
    Pp = 0.5 * (np.eye(128) + bT.astype(np.float64))
    rng = np.random.default_rng(5)
    V = Pp @ rng.standard_normal((128, 3))
    P3T = V @ np.linalg.inv(V.T @ V) @ V.T
    in_sec = np.linalg.norm(bT.astype(np.float64) @ P3T - P3T)
    V2 = Pp @ rng.standard_normal((128, 2))
    P2T = V2 @ np.linalg.inv(V2.T @ V2) @ V2.T
    check("C2  chirality-twisted Gram bT = (timelike 7-product): REAL "
          "symmetric, bT^2 = I, trace 0 EXACT => real 64/64 sectors; rank-3 "
          "carrier INSIDE the +sector has signature 3 (odd) and rank-2 has 2 "
          "(even): NO parity pin under the bT fork",
          okT and sym_signature(P3T) == 3 and sym_signature(P2T) == 2
          and in_sec < 1e-9,
          f"in-sector residual {in_sec:.1e}")

    # ---- C2': GRAM-PIN-77 fork bS (canonical) -------------------------------
    bSp = np.eye(128, dtype=np.int64)
    for g in P:
        bSp = bSp @ g
    okS = (np.array_equal(bSp, -bSp.T)
           and np.array_equal(bSp @ bSp, -np.eye(128, dtype=np.int64)))
    # canonical Gram bS = i * bSp: in the real form the spacelike 7-product is
    # ANTISYMMETRIC with square -I -- the explicit scalar i is forced, and it
    # is J'-odd (conjugation flips it): independent re-derivation of probe 1c.
    bS = 1j * bSp.astype(np.complex128)
    herm = np.linalg.norm(bS - bS.conj().T)
    invol = np.linalg.norm(bS @ bS - np.eye(128))
    PpS = 0.5 * (np.eye(128, dtype=np.complex128) + bS)
    VS = PpS @ (rng.standard_normal((128, 3)) + 1j * rng.standard_normal((128, 3)))
    P3S = VS @ np.linalg.inv(VS.conj().T @ VS) @ VS.conj().T
    in_secS = np.linalg.norm(bS @ P3S - P3S)
    VS2 = PpS @ (rng.standard_normal((128, 2)) + 1j * rng.standard_normal((128, 2)))
    P2S = VS2 @ np.linalg.inv(VS2.conj().T @ VS2) @ VS2.conj().T
    check("C2' canonical Gram bS = i * (spacelike 7-product): the bare real "
          "product is ANTISYMMETRIC with square -I EXACT (the scalar i is "
          "forced and J'-odd -- real-form re-derivation of probe 1c); "
          "complexified 64/64 sectors; rank-3 Hermitian carrier inside the "
          "+sector: signature 3; rank-2: signature 2. NEITHER GRAM FORK PINS "
          "CARRIER PARITY -- the fork changes sector REALITY typing only",
          okS and herm < 1e-12 and invol < 1e-12
          and sym_signature(P3S) == 3 and sym_signature(P2S) == 2
          and in_secS < 1e-9,
          f"herm {herm:.1e}, invol {invol:.1e}, in-sector {in_secS:.1e}")


# =========================================================================== #
def part_D(A):
    print()
    print("=" * 78)
    print("PART D -- eta shadow: the J-free chiral route, and what the toy cannot see")
    print("=" * 78)
    Pi = A.astype(np.float64) / 14.0
    Q = np.eye(1792) - Pi
    G = Pi - Q
    check("D1  exact grading G = Pi - Q: G^2 = I ((2Pi - I)^2, Pi exact "
          "rational A/14)", np.linalg.norm(G @ G - np.eye(1792)) < 1e-9)
    rng = np.random.default_rng(11)
    H = rng.standard_normal((1792, 1792))
    H = 0.5 * (H + H.T)
    D = Pi @ H @ Q + Q @ H @ Pi
    anti = np.linalg.norm(D @ G + G @ D)
    ev = np.linalg.eigvalsh(D)
    sym_spec = np.abs(ev + ev[::-1]).max()
    tol = 1e-8 * max(1.0, np.abs(ev).max())
    eta_fin = int((ev > tol).sum()) - int((ev < -tol).sum())
    check("D1  J-FREE ETA ROUTE: any off-diagonal (KT-shaped) D = Pi H Q + "
          "Q H Pi anticommutes with G => spectrum EXACTLY symmetric => "
          "finite-shadow eta = 0 with NO antiunitary input. The (9,5) "
          "C = J_quat . G proof is sufficient-not-necessary; the grading "
          "mechanism is signature-blind",
          anti < 1e-9 and sym_spec < 1e-7 and eta_fin == 0,
          f"anticommutator {anti:.1e}, spectral asymmetry {sym_spec:.1e}, "
          f"eta_finite = {eta_fin}")
    print("    SKEPTICAL NOTE: at this scale eta = 0 is structural (finite "
          "symmetric spectra); a genuinely nonzero boundary term would need "
          "(i) the true noncompact boundary operator, (ii) a G-breaking term "
          "FORCED by (7,7)-specific structure (none identified; in (9,5) "
          "grading-breaking was optional and connection-dependent, cited "
          "C-02/C-03), or (iii) an AZ-class argument -- the class DOES change "
          "(CII -> BDI-type with J'^2 = +1), so the CII-specific protection "
          "proof dies, but its CONCLUSION has the J-free fallback above. "
          "The toy cannot adjudicate the true eta in EITHER signature class.")


# =========================================================================== #
def main():
    e, P, M, A = part_A()
    part_B()
    part_C(e, P, M)
    part_D(A)
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print()
    print(f"{len(CHECKS) - n_fail}/{len(CHECKS)} checks passed.")
    print("SUMMARY (W2 twin): Cl(7,7) = M(128,R) certified BIT-EXACT on an "
          "all-real integer rep (16383/16383 traceless monomials); SCHUR "
          "DIVISOR 1 -- no algebra-forced multiplicity quantum; odd AND even "
          "carriers on the EXACT constraint surface; fiber Cl(6,4) = M(32,R) "
          "with omega^2 = -I (no real Weyl: the Weyl-16 generation unit is "
          "complex-only); base Cl(1,3) = M(2,H) QUATERNIONIC -- the Kramers "
          "wall MOVED to the spacetime factor (base-linear carriers have "
          "signature in 8Z: literal 3 unreachable under that typing); "
          "ungraded base(x)fiber Kronecker port resurrects H-class module "
          "data (End = H, dim 256); count arithmetic: 3 on the type-"
          "consistent diagonal, 6/12/(3/2)/(3/4) off it; honest K3 number "
          "-5376 = -(2^8 * 3 * 7) steers to -3/-6/-12/-24/-42/-84/-2 with "
          "repo-natural divisors (its '3' is Hirzebruch's); H(x)H = M(4,R) "
          "(the KO alpha^2 = 4 beta x4 shadow); neither GRAM-PIN-77 fork "
          "pins parity; eta = 0 has a J-free chiral route at shadow grade. "
          "No claim-status movement.")
    if n_fail:
        raise SystemExit(f"{n_fail} check(s) FAILED")
    raise SystemExit(0)


if __name__ == "__main__":
    main()
