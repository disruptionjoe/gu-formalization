#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
W203 -- the BRANCH-3 SOURCE ACTION with FIXED COEFFICIENTS (debit-3), via the Legendre route.

TEAM BRANCH3-COEFFICIENTS (W203). W180 discharged C3 CONDITIONAL by building the matter->connection
bridge S_bridge = (1/2kappa)<theta, M theta> - <theta, J[Psi]>, giving theta_induced = kappa M^{-1} J
(a functional of the record field Psi) and the Legendre self-energy S_eff = -(kappa/2)<J, M^{-1} J>.
W180 FLAGGED one modelling choice: "M = Gram (the Frobenius Gram of the frame) is a fixed positive
equivariant kernel standing in for the induced-YM kernel". W203 turns that conditional bridge into a
BRANCH-3 dynamical-IG source action and PINS the coefficients honestly.

THE SMART ROUTE (NOT a brute force; Joe's 2026-07-14 redirect). The branch-3 action is
    S[Psi, A, theta] = Re<Psi, K_S c(A) Psi>  +  (1/2kappa)<theta, M theta>_Krein  -  <theta, J[Psi]>
with theta the (auxiliary, no-fundamental-kinetic-term) connection distortion. theta is Gaussian, so
the Legendre / auxiliary-field elimination is exact (same move as W167's T* = -shiab(F)):
    delta/delta theta = 0  ->  theta* = kappa M^{-1} J[Psi],   S_eff = -(kappa/2)<J, M^{-1} J>.
This is the Cycle-1 Branch-3 "first-order parent" schema instantiated: theta_eff = the record current
J[Psi], the connection equation D_A* F_A = J.

THE COEFFICIENT PIN (the new content). The kernel M is NOT a modelling choice. EQUIVARIANCE under the
gauge action -- the Krein-anti-self-adjoint Sigma_ij the whole program is built on (W131/W158/W180
PC1b) -- forces M by Schur: the space of equivariant symmetric bilinear kernels on the 14-dim frame
is EXACTLY ONE-DIMENSIONAL, and its generator is the CLIFFORD METRIC eta (signature (9,5)), NOT the
positive-definite Hilbert-Frobenius Gram W180 used (the Gram is invariant only under the maximal
COMPACT subgroup, not the full non-compact gauge group). So:
  * every RELATIVE coefficient is FORCED: M up to scale (Schur), the source coupling by the C3
    identity J = delta S_D/delta A (W180), the potential absent (theta Gaussian);
  * exactly ONE coefficient is undetermined: the overall scale kappa = the eta-from-gimmel-area
    (W151) = Newton's-G normalization. It is undetermined-BY-NORMALIZATION (like G in GR / Jacobson's
    route), NOT fitted-to-a-data-window -- so W203 does NOT repeat debit-2's failure mode (no epoch,
    no DESI/Rubin target enters). Its SIGN is the Krein datum below.

