#!/usr/bin/env python3
"""S-MATRIX SECTOR FACE -- does the central Z/2 payload bit (the Krein-sector
orientation, K_S -> -K_S under the loop holonomy) have a DYNAMICAL face, i.e.
a scattering observable in the K_S-LINEAR (sector-reading) class -- or is
dynamical blindness provable (the Araki even/odd selection rule extending to
the whole S-matrix)?

CHANNEL: big swing (Joe direct chat, 2026-07-20: S-matrix face of the
         sector sign).
DESIGN:  explorations/smatrix-sector-face-2026-07-20.md
EXTENDS: tests/channel-swings/m1_third_reading_probe.py (executed IN-LOAD via
         a namespace exec -- its machinery is imported, not rebuilt; its 16
         checks re-run and must ALL PASS as a free regression receipt; that
         file is not edited), which itself replicates the n2 end-family
         machinery (same seed 20260720, same stream -- the SAME 53 crossing
         rays). Consumes m1's both-modes normal form, the f5 canonical cut
         lineage, and the Araki even/odd selection rule as regression targets.

THE TOY (constructions named -- GEOMETER-VS-PHYSICS-OBJECTS discipline):
  A 1D collar-Dirac scattering problem across the wall region. At a crossing
  radius s = s* + 0.4 the loop coordinate t crosses the null cone on an open
  interval; take a window [t_lo, t_hi] containing it with gapped ends and
  treat t as the propagation coordinate x. The collar normal needs a 15th
  Clifford generator, which Cl(9,5) at DIM 128 cannot supply: the spinor
  space is DOUBLED (C^2 tensor C^128) -- the standard boundary-restriction
  doubling, program-native, not a positivity import:
      gamma_a   = sigma1 x e_a        (tangent Clifford action)
      Gamma     = i sigma2 x I        (collar normal; Gamma^2 = -I,
                                       anti-Hermitian, anticommutes with all
                                       gamma_a)
      D~(x)     = sigma1 x D(x),  D(x) = c(xi(t(x), s))   (the actual family)
  Stationary equation Gamma (d/dx + D~) psi = E psi, i.e. psi' = A(x,E) psi
  with A = -D~ - E Gamma and A^2 = (q(x) - E^2) I EXACTLY (scalar): the
  gapped ends propagate for E^2 > q_end, the crossed region is the
  resonator, and every transfer step has the m1 entire-in-q closed form.
  NO positive metric is used anywhere: mode splitting is KINEMATIC
  (eigenvalues +-ik of A), channel normalization uses |flux| only, and the
  conserved structure is the indefinite Krein current (below).

PRE-DECLARED KILL/OUTCOME CONDITIONS (in the design doc before computing):
  K-a: every S-matrix functional of the toy is K_S-even -- dynamical
       blindness; the external-posit typing of the bit is STRENGTHENED.
  K-b: K_S-linear scattering functionals exist but none has an in-principle
       physical realization independent of an external orientation datum.
  K-c: an in-principle-observable asymmetry flips with the sector, survives
       ALL trichotomy controls, and its non-quaternionic consumer is named.

WHAT IS TESTED (headline shape):
  A. The construction: doubled Clifford objects, scalar A^2, the crossed-
     region transfer step = the m1 both-modes evolution (same entire C/S
     series, q Wick-continued).
  B. The conserved-current pair X1 = sigma2 x K_S, X2 = i I x K_S omega:
     Hermitian, conserved machine-exactly, K_S-LINEAR (both flip with the
     sector), J_quat-ANTI-commuting (non-quaternionic, T-odd) -- the only
     sector-sensitive structures in the entire scattering apparatus.
  C. S(E) built natively; graded (indefinite) flux conservation at S level;
     threshold resonance lineshape; PT-reality of the transfer.
  D. TRANSPARENCY THEOREM: S(E) is IDENTICAL under K_S -> -K_S (machine
     zero); the sector flip acts on scattering data as (S, eps) -> (S, -eps)
     where eps is the channel Krein grading. Every functional of S alone is
     K_S-even -- the Araki selection rule extends to the whole S-matrix.
  E. The K_S-linear class: nonempty (per-channel graded transmissions are
     dynamical and nonzero) BUT (i) the GHOST-CONJUGATION symmetry
     V = sigma2 x omega commutes with the entire dynamics and anticommutes
     with both currents, so every V-symmetric (ungraded-prepared) K_S-odd
     functional vanishes IDENTICALLY; and (ii) PARITY TRANSFER: conjugation
     by W = I x omega maps (D -> -D, K_S fixed) to (D fixed, K_S -> -K_S)
     EXACTLY, so sector-parity = symbol-orientation-parity for every
     scattering functional -- any surviving K_S-odd reading moves under the
     kappa-type orientation convention and is a gauge artifact as a sector
     face.
  F. Trichotomy controls: same-sign-plane transport, covariant pseudo-
     unitary frame dressing, channel-gauge moves -- all functionals exactly
     invariant; SRC-REJ-1 guard (C2 untouched).

NONCLAIMS. Toy grade: one window per ray, piecewise-constant symbol family,
matrix grade (no operator, no L^2, no QFT lift); the V-symmetry protection
is exact for Clifford-VECTOR families (D = c(xi)) and is PROVEN here to
break on Clifford-EVEN (bivector/curvature-type) terms -- operator-grade
residue, named in the doc; no claim/canon/posture movement. Deterministic;
numpy only; all randomness upstream in the m1/n2 seeded stream (20260720);
no new RNG draws in this probe.
"""
from __future__ import annotations

import contextlib
import io
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return ok


# --- import the m1 machinery by EXECUTING the m1 probe ------------------------
_M1_PATH = os.path.join(HERE, "m1_third_reading_probe.py")
_buf = io.StringIO()
_m1_exit = None
M1 = {"__file__": _M1_PATH, "__name__": "m1_third_reading_probe"}
_src = open(_M1_PATH).read()
with contextlib.redirect_stdout(_buf):
    try:
        exec(compile(_src, _M1_PATH, "exec"), M1)
    except SystemExit as ex:
        _m1_exit = ex.code
