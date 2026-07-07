"""
vg_v4_quantize_break_commuting_square.py -- Big-swing gauntlet 2026-07-06, ROUTE V4 (leg T6').

DOES QUANTIZATION COMMUTE WITH BREAKING?  Q(break(S)) vs break(Q(S)) on the
Pais-Uhlenbeck (PU) fourth-order oscillator, the Bateman-Turok / conformal-gravity toy.

The square:
                     break (w -> w +/- eps)
        S(eps=0)  ------------------------------>  S(eps)
           |                                          |
         Q |  (Krein quantization:                  Q |
           |   spectral C operator +                  |
           v   projector-Born physical sector)        v
        Q(S(0))   ??  <---- eps -> 0 ----??        Q(S(eps))

Arena (Bender-Mannheim PRL 100, 110402 (2008) realization, FROM MEMORY; gamma = 1,
z = -i q1 contour rotation of the Ostrogradsky form):

    H(eps) = i p_z y + p_y^2/2 + (w1^2 + w2^2) y^2/2 + (w1^2 w2^2) z^2/2,
    w1 = w + eps,  w2 = w - eps,  w = 1.

Exact spectrum (anchor): E(n1,n2) = w1(n1 + 1/2) + w2(n2 + 1/2).
Kinematic Krein metric: eta = z-parity (verified: ||eta H^dag eta - H|| ~ 0).
Truncated two-mode Fock space, N = 12 per mode (convergence re-run at N = 16).

The quantization functor Q (the physical structure, built from spectral data only):
    Q1. eigendecompose H (needs real spectrum: PT-unbroken);
    Q2. Krein-normalize: nu_k = <v_k, eta v_k> (needs nu_k != 0: eigenvectors not eta-null);
    Q3. C = sum_k sign(nu_k) Pi_k, with Pi_k = v_k (eta v_k)^dag / nu_k the eta-orthogonal
        spectral projector (checks: C^2 = 1 on the window, [C,H] ~ 0, eta*C-Gram > 0);
    Q4. physical sector P_phys = (1 + C)/2; projector Born rule lives there.

WINDOW DISCIPLINE (the truncated non-normal H carries SPURIOUS edge eigenvalues, some
complex -- e.g. 4.21 +/- 2.38j and a drifting real one at 2.48/2.80 for N = 12/16; a naive
lowest-by-real-part window sweeps them in): every physical window is selected by nearest-
matching to the EXACT level formula, then re-verified against it. Quantitative divergence
fits use the (n = 0, n = 1) window only -- 3 states, truncation error 2.0e-4 (N = 12) /
4.8e-6 (N = 16) at the degenerate point -- with a per-eps validity gate (spectrum real,
C^2 = 1) so no fitted point sits on the truncation floor; the first point BELOW the floor
is printed as an illustration and excluded from the fit.

WHAT IS MEASURED:
  (a) the degenerate point eps = 0 (conformal/unbroken analog): Jordan pathology, via the
      per-cluster self Krein norms and K-Gram eigenvalues, eigenvector coalescence,
      complex-pair counts, and a perturbation-splitting exponent (Jordan detector: 1/2);
  (b) path A = break-then-quantize: C_A(eps) for eps > 0 (well-defined; all checks pass);
  (c) path B = quantize-then-break: Q at eps = 0 fails at step Q2 (documented, with
      numbers), and the limit lim_{eps->0} C_A(eps) DIVERGES: fit ||C_A|| ~ eps^-alpha;
  (d) the kinematic ghost parity: which parity operators remain well-defined ([P,H(0)] = 0)
      at the degenerate point, vs the spectral C which does not exist there.
Controls: (i) random eta-pseudo-Hermitian input (pipeline CAN succeed -> not a tautology);
  (ii) degenerate-but-diagonalizable control (broken-chart normal form at eps = 0):
      degeneracy alone does NOT kill C -- but leaves C NON-UNIQUE (O(1,1) family exhibited).

ANCHORS FIRST: this is a toy route; the carrier anchors it informs are reproduced anyway
(triplet Krein signature (+96,-96,0) in (9,5); beta_S pseudo-anti-Hermiticity ~ 0;
rank(Gamma) = 128, dim ker(Gamma) = 1664) by importing the verified carrier recipe.

TARGET-IMPORT GUARD: no forbidden target {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8}
is assumed, inserted, hardcoded as an answer, or divided by anywhere below. The only inputs
are w = 1, the eps/delta grids, and truncation sizes N = 12/16. Every printed count is
measured. (Exact level formulas are used only to SELECT windows; the match is then verified
as an anchor check, so nothing is assumed that is not also tested.)

A separate big-swing workflow (R1-R4) is running; nothing below cites its outcomes.

Run from repo root:  python tests/big-swing/vg_v4_quantize_break_commuting_square.py
Exit 0 = all documented tolerance checks passed.
"""

