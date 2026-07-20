#!/usr/bin/env python3
"""OPERATOR-GRADE FACE (Q-C, summit wave 2026-07-20) -- the V-breaking
crack, tested: add HONEST Clifford-even connection terms (the bicomplex
fixture's so(9,5) generators Sigma_ab, a-priori named W, never read from
xi) to the scattering family and ask whether the ghost-conjugation
protection V = sigma2 x omega breaks as predicted, and if so whether a
SECTOR-ODD traced scattering functional actually appears -- or whether
the surviving mechanisms keep the bit blind.

CHANNEL: big swing (Joe direct chat, 2026-07-20: operator-grade end family,
         stage 3).
DESIGN:  explorations/operator-grade-end-2026-07-20.md (Section 0, branch
         Q-C, pre-declared before computation).
EXTENDS: imports the summit-wave machinery from operator_grade_end_probe
         (same conventions); replicates the smatrix scattering builder
         (that file is not touched) with the closed-form step generalized
         to a full matrix exponential (the dressed A^2 is no longer
         scalar); tests/rs_bicomplex_spin95_connection_2form.py is the
         verified source of the Sigma_ab = (1/4)[e_a, e_b] connection
         coefficients (its carrier convention, replicated).

THE DRESSING (K-honest, placement named): the Clifford-even term enters
the SYMBOL channel, D(x) -> sigma1 x (c(xi(x)) + i kappa B), B =
sigma_c(W) = sum W_ab Sigma_ab. The factor i makes the dressed symbol
K_S-self-adjoint for EVERY so(9,5) W (Sigma_ab is K_S-pseudo-anti-
Hermitian). The covariant-derivative placement (I2 x B added to the
propagation) COMMUTES with V and is run as a control: the crack lives in
the symbol channel only. W is chosen a-priori by J-parity class (both
classes run: a T-invariant dressing, J (i B) J^-1 = +iB, is the headline
-- the Kramers no-go's hypotheses stay intact there).

REFINEMENT DISCIPLINE: the window segmentation nseg is the resolution;
every headline functional carries an nseg in {24, 48, 96} convergence
column. Deterministic; numpy + scipy; no RNG.
"""
from __future__ import annotations

import sys
import time

import numpy as np
from scipy.linalg import expm

import operator_grade_end_probe as P

e, K_S, I128, OM, C_J = P.e, P.K_S, P.I128, P.OM, P.C_J
U_ss, U_h = P.U_ss, P.U_h
cvec, qform, xi_of, ray = P.cvec, P.qform, P.xi_of, P.ray
A_CONF_DN = P.A_CONF_DN
S1, S2, I2 = P.S1, P.S2, P.I2
RESULTS = P.RESULTS
check, log = P.check, P.log
T0 = time.time()

I256 = np.eye(256, dtype=complex)
GAM = 1j * np.kron(S2, I128)
V_GH = np.kron(S2, OM)
W_OM = np.kron(I2, OM)
CJt = np.kron(I2, C_J)
X1 = np.kron(S2, K_S)


def dbl(D):
    return np.kron(S1, D)


def Sigma(a, b):
    return 0.25 * (e[a] @ e[b] - e[b] @ e[a])


def jpar(B):
    """J_quat parity of B: +1 if C conj(B) C^-1 = +B, -1 if = -B, 0 else."""
    JB = C_J @ np.conj(B) @ np.linalg.inv(C_J)
    if float(np.max(np.abs(JB - B))) < 1e-10:
        return +1
    if float(np.max(np.abs(JB + B))) < 1e-10:
        return -1
    return 0


# J-parity census of the so(9,5) generators. i B is J-EVEN (T-invariant
# dressing) iff jpar(B) = -1.  FINDING (run before the batteries): ALL 91
# generators are J-REAL (jpar = +1) -- the quaternionic structure fixes
# the whole real Clifford algebra -- so EVERY K-honest symbol-channel
# Clifford-even dressing i kappa B is FORCED J-ODD (explicitly
# T-violating), while the T-invariant even dressing exists only in the
# covariant-derivative placement, which COMMUTES with V. The V-crack and
# the Kramers hypothesis are mutually exclusive by algebra.
pairs_jreal = [(a, b) for a in range(14) for b in range(a + 1, 14)
               if jpar(Sigma(a, b)) == +1]
