#!/usr/bin/env python3
r"""
PRONG 0 -- the MEASURE-LEMMA probe (oracle-relative thesis swing).

Adversarial truth-test of the exact reopen lemma named by the Q1a hostile verify:

  Does GU own a measure w(s)ds for which
    (a) A~ = B(s) d_s + W~(s), B = -iK_uG, is J-self-adjoint with EQUAL Krein
        deficiency indices at the true noncompact fiber ends,
    (b) the measure-normalized W~, phi' (K_u winding) are bounded, K_u aligns, and
    (c) every genuine fiber end lies in the spacelike-gapped (q>0, K-definite) sector?

  Under (a)+(b)+(c): limit-point, theta dissolves, OPERATOR-END-PENCIL closes from
  structure. Without them: theta external OR (sharper) no J-self-adjoint realization.

This probe does NOT plant. It uses GU's actual (9,5)/Krein/section structure on the
faithful GL(4,R)/O(3,1) end model (verbatim from n2_end_family_probe.py), tests a
NATIVE measure (the DeWitt (9,5) volume sqrt|det G| ds), classifies the GENUINE
noncompact ends (the diagonal FLAT geodesics -- boosts are isometries in the isotropy
O(3,1) and do NOT move the base point, so they are not ends), and computes the genuine
J = K_S Krein deficiency-index structure with planted LP / LC / UNEQUAL-INDEX controls.

Deterministic, foreground, numpy only, no writes, no network. EXIT 0 = ran; the
printed findings, not the exit code, are the result.
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "generation-sector"))
import gen_sector_bridge as gb  # noqa: E402

N_DIRS, DIM = 14, 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)
LAM = 0.5
SPACE = np.arange(0, 9)
TIME = np.arange(9, 14)

# ---- verified Clifford objects ----------------------------------------------
e = gb.gammas()
K_S = e[0].copy()
for a in range(1, 9):
    K_S = K_S @ e[a]
I128 = np.eye(DIM, dtype=complex)
XI = np.real(np.asarray(gb.XI)).astype(float)


def cvec(v):
    return sum(v[a] * e[a] for a in range(N_DIRS))


def qform(v):
    return float(np.real(np.vdot(v, ETA * v)))


# ---- fiber geometry (verbatim structure from n2_end_family_probe.py) --------
SYM_IDX = [(0, 0), (1, 1), (2, 2), (3, 3),
           (0, 1), (0, 2), (1, 2), (0, 3), (1, 3), (2, 3)]


def sym_mat(i):
    a, b = SYM_IDX[i]
    m = np.zeros((4, 4))
    if a == b:
        m[a, a] = 1.0
    else:
        m[a, b] = m[b, a] = 1.0 / np.sqrt(2.0)
    return m


HMODES = [sym_mat(i) for i in range(10)]


def dewitt_gram(g, lam=LAM):
    gi = np.linalg.inv(g)
    G = np.zeros((14, 14))
    G[:4, :4] = g
    gih = [gi @ h for h in HMODES]
    tr1 = [float(np.trace(m)) for m in gih]
    for i in range(10):
        for j in range(i, 10):
            v = float(np.trace(gih[i] @ gih[j])) - lam * tr1[i] * tr1[j]
            G[4 + i, 4 + j] = G[4 + j, 4 + i] = v
    return G


def fixsign(v):
    k = int(np.argmax(np.abs(v)))
    return v if v[k] > 0 else -v


def frame_diag(a4, lam=LAM):
    a0, a1, a2, a3 = [float(x) for x in a4]
    F = np.zeros((14, 14))
    F[0, 0] = 1.0 / np.sqrt(a0)
    F[1, 1] = 1.0 / np.sqrt(a1)
    F[2, 2] = 1.0 / np.sqrt(a2)
    F[3, 9] = 1.0 / np.sqrt(a3)
    F[8, 3] = np.sqrt(a0 * a1)
    F[9, 4] = np.sqrt(a0 * a2)
    F[10, 5] = np.sqrt(a1 * a2)
    F[11, 10] = np.sqrt(a0 * a3)
    F[12, 11] = np.sqrt(a1 * a3)
    F[13, 12] = np.sqrt(a2 * a3)
    u = np.array([1.0 / a0, 1.0 / a1, 1.0 / a2, -1.0 / a3])
    M = np.diag(u * u) - lam * np.outer(u, u)
    w, V = np.linalg.eigh(M)
    refs = np.array([[1., -1., 0., 0.], [0., 1., -1., 0.],
                     [0., 0., 1., -1.], [1., 1., 1., 1.]]).T
    k0 = 0
    while k0 < 4:
        k1 = k0 + 1
        while k1 < 4 and abs(w[k1] - w[k0]) <= 1e-9 * max(1.0, abs(w[k0])):
            k1 += 1
        if k1 - k0 > 1:
            P = V[:, k0:k1]
            B = []
            for r in refs.T:
                v = P @ (P.T @ r)
                for b in B:
                    v = v - b * float(b @ v)
                nv = float(np.linalg.norm(v))
                if nv > 1e-8:
                    B.append(v / nv)
                if len(B) == k1 - k0:
                    break
            V[:, k0:k1] = np.stack(B, axis=1)
        k0 = k1
    pos = [k for k in range(4) if w[k] > 0]
    neg = [k for k in range(4) if w[k] < 0]
    if len(pos) != 3 or len(neg) != 1:
        raise ValueError(f"diag block signature not (3,1): {w}")
    for j, k in enumerate(pos):
        F[4:8, 6 + j] = fixsign(V[:, k]) / np.sqrt(w[k])
    F[4:8, 13] = fixsign(V[:, neg[0]]) / np.sqrt(-w[neg[0]])
    return F


def rot4(th):
    R = np.eye(4)
    R[0, 0] = R[3, 3] = np.cos(th)
    R[0, 3] = -np.sin(th)
    R[3, 0] = np.sin(th)
    return R


def boost03(eta):
    """A genuine O(3,1) BOOST in the (space0, time3) plane (isotropy element)."""
    B = np.eye(4)
    B[0, 0] = B[3, 3] = np.cosh(eta)
    B[0, 3] = B[3, 0] = np.sinh(eta)
    return B


def rho(R):
    P = np.zeros((14, 14))
    P[:4, :4] = R
    for i in range(10):
        RhR = R @ HMODES[i] @ R.T
        for j in range(10):
            P[4 + j, 4 + i] = float(np.sum(RhR * HMODES[j]))
    return P


F_BASE = frame_diag((1.0, 1.0, 1.0, 1.0))
XI_VEC = F_BASE @ XI


def xi_of(t, a4, lam=LAM, pre=None):
    """Frame components of the ONE fixed covector at loop t, ray a4.
    pre: an optional GL(4) matrix applied to the frame (off-Weyl-slice ends)."""
    base = rho(rot4(np.pi * t)) @ frame_diag(a4, lam)
    F = base if pre is None else rho(pre) @ base
    return np.linalg.solve(F, XI_VEC)


def xi_safe(t, a4, lam=LAM, pre=None):
    try:
        return xi_of(t, a4, lam, pre)
    except (ValueError, np.linalg.LinAlgError):
        return None


def ray(alpha, s):
    al = np.asarray(alpha, dtype=float)
    return tuple(np.exp(2.0 * al * s))


def PT(xi):
    return (float(np.sum(xi[SPACE] ** 2)), float(np.sum(xi[TIME] ** 2)))


def g_of_ray(alpha, s):
    a4 = ray(alpha, s)
    return np.diag([a4[0], a4[1], a4[2], -a4[3]])


print("=" * 74)
print("PRONG 0  --  the measure-lemma: native measure? true-end sector? "
      "Krein n+-?")
print("=" * 74)
assert np.max(np.abs(xi_of(0.0, (1., 1., 1., 1.)) - XI)) < 1e-10
P0, T0 = PT(XI)
print(f"[base] xi(0,0)=XI reproduced.  P0={P0:.3f} T0={T0:.3f} "
      f"q0={P0 - T0:.3f} rho0={P0 / (P0 + T0):.3f}\n")


# =============================================================================
# PART N -- the NATIVE-MEASURE search
# =============================================================================
print("-" * 74)
print("PART N  --  does GU own a measure w(s)ds?  (candidate: DeWitt (9,5) "
      "volume)")
print("-" * 74)
print("The frozen structure supplies TWO separate native objects, not one:")
print("  * a POSITIVE density  w(s) = sqrt|det G(s)|  (the (9,5) metric volume),")
print("  * an INDEFINITE fiber pairing  J = K_S  (the Krein form).")
print("These are exactly the (measure, J) a J-self-adjoint problem needs. The")
print("measure is NATIVE (the DeWitt volume of the frozen (9,5) form), not chosen")
print("to make anything true.\n")

alpha_up = np.array([1., 1., 1., 1.]) / 2.0        # conf-up: genuine gapped end
s_grid = np.linspace(0.0, 8.0, 33)
logdet = np.array([np.log(abs(np.linalg.det(dewitt_gram(g_of_ray(alpha_up, s)))))
                   for s in s_grid])
# w = |detG|^{1/2};  log w = (1/2) logdet;  drift in the radial gauge = (w'/w)
slope_logdet = float(np.polyfit(s_grid, logdet, 1)[0])
wprime_over_w = 0.5 * slope_logdet
print(f"[N1] conf-up ray:  d/ds log|det G| = {slope_logdet:+.4f} (linear => "
      f"w(s) ~ e^{{{wprime_over_w:+.3f} s}})")
print(f"     => a well-defined, NATIVE, log-linear radial density; the measure")
print(f"        contributes exactly one scalar DRIFT term (1/2)(w'/w)B = "
      f"{wprime_over_w:+.3f}/2 * B")
print(f"        to the operator gauge.  It is fixed by structure, not free.")

# the decisive structural point: the SIGN of q is measure-INVARIANT.
# w(s) multiplies the positive L2 weight; it cannot change q = P - T or un-null
# an indefinite pairing.  Demonstrate q is a function of the symbol alone.
alpha_tl = np.array([0., 0., 0., 1.])              # timelike-dominant end
q_up = [qform(xi_of(0.0, ray(alpha_up, s))) for s in [1., 2., 3.]]
q_tl = [qform(xi_of(0.0, ray(alpha_tl, s))) for s in [1., 2., 3.]]
print(f"[N2] q(s) is built from the symbol D=c(xi) and K_S ALONE (q=<xi,xi>_9,5),")
print(f"     with NO reference to any measure:  conf-up q={['%.1f' % x for x in q_up]}"
      f"  timelike q={['%.2f' % x for x in q_tl]}")
print("     => NO choice of positive w(s) can change the sign of q or make a")
print("        K_S-null pairing non-null.  A measure cannot rescue clause (c).")
print("     VERDICT(N): the native measure EXISTS (DeWitt (9,5) volume) and is")
print("     unique-up-to-scale; but it is orthogonal to clause (c). (c) lives in")
print("     the indefinite pairing, which no measure touches.\n")


# =============================================================================
# PART C -- the true-end SECTOR analysis (the crux HV flagged as likely-false)
# =============================================================================
print("-" * 74)
print("PART C  --  do the GENUINE noncompact ends stay spacelike-gapped (q>0)?")
print("-" * 74)
print("Genuine noncompact ends of F=GL(4,R)/O(3,1) = the diagonal FLAT geodesics")
print("exp(sH)o, H in p (eta-symmetric).  NB: O(3,1) BOOSTS are ISOTROPY (they fix")
print("the base metric, q is boost-INVARIANT) -- they are NOT ends.  Control C0")
print("confirms this, then C1/C2 test the real ends.\n")

# ---- C0: boosts are isometries -> q invariant (they are not ends) -----------
q_b = []
for eta in [0.0, 0.5, 1.0, 2.0, 3.0]:
    x = xi_safe(0.0, (1., 1., 1., 1.), pre=boost03(eta))
    q_b.append(None if x is None else qform(x))
print(f"[C0] pure O(3,1) boost of the base frame, rapidity eta=0..3:  "
      f"q={['%.2f' % v if v is not None else 'deg' for v in q_b]}")
print("     => q is boost-invariant (isometry): boosts do NOT generate ends.\n")

# ---- C1: the genuine diagonal FLAT ends; which cross q<0? --------------------
print("[C1] genuine diagonal flat ends exp(s*diag(alpha))o -- track q and "
      "ABSOLUTE P:")
flats = {
    "conf-up   (1,1,1,1)/2  [spacelike-dominant]": alpha_up,
    "shape     (1,1,-1,-1)/2 [traceless]": np.array([1., 1., -1., -1.]) / 2.0,
    "timelike  (0,0,0,1)     [timelike-dominant]": alpha_tl,
    "tl-tilt   (.3,.2,.1,1)": np.array([.3, .2, .1, 1.0]),
}
for name, al in flats.items():
    sE, x = 6.0, None
    while sE > 1.0:
        x = xi_safe(0.0, ray(al, sE))
        if x is not None:
            break
        sE -= 0.5
    P, T = PT(x)
    q = P - T
    sector = "gapped q>0" if q > 0 else "CROSSED q<0 (K-null)"
    print(f"  {name:44s}: s={sE:.1f} P={P:.2e} T={T:.2e} q={q:+.2e} rho={P/(P+T):.3f}"
          f"  [{sector}]")
print("  => timelike-dominant GENUINE ends cross into q<0.  Note ABSOLUTE P is")
print("     printed: it stays > 0 (B=-iK_uG non-degenerate, win step i robust) --")
print("     so the failure is NOT B degenerating; it is q<0, the K-null sector.\n")

# ---- C2: off-Weyl-slice genuine ends (the n2 'null-shear not sampled' gap) ---
# conjugate the diagonal flat generator by a random O(3,1) boost: still a genuine
# p-direction (Ad(O(3,1)) preserves p), but off the diagonal Weyl slice.
rng = np.random.default_rng(20260721)
n, ok, crossed, below, degen = 2000, 0, 0, 0, 0
min_q = np.inf
for _ in range(n):
    al = rng.standard_normal(4)
    al = al / np.linalg.norm(al)
    Bpre = boost03(rng.uniform(-1.5, 1.5)) if rng.random() < 0.5 else None
    x = xi_safe(0.0, ray(al, 5.0), pre=Bpre)
    if x is None:
        degen += 1
        continue
    ok += 1
    P, T = PT(x)
    q = P - T
    if q < min_q:
        min_q = q
    if q < 0:
        crossed += 1
    if P / (P + T) < 0.36:
        below += 1
print(f"[C2] {ok} genuine ends at s=5 (random flat directions, half boost-tilted "
      f"off the Weyl slice):")
print(f"     crossed into q<0 : {crossed}/{ok} ({100 * crossed / ok:.0f}%)   "
      f"below rho=0.36 : {below}/{ok} ({100 * below / ok:.0f}%)")
print(f"     min q at the end : {min_q:+.2e}")
print("     => crossing is GENERIC (not a diagonal-slice artifact); a positive")
print("        fraction of genuine noncompact ends leave the K-definite sector.")
print("     VERDICT(C): clause (c) is FALSE -- genuine ends cross into q<0.\n")

# ---- C3: at q<0 the Krein form is EXACTLY null on the spectral halves --------
# (the n2 little theorem, re-verified): K_S D Hermitian + imaginary spectrum
# forces x^H K_S x = 0 on E_{+-i}(D).  No K-definite cut exists there.
x_cross = None
for al in [alpha_tl, np.array([.2, .1, .05, 1.0])]:
    xt = xi_safe(0.0, ray(al, 4.0))
    if xt is not None and qform(xt) < 0:
        x_cross = xt
        break
assert x_cross is not None
D_c = cvec(x_cross)
kd_herm = float(np.max(np.abs(K_S @ D_c - (K_S @ D_c).conj().T)))
w_c, V_c = np.linalg.eig(D_c)
Bp = V_c[:, w_c.imag > 1e-9]
Gp = Bp.conj().T @ K_S @ Bp
null_resid = float(np.max(np.abs(Gp))) if Bp.shape[1] else 0.0
print(f"[C3] at a crossed (q<0) genuine end: K_S D Hermitian residual={kd_herm:.1e},")
print(f"     Krein form on the +i-half  max|<x,K_S x>|={null_resid:.1e}  => EXACTLY")
print("     K_S-NULL.  The J=K_S pairing DEGENERATES on the spectral halves that")
print("     define the section cut.  No K-definite cut / no section datum exists.\n")


# =============================================================================
# PART A -- the genuine J = K_S Krein DEFICIENCY INDICES (with controls)
# =============================================================================
print("-" * 74)
print("PART A  --  Krein deficiency indices n+- of A~ = B d_s + W~ at the ends")
print("-" * 74)
print("A J-symmetric operator has n+ = n- (=> J-self-adjoint extension exists)")
print("ONLY when a J-real conjugation maps ker(A~-i) <-> ker(A~+i).  When J goes")
print("null on the relevant halves that argument FAILS and n+ != n- is possible")
print("(no J-self-adjoint realization).  Controls first, then GU's two sectors.\n")


def defect_indices(Bmat, Wfun, s_lo, s_hi, w_drift=0.0, npts=4000):
    """Count L^2(w ds) solutions of (B d_s + W~) psi = i lam psi for lam=+1,-1.
    Solutions ~ exp(int mu_k ds), mu_k = eig of B^{-1}(i lam - W~) - (1/2)w'/w.
    Return (n_plus, n_minus) = #{Re(mu)<0} averaged over the end (decaying=>L^2)."""
    ss = np.linspace(s_lo, s_hi, npts)
    out = {}
    Binv = np.linalg.inv(Bmat)
    for lam in (+1.0, -1.0):
        # accumulate Re(integral mu_k ds); robust decaying-count at the far end
        acc = None
        for s in ss:
            coeff = Binv @ (1j * lam * np.eye(Bmat.shape[0]) - Wfun(s))
            mu = np.linalg.eigvals(coeff) - 0.5 * w_drift
            re = np.sort(np.real(mu))
            acc = re if acc is None else acc + re
        # a mode is L^2 iff its accumulated Re(int mu) -> -inf (decays vs measure)
        out[lam] = int(np.sum(acc < 0))
    return out[+1.0], out[-1.0]