import importlib.util
import pathlib
import sys

import numpy as np

np.random.seed(20260706)

REPO = pathlib.Path(__file__).resolve().parents[2]
FAILURES = []


def hr(title):
    print("\n" + "=" * 92 + "\n" + title + "\n" + "=" * 92)


def check(name, value, tol):
    ok = bool(value < tol)
    if not ok:
        FAILURES.append((name, value, tol))
    print(f"    [{'PASS' if ok else 'FAIL'}] {name} = {value:.3e}  (tol {tol:.0e})")
    return ok


def require(name, cond, detail=""):
    if not cond:
        FAILURES.append((name, detail, ""))
    print(f"    [{'PASS' if cond else 'FAIL'}] {name}{('  (' + detail + ')') if detail else ''}")
    return cond


# ----------------------------------------------------------------------------------
# SECTION A1 -- carrier anchors (the receipts this route's verdict feeds back into)
# ----------------------------------------------------------------------------------
def carrier_anchors():
    hr("A1. CARRIER ANCHORS (reproduced from tests/generation-sector/ghost_parity_krein.py)")
    path = REPO / "tests" / "generation-sector" / "ghost_parity_krein.py"
    spec = importlib.util.spec_from_file_location("gpk", path)
    gpk = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gpk)
    # (9,5): prints beta_S pseudo-anti-Hermiticity residual and asserts triplet
    # Krein signature (+96, -96, 0) internally.
    gpk.analyze({4, 5, 6, 7, 8}, "(9,5)")
    e = [(1j * gpk.base[a] if a in {4, 5, 6, 7, 8} else gpk.base[a]) for a in range(14)]
    Gamma = np.hstack(e)
    r = int(np.linalg.matrix_rank(Gamma))
    ker = Gamma.shape[1] - r
    print(f"  rank(Gamma) = {r}   dim ker(Gamma) = {ker}")
    require("carrier anchors: (+96,-96,0) triplet, beta residual ~0, rank/ker",
            r == 128 and ker == 1664, f"rank {r}, ker {ker}")


# ----------------------------------------------------------------------------------
# PU machinery
# ----------------------------------------------------------------------------------
def osc(N, s):
    """Truncated oscillator: ground state ~ exp(-s x^2/2). x, p, parity."""
    b = np.zeros((N, N), dtype=complex)
    b[np.arange(N - 1), np.arange(1, N)] = np.sqrt(np.arange(1, N))
    x = (b + b.conj().T) / np.sqrt(2 * s)
    p = 1j * np.sqrt(s / 2) * (b.conj().T - b)
    par = np.diag((-1.0) ** np.arange(N)).astype(complex)
    return x, p, par


def build(N, w1, w2):
    """PT-rotated PU Hamiltonian on Fock(N) x Fock(N); kinematic parities.

    Basis scales matched to the exact ground state exp(-a z^2/2 - b y^2/2 + i c z y)
    (Bender-Mannheim, from memory): a = (w1+w2) w1 w2, b = w1 + w2. At w = 1 these are
    ~2 for all eps in the sweep, so the basis is (essentially) eps-independent and the
    family H(eps) is a smooth matrix family at fixed kinematics."""
    a_sc, b_sc = (w1 + w2) * w1 * w2, (w1 + w2)
    z1, p1, par1 = osc(N, a_sc)
    y1, py1, par2 = osc(N, b_sc)
    I = np.eye(N, dtype=complex)
    Z, Pz = np.kron(z1, I), np.kron(p1, I)
    Y, Py = np.kron(I, y1), np.kron(I, py1)
    Om2, kap = w1 ** 2 + w2 ** 2, (w1 * w2) ** 2
    H = 1j * (Pz @ Y) + Py @ Py / 2 + (Om2 / 2) * (Y @ Y) + (kap / 2) * (Z @ Z)
    return dict(H=H, eta=np.kron(par1, I), P_z=np.kron(par1, I), P_y=np.kron(I, par2),
                P_tot=np.kron(par1, par2), N=N, w1=w1, w2=w2)


def exact_levels(w1, w2, nmax):
    lv = [(w1 * (n1 + 0.5) + w2 * (n2 + 0.5), (n1, n2))
          for n1 in range(nmax + 1) for n2 in range(nmax + 1) if n1 + n2 <= nmax]
    return sorted(lv)


def low_window(H, M):
    """Lowest-M eigenpairs by real part (unit-normalized). Controls only -- the PU
    truncation carries spurious edge eigenvalues that this window would sweep in."""
    E, V = np.linalg.eig(H)
    order = np.argsort(E.real)[:M]
    E, V = E[order], V[:, order]
    V = V / np.linalg.norm(V, axis=0, keepdims=True)
    return E, V


