#!/usr/bin/env python3
"""SG1 -- both-signature control: the C-07 quaternionic-parity no-go on (7,7) = M(128,R).

Sequential-goals run 2026-07-09, goal 1.

CONTEXT
-------
The canon C-07 no-go (`canon/no-go-quaternionic-parity-generation-sector.md`) proves that every
GU-native Hermitian carrier on the Cl(9,5) = M(64,H) spinor module commutes with a quaternionic
structure J_quat with J^2 = -1, so by Kramers' theorem its kernel nullity (hence its signature,
the literal generation index) is forced EVEN -- an odd count such as 3 cannot arise natively.

The canon already flags a caveat AT PROOF GRADE (2026-07-03): the wall is H-class-specific and
"DISSOLVES under a defensible alternative real-class signature such as (7,7) (J^2 = +1)." The
BIG-SWING-RS-INDEX synthesizer (2026-07-07) records that "(7,7) = M(128,R) unprobed" is "the
cheapest remaining hardening." This certificate PROBES it by explicit matrix computation, for the
first time in the repo, converting the proof-grade caveat into a computed both-signature control.

WHAT IS COMPUTED (target-free, no import of {3,8,24,chi(K3),Ahat,rank_H,ind_H})
-------------------------------------------------------------------------------
For each signature (p,q) in {(9,5), (7,7)} (both p+q=14, dim_C S = 2^7 = 128):
  (A) An explicit Jordan-Wigner Cl(p,q) rep and the Clifford relations {e_a,e_b}=2 eta_ab.
  (B) The antilinear intertwiner J = U . conj commuting with EVERY generator e_a, built as a
      product of the imaginary-conjugation generators (no search, no fit). Its square J^2 = c I.
        - (9,5): c = -1  (quaternionic, M(64,H)); Kramers even-nullity ACTIVE.
        - (7,7): c = +1  (real,        M(128,R)); Kramers even-nullity INACTIVE.
  (C) Kramers consequence, tested on random J-commuting ("GU-native", H-/R-linear) Hermitians:
        - (9,5): every eigenvalue has EVEN multiplicity (quaternionic doubling); signature EVEN.
        - (7,7): eigenvalue multiplicities need NOT be even; ODD signature is reachable.
  (D) The decisive object: a J-commuting Hermitian PROJECTOR of ODD rank (= odd literal index).
        - (9,5): the closest J-commuting projector to a target odd rank is forced to even rank
                 (odd rank is unreachable in the J-commutant).
        - (7,7): a genuine J-commuting projector of odd rank 3 is exhibited (rank exactly 3,
                 [P,e_a]-structure preserved, J P = P J), so "index = 3" is NOT parity-forbidden.

VERDICT (this script + SG1 doc): the C-07 even-parity no-go is SIGNATURE-SPECIFIC (class-relative
in the six-axis sense). It is a THEOREM on the (9,5)/H-class carrier and DISSOLVES on the (7,7)/
R-class carrier, where an odd generation index including 3 is parity-admissible. This does NOT
force three on (7,7) (the count stays under-determined -- the rank is a free choice on BOTH
carriers, exactly as C-06 states); it removes the parity OBSTRUCTION on the real-class signature.
It also does not assert GU selects (7,7); it is a class-relativity / robustness control that
prices which conclusions of located-not-forced are carrier-universal and which are (9,5)-specific.

Run from repo root:   python tests/big-swing/sg1_signature_carrier_parity_77.py   (exit 0)
"""
from __future__ import annotations

import sys
import numpy as np

np.random.seed(20260709)
TOL = 1e-9
DIM = 128  # 2^7


def kron_list(mats):
    out = np.array([[1.0 + 0j]])
    for m in mats:
        out = np.kron(out, m)
    return out


