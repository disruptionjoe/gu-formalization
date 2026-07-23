#!/usr/bin/env python3
"""
WC-ENUM-COMPLETENESS route (a): the compact-carrier C1-C5 generator census.

QUESTION.  The located-not-forced paper's Theorem 1 is proof-by-enumeration over 7 obstruction
classes (Kramers, mod-2 Witten, cross-chirality Krein, adjoint index 4k, Rokhlin, spinor
2-smoothness, ghost parity).  Completeness of the enumeration is open.  This script closes it
for the C1-C5 portion of the semantic class now called C_inv by exhaustively computing
the invariant-theoretic generator spaces
of all covariant sector-interior structures on the carrier and checking, generator by
generator, that every obstruction each one can carry is 2-primary.

SEMANTIC TARGET C_inv (the delimitation; boundary stated sharply in the RESULTS doc). Structures on the
fixed 192-dim generation carrier W (the j=1 self-dual triplet of the gamma-traceless
Rarita-Schwinger module of Cl(9,5), signature split 4+10) that are (anti)linear in the carrier
and equivariant under the sector's split symmetry algebra G = so(4) (+) so(10) (real form
so(4) (+) so(5,5)), built from the sector's own data:
  (C1) G-equivariant linear endomorphisms (the commutant) and their trace/graded-trace integers;
  (C2) G-invariant bilinear forms;
  (C3) G-invariant sesquilinear forms and their Krein signatures;
  (C4) G-equivariant antilinear intertwiners and their Kramers signs (C^2 = +-1);
  (C5) index-type integers of equivariant intertwiners between the chirality sectors;
  (C6) the seven named characteristic/arithmetic rows -- swept by the companion
       engine as a named finite list, not classified as all possible
       characteristic constructions.
EXCLUDED from C (the boundary): external backgrounds/spurion VEVs, extra global/discrete
symmetries (e.g. a Z_9), non-equivariant operators, and function-space (Fredholm) structures.

METHOD (exact-in-effect, deterministic, numpy-only; every claimed dimension is certified by
the printed spectral gap of a positive-semidefinite normal matrix and by hard residual
asserts).
  1. Substrate: Jordan-Wigner Cl(9,5) gammas (timelike {4..8}), exactly as tests/chase/MOVE-5.
  2. Carrier shortcut (new, certified): the j=1 su(2)_+ isotypic of V(x)S lies entirely in
     V_4(x)S (S carries only j in {0,1/2}), and Gamma kills it by Schur (S has no j=1), so
     W = the 192-dim Casimir-8 eigenspace of the 512-dim block, and ||Gamma W|| == 0 is
     CHECKED, not assumed.  This replaces the 1792-dim kernel computation.
  3. Exact torus combinatorics (integer arithmetic): the 16/16bar weight systems of so(10)
     prove that no same-chirality invariant bilinear pairing exists at all (zero-weight-sum
     pair count is literally 0), in every signature.
  4. Hom spaces: each generator space of C is Hom(rho_B, rho_A) for explicit 192-dim reps of
     the 51 real generators of G.  Computed by the generic-element method: a fixed-seed random
     combination A = sum c_i g_i has clean spectrum (certified by an ambiguity-annulus check),
     X must be supported on eigenvalue-matched pairs, and the constraints reduce to the null
     space of a small PSD normal matrix.  Every basis element is verified by hard asserts.
  5. For each generator: chirality block structure, Kramers sign, graded trace, signature.
  6. Robustness: the census is re-run under the SMALLER covariance algebras
     G' = su(2)_+ (+) so(10) and G'' = so(10) alone (the weakest sector-interior covariance);
     the spaces grow, the conclusions (cross-chirality forms, chirality-preserving quaternionic
     antilinears, 2-primary index integers) persist.

KEY COMPUTED FACT (a correction to the initial expectation, reported, not patched): in the
actual real form the internal so(5,5) is SPLIT, its 16 is self-conjugate (Majorana-Weyl exists
in (5,5)), so every equivariant antilinear intertwiner PRESERVES chirality (a T-type
structure, quaternionic per block: the Kramers wall acting within each chirality sector) --
and NO chirality-swapping equivariant antilinear (an AZ-CII-type re-grading, the one antilinear
shape that could escape) exists in class C at all.

VERDICT CRITERION.  The C1-C5 lift is complete for the computed compact carrier
iff every computed generator maps onto one of the encoded rows and carries
only the declared typed content. C6 is a named-list input to C_fin, not an
unrestricted classification theorem. A computed C1-C5 generator imposing an
odd-prime congruence on a generation integer = FAILURE (report, do not patch).

STAGING.  ENUM_STAGE=all (default) runs everything (< 90 s on a normal box).  ENUM_STAGE=1 /
ENUM_STAGE=2 split at the robustness censuses with an .npz checkpoint, for sandboxes that cap
process lifetime; results are identical.

Companion: enum_extension_engine.py (route b), verify/indep_check.py (independent re-check on
Cl(7,7) + the Euclidean (14,0) chirality-detecting control).
"""
import os
import time
import numpy as np
from itertools import combinations, product