def select_window(H, centers):
    """Physical window by greedy nearest-matching to expected level centers
    (list of (center, count)), with global dedupe. Genuine levels sit within
    <= 3.5e-3 of their centers at N = 12 while spurious ones are O(0.5) away,
    so the assignment is unambiguous; the match is re-verified by the caller."""
    E, V = np.linalg.eig(H)
    used = np.zeros(len(E), dtype=bool)
    sel = []
    for c, cnt in centers:
        d = np.abs(E - c)
        d[used] = np.inf
        for _ in range(cnt):
            k = int(np.argmin(d))
            sel.append(k)
            used[k] = True
            d[k] = np.inf
    sel = np.array(sel)
    sel = sel[np.argsort(E[sel].real)]
    Vs = V[:, sel]
    Vs = Vs / np.linalg.norm(Vs, axis=0, keepdims=True)
    return E[sel], Vs


def spectral_Q(H, eta, M, centers=None):
    """The quantization functor Q on the physical window. Returns diagnostics; never raises."""
    if centers is None:
        E, V = low_window(H, M)
    else:
        E, V = select_window(H, centers)
        assert len(E) == M
    imag_max = float(np.max(np.abs(E.imag)))
    nus = np.array([(V[:, k].conj() @ eta @ V[:, k]).real for k in range(M)])
    min_nu = float(np.min(np.abs(nus)))
    s0 = np.sign(nus[0]) if nus[0] != 0 else 1.0   # convention: C = +1 on ground state
    with np.errstate(divide="ignore", invalid="ignore"):
        Pis = [np.outer(V[:, k], (eta @ V[:, k]).conj()) / nus[k] for k in range(M)]
    C = s0 * sum(np.sign(nus[k]) * Pis[k] for k in range(M))
    SM = sum(Pis)                                   # identity on the window span
    r_C2 = float(np.linalg.norm(C @ C - SM) / max(np.linalg.norm(SM), 1e-300))
    r_comm = float(np.linalg.norm(C @ H - H @ C) /
                   (max(np.linalg.norm(C), 1e-300) * np.linalg.norm(H)))
    # eta*C positivity on the window: Gram of eta C in an orthonormal basis of span(V)
    Qb, _ = np.linalg.qr(V)
    G = Qb.conj().T @ (eta @ C) @ Qb
    G = 0.5 * (G + G.conj().T)
    gev = np.linalg.eigvalsh(G)
    min_etaC, max_etaC = float(np.min(gev)), float(np.max(gev))
    Pphys = 0.5 * (SM + C)
    return dict(E=E, V=V, nus=nus * s0, min_nu=min_nu, C=C, r_C2=r_C2, r_comm=r_comm,
                min_etaC=min_etaC, max_etaC=max_etaC, condV=float(np.linalg.cond(V)),
                normC=float(np.linalg.norm(C, 2)), imag_max=imag_max,
                normPphys=float(np.linalg.norm(Pphys, 2)))


def splitting_exponent(H, Ebar, B, deltas):
    """Perturbation-splitting exponent at the 2-fold cluster around Ebar:
    Jordan block -> splitting ~ delta^(1/2); diagonalizable degenerate -> ~ delta^1."""
    sps = []
    for d in deltas:
        Ep = np.linalg.eigvals(H + d * B)
        sel = np.argsort(np.abs(Ep - Ebar))[:2]
        sps.append(abs(Ep[sel[0]] - Ep[sel[1]]))
    slope = float(np.polyfit(np.log10(np.array(deltas)), np.log10(np.array(sps)), 1)[0])
    return slope, sps