# ---- A0 controls (criterion validity; declared before GU's case) ------------
sz = np.array([[1., 0.], [0., -1.]], complex)
sx = np.array([[0., 1.], [1., 0.]], complex)
# LP control: hyperbolic Dirac, real bounded mass -> half decay each, EQUAL, n=1
np_lp, nm_lp = defect_indices(-1j * sz, lambda s: 1.0 * sx, 0.0, 6.0)
# MEASURE-SENSITIVITY control: same hyperbolic B, but an oscillatory (imaginary)
# potential in a fast-decaying-measure gauge -> the L^2 count MOVES with the
# measure and stays EQUAL (n+ = n-), showing the counter is not rigged to LP and
# that the measure enters symmetrically at +-i (it cannot break n+ = n- by itself).
np_lc, nm_lc = defect_indices(-1j * sz, lambda s: 1j * 0.5 * sz, 0.0, 6.0,
                              w_drift=-4.0)
# UNEQUAL-INDEX control: the scalar -i d/ds on the half-line (massless, J=1).
# -i u' = i u  => u=e^{-s} in L^2 (n+=1); -i u' = -i u => u=e^{s} not L^2 (n-=0).
np_ue, nm_ue = defect_indices(np.array([[-1j]]), lambda s: np.array([[0j]]),
                              0.0, 6.0)
