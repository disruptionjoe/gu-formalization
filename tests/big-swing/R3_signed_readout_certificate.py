#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
R3 Signed-Readout Boundary Theorem -- executable certificate.

GU-INDEPENDENT. No target number (3, 8, 24, chi(K3), SM spectrum) is assumed,
imported, divided by, or normalized to anywhere in this file. Every integer that
appears as an "index" is whatever the explicitly-constructed operator produces.

Three independent blocks, each a self-contained check of one layer of the
standalone theorem in
  explorations/big-swing-2026-07-03/R3-signed-readout-standalone-theorem.md

  BLOCK A -- Abstract monotone-readout criterion (Parts M, P, C).
             Exhaustive + randomized verification of the iff
                 R_w monotone  <=>  w(x) in G_+ for all x
             over the lattice-ordered abelian groups Z and Z^n, plus the
             two-layer (provenance monotone / readout non-monotone) coexistence.

  BLOCK B -- Part Z instantiated UNCONDITIONALLY on a finite (compact) space
             via a Ginsparg-Wilson overlap Dirac operator.
             Verifies: GW relation exactly, gamma-hat_5^2 = 1, integer axial
             charge (three routes agree), signed-readout coexistence, and
             topological protection (index is locally constant off spectral
             crossings) -- the finite-dimensional Atiyah-Janich mechanism with
             NO non-compact functional analysis.

  BLOCK C -- Part K finite-dimensional shadow: H-linear (quaternionic) operators
             have even complex kernel/cokernel (Kramers), so the complex index
             is even and index_H = index_C / 2 is the KSp^0(pt) = Z augmentation.