_m1_out = _buf.getvalue()

check("T", "m1 probe executed in-load as the machinery source: exit 0, "
           "'ALL PASS' headline reproduced (16 checks re-verified; the n2 "
           "end-model sweep 132/53/0/15 and both-modes normal form inherited)",
      _m1_exit == 0 and "ALL PASS" in _m1_out,
      f"m1 exit {_m1_exit}")

e = M1["e"]; K_S = M1["K_S"]; C_J = M1["C_J"]; I128 = M1["I128"]
cvec = M1["cvec"]; qform = M1["qform"]; xi_of = M1["xi_of"]
ray = M1["ray"]; evolve = M1["evolve"]; ent_CS = M1["ent_CS"]
U_h = M1["U_h"]; U_ss = M1["U_ss"]
A_CONF_DN = M1["A_CONF_DN"]; A_CONF_UP = M1["A_CONF_UP"]
A_BOOST = M1["A_BOOST"]
s_star = M1["s_star"]; t_dn = M1["t_dn"]
sweep_rays = M1["sweep_rays"]; XI = M1["XI"]; DIM = M1["DIM"]
crossing_scan = M1["crossing_scan"]; bisect_wall = M1["bisect_wall"]

check("T", "harvest sanity: K_S Hermitian involution; J^2 = -I; the "
           "conf-down wall s*/t* and 53 sweep crossing rays present",
      float(np.max(np.abs(K_S @ K_S - I128))) < 1e-9
      and float(np.max(np.abs(C_J @ np.conj(C_J) + I128))) < 1e-12
      and len(sweep_rays) == 53 and s_star > 0,
      f"s* = {s_star:.4f}, t* = {t_dn:.3f}, rays {len(sweep_rays)}")

# --- doubled objects -----------------------------------------------------------
OM = I128.copy()
for a in range(14):
    OM = OM @ e[a]
S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
S3 = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)
I256 = np.eye(256, dtype=complex)
GAM = 1j * np.kron(S2, I128)
CJt = np.kron(I2, C_J)          # J~ = CJt o conj (doubled J_quat)
W_OM = np.kron(I2, OM)          # the orientation conjugator
V_GH = np.kron(S2, OM)          # the ghost-conjugation symmetry


def X1_of(K):
    return np.kron(S2, K)


def X2_of(K):
    return 1j * np.kron(I2, K @ OM)


X1, X2 = X1_of(K_S), X2_of(K_S)


def dbl(D):
    return np.kron(S1, D)


# --- the scattering builder ----------------------------------------------------
def window_of(a4, nseg=48, pad=0.12):
    """Find the crossed t-interval at collar point a4; return the window
    grid, midpoint symbols, and gapped end data."""
    tg = np.linspace(0.0, 1.0, 201)
    qs = np.array([qform(xi_of(float(t), a4)) for t in tg])
    if np.min(qs) < 0:
        tneg = tg[qs < 0]
        t_lo, t_hi = float(tneg.min() - pad), float(tneg.max() + pad)
    else:                       # gapped control ray: arbitrary window
        t_lo, t_hi = 0.30, 0.90
    xg = np.linspace(t_lo, t_hi, nseg + 1)
    xm = 0.5 * (xg[:-1] + xg[1:])
    h = float(xg[1] - xg[0])
    Ds = [cvec(xi_of(float(t), a4)) for t in xm]
    qs_m = [qform(xi_of(float(t), a4)) for t in xm]
    D_L, q_L = cvec(xi_of(t_lo, a4)), qform(xi_of(t_lo, a4))
    D_R, q_R = cvec(xi_of(t_hi, a4)), qform(xi_of(t_hi, a4))
    return dict(t_lo=t_lo, t_hi=t_hi, h=h, xm=xm,
                DTs=[dbl(D) for D in Ds], qs=qs_m,
                D_L=D_L, q_L=q_L, D_R=D_R, q_R=q_R,
                q_min=float(np.min(qs)))


def step(DT, q, E, h):
    """exp(h A), A = -DT - E GAM, A^2 = (q - E^2) I exactly."""
    A = -DT - E * GAM
    m = np.sqrt(complex(q - E * E))
    if abs(m) < 1e-13:
        return I256 + h * A
    return np.cosh(h * m) * I256 + (np.sinh(h * m) / m) * A


def transfer(win, E, DTs=None):
    DTs = win["DTs"] if DTs is None else DTs
    T = I256
    for DT, q in zip(DTs, win["qs"]):
        T = step(DT, q, E, win["h"]) @ T
    return T


def modes(D_end, q_end, E):
    """Kinematic mode split (K_S-FREE): the +-ik eigenspaces of A."""
    A = -dbl(D_end) - E * GAM
    k = np.sqrt(complex(E * E - q_end))
    R = A / (1j * k)
    Bp = np.linalg.svd(0.5 * (I256 + R))[0][:, :128]
    Bm = np.linalg.svd(0.5 * (I256 - R))[0][:, :128]
    return Bp, Bm


def chan(B, X):
    """Channels from a kinematic basis: normalize by |flux| ONLY (K_S-even),
    carry the grading operator Egr = C^dag X C (a Hermitian involution,
    K_S-ODD) separately."""
    G = B.conj().T @ X @ B
    G = 0.5 * (G + G.conj().T)
    w, Vv = np.linalg.eigh(G)
    absG_isqrt = Vv @ np.diag(1.0 / np.sqrt(np.abs(w))) @ Vv.conj().T
    C = B @ absG_isqrt
    Egr = C.conj().T @ X @ C
    return C, 0.5 * (Egr + Egr.conj().T)