# ----------------------------------------------------------------------------------
def pu_anchors(N):
    hr(f"A2. PU TOY ANCHORS (N = {N} per mode, w1 = 1.3, w2 = 0.7 -- broken, far from degeneracy)")
    mdl = build(N, 1.3, 0.7)
    H, eta = mdl["H"], mdl["eta"]
    check("pseudo-Hermiticity ||eta H^dag eta - H|| / ||H||",
          np.linalg.norm(eta @ H.conj().T @ eta - H) / np.linalg.norm(H), 1e-12)
    check("[P_tot, H] / ||H||",
          np.linalg.norm(mdl["P_tot"] @ H - H @ mdl["P_tot"]) / np.linalg.norm(H), 1e-12)
    lv = exact_levels(1.3, 0.7, 3)          # n1 + n2 <= 3: 10 distinct levels, all well
    M = len(lv)                              # inside the truncation-accurate window
    print(f"  window: the {M} exact levels with n1 + n2 <= 3 (nearest-matched, then verified)")
    centers = [(x[0], 1) for x in lv]
    q = spectral_Q(H, eta, M, centers=centers)
    E = q["E"]
    Eex = np.array([x[0] for x in lv])
    check(f"spectrum anchor: max |E_num - E(n1,n2)| over these {M}",
          float(np.max(np.abs(np.sort(E.real) - Eex))), 1e-3)
    check("max |Im E| over the window", q["imag_max"], 1e-6)
    # ghost grading: Krein-norm sign vs mode labels (measured, not assumed)
    labels = [x[1] for x in lv]              # sorted by energy; E order matches (distinct)
    signs = np.sign(q["nus"])
    match1 = int(np.sum(signs == np.array([(-1.0) ** l[0] for l in labels])))
    match2 = int(np.sum(signs == np.array([(-1.0) ** l[1] for l in labels])))
    print(f"  Krein-norm sign pattern vs (-1)^n1: {match1}/{M} match;"
          f" vs (-1)^n2: {match2}/{M} match")
    grading = ("(-1)^n1 (w1 quanta)" if match1 == M
               else ("(-1)^n2 (w2 quanta)" if match2 == M else "MIXED"))
    print(f"  -> ghost grading is the parity of ONE mode's occupation (measured: {grading};"
          f" which mode is a w1<->w2 labeling convention)")
    require("ghost grading is a single-mode occupation parity", match1 == M or match2 == M,
            f"{match1}/{M}, {match2}/{M}")
    check("C^2 = 1 on window (relative)", q["r_C2"], 1e-6)
    check("[C, H] relative residual", q["r_comm"], 1e-8)
    print(f"  min eig of eta*C Gram on window = {q['min_etaC']:.6f} (positive => Born sector OK)")
    require("eta*C > 0 on window", q["min_etaC"] > 0, f"{q['min_etaC']:.3e}")
    print(f"  ||C|| = {q['normC']:.3f}, cond(V) = {q['condV']:.3f}, min|nu| = {q['min_nu']:.3f}")
    print("  => far from degeneracy, Q is a complete, well-conditioned quantization: the toy")
    print("     is a faithful Krein/ghost-parity arena, not a numerical accident.")


def degenerate_point(N):
    hr(f"B. THE DEGENERATE POINT eps = 0 (equal-frequency PU = conformal/unbroken analog), N = {N}")
    mdl = build(N, 1.0, 1.0)
    H, eta = mdl["H"], mdl["eta"]
    check("pseudo-Hermiticity at eps=0", np.linalg.norm(eta @ H.conj().T @ eta - H)
          / np.linalg.norm(H), 1e-12)
    E, V = np.linalg.eig(H)
    print("  cluster n | size | #complex E | max self |nu_k| | min |K-Gram eig| | max eigvec overlap")
    rows = []
    for n in range(1, 4):
        d = np.abs(E - (n + 1.0))
        sel = np.argsort(d)[: n + 1]
        Ec, Vc = E[sel], V[:, sel]
        Vc = Vc / np.linalg.norm(Vc, axis=0, keepdims=True)
        m = n + 1
        ncx = int(np.sum(np.abs(Ec.imag) > 1e-9))
        selfnu = float(np.max(np.abs([Vc[:, i].conj() @ eta @ Vc[:, i] for i in range(m)])))
        Gr = Vc.conj().T @ eta @ Vc
        Gr = 0.5 * (Gr + Gr.conj().T)
        gmin = float(np.min(np.abs(np.linalg.eigvalsh(Gr))))
        ov = max(abs(Vc[:, i].conj() @ Vc[:, j]) for i in range(m) for j in range(i + 1, m))
        rows.append((n, m, ncx, selfnu, gmin, ov))
        print(f"     {n}     |  {m}   |     {ncx}      |   {selfnu:11.3e}   |   {gmin:11.3e}    |     {ov:9.6f}")
    n1 = rows[0]
    check("cluster n=1: max self Krein norm |nu_k| (exactly eta-null pair)", n1[3], 1e-9)
    print(f"  (self-norms vanish EXACTLY for truncation-resolved complex pairs: eta-pseudo-"
          f"Hermiticity forces <v, eta v> = 0 whenever Im E != 0.)")
    print(f"  smallest K-Gram eigenvalue of the n=1 eigenspace = {n1[4]:.3e} "
          f"(-> 0 with N: K-null degeneracy)")
    require("cluster n=1: K-Gram degenerating (min |eig| < 1e-3)", n1[4] < 1e-3, f"{n1[4]:.3e}")
    print(f"  eigenvector coalescence at n=1: max overlap = {n1[5]:.6f} (Jordan -> 1)")
    require("eigenvector coalescence > 0.999 at the degenerate point", n1[5] > 0.999,
            f"{n1[5]:.6f}")
    # perturbation-splitting exponent (Jordan detector): 1/2 for a 2x2 Jordan block
    B = np.random.randn(*H.shape) + 1j * np.random.randn(*H.shape)
    B = B / np.linalg.norm(B, 2)
    deltas = [3e-2, 1e-2, 3e-3, 1e-3]
    slope, sps = splitting_exponent(H, 2.0, B, deltas)
    print(f"  perturbation-splitting at n=1 under random B: " +
          " ".join(f"delta={d:.0e}->{s:.2e}" for d, s in zip(deltas, sps)))
    print(f"  splitting exponent = {slope:.3f} (Jordan block -> 0.5; diagonalizable -> 1.0)")
    require("splitting exponent within 0.1 of the Jordan value 1/2", abs(slope - 0.5) < 0.1,
            f"{slope:.3f}")
    return rows, slope