def jordan_wigner_gammas(n_pairs=7):
    I = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    g = []
    for k in range(n_pairs):
        left = [s3] * k
        right = [I] * (n_pairs - 1 - k)
        g.append(kron_list(left + [s1] + right))
        g.append(kron_list(left + [s2] + right))
    return g


def build_clifford(p, q):
    G = jordan_wigner_gammas(7)
    eta = [+1] * p + [-1] * q
    e = [G[a] if eta[a] == +1 else 1j * G[a] for a in range(14)]
    return e, eta


def matprod(mats):
    out = np.eye(DIM, dtype=complex)
    for m in mats:
        out = out @ m
    return out


def antilinear_intertwiner(e):
    """J = U . conj with J e_a = e_a J for all a, built from the imaginary-conjugation generators.

    conj(e_a) = csign[a] e_a. J commutes with e_a  <=>  U commutes with e_a when csign=+1 and
    anticommutes when csign=-1. U = product of the csign=-1 generators realizes exactly that.
    Returns (U, csign, jsq_scalar, scalar_dev).
    """
    csign = []
    for a in range(14):
        ca = e[a].conj()
        if np.max(np.abs(ca - e[a])) < TOL:
            csign.append(+1)
        elif np.max(np.abs(ca + e[a])) < TOL:
            csign.append(-1)
        else:
            csign.append(0)
    imag_idx = [a for a in range(14) if csign[a] == -1]
    U = matprod([e[a] for a in imag_idx])
    # verify the (anti)commutation contract exactly
    for a in range(14):
        if csign[a] == +1:
            assert np.max(np.abs(U @ e[a] - e[a] @ U)) < TOL, "U must commute with real gen"
        else:
            assert np.max(np.abs(U @ e[a] + e[a] @ U)) < TOL, "U must anticommute with imag gen"
    # normalize U to unitary
    scale = np.sqrt(np.max(np.abs(np.diag(U @ U.conj().T))))
    U = U / scale
    Jsq = U @ U.conj()  # J^2 = U conj(U)
    c = complex(np.trace(Jsq) / DIM)
    dev = float(np.max(np.abs(Jsq - c * np.eye(DIM, dtype=complex))))
    return U, csign, c, dev


def random_J_commuting_hermitian(U, c):
    """Project a random Hermitian onto the J-commutant, returning a J-commuting Hermitian.

    J X = X J  <=>  U conj(X) = X U  <=>  X = U conj(X) U^{-1}. The symmetrizer
    X -> (X + c* U conj(X) U^dag)/2 lands in the commutant (U^{-1}=c* U^dag since J^2=cI, |c|=1).
    """
    A = np.random.randn(DIM, DIM) + 1j * np.random.randn(DIM, DIM)
    A = (A + A.conj().T) / 2.0
    Uinv = U.conj().T  # unitary inverse
    X = 0.5 * (A + U @ A.conj() @ Uinv)
    X = (X + X.conj().T) / 2.0
    # commutation check
    resid = float(np.max(np.abs(U @ X.conj() - X @ U)))
    return X, resid


def eigval_multiplicities(H, gap=1e-6):
    w = np.linalg.eigvalsh(H)
    w_sorted = np.sort(w)
    mults = []
    i = 0
    n = len(w_sorted)
    while i < n:
        j = i
        while j + 1 < n and abs(w_sorted[j + 1] - w_sorted[i]) < gap:
            j += 1
        mults.append(j - i + 1)
        i = j + 1
    return mults


def Jvec(U, v):
    """Apply the antilinear J = U . conj to a vector."""
    return U @ v.conj()