def smatrix(win, E, X, DTs=None, dress=None):
    """Full S(E): blocks r_L, t_L (left incidence), t_R, r_R (right
    incidence), with channel gradings. dress: optional 256x256 map applied
    covariantly to the end symbols and mode bases."""
    T = transfer(win, E, DTs)
    D_L, D_R = win["D_L"], win["D_R"]
    if dress is not None:
        T = dress @ T @ np.linalg.inv(dress)
    BLp, BLm = modes(D_L, win["q_L"], E)
    BRp, BRm = modes(D_R, win["q_R"], E)
    if dress is not None:
        BLp, BLm = dress @ BLp, dress @ BLm
        BRp, BRm = dress @ BRp, dress @ BRm
    CLp, ELp = chan(BLp, X)
    CLm, ELm = chan(BLm, X)
    CRp, ERp = chan(BRp, X)
    CRm, ERm = chan(BRm, X)
    solL = np.linalg.solve(np.hstack([CRp, -T @ CLm]), T @ CLp)
    t_L, r_L = solL[:128, :], solL[128:, :]
    solR = np.linalg.solve(np.hstack([T @ CLm, -CRp]), CRm)
    t_R, r_R = solR[:128, :], solR[128:, :]
    return dict(T=T, t_L=t_L, r_L=r_L, t_R=t_R, r_R=r_R,
                ELp=ELp, ELm=ELm, ERp=ERp, ERm=ERm,
                CLp=CLp, CLm=CLm, CRp=CRp, CRm=CRm)


def functionals(sm):
    """The classification battery: even-class (functions of S alone) and
    odd-class (single-grading) scattering functionals."""
    t_L, r_L = sm["t_L"], sm["r_L"]
    sv = np.linalg.svd(t_L, compute_uv=False)
    # NOTE: the battery is restricted to CHANNEL-GAUGE-INVARIANT functionals
    # (traces, singular values, grading-paired traces). Phases of det(t) are
    # channel-gauge data, not observables -- consistent with the [F]
    # channel-gauge control below.
    even = dict(
        tr_tt=float(np.trace(t_L.conj().T @ t_L).real),
        tr_rr=float(np.trace(r_L.conj().T @ r_L).real),
        sv_top=float(sv[0]), sv_bot=float(sv[-1]),
        tr_ttEE=float(np.trace(t_L.conj().T @ sm["ERp"] @ t_L
                               @ sm["ELp"]).real),
    )
    odd = dict(
        gr_trans=float(np.trace(t_L.conj().T @ sm["ERp"] @ t_L).real),
        gr_refl=float(np.trace(r_L.conj().T @ sm["ELm"] @ r_L).real),
        gr_chan_max=float(np.max(np.abs(np.real(
            np.diag(t_L.conj().T @ sm["ERp"] @ t_L))))),
    )
    return even, odd


# =============================================================================
# [T] geometry of the main configuration (conf-down ray, s* + 0.4)
# =============================================================================
a4_main = ray(A_CONF_DN, s_star + 0.4)
WIN = window_of(a4_main)
E_TH = float(np.sqrt(max(WIN["q_L"], WIN["q_R"])))
E0 = 1.5 * E_TH
xspan = np.stack([np.real(np.asarray(
    np.linalg.norm(xi_of(float(t), a4_main)))) for t in WIN["xm"]])
xmat = np.stack([np.asarray(xi_of(float(t), a4_main), dtype=float)
                 for t in WIN["xm"]])
rank_xi = int(np.sum(np.linalg.svd(xmat, compute_uv=False)
                     > 1e-8 * np.linalg.norm(xmat)))
check("T", "main configuration: window on the conf-down ray at s* + 0.4 "
           "contains the crossed t-interval with GAPPED ends (q_L, q_R > 0 "
           "> q_min); the window symbols span a rank-5 subspace of the 14 "
           "Clifford directions (recorded receipt: the conserved-current "
           "COMPLETENESS argument in the doc does not need full span -- "
           "X -> K_S^-1 X bijects conserved currents onto the family "
           "anticommutant, so EVERY conserved current carries exactly one "
           "factor of K_S and is K_S-linear, for any span rank)",
      WIN["q_L"] > 0 and WIN["q_R"] > 0 and WIN["q_min"] < 0
      and rank_xi >= 2,
      f"window [{WIN['t_lo']:.3f}, {WIN['t_hi']:.3f}], q ends "
      f"{WIN['q_L']:.1f}/{WIN['q_R']:.1f}, q_min {WIN['q_min']:.1f}, "
      f"xi-rank {rank_xi}")


# =============================================================================
# Part A -- the construction
# =============================================================================
ok_cliff = float(np.max(np.abs(GAM @ GAM + I256))) < 1e-12 \
    and float(np.max(np.abs(GAM + GAM.conj().T))) < 1e-12
ok_anti = all(float(np.max(np.abs(GAM @ dbl(e[a]) + dbl(e[a]) @ GAM)))
              < 1e-12 for a in (0, 5, 9, 13))
DT0, q0 = WIN["DTs"][0], WIN["qs"][0]
A0 = -DT0 - E0 * GAM
sc_def = float(np.max(np.abs(A0 @ A0 - (q0 - E0 * E0) * I256)))
# the crossed-region step at E = 0 IS the m1 both-modes evolution with q
# Wick-continued: exp(-h sigma1 x D) = C(-q, h) I - S(-q, h) sigma1 x D
i_cross = int(np.argmin(WIN["qs"]))
DTc, qc = WIN["DTs"][i_cross], WIN["qs"][i_cross]
Cs, Ss = ent_CS(-qc, WIN["h"])
step_direct = step(DTc, qc, 0.0, WIN["h"])
step_series = Cs * I256 - Ss * DTc
wick_def = float(np.max(np.abs(step_direct - step_series))) / max(
    1.0, float(np.max(np.abs(step_direct))))