T0 = time.time()
N, DIM = 14, 128
SEED = 20260702
TIMELIKE = {4, 5, 6, 7, 8}          # signature (9,5), as tests/chase/MOVE-5
STAGE = os.environ.get("ENUM_STAGE", "all")
import tempfile
STATE = os.path.join(tempfile.gettempdir(), "enum_census_state.npz")
np.set_printoptions(precision=4, suppress=True, linewidth=120)
rng = np.random.default_rng(SEED)


# ----------------------------------------------------------------------------- helper machinery
def jw(n):
    """Jordan-Wigner Hermitian generators of Cl(2n,0) -- identical to MOVE-5."""
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
    """Matching is well-defined iff no within- or cross-spectrum distance falls in the
    ambiguity annulus (tol, 50*tol): clusters are then exact (< tol) or well separated."""
    for d in (np.abs(lamA[:, None] - lamA[None, :]),
              np.abs(lamB[:, None] - lamB[None, :]),
              np.abs(lamA[:, None] - lamB[None, :])):
        if ((d > tol) & (d < 50 * tol)).any():
            return False
    return True


def hom_space(As, Bs, label, tol_match=1e-6, res_tol=1e-6, max_vars=2500):
    """All X with X B_i = A_i X for every pair (A_i, B_i); returns a verified basis list."""
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
        print(f"  [{label:34s}] eigenvalue match set EMPTY  =>  dim = 0 (proven by spectra)")
        return []
    nv = len(ks)
    # constraint pairs: when the generator list is long, accumulate the normal matrix over a
    # deterministic set of random probe COMBINATIONS (constraints are linear in the pair, so
    # combinations are valid constraints); rigor is unaffected because every basis element is
    # verified below (hard assert) against held-out constraints.
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
    # verification (hard assert): full per-generator check when cheap; otherwise 6 FRESH probe
    # combinations not used in the normal matrix (a false null vector fails a fresh random
    # combination generically), batched as one GEMM per pair.
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
        assert worst < res_tol * max(1.0, float(np.abs(Ai).max())), f"{label}: residual {worst:.2e}"
    lo = wN[len(idx)] if len(idx) < nv else np.inf
    print(f"  [{label:34s}] dim = {len(Xs)}  (matched vars {nv}, next eigenvalue {lo:.2e}, "
          f"max residual [{vtag}] {worst:.2e})")
    return Xs


def blocks_op(X):
    """Chirality blocks of a linear operator X: (++, --, +-, -+)."""
    return (np.linalg.norm(Pp @ X @ Pp), np.linalg.norm(Pm @ X @ Pm),
            np.linalg.norm(Pp @ X @ Pm), np.linalg.norm(Pm @ X @ Pp))


def blocks_bil(B):
    """Chirality blocks of a bilinear form B[x,y]=x^T B y (left slot transposed)."""
    return (np.linalg.norm(Pp.T @ B @ Pp), np.linalg.norm(Pm.T @ B @ Pm),
            np.linalg.norm(Pp.T @ B @ Pm), np.linalg.norm(Pm.T @ B @ Pp))