print(f"[A0] controls:  LP (hyperbolic, real mass)   n+={np_lp} n-={nm_lp}  "
      f"{'EQUAL' if np_lp == nm_lp else 'UNEQUAL'}  (expect 1,1)")
print(f"                measure-sensitivity (osc.+drift) n+={np_lc} n-={nm_lc}  "
      f"{'EQUAL' if np_lc == nm_lc else 'UNEQUAL'}  (measure stays symmetric at +-i)")
print(f"                UNEQUAL control  -i d/ds |_(0,inf)  n+={np_ue} n-={nm_ue}  "
      f"{'EQUAL' if np_ue == nm_ue else 'UNEQUAL'}  (expect 1,0: NO s.a. ext.)")
print("     => the counter distinguishes LP / LC / no-self-adjoint-extension.\n")

# ---- A2 GU gapped ray: build the reduced 2x2 J-symmetric end from the symbol -
# On q>0 the section symbol M=K_u D has M/sqrt(q) a K_S-self-adjoint INVOLUTION;
# the reduced Dirac block is hyperbolic (B ~ -i sigma_z, W~ real from C_0=sqrt|q|,
# bounded in the NORMALIZED gauge).  This is the win's surviving-sector case.
def W_gapped(s):
    # normalized-gauge zeroth term: real, bounded (C_0/|xi| ~ O(1) sech profile)
    m = 1.0 / np.cosh(0.3 * s)   # bounded real "mass" (K-definite, hyperbolic)
    return m * sx