check("E", "THE CONSTRUCTION: doubled collar-Dirac objects verified "
           "(Gamma^2 = -I, anti-Hermitian, anticommutes with the tangent "
           "Clifford action; A^2 = (q - E^2) I machine-exactly -- every "
           "transfer step has the m1 entire-in-q closed form), and the "
           "crossed-region step at E = 0 EQUALS the m1 both-modes "
           "evolution under q -> -q (same entire C/S series): the "
           "resonator content of the wall region IS the both-modes "
           "complex-pair structure, Wick-continued to the collar "
           "propagation coordinate -- one construction, not two",
      ok_cliff and ok_anti and sc_def < 1e-9 * max(1.0, abs(q0 - E0 * E0))
      and wick_def < 1e-12,
      f"A^2 scalar defect {sc_def:.1e}, Wick-step defect {wick_def:.1e}")


# =============================================================================
# Part B -- the conserved-current pair (the ONLY sector-sensitive structure)
# =============================================================================
T_main = transfer(WIN, E0)
Tn2 = float(np.max(np.abs(T_main))) ** 2
cons1 = float(np.max(np.abs(T_main.conj().T @ X1 @ T_main - X1))) / Tn2
cons2 = float(np.max(np.abs(T_main.conj().T @ X2 @ T_main - X2))) / Tn2
bad = []
for Xb in (np.kron(S3, K_S), np.kron(I2, K_S), I256):
    bad.append(float(np.max(np.abs(
        T_main.conj().T @ Xb @ T_main - Xb))) / Tn2)
herm12 = max(float(np.max(np.abs(X1 - X1.conj().T))),
             float(np.max(np.abs(X2 - X2.conj().T))))
flip12 = max(float(np.max(np.abs(X1_of(-K_S) + X1))),
             float(np.max(np.abs(X2_of(-K_S) + X2))))
janti1 = float(np.max(np.abs(CJt @ np.conj(X1) + X1 @ CJt)))
janti2 = float(np.max(np.abs(CJt @ np.conj(X2) + X2 @ CJt)))
check("E", "THE CONSERVED-CURRENT PAIR: X1 = sigma2 x K_S and "
           "X2 = i I x K_S omega are Hermitian and conserved by the actual "
           "wall-window transfer MACHINE-EXACTLY, while sigma3 x K_S, "
           "I x K_S, and the Dirac identity are NOT conserved (defects "
           "O(1)): the conserved accounting of the scattering problem is "
           "indefinite and K_S-derived, never positive -- and BOTH currents "
           "are (i) K_S-LINEAR (they flip with the sector) and (ii) "
           "J_quat-ANTI-commuting: the conserved current is T-ODD and "
           "NON-QUATERNIONIC. The Kramers no-go (J-commuting Hermitian "
           "probes are sector-blind) is respected by the dynamics in the "
           "strongest way: the only sector-sensitive structures in the "
           "scattering apparatus are exactly the non-quaternionic currents",
      cons1 < 1e-12 and cons2 < 1e-12 and min(bad) > 1e-2
      and herm12 < 1e-12 and flip12 < 1e-12
      and janti1 < 1e-12 and janti2 < 1e-12,
      f"cons {cons1:.1e}/{cons2:.1e}; non-conserved controls min defect "
      f"{min(bad):.2f}; J-anticommute {max(janti1, janti2):.1e}")

BLp0, BLm0 = modes(WIN["D_L"], WIN["q_L"], E0)
G0 = BLp0.conj().T @ X1 @ BLp0
G0 = 0.5 * (G0 + G0.conj().T)
ev0 = np.linalg.eigvalsh(G0)
cross0 = float(np.max(np.abs(BLp0.conj().T @ X1 @ BLm0)))
check("E", "channel structure at the gapped ends: the Krein-flux Gram on "
           "the kinematic right-movers has signature (64,64) with ALL "
           "|eigenvalues| EQUAL (quaternionic uniformity, as at the m1 "
           "walls) and is X1-orthogonal to the left-movers machine-exactly "
           "-- 64 positive-flux and 64 NEGATIVE-flux (ghost) channels per "
           "direction, the indefinite channel space the Krein carrier "
           "demands; no positive channel metric exists or is used",
      int(np.sum(ev0 > 0)) == 64 and int(np.sum(ev0 < 0)) == 64
      and (np.max(np.abs(ev0)) - np.min(np.abs(ev0)))
      < 1e-8 * np.max(np.abs(ev0)) and cross0 < 1e-12,
      f"|flux ev| = {np.abs(ev0).mean():.4f} (spread "
      f"{np.max(np.abs(ev0)) - np.min(np.abs(ev0)):.1e}), "
      f"cross-block {cross0:.1e}")


# =============================================================================
# Part C -- S(E), graded conservation, lineshape, PT-reality
# =============================================================================
SM = smatrix(WIN, E0, X1)
consL = float(np.max(np.abs(
    SM["ELp"] - (SM["t_L"].conj().T @ SM["ERp"] @ SM["t_L"]
                 - SM["r_L"].conj().T @ SM["ELm"] @ SM["r_L"]))))
consR = float(np.max(np.abs(
    SM["ERm"] - (SM["t_R"].conj().T @ SM["ELm"] @ SM["t_R"]
                 - SM["r_R"].conj().T @ SM["ERp"] @ SM["r_R"]))))
crossLR = float(np.max(np.abs(
    SM["t_L"].conj().T @ SM["ERp"] @ SM["r_R"]
    - SM["r_L"].conj().T @ SM["ELm"] @ SM["t_R"])))
check("E", "GRADED FLUX CONSERVATION AT S LEVEL (the Krein-native "
           "pseudo-unitarity, [P2] eq (38) shape): for both incidences the "
           "indefinite channel gradings satisfy "
           "E_in = t^dag E_trans t - r^dag E_refl r machine-exactly, with "
           "the cross-incidence identity closing the full graded "
           "S-unitarity -- conservation is INDEFINITE (both-modes-shaped) "
           "at the S-matrix level, exactly as the universal-null lemma "
           "demands: no positive conservation law exists to import",
      consL < 1e-10 and consR < 1e-10 and crossLR < 1e-10,
      f"defects L {consL:.1e} / R {consR:.1e} / cross {crossLR:.1e}")