check("E", "FORCED T-PARITY (structural finding): all 91 Sigma_ab are "
           "J_quat-real, hence every K_S-self-adjoint symbol-channel even "
           "dressing (i kappa B) is J-ODD -- opening the V-crack costs "
           "explicit T-violation in the family; the T-invariant placement "
           "(covariant derivative, no i) is exactly the V-commuting one",
      len(pairs_jreal) == 91, f"J-real generators: {len(pairs_jreal)}/91")

# named a-priori connection, fixture style (one boost leg pair + one
# compact rotation pair); never reads xi
B_EVEN = 1.0 * Sigma(0, 9) + 0.7 * Sigma(1, 2)

ksa = float(np.max(np.abs(
    K_S @ (1j * B_EVEN).conj().T @ K_S - 1j * B_EVEN)))
vanti = float(np.max(np.abs(
    V_GH @ np.kron(S1, 1j * B_EVEN) + np.kron(S1, 1j * B_EVEN) @ V_GH)))
vcomm_cd = float(np.max(np.abs(
    V_GH @ np.kron(I2, B_EVEN) - np.kron(I2, B_EVEN) @ V_GH)))
check("T", "the crack is real at the algebra level: i B is K_S-self-"
           "adjoint (honest family member), the SYMBOL-channel dressing "
           "sigma1 x iB ANTI-commutes with V (protection broken exactly as "
           "the smatrix doc predicted), while the covariant-derivative "
           "placement I2 x B COMMUTES with V (that placement cannot open "
           "a face -- control)",
      ksa < 1e-12 and vanti < 1e-12 and vcomm_cd < 1e-12,
      f"K-sa {ksa:.1e}; V-anticomm (symbol) {vanti:.1e}; "
      f"V-comm (cov-der) {vcomm_cd:.1e}")


# --- scattering builder (smatrix conventions, expm step) -----------------------
def window_of(a4, nseg, pad=0.12):
    tg = np.linspace(0.0, 1.0, 201)
    qs = np.array([qform(xi_of(float(t), a4)) for t in tg])
    tneg = tg[qs < 0]
    t_lo, t_hi = float(tneg.min() - pad), float(tneg.max() + pad)
    xg = np.linspace(t_lo, t_hi, nseg + 1)
    xm = 0.5 * (xg[:-1] + xg[1:])
    h = float(xg[1] - xg[0])
    Ds = [cvec(xi_of(float(t), a4)) for t in xm]
    return dict(t_lo=t_lo, t_hi=t_hi, h=h, xm=xm, Ds=Ds,
                D_L=cvec(xi_of(t_lo, a4)), q_L=qform(xi_of(t_lo, a4)),
                D_R=cvec(xi_of(t_hi, a4)), q_R=qform(xi_of(t_hi, a4)))


def transfer(win, E, kappa, B, sgn=+1.0, place="symbol"):
    T = I256
    for D in win["Ds"]:
        if place == "symbol":
            A = -dbl(sgn * D + 1j * kappa * B) - E * GAM
        else:  # covariant-derivative placement control
            A = -dbl(sgn * D) - E * GAM + kappa * np.kron(I2, B)
        T = expm(win["h"] * A) @ T
    return T


def modes_gen(D_end, E, kappa, B, sgn=+1.0):
    """Generalized kinematic split: ORTHONORMALIZED spectral projectors of
    A_end onto Im(lambda) >< 0 (reduces to the smatrix (I +- R)/2 SVD
    construction when A^2 is scalar -- graded traces are then invariant
    under the residual unitary basis freedom)."""
    A = -dbl(sgn * D_end + 1j * kappa * B) - E * GAM
    lam, V = np.linalg.eig(A)
    Vi = np.linalg.inv(V)
    plus = np.imag(lam) > 0
    re_max = float(np.max(np.abs(np.real(lam))))
    Pp = V[:, plus] @ Vi[plus, :]
    Bp = np.linalg.svd(Pp)[0][:, :int(np.sum(plus))]
    Bm = np.linalg.svd(I256 - Pp)[0][:, :int(np.sum(~plus))]
    return Bp, Bm, re_max