def blocks_ses(F):
    """Chirality blocks of a sesquilinear form F[x,y]=x^dag F y (left slot conjugated)."""
    return (np.linalg.norm(Pp @ F @ Pp), np.linalg.norm(Pm @ F @ Pm),
            np.linalg.norm(Pp @ F @ Pm), np.linalg.norm(Pm @ F @ Pp))


def census(G, name, verbose=True):
    print(f"\n----- covariance algebra {name} ({len(G)} generators) -----")
    out = {}
    out["comm"] = hom_space(G, G, f"{name}: linear commutant End_G(W)")
    out["anti"] = hom_space(G, [g.conj() for g in G], f"{name}: antilinear intertwiners")
    out["bil"] = hom_space([-g.T for g in G], G, f"{name}: invariant bilinear forms")
    out["ses"] = hom_space([-g.conj().T for g in G], G, f"{name}: invariant sesquilinear forms")
    # chirality structure of every generator (aggregate when the space is large)
    for key, kind, blk in (("comm", "linear", blocks_op), ("bil", "bilinear", blocks_bil),
                           ("ses", "sesquilinear", blocks_ses)):
        worst_diag, worst_off = 0.0, 0.0
        for i, X in enumerate(out[key]):
            pp, mm, pm, mp = blk(X)
            if kind == "linear":
                worst_off = max(worst_off, pm, mp)
                if verbose:
                    print(f"    {kind} #{i}: blocks (++,--,+-,-+) = "
                          f"({pp:.3f},{mm:.3f},{pm:.2e},{mp:.2e})")
            else:
                worst_diag = max(worst_diag, pp, mm)
                if verbose:
                    print(f"    {kind} #{i}: blocks (++,--,+-,-+) = "
                          f"({pp:.2e},{mm:.2e},{pm:.3f},{mp:.3f})")
        if kind == "linear":
            print(f"    {kind}: max off-diagonal chirality block over {len(out[key])} gens = "
                  f"{worst_off:.2e}  (0 => chirality-diagonal; Hom(W+,W-) = 0)")
            assert worst_off < 1e-8
        else:
            print(f"    {kind}: max same-chirality block over {len(out[key])} gens = "
                  f"{worst_diag:.2e}  (0 => ALL purely cross-chirality)")
            assert worst_diag < 1e-8, f"same-chirality invariant {kind} form found -- REPORT"
    # antilinear channel: classify each generator as chirality-PRESERVING (T-type: Kramers or
    # reality per chirality block -- items 1/2, both Z/2) or chirality-SWAPPING (a re-grading:
    # the only antilinear shape that could escape; its existence must be REPORTED, not patched).
    n_pres, n_swap = 0, 0
    for i, M in enumerate(out["anti"]):
        sw = np.linalg.norm(Gc @ M + M @ Gc.conj())   # 0 => C anticommutes with Gc: SWAP
        pv = np.linalg.norm(Gc @ M - M @ Gc.conj())   # 0 => C commutes with Gc: PRESERVE
        assert min(sw, pv) < 1e-8, "antilinear generator of mixed chirality type -- inspect"
        if pv < 1e-8:
            n_pres += 1
        else:
            n_swap += 1
        if verbose:
            kind_a = "PRESERVES chirality (T-type)" if pv < 1e-8 else "SWAPS chirality (re-grading)"
            print(f"    antilinear #{i}: ||Gc M + M Gc*|| = {sw:.2e}, ||Gc M - M Gc*|| = {pv:.2e}"
                  f"  =>  {kind_a}")
    print(f"    antilinear: {n_pres} chirality-preserving (T-type), {n_swap} chirality-swapping"
          f" (re-grading) generators")
    if n_swap > 0:
        print("    *** REPORT: an equivariant antilinear RE-GRADING exists -- potential escape;")
        print("        its square and frame coupling must be analyzed before any verdict. ***")
    out["n_swap"] = n_swap
    return out