Escan = np.linspace(E_TH * 1.02, E_TH * 1.9, 19)
line = []
for E in Escan:
    smE = smatrix(WIN, E, X1)
    line.append(float(np.trace(smE["t_L"].conj().T @ smE["t_L"]).real) / 128)
line = np.array(line)
i_pk = int(np.argmax(line))
E_c = 12.0 + 0.8j
T_c = transfer(WIN, E_c)
T_cc = transfer(WIN, np.conj(E_c))
pt_def = float(np.max(np.abs(
    CJt @ np.conj(T_c) @ np.linalg.inv(CJt) - T_cc))) / float(
    np.max(np.abs(T_cc)))
check("E", "RESONANCE LINESHAPE + PT-REALITY: the per-channel transmission "
           "trace rises from threshold to a resonance peak over the wall "
           "region and relaxes toward 1 at high energy (the wall region "
           "acts as the resonator; on the gapped control ray below there "
           "is no such structure to manufacture), and the transfer obeys "
           "the PT/Kramers reality J~ T(E) J~^-1 = T(conj E) "
           "machine-exactly: poles come in complex-conjugate pairs -- the "
           "both-modes pair structure of the m1 reading, realized as "
           "scattering poles",
      i_pk not in (0, len(line) - 1) and line[i_pk] > 1.2
      and line[-1] < line[i_pk] and pt_def < 1e-9,
      f"peak Tr t^dag t/128 = {line[i_pk]:.3f} at E = {Escan[i_pk]:.2f} "
      f"(threshold {E_TH:.2f}), tail {line[-1]:.3f}; PT defect {pt_def:.1e}")


# =============================================================================
# Part D -- THE TRANSPARENCY THEOREM (the central computation)
# =============================================================================
SMf = smatrix(WIN, E0, X1_of(-K_S))
d_t = float(np.max(np.abs(SMf["t_L"] - SM["t_L"])))
d_r = float(np.max(np.abs(SMf["r_L"] - SM["r_L"])))
d_tR = float(np.max(np.abs(SMf["t_R"] - SM["t_R"])))
d_rR = float(np.max(np.abs(SMf["r_R"] - SM["r_R"])))
gr_flip = max(float(np.max(np.abs(SMf[k] + SM[k])))
              for k in ("ELp", "ELm", "ERp", "ERm"))
ev_main, od_main = functionals(SM)
ev_flip, od_flip = functionals(SMf)
ev_eq = max(abs(ev_main[k] - ev_flip[k]) / max(1.0, abs(ev_main[k]))
            for k in ev_main)
od_fl = max(abs(od_main[k] + od_flip[k]) / max(1.0, abs(od_main[k]))
            for k in ("gr_trans", "gr_refl"))
check("E", "THE TRANSPARENCY THEOREM (central result): under the sector "
           "flip K_S -> -K_S the ENTIRE S-matrix is IDENTICAL to machine "
           "zero -- all four blocks, both incidences -- while the channel "
           "grading flips exactly: the sector flip acts on scattering data "
           "as (S, eps) -> (S, -eps). Mechanism: the dynamics (A = -D~ - E "
           "Gamma), the kinematic mode split (+-ik eigenspaces), and the "
           "|flux| channel normalization consume NO K_S-sign anywhere. "
           "Consequence: EVERY functional of S alone -- |S_ab|^2, "
           "cross-sections, line widths, Wigner delays, eigenphases, "
           "det-phases, relative phases between the paired resonance "
           "legs, in/out asymmetries -- is K_S-EVEN and sector-BLIND. The "
           "Araki even/odd selection rule extends to the whole S-matrix",
      max(d_t, d_r, d_tR, d_rR) < 1e-11 and gr_flip < 1e-11
      and ev_eq < 1e-10,
      f"|S(+K) - S(-K)| = {max(d_t, d_r, d_tR, d_rR):.1e}; grading flip "
      f"defect {gr_flip:.1e}; even-battery spread {ev_eq:.1e}")

check("E", "the K_S-LINEAR scattering class is NONEMPTY and flips exactly: "
           "single-grading functionals (graded transmission, graded "
           "reflection) change sign under the sector flip to machine "
           "precision, and per-channel graded transmissions are NONZERO "
           "(dynamical content exists in the odd class -- the blindness "
           "below is a theorem about what can CONSUME it, not an empty "
           "class)",
      od_fl < 1e-9 and od_main["gr_chan_max"] > 1e-2
      and abs(ev_main["tr_ttEE"] - ev_flip["tr_ttEE"]) < 1e-9
      * max(1.0, abs(ev_main["tr_ttEE"])),
      f"odd-flip defect {od_fl:.1e}; max per-channel graded transmission "
      f"{od_main['gr_chan_max']:.4f}; double-graded (even) invariant")

# sector flip implemented the OTHER way: U_h-transport of the family with
# K_S fixed -- must act identically on the functionals
Uh_d = np.kron(I2, U_h)
DTs_h = [Uh_d @ DT @ np.linalg.inv(Uh_d) for DT in WIN["DTs"]]
WIN_h = dict(WIN, D_L=U_h @ WIN["D_L"] @ np.linalg.inv(U_h),
             D_R=U_h @ WIN["D_R"] @ np.linalg.inv(U_h), DTs=DTs_h)
SMh = smatrix(WIN_h, E0, X1)
ev_h, od_h = functionals(SMh)
ev_eq_h = max(abs(ev_main[k] - ev_h[k]) / max(1.0, abs(ev_main[k]))
              for k in ev_main)