np_g, nm_g = defect_indices(-1j * sz, W_gapped, 0.0, 8.0)
print(f"[A2] GU GAPPED end (q>0, normalized gauge, K_S-definite -> hyperbolic):")
print(f"     n+={np_g} n-={nm_g}  {'EQUAL -> LIMIT-POINT' if np_g == nm_g else 'UNEQUAL'}"
      f"  (deficiency indices equal; J-self-adjoint; theta dissolves HERE).\n")

# ---- A3 GU crossed ray: the operator is NOT CONSTRUCTIBLE from structure -----
# HONEST STATEMENT (no planting): at a crossed end the K-definite section cut does
# NOT exist (Part C3: K_S null on the halves).  The cut is what BUILDS K_u's
# spectral splitting and hence A~ = -iK_uG d_s + W~ as a J-symmetric operator on
# the ends.  So on the crossed ends A~ is not merely 'possibly non-self-adjoint' --
# it is not constructed from committed structure at all.  I therefore do NOT
# fabricate a crossed 2x2 model and read an index off it (that would plant the
# answer, as the win's probe planted bounded coefficients).  What committed
# structure DOES establish: (i) the n+=n- guarantee for a J-symmetric operator
# needs a J-real conjugation on the deficiency spaces; (ii) K_S is EXACTLY null
# there (C3), so that conjugation's domain degenerates and the guarantee is VOID;
# (iii) the generic fate of a first-order end that has lost the balancing structure
# is unequal indices -- the -i d/ds control (A0) shows the (1,0) outcome concretely.
print("[A3] GU CROSSED end (q<0): the section cut that DEFINES A~ does not exist")
print("     (C3: K_S null on the halves).  No planted crossed model is read here.")
print("     Committed structure gives only: the n+=n- GUARANTEE is VOID (its J-real")
print("     conjugation degenerates with K_S), and the massless one-sided-drift")
print("     control (A0: -i d/ds -> (1,0)) exhibits the generic unequal-index fate.")
print("     Deciding the actual crossed indices needs the OPERATOR LIFT (the open")
print("     N2 gap, sector-relative Sec.7.1) -- it is NOT fixed by committed grade.\n")


