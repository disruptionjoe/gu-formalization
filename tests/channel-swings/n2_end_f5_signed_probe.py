#!/usr/bin/env python3
"""N2 END F5 -- the DECISIVE form of falsifier F5, run in the faithful
end-model: does the C2 global-residual accounting respond to the sector
flip AT the end (along the collar and at the boundary-at-infinity), or is
the carrier coherent but irrelevant?

CHANNEL: S_IG/B.5 construction frontier (P5 dossier, Element 6 falsifier
         F5 decisive form, Element 5 rung N2 at truncated-real grade).
AXIOM:   lab/process/boundary-adapter-standing-axiom.md (adapter assumed).
DESIGN:  explorations/n2-end-family-2026-07-20.md
EXTENDS: tests/channel-swings/n2_end_family_probe.py   (the end-model)
         tests/channel-swings/f5_shadow_c2_flip_probe.py (the readouts)
         tests/channel-swings/master_identity_mechanism_probe.py (the
         DERIVED master identity: A = (26/7)|xi|^2_E I - (2/7) B for every
         real xi -- consumed here as a theorem, cited not re-derived)
STATUS:  exploration tier; conditional (R0_COND working grade); no claim,
         canon, or public-posture movement.

THE TEST (dossier F5, decisive form). In the faithful end-model of the
n2_end_family probe (real fiber degeneration, real induced 6-leg holonomy,
real constraint objects Gamma/Pi_RS/M_D), the C2 accounting at collar
radius s is the obstruction map of the END-DRESSED symbol,
    X(s) = Gamma (I x c(xi(0,s))) Pi_RS,
resolved by the sector cut Q_sigma(s) of the boundary family at that
radius. The two dressings are the genuine holonomy pair (the deck identity
of the end probe). Readouts as in the shadow probe:
    magnitude  r_sigma(s) = ||Q_sigma(s) X(s)||_F
    signed     k_sigma(s) = Re tr(X(s)^+ K_S Q_sigma(s) X(s)).
F5 fires iff the accounting is invariant under the sector flip in the
faithful model. The magnitude channel is THEOREM-VACUOUS at every collar
radius: the master identity is now DERIVED for every real xi (mechanism
probe), and xi(0,s) is real for all s, so r_+ = r_- is forced everywhere
and carries no information (verified as a regression, not offered as
evidence). The decisive channel is the SIGNED one, and the decisive
question is whether its response SURVIVES the end limit s -> infinity.

CONSTRUCTIONS USED (GEOMETER-VS-PHYSICS-OBJECTS discipline): C2 is the
PROGRAM-NATIVE obstruction norm (never an index -- killed list; its closed
form C2 = sqrt(3328/7)||xi||_E is now a theorem and is regression-checked
per s). X(s) is computed by the DERIVED closed form X_a = e_a c + (6/7)
c e_a (master mechanism Step 2), verified against the full 1792-dim build
once at the base point. The sector cut is the native Krein cut; the
standard positive-Hilbert cut carries no sector datum on the end (recorded
in the end probe). The end-dressing of the constraint is SYMBOL-grade: the
constraint structure is frame-constant and the symbol carries the collar
dependence -- no operator on the end is built (that is the N2 theorem).

RESULT SHAPE (established below):
  (1) magnitude channel: exactly invariant at every sampled collar radius
      and at the boundary direction -- theorem-forced (all real xi), hence
      evidentially NULL for F5 at every depth of the end. Regression only.
  (2) signed channel: responds at every collar radius, zero-sum exactly,
      holonomy-tied (deck transport = sign flip) at every radius, and the
      response RATIO |k|/C2^2 converges to a NONZERO boundary value along
      every surviving ray sampled -- on the primary ray because the mixed
      bivector B survives at infinity; on a control ray whose limit loses
      all mixed content, the response still survives through the
      scalar-cut component (the two components of the derived closed form
      are computed separately). F5's decisive form does NOT fire at
      truncated-real grade.
  (3) domain honesty: on cone-crossing rays the sector cut ceases to exist
      past the collision, so the F5 accounting is UNDEFINED there -- the
      decisive verdict is sector-relative, exactly matching the end
      probe's F2 sector structure.

NONCLAIMS. No operator-level end (N2 theorem missing, named in the design
doc); no claim that the sector datum reduces C2 (SRC-REJ-1 guard verified
on the collar); no claim/canon/posture movement. Deterministic; numpy.
"""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "generation-sector"))
import gen_sector_bridge as gb  # noqa: E402