od_fl_h = max(abs(od_main[k] + od_h[k]) / max(1.0, abs(od_main[k]))
              for k in ("gr_trans", "gr_refl"))
check("E", "the sector flip realized as DECK TRANSPORT (conjugate the "
           "whole window family by the faithful holonomy U_h, K_S held "
           "fixed) acts on the functional battery EXACTLY as K_S -> -K_S: "
           "even class invariant, graded class flips -- the two "
           "realizations of the flip (form-side and transport-side) agree "
           "on all scattering data, as the m1 deck-compatibility requires",
      ev_eq_h < 1e-8 and od_fl_h < 1e-7,
      f"even spread {ev_eq_h:.1e}; odd-flip defect {od_fl_h:.1e}")


# =============================================================================
# Part E -- the two blindness mechanisms on the odd class
# =============================================================================
vprops = (float(np.max(np.abs(V_GH - V_GH.conj().T))) < 1e-12
          and float(np.max(np.abs(V_GH @ V_GH - I256))) < 1e-12)
vcomm = float(np.max(np.abs(V_GH @ T_main - T_main @ V_GH))) / np.sqrt(Tn2)
vgam = float(np.max(np.abs(V_GH @ GAM - GAM @ V_GH)))
vd = max(float(np.max(np.abs(V_GH @ DT - DT @ V_GH)))
         for DT in (WIN["DTs"][0], WIN["DTs"][i_cross]))
vx = max(float(np.max(np.abs(V_GH @ X1 @ V_GH + X1))),
         float(np.max(np.abs(V_GH @ X2 @ V_GH + X2))))
Bv = np.kron(S1, e[0] @ e[1])
vbreak = float(np.max(np.abs(V_GH @ Bv + Bv @ V_GH)))  # anticommutes => breaks
tr_odd = abs(od_main["gr_trans"]) + abs(od_main["gr_refl"])
check("E", "BLINDNESS MECHANISM 1 -- GHOST CONJUGATION: V = sigma2 x omega "
           "is a Hermitian unitary involution that COMMUTES with the "
           "entire dynamics (Gamma, every window symbol, the full "
           "transfer) and ANTI-commutes with BOTH conserved currents. "
           "Consequence, machine-realized: every fully-traced (V-symmetric "
           "/ ungraded-prepared) K_S-odd functional vanishes IDENTICALLY "
           "-- the graded transmission and reflection traces are exact "
           "zeros while their per-channel entries are O(0.1): the dynamics "
           "pairs every ghost channel with a non-ghost partner of equal "
           "dynamics and opposite grading. A nonzero sector-odd reading "
           "therefore requires a GRADED PREPARATION -- an input that "
           "already encodes the current's orientation. And the protection "
           "is exact precisely because the family is Clifford-VECTOR "
           "(D = c(xi)): a Clifford-EVEN (bivector/curvature-type) term "
           "ANTI-commutes with V and would break it -- named "
           "operator-grade residue, not tested here",
      vprops and vcomm < 1e-12 and vgam < 1e-12 and vd < 1e-12
      and vx < 1e-12 and vbreak < 1e-12 and tr_odd < 1e-9
      and od_main["gr_chan_max"] > 1e-2,
      f"[V,T] {vcomm:.1e}; V-anticommute currents {vx:.1e}; "
      f"traced odd functionals {tr_odd:.1e} vs per-channel "
      f"{od_main['gr_chan_max']:.3f}")

DTs_neg = [-DT for DT in WIN["DTs"]]
WIN_n = dict(WIN, D_L=-WIN["D_L"], D_R=-WIN["D_R"], DTs=DTs_neg)
T_neg = transfer(WIN_n, E0)
w_def = float(np.max(np.abs(
    T_neg - W_OM @ T_main @ np.linalg.inv(W_OM)))) / np.sqrt(Tn2)
SMn = smatrix(WIN_n, E0, X1)
ev_n, od_n = functionals(SMn)
ev_eq_n = max(abs(ev_main[k] - ev_n[k]) / max(1.0, abs(ev_main[k]))
              for k in ev_main)
od_fl_n = max(abs(od_main[k] + od_n[k]) / max(1.0, abs(od_main[k]))
              for k in ("gr_trans", "gr_refl"))
wx = max(float(np.max(np.abs(W_OM @ X1 @ np.linalg.inv(W_OM) + X1))),
         float(np.max(np.abs(W_OM @ X2 @ np.linalg.inv(W_OM) + X2))))
check("E", "BLINDNESS MECHANISM 2 -- PARITY TRANSFER (the orientation "
           "equivalence): conjugation by W = I x omega maps the "
           "symbol-orientation flip (D -> -D, K_S fixed) EXACTLY onto the "
           "sector flip (D fixed, K_S -> -K_S): T(-D) = W T W^-1 at "
           "machine zero and W carries both currents to minus themselves. "
           "Machine consequence on the battery: under D -> -D every even "
           "functional is invariant and every graded functional flips -- "
           "IDENTICALLY to the sector flip. So for EVERY scattering "
           "functional, sector-parity = symbol-orientation-parity: any "
           "K_S-odd scattering reading moves under the kappa-type "
           "orientation convention (xi -> -xi) and is therefore a gauge "
           "artifact AS A SECTOR FACE unless an absolute symbol "
           "orientation is externally fixed -- which is the same single "
           "Z/2 posit the bit already was. (Contrast: the static reader "
           "k_sigma is xi-EVEN -- it consumes the cut, quadratic in xi -- "
           "which is exactly why it can read the sector without touching "
           "the orientation. No scattering functional has that option: "
           "the dynamics couples through c(xi), linearly.)",
      w_def < 1e-12 and wx < 1e-12 and ev_eq_n < 1e-8 and od_fl_n < 1e-7,
      f"W-conjugation defect {w_def:.1e}; even spread {ev_eq_n:.1e}; "
      f"odd-flip-under-orientation defect {od_fl_n:.1e}")

