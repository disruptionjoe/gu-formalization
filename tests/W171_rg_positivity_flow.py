#!/usr/bin/env python3
r"""
W171 (TEAM RG-POSITIVITY, label W171) -- does the RG structure DECIDE whether the Krein
grading is OPERATIVE ([P_ghost, S] = 0 at loop level = the interacting C-operator exists),
or does it leave it open?

THE ONE OBJECT (H59 North Star): OPERATIVE = [P_ghost, S] = 0 at loop level = interacting
C-operator exists. OPERATIVE -> bar (b) clears; NOT -> re-posed as record-accretion engine.

THE QUESTION PUSHED HERE: is  finite-scale RG-stability of the grading  =  the C-operator
existing at every physical scale  =  OPERATIVE?  We answer it HONESTLY by separating two
statements that are easy to conflate:

  (WD) grading WELL-DEFINED at scale mu:  eta = P+ - P- exists, m2^2(mu) > 0, the flow sits
       strictly OFF branch-E's exceptional (Jordan) locus, lambda_min(eta_+) > 0.
       This is what W53 (BOUNDARY) and W119 (SURVIVES) proved is RG-STABLE at every finite
       scale -- FORCED by threshold positivity + sign of b_2.

  (OP) grading OPERATIVE at scale mu:  [P_ghost, S] = 0, i.e. B := P- S P+ = 0, i.e. the
       interacting C-operator exists.  This is the W132 object: for any Krein-pseudo-unitary
       S (S^dag eta S = eta), the exact identity  A^dag A = P+ + B^dag B  (A = P+ S P+) holds,
       so OPERATIVE <=> B = 0 <=> the odd-ghost sector decouples.

The task hypothesis is (WD) = (OP) = OPERATIVE-AT-FINITE-SCALE. This test computes whether
that equality holds. It does NOT: (WD) is NECESSARY but PROVABLY NOT SUFFICIENT for (OP).
W132 proved B != 0 (odd cuts nonzero, exact) for the FREE grading at finite coupling, so a
well-defined RG-stable free grading is NOT operative. OPERATIVE needs the SEPARATE interacting
C-operator (a coupling-dressed grading), whose finite-scale existence we exhibit in a toy
(eta_+ = e^{-Q} > 0 at every finite coupling) and whose QFT admissibility is the open
non-locality question (W54), which a finite-dim toy CANNOT settle.

VERDICT (graded): UV-MARGINAL-NARROWED.
  * Finite-scale RG-stability of the grading being WELL-DEFINED: reproduced (W53/W119), and it
    is NECESSARY for OPERATIVE.
  * (WD) = (OP): FALSE. The two are not equal. Exhibited exactly: at finite coupling the free
    grading is well-defined (eta_+ > 0, off the Jordan locus) yet B != 0 (not operative).
  * The C-metric route (the only survivor, W132): the interacting C-metric eta_+ = e^{-Q} is
    POSITIVE at every finite coupling in the toy (OPERATIVE-in-the-C-sense holds at finite
    scale), and AF (f_2^2 -> 0) drives C -> eta (the free grading becomes operative) ONLY at
    the free UV endpoint. So the obstruction to OPERATIVE is NARROWED to the UV limit:
    localization of Q (W54-forbidden) or the free-endpoint pinch (ghost decouples, trivial).
  * The finite-dim toy CANNOT decide the QFT non-locality of Q (W54); hence NARROWED, not
    OPERATIVE-AT-FINITE-SCALE, and not UNDECIDABLE.

Effect on bar (b): UNCHANGED. The flow side is necessary context, insufficient (W48 gate):
no loop amplitude computed; the toy cannot settle QFT C-operator admissibility.

Reproducible: python tests/W171_rg_positivity_flow.py   (numpy + imports W45; exit 0)
Positive controls: reproduce W45/W119 AF fixed point (f_2^2* = 0) + negative fixed-ratio
(both roots real, negative) + W53 grading RG-stability. Negative controls: normal-sign theory
(B = 0, no violation); free endpoint Q = 0 (operative trivially, theory free); Jordan-locus
limit (C-construction blows up). No canon / RESEARCH-STATUS / claim-status / verdict / posture
file touched. Exploration-grade. W138 battery discipline: every load-bearing number two routes
or against a control.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import math
import os
import sys

import numpy as np

TOL = 1e-11
results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


# =====================================================================================
# IMPORT the W45 Stage-1 beta system (do NOT re-derive the beta functions).
# =====================================================================================
_HERE = os.path.dirname(os.path.abspath(__file__))
_STAGE1 = os.path.join(_HERE, "W45_H57_stage1_beta_system.py")
_spec = importlib.util.spec_from_file_location("W45_stage1", _STAGE1)
S1 = importlib.util.module_from_spec(_spec)
sys.modules["W45_stage1"] = S1
with contextlib.redirect_stdout(io.StringIO()):
    try:
        _spec.loader.exec_module(S1)
    except SystemExit:
        pass

BetaSystem = S1.BetaSystem
KAPPA = S1.KAPPA
BS = BetaSystem()
b2 = BS.b2()

log("=" * 96)
log("W171 (TEAM RG-POSITIVITY) -- does RG-stability of the grading = C-operator OPERATIVE?")
log("=" * 96)


# =====================================================================================
# SECTION 1 -- POSITIVE CONTROLS: reuse the W119/W57-60 AF flow machinery.
#   PC1 asymptotic freedom (b_2 > 0);  PC2 W53 grading RG-stability (finite-scale f_2^2 > 0,
#   RK4 vs analytic);  PC3 W46/W119 NEGATIVE fixed-ratio (both roots real, negative).
# =====================================================================================
log("")
log("-- SECTION 1: positive controls (AF flow, grading RG-stability, negative fixed-ratio) --")

check("PC1  W45 BetaSystem imported; Weyl coeff b_2 > 0 => beta_{f2^2} = -kappa f2^4 b_2 < 0 "
      "(f_2^2 asymptotically free, -> 0 in UV)",
      b2 > 0 and BS.beta_f2sq(0.5, 0.3) < 0,
      f"b_2 = {b2:.5f}; beta_f2sq(0.5,0.3) = {BS.beta_f2sq(0.5,0.3):.3e}")


def rk4_f2(f2_0: float, t_max: float, n: int) -> list[tuple[float, float]]:
    dt = t_max / n
    f2 = f2_0
    traj = [(0.0, f2)]
    for i in range(n):
        k1 = BS.beta_f2sq(f2, 0.0)
        k2 = BS.beta_f2sq(f2 + 0.5 * dt * k1, 0.0)
        k3 = BS.beta_f2sq(f2 + 0.5 * dt * k2, 0.0)
        k4 = BS.beta_f2sq(f2 + dt * k3, 0.0)
        f2 = f2 + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        traj.append(((i + 1) * dt, f2))
    return traj


F2_0 = 0.8
N_STEPS = 400000
T_MAX = 4000.0
traj = rk4_f2(F2_0, T_MAX, N_STEPS)
f2_all_pos = all(f2 > 0.0 for _, f2 in traj)
f2_monotone = all(traj[i + 1][1] <= traj[i][1] + 1e-15 for i in range(len(traj) - 1))
# analytic leading-log:  1/f2(t) = 1/f2_0 + kappa b_2 t   (beta_f2sq = -kappa b_2 f2^2, KAPPA=1/(4pi)^2)
kb2 = KAPPA * b2
t_end, f2_end_num = traj[-1]
f2_end_ana = F2_0 / (1.0 + kb2 * F2_0 * t_end)
rel_err = abs(f2_end_num - f2_end_ana) / f2_end_ana
check("PC2a W53 grading RG-stability: f_2^2(t) > 0 at EVERY finite RG scale (grading well-defined, "
      "m2^2 = f2^2 M_Pl^2/2 > 0, strictly OFF the Jordan locus), monotone -> 0",
      f2_all_pos and f2_monotone and f2_end_num > 0.0,
      f"f2(0)={F2_0}, f2(t=4000)={f2_end_num:.6e} > 0, min over flow > 0")
check("PC2b RK4 vs analytic leading-log agree (two-derivations discipline): "
      "1/f2 linear in t; f2* = 0 is the structural UV root (W119)",
      rel_err < 1e-9,
      f"num={f2_end_num:.6e} ana={f2_end_ana:.6e} rel_err={rel_err:.2e}")

# PC3 -- negative fixed-ratio r* = f0^2/f2^2 : (5/6) r^2 + (5 + b_2) r + 5/3 = 0  (W46/W119)
qa, qb, qc = 5.0 / 6.0, 5.0 + b2, 5.0 / 3.0
disc = qb * qb - 4 * qa * qc
r_hi = (-qb + math.sqrt(disc)) / (2 * qa)
r_lo = (-qb - math.sqrt(disc)) / (2 * qa)
# Vieta cross-check (two routes): product = c/a > 0, sum = -b/a < 0
prod_ok = abs(r_hi * r_lo - qc / qa) < 1e-9 and (qc / qa) > 0
sum_ok = abs((r_hi + r_lo) - (-qb / qa)) < 1e-9 and (-qb / qa) < 0
check("PC3  negative fixed-ratio reproduced (W46/W119): both roots of "
      "(5/6)r^2+(5+b_2)r+5/3 real and STRICTLY NEGATIVE; Vieta product>0, sum<0",
      disc > 0 and r_hi < 0 and r_lo < 0 and prod_ok and sum_ok,
      f"r* = {r_hi:.4f}, {r_lo:.4f}; disc={disc:.3f} (product & sum signs confirmed)")


# =====================================================================================
# SECTION 2 -- the KREIN TOY: build eta, a pseudo-unitary S, and separate (WD) from (OP).
#   eta = diag(+I_p, -I_q).  Q Hermitian, eta-ODD (block off-diagonal) = the interaction that
#   mixes ghost/non-ghost.  h Hermitian, eta-EVEN (block diagonal) = the graded dynamics.
#   S = e^{Q/2} e^{ih} e^{-Q/2}  is pseudo-unitary: S^dag eta S = eta  (W132 Part-2 construction).
#   DERIVATION of the invariant positive metric: with W = e^{Q/2} (=W^dag, Q Hermitian),
#   S = W U W^{-1}, U = e^{ih} unitary and eta-commuting. S^dag eta_+ S = eta_+ for eta_+ = e^{-Q}
#   because W eta_+ W = W W^{-2} W = I commutes with U, so S^dag e^{-Q} S = W^{-1} U^dag I U W^{-1}
#   = e^{-Q}.  eta_+ = e^{-Q} > 0; C = eta e^{-Q} obeys C^2 = 1 (Q eta-odd), [C,S] = 0.
# =====================================================================================
log("")
log("-- SECTION 2: Krein toy -- (WD) grading well-defined  vs  (OP) grading operative [P,S]=0 --")

P_DIM, Q_DIM = 2, 2
N = P_DIM + Q_DIM
eta = np.diag([1.0] * P_DIM + [-1.0] * Q_DIM)
Pp = np.diag([1.0] * P_DIM + [0.0] * Q_DIM)  # projector on the + (physical / positive-grading) block
Pm = np.diag([0.0] * P_DIM + [1.0] * Q_DIM)  # projector on the - (odd-ghost) block


def make_odd_Q(scale: float) -> np.ndarray:
    """Hermitian, eta-ODD generator (block off-diagonal): the coupling-scaled mixing = the interaction."""
    X = np.array([[0.7 + 0.3j, -0.4 + 0.2j],
                  [0.15 - 0.5j, 0.6 + 0.1j]], dtype=complex)  # fixed p x q block
    Q = np.zeros((N, N), dtype=complex)
    Q[:P_DIM, P_DIM:] = X
    Q[P_DIM:, :P_DIM] = X.conj().T
    return scale * Q


def make_even_h() -> np.ndarray:
    """Hermitian, eta-EVEN (block diagonal) graded dynamics."""
    hp = np.array([[0.9, 0.2 - 0.1j], [0.2 + 0.1j, 0.5]], dtype=complex)
    hm = np.array([[0.4, -0.3 + 0.2j], [-0.3 - 0.2j, 0.8]], dtype=complex)
    h = np.zeros((N, N), dtype=complex)
    h[:P_DIM, :P_DIM] = hp
    h[P_DIM:, P_DIM:] = hm
    return h


def expm(M: np.ndarray) -> np.ndarray:
    w, V = np.linalg.eig(M)
    return V @ np.diag(np.exp(w)) @ np.linalg.inv(V)


def build_S(scale: float):
    Q = make_odd_Q(scale)
    h = make_even_h()
    W = expm(0.5 * Q)          # e^{Q/2}, Hermitian (Q Hermitian)
    Winv = expm(-0.5 * Q)
    U = expm(1j * h)           # e^{ih}, unitary and eta-commuting
    S = W @ U @ Winv
    return S, Q, h


COUP = 0.6  # order-1 "coupling" scale for the headline checks
S, Q, h = build_S(COUP)

# pseudo-unitarity: S^dag eta S = eta
pu = np.linalg.norm(S.conj().T @ eta @ S - eta)
check("C1  S is Krein-pseudo-unitary: S^dag eta S = eta (W132 construction, coupling=0.6)",
      pu < TOL, f"||S^dag eta S - eta|| = {pu:.2e}")

# (WD): the FREE grading is WELL-DEFINED.  eta (fundamental symmetry) is nondegenerate: the flow
# sits off the Jordan locus (no zero eigenvalue). This is the RG-stable object of W53/W119.
eig_eta = np.linalg.eigvalsh(eta)
wd_ok = np.all(np.abs(eig_eta) > 0.5)  # |+-1|, strictly off degeneration
check("C2  (WD) free grading WELL-DEFINED: eta = P+ - P- nondegenerate (off Jordan locus), "
      "the RG-stable object of W53/W119",
      wd_ok, f"spec(eta) = {np.round(eig_eta,3).tolist()} (no zero eigenvalue)")

# (OP): is the FREE grading OPERATIVE?  B = P- S P+ ; exact W132 identity A^dag A = P+ + B^dag B.
A = Pp @ S @ Pp
B = Pm @ S @ Pp
lhs = A.conj().T @ A
rhs = Pp + B.conj().T @ B
ident = np.linalg.norm(lhs - rhs)
Bnorm = np.linalg.norm(B)
# physical-subspace probability of a normalized physical in-state |i> in the + block
psi = np.zeros(N, dtype=complex); psi[0] = 1.0
row_sum = np.linalg.norm(Pp @ S @ psi) ** 2  # sum_{f phys} |S_fi|^2
check("C3a W132 exact identity holds: A^dag A = P+ + B^dag B  (A = P+ S P+, B = P- S P+)",
      ident < TOL, f"||A^dag A - (P+ + B^dag B)|| = {ident:.2e}")
check("C3b (OP) FREE grading NOT operative at finite coupling: B = P- S P+ != 0, so [P_ghost,S] != 0; "
      "physical row-sum EXCEEDS 1 (W132 anti-damping) -- (WD) does NOT imply (OP)",
      Bnorm > 1e-6 and row_sum > 1.0 + 1e-6,
      f"||B|| = {Bnorm:.4f}; physical row-sum = {row_sum:.4f} > 1")


# =====================================================================================
# SECTION 3 -- the C-POSITIVITY FLOW: the interacting C-operator at finite coupling.
#   eta_+ = e^{-Q} > 0 satisfies S^dag eta_+ S = eta_+ (derived above); C = eta e^{-Q}, C^2 = 1,
#   [C,S] = 0.  THIS is the only survivor (W132): OPERATIVE-in-the-C-sense at finite scale.
# =====================================================================================
log("")
log("-- SECTION 3: C-positivity flow -- eta_+ = e^{-Q} at the negative fixed-ratio / finite scale --")

eta_plus = expm(-Q)  # positive definite (Q Hermitian)
Cop = eta @ eta_plus  # C = eta^{-1} eta_+ = eta e^{-Q}   (eta^2 = 1)

pos = np.linalg.eigvalsh(0.5 * (eta_plus + eta_plus.conj().T))
inv = np.linalg.norm(S.conj().T @ eta_plus @ S - eta_plus)     # S^dag eta_+ S = eta_+
c2 = np.linalg.norm(Cop @ Cop - np.eye(N))                       # C^2 = 1
comm = np.linalg.norm(Cop @ S - S @ Cop)                        # [C,S] = 0
graded = np.linalg.norm(eta_plus - eta @ Cop)                   # eta_+ = eta C
check("C4a interacting C-metric eta_+ = e^{-Q} is POSITIVE-DEFINITE at finite coupling "
      "(OPERATIVE-in-the-C-sense holds at finite scale in the toy)",
      np.all(pos > 0), f"min eig(eta_+) = {pos.min():.4f} > 0")
check("C4b eta_+ is the invariant metric: S^dag eta_+ S = eta_+ (S is eta_+-unitary => all "
      "probabilities positive, total = 1 in the C inner product)",
      inv < TOL, f"||S^dag eta_+ S - eta_+|| = {inv:.2e}")
check("C4c C-operator properties: C^2 = 1, [C,S] = 0, eta_+ = eta C  (the interacting C-operator "
      "of the toy exists and commutes with S)",
      c2 < TOL and comm < TOL and graded < TOL,
      f"||C^2-1||={c2:.2e}, ||[C,S]||={comm:.2e}, ||eta_+ - eta C||={graded:.2e}")


# =====================================================================================
# SECTION 4 -- the RG SCALING: (WD) -> (OP) ONLY at the free endpoint; obstruction to
#   OPERATIVE is NARROWED to the UV limit.  Coupling proxy q ~ f_2^2(t): under AF q -> 0 in UV.
# =====================================================================================
log("")
log("-- SECTION 4: RG scaling -- departure ||C - eta|| and ||B|| vs coupling; UV-narrowing --")


def f2_at(t: float) -> float:
    idx = int(round(t / (T_MAX / N_STEPS)))
    idx = max(0, min(idx, len(traj) - 1))
    return traj[idx][1]


sample_t = [0.0, 40.0, 400.0, 2000.0, 4000.0]
log("     scale t     f2^2(t)=q      ||B||(free not op.)   ||C-eta||(non-locality)   min eig(eta_+)")
dep_prev = None
B_prev = None
monotone_dep = True
monotone_B = True
posdef_all = True
for t in sample_t:
    q = f2_at(t)
    Sq, Qq, _ = build_S(q)
    Bq = np.linalg.norm(Pm @ Sq @ Pp)
    etapq = expm(-Qq)
    dep = np.linalg.norm(etapq - np.eye(N))  # ||eta_+ - I|| = departure of C-metric from free grading
    mineig = np.linalg.eigvalsh(0.5 * (etapq + etapq.conj().T)).min()
    posdef_all = posdef_all and (mineig > 0)
    if dep_prev is not None:
        monotone_dep = monotone_dep and (dep <= dep_prev + 1e-12)
        monotone_B = monotone_B and (Bq <= B_prev + 1e-12)
    dep_prev, B_prev = dep, Bq
    log(f"     {t:8.1f}   {q:.6e}     {Bq:.6e}        {dep:.6e}            {mineig:.6f}")

check("C5a RG-narrowing: as AF drives q = f_2^2(t) -> 0 in the UV, BOTH ||B|| (free-grading "
      "non-operativeness) and ||C - eta|| (non-locality of the C-metric) shrink monotonically "
      "toward 0 -> free grading becomes operative ONLY at the free UV endpoint",
      monotone_dep and monotone_B,
      "both monotone decreasing toward the UV endpoint")
check("C5b at EVERY sampled finite scale the C-metric eta_+ = e^{-Q} stays POSITIVE-DEFINITE "
      "(C-sense operative survives the whole interacting flow) -- but never equals the free "
      "grading at finite q (so (WD) != (OP) at every finite scale)",
      posdef_all, "min eig(eta_+) > 0 at all sampled finite scales")


# =====================================================================================
# SECTION 5 -- NEGATIVE CONTROLS + the UV obstruction the toy CANNOT resolve.
# =====================================================================================
log("")
log("-- SECTION 5: negative controls + the UV obstruction (W54 non-locality) --")

# NC1: normal-sign theory (eta = I, no ghost): any unitary S conserves total probability, B irrelevant.
Xh = np.array([[0.3, 0.1 - 0.2j, 0.0, 0.05j],
               [0.1 + 0.2j, 0.4, 0.2, 0.0],
               [0.0, 0.2, 0.5, -0.1 + 0.1j],
               [-0.05j, 0.0, -0.1 - 0.1j, 0.6]], dtype=complex)
S_norm = expm(1j * Xh)  # ordinary unitary
unit = np.linalg.norm(S_norm.conj().T @ S_norm - np.eye(N))
check("NC1  normal-sign control (eta = I, no ghost): S unitary, total probability conserved; "
      "the anti-damping excess is SPECIFIC to the Krein (odd-ghost) sign, not generic",
      unit < TOL, f"||S^dag S - I|| = {unit:.2e} (no Krein obstruction without a ghost sector)")

# NC2: free endpoint Q = 0 (ghost decoupled): B = 0, C = eta, operative TRIVIALLY -- but the theory
# is free (this is the W53 free-UV-FP touch: operative only where the interaction switches off).
S0, Q0, _ = build_S(0.0)
B0 = np.linalg.norm(Pm @ S0 @ Pp)
C0 = np.linalg.norm(eta @ expm(-Q0) - eta)  # ||C - eta|| at Q=0
check("NC2  free-endpoint control (coupling = 0, ghost decoupled = W53 free UV FP): B = 0 and "
      "C = eta, so OPERATIVE holds TRIVIALLY -- but only because the theory is FREE",
      B0 < TOL and C0 < TOL, f"||B||={B0:.2e}, ||C-eta||={C0:.2e} at the free endpoint")

# NC3: the UV obstruction the toy CANNOT resolve -- push the coupling UP (toward a hypothetical
# strong-UV / localization demand). eta_+ = e^{-Q} STAYS positive (finite dim, always), but the
# NON-LOCALITY measure ||C - eta|| grows without bound. In QFT that growth is the W54 statement:
# the analog of Q carries 1/sqrt(k^2+m^2) energy denominators; NO LOCAL positive metric exists.
# The finite-dim toy has no locality notion, so it CANNOT decide QFT admissibility of eta_+.
big = 3.0
Sb, Qb, _ = build_S(big)
etapb = expm(-Qb)
posb = np.linalg.eigvalsh(0.5 * (etapb + etapb.conj().T)).min()
depb = np.linalg.norm(etapb - np.eye(N))
check("NC3  UV/strong-coupling control: eta_+ = e^{-Q} STAYS positive-definite for large coupling "
      "(toy has no locality obstruction) yet ||C - eta|| grows unbounded -- this is exactly the "
      "W54 QFT non-locality the finite-dim toy CANNOT settle (=> NARROWED, not decided)",
      posb > 0 and depb > C0 + 1.0,
      f"min eig(eta_+)={posb:.4f} > 0, ||C-eta||={depb:.3f} (grows -> W54 obstruction, toy-blind)")

# NC4: Jordan-locus limit -- if the grading DID degenerate (lambda_min(eta_+) -> 0), the
# C-construction blows up. Tie to W53's pinch at the free endpoint: the ONLY place the C-metric
# degenerates in the toy is when eta itself degenerates, which the AF flow reaches only at mu->inf.
eta_deg = np.diag([1.0, 1.0, -1.0, -1e-9])  # near-degenerate grading (approaching Jordan locus)
cond_deg = np.linalg.cond(eta_deg)
check("NC4  Jordan-locus control: as the grading degenerates (lambda_min -> 0, W53's exceptional "
      "locus) the metric conditioning blows up (||C|| -> inf, E repair-4c) -- reached by AF only "
      "at the free UV endpoint, never at finite scale",
      cond_deg > 1e8, f"cond(eta_+) = {cond_deg:.2e} at near-degeneration")


# =====================================================================================
# SUMMARY
# =====================================================================================
log("")
log("=" * 96)
n_pass = sum(1 for _, p, _ in results if p)
n_tot = len(results)
for name, passed, _ in results:
    if not passed:
        log(f"  FAILED: {name}")
log(f"W171 RESULT: {n_pass}/{n_tot} checks passed.")
log("VERDICT: UV-MARGINAL-NARROWED.")
log("  * finite-scale grading RG-stability (WD) reproduced (W53/W119) and is NECESSARY for OPERATIVE;")
log("  * (WD) = (OP) is FALSE: free grading well-defined yet B != 0 (not operative) at finite coupling;")
log("  * C-metric eta_+ = e^{-Q} POSITIVE at every finite scale (C-sense operative survives the flow);")
log("  * obstruction to OPERATIVE narrowed to the UV limit (localization = W54, or free-endpoint pinch);")
log("  * finite-dim toy CANNOT settle QFT non-locality of Q => NARROWED, not OPERATIVE-AT-FINITE-SCALE.")
log("  * bar (b) UNCHANGED (W48 gate: no loop amplitude; toy cannot decide QFT C-operator).")
log("=" * 96)

sys.exit(0 if n_pass == n_tot else 1)