def path_A_sweep(N, eps_list, eps_floor_demo=None):
    hr(f"C. PATH A: break THEN quantize -- C_A(eps) for eps > 0, N = {N}")
    print("  window: 3 states (clusters n = 0, 1), exact centers E = 1 and 2 +/- eps.")
    print("  Q(H(eps)) is well-defined at every eps in the sweep; its cost as eps -> 0:")
    print("     eps     |  min|nu| (n=1) |   ||C_A||   | ||P_phys|| |  cond(V)  | C^2-1 rel | [C,H] rel | max|Im E|")
    out = []
    prevC, cauchy = None, []
    for eps in eps_list:
        mdl = build(N, 1.0 + eps, 1.0 - eps)
        q = spectral_Q(mdl["H"], mdl["eta"], 3, centers=[(1.0, 1), (2.0, 2)])
        print(f"  {eps:9.1e} |  {q['min_nu']:12.4e}  | {q['normC']:11.4e} |"
              f" {q['normPphys']:9.3e} | {q['condV']:9.3e} | {q['r_C2']:8.1e} |"
              f" {q['r_comm']:8.1e} | {q['imag_max']:8.1e}")
        out.append(dict(eps=eps, **{k: q[k] for k in
                    ("min_nu", "normC", "condV", "r_C2", "r_comm", "min_etaC", "imag_max",
                     "normPphys")}))
        if prevC is not None:
            cauchy.append(float(np.linalg.norm(q["C"] - prevC, 2)))
        prevC = q["C"]
    # validity gate: every FITTED point is a genuine quantization, off the truncation floor
    for o in out:
        require(f"path A valid at eps={o['eps']:.0e} (real spectrum, C^2=1, [C,H]~0, etaC>0)",
                o["imag_max"] < 1e-9 and o["r_C2"] < 1e-6 and o["r_comm"] < 1e-8
                and o["min_etaC"] > 0,
                f"imag {o['imag_max']:.1e}, C2 {o['r_C2']:.1e}")
    print("  Cauchy check ||C(eps_k+1) - C(eps_k)||_2:", " ".join(f"{c:.3e}" for c in cauchy))
    require("C_A(eps) is NOT Cauchy as eps -> 0 (differences grow)", cauchy[-1] > 10 * cauchy[0],
            f"first {cauchy[0]:.2e}, last {cauchy[-1]:.2e}")
    le = np.log10(np.array([o["eps"] for o in out]))
    lc = np.log10(np.array([o["normC"] for o in out]))
    ln = np.log10(np.array([o["min_nu"] for o in out]))
    fitC = np.polyfit(le, lc, 1)
    alpha = -float(fitC[0])
    resC = float(np.max(np.abs(np.polyval(fitC, le) - lc)))
    beta = float(np.polyfit(le, ln, 1)[0])
    print(f"  FIT: ||C_A(eps)|| ~ eps^-alpha, alpha = {alpha:.3f} (max log10 fit residual {resC:.3f})")
    print(f"  FIT: min|nu|(n=1 pair) ~ eps^+beta, beta = {beta:.3f}")
    require("divergence detected: alpha > 0.5 (square would commute if C converged)",
            alpha > 0.5, f"alpha = {alpha:.3f}")
    if eps_floor_demo is not None:
        mdl = build(N, 1.0 + eps_floor_demo, 1.0 - eps_floor_demo)
        q = spectral_Q(mdl["H"], mdl["eta"], 3, centers=[(1.0, 1), (2.0, 2)])
        print(f"  [illustration, EXCLUDED from fit] eps = {eps_floor_demo:.0e} is at/below the"
              f" N = {N} truncation floor:")
        print(f"      max|Im E| = {q['imag_max']:.1e}, min|nu| = {q['min_nu']:.1e},"
              f" ||C|| = {q['normC']:.1e}, C^2-1 rel = {q['r_C2']:.1e}")
        print("      -- the truncated family hits its effective Jordan point (complex pair /"
              " failing involution) before")
        print("      the exact eps = 0, and Q degrades exactly as at the degenerate point."
              " (The floor moves down with N.)")
    return out, alpha, beta