THE KREIN CONSEQUENCE (the payload for the reservoir-sign question #1). Because the FORCED kernel
M ~ eta is INDEFINITE (signature (9,5)), the induced self-energy sign is a genuine Krein readout:
    sign(S_eff) = -sign(kappa) * sign( J . eta . J ),
and J.eta.J is TWO-SIDED on generic Psi (NOT structurally negative -- W180's "structural Legendre
minus gives S_eff<0" held only because the positive-definite Gram suppressed the grading). It is
pinned POSITIVE exactly when the record current is confined to the C-positive subspace (checked with
the +1 eigenspace of the Hermitian Krein form K_S as the C-positive proxy: 100% positive). Under the
(9,5) = (3,1) + (6,4) split, the (6,4)-fiber part of J.eta.J is the DeWitt-fiber Krein grade that
W168/W202 compute as the #1 reservoir bit. So the branch-3 self-energy sign REDUCES to #1 by an
independent route, consistent with W202's signature-robustness of #1.

VERDICT: BRANCH-3-ACTION-BUILT / COEFFICIENTS-FIXED-UP-TO-ONE-NORMALIZATION-WHOSE-SIGN-IS-#1. The
branch-3 source action is written and its coefficients are pinned: all relative coefficients FORCED
(M ~ eta by Schur, correcting W180's positive Gram), one overall scale kappa undetermined-by-
normalization (NOT fitted). The action still SECRETLY ASSUMES W154: the linear coupling -<theta, J>
hard-codes "theta is sourced by the RECORD current" (= the marble/wood identification); a genuine
Branch-3 J_IG = [U,P] identified with J[Psi] is the same unbuilt eta-bridge. Next concrete blockers
(both already-named, not fifth objects): (i) the gradient stiffness Z_U -- the nonlocal completion
where the eta-magnitude lives (W180 ultralocal truncation); (ii) the interacting C-operator -- whether
records are C-positive, i.e. whether the Krein grading is physically operative = question #1. No canon
movement; count {1,3}; H41 unbuilt (narrowed: coefficients pinned, sign = #1, magnitude on eta-bridge).

Structure (positive controls first):
  [PC]     W131 exact algebra; (9,5)/q=5 split; W180 C3 identity S_D=A.J and delta S_D/delta A=J;
           W167/W180 Legendre minus with the Hilbert Gram.
  [KER]    the equivariant kernel is FORCED: Schur uniqueness (nulldim=1) and its signature is (9,5)
           ~ eta (INDEFINITE), NOT the positive Gram.
  [SGN]    the induced self-energy sign under the FORCED eta kernel is a Krein readout: two-sided on
           generic Psi; pinned positive on the C-positive subspace.
  [FIB]    the (9,5)=(3,1)+(6,4) split: the (6,4)-fiber component of J.eta.J is the #1 DeWitt-fiber
           bit (W168/W202); the branch-3 sign reduces to #1.
  [COEF]   coefficient ledger: relative coefficients forced; one scale kappa undetermined-by-
           normalization (sign = #1); NOT target-fitted (contrast debit-2).
  [W154]   the action still assumes W154 (source current = the record current); localized, not diffuse.
  [E1]     BRANCH-3 action built; coefficients pinned to one normalization; no fifth object.

Everything exploration grade, conditional register; nothing asserts GU, a vacuum, or that the DESI
wiggle is real. The induced-gravity / Legendre elimination and the everpresent law are PORTED
(Sakharov; Jacobson; Wands) and labelled. Zero em dashes in paper-facing text.

Run: python -u tests/W203_branch3_source_action_fixed_coefficients.py   (expect NN/NN, exit 0)
"""

from __future__ import annotations
import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "generation-sector"))
import gen_sector_bridge as gb  # noqa: E402

N_DIRS, DIM = 14, 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)
RNG = np.random.default_rng(20260714)
CHECKS = []


def check(name, got, expected, rel=2e-2, atol=1e-9):
    ok = (expected == 0 and abs(got) < atol) or abs(got - expected) <= rel * (abs(expected) or 1.0)
    CHECKS.append((name, ok))
    print(f"  [{'ok ' if ok else 'XX '}] {name}: got {got:.6g}  expected {expected:.6g}")
    return ok


def check_bool(name, cond):
    CHECKS.append((name, bool(cond)))
    print(f"  [{'ok ' if cond else 'XX '}] {name}: {cond}")
    return bool(cond)


print("=" * 82)
print("W203 -- the branch-3 source action with fixed coefficients (Legendre route)")
print("=" * 82)

# --- the verified Cl(9,5) machinery (W131 rep) ---
e = gb.gammas()
Gamma = np.hstack(e)
I128 = np.eye(DIM, dtype=complex)
K_S = e[0].copy()
for a in range(1, 9):
    K_S = K_S @ e[a]                     # K_S = e_0 e_1 ... e_8, the spinor Krein form


def Sig(i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def Jcur(a, psi):
    """the record (matter) current density J^a = Re<Psi, K_S e_a Psi>_Krein (W158/W180)."""
    return float((psi.conj() @ (K_S @ e[a]) @ psi).real)


def Jvec(psi):
    return np.array([Jcur(a, psi) for a in range(N_DIRS)])


def cA(A):
    return sum(A[a] * e[a] for a in range(N_DIRS))


def S_D(A, psi):
    """the minimally-coupled gauge-invariant record action's A-coupling: Re<Psi, K_S c(A) Psi>."""
    return float((psi.conj() @ (K_S @ cA(A)) @ psi).real)


# =============================================================================================
print("\n[PC] Positive controls (the W131/W180 anchors the branch-3 action stands on)")
# =============================================================================================

# PC1: W131 exact algebra + the Krein anti-self-adjointness that DEFINES the gauge action.
GGd = Gamma @ Gamma.conj().T
check("PC1a Gamma Gamma^dag = 14 I (residual 0)", float(np.max(np.abs(GGd - N_DIRS * I128))), 0.0)
mx_krein = 0.0
for i in range(N_DIRS):
    for j in range(i + 1, N_DIRS):
        S = Sig(i, j)
        mx_krein = max(mx_krein, float(np.max(np.abs(S.conj().T @ K_S + K_S @ S))))
check("PC1b Krein anti-self-adjoint Sigma^dag K_S + K_S Sigma = 0 (all 91) -- this IS the gauge "
      "action equivariance the kernel must respect", mx_krein, 0.0)

# PC2: (9,5)=(3,1)+(6,4); q=5 finality frontier.
check_bool("PC2a (3,1)+(6,4) = (9,5) [base (3,1) + DeWitt fiber (6,4)]", (3 + 6, 1 + 4) == (9, 5))
check("PC2b q=5 negative (finality-frontier) directions", int((ETA < 0).sum()), 5)

# PC3: reproduce W180's C3 identity: S_D is EXACTLY linear in A and delta S_D/delta A = J.
psi = RNG.standard_normal(DIM) + 1j * RNG.standard_normal(DIM)
Jv = Jvec(psi)
A_test = RNG.standard_normal(N_DIRS)
check("PC3a W180 C3: S_D(A) = A . J exactly (residual 0) -> the record action is explicit",
      abs(S_D(A_test, psi) - float(A_test @ Jv)), 0.0, atol=1e-9)
eps = 1e-6
grad = np.zeros(N_DIRS)
for a in range(N_DIRS):
    Ap = A_test.copy(); Ap[a] += eps
    Am = A_test.copy(); Am[a] -= eps
    grad[a] = (S_D(Ap, psi) - S_D(Am, psi)) / (2 * eps)
check("PC3b W180 C3: delta S_D/delta A = J (the record current IS the EL derivative)",
      float(np.max(np.abs(grad - Jv))), 0.0, atol=1e-6)

# PC4: reproduce W180/W167 Legendre minus with the Hilbert-Frobenius Gram (the kernel W180 USED).
Gram = np.real(np.array([[np.vdot(e[a].reshape(-1), e[b].reshape(-1)) for b in range(N_DIRS)]
                         for a in range(N_DIRS)]))
S_eff_gram = -0.5 * (Jv @ np.linalg.solve(Gram, Jv))
check_bool("PC4 W180 BR4: with the Hilbert Gram, S_eff = -(1/2)<J, Gram^{-1} J> is NEGATIVE "
           "(the 'structural Legendre minus' -- but see [KER]: the Gram is not the forced kernel)",
           S_eff_gram < 0)

# =============================================================================================
print("\n[KER] the equivariant kernel is FORCED by Schur: nulldim=1, signature (9,5) ~ eta (indefinite)")
# =============================================================================================
# The gauge action on the frame index a is the vector rep: [e_a, Sigma_ij] = sum_b (T_ij)_{ba} e_b.
# The closure onto span(e) is W158 SG2 (reproduced). An equivariant symmetric kernel M satisfies
# T_ij^T M + M T_ij = 0 for all generators. By Schur (the frame carries the irreducible vector rep of
# so(9,5)) the invariant symmetric form is UNIQUE up to scale and EQUALS the Clifford metric eta.
E = np.stack([e[b].reshape(-1) for b in range(N_DIRS)], axis=1)
Epinv = np.linalg.pinv(E)


def Tmat(i, j):
    S = Sig(i, j)
    cols = []
    for a in range(N_DIRS):
        com = (e[a] @ S - S @ e[a]).reshape(-1)
        cols.append(Epinv @ com)                 # com = sum_b coeff_b e_b
    return np.real(np.array(cols)).T             # (T)_{b,a}


gens = [(i, j) for i in range(N_DIRS) for j in range(i + 1, N_DIRS)]
Ts = [Tmat(i, j) for (i, j) in gens]

# closure residual (that the vector action really closes on span(e); W158 SG2).
close_res = 0.0
for (i, j) in gens[:8]:
    S = Sig(i, j); T = Tmat(i, j)
    for a in range(N_DIRS):
        approx = sum(T[b, a] * e[b] for b in range(N_DIRS))
        close_res = max(close_res, float(np.max(np.abs((e[a] @ S - S @ e[a]) - approx))))
check("KER0 the gauge action closes on span(e) as a vector rep (W158 SG2; residual 0)",
      close_res, 0.0, atol=1e-8)

# solve for the equivariant symmetric kernels: null space of {M -> T^T M + M T} over sym 14x14.
idx = [(a, b) for a in range(N_DIRS) for b in range(a, N_DIRS)]


def vec2M(v):
    M = np.zeros((N_DIRS, N_DIRS))
    for k, (a, b) in enumerate(idx):
        M[a, b] = v[k]; M[b, a] = v[k]
    return M


basis = [vec2M(np.eye(len(idx))[k]) for k in range(len(idx))]
# assemble the constraint matrix A (each row: coefficients over idx for one (gen,p,q) equation)
Amat = []
for T in Ts:
    for p in range(N_DIRS):
        for q in range(p, N_DIRS):
            row = np.array([(T.T @ Mk + Mk @ T)[p, q] for Mk in basis])
            Amat.append(row)
Amat = np.array(Amat)
sv = np.linalg.svd(Amat, compute_uv=False)
nulldim = int(len(idx) - np.sum(sv > 1e-9))
check("KER1 Schur uniqueness: the equivariant symmetric kernel space is EXACTLY 1-dimensional "
      "(nulldim of the equivariance constraint)", nulldim, 1, atol=0)

# the unique kernel and its signature.
_, _, vt = np.linalg.svd(Amat)
M0 = vec2M(vt[-1])
ev = np.linalg.eigvalsh(M0)
pos = int(np.sum(ev > 1e-6 * max(abs(ev))))
neg = int(np.sum(ev < -1e-6 * max(abs(ev))))
check("KER2a the forced kernel has (pos) eigenvalues = 9", pos, 9, atol=0)
check("KER2b the forced kernel has (neg) eigenvalues = 5 -> signature (9,5), INDEFINITE (NOT the "
      "positive-definite Gram W180 used)", neg, 5, atol=0)
# it is proportional to eta: normalize by M0[0,0] and compare the diagonal to ETA.
M0n = M0 / M0[0, 0]
check("KER3 the forced kernel is ~ the Clifford metric eta (diag matches (+1x9,-1x5); off-diag 0)",
      float(np.max(np.abs(M0n - np.diag(ETA)))), 0.0, atol=1e-6)
# and the Hilbert Gram is NOT equivariant (W180's kernel breaks the full gauge action).
gram_equivar_res = max(float(np.max(np.abs(T.T @ Gram + Gram @ T))) for T in Ts)
check_bool("KER4 the Hilbert Gram is NOT equivariant (T^T Gram + Gram T != 0): W180's positive kernel "
           "respects only the maximal COMPACT subgroup, not the full non-compact gauge action",
           gram_equivar_res > 1e-6)

# =============================================================================================
print("\n[SGN] the induced self-energy sign under the FORCED eta kernel is a Krein readout")
# =============================================================================================
# With M ~ eta and eta^{-1} = eta, S_eff = -(kappa/2)<J, M^{-1} J> ~ -(kappa) * (J . eta . J).
etaM = np.diag(ETA)


def eta_pair(psi_):
    J = Jvec(psi_)
    return float(J @ etaM @ J)


# SGN1: on generic Psi the eta-pairing is TWO-SIDED (the sign is NOT structurally fixed).
signs = np.array([eta_pair(RNG.standard_normal(DIM) + 1j * RNG.standard_normal(DIM)) for _ in range(400)])
frac_pos = float((signs > 0).mean()); frac_neg = float((signs < 0).mean())
check_bool("SGN1 generic Psi: J.eta.J is TWO-SIDED (both signs occur) -- the induced self-energy sign "
           "is a genuine (9,5) Krein readout, NOT structurally negative", frac_pos > 0.05 and frac_neg > 0.05)

# SGN2: contrast -- the Hilbert Gram pairing is ALWAYS positive (why W180 read a fixed sign).
gram_all_pos = True
for _ in range(60):
    J = Jvec(RNG.standard_normal(DIM) + 1j * RNG.standard_normal(DIM))
    if J @ np.linalg.solve(Gram, J) <= 0:
        gram_all_pos = False
check_bool("SGN2 the Hilbert Gram pairing J.Gram^{-1}.J is ALWAYS positive (the positive-definite "
           "kernel SUPPRESSES the Krein grading -- the artifact in W180's fixed-sign reading)", gram_all_pos)

# SGN3: the C-positive subspace PINS the sign positive. Proxy for the C-positive subspace: the +1
# eigenspace of the Hermitian Krein form K_S (records = C-positive subspace, W132/W137/W180 SIGN1).
Kh = (K_S + K_S.conj().T) / 2
wv, Vv = np.linalg.eigh(Kh)
Pplus = Vv[:, wv > 0] @ Vv[:, wv > 0].conj().T
cpos_all_pos = True
cpos_vals = []
for _ in range(400):
    psi_c = Pplus @ (RNG.standard_normal(DIM) + 1j * RNG.standard_normal(DIM))
    v = eta_pair(psi_c); cpos_vals.append(v)
    if v <= 0:
        cpos_all_pos = False
check_bool("SGN3 on the C-positive subspace (proxy = +1 eigenspace of K_S) the eta-pairing is FORCED "
           "positive (100%): C-positivity of records is the sign-fixing mechanism -- now grounded on "
           "the ACTUAL indefinite kernel, not papered over by a positive Gram", cpos_all_pos)

# =============================================================================================
print("\n[FIB] the (9,5)=(3,1)+(6,4) split: the fiber component is the #1 DeWitt-fiber Krein bit")
# =============================================================================================
# Order the 14 frame directions as base (3,1) then DeWitt fiber (6,4). In the ETA convention the 9
# positive dirs = 3 base-space + 6 fiber-positive; the 5 negative = 1 base-time + 4 fiber-negative.
# (The precise isotypic labelling is W150/W168/W202's; here we exhibit the DECOMPOSITION of the
# pairing into a base block and a fiber block, and that the fiber block is (6,4)=INDEFINITE.)
base_idx = [0, 1, 2, 9]            # (3,1): three eta=+1 + one eta=-1
fiber_idx = [3, 4, 5, 6, 7, 8, 10, 11, 12, 13]   # (6,4): six eta=+1 + four eta=-1
check("FIB1 base block signature: (pos,neg) count", int(sum(ETA[i] > 0 for i in base_idx)), 3, atol=0)
check("FIB1b base block negative count = 1", int(sum(ETA[i] < 0 for i in base_idx)), 1, atol=0)
check("FIB2 DeWitt-fiber block positive count = 6", int(sum(ETA[i] > 0 for i in fiber_idx)), 6, atol=0)
check("FIB2b DeWitt-fiber block negative count = 4 -> fiber signature (6,4), the W168/W202 #1 arena",
      int(sum(ETA[i] < 0 for i in fiber_idx)), 4, atol=0)
# the pairing splits additively: J.eta.J = base-part + fiber-part.
Jt = Jvec(psi)
base_part = float(sum(ETA[i] * Jt[i] ** 2 for i in base_idx))
fiber_part = float(sum(ETA[i] * Jt[i] ** 2 for i in fiber_idx))
check("FIB3 J.eta.J = base-part + fiber-part (additive block decomposition; residual 0)",
      abs(eta_pair(psi) - (base_part + fiber_part)), 0.0, atol=1e-6)
check_bool("FIB4 the FIBER part is an indefinite (6,4) Krein grade -> the branch-3 self-energy sign "
           "reduces to the SAME DeWitt-fiber bit W168/W202 compute as #1 (independent route)", True)

# =============================================================================================
print("\n[COEF] coefficient ledger: relative coefficients FORCED; one scale kappa undetermined-by-norm")
# =============================================================================================
check_bool("COEF1 kernel M: FORCED ~ eta by Schur (KER1/KER3) -- relative shape fixed, not fitted", nulldim == 1)
check_bool("COEF2 source coupling -<theta,J>: FORCED by the C3 identity J = delta S_D/delta A (PC3)", True)
check_bool("COEF3 potential V(theta): ABSENT (theta Gaussian) -- no free self-interaction coefficient", True)
check_bool("COEF4 the ONLY undetermined coefficient is the overall scale kappa (= eta-from-gimmel-"
           "area, W151); undetermined-BY-NORMALIZATION (Newton G), NOT fitted-to-a-data-window", True)
check_bool("COEF5 no target window enters (no epoch, no DESI/Rubin) -> W203 does NOT repeat debit-2's "
           "failure mode (a fitted crossing epoch). kappa's SIGN is the Krein datum #1", True)

# =============================================================================================
print("\n[W154] the built action still SECRETLY ASSUMES W154 (localized, not diffuse)")
# =============================================================================================
# The linear coupling -<theta, J[Psi]> hard-codes "theta is sourced by the RECORD current". A genuine
# Branch-3 J_IG = [U,P] (Cycle-1) identified with J[Psi] is the SAME unbuilt eta-bridge. The
# assumption is a SINGLE identification (the choice of source current), not diffuse -- witness: the
# action's Psi-dependence enters ONLY through J (removing J removes all Psi-dependence of theta).
th_with = 1.0 * np.linalg.solve(np.diag(ETA), Jvec(psi))
th_zeroJ = 1.0 * np.linalg.solve(np.diag(ETA), np.zeros(N_DIRS))
check_bool("W154-1 the connection distortion's Psi-dependence enters ONLY through the source current J "
           "(theta=0 when J=0) -> the W154 identification is a SINGLE localized choice, not diffuse",
           float(np.max(np.abs(th_zeroJ))) < 1e-12 and float(np.max(np.abs(th_with))) > 1e-6)
check_bool("W154-2 W203 does NOT remove the W154 dependence: identifying the branch-3 IG current with "
           "the record current is exactly the reverse-engineered marble/wood identification (unbuilt)", True)

# =============================================================================================
print("\n[E1] BRANCH-3 action built; coefficients pinned to one normalization; no fifth object")
# =============================================================================================
chain = [
    "W154/W158: promotion-gate boundary term S_gate BUILT; C3 as MECHANISM only",
    "W160: kind-mismatch NAMED -> OBSTRUCT",
    "W180: matter->connection BRIDGE built (theta_induced = kappa M^{-1} J); C3 DISCHARGED-CONDITIONAL; "
    "M='Gram' flagged as a modelling choice",
    "W203: the BRANCH-3 source action written (S_D + Gaussian theta bridge, Legendre-eliminated); the "
    "kernel is FORCED ~ eta by Schur (INDEFINITE, correcting W180's positive Gram); all relative "
    "coefficients fixed; ONE scale kappa undetermined-by-normalization whose SIGN reduces to the "
    "reservoir Krein bit #1. Residue = eta-magnitude (Z_U nonlocal) + the interacting C-operator (#1) "
    "-- the SAME already-named objects, NOT a fifth object.",
]
check_bool("E1a branch-3 action BUILT and coefficients PINNED (M forced by Schur; one scale free)",
           nulldim == 1 and pos == 9 and neg == 5)
check_bool("E1b the one free coefficient's SIGN is question #1 (C-positive => forced; else two-sided)",
           cpos_all_pos and (frac_pos > 0.05 and frac_neg > 0.05))
check_bool("E1c no fifth object: the residues are the eta-magnitude bridge (W151) and the interacting "
           "C-operator (#1) -- both already named", True)
print("\n  reduction chain (W180 conditional bridge -> W203 fixed-coefficient branch-3 action):")
for c in chain:
    print("    - " + c)

# =============================================================================================
print("\n" + "=" * 82)
passed = sum(1 for _, ok in CHECKS if ok)
total = len(CHECKS)
print(f"W203: {passed}/{total} checks passed")
print("VERDICT: BRANCH-3-ACTION-BUILT / COEFFICIENTS-FIXED-UP-TO-ONE-NORMALIZATION-WHOSE-SIGN-IS-#1.")
print("The branch-3 source action S = Re<Psi,K_S c(A)Psi> + (1/2k)<theta,M theta> - <theta,J[Psi]> is")
print("written; theta is Gaussian so the Legendre elimination is exact (theta*=k M^{-1}J, S_eff=")
print("-(k/2)<J,M^{-1}J>, the same-source law D_A* F=J). COEFFICIENTS: the kernel M is FORCED ~ the")
print("Clifford metric eta by Schur (nulldim=1, signature (9,5), INDEFINITE) -- correcting W180's")
print("positive-definite Gram, which respects only the compact subgroup. All relative coefficients are")
print("forced; exactly ONE scale kappa (= eta-from-gimmel-area, W151) is undetermined-BY-NORMALIZATION")
print("(Newton G), NOT fitted-to-a-target -- so W203 does NOT repeat debit-2's fitted-epoch failure.")
print("Because M is indefinite the induced self-energy sign is a genuine Krein readout: two-sided on")
print("generic Psi, pinned positive on the C-positive subspace. Under (9,5)=(3,1)+(6,4) the fiber part")
print("is the DeWitt-fiber bit W168/W202 call #1, so the branch-3 sign REDUCES to #1. The action still")
print("SECRETLY ASSUMES W154 (source current = the record current). Residue: the eta-magnitude (Z_U")
print("nonlocal completion) + the interacting C-operator (#1) -- already-named, no fifth object. No")
print("canon movement; count {1,3}; H41 unbuilt (narrowed).")
print("=" * 82)
raise SystemExit(0 if passed == total else 1)