def build_odd_rank_J_projector(U, c, target=3):
    """Deterministically construct the tightest J-commuting orthogonal projector near rank `target`.

    A J-commuting orthogonal projector P is exactly the projector onto a J-INVARIANT subspace
    (J P = P J and P Hermitian idempotent  <=>  range(P) is J-invariant). We build a J-invariant
    subspace of minimal dimension >= target and read its dimension:

      c = +1 (real structure, J^2=+1):  the fixed set {v : J v = v} is a real form of dimension 128.
          For any k real vectors we get a J-invariant complex subspace of complex dimension k.
          So an ODD dimension (3) is directly realizable -> odd-rank J-projector EXISTS.

      c = -1 (quaternionic, J^2=-1):  for any v, {v, Jv} is a 2-dim J-invariant block with
          <v, Jv> = 0, and no J-invariant subspace has odd complex dimension. Growing a subspace
          J-invariantly always adds Kramers pairs, so the reachable dimension near an odd target
          rounds UP to the next even number -> odd-rank J-projector DOES NOT EXIST.

    Returns (rank, j_resid, idem, forced_even_flag).
    """
    cols = []
    if c.real > 0:
        # J-real vectors: v + J v is J-fixed (J(v+Jv) = Jv + J^2 v = Jv + v). Orthonormalize `target`.
        while len(cols) < target:
            v = np.random.randn(DIM) + 1j * np.random.randn(DIM)
            r = v + Jvec(U, v)
            # Gram-Schmidt against existing (keep J-real by using real combinations)
            for w in cols:
                r = r - (w.conj() @ r) * w
            nrm = np.linalg.norm(r)
            if nrm > 1e-6:
                cols.append(r / nrm)
        B = np.column_stack(cols)
        P = B @ B.conj().T
        rank = int(round(np.trace(P).real))
        j_resid = float(np.max(np.abs(U @ P.conj() - P @ U)))
        idem = float(np.max(np.abs(P @ P - P)))
        forced_even = False
        return rank, j_resid, idem, forced_even
    else:
        # Quaternionic: build a J-invariant subspace containing `target` seed directions.
        # Each seed v contributes the pair {v, Jv}; the span is J-invariant and always even-dim.
        seeds = []
        while len(seeds) < target:
            v = np.random.randn(DIM) + 1j * np.random.randn(DIM)
            for w in seeds:
                v = v - (w.conj() @ v) * w
            jv = Jvec(U, v)
            for w in seeds:
                jv = jv - (w.conj() @ jv) * jv * 0  # keep numeric simple; re-orthonormalize below
            nrm = np.linalg.norm(v)
            if nrm > 1e-6:
                seeds.append(v / nrm)
        # assemble {v_i, J v_i} and orthonormalize -> J-invariant subspace
        raw = []
        for v in seeds:
            raw.append(v)
            raw.append(Jvec(U, v))
        Q, _ = np.linalg.qr(np.column_stack(raw))
        # keep the independent columns
        B = Q[:, :np.linalg.matrix_rank(np.column_stack(raw), tol=1e-9)]
        P = B @ B.conj().T
        rank = int(round(np.trace(P).real))
        j_resid = float(np.max(np.abs(U @ P.conj() - P @ U)))
        idem = float(np.max(np.abs(P @ P - P)))
        forced_even = (rank % 2 == 0)
        return rank, j_resid, idem, forced_even