def path_B(N):
    hr(f"D. PATH B: quantize THEN break -- attempt Q at eps = 0, N = {N}")
    mdl = build(N, 1.0, 1.0)
    H, eta = mdl["H"], mdl["eta"]
    E, V = select_window(H, [(1.0, 1), (2.0, 2)])
    ncx = int(np.sum(np.abs(E.imag) > 1e-9))
    print(f"  Q1 (spectral resolution): {ncx}/3 window eigenvalues acquire imaginary parts")
    print(f"     (the truncation resolves the defective n=1 cluster into a complex pair;"
          f" max|Im E| = {np.max(np.abs(E.imag)):.3e};")
    print("      in the exact model the cluster is a Jordan block -- either way, no real"
          " simple spectrum exists).")
    nus = np.array([(V[:, k].conj() @ eta @ V[:, k]).real for k in range(3)])
    print(f"  Q2 (Krein normalization): min |nu_k| = {np.min(np.abs(nus)):.3e} -- the n=1"
          f" eigenvectors are eta-NULL;")
    print("     sign(nu_k) is undefined at 0 and 1/nu_k in the spectral projector diverges."
          " Q FAILS AT STEP Q2.")
    q = spectral_Q(H, eta, 3, centers=[(1.0, 1), (2.0, 2)])
    print(f"  Q3 (forcing the construction anyway): ||C|| = {q['normC']:.3e},"
          f" C^2-1 relative residual = {q['r_C2']:.3e}")
    print("     -> the C operator does not exist at the degenerate (unbroken/conformal)"
          " point. There is nothing")
    print("        to 'break' on path B: break(Q(S)) is undefined at its first arrow.")
    require("path B fails at Q2 (eta-null: min|nu| < 1e-9) and forced C is not an involution",
            float(np.min(np.abs(nus))) < 1e-9 and q["r_C2"] > 1e-2,
            f"min|nu| {np.min(np.abs(nus)):.1e}, C2 rel {q['r_C2']:.1e}")
    return dict(ncx=ncx, min_nu=float(np.min(np.abs(nus))), normC=q["normC"], r_C2=q["r_C2"])


def controls(N, M):
    hr("E. CONTROLS (the checks can fail; the pipeline is not theater)")
    # E1: random eta-pseudo-Hermitian, generically diagonalizable with real spectrum:
    # H_r = eta G with G Hermitian positive definite  =>  eta H_r^dag eta = H_r, spec real.
    dim = N * N
    par = np.diag((-1.0) ** np.arange(N)).astype(complex)
    eta = np.kron(par, np.eye(N, dtype=complex))
    R = np.random.randn(dim, dim) + 1j * np.random.randn(dim, dim)
    G = R @ R.conj().T / dim + 0.5 * np.eye(dim)
    Hr = eta @ G
    q = spectral_Q(Hr, eta, M)
    print("  E1 random pseudo-Hermitian control (same pipeline, same window size):")
    check("    E1: max |Im E|", q["imag_max"], 1e-8)
    check("    E1: C^2 = 1 relative", q["r_C2"], 1e-8)
    check("    E1: [C, H] relative", q["r_comm"], 1e-10)
    print(f"    E1: min|nu| = {q['min_nu']:.3f}, ||C|| = {q['normC']:.3f} (bounded; C exists)")
    definite = (q["min_etaC"] > 0) or (q["max_etaC"] < 0)
    print(f"    E1: eta*C Gram eigenvalue range [{q['min_etaC']:.3f}, {q['max_etaC']:.3f}]"
          f" (DEFINITE; the overall sign is the ground-state labeling convention s0 --")
    print("        for this random input the lowest-Re state happens to be a ghost, which"
          " flips the convention, not the physics)")
    require("    E1: generic input passes Q (min|nu| > 1e-2, eta*C definite)",
            q["min_nu"] > 1e-2 and definite,
            f"min|nu| {q['min_nu']:.3f}, Gram range [{q['min_etaC']:.2f},{q['max_etaC']:.2f}]")
    # E2: degenerate-but-diagonalizable control: the broken-phase NORMAL FORM at eps = 0.
    # H_diag = w1(N1+1/2) + w2(N2+1/2) with ghost metric K2 = (-1)^{N2}, at w1 = w2 = 1.
    print("  E2 degenerate-but-diagonalizable control (broken-chart normal form at eps = 0):")
    n_op = np.diag(np.arange(N)).astype(complex)
    I = np.eye(N, dtype=complex)
    Hd = np.kron(n_op + 0.5 * I, I) + np.kron(I, n_op + 0.5 * I)
    K2 = np.kron(I, par)
    P2 = K2.copy()      # kinematic ghost parity (-1)^{N2} in this chart
    qd = spectral_Q(Hd, K2, M)
    check("    E2: C^2 = 1 relative", qd["r_C2"], 1e-10)
    check("    E2: [C, H] relative", qd["r_comm"], 1e-12)
    print(f"    E2: min |nu_k| on degenerate eigenspaces = {qd['min_nu']:.3f} (NONsingular)")
    SM = qd["C"] @ qd["C"]      # identity on the window span (C^2 = SM verified above)
    dC = float(np.linalg.norm(SM @ (qd["C"] - P2) @ SM, 2))
    print(f"    E2: ||C|| = {qd['normC']:.3f}; ||C - (-1)^N2|| on window = {dC:.3e}")
    require("    E2: degeneracy alone does NOT break Q (min|nu| ~ 1, C = (-1)^N2)",
            qd["min_nu"] > 0.99 and dC < 1e-8, f"min|nu| {qd['min_nu']:.3f}, dC {dC:.1e}")
    print("    -> the eps=0 failure in section D is the K-NULL (Jordan) degeneracy of the")
    print("       PU dynamics, not degeneracy per se.")
    # E2b: but C at the degenerate point of the normal form is NOT unique: O(1,1) family.
    e10 = np.zeros(N * N, dtype=complex); e10[N * 1 + 0] = 1.0   # |n1=1, n2=0>
    e01 = np.zeros(N * N, dtype=complex); e01[N * 0 + 1] = 1.0   # |n1=0, n2=1>
    th = 0.3
    u = np.cosh(th) * e10 + np.sinh(th) * e01      # K-norm +1
    v = np.sinh(th) * e10 + np.cosh(th) * e01      # K-norm -1
    Cth = qd["C"].copy()
    for vec, s in ((e10, 1.0), (e01, -1.0)):        # remove the theta=0 pair
        Cth -= s * np.outer(vec, (K2 @ vec).conj()) / (vec.conj() @ K2 @ vec)
    for vec, s in ((u, 1.0), (v, -1.0)):            # insert the boosted pair
        Cth += s * np.outer(vec, (K2 @ vec).conj()) / (vec.conj() @ K2 @ vec)
    rC2 = float(np.linalg.norm(Cth @ Cth - SM) / np.linalg.norm(SM))
    rcm = float(np.linalg.norm(Cth @ Hd - Hd @ Cth) /
                (np.linalg.norm(Cth) * np.linalg.norm(Hd)))
    Qb, _ = np.linalg.qr(np.column_stack([e10, e01]))
    Gth = Qb.conj().T @ (K2 @ Cth) @ Qb; Gth = 0.5 * (Gth + Gth.conj().T)
    dth = float(np.linalg.norm(Cth - qd["C"], 2))
    print(f"    E2b: O(1,1)-boosted C_theta (theta=0.3): C^2=1 rel {rC2:.1e}, [C,H] rel {rcm:.1e},"
          f" eta*C>0 min-eig {np.min(np.linalg.eigvalsh(Gth)):.3f},")
    print(f"         yet ||C_theta - C_0|| = {dth:.3f} -> C at the degenerate point of the"
          f" normal form EXISTS but is NOT UNIQUE;")
    print("         the breaking direction is precisely the datum that selects one member.")
    require("    E2b: valid inequivalent C exhibited at the degenerate normal form",
            rC2 < 1e-10 and rcm < 1e-12 and dth > 0.1,
            f"rC2 {rC2:.1e}, rcm {rcm:.1e}, dth {dth:.3f}")
    return dict(dC=dC)