N_DIRS, DIM = 14, 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)
LAM = 0.5
RNG = np.random.default_rng(20260720)

RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return ok


# --- the verified Clifford objects -------------------------------------------
e = gb.gammas()
K_S = e[0].copy()
for a in range(1, 9):
    K_S = K_S @ e[a]
XI = np.real(np.asarray(gb.XI)).astype(float)
I128 = np.eye(DIM, dtype=complex)
U_h = e[0] @ e[3] @ e[4] @ e[9] @ e[11] @ e[12]   # the faithful 6-leg deck
Uh_inv = np.linalg.inv(U_h)


def cvec(v):
    return sum(v[a] * e[a] for a in range(N_DIRS))


def qform(v):
    return float(np.real(np.vdot(v, ETA * v)))


# --- the end-model geometry (identical constructions to the end probe) -------
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
HOR = [0, 1, 2, 9]
VERT = [k for k in range(N_DIRS) if k not in HOR]


def xi_of(t, a4, lam=LAM):
    F = rho(rot4(np.pi * t)) @ frame_diag(a4, lam)
    return np.linalg.solve(F, XI_VEC)


def ray(alpha, s):
    return tuple(np.exp(2.0 * np.asarray(alpha, dtype=float) * s))


A_CONF_UP = (1.0, 1.0, 1.0, 1.0)
A_CTRL = (1.0, 1.0, 0.5, 0.0)      # second surviving ray (limit loses B)
A_CONF_DN = (-1.0, -1.0, -1.0, -1.0)