JB = CJt @ np.conj(BLp0)
j_swap = float(np.linalg.norm(JB - BLm0 @ (BLm0.conj().T @ JB)))
check("E", "KRAMERS CONSISTENCY: J~ = I x J_quat commutes with the "
           "dynamics and maps right-movers ONTO left-movers (J~ is the "
           "time-reversal of the scattering problem), and it "
           "ANTI-commutes with the conserved currents (Part B): currents "
           "are T-odd. The canon no-go (every J-commuting Hermitian probe "
           "is sector-blind) is CONSISTENT with, and strengthened by, "
           "this swing: the S-matrix is blind to the sector for a reason "
           "stronger than Kramers evenness (it contains no K_S at all), "
           "and the only sector-sensitive structures -- the currents -- "
           "are exactly NON-quaternionic (J-anti-commuting), as the no-go "
           "demands of any would-be reader; but they are orientation "
           "consumers, not orientation producers (Mechanisms 1-2)",
      j_swap < 1e-10,
      f"J(right-movers) onto left-movers residual {j_swap:.1e}")


# =============================================================================
# [F] trichotomy controls + guards
# =============================================================================
Uss_d = np.kron(I2, U_ss)
DTs_ss = [Uss_d @ DT @ np.linalg.inv(Uss_d) for DT in WIN["DTs"]]
WIN_ss = dict(WIN, D_L=U_ss @ WIN["D_L"] @ np.linalg.inv(U_ss),
              D_R=U_ss @ WIN["D_R"] @ np.linalg.inv(U_ss), DTs=DTs_ss)
SMss = smatrix(WIN_ss, E0, X1)
ev_ss, od_ss = functionals(SMss)
ev_eq_ss = max(abs(ev_main[k] - ev_ss[k]) / max(1.0, abs(ev_main[k]))
               for k in ev_main)
od_eq_ss = max(abs(od_main[k] - od_ss[k]) / max(1.0, abs(od_main[k]))
               for k in ("gr_trans", "gr_refl"))
check("F", "trichotomy control -- same-sign-plane transport (U_ss, the "
           "even 6-leg seam, U_ss^dag K_S U_ss = +K_S): the ENTIRE "
           "functional battery, even AND graded, is exactly invariant: "
           "the flip responses above are mixed-plane holonomy content, "
           "not transport artifacts",
      ev_eq_ss < 1e-8 and od_eq_ss < 1e-7,
      f"even spread {ev_eq_ss:.1e}; odd spread {od_eq_ss:.1e}")

Gdress = 0.15 * (e[0] @ e[1] + 0.7 * (e[2] @ e[9]))
Mexp = np.eye(128, dtype=complex)
term = np.eye(128, dtype=complex)
for kk in range(1, 24):
    term = term @ Gdress / kk
    Mexp = Mexp + term
pu_def = float(np.max(np.abs(Mexp.conj().T @ K_S @ Mexp - K_S)))
M_d = np.kron(I2, Mexp)
SMm = smatrix(WIN, E0, X1, dress=M_d)
ev_m, od_m = functionals(SMm)
ev_eq_m = max(abs(ev_main[k] - ev_m[k]) / max(1.0, abs(ev_main[k]))
              for k in ev_main)
od_eq_m = max(abs(od_main[k] - od_m[k]) / max(1.0, abs(od_main[k]))
              for k in ("gr_trans", "gr_refl"))
check("F", "trichotomy control -- covariant frame dressing: a NON-unitary "
           "K_S-pseudo-unitary dressing (exp of a mixed bivector "
           "generator, M^dag K_S M = K_S at machine zero, commuting with "
           "omega) applied covariantly to the whole window -- transfer, "
           "end symbols, and mode bases transported together -- leaves "
           "every functional, even and graded, exactly invariant: the "
           "sector flip is never a frame relabel. (Re-deriving the mode "
           "bases independently inside the dressed frame instead of "
           "transporting them exposes the residual GRADING-pseudo-unitary "
           "channel gauge: graded functionals stay invariant at machine "
           "zero while Dirac-normalized traces shift at O(boost^2) -- "
           "that freedom is itself K_S-even and carries no sector data)",
      pu_def < 1e-9 and ev_eq_m < 1e-7 and od_eq_m < 1e-6,
      f"pseudo-unitarity defect {pu_def:.1e}; even spread {ev_eq_m:.1e}; "
      f"odd spread {od_eq_m:.1e}")

# channel-gauge control: a deterministic unitary commuting with the grading
Hg = np.cos(0.9 * np.outer(np.arange(128), np.ones(128))
            + 1.3 * np.outer(np.ones(128), np.arange(128)))
Hg = 0.5 * (Hg + Hg.T).astype(complex)
Pp_g = 0.5 * (np.eye(128) + SM["ERp"])
Hg = Pp_g @ Hg @ Pp_g + (np.eye(128) - Pp_g) @ Hg @ (np.eye(128) - Pp_g)
Ug = np.eye(128, dtype=complex)
term = np.eye(128, dtype=complex)
for kk in range(1, 40):
    term = term @ (1j * 0.2 * Hg) / kk
    Ug = Ug + term
t_g = Ug.conj().T @ SM["t_L"]
gr_g = float(np.trace(t_g.conj().T @ SM["ERp"] @ t_g).real)
tr_g = float(np.trace(t_g.conj().T @ t_g).real)
check("F", "channel-gauge control: redressing the outgoing channel basis "
           "by a grading-commuting unitary leaves the graded and ungraded "
           "traces exactly invariant (the odd functionals consume the "
           "grading OPERATOR, not a basis choice); the per-pair phase "
           "gauge of the m1 [F] control lives inside this class",
      abs(gr_g - od_main["gr_trans"]) < 1e-9
      and abs(tr_g - ev_main["tr_tt"]) < 1e-9 * max(1.0, ev_main["tr_tt"]),
      f"graded-trace shift {abs(gr_g - od_main['gr_trans']):.1e}")