def parity_asymmetry(N):
    hr(f"F. THE SHARP ASYMMETRY: kinematic parity SURVIVES eps = 0; the C operator DOES NOT (N = {N})")
    mdl = build(N, 1.0, 1.0)
    H = mdl["H"]
    nH = np.linalg.norm(H)
    r_tot = np.linalg.norm(mdl["P_tot"] @ H - H @ mdl["P_tot"]) / nH
    r_z = np.linalg.norm(mdl["P_z"] @ H - H @ mdl["P_z"]) / nH
    r_y = np.linalg.norm(mdl["P_y"] @ H - H @ mdl["P_y"]) / nH
    print("  BM chart (fixed kinematics), at the degenerate point eps = 0:")
    check("    [P_tot, H(0)] / ||H|| (total parity = the kinematic PT-type parity)", r_tot, 1e-13)
    print(f"    [P_z, H(0)] / ||H|| = {r_z:.3f}, [P_y, H(0)] / ||H|| = {r_y:.3f}"
          f" (single-mode parities do not commute in these variables;")
    print("     P_z is the Krein METRIC eta, not a symmetry -- it intertwines H and H^dag).")
    # Diagonal chart: [(-1)^{N2}, H_diag(eps)] = 0 exactly for all eps including 0.
    n_op = np.diag(np.arange(N)).astype(complex)
    I = np.eye(N, dtype=complex)
    par = np.diag((-1.0) ** np.arange(N)).astype(complex)
    P2 = np.kron(I, par)
    for eps in (0.0, 0.1):
        Hd = ((1 + eps) * np.kron(n_op + 0.5 * I, I) + (1 - eps) * np.kron(I, n_op + 0.5 * I))
        check(f"    diagonal chart: [(-1)^N2, H_diag(eps={eps})] / ||H||",
              np.linalg.norm(P2 @ Hd - Hd @ P2) / np.linalg.norm(Hd), 1e-14)
    print("  => The kinematic (mode-counting / Bateman-Turok-type) parity is well-defined AT")
    print("     the degenerate point in both charts ([P_tot, H(0)] = 0 exactly in the BM chart;")
    print("     [(-1)^N2, H_diag(eps)] = 0 for ALL eps in the normal-form chart). The spectrally")
    print("     DERIVED C operator exists in neither: BM chart -- K-null Jordan eigenvectors")
    print("     (section D); normal-form chart -- exists but is NON-UNIQUE (control E2b), i.e.")
    print("     carries no canonical physical-sector split until the breaking selects one.")
    return r_tot, r_z, r_y