def chan(Bb, X):
    G = Bb.conj().T @ X @ Bb
    G = 0.5 * (G + G.conj().T)
    w, Vv = np.linalg.eigh(G)
    absG_isqrt = Vv @ np.diag(1.0 / np.sqrt(np.abs(w))) @ Vv.conj().T
    C = Bb @ absG_isqrt
    Egr = C.conj().T @ X @ C
    return C, 0.5 * (Egr + Egr.conj().T)


def smatrix(win, E, X, kappa, B, sgn=+1.0, place="symbol", dress=None):
    T = transfer(win, E, kappa, B, sgn, place)
    if dress is not None:
        T = dress @ T @ np.linalg.inv(dress)
    BLp, BLm, evL = modes_gen(win["D_L"], E, kappa, B, sgn)
    BRp, BRm, evR = modes_gen(win["D_R"], E, kappa, B, sgn)
    if dress is not None:
        BLp, BLm, BRp, BRm = (dress @ Z for Z in (BLp, BLm, BRp, BRm))
    CLp, ELp = chan(BLp, X)
    CLm, ELm = chan(BLm, X)
    CRp, ERp = chan(BRp, X)
    CRm, ERm = chan(BRm, X)
    solL = np.linalg.solve(np.hstack([CRp, -T @ CLm]), T @ CLp)
    t_L, r_L = solL[:128, :], solL[128:, :]
    return dict(T=T, t_L=t_L, r_L=r_L, ELp=ELp, ELm=ELm, ERp=ERp, ERm=ERm,
                ev=max(evL, evR))


def functionals(sm):
    t_L, r_L = sm["t_L"], sm["r_L"]
    sv = np.linalg.svd(t_L, compute_uv=False)
    even = dict(tr_tt=float(np.trace(t_L.conj().T @ t_L).real),
                sv_top=float(sv[0]))
    odd = dict(
        gr_trans=float(np.trace(t_L.conj().T @ sm["ERp"] @ t_L).real),
        gr_refl=float(np.trace(r_L.conj().T @ sm["ELm"] @ r_L).real))
    return even, odd


# =============================================================================
# [T] configuration + kappa = 0 regression (V-blindness reproduced)
# =============================================================================
a4_main = ray(A_CONF_DN, P.s_star + 0.4)
WIN0 = window_of(a4_main, 48)
E_TH = float(np.sqrt(max(WIN0["q_L"], WIN0["q_R"])))
E0 = 1.5 * E_TH

# closed-form step regression at kappa = 0 on one segment
D_seg = WIN0["Ds"][0]
q_seg = qform(xi_of(float(WIN0["xm"][0]), a4_main))
A0 = -dbl(D_seg) - E0 * GAM
m = np.sqrt(complex(q_seg - E0 * E0))
step_cf = np.cosh(WIN0["h"] * m) * I256 + (np.sinh(WIN0["h"] * m) / m) * A0
step_ex = expm(WIN0["h"] * A0)
reg = float(np.max(np.abs(step_cf - step_ex)))
SM0 = smatrix(WIN0, E0, X1, 0.0, B_EVEN)
ev0, od0 = functionals(SM0)
tr_odd0 = abs(od0["gr_trans"]) + abs(od0["gr_refl"])
check("T", "kappa = 0 regression: expm step equals the m1 closed-form "
           "entire step machine-exactly, and the traced odd functionals "
           "are exact zeros (V-blindness reproduced in this builder before "
           "any dressing)",
      reg < 1e-10 and tr_odd0 < 1e-8 and SM0["ev"] < 1e-8,
      f"step defect {reg:.1e}; traced odd {tr_odd0:.1e}; "
      f"evanescent {SM0['ev']:.1e}")

# conservation of the current by the DRESSED dynamics (exact algebra)
Ad = -dbl(D_seg + 0.2j * B_EVEN) - E0 * GAM
cons = float(np.max(np.abs(Ad.conj().T @ X1 + X1 @ Ad)))
check("T", "the conserved current X1 = sigma2 x K_S remains EXACTLY "
           "conserved by the dressed dynamics (A^dag X1 + X1 A = 0 with "
           "the Clifford-even term in place): the sector-reading current "
           "survives the dressing",
      cons < 1e-10, f"conservation defect {cons:.1e}")