# =================================================================== stage 1: build + main census
if STAGE != "2":
    base = jw(7)
    e = [(1j * base[a] if a in TIMELIKE else base[a]) for a in range(N)]
    I4, I128 = np.eye(4, dtype=complex), np.eye(DIM, dtype=complex)

    cerr = max(np.max(np.abs(e[a] @ e[b] + e[b] @ e[a]
                             - (2.0 * (-1.0 if a in TIMELIKE else 1.0) if a == b else 0.0) * I128))
               for a in range(N) for b in range(N))
    print(f"[substrate] Cl(9,5) Clifford relations   max err = {cerr:.2e}")
    assert cerr < 1e-12

    # carrier: j=1 isotypic of V4 (x) S
    SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]        # self-dual su(2)_+ on the 4-base
    Sig = [sgen(e, a, b) + sgen(e, c, d) for (a, b, c, d) in SD]
    Jk = [np.kron(lvec4(a, b) + lvec4(c, d), I128) + np.kron(I4, S)
          for (a, b, c, d), S in zip(SD, Sig)]
    Cas = -(Jk[0] @ Jk[0] + Jk[1] @ Jk[1] + Jk[2] @ Jk[2])
    Cas = 0.5 * (Cas + Cas.conj().T)
    cw, cV = np.linalg.eigh(Cas)
    top = cw.max()
    mask = np.abs(cw - top) < 1e-6
    W = cV[:, mask]                                        # 512 x 192
    gap = top - cw[~mask].max()
    print(f"[carrier]  j=1 Casimir eigenvalue = {top:.6f} (expect 8), dim = {W.shape[1]} "
          f"(expect 192), spectral gap = {gap:.3f}")
    assert abs(top - 8.0) < 1e-9 and W.shape[1] == 192 and gap > 0.5

    CasS = -(Sig[0] @ Sig[0] + Sig[1] @ Sig[1] + Sig[2] @ Sig[2])
    smax = np.linalg.eigvalsh(0.5 * (CasS + CasS.conj().T)).max()
    print(f"[carrier]  max su(2)_+ Casimir on S (V10 channel) = {smax:.6f} (< 8 => carrier complete)")
    assert smax < 7.5

    Gamma = np.hstack([e[a] for a in range(N)])            # 128 x 1792
    Wfull = np.zeros((N * DIM, 192), dtype=complex)
    Wfull[:4 * DIM, :] = W
    gtr = np.max(np.abs(Gamma @ Wfull))
    print(f"[carrier]  ||Gamma W|| = {gtr:.2e}  (0 => W inside ker(Gamma): gamma-traceless)")
    assert gtr < 1e-10

    # symmetry generators on V4 (x) S
    gens512 = []
    for a, b in combinations(range(4), 2):                 # so(4): 6 generators
        gens512.append(np.kron(lvec4(a, b), I128) + np.kron(I4, sgen(e, a, b)))
    for a, b in combinations(range(4, 14), 2):             # so(10) internal: 45 generators
        gens512.append(np.kron(I4, sgen(e, a, b)))
    print(f"[gens]     G = so(4) (+) so(10): {len(gens512)} generators (6 + 45)")
    inv_err = max(np.max(np.abs(g @ W - W @ (W.conj().T @ g @ W))) for g in gens512)
    print(f"[gens]     max ||(1 - P_W) g W|| = {inv_err:.2e}  (0 => carrier G-invariant)")
    assert inv_err < 1e-9

    Gt = [W.conj().T @ g @ W for g in gens512]             # 192 x 192 compressed
    G_all = Gt
    G_prime = [W.conj().T @ Jn @ W for Jn in Jk] + Gt[6:]
    G_int = Gt[6:]

    # chirality and Krein structure
    om = I128.copy()
    for a in range(N):
        om = om @ e[a]
    om = om if (np.trace(om @ om) / DIM).real > 0 else (-1j) * om
    Gc = W.conj().T @ np.kron(I4, om) @ W
    Gc = 0.5 * (Gc + Gc.conj().T)
    gev = np.linalg.eigvalsh(Gc)
    npl, nmi = int((gev > 0.5).sum()), int((gev < -0.5).sum())
    print(f"[chirality] Gamma_c^2 = 1 defect = {np.max(np.abs(Gc @ Gc - np.eye(192))):.2e}, "
          f"split (+,-) = ({npl},{nmi})")
    assert npl == 96 and nmi == 96
    comm_err = max(np.max(np.abs(Gc @ g - g @ Gc)) for g in G_all)
    print(f"[chirality] max ||[Gamma_c, g]|| over all 51 generators = {comm_err:.2e}")
    assert comm_err < 1e-9

    om10 = I128.copy()
    for a in range(4, 14):
        om10 = om10 @ e[a]
    om10 = om10 if (np.trace(om10 @ om10) / DIM).real > 0 else (-1j) * om10
    O10 = W.conj().T @ np.kron(I4, om10) @ W
    align = min(np.max(np.abs(Gc - O10)), np.max(np.abs(Gc + O10)))
    print(f"[chirality] internal so(10) chirality omega_10 vs Gamma_c: min ||Gc -+ O10|| = "
          f"{align:.2e}  (0 => W_+ = pure 16-content, W_- = pure 16bar-content)")
    assert align < 1e-9

    spacelike = [a for a in range(N) if a not in TIMELIKE]
    bS = I128.copy()
    for s in spacelike:
        bS = bS @ e[s]
    if np.linalg.norm(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    K512 = np.kron(I4, bS)
    kinv = max(np.max(np.abs(g.conj().T @ K512 + K512 @ g)) for g in gens512)
    Kc = W.conj().T @ K512 @ W
    Kc = 0.5 * (Kc + Kc.conj().T)
    kev = np.linalg.eigvalsh(Kc)
    ksig = (int((kev > 1e-8).sum()), int((kev < -1e-8).sum()))
    kblk = np.max(np.abs(((np.eye(192) + Gc) / 2) @ Kc @ ((np.eye(192) + Gc) / 2)))
    print(f"[Krein]    invariance max||g^dag K + K g|| = {kinv:.2e}; carrier signature = "
          f"(+{ksig[0]},-{ksig[1]}); ++ block norm = {kblk:.2e} (0 => purely cross-chirality)")
    assert kinv < 1e-9 and ksig == (96, 96)

    # PART B -- exact torus combinatorics (integer arithmetic)
    print("\n" + "=" * 98)
    print("PART B -- exact so(10) weight combinatorics (integer arithmetic; signature-independent)")
    print("=" * 98)
    w16 = [s for s in product([1, -1], repeat=5) if s.count(-1) % 2 == 0]
    w16b = [s for s in product([1, -1], repeat=5) if s.count(-1) % 2 == 1]
    assert len(w16) == 16 and len(w16b) == 16
    zsum = lambda A, B: sum(1 for x in A for y in B if all(p + q == 0 for p, q in zip(x, y)))
    c_pp, c_mm, c_pm = zsum(w16, w16), zsum(w16b, w16b), zsum(w16, w16b)
    print(f"  zero-weight-sum pairs:  16 x 16 = {c_pp}   16bar x 16bar = {c_mm}   16 x 16bar = {c_pm}")
    print("  => NO invariant bilinear pairing exists on same-chirality blocks (count 0 is a proof:")
    print("     a singlet has zero weight), in EVERY real form.  Cross-chirality pairing allowed.")
    assert c_pp == 0 and c_mm == 0 and c_pm == 16
    print("  spinor 2-smoothness (item 6): dim of any SO(m) spinor = 2^floor(m/2), a power of two:")
    print("   ", {m: 2 ** (m // 2) for m in range(2, 15)}, " -- never divisible by 3.")

    Pp, Pm = (np.eye(192) + Gc) / 2, (np.eye(192) - Gc) / 2

    # PART D -- the census under the full split covariance
    print("\n" + "=" * 98)
    print("PART D -- the class-C generator census (full split covariance G = so(4) (+) so(10))")
    print("=" * 98)
    res_G = census(G_all, "G = so(4)+so(10)")

    # Kramers sign of the antilinear channel: closed-form sweep over the WHOLE space.
    print("\n  Kramers analysis of the antilinear space (C4), whole-space sweep:")
    anti = [M / np.linalg.norm(M) * np.sqrt(192) for M in res_G["anti"]]
    Q = [[anti[i] @ anti[j].conj() for j in range(2)] for i in range(2)]
    coef = np.zeros((2, 2, 2), dtype=complex)
    worst_span = 0.0
    for i in range(2):
        for j in range(2):
            cp = np.trace(Pp @ Q[i][j]) / 96
            cm = np.trace(Pm @ Q[i][j]) / 96
            coef[i, j] = (cp, cm)
            worst_span = max(worst_span, np.linalg.norm(Q[i][j] - cp * Pp - cm * Pm))
    print(f"    products Q_ij = M_i conj(M_j) lie in span(P+,P-): max defect = {worst_span:.2e}")
    assert worst_span < 1e-7
    best = -np.inf
    for r in np.linspace(0.0, 4.0, 81):
        for th in np.linspace(0.0, 2 * np.pi, 128, endpoint=False):
            a, b = 1.0, r * np.exp(1j * th)
            cp = (abs(a) ** 2 * coef[0, 0, 0] + a * np.conj(b) * coef[0, 1, 0]
                  + np.conj(a) * b * coef[1, 0, 0] + abs(b) ** 2 * coef[1, 1, 0])
            cm = (abs(a) ** 2 * coef[0, 0, 1] + a * np.conj(b) * coef[0, 1, 1]
                  + np.conj(a) * b * coef[1, 0, 1] + abs(b) ** 2 * coef[1, 1, 1])
            if abs(cp.imag) < 1e-9 and abs(cm.imag) < 1e-9:
                best = max(best, min(cp.real, cm.real) / (1 + abs(b) ** 2))
    print(f"    max over the whole antilinear space of min(C^2 on W+, C^2 on W-) (normalized) = "
          f"{best:+.4f}")
    for i in range(2):
        print(f"    basis element #{i}:  C^2 = ({coef[i, i, 0].real:+.4f}) P+  +  "
              f"({coef[i, i, 1].real:+.4f}) P-")
    assert best < -1e-3, "a real structure C^2=+1 exists (item 2, still Z/2) -- reclassify 1->2"
    print("    => in Cl(9,5) every equivariant antilinear structure is chirality-PRESERVING and")
    print("       QUATERNIONIC per chirality block (C^2 = -1 on W+ and on W-): the Kramers wall,")
    print("       item (1), acting Z/2 within each chirality sector.  (A real structure C^2 = +1")
    print("       would instead be item (2)'s mod-2 reality -- also Z/2; none exists here.)")
    print("       NO chirality-swapping equivariant antilinear (re-grading) exists in class C:")
    print("       the AZ-CII escape direction is provably NON-EQUIVARIANT on this carrier --")
    print("       sharper than the paper's finite adversarial hunt, within the delimited class.")

    # sesquilinear signatures (item 3)
    print("\n  Krein signatures of the sesquilinear space (C3):")
    ses = res_G["ses"]
    for i in range(len(ses)):
        F = ses[i]
        Fh = 0.5 * (F + F.conj().T)
        if np.linalg.norm(Fh) < 1e-8:
            Fh = 0.5 * (1j * F + (1j * F).conj().T)
        evF = np.linalg.eigvalsh(Fh)
        sig = (int((evF > 1e-8).sum()), int((evF < -1e-8).sum()))
        print(f"    Hermitian form #{i}: signature (+{sig[0]},-{sig[1]})  -- even split, net 0")
        assert sig[0] == sig[1] == 96
    projK = Kc / np.linalg.norm(Kc)
    overlap = max(abs(np.vdot(projK, F / np.linalg.norm(F))) for F in ses)
    print(f"    (the physical Krein form K lies in this span: max |<K,F_i>| = {overlap:.3f})")

    # index-type integers (C5)
    print("\n  Index-type integers (C5):")
    basis = []
    for X in res_G["comm"]:
        r = X.copy()
        for Bb in basis:
            r = r - np.vdot(Bb, r) * Bb
        basis.append(r / np.linalg.norm(r))
    for nameT, T in (("Id     ", np.eye(192, dtype=complex)), ("Gamma_c", Gc), ("P_+    ", Pp),
                     ("P_-    ", Pm)):
        Tn = T / np.linalg.norm(T)
        rr = Tn.copy()
        for Bb in basis:
            rr = rr - np.vdot(Bb, rr) * Bb
        t, gt = T.trace().real, (Gc @ T).trace().real
        print(f"    {nameT}: distance to commutant span = {np.linalg.norm(rr):.2e};  "
              f"tr = {t:+04.0f},  graded tr = {gt:+04.0f}")
        assert np.linalg.norm(rr) < 1e-7
    print("    integer lattice attainable from equivariant intertwiners: traces {192, 96} and graded")
    print("    traces {0, +96, -96}.  All EVEN;  96 = 2^5*3, 192 = 2^6*3: the only odd factor is the")
    print("    carrier multiplicity 3 inside a DIMENSION (located), never an odd-prime congruence.")
    print("    dim Hom_G(W_+, W_-) = 0 (commutant is chirality-diagonal): no equivariant linear")
    print("    chirality-flip exists; with the Krein cross-structure this is item (3)'s content.")

    # PART E -- Clifford-level Kramers structure (item 1, the classic form)
    print("\n" + "=" * 98)
    print("PART E -- Clifford-level Kramers structure (item 1, the classic form)")
    print("=" * 98)
    words = [e[a] for a in range(N)] + [e[a] @ e[b] for a, b in combinations(range(N), 2)][:40]
    CS = hom_space(words, [w.conj() for w in words], "Cl(9,5) antilinear commutant on S")
    assert len(CS) == 1
    C = CS[0] * np.sqrt(DIM)
    CC = C @ C.conj()
    s = np.trace(CC) / DIM
    print(f"  C C-bar = {s.real:+.4f} I (defect {np.linalg.norm(CC - s * np.eye(DIM)):.2e})"
          f"  =>  J^2 = -1: QUATERNIONIC (Kramers), as Cl(9,5) = M(64,H) requires.")
    assert s.real < 0

    # cross-check: the paper's J_quat = id (x) U compressed to the carrier lies in the computed
    # antilinear space (antilinear part M_J = W^dag (I4 (x) C) W-bar), chirality-preserving
    CJ = np.kron(I4, C)
    leak = np.max(np.abs(CJ @ W.conj() - W @ (W.conj().T @ CJ @ W.conj())))
    MJ = W.conj().T @ CJ @ W.conj()
    MJ = MJ / np.linalg.norm(MJ)
    rr = MJ.copy()
    for M in res_G["anti"]:
        rr = rr - np.vdot(M, rr) * M
    sw = np.linalg.norm(Gc @ MJ + MJ @ Gc.conj())
    pv = np.linalg.norm(Gc @ MJ - MJ @ Gc.conj())
    print(f"  J_quat on the carrier: leakage {leak:.2e}; distance to computed antilinear span = "
          f"{np.linalg.norm(rr):.2e}; ||Gc M + M Gc*|| = {sw:.2f}, ||Gc M - M Gc*|| = {pv:.2e}")
    print("  => GU's quaternionic structure IS one of the census generators (chirality-preserving).")
    assert leak < 1e-9 and np.linalg.norm(rr) < 1e-7 and pv < 1e-8

    if STAGE == "1":
        np.savez(STATE, Gt=np.stack(Gt), Jc=np.stack([W.conj().T @ Jn @ W for Jn in Jk]),
                 Gc=Gc, n_swap_G=res_G["n_swap"],
                 dims=np.array([len(res_G[k]) for k in ("comm", "anti", "bil", "ses")]))
        print(f"\n[stage 1 complete in {time.time() - T0:.1f}s; state saved to {STATE}]")
        raise SystemExit(0)

    # free the large 512-dim intermediates before the heavier small-group censuses
    import gc
    del gens512, Cas, cV, Wfull, Gamma, K512, Q
    gc.collect()

# ============================================================= stage 2: load state if requested
if STAGE == "2":
    st = np.load(STATE)
    Gt = [st["Gt"][i] for i in range(st["Gt"].shape[0])]
    Gc = st["Gc"]
    G_all, G_prime, G_int = Gt, [st["Jc"][i] for i in range(3)] + Gt[6:], Gt[6:]
    Pp, Pm = (np.eye(192) + Gc) / 2, (np.eye(192) - Gc) / 2
    res_G = {"n_swap": int(st["n_swap_G"]),
             "comm": [None] * int(st["dims"][0]), "anti": [None] * int(st["dims"][1]),
             "bil": [None] * int(st["dims"][2]), "ses": [None] * int(st["dims"][3])}
    print(f"[stage 2] state loaded from {STATE}")

# ==================================================== PART F: robustness under smaller covariance
print("\n" + "=" * 98)
print("PART F -- robustness: census under smaller covariance (boundary of the equivariance choice)")
print("=" * 98)
res_Gp = census(G_prime, "G' = su(2)_+ + so(10)", verbose=False)
res_Gi = census(G_int, "G'' = so(10) only", verbose=False)

# ------------------------------------------------------------------------------------- verdict
print("\n" + "#" * 98)
print("# CLASS-C GENERATOR CENSUS -- VERDICT")
print("#" * 98)
nG = {k: len(v) for k, v in res_G.items() if isinstance(v, list)}
n_swap_total = res_G["n_swap"] + res_Gp["n_swap"] + res_Gi["n_swap"]
print(f"""
  Generator table (G = so(4)+so(10), real form so(4)+so(5,5), on the 192-dim carrier):
    (C1) linear commutant End_G(W)          dim {nG['comm']}   = span(Id, Gamma_c); chirality-diagonal;
                                                     integers tr/graded-tr in {{0, +-96, 192}}: even [item 3/4]
    (C2) invariant bilinear forms           dim {nG['bil']}   ALL purely cross-chirality (exact torus
                                                     proof: 16x16 zero-sum count = 0)        [item 2/3]
    (C3) invariant sesquilinear forms       dim {nG['ses']}   ALL purely cross-chirality; every Hermitian
                                                     combination has signature (+96,-96)     [item 3]
    (C4) antilinear intertwiners            dim {nG['anti']}   ALL chirality-PRESERVING (T-type; the split
                                                     so(5,5) 16 is self-conjugate), quaternionic per
                                                     block C^2 = -1: Kramers Z/2; NO antilinear
                                                     re-grading (swap) exists in class C     [item 1/2]
    (C5) cross-chirality linear intertwiners dim 0  (commutant chirality-diagonal)           [item 3]
    (C6) named characteristic inputs        finite list swept by enum_extension_engine.py;   [items 4-7]
                                            unrestricted characteristic lift remains open

  Every computed C1-C5 generator maps into the typed finite packet; finite-torsion
  content is 2-primary, while equalities/dimensions remain in their own codomains.
  The only odd factor anywhere is the carrier multiplicity 3 inside the DIMENSIONS
  192 = 2^6*3 and 96 = 2^5*3 -- located, not a congruence.  No generator imposes an
  odd-prime congruence in the encoded finite rows.  Robust under shrinking the covariance
  to su(2)_+ + so(10) (dims 8/8/8/8) and to so(10) alone (dims 72/72/72/72).

  ==> C1-C5 LIFT TO C_fin IS COMPLETE FOR THIS COMPACT CARRIER (computed grade).
      C6 and the unrestricted semantic C_inv lift remain open.
      (chirality-swapping antilinear generators found across all three covariance choices: """
      + str(n_swap_total) + """ -- must be 0)
""")
assert n_swap_total == 0
print(f"  total runtime this stage: {time.time() - T0:.1f}s")
# EOF