def main():
    hr("ROUTE V4 (T6'): DOES QUANTIZATION COMMUTE WITH BREAKING?  Q(break(S)) vs break(Q(S))")
    print("Toy: Pais-Uhlenbeck, w1 = 1+eps, w2 = 1-eps; truncated 2-mode Fock, N = 12 (check 16).")
    carrier_anchors()

    NMAIN, NCHK = 12, 16

    pu_anchors(NMAIN)
    rows0, slope0 = degenerate_point(NMAIN)
    eps12 = [1e-1, 3e-2, 1e-2, 3e-3, 1e-3, 3e-4]
    outA, alpha, beta = path_A_sweep(NMAIN, eps12, eps_floor_demo=1e-4)
    outB = path_B(NMAIN)
    controls(NMAIN, 15)
    parity_asymmetry(NMAIN)

    hr(f"G. CONVERGENCE RE-RUN AT N = {NCHK} (fitted grid one decade deeper: to 1e-4)")
    pu_anchors(NCHK)
    rows16, slope16 = degenerate_point(NCHK)
    eps16 = [1e-1, 3e-2, 1e-2, 3e-3, 1e-3, 3e-4, 1e-4]
    outA16, alpha16, beta16 = path_A_sweep(NCHK, eps16, eps_floor_demo=3e-5)
    path_B(NCHK)
    print(f"\n  N=12 vs N=16: alpha = {alpha:.3f} vs {alpha16:.3f}; beta = {beta:.3f} vs"
          f" {beta16:.3f}; splitting exponent = {slope0:.3f} vs {slope16:.3f}")
    print(f"  n=1 K-Gram min |eig| at eps=0: {rows0[0][4]:.3e} (N=12) vs {rows16[0][4]:.3e}"
          f" (N=16) -- shrinking toward the exact K-null Jordan pair")
    require("alpha converged in N (|alpha_12 - alpha_16| < 0.05)",
            abs(alpha - alpha16) < 0.05, f"{alpha:.3f} vs {alpha16:.3f}")
    require("K-Gram nullity deepens with N", rows16[0][4] < rows0[0][4],
            f"{rows0[0][4]:.1e} -> {rows16[0][4]:.1e}")

    hr("VERDICT")
    print(f"  (a) eps = 0 pathology CONFIRMED: the n=1 eigenvectors are exactly eta-null"
          f" (max self |nu| = {rows0[0][3]:.1e}),")
    print(f"      K-Gram min |eig| = {rows0[0][4]:.1e} (N=12) -> {rows16[0][4]:.1e} (N=16),"
          f" eigenvector coalescence {rows0[0][5]:.6f},")
    print(f"      perturbation-splitting exponent {slope0:.3f} (Jordan block value 1/2).")
    print(f"  (b) Path A (break -> quantize) WELL-DEFINED at every fitted eps > 0:"
          f" C^2 = 1, [C,H] ~ 0, eta*C > 0, spectrum real.")
    print(f"  (c) Path B (quantize -> break) FAILS at step Q2 (eta-null eigenvectors:"
          f" min|nu| = {outB['min_nu']:.0e}), and the limit does not exist:")
    print(f"      ||C_A(eps)|| ~ eps^-{alpha:.2f} (N=16: eps^-{alpha16:.2f}),"
          f" min|nu| ~ eps^+{beta:.2f}, C_A(eps) is not Cauchy.")
    print("      THE SQUARE DOES NOT COMMUTE: Q(break(S)) exists, break(Q(S)) is undefined,")
    print("      and the eps -> 0 limit of the broken quantization diverges at rate ~ 1/eps.")
    print("  (d) The kinematic ghost parity remains well-defined at eps = 0 ([P,H] = 0 to")
    print("      machine precision in both charts); the spectral C operator does not (BM chart)")
    print("      or is non-unique (normal form). Assembly order is physical content: the")
    print("      federation must declare BREAK-BEFORE-QUANTIZE; the deep-UV (unbroken/conformal)")
    print("      phase carries only the kinematic parity, no C-operator quantization.")
    if FAILURES:
        print("\nFAILED CHECKS:")
        for f in FAILURES:
            print("   ", f)
        sys.exit(1)
    print("\nALL CHECKS PASSED (exit 0).")


if __name__ == "__main__":
    main()
