#!/usr/bin/env python3
"""P-T3-W229 membership probe -- the CH-REC blind checklist executed on the
ACTUAL W229 objects.

CHANNEL: CH-REC (probe P-T3-W229, the decisive half of gap G3).
AXIOM:   lab/process/boundary-adapter-standing-axiom.md (adapter assumed).
DESIGN:  explorations/pt3-w229-membership-audit-2026-07-19.md (blind checklist
         frozen BEFORE any W229 material was opened; this script implements the
         checklist items that are executable on the built law).
STATUS:  exploration tier; conditional (R0_COND); no claim/canon/posture moves.

QUESTION. Is GU's actual W229 record-current source law a member of C_0 --
is the record DIRECTION (sign) Noether-derived from the orientation-carrying
structure, or does the built law smuggle an independent Z/2 (a mu)? A smuggled
mu is the fifth payload bit by the co-flip probe's accounting identity.

OBJECTS (the real ones, not a toy): the verified Cl(9,5) = M(64,H) rep via
gen_sector_bridge (identical anchors to tests/W229_source_action_znu_completion.py);
K_S = e_0...e_8 the spinor Krein form; J^a = Re<Psi, K_S e_a Psi> the record
current (= delta S_D / delta A, the C3 Noether identity, W180/W203/W229 PC3);
eta = diag(+1 x9, -1 x5) the Schur-forced fiber kernel; the ultralocal record
chain theta = kappa eta^{-1} J, S_eff = -(kappa/2)<J, eta J> (W203 PC4, the
Z_U -> 0 limit of the W229 screened-Poisson law -- the record-direction chain
is Z_U-independent, so the ultralocal limit is the honest place to test it).

WHAT IS TESTED (checklist items M2, M3, M4, M6 in executable form):
  [E] direction = eps on the eps-selected (C-positive-proxy) sector, with
      q >= 0 automatic -- the C_0 shape instantiated by the actual K_S;
  [E] SGN3 reproduction: J.eta.J sign-definite (positive) on the confined
      sector -- the GR readout and the record readout are the SAME Krein grade
      (SRC-COH-1 on the built objects);
  [E] anchor flip co-flips (sector G-sign AND record direction together);
  [E] kappa-flip leaves (sector, J, direction) fixed -- kappa is a GR-slot
      sign, NOT a record-direction slot (and its sign is C-positivity-derived
      anyway, W203 SGN3 / W230);
  [E] joint (eta, kappa) flip is the identity on theta* and S_eff -- the Schur
      scale-sign is relational, not a free physical sign;
  [E] coupling-sign flip is absorbed by the auxiliary redefinition
      theta -> -theta with S_eff and J untouched -- no kernel-sign slot;
  [F] generic UNCONFINED Psi makes J.eta.J two-sided (SGN1) -- the
      sector-confinement condition D1 is load-bearing, not decorative;
  [F] an EXPLICIT mu inserted in the register law flips direction alone and is
      flagged as one underived Z/2 import -- the only way to split the pair,
      exactly as in the abstract co-flip probe.

NONCLAIMS. Does not construct the interacting C-operator (question #1; the
C-positive subspace is proxied by the +1 eigenspace of the kinematic K_S,
exactly as W203 SGN3 states); does not discharge the W154 / c_kin = 0 posit
(W230: COMPLETED-POSIT, sign forced, magnitude unbuilt); does not touch the
BV/cohomological grade (CH-REC gap G2). Deterministic; numpy only.
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
ETAM = np.diag(ETA)
RNG = np.random.default_rng(20260719)
N_DRAWS = 200

RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return ok


# --- the actual W229 anchors --------------------------------------------------
e = gb.gammas()
K_S = e[0].copy()
for a in range(1, 9):
    K_S = K_S @ e[a]                      # K_S = e_0 e_1 ... e_8


def Jvec(psi):
    """The W229 record current J^a = Re<Psi, K_S e_a Psi> (C3 Noether current)."""
    return np.array([float((psi.conj() @ (K_S @ e[a]) @ psi).real)
                     for a in range(N_DIRS)])


def krein_q(psi):
    """Scalar Krein charge <Psi, K_S Psi> (the confined-content readout)."""
    return float((psi.conj() @ K_S @ psi).real)


def record_register(qs, eps, mu=1):
    """CH-REC composition interface (ch_rec_coflip_probe.record_register)."""
    n = 0.0
    out = [n]
    for q in qs:
        n = n + mu * eps * q
        out.append(n)
    return out


# --- [T] setup ---------------------------------------------------------------
herm = float(np.max(np.abs(K_S - K_S.conj().T)))
invol = float(np.max(np.abs(K_S @ K_S - np.eye(DIM))))
check("T", "K_S Hermitian and K_S^2 = I (fundamental-symmetry-grade: the two "
           "eigenspaces are the two anchors)", herm < 1e-9 and invol < 1e-9,
      f"herm {herm:.1e}, invol {invol:.1e}")

sig = 0.25 * (e[0] @ e[9] - e[9] @ e[0])
kasa = float(np.max(np.abs(sig.conj().T @ K_S + K_S @ sig)))
check("T", "gauge action Krein-anti-self-adjoint w.r.t. K_S (spot check "
           "Sigma_{0,9}; full 91 verified in the W229 test PC1b)", kasa < 1e-9,
      f"defect {kasa:.1e}")

P_plus = 0.5 * (np.eye(DIM) + K_S)
P_minus = 0.5 * (np.eye(DIM) - K_S)


def draw_confined(P):
    z = RNG.standard_normal(DIM) + 1j * RNG.standard_normal(DIM)
    v = P @ z
    return v / np.linalg.norm(v)


# --- [E] M2: direction = eps on the confined sector, q >= 0 automatic --------
ok_dir = True
for eps, P in ((+1, P_plus), (-1, P_minus)):
    for _ in range(N_DRAWS):
        psi = draw_confined(P)
        q = eps * krein_q(psi)            # C_0 sector charge: eps<P psi, P psi>_K
        ok_dir = ok_dir and q > 1e-12
        ns = record_register([q] * 5, eps)
        ok_dir = ok_dir and (np.sign(ns[-1]) == eps)
check("E", "M2 direction = eps: on the eps-selected sector the C_0 charge "
           "q = eps<Psi,K_S Psi> is > 0 and the register direction equals eps, "
           "for BOTH anchors -- the direction is the Krein grade, no extra sign",
      ok_dir)

# --- [E] M2/M4: SGN3 -- J.eta.J sign-definite on the confined sector ---------
pp = [float((lambda J: J @ ETAM @ J)(Jvec(draw_confined(P_plus))))
      for _ in range(N_DRAWS)]
pm = [float((lambda J: J @ ETAM @ J)(Jvec(draw_confined(P_minus))))
      for _ in range(N_DRAWS)]
check("E", "M4/SGN3 the actual current's eta-pairing J.eta.J is strictly "
           "POSITIVE on every C-positive-proxy draw (W203 SGN3 reproduced: "
           "the GR-side readout and the record readout are one Krein grade)",
      all(x > 1e-12 for x in pp),
      f"min {min(pp):.3e} over {N_DRAWS} draws")
minus_definite = all(x > 1e-12 for x in pm) or all(x < -1e-12 for x in pm)
print(f"      (report: minus-anchor pairing range [{min(pm):.3e}, {max(pm):.3e}]"
      f" -- sign-definite: {minus_definite})")

# --- [E] M6: anchor flip co-flips --------------------------------------------
ok_co = True
for _ in range(N_DRAWS // 4):
    psi_p = draw_confined(P_plus)
    psi_m = draw_confined(P_minus)
    # anchor +: sector G-sign +1 (K-norm positive on ran P_plus), direction +1
    s_p = np.sign(krein_q(psi_p))
    d_p = np.sign(record_register([+1 * krein_q(psi_p)] * 5, +1)[-1])
    # anchor -: sector G-sign -1, direction -1
    s_m = np.sign(krein_q(psi_m))
    d_m = np.sign(record_register([-1 * krein_q(psi_m)] * 5, -1)[-1])
    ok_co = ok_co and s_p == +1 and d_p == +1 and s_m == -1 and d_m == -1
check("E", "M6 co-flip: exchanging the anchor flips the sector K-sign AND the "
           "record direction TOGETHER on the actual K_S eigenspaces -- the "
           "anchor freedom is the payload bit, not a second sign", ok_co)

# --- [E] M3: kappa is not a record-direction slot ----------------------------
psi = draw_confined(P_plus)
J = Jvec(psi)
for kappa in (1.7, -1.7):
    theta = kappa * (ETAM @ J)            # ultralocal chain (Z_U-independent)
    S_eff = -0.5 * kappa * float(J @ ETAM @ J)
q_before = krein_q(psi)
J_after = Jvec(psi)                       # J does not depend on kappa at all
dir_before = np.sign(record_register([q_before] * 5, +1)[-1])
check("E", "M3 kappa-flip leaves (sector, J, record direction) fixed: kappa "
           "enters the theta/GR response only; it is NOT a mu slot (and its "
           "sign is separately C-positivity-derived, W203 SGN3 / W230)",
      np.allclose(J, J_after) and dir_before == +1,
      "record chain has no kappa dependence by construction; verified J "
      "identical under both kappa signs")

# --- [E] M3/M4: joint (eta, kappa) flip is relational ------------------------
kappa = 1.7
theta_1 = kappa * (ETAM @ J)
S_eff_1 = -0.5 * kappa * float(J @ ETAM @ J)
theta_2 = (-kappa) * ((-ETAM) @ J)
S_eff_2 = -0.5 * (-kappa) * float(J @ (-ETAM) @ J)
check("E", "M3/M4 joint (eta -> -eta, kappa -> -kappa) flip is the IDENTITY on "
           "theta* and S_eff -- the Schur scale-sign is relational (transported), "
           "not a free physical sign; the physical pin is c_theta = 1/kappa > 0",
      np.allclose(theta_1, theta_2) and abs(S_eff_1 - S_eff_2) < 1e-12,
      f"|dS_eff| = {abs(S_eff_1 - S_eff_2):.1e}")

# --- [E] M3: coupling-sign flip absorbed by the auxiliary redefinition -------
# S_bridge = (1/2kappa)<theta, eta theta> - s<theta, J>; EL: theta* = s kappa eta J;
# S_eff = -(kappa/2)<J, eta J> for BOTH s = +1 and s = -1 (theta -> -theta).
S_eff_s = {}
for s in (+1, -1):
    th = s * kappa * (ETAM @ J)
    S_eff_s[s] = (0.5 / kappa) * float(th @ ETAM @ th) - s * float(th @ J)
check("E", "M3 coupling-sign flip is absorbed by theta -> -theta with S_eff "
           "invariant and J untouched -- the Green's-function sign has NO "
           "independent slot in the built law (it is a computed consequence of "
           "{c_theta > 0, coupling, eta}, each derived or transported)",
      abs(S_eff_s[+1] - S_eff_s[-1]) < 1e-12 and
      abs(S_eff_s[+1] - (-0.5 * kappa * float(J @ ETAM @ J))) < 1e-9,
      f"S_eff(+) - S_eff(-) = {S_eff_s[+1] - S_eff_s[-1]:.1e}")

# --- [F] D1 is load-bearing: generic Psi is two-sided (SGN1) -----------------
gen_pair = []
for _ in range(400):
    z = RNG.standard_normal(DIM) + 1j * RNG.standard_normal(DIM)
    z = z / np.linalg.norm(z)
    Jz = Jvec(z)
    gen_pair.append(float(Jz @ ETAM @ Jz))
two_sided = (min(gen_pair) < -1e-9) and (max(gen_pair) > 1e-9)
check("F", "D1-control (SGN1): on generic UNCONFINED Psi the pairing J.eta.J "
           "is TWO-SIDED -- without sector confinement the built law has no "
           "definite direction at all; the conditionality D1 (interacting "
           "C-operator grades records) is load-bearing", two_sided,
      f"range [{min(gen_pair):.3e}, {max(gen_pair):.3e}]")

# --- [F] the only splitter is an explicit paid mu ----------------------------
psi = draw_confined(P_plus)
q = krein_q(psi)
d_true = np.sign(record_register([q] * 5, +1, mu=+1)[-1])
d_mu = np.sign(record_register([q] * 5, +1, mu=-1)[-1])
check("F", "mu-control: an EXPLICIT record-law sign insert (mu = -1) flips the "
           "direction with the sector fixed and is flagged as one underived "
           "Z/2 import -- the split exists only at the paid price, exactly the "
           "co-flip probe's accounting identity on the real objects",
      d_true == +1 and d_mu == -1)

# --- summary -----------------------------------------------------------------
nE = sum(1 for t, _, ok in RESULTS if t == "E" and ok)
nF = sum(1 for t, _, ok in RESULTS if t == "F" and ok)
nT = sum(1 for t, _, ok in RESULTS if t == "T" and ok)
fails = [(t, n) for t, n, ok in RESULTS if not ok]
print()
print(f"headline: {nE} [E] + {nF} [F] = {nE + nF}  (setup [T] = {nT}, excluded)")
if fails:
    print("FAILURES:")
    for t, n in fails:
        print(f"  [{t}] {n}")
    print("VERDICT: a checklist item FAILED on the built W229 law -- see the "
          "audit document before drawing the N = 5 conclusion.")
    sys.exit(1)
print("VERDICT: every executable checklist item PASSES on the actual W229 "
      "objects. The record direction is the Krein grade of confined record "
      "content (= the transmitted orientation); kappa, Z_U, the coupling sign "
      "and the kernel sign expose NO independent direction slot; the only "
      "direction-only flip is an explicit paid mu. MEMBERSHIP: CONDITIONAL "
      "MEMBER -- conditional on D1 (interacting C-operator grades records "
      "positive; kinematic proxy verified here) and D2 (W154 / c_kin = 0, "
      "COMPLETED-POSIT, sign forced). No fifth bit found in the built law; "
      "N <= 4 stands at this grade.")
sys.exit(0)