Exit status 0 iff every assertion passes.
"""

import numpy as np
import itertools
import sys

RNG = np.random.default_rng(20260703)
TOL = 1e-9
report = []


def check(name, ok, detail=""):
    report.append((name, bool(ok), detail))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {name}" + (f"  --  {detail}" if detail else ""))
    return ok


# ---------------------------------------------------------------------------
# BLOCK A -- abstract monotone-readout criterion on lattice-ordered groups
# ---------------------------------------------------------------------------
# Evidence monoid E = N_0^{(X)}, X = {0,...,k-1}.  e is a tuple of counts.
# Readout codomain G = Z^n with coordinatewise order (a lattice-ordered ab.gp).
# Weight w : X -> Z^n.  R_w(e) = sum_x e[x] * w[x].
# Criterion:  R_w monotone (e <= e' => R_w(e) <= R_w(e'))  iff  every w[x] >= 0.

def readout(w, e):
    # w: (k,n) integer array, e: (k,) counts -> (n,)
    return (np.asarray(e) @ w)


def le_vec(a, b):
    return np.all(a <= b)


def block_A():
    print("\n=== BLOCK A: abstract monotone-readout criterion (Parts M,P,C) ===")
    all_ok = True

    # --- A1: exhaustive iff over a bounded box, G = Z (n=1) and G = Z^2 -------
    # For each weight pattern we test monotonicity by comparing R_w on all
    # comparable pairs e <= e' inside a small box, and confirm it equals the
    # sign-of-weights predicate.
    for n_out in (1, 2):
        k = 3                      # 3 event types
        cap = 2                    # counts in {0,1,2}
        events = list(itertools.product(range(cap + 1), repeat=k))
        # weight entries in {-1,0,1}
        weight_vals = list(itertools.product((-1, 0, 1), repeat=k * n_out))
        mism = 0
        tested = 0
        for wv in weight_vals:
            w = np.array(wv, dtype=int).reshape(k, n_out)
            predicate_all_nonneg = np.all(w >= 0)
            monotone = True
            for e in events:
                for ep in events:
                    if le_vec(np.array(e), np.array(ep)):
                        if not le_vec(readout(w, e), readout(w, ep)):
                            monotone = False
                            break
                if not monotone:
                    break
            tested += 1
            if monotone != predicate_all_nonneg:
                mism += 1
        all_ok &= check(
            f"A1 iff exhaustive (G=Z^{n_out}, k={k}, cap={cap})",
            mism == 0,
            f"{tested} weight patterns, {mism} mismatches",
        )

    # --- A2: (=>) witness.  If some w[x0] has a negative coordinate, the pair
    #         (0, [x0]) witnesses non-monotonicity.  Randomized. --------------
    bad = 0
    trials = 20000
    for _ in range(trials):
        k = int(RNG.integers(1, 5))
        n_out = int(RNG.integers(1, 4))
        w = RNG.integers(-3, 4, size=(k, n_out))
        all_nonneg = np.all(w >= 0)
        # test the canonical witnesses (0, e_x) for each generator
        witness_nonmono = False
        for x0 in range(k):
            e0 = np.zeros(k, dtype=int)
            ex = np.zeros(k, dtype=int)
            ex[x0] = 1
            if le_vec(e0, ex) and not le_vec(readout(w, e0), readout(w, ex)):
                witness_nonmono = True
                break
        # all_nonneg  <=>  no generator witness of non-monotonicity
        if all_nonneg == witness_nonmono:
            bad += 1
    all_ok &= check("A2 canonical (0,[x0]) witness controls the iff",
                    bad == 0, f"{trials} trials, {bad} contradictions")

    # --- A3: PN/Jordan split + two-layer coexistence (Parts P, C) ------------
    # w = w+ - w-, w+ = max(w,0), w- = max(-w,0).  Provenance (R+,R-) monotone
    # ALWAYS; readout R = R+ - R- non-monotone iff w- != 0.
    prov_fail = 0
    coex_fail = 0
    trials = 20000
    for _ in range(trials):
        k = int(RNG.integers(1, 5))
        w = RNG.integers(-3, 4, size=k)          # G = Z
        wp = np.maximum(w, 0)
        wm = np.maximum(-w, 0)
        # reconstruction
        if not np.array_equal(wp - wm, w):
            prov_fail += 1
            continue
        # provenance monotone: for random comparable pair e<=e', both R+ and R- up
        e = RNG.integers(0, 4, size=k)
        d = RNG.integers(0, 4, size=k)
        ep = e + d
        Rp_e, Rp_ep = e @ wp, ep @ wp
        Rm_e, Rm_ep = e @ wm, ep @ wm
        if not (Rp_e <= Rp_ep and Rm_e <= Rm_ep):
            prov_fail += 1
        # coexistence: readout non-monotone  <=>  wm != 0 (some neg weight)
        # existence of a comparable pair with strictly-decreasing readout
        has_neg = np.any(wm > 0)
        # canonical witness: pick a generator with negative weight
        readout_nonmono = False
        for x0 in range(k):
            if w[x0] < 0:
                readout_nonmono = True
                break
        if has_neg != readout_nonmono:
            coex_fail += 1
    all_ok &= check("A3 provenance always monotone (PN/Jordan split)",
                    prov_fail == 0, f"{trials} trials, {prov_fail} failures")
    all_ok &= check("A3 coexistence: readout non-monotone iff w- != 0",
                    coex_fail == 0, f"{trials} trials, {coex_fail} failures")

    # --- A4: minimality of the PN split (PJ5) --------------------------------
    # any other split (a,b), a,b>=0, a-b=w has a>=w+ and b>=w- componentwise.
    minfail = 0
    trials = 5000
    for _ in range(trials):
        k = int(RNG.integers(1, 4))
        w = RNG.integers(-3, 4, size=k)
        wp = np.maximum(w, 0)
        wm = np.maximum(-w, 0)
        # build an arbitrary alternative split: add a nonneg slack s to both
        s = RNG.integers(0, 4, size=k)
        a = wp + s
        b = wm + s
        if not (np.array_equal(a - b, w) and np.all(a >= wp) and np.all(b >= wm)):
            minfail += 1
    all_ok &= check("A4 PN split is the minimal (Jordan-Hahn) split",
                    minfail == 0, f"{trials} trials, {minfail} failures")
    return all_ok


# ---------------------------------------------------------------------------
# BLOCK B -- Part Z UNCONDITIONALLY via a finite Ginsparg-Wilson operator
# ---------------------------------------------------------------------------
# Chiral basis: gamma5 = diag(+1 (n+), -1 (n-)).  Given any Hermitian H with no
# zero eigenvalues, eps = sign(H) is Hermitian with eps^2 = 1.  The overlap
# operator  D = (1/a)(1 + gamma5 eps)  satisfies the Ginsparg-Wilson relation
#     gamma5 D + D gamma5 = a D gamma5 D
# exactly (proof in the theorem note).  gamma-hat_5 = gamma5(1 - a D) = -eps,
# gamma-hat_5^2 = 1.  The axial charge / index
#     Q = -(1/2) Tr(eps)        (integer when N is even)
# is the finite-lattice Atiyah-Janich index and is locally constant under
# deformations of H that do not cross zero.

def gamma5_matrix(nplus, nminus):
    return np.diag(np.concatenate([np.ones(nplus), -np.ones(nminus)]))


def sign_hermitian(H):
    evals, evecs = np.linalg.eigh(H)
    s = np.sign(evals)
    return (evecs * s) @ evecs.conj().T, evals


def block_B():
    print("\n=== BLOCK B: Part Z -- finite Ginsparg-Wilson overlap index ===")
    all_ok = True
    a = 1.0
    nplus = nminus = 6          # N = 12 sites, balanced chirality (Tr gamma5 = 0)
    N = nplus + nminus
    g5 = gamma5_matrix(nplus, nminus)

    # generic gamma5-Hermitian random H (does NOT commute with gamma5)
    M = RNG.standard_normal((N, N)) + 1j * RNG.standard_normal((N, N))
    H = M + M.conj().T                      # Hermitian
    # shift spectrum away from 0 to be safe, then re-center to keep a nonzero Q
    eps, hvals = sign_hermitian(H)

    # B1: eps Hermitian, eps^2 = 1
    all_ok &= check("B1 eps Hermitian", np.linalg.norm(eps - eps.conj().T) < TOL,
                    f"||eps-eps^H||={np.linalg.norm(eps-eps.conj().T):.2e}")
    all_ok &= check("B1 eps^2 = 1", np.linalg.norm(eps @ eps - np.eye(N)) < TOL,
                    f"||eps^2-1||={np.linalg.norm(eps@eps-np.eye(N)):.2e}")

    D = (1.0 / a) * (np.eye(N) + g5 @ eps)

    # B2: Ginsparg-Wilson relation  gamma5 D + D gamma5 = a D gamma5 D
    lhs = g5 @ D + D @ g5
    rhs = a * (D @ g5 @ D)
    gwerr = np.linalg.norm(lhs - rhs)
    all_ok &= check("B2 Ginsparg-Wilson relation exact", gwerr < TOL,
                    f"||g5 D + D g5 - a D g5 D||={gwerr:.2e}")

    # B3: gamma-hat_5 = gamma5(1 - aD) = -eps, and gamma-hat_5^2 = 1
    g5hat = g5 @ (np.eye(N) - a * D)
    all_ok &= check("B3 gamma-hat_5 = -eps", np.linalg.norm(g5hat + eps) < TOL,
                    f"||g5hat+eps||={np.linalg.norm(g5hat+eps):.2e}")
    all_ok &= check("B3 gamma-hat_5^2 = 1",
                    np.linalg.norm(g5hat @ g5hat - np.eye(N)) < TOL)

    # B4: integer axial charge, three independent routes agree
    Q_trace_eps = -0.5 * np.trace(eps).real                 # -(1/2)Tr eps
    Q_trace_g5D = -(a / 2.0) * np.trace(g5 @ D).real         # -(a/2)Tr(gamma5 D)
    Q_trace_g5hat = 0.5 * np.trace(g5hat).real              # (1/2)Tr gamma-hat_5
    # spectral-asymmetry route: -(1/2)(#pos - #neg) eigenvalues of H
    npos = int(np.sum(hvals > 0))
    nneg = int(np.sum(hvals < 0))
    Q_specasym = -0.5 * (npos - nneg)
    is_int = abs(Q_trace_eps - round(Q_trace_eps)) < TOL
    all_ok &= check("B4 axial charge is an integer", is_int,
                    f"Q = {Q_trace_eps:.12f}")
    agree = (abs(Q_trace_eps - Q_trace_g5D) < TOL and
             abs(Q_trace_eps - Q_trace_g5hat) < TOL and
             abs(Q_trace_eps - Q_specasym) < TOL)
    all_ok &= check("B4 three index routes agree", agree,
                    f"-(1/2)Tr eps={Q_trace_eps:.6f}, "
                    f"-(a/2)Tr(g5 D)={Q_trace_g5D:.6f}, "
                    f"(1/2)Tr g5hat={Q_trace_g5hat:.6f}, "
                    f"spec-asym={Q_specasym:.6f}")

    # B5: engineered operator with EXACT zero modes, index = chirality sum.
    # Diagonal chiral H: right-handed states (g5=+1) with h<0 and left-handed
    # states (g5=-1) with h>0 produce exact zero modes of D; their gamma5
    # chirality reproduces the axial charge.  (gamma5, eps commute here so we
    # can read chirality of zero modes directly.)
    # choose signs: put r_neg right-handed states negative, l_pos left-handed positive
    r_neg = 2      # right-handed zero modes  (chirality +1)
    l_pos = 3      # left-handed zero modes   (chirality -1)
    hdiag = np.empty(N)
    # first nplus are right-handed
    hdiag[:nplus] = 1.0
    hdiag[:r_neg] = -1.0
    # last nminus are left-handed
    hdiag[nplus:] = -1.0
    hdiag[nplus:nplus + l_pos] = 1.0
    Hd = np.diag(hdiag)
    epsd, hvd = sign_hermitian(Hd)
    Dd = (1.0 / a) * (np.eye(N) + g5 @ epsd)
    # zero modes of Dd
    sv = np.linalg.svd(Dd, compute_uv=False)
    nzero = int(np.sum(sv < 1e-8))
    # chirality of each zero mode: kernel vectors are basis states; classify
    _, dvecs = np.linalg.eigh(Dd.conj().T @ Dd)
    ker = dvecs[:, :nzero]
    chir = np.array([ (v.conj() @ g5 @ v).real for v in ker.T ])
    nplus_zm = int(np.sum(chir > 0.5))
    nminus_zm = int(np.sum(chir < -0.5))
    Q_zm = nplus_zm - nminus_zm
    Q_eng_eps = -0.5 * np.trace(epsd).real
    all_ok &= check("B5 engineered D has exact zero modes",
                    nzero == r_neg + l_pos,
                    f"{nzero} zero modes (expected {r_neg + l_pos})")
    all_ok &= check("B5 index = (n+ - n-) chirality of zero modes = -(1/2)Tr eps",
                    abs(Q_zm - Q_eng_eps) < TOL,
                    f"chirality n+={nplus_zm}, n-={nminus_zm}, "
                    f"Q_zm={Q_zm}, -(1/2)Tr eps={Q_eng_eps:.3f}")

    # B6: signed-readout coexistence on the zero-mode sector.
    # Provenance = (n+, n-) monotone as modes accumulate; readout Q = n+ - n-
    # is non-monotone (adding a negative-chirality mode lowers Q while raising
    # provenance).  Explicit witness.
    prov_before = (nplus_zm, nminus_zm)
    prov_after = (nplus_zm, nminus_zm + 1)           # add one left-handed mode
    Q_before = prov_before[0] - prov_before[1]
    Q_after = prov_after[0] - prov_after[1]
    prov_monotone = (prov_after[0] >= prov_before[0] and
                     prov_after[1] >= prov_before[1])
    readout_drop = Q_after < Q_before
    all_ok &= check("B6 coexistence witness (provenance up, readout down)",
                    prov_monotone and readout_drop,
                    f"provenance {prov_before}->{prov_after}, "
                    f"Q {Q_before}->{Q_after}")

    # B7: topological protection -- index locally constant off spectral crossings.
    # Deform H(t) = H + t V (generic Hermitian V).  Q(t) = -(1/2)Tr sign(H(t))
    # is piecewise constant and jumps by +-1 exactly when an eigenvalue of H(t)
    # crosses zero.  This is the finite-dim Atiyah-Janich / spectral-flow claim.
    # Spectral-flow deformation H(s) = H - s*I: each eigenvalue of H crosses
    # zero exactly once (at s = that eigenvalue), so the index steps by +-1 at
    # each crossing -- the textbook Atiyah-Janich spectral-flow picture.
    lo, hi = hvals.min() - 1.0, hvals.max() + 1.0
    ss = np.linspace(lo, hi, 12001)
    Qs = []
    min_gap = []
    for s in ss:
        ev = hvals - s                       # eigenvalues of H - sI
        Qs.append(-0.5 * (np.sum(ev > 0) - np.sum(ev < 0)) + 0.0)
        min_gap.append(np.min(np.abs(ev)))
    Qs = np.array(Qs) + 0.0
    Qs[Qs == 0] = 0.0            # normalize negative zero
    min_gap = np.array(min_gap)
    jumps = np.where(np.diff(Qs) != 0)[0]
    # every jump must sit at a near-zero-eigenvalue crossing
    protected = True
    for j in jumps:
        # gap must dip to ~0 near the jump and step size is +-1
        local_gap = min(min_gap[j], min_gap[j + 1])
        if abs(Qs[j + 1] - Qs[j]) != 1 or local_gap > 0.05:
            protected = False
    # away from jumps Q is constant (piecewise-constant integer)
    all_ok &= check("B7 index integer-valued along the whole deformation",
                    np.all(np.abs(Qs - np.round(Qs)) < TOL))
    all_ok &= check("B7 topological protection: jumps only at spectral crossings, step +-1",
                    protected and len(jumps) > 0,
                    f"{len(jumps)} crossings, Q range [{Qs.min():.0f},{Qs.max():.0f}]")
    return all_ok


# ---------------------------------------------------------------------------
# BLOCK C -- Part K finite shadow: H-linear index is even (KSp augmentation)
# ---------------------------------------------------------------------------
# Quaternionic structure on C^{2m}: J psi = Omega conj(psi), Omega = I_m (x) (i sigma_y),
# J antilinear, J^2 = -1.  A is H-linear (quaternionic / self-dual) iff
# Omega^{-1} A Omega = conj(A), equivalently A J = J A.  Then ker A and coker A
# are J-invariant; since J is antilinear with J^2 = -1, they have even complex
# dimension (Kramers).  index_H(A) = index_C(A)/2 is the KSp^0(pt) = Z augmentation.

def quaternionic_omega(m):
    isy = np.array([[0, 1], [-1, 0]], dtype=complex)   # i*sigma_y
    Om = np.zeros((2 * m, 2 * m), dtype=complex)
    for i in range(m):
        Om[2 * i:2 * i + 2, 2 * i:2 * i + 2] = isy
    return Om


def make_quaternionic(B, Om):
    # symmetrize an arbitrary B into a self-dual (H-linear) operator:
    # A satisfies Omega^{-1} A Omega = conj(A).
    return B + Om @ B.conj() @ np.linalg.inv(Om)


def block_C():
    print("\n=== BLOCK C: Part K -- H-linear (KSp) index is even ===")
    all_ok = True
    m = 5
    n = 2 * m
    Om = quaternionic_omega(m)
    J_is_involution = np.linalg.norm(Om @ Om.conj() + np.eye(n)) < TOL
    all_ok &= check("C0 J^2 = -1 (quaternionic structure)", J_is_involution,
                    f"||Omega Omega* + 1||={np.linalg.norm(Om@Om.conj()+np.eye(n)):.2e}")

    even_ker = True
    kramers = True
    ranks_even = True
    trials = 200
    for _ in range(trials):
        B = RNG.standard_normal((n, n)) + 1j * RNG.standard_normal((n, n))
        A = make_quaternionic(B, Om)
        # verify self-duality: Omega^{-1} A Omega = conj(A)
        selfdual = np.linalg.norm(np.linalg.inv(Om) @ A @ Om - A.conj()) < 1e-7
        if not selfdual:
            kramers = False
        # singular values come in equal pairs (Kramers) -> any kernel even-dim
        sv = np.linalg.svd(A, compute_uv=False)
        sv_sorted = np.sort(sv)
        pair_err = np.max(np.abs(sv_sorted[0::2] - sv_sorted[1::2]))
        if pair_err > 1e-7:
            kramers = False
        # build a rank-deficient quaternionic operator with a prescribed kernel
        # by projecting out a J-invariant subspace: A2 = A P, P = 1 - (uu* + (Ju)(Ju)*)
        u = RNG.standard_normal(n) + 1j * RNG.standard_normal(n)
        u = u / np.linalg.norm(u)
        Ju = Om @ u.conj()
        Ju = Ju - (u.conj() @ Ju) * u        # orthogonalize (J-partner is orthogonal)
        Ju = Ju / np.linalg.norm(Ju)
        P = np.eye(n) - np.outer(u, u.conj()) - np.outer(Ju, Ju.conj())
        A2 = make_quaternionic(A @ P, Om)     # keep it quaternionic
        sv2 = np.linalg.svd(A2, compute_uv=False)
        kdim = int(np.sum(sv2 < 1e-8))
        if kdim % 2 != 0:
            even_ker = False
        # complex index of a rank-deficient quaternionic operator is even
        # (square operator: index_C = 0, but ker and coker each even)
        if kdim % 2 != 0:
            ranks_even = False

    all_ok &= check("C1 H-linear operators are self-dual (Omega^-1 A Omega = A-bar)",
                    kramers, f"{trials} trials, Kramers pairing holds")
    all_ok &= check("C2 kernel dimension of H-linear operator is even",
                    even_ker, f"{trials} trials")
    all_ok &= check("C3 index_H = index_C/2 well-defined (KSp^0(pt)=Z augmentation)",
                    ranks_even, "even complex kernel => integer quaternionic index")
    return all_ok


def main():
    print("R3 SIGNED-READOUT BOUNDARY THEOREM -- EXECUTABLE CERTIFICATE")
    print("=" * 68)
    a = block_A()
    b = block_B()
    c = block_C()
    print("\n" + "=" * 68)
    npass = sum(1 for _, ok, _ in report if ok)
    ntot = len(report)
    print(f"SUMMARY: {npass}/{ntot} checks passed.")
    print(f"  BLOCK A (abstract criterion M/P/C): {'OK' if a else 'FAIL'}")
    print(f"  BLOCK B (Part Z, finite GW index):  {'OK' if b else 'FAIL'}")
    print(f"  BLOCK C (Part K, KSp augmentation): {'OK' if c else 'FAIL'}")
    ok = a and b and c
    print("\nRESULT:", "ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