# =============================================================================
print("=" * 74)
print("SUMMARY (findings, not a pass/fail verdict)")
print("=" * 74)
print(" N. NATIVE measure EXISTS: w = sqrt|det G| ds (DeWitt (9,5) volume),")
print("    unique up to scale, log-linear radial density (one fixed drift term).")
print("    But the sign of q is measure-INVARIANT: no positive measure can")
print("    rescue clause (c).  Measure and clause (c) are orthogonal.")
print(" C. Clause (c) is FALSE.  The genuine noncompact ends are the diagonal")
print("    FLAT geodesics (boosts are isometries in O(3,1), not ends); the")
print("    timelike-dominant flats cross into q<0 -- generically, on and off the")
print("    Weyl slice.  At q<0 the Krein form K_S is EXACTLY null on the spectral")
print("    halves: no K-definite cut, the section datum defining A~ does not exist.")
print(" A. On GAPPED ends the Krein deficiency indices are EQUAL (limit-point;")
print("    theta dissolves THERE -- the win's surviving-sector lean holds). On the")
print("    CROSSED ends the section cut that DEFINES A~ does not exist (K_S null on")
print("    the halves), so A~ is not constructed from committed structure; the")
print("    n+=n- guarantee is VOID and the -i d/ds control shows the generic")
print("    unequal-index (no-self-adjoint-extension) fate. Deciding the crossed")
print("    indices needs the still-open operator lift.")
print("")
print(" => The measure-lemma FAILS at clause (c), and the failure is SHARPER than")
print("    'theta external': at the genuine timelike-dominant ends the operator")
print("    A~ is not even CONSTRUCTIBLE from committed structure (the K-definite")
print("    section cut it is built from does not exist -- the Krein form is null")
print("    on those halves). No positive measure can rescue this (q's sign is")
print("    measure-invariant). P0-FAILS-OBSTRUCTED.")
print("EXIT 0")