def battery():
    # --- [E] the kappa ladder: the traced sector-odd functionals STAY ZERO
    print("\n=== STAGE 3: the V-breaking crack, kappa ladder ===", flush=True)
    kappas = (0.05, 0.1, 0.2)
    worst_tr, worst_chan = 0.0, 0.0
    for kap in kappas:
        sm = smatrix(WIN0, E0, X1, kap, B_EVEN)
        ev, od = functionals(sm)
        tr0 = abs(od["gr_trans"]) + abs(od["gr_refl"])
        chan_max = float(np.max(np.abs(np.real(
            np.diag(sm["t_L"].conj().T @ sm["ERp"] @ sm["t_L"])))))
        worst_tr, worst_chan = max(worst_tr, tr0), max(worst_chan, chan_max)
        log(f"kappa={kap}: traced odd = {tr0:.3g}, per-channel max = "
            f"{chan_max:.3f}, tr_tt = {ev['tr_tt']:.6g}, "
            f"evanescent {sm['ev']:.1e}")
    check("E", "DEEP BLINDNESS (the crack does NOT open): with the honest "
               "Clifford-even symbol dressing -- V provably broken -- every "
               "traced (ungraded-prepared) sector-odd functional REMAINS AN "
               "EXACT ZERO at every kappa, while per-channel graded entries "
               "are O(0.5): the cancellation survives curvature; a graded "
               "preparation is still required to read anything",
          worst_tr < 1e-9 and worst_chan > 1e-2,
          f"worst traced odd {worst_tr:.1e}; per-channel max {worst_chan:.3f}")

    # --- [E] the surviving mechanism, NAMED: ghost-Kramers conjugation
    kap = 0.1
    SVJ = V_GH @ CJt          # S_VJ = (sigma2 x OM C_J) o conj, antiunitary
    SVJi = np.linalg.inv(SVJ)
    A_d = -dbl(WIN0["Ds"][3] + 1j * kap * B_EVEN) - E0 * GAM
    m_dyn = float(np.max(np.abs(SVJ @ np.conj(A_d) @ SVJi - A_d)))
    m_x1 = float(np.max(np.abs(SVJ @ np.conj(X1) @ SVJi - X1)))
    m_gam = float(np.max(np.abs(SVJ @ np.conj(GAM) @ SVJi - GAM)))
    # universality: any K-honest symbol term (vector, even-with-forced-i,
    # grade-3 torsion-type with its K-honest factor) is S_VJ-real
    y = np.cos(1.1 * np.arange(14))
    B2 = Sigma(2, 9) - 0.4 * Sigma(3, 4)
    A_u = -dbl(cvec(y) + 1j * 0.07 * B2) - 1.3 * E0 * GAM
    m_uni = float(np.max(np.abs(SVJ @ np.conj(A_u) @ SVJi - A_u)))
    # boundary: the K-honest grade-3 (torsion-type) term BREAKS S_VJ
    # (K-honesty forces i on grade 3 as well; grade 3 is V-commuting and
    # J-odd, so the V/J flips no longer cancel)
    T3 = e[1] @ e[2] @ e[9]
    t3_needs_i = float(np.max(np.abs(K_S @ (1j * T3).conj().T @ K_S
                                     - 1j * T3))) < 1e-12
    A_3 = A_u - dbl(0.05j * T3)
    m_t3 = float(np.max(np.abs(SVJ @ np.conj(A_3) @ SVJi - A_3)))
    # and S_VJ swaps the movers (antiunitarity flips +-ik)
    Bp, Bm, _ = modes_gen(WIN0["D_L"], E0, kap, B_EVEN)
    SB = SVJ @ np.conj(Bp)
    m_swap = float(np.linalg.norm(SB - Bm @ (np.linalg.pinv(Bm) @ SB)))
    check("E", "THE SURVIVING MECHANISM, NAMED -- GHOST-KRAMERS CONJUGATION "
               "S_VJ = (sigma2 x omega J_quat) o conj: V and J_quat are "
               "EACH broken by the even term (V anticommutes with it, "
               "J flips its forced i), but BOTH flips cancel in the "
               "product: S_VJ is an exact antiunitary symmetry of EVERY "
               "K_S-honest vector+even family (universality witnessed on "
               "an unrelated symbol and connection), fixes X1 and Gamma, "
               "and exchanges right- and left-movers",
          m_dyn < 1e-12 and m_x1 < 1e-12 and m_gam < 1e-12
          and m_uni < 1e-12 and m_swap < 1e-8,
          f"dressed-dynamics defect {m_dyn:.1e}; X1 fix {m_x1:.1e}; "
          f"universality {m_uni:.1e}; mover swap {m_swap:.1e}")
    check("E", "THE PROTECTION'S ALGEBRAIC BOUNDARY: K-honesty forces the "
               "i on grade-3 (torsion-type) terms too, which are "
               "V-COMMUTING and J-ODD -- the flips no longer cancel and "
               "S_VJ is broken by a K-honest torsion term (defect = the "
               "full size of the term). With grade-2 AND grade-3 dressing "
               "together, V, J_quat, AND S_VJ are ALL broken",
          t3_needs_i and m_t3 > 0.05,
          f"grade-3 needs i: {t3_needs_i}; S_VJ defect with torsion "
          f"{m_t3:.3f}")

    # --- [E] the current PAIR collapses: X2 conservation dies
    X2 = 1j * np.kron(I2, K_S @ OM)
    A_0 = -dbl(WIN0["Ds"][3]) - E0 * GAM
    c_0 = float(np.max(np.abs(A_0.conj().T @ X2 + X2 @ A_0)))
    c_d = float(np.max(np.abs(A_d.conj().T @ X2 + X2 @ A_d)))
    check("E", "the second current X2 = i I x K_S omega is EXACTLY "
               "conserved by the vector family and NOT conserved by the "
               "dressed family: curvature collapses the conserved "
               "K_S-linear current pair to {X1} alone -- any X2-graded "
               "number on the dressed family is not a conserved reading "
               "(selection-rule honesty; its raw value is reported as "
               "non-observable residue only)",
          c_0 < 1e-10 and c_d > 1e-3,
          f"X2 conservation defect: undressed {c_0:.1e}, dressed {c_d:.3g}")

    # --- [E] refinement honesty on the ZERO (nseg ladder)
    col = {}
    for nseg in (24, 48, 96):
        w = window_of(a4_main, nseg)
        smn = smatrix(w, E0, X1, kap, B_EVEN)
        _e, o = functionals(smn)
        col[nseg] = abs(o["gr_trans"]) + abs(o["gr_refl"])
        log(f"nseg={nseg}: traced odd (kappa=0.1) = {col[nseg]:.3g}")
    sm_e2 = smatrix(WIN0, 2.2 * E_TH, X1, kap, B_EVEN)
    _e2, o2 = functionals(sm_e2)
    check("E", "the zero is not a discretization or energy accident: exact "
               "at nseg = 24/48/96 and at a second scattering energy",
          max(col.values()) < 1e-9
          and abs(o2["gr_trans"]) + abs(o2["gr_refl"]) < 1e-9,
          f"traced-odd column {dict((k, float(f'{v:.2g}')) for k, v in col.items())}; "
          f"E2 {abs(o2['gr_trans']) + abs(o2['gr_refl']):.1e}")

    # --- [F] controls: even functionals invariant; cov-der placement blind
    Ui = np.linalg.inv(U_ss)
    WIN_ss = dict(WIN0, Ds=[U_ss @ D @ Ui for D in WIN0["Ds"]],
                  D_L=U_ss @ WIN0["D_L"] @ Ui, D_R=U_ss @ WIN0["D_R"] @ Ui)
    sm_b = smatrix(WIN0, E0, X1, kap, B_EVEN)
    ev_b, _ob = functionals(sm_b)
    sm_ss = smatrix(WIN_ss, E0, X1, kap, U_ss @ B_EVEN @ Ui)
    ev_ss, _os = functionals(sm_ss)
    c1 = max(abs(ev_b[k] - ev_ss[k]) / max(1.0, abs(ev_b[k])) for k in ev_b)
    Mexp = expm(0.15 * (e[0] @ e[1] + 0.7 * (e[2] @ e[9])))
    sm_fr = smatrix(WIN0, E0, X1, kap, B_EVEN, dress=np.kron(I2, Mexp))
    ev_fr, o_fr = functionals(sm_fr)
    c2 = max(abs(ev_b[k] - ev_fr[k]) / max(1.0, abs(ev_b[k])) for k in ev_b)
    sm_cd = smatrix(WIN0, E0, X1, kap, B_EVEN, place="cov")
    _ec, oc = functionals(sm_cd)
    c3 = abs(oc["gr_trans"]) + abs(oc["gr_refl"])
    check("F", "trichotomy controls at kappa = 0.1: same-sign-plane "
               "covariant transport and K_S-pseudo-unitary frame dressing "
               "leave the battery invariant (and the odd zeros stay zero "
               "under both); the V-COMMUTING covariant-derivative "
               "placement of the SAME connection is blind outright",
          c1 < 1e-6 and c2 < 1e-4 and c3 < 1e-9
          and abs(o_fr["gr_trans"]) + abs(o_fr["gr_refl"]) < 1e-9,
          f"U_ss even spread {c1:.1e}; frame even spread {c2:.1e}; "
          f"cov-der odd {c3:.1e}")

    return worst_tr < 1e-9


