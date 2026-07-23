#!/usr/bin/env python3
"""
WC-ANTILINEAR-BOUND, script 1 of 2: the symmetry-breaking-ladder census of antilinear
operators on the 192-dim generation carrier.

QUESTION.  The located-not-forced paper's caveat (d): its antilinear non-existence leg (no
frame-non-trivial antilinear chiralizer) is a finite adversarial hunt, not a closed proof.
WC-ENUM-COMPLETENESS already closed the FULLY EQUIVARIANT core at computed grade (under
G = so(4) (+) so(5,5), and down to so(5,5) alone, every antilinear intertwiner PRESERVES
chirality; no antilinear re-grading exists).  The residual is the NON-equivariant antilinear
space.  This script delimits that residual by a DECLARED symmetry-breaking ladder and decides
each rung; the companion script antilinear_symmetry_free_bound.py closes the symmetry-free
bottom of the ladder with the index-nullity theorem.

THE SEARCH SPACE S (the delimitation; full statement in canon/antilinear-bound-RESULTS.md).
Antilinear operators C = M . conj on the fixed 192-dim carrier W (the j=1 self-dual triplet
of the gamma-traceless Rarita-Schwinger module of Cl(9,5), split 14 = 4 + 10, frame so(4)
compact, internal so(5,5) split), subject to the ADMISSIBILITY the paper's physical argument
actually uses:
  (A1) carrier-preserving (we work on the compressed carrier; upstairs candidates must have
       zero leakage -- as in the enum census);
  (A2) Krein-compatible (the antiunitary condition, stated correctly for ANTIlinear
       operators): k(Cx, Cy) = lambda conj(k(x, y)) for all x, y, i.e. in matrix form
       M^dag K M = lambda K-bar, lambda real nonzero (lambda = +1: Krein antiunitary;
       lambda = -1: anti-antiunitary; hermiticity forces lambda real; K-bar = conj(K) --
       K is genuinely complex on this carrier, so the conjugate matters).  On this
       carrier A2 IS ghost-grading compatibility: the ghost sector enters the carrier
       kinematics only through the hyperbolic 50/50 Krein pairing
       (canon/ghost-parity-krein-synthesis.md), so respecting the ghost structure = A2;
  (A3) Wigner/Kramers normalization: C^2 = M conj(M) = eps I, eps in {+1,-1} (the paper's
       escape has eps = -1; both signs admitted);
  (A4) CHIRALIZER shape: nonzero chirality-swapping component (P_-/+ M P_+/- != 0) -- the
       AZ-CII-type re-grading direction, the one antilinear shape Theorem 2 leaves open.
FRAME-TRIVIALITY (the paper's criterion, formalized): C is frame-trivial iff C commutes with
every tangent-frame so(4) rotation, i.e. M rho(f)-bar = rho(f) M for all 6 frame generators
(the paper's computed criterion "max ||[J_quat, any tangent-frame rotation]|| = 0.00e+00").
fc(C) := max_f ||M rho(f)-bar - rho(f) M|| is the frame-charge diagnostic; fc = 0 iff
frame-trivial.

THE LADDER (declared rungs; every rung is a genuine Lie subalgebra of the sector's own
g = so(4) (+) so(5,5), real forms as the sector fixes them):
  L0   so(4) (+) so(5,5)      (full; re-verifies the enum-completeness result)
  L2   so(3) (+) so(5,5)      (frame broken to so(3); internal intact)
  L2b  so(5,5) alone          (weakest rung containing the internal algebra)
  L3   so(4) (+) t5_split     (internal broken to its split Cartan; frame intact)
  L4   t2 (+) t5              (Cartan only: compact frame torus + split internal Cartan)
  L1   so(4) (+) so(5,4)      (internal broken to so(9), spacelike direction removed)
  L1b  so(4) (+) so(4,5)      (internal broken to so(9), timelike direction removed)
  L5   so(3) (+) so(5,4)      (BOTH broken: the adversarial rung -- frame-activity possible)
  L6   symmetry-free          (companion script: index-nullity theorem, exact)

MONOTONICITY LEMMA (trivial but load-bearing): h in h' implies Anti_{h'}(W) in Anti_h(W).
So the swap-0 result at L2b (so(5,5) alone) closes EVERY rung whose algebra contains
so(5,5) -- L0, L2, and anything between -- and the census below confirms each directly.

DECISION PER RUNG.  For each rung: compute the FULL antilinear intertwiner space (exhaustive
parametrization: antilinear operators form a vector space; the equivariance condition is
linear in M), split it into chirality-preserving and chirality-swapping parts (Gamma_c
commutes with every rung generator, so the split is rung-stable), and for nonzero swap parts
run the admissibility analysis (A2 + A3 on the swap span, exact structure constants printed)
and the frame-charge computation.  Verdict criteria:
  - swap dim 0                     => no chiralizer shape exists at this rung at all (proof
                                      at computed grade, spectral-gap certified);
  - swap dim > 0, rung contains
    the frame so(4)                => every candidate is frame-trivial BY EQUIVARIANCE
                                      (fc = 0 identically); the paper's frame-non-trivial
                                      escape cannot live here;
  - swap dim > 0, frame broken     => frame-active candidates exist; report admissibility
                                      scalars and frame charges; the index-nullity theorem
                                      (companion script) shows even these force NOTHING.
FAILURE CONDITION (report, do not patch): an admissible frame-non-trivial antilinear
chiralizer that forces a nonzero net physical index.  The companion script proves class S
admits none (net index exactly 0 for every physical subspace under every A2 operator), so
the failure condition can only fire there, not here; this census still reports every
candidate it finds.

METHOD.  Substrate identical to tests/enum-completeness/enum_class_c_generators.py
(Jordan-Wigner Cl(9,5), timelike {4..8}; j=1 Casimir-8 carrier shortcut, certified).
Hom spaces by the generic-element method with hard residual asserts and printed spectral
gaps (exact-in-effect).  Admissibility on each swap span is solved through EXACT structure
constants (the quadratic maps M M-bar and M^dag K M restricted to the span), with exact
pattern certificates where they fire; every witness is verified on the full 192-dim
matrices by hard assert.  Deterministic, numpy-only.

STAGING.  ANTI_STAGE=all (default) runs everything (< 90 s on a normal box).  ANTI_STAGE=1 /
ANTI_STAGE=2 split at the ladder midpoint with an .npz checkpoint (system temp dir), for
sandboxes that cap process lifetime; results are identical per stage mode.
"""
import os
import time
import tempfile
import numpy as np
from itertools import combinations