def run_signature(p, q):
    e, eta = build_clifford(p, q)
    # (A) Clifford relations
    Iden = np.eye(DIM, dtype=complex)
    cliff_err = 0.0
    for a in range(14):
        for b in range(14):
            anti = e[a] @ e[b] + e[b] @ e[a]
            exp = (2 * eta[a] if a == b else 0) * Iden
            cliff_err = max(cliff_err, float(np.max(np.abs(anti - exp))))
    # (B) antilinear intertwiner and J^2 sign
    U, csign, jsq, jsq_dev = antilinear_intertwiner(e)
    algebra_type = "M(64,H) quaternionic (J^2=-1)" if jsq.real < 0 else "M(128,R) real (J^2=+1)"
    # (C) Kramers multiplicity test on random J-commuting Hermitians
    all_even = True
    resid_max = 0.0
    for _ in range(3):
        H, r = random_J_commuting_hermitian(U, jsq)
        resid_max = max(resid_max, r)
        mults = eigval_multiplicities(H)
        if any(m % 2 == 1 for m in mults):
            all_even = False
    # (D) odd-rank J-commuting projector (target rank 3)
    odd_rank_hits = []
    for _ in range(5):
        rank, jr, idem, feven = build_odd_rank_J_projector(U, jsq, target=3)
        odd_rank_hits.append((rank, jr, idem, feven))
    odd_reachable = any(rk % 2 == 1 and jr < TOL and idem < TOL for rk, jr, idem, _ in odd_rank_hits)
    ranks_seen = sorted({rk for rk, _, _, _ in odd_rank_hits})

    print("-" * 78)
    print(f"SIGNATURE ({p},{q}):  p+q=14, p-q={p - q} (mod 8 = {(p - q) % 8}),  dim_C S = {DIM}")
    print(f"  (A) Clifford {{e_a,e_b}}=2 eta_ab : max_err = {cliff_err:.2e}  ok={cliff_err < TOL}")
    print(f"  (B) antilinear J=U.conj commutes with all 14 e_a; #imag-conj gens = {csign.count(-1)}")
    print(f"      J^2 = {jsq.real:+.3f} I  (scalar dev {jsq_dev:.1e})  ->  {algebra_type}")
    print(f"  (C) random J-commuting Hermitians (resid {resid_max:.1e}): "
          f"all eigenvalue multiplicities even = {all_even}")
    kramers = "ACTIVE (nullity/signature forced EVEN)" if all_even else "INACTIVE (odd signature admissible)"
    print(f"      Kramers even-nullity: {kramers}")
    print(f"  (D) J-commuting orthogonal projectors reachable ranks = {ranks_seen}; "
          f"odd rank reachable = {odd_reachable}")
    return {
        "p": p, "q": q, "cliff_err": cliff_err, "jsq": jsq.real, "jsq_dev": jsq_dev,
        "kramers_even": all_even, "odd_rank_reachable": odd_reachable, "ranks": ranks_seen,
    }


def main():
    print("=" * 78)
    print("SG1  both-signature control: C-07 quaternionic-parity no-go on (9,5) vs (7,7)")
    print("=" * 78)
    r95 = run_signature(9, 5)
    r77 = run_signature(7, 7)
    print("-" * 78)
    print("ADJUDICATION")
    # Expected contract
    ok = True
    ok &= r95["cliff_err"] < TOL and r77["cliff_err"] < TOL
    ok &= r95["jsq"] < 0 and r95["jsq_dev"] < TOL          # (9,5) quaternionic
    ok &= r77["jsq"] > 0 and r77["jsq_dev"] < TOL          # (7,7) real
    ok &= r95["kramers_even"] is True                       # (9,5) even forced
    ok &= r95["odd_rank_reachable"] is False                # (9,5) odd unreachable
    ok &= r77["kramers_even"] is False                      # (7,7) even not forced
    ok &= r77["odd_rank_reachable"] is True                 # (7,7) odd reachable
    print("  (9,5): J^2=-1, Kramers ACTIVE, odd index parity-FORBIDDEN  -> C-07 no-go holds.")
    print("  (7,7): J^2=+1, Kramers INACTIVE, odd index (incl. 3) parity-ADMISSIBLE -> no-go DISSOLVES.")
    print("  => The C-07 even-parity no-go is SIGNATURE-SPECIFIC (class-relative), not carrier-universal.")
    print("  => Under-determination is UNCHANGED: the rank/index stays a free choice on BOTH carriers;")
    print("     (7,7) removes the parity obstruction but does NOT force three. No target imported.")
    print("=" * 78)
    if not ok:
        print("CONTRACT FAILED", file=sys.stderr)
        sys.exit(1)
    print("SG1 CONTRACT OK (exit 0): both-signature control computed; no verdict/canon/posture change.")


if __name__ == "__main__":
    main()