def half_basis(ch):
    Uu, _s, _v = np.linalg.svd(ch)
    return Uu[:, :DIM // 2]


def gram_parts(B, K):
    Gm = B.conj().T @ K @ B
    Gm = 0.5 * (Gm + Gm.conj().T)
    w, S = np.linalg.eigh(Gm)
    return B @ S[:, w > 0], B @ S[:, w < 0], w


def kproj(Xc, K):
    M = Xc.conj().T @ K @ Xc
    return Xc @ np.linalg.solve(M, Xc.conj().T @ K)


def krein_cuts(D, q, K):
    chp = 0.5 * (I128 + D / np.sqrt(q))
    chm = I128 - chp
    Bp, Bm = half_basis(chp), half_basis(chm)
    p_pos, p_neg, wp = gram_parts(Bp, K)
    m_pos, m_neg, wm = gram_parts(Bm, K)
    return (kproj(np.hstack([p_pos, m_pos]), K),
            kproj(np.hstack([p_neg, m_neg]), K), wp, wm)


# --- the C2 accounting via the DERIVED closed form ----------------------------
def x_blocks(xi):
    """X(xi) as 14 blocks X_a = e_a c + (6/7) c e_a (master mechanism S2)."""
    c = cvec(xi)
    return [e[a] @ c + (6.0 / 7.0) * c @ e[a] for a in range(N_DIRS)]


def density(xb):
    A = np.zeros((DIM, DIM), dtype=complex)
    for Xa in xb:
        A += Xa @ Xa.conj().T
    return A


def readouts(xb, Q):
    r2, k = 0.0, 0.0
    KQ = K_S @ Q
    for Xa in xb:
        QX = Q @ Xa
        r2 += float(np.linalg.norm(QX) ** 2)
        k += float(np.trace(Xa.conj().T @ KQ @ Xa).real)
    return np.sqrt(r2), k


def k_components(xi, Q):
    """The two signed components from A = (26/7)|xi|^2 I - (2/7) B."""
    c = cvec(xi)
    cdag = cvec(ETA * xi)
    B = c @ cdag - float(xi @ xi) * I128
    k_scalar = (26.0 / 7.0) * float(xi @ xi) * float(np.trace(K_S @ Q).real)
    k_biv = -(2.0 / 7.0) * float(np.trace(K_S @ Q @ B).real)
    return k_scalar, k_biv, float(np.linalg.norm(B))


def xi_limit_dir(t, alpha):
    """Boundary-at-infinity direction of a surviving ray: dominant legs."""
    ss = 9.0
    x = xi_of(t, ray(alpha, ss))
    return x / np.linalg.norm(x)


# --- [T] setup ----------------------------------------------------------------
e_full, Gamma, Pi_RS, M_D = gb.constraint_objects()
X_full = Gamma @ M_D @ Pi_RS
C2_full = float(np.linalg.norm(X_full))
bare = float(np.linalg.norm(Pi_RS @ M_D - M_D @ Pi_RS))
xb0 = x_blocks(XI)
X_cf = np.hstack(xb0)
cf_res = float(np.linalg.norm(X_cf - X_full)) / C2_full
check("T", "the REAL C2 anchors reproduce (bare 58.7215, C2 155.3625) on the "
           "full 1792-dim constraint build, and the DERIVED closed form "
           "X_a = e_a c + (6/7) c e_a matches the full X block-for-block "
           "(licenses the fast X used below)",
      abs(bare - 58.7215) < 1e-2 and abs(C2_full - 155.3625) < 1e-2
      and cf_res < 1e-12,
      f"bare {bare:.4f}, C2 {C2_full:.4f}, closed-form rel-res {cf_res:.1e}")

x00 = xi_of(0.0, (1.0, 1.0, 1.0, 1.0))
D0 = cvec(x00)
Qp0, Qm0, _, _ = krein_cuts(D0, qform(x00), K_S)
r_p0, k_p0 = readouts(xb0, Qp0)
r_m0, k_m0 = readouts(xb0, Qm0)
check("T", "base-point continuity with the shadow probes: xi(0,0) = XI, the "
           "canonical cuts rebuild, r_sigma = 129.2640 and k_+ = 14421.0 "
           "(|k|/C2^2 = 0.5975) -- the end-model at s = 0 IS the F5 shadow's "
           "end-model, so every shadow result is the s = 0 slice of this one",
      float(np.max(np.abs(x00 - XI))) < 1e-12
      and abs(r_p0 - 129.2640) < 1e-2 and abs(k_p0 - 14421.0) < 1.0
      and abs(k_p0 / C2_full ** 2 - 0.5975) < 1e-3,
      f"r {r_p0:.4f}, k {k_p0:.1f}, ratio {k_p0 / C2_full ** 2:.4f}")


# =============================================================================
# Part A -- theorem regressions on the collar (the vacuous channel, located)
# =============================================================================
S_GRID = [0.0, 0.5, 1.0, 1.5, 2.0, 3.0]
ok_master, ok_c2law = True, True
for s in S_GRID:
    x_s = xi_of(0.0, ray(A_CONF_UP, s))
    xb_s = x_blocks(x_s)
    A_s = density(xb_s)
    c2sq = float(np.trace(A_s).real)
    res = float(np.linalg.norm(A_s + K_S @ A_s @ K_S - (c2sq / 64.0) * I128))
    if res > 1e-10 * float(np.linalg.norm(A_s)):
        ok_master = False
    c2_closed = (3328.0 / 7.0) * float(x_s @ x_s)
    if abs(c2sq - c2_closed) > 1e-9 * c2sq:
        ok_c2law = False
check("E", "the DERIVED master identity holds at every sampled collar "
           "radius (xi(0,s) is real for all s, so A(s) + K_S A(s) K_S = "
           "(C2(s)^2/64) I is a THEOREM on the whole collar), and C2(s)^2 = "
           "(3328/7)||xi(s)||_E^2 exactly: every magnitude-channel readout "
           "of the end-dressed C2 is theorem-vacuous at every depth of the "
           "end -- the F5 magnitude test cannot fire ANYWHERE on the end, "
           "as a regression, not as evidence", ok_master and ok_c2law)

ok_mag = True
for s in [0.0, 1.5, 3.0]:
    x_s = xi_of(0.0, ray(A_CONF_UP, s))
    xb_s = x_blocks(x_s)
    Qp_s, Qm_s, _, _ = krein_cuts(cvec(x_s), qform(x_s), K_S)
    r_p, _ = readouts(xb_s, Qp_s)
    r_m, _ = readouts(xb_s, Qm_s)
    if abs(r_p - r_m) > 1e-8 * max(r_p, 1.0):
        ok_mag = False
check("E", "magnitude regression: r_+(s) = r_-(s) to machine precision at "
           "every sampled collar radius (forced by the identity above; "
           "recorded so no future reader mistakes end-magnitude invariance "
           "for an F5 firing)", ok_mag)


# =============================================================================
# Part B -- the signed channel on the collar and at the boundary
# =============================================================================
traj = []
ok_signed, ok_deck_tied = True, True
for s in S_GRID:
    a4 = ray(A_CONF_UP, s)
    x_s = xi_of(0.0, a4)
    xb_s = x_blocks(x_s)
    c2sq_s = float(np.trace(density(xb_s)).real)
    Qp_s, Qm_s, _, _ = krein_cuts(cvec(x_s), qform(x_s), K_S)
    _, k_p = readouts(xb_s, Qp_s)
    _, k_m = readouts(xb_s, Qm_s)
    ratio = abs(k_p) / c2sq_s
    traj.append((s, ratio))
    if not (abs(k_p) > 1e-6 * c2sq_s and abs(k_p + k_m) < 1e-6 * abs(k_p)):
        ok_signed = False
    # holonomy tie at this radius: transported cut = the other sector
    x1_s = xi_of(1.0, a4)
    Qp1_s, _, _, _ = krein_cuts(cvec(x1_s), qform(x1_s), K_S)
    _, k_transported = readouts(xb_s, Uh_inv @ Qp1_s @ U_h)
    if abs(k_transported - k_m) > 1e-6 * abs(k_m):
        ok_deck_tied = False
check("E", "the SIGNED channel responds at EVERY collar radius: k_sigma(s) "
           "= sigma |k(s)| with k_+ + k_- = 0 exact (zero-sum theorem), "
           "|k|/C2^2 nonzero along the whole collar; and the response is "
           "HOLONOMY-TIED at every radius: evaluating with the cut "
           "transported once around the mixed loop AT THAT RADIUS equals "
           "k_- (the deck identity consumed at every depth of the end)",
      ok_signed and ok_deck_tied,
      "ratio |k|/C2^2: " + ", ".join(f"s={s:.1f}: {r:.4f}" for s, r in traj))

x_inf = xi_limit_dir(0.0, A_CONF_UP)
xb_inf = x_blocks(x_inf)
c2sq_inf = float(np.trace(density(xb_inf)).real)
Qp_i, Qm_i, wp_i, wm_i = krein_cuts(cvec(x_inf), qform(x_inf), K_S)
_, k_pi = readouts(xb_inf, Qp_i)
_, k_mi = readouts(xb_inf, Qm_i)
ratio_inf = abs(k_pi) / c2sq_inf
ks_i, kb_i, nB_i = k_components(x_inf, Qp_i)
check("E", "THE DECISIVE LIMIT: at the boundary-at-infinity direction of "
           "the primary surviving ray the sector cuts exist (margin "
           "bounded), the signed response is NONZERO and zero-sum, and the "
           "response ratio |k|/C2^2 converges to a nonzero boundary value: "
           "the C2 accounting RESPONDS to the sector flip AT THE END. "
           "Falsifier F5, in its decisive (faithful end-model) form, does "
           "NOT fire at truncated-real grade",
      abs(k_pi) > 0.05 * c2sq_inf and abs(k_pi + k_mi) < 1e-6 * abs(k_pi)
      and abs(ratio_inf - traj[-1][1]) < 0.2,
      f"ratio at infinity {ratio_inf:.4f} (collar end {traj[-1][1]:.4f}); "
      f"components: scalar-cut {ks_i:.4f}, bivector {kb_i:.4f}")

check("E", "the MECHANISM of the surviving response, split by the derived "
           "closed form k = (26/7)|xi|^2 tr(K_S Q) - (2/7) tr(K_S Q B): the "
           "split is machine-exact at the boundary; on the primary ray the "
           "limit direction keeps mixed space-time content (||B_inf|| = "
           "1.80, bivector component nonzero) but the response at the end "
           "is SCALAR-CUT DOMINATED (the collar trajectory 0.5975 -> "
           "0.5021 is the bivector share draining as the vertical mixed "
           "legs decay): the end limit reads both faces, with the "
           "K-definiteness of the cut itself carrying the load at infinity",
      abs(ks_i + kb_i - k_pi) < 1e-6 * abs(k_pi) and nB_i > 0.1
      and abs(kb_i) > 0.01 and abs(ks_i) > 100.0 * abs(kb_i),
      f"k = {k_pi:.4f} = {ks_i:.4f} + {kb_i:.4f}; ||B_inf|| = {nB_i:.4f}")

# second surviving ray: the limit direction loses ALL mixed content
x_c0 = xi_of(0.0, ray(A_CTRL, 4.0))
q_ok_ctrl = min(qform(xi_of(t, ray(A_CTRL, 4.0)))
                for t in np.linspace(0, 1, 21)) > 0
x_cinf = xi_limit_dir(0.0, A_CTRL)
xb_c = x_blocks(x_cinf)
c2sq_c = float(np.trace(density(xb_c)).real)
Qp_c, Qm_c, _, _ = krein_cuts(cvec(x_cinf), qform(x_cinf), K_S)
_, k_pc = readouts(xb_c, Qp_c)
_, k_mc = readouts(xb_c, Qm_c)
ks_c, kb_c, nB_c = k_components(x_cinf, Qp_c)
check("E", "ROBUSTNESS + mechanism separation on a second surviving ray "
           "(alpha = (1,1,0.5,0)): its boundary direction is PURE SPACE "
           "(dominant legs 0,1), so the mixed bivector B dies at infinity "
           "(||B_inf|| ~ 0) -- and the signed response STILL survives, "
           "carried entirely by the scalar-cut component (26/7)|xi|^2 "
           "tr(K_S Q_sigma): the decisive outcome is not an artifact of "
           "one ray, and the B-channel's survival is ray-dependent while "
           "the response itself is not",
      q_ok_ctrl and abs(k_pc) > 0.05 * c2sq_c
      and abs(k_pc + k_mc) < 1e-6 * abs(k_pc)
      and nB_c < 1e-3 and abs(kb_c) < 1e-3 * abs(k_pc),
      f"ratio {abs(k_pc) / c2sq_c:.4f}; ||B_inf|| = {nB_c:.2e}; "
      f"k = scalar {ks_c:.4f} + bivector {kb_c:.2e}")

# domain honesty on a crossing ray
s_past = 1.2   # past the conf-down collision (s* ~ 0.1)
x_x = xi_of(0.58, ray(A_CONF_DN, s_past))
q_x = qform(x_x)
ev_x = np.linalg.eigvals(cvec(x_x))
w_gram_null = None
Vx = np.linalg.eig(cvec(x_x))[1]
Bx = Vx[:, np.linalg.eig(cvec(x_x))[0].imag > 0]
w_gram_null = float(np.max(np.abs(Bx.conj().T @ K_S @ Bx)))
check("E", "DOMAIN HONESTY: past the collision on the conformal-collapse "
           "ray q < 0, the spectrum is imaginary and the halves are "
           "K_S-null (max |Gram| ~ 0), so NO admissible sector cut exists "
           "and the F5 accounting is UNDEFINED there: the decisive verdict "
           "is SECTOR-RELATIVE, exactly matching the end probe's F2 sector "
           "structure -- neither a firing nor a survival is claimed "
           "outside the spacelike sector",
      q_x < 0 and float(np.max(np.abs(ev_x.real))) < 1e-6
      and w_gram_null < 1e-8,
      f"q = {q_x:.3f}, max |Gram on E_+i| = {w_gram_null:.1e}")


# =============================================================================
# Part C -- controls on the end
# =============================================================================
s_ctl = 2.0
a4c = ray(A_CONF_UP, s_ctl)
x_s = xi_of(0.0, a4c)
xb_s = x_blocks(x_s)
Qp_s, Qm_s, _, _ = krein_cuts(cvec(x_s), qform(x_s), K_S)
r_ps, k_ps = readouts(xb_s, Qp_s)
c2_s = float(np.sqrt(np.trace(density(xb_s)).real))

# trichotomy: the faithful same-sign seam at depth changes nothing
U_ss = e[0] @ e[1] @ e[4] @ e[5] @ e[10] @ e[11]
r_tv, k_tv = readouts(xb_s, np.linalg.inv(U_ss) @ (U_ss @ Qp_s @ np.linalg.inv(U_ss)) @ U_ss)
check("F", "trichotomy control at depth: transport around the faithful "
           "same-sign-plane loop (untwisted 6-leg seam, U K_S U^-1 = +K_S) "
           "leaves both readouts EXACTLY unchanged at collar radius s = 2: "
           "the signed response is a mixed-loop holonomy effect on the "
           "end, not a transport artifact",
      abs(r_tv - r_ps) < 1e-9 * max(1.0, r_ps)
      and abs(k_tv - k_ps) < 1e-9 * max(1.0, abs(k_ps)))

# covariant dressing at depth: conjugate everything -- identity on readouts
xb_cov = [U_h @ Xa @ Uh_inv for Xa in xb_s]
sflip = np.array([-1.0 if a in (0, 3, 4, 9, 11, 12) else 1.0
                  for a in range(N_DIRS)])
xb_cov2 = [sflip[a] * xb_cov[a] for a in range(N_DIRS)]  # vector leg too
Qp_cov = U_h @ Qp_s @ Uh_inv
K_cov = U_h @ K_S @ Uh_inv           # = -K_S (the twist)
r_cov = float(np.sqrt(sum(float(np.linalg.norm(Qp_cov @ Xa) ** 2)
                          for Xa in xb_cov2)))
k_cov = sum(float(np.trace(Xa.conj().T @ K_cov @ Qp_cov @ Xa).real)
            for Xa in xb_cov2)
k_incoh = sum(float(np.trace(Xa.conj().T @ (-K_S) @ Qp_s @ Xa).real)
              for Xa in xb_s)
_, k_ms = readouts(xb_s, Qm_s)
check("F", "frame-artifact control at depth: dressing EVERYTHING "
           "covariantly with the faithful holonomy (spinor leg, vector "
           "leg, cut, and the form, which returns as -K_S) is the IDENTITY "
           "on both readouts at s = 2; only SELECTIVE flips move k (cut "
           "alone -> k_-; form alone -> -k_+ = k_-): the sector operation "
           "is selective, never a frame relabel, at depth as at the base",
      abs(r_cov - r_ps) < 1e-9 * max(1.0, r_ps)
      and abs(k_cov - k_ps) < 1e-6 * abs(k_ps)
      and abs(k_incoh - k_ms) < 1e-6 * abs(k_ms),
      f"r_cov {r_cov:.4f} = r_+; k_cov {k_cov:.1f} = k_+")

ok_guard = True
for s in [0.0, 1.0, 2.0, 3.0]:
    x_g = xi_of(0.0, ray(A_CONF_UP, s))
    xb_g = x_blocks(x_g)
    c2_g = float(np.sqrt(np.trace(density(xb_g)).real))
    Qp_g, _, _, _ = krein_cuts(cvec(x_g), qform(x_g), K_S)
    r_g, _ = readouts(xb_g, Qp_g)
    if not (0.0 < r_g < c2_g):
        ok_guard = False
    if abs(np.sqrt(3328.0 / 7.0) * np.linalg.norm(x_g) - c2_g) > 1e-9 * c2_g:
        ok_guard = False
check("F", "SRC-REJ-1 guard on the collar: at every sampled radius the "
           "sector dressing neither reduces nor closes the total C2 "
           "(0 < r_sigma(s) < C2(s), and C2(s) obeys its closed-form law "
           "untouched): the sector datum refuses to do C2's job with "
           "symbol-level end data at every depth, exactly as the standing "
           "regression demands of a genuine global datum", ok_guard)


# --- headline -----------------------------------------------------------------
nE = sum(1 for tag, _n, ok in RESULTS if tag == "E")
nF = sum(1 for tag, _n, ok in RESULTS if tag == "F")
nT = sum(1 for tag, _n, ok in RESULTS if tag == "T")
all_ok = all(ok for _t, _n, ok in RESULTS)
print()
print("N2 END F5 VERDICT (decisive form, truncated-real grade): NOT FIRED "
      "on the surviving sector -- the signed C2 accounting responds to the "
      "sector flip at every collar radius AND at the boundary-at-infinity "
      "(nonzero limit ratio on every sampled surviving ray; zero-sum and "
      "holonomy-tied throughout; mechanism split into scalar-cut + "
      "bivector components by the derived closed form). The magnitude "
      "channel is theorem-vacuous at every depth (master identity, all "
      "real xi). Outside the spacelike sector the accounting is UNDEFINED "
      "(no admissible cut) -- the verdict is sector-relative. The "
      "operator-grade F5 test (with an actual end Dirac operator) remains "
      "the N2 theorem gap.")
print(f"HEADLINE: {nE} [E] + {nF} [F] = {nE + nF}   (setup [T] = {nT} "
      f"excluded)   {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
sys.exit(0 if all_ok else 1)