T0 = time.time()
N, DIM = 14, 128
SEED = 20260702
TIMELIKE = {4, 5, 6, 7, 8}
STAGE = os.environ.get("ANTI_STAGE", "all")
STATE = os.path.join(tempfile.gettempdir(), "antilinear_ladder_state.npz")
np.set_printoptions(precision=4, suppress=True, linewidth=120)
rng = np.random.default_rng(SEED)
NASSERT = 0


def check(cond, msg):
    global NASSERT
    NASSERT += 1
    assert cond, msg


# ------------------------------------------------------------------ substrate (as enum census)
def jw(n):
    I = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    G = []
    for k in range(n):
        L, R = [s3] * k, [I] * (n - 1 - k)
        for mid in (s1, s2):
            o = np.array([[1 + 0j]])
            for m in L + [mid] + R:
                o = np.kron(o, m)
            G.append(o)
    return G


def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec4(i, j):
    M = np.zeros((4, 4), dtype=complex)
    M[i, j] = 1
    M[j, i] = -1
    return M


def clean_spectra(lamA, lamB, tol):
    for d in (np.abs(lamA[:, None] - lamA[None, :]),
              np.abs(lamB[:, None] - lamB[None, :]),
              np.abs(lamA[:, None] - lamB[None, :])):
        if ((d > tol) & (d < 50 * tol)).any():
            return False
    return True


def hom_space(As, Bs, label, tol_match=1e-6, res_tol=1e-6, max_vars=2500):
    """All X with X B_i = A_i X (verified basis); generic-element method as in the enum census."""
    n = As[0].shape[0]
    ok = False
    for attempt in range(12):
        c = rng.uniform(0.5, 1.5, size=len(As)) * rng.choice([-1.0, 1.0], size=len(As))
        A = sum(ci * Ai for ci, Ai in zip(c, As))
        B = sum(ci * Bi for ci, Bi in zip(c, Bs))
        lamA, VA = np.linalg.eig(A)
        lamB, VB = np.linalg.eig(B)
        if not clean_spectra(lamA, lamB, tol_match):
            continue
        diff = np.abs(lamA[:, None] - lamB[None, :])
        ks, ls = np.nonzero(diff < tol_match)
        if len(ks) <= max_vars:
            ok = True
            break
    if not ok:
        raise RuntimeError(f"{label}: no clean generic draw in 12 attempts")
    VAi, VBi = np.linalg.inv(VA), np.linalg.inv(VB)
    if len(ks) == 0:
        print(f"  [{label:36s}] eigenvalue match set EMPTY  =>  dim = 0 (proven by spectra)")
        return []
    nv = len(ks)
    if len(As) > 10:
        pairs = []
        for _ in range(10):
            cc = rng.standard_normal(len(As))
            pairs.append((sum(x * Ai for x, Ai in zip(cc, As)),
                          sum(x * Bi for x, Bi in zip(cc, Bs))))
    else:
        pairs = list(zip(As, Bs))
    Nmat = np.zeros((nv, nv), dtype=complex)
    for Ai, Bi in pairs:
        At, Bt = VAi @ Ai @ VA, VBi @ Bi @ VB
        BBH, AHA = Bt @ Bt.conj().T, At.conj().T @ At
        Ak, Bl = At[np.ix_(ks, ks)], Bt[np.ix_(ls, ls)]
        Nmat += ((ks[:, None] == ks[None, :]) * BBH[np.ix_(ls, ls)].T
                 - Ak * Bl.conj()
                 - Ak.conj().T * Bl.T
                 + (ls[:, None] == ls[None, :]) * AHA[np.ix_(ks, ks)])
    Nmat = 0.5 * (Nmat + Nmat.conj().T)
    wN, UN = np.linalg.eigh(Nmat)
    thr = 1e-8 * max(1.0, wN.max())
    idx = np.nonzero(wN < thr)[0]
    Xs = []
    for i in idx:
        Xt = np.zeros((n, n), dtype=complex)
        Xt[ks, ls] = UN[:, i]
        X = VA @ Xt @ VBi
        Xs.append(X / np.linalg.norm(X))
    worst, vtag = 0.0, "n/a"
    if Xs:
        Xst = np.stack(Xs)
        if len(As) * len(Xs) <= 500:
            vpairs, vtag = list(zip(As, Bs)), "all gens"
        else:
            vpairs = []
            for _ in range(6):
                cc = rng.standard_normal(len(As))
                vpairs.append((sum(x * Ai for x, Ai in zip(cc, As)),
                               sum(x * Bi for x, Bi in zip(cc, Bs))))
            vtag = "6 fresh probe combos"
        for Ai, Bi in vpairs:
            worst = max(worst, float(np.linalg.norm(Xst @ Bi - Ai @ Xst, axis=(1, 2)).max()))
        check(worst < res_tol * max(1.0, float(np.abs(Ai).max())), f"{label}: residual {worst:.2e}")
    lo = wN[len(idx)] if len(idx) < nv else np.inf
    print(f"  [{label:36s}] dim = {len(Xs)}  (matched vars {nv}, next eigenvalue {lo:.2e}, "
          f"max residual [{vtag}] {worst:.2e})")
    return Xs