def deep_identity():
    """The decisive escalation: break EVERY named symmetry (V, J, S_VJ via
    mixed grade-2 + grade-3 dressing; then X1-conservation itself via a
    non-K-honest term; then all Clifford structure via a generic
    deterministic family) and watch the traced sector-odd functionals."""
    print("\n=== STAGE 3b: the deep-blindness identity ===", flush=True)
    T3 = e[1] @ e[2] @ e[9]

    # (i) mixed dressing: V, J, S_VJ all broken
    sm_mix = smatrix(WIN0, E0, X1, 0.1, B_EVEN + 0.5 * T3)
    _em, om_ = functionals(sm_mix)
    z_mix = abs(om_["gr_trans"]) + abs(om_["gr_refl"])

    # (ii) generic deterministic K-honest family (no end-model structure)
    def hgen(x):
        v = 2.0 * np.cos(1.7 * np.arange(14) + x)
        return (cvec(v) + 0.3j * np.cos(2.3 + x) * (e[2] @ e[9])
                + 0.25j * np.cos(0.7 * x) * T3)

    xs = np.linspace(0.0, 1.0, 25)[:24]
    wing = dict(WIN0, Ds=[hgen(float(x)) for x in xs], h=1.0 / 24,
                D_L=hgen(-0.3), D_R=hgen(1.4))
    sm_g = smatrix(wing, 9.0, X1, 0.0, 0 * B_EVEN)
    _eg, og = functionals(sm_g)
    z_gen = abs(og["gr_trans"]) + abs(og["gr_refl"])
    tg = sm_g["t_L"]
    dmax_g = float(np.max(np.abs(np.real(
        np.diag(tg.conj().T @ sm_g["ERp"] @ tg)))))
    wtr = float(np.trace(tg.conj().T
                         @ np.diag(np.cos(0.9 * np.arange(128))).astype(complex)
                         @ tg).real)

    # (iii) X1-conservation broken outright (non-K-honest grade-2, no i)
    def hbad(x):
        v = 2.0 * np.cos(1.7 * np.arange(14) + x)
        return cvec(v) + 0.3 * np.cos(2.3 + x) * (e[2] @ e[9])

    winb = dict(wing, Ds=[hbad(float(x)) for x in xs],
                D_L=hbad(-0.3), D_R=hbad(1.4))
    Ab = -dbl(winb["Ds"][0]) - 9.0 * GAM
    x1_broken = float(np.max(np.abs(Ab.conj().T @ X1 + X1 @ Ab)))
    sm_b = smatrix(winb, 9.0, X1, 0.0, 0 * B_EVEN)
    _eb, ob = functionals(sm_b)
    z_bad = abs(ob["gr_trans"]) + abs(ob["gr_refl"])

    check("E", "DEEP-BLINDNESS IDENTITY (the strongest finding of this "
               "stage): the traced graded transmission/reflection vanish "
               "IDENTICALLY -- with V+J+S_VJ all broken (mixed grade-2 + "
               "grade-3 dressing), for a generic non-end-model K-honest "
               "family, and EVEN for a family that breaks X1-conservation "
               "itself -- while per-channel readings stay O(0.5) and "
               "non-grading-weighted traces are O(1). The zero is an "
               "identity of the graded scattering construction, NOT a "
               "consequence of any of the named symmetries: mechanism 1 "
               "(V) was sufficient but never necessary",
          z_mix < 1e-9 and z_gen < 1e-9 and z_bad < 1e-9
          and x1_broken > 0.1 and dmax_g > 1e-2 and abs(wtr) > 1e-2,
          f"traced-odd: mixed {z_mix:.1e}, generic {z_gen:.1e}, "
          f"X1-broken {z_bad:.1e}; per-chan {dmax_g:.3f}; "
          f"control weight {wtr:.3f}")

    # (iv) the pairing structure behind the identity, extracted
    Q = tg.conj().T @ sm_g["ERp"] @ tg
    w, U = np.linalg.eigh(0.5 * (Q + Q.conj().T))
    idx = np.argsort(w)
    Us = U[:, idx]
    pair_def = float(np.max(np.abs(np.sort(w) + np.sort(w)[::-1])))
    sig = Us @ np.fliplr(np.eye(len(w))) @ Us.conj().T
    s_inv = float(np.max(np.abs(sig @ sig - np.eye(len(w)))))
    s_anti = float(np.max(np.abs(sig @ Q @ sig + Q)))
    s_acE = float(np.max(np.abs(sig @ sm_g["ELp"] + sm_g["ELp"] @ sig)))
    check("E", "the identity's shape: Q = t^dag E_R t has an EXACTLY "
               "+/- paired spectrum; a Hermitian involution sig with "
               "sig Q sig = -Q exists (extracted), approximately "
               "anticommuting with the incident grading. Identifying sig "
               "with a named channel-algebra element is the residual open "
               "object of the blindness theory (stated in the doc)",
          pair_def < 1e-10 and s_inv < 1e-10 and s_anti < 1e-10,
          f"spectral pairing {pair_def:.1e}; sig^2-I {s_inv:.1e}; "
          f"sig-anticommute-Q {s_anti:.1e}; {{sig, E_Lp}} {s_acE:.2e}")

    print("\nVERDICT Q-C: C-BLIND, STRENGTHENED TWICE OVER. (1) The "
          "V-crack opens exactly as predicted and the blindness survives; "
          "at connection grade the named surviving symmetry is the "
          "ghost-Kramers conjugation S_VJ = (sigma2 x omega J_quat) o "
          "conj, exact for every K_S-honest vector+even family. (2) "
          "Deeper: even with V, J, AND S_VJ all broken -- and even with "
          "X1-conservation broken -- the traced sector-odd functionals "
          "vanish by an exact spectral-pairing identity of the graded "
          "scattering construction. The dynamical face does NOT reopen; "
          "no PP4 candidate is written; the pairing involution's algebraic "
          "name is the sharpest new open object.", flush=True)


if __name__ == "__main__":
    battery()
    deep_identity()
    print("\nHEADLINE: Q-C = C-BLIND, strengthened twice over -- the "
          "V-crack opens (honest Clifford-even dressing, forced T-odd) "
          "and the sector stays dynamically unreadable: ghost-Kramers "
          "conjugation S_VJ protects all vector+even families, and beyond "
          "it an exact spectral-pairing identity of graded scattering "
          "keeps every traced sector-odd functional at zero (V was "
          "sufficient, never necessary). No PP4 candidate.", flush=True)
    bad = [r for r in RESULTS if not r[2]]
    print(f"\n{'ALL PASS' if not bad else 'FAILURES: ' + str(len(bad))}"
          f"  ({len(RESULTS)} checks)  [t={time.time()-T0:.1f}s]")
    sys.exit(0 if not bad else 1)