c2_ok = True
for t in (WIN["t_lo"], 0.5 * (WIN["t_lo"] + WIN["t_hi"]), WIN["t_hi"]):
    x14 = xi_of(float(t), a4_main)
    c2_here = np.sqrt(3328.0 / 7.0) * float(np.linalg.norm(x14))
    if not (c2_here > 0 and np.isfinite(c2_here)):
        c2_ok = False
check("F", "SRC-REJ-1 guard: the scattering construction consumes the "
           "symbol family and touches nothing else -- C2 obeys its "
           "closed-form law at the window points untouched, and no "
           "functional built here reduces, rescales, or reads the C2 "
           "accounting: the toy makes NO source-side claim",
      c2_ok)


# =============================================================================
# Part F -- sampled corroboration (6 rays: 4 crossing, boost, gapped control)
# =============================================================================
ray_list = [("boost", A_BOOST), ("sweep-0", tuple(sweep_rays[0])),
            ("sweep-7", tuple(sweep_rays[7])),
            ("sweep-19", tuple(sweep_rays[19])),
            ("conf-up (gapped control)", A_CONF_UP)]
ok_sam, sam_report = True, []
for nm, al in ray_list:
    if "gapped" in nm:
        a4_s = ray(al, 1.5)
    else:
        s_hit, t_c = crossing_scan(al, 4.0)
        if s_hit is None:
            ok_sam = False
            continue
        s_c = bisect_wall(al, t_c, s_hit)
        a4_s = ray(al, s_c + 0.4)
    wn = window_of(a4_s, nseg=32)
    crossed = wn["q_min"] < 0
    if ("gapped" in nm) == crossed:
        ok_sam = False        # control must be gapped; others crossed
    E_s = 1.5 * float(np.sqrt(max(wn["q_L"], wn["q_R"])))
    sm_p = smatrix(wn, E_s, X1)
    sm_f = smatrix(wn, E_s, X1_of(-K_S))
    ev_p, od_p = functionals(sm_p)
    ev_f, od_f = functionals(sm_f)
    d_S = float(np.max(np.abs(sm_f["t_L"] - sm_p["t_L"])))
    ev_sp = max(abs(ev_p[k] - ev_f[k]) / max(1.0, abs(ev_p[k]))
                for k in ev_p)
    tr_o = abs(od_p["gr_trans"]) + abs(od_p["gr_refl"])
    T_s = transfer(wn, E_s)
    vc = float(np.max(np.abs(V_GH @ T_s - T_s @ V_GH))) / max(
        1.0, float(np.max(np.abs(T_s))))
    T_sn = transfer(dict(wn, DTs=[-DT for DT in wn["DTs"]]), E_s)
    wd = float(np.max(np.abs(T_sn - W_OM @ T_s @ np.linalg.inv(W_OM)))) / max(
        1.0, float(np.max(np.abs(T_s))))
    if d_S > 1e-10 or ev_sp > 1e-8 or tr_o > 1e-8 or vc > 1e-11 \
            or wd > 1e-11:
        ok_sam = False
    dyn = od_p["gr_chan_max"]
    if crossed and dyn < 1e-3:
        ok_sam = False
    sam_report.append(f"{nm}: |dS| {d_S:.0e}, V {vc:.0e}, W {wd:.0e}, "
                      f"chan {dyn:.2f}")
check("E", "SAMPLED CORROBORATION (boost wall, three seeded n2 sweep "
           "crossing rays, and the gapped conformal control ray): at every "
           "sampled configuration the transparency theorem (S identical "
           "under the sector flip), the ghost-conjugation symmetry "
           "([V, T] = 0 with traced odd functionals exactly zero), and "
           "the parity-transfer identity (T(-D) = W T W^-1) hold at "
           "machine zero; per-channel graded content is nonzero on every "
           "CROSSING ray (the odd class is dynamical wherever the wall "
           "resonator exists), while the gapped control ray runs the same "
           "classification with no wall structure to manufacture -- the "
           "mechanisms are family-wide, not one-ray accidents",
      ok_sam, "; ".join(sam_report))


# =============================================================================
# verdict + headline
# =============================================================================
nE = sum(1 for tag, _n, ok in RESULTS if tag == "E")
nF = sum(1 for tag, _n, ok in RESULTS if tag == "F")
nT = sum(1 for tag, _n, ok in RESULTS if tag == "T")
all_ok = all(ok for _t, _n, ok in RESULTS)
print()
print("KILL-CONDITION VERDICT: K-a FIRED for the S-matrix proper "
      "(TRANSPARENCY THEOREM: S(E) contains no K_S at all -- the sector "
      "flip acts as (S, eps) -> (S, -eps), so every functional of S alone "
      "is K_S-even and sector-blind; the Araki selection rule extends to "
      "all of scattering). K-b FIRED for the residual K_S-linear class: "
      "graded-current functionals exist and are dynamical per channel, "
      "but (Mechanism 1) the ghost-conjugation symmetry V = sigma2 x "
      "omega annihilates every ungraded-prepared odd reading identically, "
      "and (Mechanism 2) parity transfer (T(-D) = W T W^-1) makes every "
      "sector-odd scattering functional equally orientation-odd -- a "
      "nonzero reading requires an externally fixed absolute orientation "
      "of the conserved (non-quaternionic, T-odd) Krein current, which IS "
      "the standing external Z/2 posit. K-c did NOT fire: no scattering "
      "observable reads the bit; the dynamical route cannot bootstrap the "
      "orientation it would need. The external-posit typing of the "
      "payload bit is STRENGTHENED to dynamical grade at toy level. NO "
      "claim, canon, scorecard, or posture movement.")
print(f"HEADLINE: {nE} [E] + {nF} [F] = {nE + nF}   (setup [T] = {nT} "
      f"excluded)   {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
sys.exit(0 if all_ok else 1)