def build_substrate():
    print("=" * 98)
    print("WC-ANTILINEAR-BOUND ladder census: substrate")
    print("=" * 98)
    base = jw(7)
    e = [(1j * base[a] if a in TIMELIKE else base[a]) for a in range(N)]
    I4, I128 = np.eye(4, dtype=complex), np.eye(DIM, dtype=complex)
    cerr = max(np.max(np.abs(e[a] @ e[b] + e[b] @ e[a]
                             - (2.0 * (-1.0 if a in TIMELIKE else 1.0) if a == b else 0.0) * I128))
               for a in range(N) for b in range(N))
    print(f"[substrate] Cl(9,5) Clifford relations   max err = {cerr:.2e}")
    check(cerr < 1e-12, "Clifford relations")

    SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
    Sig = [sgen(e, a, b) + sgen(e, c, d) for (a, b, c, d) in SD]
    Jk = [np.kron(lvec4(a, b) + lvec4(c, d), I128) + np.kron(I4, S)
          for (a, b, c, d), S in zip(SD, Sig)]
    Cas = -(Jk[0] @ Jk[0] + Jk[1] @ Jk[1] + Jk[2] @ Jk[2])
    Cas = 0.5 * (Cas + Cas.conj().T)
    cw, cV = np.linalg.eigh(Cas)
    top = cw.max()
    mask = np.abs(cw - top) < 1e-6
    W = cV[:, mask]
    gap = top - cw[~mask].max()
    print(f"[carrier]  j=1 Casimir eigenvalue = {top:.6f} (expect 8), dim = {W.shape[1]} "
          f"(expect 192), spectral gap = {gap:.3f}")
    check(abs(top - 8.0) < 1e-9 and W.shape[1] == 192 and gap > 0.5, "carrier")

    Gamma = np.hstack([e[a] for a in range(N)])
    Wfull = np.zeros((N * DIM, 192), dtype=complex)
    Wfull[:4 * DIM, :] = W
    gtr = np.max(np.abs(Gamma @ Wfull))
    print(f"[carrier]  ||Gamma W|| = {gtr:.2e}  (0 => gamma-traceless)")
    check(gtr < 1e-10, "gamma-tracelessness")

    gens512 = {}
    for a, b in combinations(range(4), 2):
        gens512[("f", a, b)] = np.kron(lvec4(a, b), I128) + np.kron(I4, sgen(e, a, b))
    for a, b in combinations(range(4, 14), 2):
        gens512[("i", a, b)] = np.kron(I4, sgen(e, a, b))
    inv_err = max(np.max(np.abs(g @ W - W @ (W.conj().T @ g @ W))) for g in gens512.values())
    print(f"[gens]     max ||(1 - P_W) g W|| = {inv_err:.2e}  (0 => carrier invariant)")
    check(inv_err < 1e-9, "carrier invariance")
    Gt = {k: W.conj().T @ g @ W for k, g in gens512.items()}

    om = I128.copy()
    for a in range(N):
        om = om @ e[a]
    om = om if (np.trace(om @ om) / DIM).real > 0 else (-1j) * om
    Gc = W.conj().T @ np.kron(I4, om) @ W
    Gc = 0.5 * (Gc + Gc.conj().T)
    gev = np.linalg.eigvalsh(Gc)
    check(int((gev > 0.5).sum()) == 96 and int((gev < -0.5).sum()) == 96, "chirality split 96/96")
    comm_err = max(np.max(np.abs(Gc @ g - g @ Gc)) for g in Gt.values())
    print(f"[chirality] split (+96,-96); max ||[Gamma_c, g]|| over all 51 generators = {comm_err:.2e}")
    check(comm_err < 1e-9, "Gamma_c commutes with g (swap/preserve split is rung-stable)")

    spacelike = [a for a in range(N) if a not in TIMELIKE]
    bS = I128.copy()
    for s in spacelike:
        bS = bS @ e[s]
    if np.linalg.norm(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    Kc = W.conj().T @ np.kron(I4, bS) @ W
    Kc = 0.5 * (Kc + Kc.conj().T)
    kev = np.linalg.eigvalsh(Kc)
    ksig = (int((kev > 1e-8).sum()), int((kev < -1e-8).sum()))
    Pp, Pm = (np.eye(192) + Gc) / 2, (np.eye(192) - Gc) / 2
    kpp = np.max(np.abs(Pp @ Kc @ Pp))
    kmm = np.max(np.abs(Pm @ Kc @ Pm))
    print(f"[Krein]    signature (+{ksig[0]},-{ksig[1]}); same-chirality blocks "
          f"(++, --) = ({kpp:.2e}, {kmm:.2e})  (0 => W_+/- are K-Lagrangian)")
    check(ksig == (96, 96), "Krein signature (96,96)")
    check(kpp < 1e-10 and kmm < 1e-10, "K purely cross-chirality (Lagrangian chirality pair)")
    return Gt, Gc, Kc


# ---------------------------------------------------------------- rung machinery + admissibility
def swap_split(M, Gc):
    """Preserve/swap components of the antilinear generator M (C = M . conj):
    preserve <=> M Gc-bar = Gc M; swap <=> M Gc-bar = -Gc M."""
    Gcc = Gc.conj()
    return 0.5 * (M + Gc @ M @ Gcc), 0.5 * (M - Gc @ M @ Gcc)


def frame_charge(M, FRAME):
    """fc(C) = max_f ||M rho(f)-bar - rho(f) M|| over the 6 tangent-frame so(4) generators
    (0 <=> frame-trivial, the paper's criterion); plus the plain-commutator diagnostic."""
    fc = max(np.linalg.norm(M @ f.conj() - f @ M) for f in FRAME)
    cc = max(np.linalg.norm(M @ f - f @ M) for f in FRAME)
    return fc, cc


def gram_schmidt(mats):
    out = []
    for m in mats:
        r = m.copy()
        for b in out:
            r = r - np.vdot(b, r) * b
        n = np.linalg.norm(r)
        if n > 1e-7:
            out.append(r / n)
    return out


def scalar_part(X, T):
    s = np.vdot(T, X) / np.vdot(T, T)
    return s, float(np.linalg.norm(X - s * T))


def quad_structure(Ss, pair, target, tname):
    """Structure constants of the quadratic map q(c) = sum_ij c_i conj(c_j) pair(S_i,S_j),
    decomposed as (target-component form t0[ij]) + (orthogonal components e_a[ij] over an
    orthonormal basis E_a of span{pair(S_i,S_j) - t0_ij target})."""
    nU = len(Ss)
    Tn2 = np.vdot(target, target)
    t0 = np.zeros((nU, nU), dtype=complex)
    perp = {}
    for i in range(nU):
        for j in range(nU):
            T = pair(Ss[i], Ss[j])
            co = np.vdot(target, T) / Tn2
            t0[i, j] = co
            perp[(i, j)] = T - co * target
    Eb = gram_schmidt([perp[(i, j)] for i in range(nU) for j in range(nU)])
    ems = [np.array([[np.vdot(E, perp[(i, j)]) for j in range(nU)] for i in range(nU)])
           for E in Eb]
    scale = max(max(np.linalg.norm(perp[k]) for k in perp), float(np.linalg.norm(t0)), 1e-30)
    print(f"    {tname}: target-component form ||t0|| = {np.linalg.norm(t0):.3e}, "
          f"off-target span dim = {len(ems)}")
    return t0, ems, scale


def form_value(c, f):
    return complex(np.tensordot(np.outer(c, c.conj()), f, axes=2))


def definite_certificate(ems, tag):
    for a, f in enumerate(ems):
        if np.linalg.norm(f - f.conj().T) < 1e-9 * max(1.0, np.linalg.norm(f)):
            ev = np.linalg.eigvalsh(0.5 * (f + f.conj().T))
            if ev.min() > 1e-9 or ev.max() < -1e-9:
                print(f"    EXACT CERTIFICATE ({tag}): Hermitian off-target constraint form "
                      f"#{a} is definite -- satisfied only at c = 0.  Proof on the whole span.")
                return True
    return False


def admissibility_on_swap_span(Ss, Gc, Kc, FRAME, label):
    """Exhaustive A2+A3 analysis on the swap span {M(c) = sum c_i S_i}, via exact structure
    constants (no Schur-scalar assumption; valid at every rung).

    A3 (C^2 = eps I): M M-bar = sum_ij c_i conj(c_j) T_ij, T_ij = S_i conj(S_j).  Decompose
    against the target I: A3 <=> t0-form(c) = eps AND every off-I component form = 0.
    A2 (M^dag K M = lambda K): F_ij = S_i^dag K S_j, decomposed against the target K:
    A2 <=> k0-form(c) = lambda real nonzero AND every off-K component form = 0.

    EXACT certificates (each, when it fires, is a PROOF on the whole span, not a search):
      (C1) t0 = 0 identically: tr(C^2) = 0 for every element, so C^2 = eps I never holds;
      (C2) a Hermitian off-I constraint form is definite: no nonzero c satisfies A3;
      (C3) k0 = 0 identically: every swap combination is K-null -- no Krein-conformal (A2)
           antilinear swap exists in the rung-equivariant span at all;
      (C4) a Hermitian off-K constraint form is definite: same conclusion as (C3);
      (C5) [1/1 channel closed form] if the up/down channel dims are 1/1 the whole system
           is solved in closed form: with U D-bar = gU P+ + (verified 0) and D U-bar =
           gD P-, A3 is solvable iff gD = conj(gU) != 0 (z = a conj(b) = eps/gU forced);
           the remaining A2 system is LINEAR in (|a|^2, |b|^2) and decided exactly.
    Otherwise: deterministic multistart Gauss-Newton on the exact structure-constant
    system (search-grade when it finds nothing); every witness is re-verified on the full
    192-dim matrices by hard assert.  Class-S admissibility needs lambda real nonzero
    (Krein-conformal); the STRICT paper normalization wants |lambda|/|eps| = 1
    (scale-invariant ratio printed)."""
    nU = len(Ss)
    Pp, Pm = (np.eye(192) + Gc) / 2, (np.eye(192) - Gc) / 2
    # up/down channel split (both components are themselves rung-equivariant since
    # Gamma_c commutes with the rung action)
    ups = gram_schmidt([Pp @ S for S in Ss if np.linalg.norm(Pp @ S) > 1e-7])
    dns = gram_schmidt([Pm @ S for S in Ss if np.linalg.norm(Pm @ S) > 1e-7])
    print(f"\n  admissibility analysis on the swap span at {label} "
          f"(dim {nU}; channels: up {len(ups)}, down {len(dns)}):")
    check(len(ups) + len(dns) == 2 * nU or len(ups) + len(dns) == nU,
          f"{label}: channel split dims (up {len(ups)} + down {len(dns)} vs span {nU})")
    Sb = ups + dns                                  # channel-adapted basis of the same span
    nB = len(Sb)
    I192 = np.eye(192, dtype=complex)
    Kb = Kc.conj()
    t0, emsT, scT = quad_structure(Sb, lambda X, Y: X @ Y.conj(), I192, "A3 vs I")
    k0, emsK, scK = quad_structure(Sb, lambda X, Y: X.conj().T @ Kc @ Y, Kb, "A2 vs K-bar")
    check(np.max(np.abs(k0 - k0.conj().T)) < 1e-8 * max(1.0, np.linalg.norm(k0)),
          f"{label}: K-component form Hermitian (lambda auto-real)")

    # ---- exact certificates
    if np.linalg.norm(t0) < 1e-9 * scT:
        print("    EXACT CERTIFICATE (C1): tr(C^2) = 0 identically on the span, so")
        print("    C^2 = eps I has no solution.  A3 fails on the whole span -- proof.")
        return "NON-EXISTENCE (C1: C^2 traceless on the whole span)"
    if definite_certificate(emsT, "C2"):
        return "NON-EXISTENCE (C2: definite off-I constraint)"
    if np.linalg.norm(k0) < 1e-9 * scK:
        print("    EXACT CERTIFICATE (C3): <K-bar, M^dag K M> = 0 identically: every swap")
        print("    combination is K-NULL -- no Krein-conformal (A2) antilinear swap exists")
        print("    in the rung-equivariant span at all.  Proof, not search.")
        return "NON-EXISTENCE (C3: all equivariant swaps K-null)"
    if definite_certificate(emsK, "C4"):
        return "NON-EXISTENCE (C4: definite off-K constraint)"

    # ---- C5: 1/1-channel closed form
    if len(ups) == 1 and len(dns) == 1:
        U, D = ups[0], dns[0]
        UD = U @ D.conj()
        gU, rU = scalar_part(UD, Pp)
        DU = D @ U.conj()
        gD, rD = scalar_part(DU, Pm)
        # sanity: U U-bar and D D-bar vanish identically (channel mismatch)
        check(np.linalg.norm(U @ U.conj()) < 1e-9 and np.linalg.norm(D @ D.conj()) < 1e-9,
              f"{label}: pure channels satisfy U U-bar = D D-bar = 0")
        print(f"    C5 closed form: U D-bar = ({gU:+.4e}) P+ (residual {rU:.2e}), "
              f"D U-bar = ({gD:+.4e}) P- (residual {rD:.2e})")
        check(rU < 1e-7 and rD < 1e-7, f"{label}: C5 Schur scalars on irreducible blocks")
        if abs(gU) < 1e-10 or abs(gD) < 1e-10:
            print("    EXACT CERTIFICATE (C5a): a channel product vanishes: C^2 = eps I")
            print("    has no solution on the span.  Proof.")
            return "NON-EXISTENCE (C5a: channel product zero)"
        if abs(gD - np.conj(gU)) > 1e-8 * abs(gU):
            print(f"    EXACT CERTIFICATE (C5b): A3 forces z gU = eps AND conj(z) gD = eps,")
            print(f"    i.e. gD = conj(gU); computed gD - conj(gU) = "
                  f"{abs(gD - np.conj(gU)):.3e} != 0.  C^2 = eps I has NO solution on the")
            print("    span (any eps, any scaling).  Proof, not search.")
            return "NON-EXISTENCE (C5b: Kramers phase obstruction gD != conj(gU))"
        # A3 solvable: z = a conj(b) = eps/gU.  Decide A2 exactly on the family.
        print("    C5: A3 IS solvable (gD = conj(gU)); deciding A2 on the A3 family exactly")
        for eps in (-1.0, 1.0):
            z = eps / gU
            # M = a U + b D, a conj(b) = z; unknowns u = |a|^2 > 0, v = |b|^2 > 0, uv = |z|^2
            FUU = U.conj().T @ Kc @ U
            FDD = D.conj().T @ Kc @ D
            FUD = U.conj().T @ Kc @ D
            FDU = D.conj().T @ Kc @ U
            fixed = np.conj(z) * FUD + z * FDU
            # off-K-bar components must vanish: u*FUU_perp + v*FDD_perp + fixed_perp = 0
            Kn2 = np.vdot(Kb, Kb)
            pK = lambda X: X - (np.vdot(Kb, X) / Kn2) * Kb
            A = np.stack([pK(FUU).ravel(), pK(FDD).ravel()], axis=1)
            rhs = -pK(fixed).ravel()
            sol, res2, rank, _ = np.linalg.lstsq(A, rhs, rcond=None)
            resid = np.linalg.norm(A @ sol - rhs)
            u, v = sol.real
            lam = ((u * np.vdot(Kb, FUU) + v * np.vdot(Kb, FDD) + np.vdot(Kb, fixed)) / Kn2).real
            print(f"      eps = {eps:+.0f}: linear A2 system rank {rank}, residual {resid:.2e}, "
                  f"(u,v) = ({u:+.3e},{v:+.3e}), uv - |z|^2 = {u * v - abs(z) ** 2:+.3e}, "
                  f"lambda = {lam:+.3e}")
            if resid < 1e-8 and u > 1e-12 and v > 1e-12 and abs(u * v - abs(z) ** 2) < 1e-8 and abs(lam) > 1e-9:
                a = np.sqrt(u)
                b = np.conj(z) / a
                M = a * U + b * D
                return verify_witness(M, eps, Gc, Kc, FRAME, label)
        print("    EXACT CERTIFICATE (C5c): the A2 linear system is infeasible on the A3")
        print("    family (or forces u,v <= 0 / uv != |z|^2 / lambda = 0) for both eps.")
        print("    No admissible swap exists on the span.  Proof (linear algebra), not search.")
        return "NON-EXISTENCE (C5c: A2 infeasible on the A3 family)"

    # ---- general case: deterministic multistart Gauss-Newton on the exact system
    def residual(c, eps):
        out = []
        h = form_value(c, t0) - eps
        out += [h.real, h.imag]
        for f in emsT:
            v = form_value(c, f)
            out += [v.real, v.imag]
        for f in emsK:
            v = form_value(c, f)
            out += [v.real, v.imag]
        return np.array(out)

    found = []
    for eps in (-1.0, 1.0):
        for start in range(60):
            c = rng.standard_normal(nB) + 1j * rng.standard_normal(nB)
            for it in range(80):
                r = residual(c, eps)
                if np.linalg.norm(r) < 1e-12:
                    break
                x = np.concatenate([c.real, c.imag])
                J = np.zeros((len(r), 2 * nB))
                h = 1e-7
                for k in range(2 * nB):
                    xp = x.copy()
                    xp[k] += h
                    cp = xp[:nB] + 1j * xp[nB:]
                    J[:, k] = (residual(cp, eps) - r) / h
                dx, *_ = np.linalg.lstsq(J, -r, rcond=None)
                x = x + dx
                c = x[:nB] + 1j * x[nB:]
            if np.linalg.norm(residual(c, eps)) < 1e-10:
                lam = form_value(c, k0).real
                if abs(lam) > 1e-9:
                    M = sum(ci * Si for ci, Si in zip(c, Sb))
                    return verify_witness(M, eps, Gc, Kc, FRAME, label)
    print("    no admissible (A2+A3) combination found (deterministic 120-start Gauss-")
    print("    Newton on the exact structure-constant system).  SEARCH-GRADE evidence")
    print("    only; the rung is closed by the index-nullity theorem regardless.")
    return "NOT-FOUND (search-grade)"


def verify_witness(M, eps, Gc, Kc, FRAME, label):
    """Hard-assert verification of an admissibility witness on the full 192-dim matrices."""
    MMb = M @ M.conj()
    rI = np.linalg.norm(MMb - eps * np.eye(192))
    Kb = Kc.conj()
    KM = M.conj().T @ Kc @ M
    lam = (np.vdot(Kb, KM) / np.vdot(Kb, Kb)).real
    rK = np.linalg.norm(KM - lam * Kb) / np.linalg.norm(Kb)
    check(rI < 1e-8, f"{label}: witness C^2 = eps I on full matrices (residual {rI:.2e})")
    check(rK < 1e-8, f"{label}: witness M^dag K M = lambda K on full matrices (residual {rK:.2e})")
    sw = np.linalg.norm(Gc @ M + M @ Gc.conj())
    check(sw < 1e-7 * np.linalg.norm(M), f"{label}: witness is a pure chirality swap")
    fc, cc = frame_charge(M / np.linalg.norm(M) * np.sqrt(192), FRAME)
    strict = abs(abs(lam) - 1.0) < 1e-9
    print(f"    ADMISSIBLE SWAP WITNESS: C^2 = {eps:+.0f} I (residual {rI:.2e}), "
          f"M^dag K M = ({lam:+.4f}) K-bar (residual {rK:.2e})")
    print(f"      scale-invariant |lambda|/|eps| = {abs(lam):.4f} "
          f"({'STRICT +-1 normalization attainable' if strict else 'conformal class S; strict +-1 needs |lambda|=1'})")
    print(f"      frame charge fc = {fc:.2e} (plain commutator {cc:.2e})")
    return f"EXISTS (C^2 = {eps:+.0f}, lambda = {lam:+.3f}, fc = {fc:.1e})"


RUNG_DEFS = [
    # (label, frame_part, internal_part) resolved against Gt at runtime
    ("L0   so(4)+so(5,5)  [full equivariance]", "so4", "so55"),
    ("L2   so(3)+so(5,5)  [frame broken]", "so3", "so55"),
    ("L2b  so(5,5) alone  [weakest internal-full]", None, "so55"),
    ("L3   so(4)+t5split  [internal -> split Cartan]", "so4", "t5"),
    ("L4   t2+t5 Cartan-only", "t2", "t5"),
    ("L1   so(4)+so(5,4)  [drop spacelike 13]", "so4", "so9s"),
    ("L1b  so(4)+so(4,5)  [drop timelike 8]", "so4", "so9t"),
    ("L5   so(3)+so(5,4)  [BOTH broken: adversarial]", "so3", "so9s"),
]
STAGE1_RUNGS = {"L0", "L2", "L2b", "L3"}


def rung_generators(Gt, fpart, ipart):
    F = {
        "so4": [Gt[("f", a, b)] for a, b in combinations(range(4), 2)],
        "so3": [Gt[("f", a, b)] for a, b in [(0, 1), (0, 2), (1, 2)]],
        "t2": [Gt[("f", 0, 1)], Gt[("f", 2, 3)]],
        None: [],
    }[fpart]
    I = {
        "so55": [Gt[("i", a, b)] for a, b in combinations(range(4, 14), 2)],
        "so9s": [Gt[("i", a, b)] for a, b in combinations(range(4, 14), 2) if 13 not in (a, b)],
        "so9t": [Gt[("i", a, b)] for a, b in combinations(range(4, 14), 2) if 8 not in (a, b)],
        "t5": [Gt[("i", a, b)] for a, b in [(4, 9), (5, 10), (6, 11), (7, 12), (8, 13)]],
    }[ipart]
    return F + I


def run_rung(label, gens, Gc, Kc, FRAME):
    print(f"\n----- rung {label} ({len(gens)} generators) -----")
    anti = hom_space(gens, [g.conj() for g in gens], f"{label.split()[0]}: antilinear intertwiners")
    pres_parts, swap_parts = [], []
    for M in anti:
        Mp, Ms = swap_split(M, Gc)
        if np.linalg.norm(Mp) > 1e-7:
            pres_parts.append(Mp)
        if np.linalg.norm(Ms) > 1e-7:
            swap_parts.append(Ms)
    pres_basis = gram_schmidt(pres_parts)
    swap_basis = gram_schmidt(swap_parts)
    check(len(pres_basis) + len(swap_basis) == len(anti),
          f"{label}: preserve/swap split must exhaust the space "
          f"({len(pres_basis)}+{len(swap_basis)} != {len(anti)})")
    print(f"  chirality split of the antilinear space: preserve dim = {len(pres_basis)}, "
          f"SWAP dim = {len(swap_basis)}")
    fc_max = 0.0
    if len(swap_basis) == 0:
        verdict = "NO chiralizer shape exists (swap dim 0) -- computed-grade proof"
        print(f"  => {verdict}")
    else:
        for i, S in enumerate(swap_basis):
            Sn = S / np.linalg.norm(S) * np.sqrt(192)
            fc, cc = frame_charge(Sn, FRAME)
            fc_max = max(fc_max, fc)
            print(f"    swap generator #{i}: frame charge fc = {fc:.2e} "
                  f"(plain commutator {cc:.2e})")
        contains_frame = len([g for g in gens if any(np.linalg.norm(f - g) < 1e-12 for f in FRAME)]) == 6
        if contains_frame:
            check(fc_max < 1e-6, f"{label}: rung contains so(4) => swaps must be frame-trivial")
            print("  => swap candidates EXIST but are ALL FRAME-TRIVIAL (forced by the rung's own")
            print("     so(4)-equivariance).  The paper's frame-non-trivial escape cannot live here.")
            verdict = "swaps exist, ALL frame-trivial by equivariance"
        else:
            print("  => frame-ACTIVE swap candidates exist at this rung (frame broken).")
            verdict = "frame-active swaps exist -- closed by the index-nullity theorem"
        res = admissibility_on_swap_span(swap_basis, Gc, Kc, FRAME, label.split()[0])
        verdict += f"; admissibility: {res}"
    return (label, len(anti), len(pres_basis), len(swap_basis), fc_max, verdict)


# ------------------------------------------------------------------------------ staged driver
summary = []
if STAGE in ("all", "1"):
    Gt, Gc, Kc = build_substrate()
    FRAME = [Gt[("f", a, b)] for a, b in combinations(range(4), 2)]
    print("\n" + "=" * 98)
    print("THE LADDER (antilinear intertwiner census; C = M . conj, condition M g-bar = g M)")
    print("=" * 98)
    print("  monotonicity lemma: h in h' => Anti_{h'}(W) in Anti_h(W).  Swap-0 at L2b closes")
    print("  every rung containing so(5,5); each rung is also verified directly below.")
    for label, fp, ip in RUNG_DEFS:
        if label.split()[0] in STAGE1_RUNGS:
            summary.append(run_rung(label, rung_generators(Gt, fp, ip), Gc, Kc, FRAME))
    if STAGE == "1":
        np.savez(STATE,
                 Gtk=np.array([",".join(map(str, k)) for k in Gt]),
                 Gtv=np.stack([Gt[k] for k in Gt]), Gc=Gc, Kc=Kc,
                 summary=np.array([" | ".join(map(str, row)) for row in summary]))
        print(f"\n[stage 1 complete in {time.time() - T0:.1f}s; state saved; asserts so far: {NASSERT}]")
        raise SystemExit(0)

if STAGE == "2":
    st = np.load(STATE, allow_pickle=True)
    keys = [tuple(s.split(",")) for s in st["Gtk"]]
    keys = [(k[0], int(k[1]), int(k[2])) for k in keys]
    Gt = {k: st["Gtv"][i] for i, k in enumerate(keys)}
    Gc, Kc = st["Gc"], st["Kc"]
    FRAME = [Gt[("f", a, b)] for a, b in combinations(range(4), 2)]
    summary = [tuple(s.split(" | ")) for s in st["summary"]]
    print(f"[stage 2] state loaded from {STATE}")

if STAGE in ("all", "2"):
    for label, fp, ip in RUNG_DEFS:
        if label.split()[0] not in STAGE1_RUNGS:
            summary.append(run_rung(label, rung_generators(Gt, fp, ip), Gc, Kc, FRAME))

    # ------------------------------------------------------------------------------- verdict
    print("\n" + "#" * 98)
    print("# LADDER CENSUS -- VERDICT")
    print("#" * 98)
    print(f"\n  {'rung':46s} {'anti':>5s} {'pres':>5s} {'swap':>5s} {'max fc':>9s}   verdict")
    for row in summary:
        label, na, npres, nswap, fc, verdict = row
        print(f"  {str(label):46s} {int(na):5d} {int(npres):5d} {int(nswap):5d} "
              f"{float(fc):9.2e}   {verdict}")
    print("""
  Reading (full statement in canon/antilinear-bound-RESULTS.md):
  - Every rung whose algebra contains the internal so(5,5) has swap dim 0: the chiralizer
    SHAPE does not exist there at all (confirms + extends the enum-completeness result).
  - Breaking the internal algebra to its split Cartan (L3, L4) STILL gives swap dim 0:
    conjugation preserves split (real) weights, so antilinear intertwiners cannot reach the
    opposite half-spinor.  The chiralizer shape needs the internal algebra broken to a
    subalgebra with self-associate half-spinors (the so(9) forms: L1, L1b, L5).
  - Where the swap shape exists with the frame so(4) intact (L1, L1b), every candidate is
    frame-trivial BY EQUIVARIANCE: the frame-non-trivial escape is structurally excluded.
  - Only the both-broken rung L5 (and below, down to symmetry-free) admits frame-active swap
    candidates.  For every rung the companion script proves the index-nullity theorem: NO
    Krein-compatible antilinear operator (M^dag K M = lambda K-bar) -- equivariant or not,
    frame-trivial or not -- moves the net chiral index of any physical subspace off 0.  The
    chiralizer escape is closed at every rung of the declared ladder.
""")
    print(f"  hard asserts passed: {NASSERT}")
    print(f"  total runtime this stage: {time.time() - T0:.1f}s")
# EOF
